# GateBoy Codebase Structure

## Overview

GateBoy is a gate-level simulator of the DMG-CPU B (original Game Boy SoC), part of the [MetroBoy](https://github.com/aappleby/metroboy) project. It models the actual silicon gates derived from Furrtek's die photo tracing (DMG-CPU-Inside). The simulation is written in C++ but functions as a bespoke HDL — structs represent storage elements, inline functions represent combinatorial gates, and signal assignments model wire connections.

## Repository Layout

All gate-level simulation code lives in `metroboy/src/GateBoyLib/` (~70 files). Key files:

### PPU Core
| File | Purpose |
|------|---------|
| `GateBoyLCD.cpp/.h` | LY counter, LCD timing, line/frame end signals, LY/LYC match |
| `GateBoyPixPipe.cpp/.h` | Pixel pipelines (BG/Win, Sprite), palette lookup, window logic |
| `GateBoyTileFetcher.cpp/.h` | Background/window tile fetch state machine |
| `GateBoySpriteFetcher.cpp/.h` | Sprite tile fetch state machine |
| `GateBoySpriteScanner.cpp/.h` | OAM sprite scanning (mode 2) |
| `GateBoySpriteStore.cpp/.h` | Sprite X-position match, sprite buffer (10 sprites) |
| `GateBoyRegisters.h` | PPU register structs (LCDC, STAT, SCY, SCX, LY, LYC, BGP, OBP0/1, WY, WX) |

### System Integration (PPU-relevant)
| File | Purpose |
|------|---------|
| `GateBoyClocks.cpp/.h` | Clock phase generation (ABCDEFGH subcycles) |
| `GateBoyDMA.cpp/.h` | DMA controller (shares OAM bus with PPU) |
| `GateBoyInterrupts.cpp/.h` | STAT/VBlank interrupt generation |
| `GateBoyCpuBus.cpp/.h` | CPU address/data bus, register write detection |
| `GateBoyVramBus.h` | VRAM address/data buses |
| `GateBoyOamBus.h` | OAM control, address, dual data buses |
| `GateBoyState.h` | Master state struct containing all SoC elements |

### Key Infrastructure
| File | Purpose |
|------|---------|
| `Regs.h` | All storage element types (DFF, Latch, Bus, Gate, etc.) |
| `Gates.h` | All combinatorial gate functions |

## Type System

### Storage Elements (registered / clocked)

All derive from `BitBase` (1 byte per bit, packs state + metadata flags).

| Type | Behaviour | Silicon |
|------|-----------|---------|
| `DFF8` | 8-rung FF, no reset, rising-edge | Palette registers (BGP, OBP) |
| `DFF9` | 9-rung FF, async reset, rising-edge | Most CPU-writable registers (LYC, WY, WX, SCY, SCX) |
| `DFF11` | 11-rung FF, async reset | Background pixel temp |
| `DFF13` | 13-rung FF, async reset | Specific pinout variant |
| `DFF17` | 17-rung FF, async reset, rising-edge | Main counters (LY, LX, DIV), control FFs |
| `DFF20` | 20-rung counter FF, async load, falling-edge | TIMA, some audio |
| `DFF22` | 22-rung FF, async set/reset | Pixel pipe shift registers, serial |
| `NorLatch` | SR latch (NOR-based) | Mode latches, match latches |
| `NandLatch` | SR latch (NAND-based) | TAKA, LONY |
| `TpLatch` | Transparent latch (level-sensitive) | Data latches, address latches |
| `Bus` | Tri-state bus with collision detection | CPU/VRAM/OAM data buses |

### Combinatorial Gates

Pure functions in `Gates.h`, all take and return `wire` (alias for `const uint8_t`):

| Function | Gate | Inputs |
|----------|------|--------|
| `not1(a)` | NOT/inverter | 1 |
| `and2..7(a,b,...)` | AND | 2-7 |
| `or2..6(a,b,...)` | OR | 2-6 |
| `nor2..8(a,b,...)` | NOR | 2-8 |
| `nand2..7(a,b,...)` | NAND | 2-7 |
| `xor2(a,b)` | XOR | 2 |
| `xnor2(a,b)` | XNOR | 2 |
| `mux2p(m,a,b)` | MUX (non-inverting) | 3 |
| `mux2n(m,a,b)` | MUX (inverting) | 3 |
| `amux2..6(...)` | AND-MUX | 4-12 |
| `and_or3(a,b,c)` | (a&b)\|c | 3 |
| `or_and3(a,b,c)` | (a\|b)&c | 3 |
| `not_or_and3(a,b,c)` | ~((a\|b)&c) | 3 |
| `add3(a,b,c)` | Full adder | 3 (returns sum+carry) |
| `tri6_nn`, `tri6_pn`, `tri10_np`, `tri_pp` | Tri-state driver | 2 (returns `triwire`) |

### Signal Types
| Type | Role |
|------|------|
| `Gate` | Combinatorial output node (assigned via `<<=`) |
| `SigIn` | Signal input boundary (assigned via `.sig_in()`) |
| `SigOut` | Signal output boundary |
| `wire` | Temporary combinatorial value (`const uint8_t`) |

## Signal Naming Conventions

Signal names encode die-level cell identifiers and functional meaning:

```
MUWY_LY0p_odd
^^^^          4-char cell name (die reference)
     ^^^      functional name (LY bit 0)
        ^     polarity: p = positive, n = negative/inverted
          ^^^ clock phase: odd/evn (which subcycle it's valid)
```

Additional suffixes:
- `_D0` through `_D7` — bit index
- `_A00n` through `_A15p` — address bus bit + polarity
- `_CLK`, `_EN`, `_RST` — control signal role
- `_old`, `_new` — temporal phase (old = read-only previous state, new = being computed)

Comments reference die pages: `/*#p21.MUWY*/` = page 21, cell MUWY.

## Dependency Expression Patterns

### Pattern 1: Combinatorial wire assignment
```cpp
wire PALY_LY_MATCHa_old = not1(RAPE_LY_MATCHn_old);
```
Local `wire` variable depends on one or more other wires/register outputs.

### Pattern 2: Register update (DFF method call)
```cpp
reg_new.reg_lyc.SYRY_LYC0p.dff9(WANE_FF45_WRp_new, WESY_SYS_RSTn, reg_old.cpu_dbus.BUS_CPU_D00p.out_old());
```
Register's new state depends on clock, reset, and data inputs. These are path terminators (edges between registered nodes).

### Pattern 3: Gate assignment (combinatorial output stored in state)
```cpp
reg_new.win_ctrl.ROGE_WY_MATCHp_odd <<= not1(PAFU_WY_MATCHn_odd_new);
```
A `Gate` type in the state struct, assigned via `<<=`. Combinatorial, not clocked — just a named wire that persists in state for cross-function visibility.

### Pattern 4: Latch update
```cpp
reg_new.int_ctrl.RUPO_LYC_MATCHn.nor_latch(SET_signal, RST_signal);
```
SR latch — level-sensitive, not edge-triggered. Treated as a registered element for path analysis.

### Pattern 5: Bus tri-state write
```cpp
triwire RETU = tri6_nn(OE_signal, data_signal);
reg_new.cpu_dbus.BUS_CPU_D00p.tri_bus(RETU);
```
Two-step: create triwire from gate function, then drive onto bus.

### Pattern 6: Register output reads
```cpp
reg_old.reg_ly.MUWY_LY0p_odd.qp_old()  // Q+ of register, old phase
reg_new.reg_lcdc.WYMO_LCDC_WINENp.qp_new()  // Q+ of register, new phase
reg_old.reg_ly.MUWY_LY0p_odd.qn_old()  // Q- (inverted), old phase
```

## Temporal Programming Model

The simulation uses a two-phase update model:
1. **Read** `reg_old` (const reference to previous state)
2. **Compute** and write to `reg_new` (current state being built)
3. After all `tock_*_gates()` functions complete, `commit_regs()` atomically transitions `reg_new` → `reg_old`

Each `tock_*_gates()` function computes a subset of the state. The call order within a tick establishes implicit dependencies between functions.

## Clock Phases

The CPU runs at 4.194 MHz. Each machine cycle has 8 subcycles labeled A-H:
- Even phases: A, C, E, G (`AxCxExGx`)
- Odd phases: B, D, F, H (`xBxDxFxH`)
- Various groupings: `xxCDEFxx`, `ABxxxxGH`, etc.

Signals are annotated with their valid phases in comments (e.g., `Axxxxxxx` means valid only on phase A).

## Node Classification for Graph Analysis

For the dependency graph, nodes should be classified as:

| Classification | Types | Path Role |
|----------------|-------|-----------|
| **Registered** | DFF8, DFF9, DFF11, DFF13, DFF17, DFF20, DFF22 | Path terminator (source/sink) |
| **Latch** | NorLatch, NandLatch, TpLatch | Path terminator (treat as registered) |
| **Bus** | Bus | Path terminator (driven by tri-state, read by multiple) |
| **Combinatorial** | `wire` locals, `Gate` state members | Path interior (counts toward depth) |
| **Boundary** | SigIn, SigOut, PinIn, PinOut, PinIO | Graph boundary |
