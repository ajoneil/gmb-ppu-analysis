# Game Boy (DMG-CPU B) Propagation Path Analysis

Static analysis of the DMG-CPU B gate-level netlist identifying deep
combinatorial paths that cause propagation delay on real hardware.
Data source: [msinger/dmg-schematics](https://github.com/msinger/dmg-schematics).

## Timing Reference

| Parameter | Value |
|-----------|-------|
| Master clock | 4.194304 MHz |
| T-cycle (one dot) | ~238.4 ns |
| Half T-cycle | ~119.2 ns |
| Gate delay (Sharp ~5 um CMOS) | 5-15 ns |
| Gate-equivalent counting | NOT=1, AND/OR=2, MUX=3, XOR=3, full_add=4 |

## Overview

**4102 cells** analyzed across the full DMG-CPU B chip
(974 registered,
2970 combinatorial).

| Category | Paths | Max Depth | Worst-case Delay |
|----------|-------|-----------|-----------------|
| **Operational** | 588 | 39 ge | 585 ns (491% half T-cycle) |
| Reset-only | 236 | 45 ge | 675 ns |
| **Total paths** | 824 | | |
| **Race pairs** | 991 (491 PPU) | max diff 51 | |

## Key Findings

### 1. CLKPIPE (sacu) — The Most Impactful Timing Race

`sacu` is an OR2 gate at depth **19** with fan-out **53**.
It is the pixel pipe shift clock (CLKPIPE) — the single most impactful
signal for emulator accuracy.

**What it drives:**

| Destination | Cells | Role |
|-------------|-------|------|
| Sprite Pixel Shifter | 16 | Shifts sprite pixel data out one dot at a time |
| Sprite X Match | 16 | Compares sprite X position against pixel counter |
| BG Pixel Shifter | 16 | Shifts BG/window tile data out one dot at a time |
| STAT/LY | 4 | Increments pixel X counter (PX) |
| BG/Win Cycles | 1 | Tile fetch cycle counter |

**The core problem:**

All pixel pipe data (BG tile bits, sprite tile bits, palette/priority)
is loaded into the pipe shift registers at depth 0-5. But CLKPIPE, which
triggers the shift, arrives at depth 19. On every single dot,
the pipe data is ready and waiting while the shift clock propagates through
a 19-gate chain. The pipe effectively shifts
95-285 ns after data settles.

A behavioral emulator applies the shift and data load simultaneously.
On real hardware, the data is stable before the shift happens — meaning
the previous dot's shift output is what gets captured by downstream logic
during the propagation window. This is the primary source of one-dot
horizontal pixel offset in emulators.

**CLKPIPE input tree** (`sacu` = OR2):

```
sacu [or2] — Pixel Shift Clock (CLKPIPE)
├── roxy [nor_latch] — Fine Scroll Done (depth 0, registered)
└── segu [not_x4] — CLKPIPE buffer (depth 17)
    └── tyfa [and3] — CLKPIPE gate (depth 16)
        ├── poky [nor_latch] — Pixel Pipe Done (depth 0, registered)
        ├── socy (depth 14) — through reset inverter chain
        │   └── ... xapo [Video Reset] → pyry → rydy → sylo → tomu → socy
        │   (stable during rendering — only changes on LCDC toggle/reset)
        └── vybo [nor3] (depth 14) — OPERATIONAL path, active every dot:
            ├── fepo [or2] — sprite X priority match (depth 10)
            │   └── 10 sprite X comparators (NAND5+NAND3 trees)
            ├── myvo — PPU clock phase (depth 8)
            └── wodu [and2] — H-blank gate (depth 13)
                └── pixel counter X == 160 check (NAND5)
```

During normal rendering, the reset chain (`socy`) is stable — it only
changes on system reset or LCDC bit 7 toggle. The actual per-dot delay
comes from `vybo`, which combines three signals that change every dot:
the sprite X priority match result, the PPU clock phase, and the H-blank
detection. The sprite X priority path (depth 10) is the deepest of these —
it must check all 10 stored sprite X positions against the current pixel
counter before CLKPIPE can fire.

**Races caused** (36 where CLKPIPE is the late-arriving signal):

- Sprite Pixel Shifter: 16 races
- Sprite X Match: 16 races
- STAT/LY: 4 races

### 2. Deepest Operational Path: 39 Gate-equivalents

The longest operational combinatorial chain runs from `muwy` (LY bit 0)
to `dezy` (Sprite Control), passing through
8 adder cells and 14 total combinatorial gates.
Worst-case delay: 195-585 ns
(491% of half T-cycle).

```
[dffr] muwy  — LY bit 0
  [not_x1] ebos  — Sprite Y Compare
    [full_add] eruc  — Sprite Y Compare
      [full_add] enef  — Sprite Y Compare
        [full_add] feco  — Sprite Y Compare
          [full_add] gyky  — Sprite Y Compare
            [full_add] gopu  — Sprite Y Compare
              [full_add] fuwa  — Sprite Y Compare
                [full_add] goju  — Sprite Y Compare
                  [full_add] wuhu  — Sprite Y Compare
                    [not_x1] gewy  — Sprite Y Compare
                      [nand6] wota  — Sprite Y Compare
                        [not_x1] gese  — Sprite Y Compare
                          [and3] care  — Sprite Control
                            [not_x2] dyty  — Sprite Control
                              [dffr] dezy  — Sprite Control
```

The 8-stage ripple carry adder chain dominates this path.
Each full_add costs 4 gate-equivalents, accounting for
32 of the 39 total depth.

### 3. VRAM Address Adder (32 ge)

The VRAM tile map address is computed from LY + SCY (or pixel X + SCX)
via an 8-bit ripple carry adder (8 adder stages, depth 32 ge).
The carry chain means the high address bits settle last —
the VRAM address may not be valid until 160-480 ns
after the inputs change. In practice, LY and SCY are stable for the full
scanline so the address settles well before fetch begins. But mid-scanline
SCX writes (used for split-scroll effects) may take 2+ dots to propagate.

### 4. Sprite Store Races (diff=44, all 10 stores identical)

All 10 sprite stores exhibit identical timing races. The sprite control
signal arrives at depth 44 (through the Y comparator
carry chain and sprite control logic) while OAM data arrives at depth 0.
At scanline boundaries, the stores may capture stale data instead of
clearing — causing wrong sprite position, tile, or attributes for one
dot at the start of the next scanline.

### 5. Sprite X Match (112 races, max diff=43)

The sprite X comparators check each sprite's stored X position against the
pixel counter on every dot. The comparator result depends on the pixel counter,
which is clocked by CLKPIPE (depth 19). The X match output settles
at a different time than the fetch control signals, causing sprites to
potentially trigger fetch one dot early or late.

### 6. Window Trigger Races (30 races, max diff=20)

The WX/WY comparison and window activation signals race against the rendering
pipeline. Window content may shift one pixel right. Affects games that use the
window for status bars, dialogue boxes, or HUD overlays.

## Critical Paths by Functional Area

| Area | Paths | Max Depth | Max Delay | Key Race |
|------|-------|-----------|-----------|----------|
| Sprite Control | 3 | 39 ge | 585 ns | diff=33 (17 races) |
| Bus | 326 | 32 ge | 480 ns | diff=27 (71 races) |
| Sprite X Priority | 10 | 27 ge | 405 ns | diff=23 (10 races) |
| LCD Output | 10 | 14 ge | 210 ns | diff=11 (17 races) |
| STAT/LY | 8 | 13 ge | 195 ns | diff=21 (33 races) |
| Address Bus | 15 | 9 ge | 135 ns | diff=15 (15 races) |
| Sprite Pixel Shifter | 16 | 9 ge | 135 ns | diff=19 (16 races) |
| BG/Win Cycles | 3 | 8 ge | 120 ns | diff=20 (20 races) |
| Window Logic | 1 | 7 ge | 105 ns | diff=20 (30 races) |
| APU CH3 (Wave) | 16 | 7 ge | 105 ns | diff=20 (59 races) |
| APU CH2 (Square) | 16 | 6 ge | 90 ns | diff=20 (56 races) |
| APU CH1 (Square+Sweep) | 35 | 6 ge | 90 ns | diff=51 (102 races) |
| APU Control | 1 | 5 ge | 75 ns | diff=19 (27 races) |
| Serial | 5 | 5 ge | 75 ns | diff=17 (17 races) |
| APU CH4 (Noise) | 9 | 4 ge | 60 ns | diff=20 (68 races) |
| Joypad | 12 | 3 ge | 45 ns | diff=15 (11 races) |
| VRAM Interface | 13 | 2 ge | 30 ns | diff=3 (8 races) |
| DMA | 1 | 2 ge | 30 ns | diff=20 (21 races) |
| Boot ROM | 1 | 2 ge | 30 ns | diff=13 (1 races) |
| Sprite X Match | 80 | 1 ge | 15 ns | diff=43 (112 races) |
| Timer | 1 | 1 ge | 15 ns | diff=19 (21 races) |
| OAM Interface | 6 | 1 ge | 15 ns | diff=4 (1 races) |

## High Fan-out Signals (>= 20 outputs)

These signals drive many downstream gates. High fan-out combined with deep
combinatorial depth means the signal arrives late at many destinations simultaneously.

| Signal | Description | Fan-out | Depth | Cell Type | Category |
|--------|-------------|---------|-------|-----------|----------|
| `keba` | APU Master Enable | 100 | 8 ge | not_x6 | APU Control |
| `sacu` | Pixel Shift Clock (CLKPIPE) | 53 | 19 ge | or2 | BG/Win Cycles |
| `alur` | System Clock Inv | 48 | 3 ge | not_x2 | Clock Distribution |
| `bus:d0` | CPU data bus D0 | 46 | 0 ge |  | Bus |
| `bus:d1` | CPU data bus D1 | 44 | 0 ge |  | Bus |
| `bus:d2` | CPU data bus D2 | 43 | 0 ge |  | Bus |
| `cpu` |  | 42 | 9 ge | sm83 |  |
| `bus:d6` | CPU data bus D6 | 41 | 0 ge |  | Bus |
| `bus:d7` | CPU data bus D7 | 41 | 0 ge |  | Bus |
| `bus:d4` | CPU data bus D4 | 40 | 0 ge |  | Bus |
| `bus:d3` | CPU data bus D3 | 39 | 0 ge |  | Bus |
| `bus:d5` | CPU data bus D5 | 39 | 0 ge |  | Bus |
| `bogy` | APU Clock Gate | 37 | 16 ge | not_x6 | APU Control |
| `unor` | Test Mode Gate | 34 | 3 ge | and2 | Test Mode |
| `tova` | Ext Bus Enable | 32 | 4 ge | not_x1 | Address Bus |
| `aguz` | APU Length Clock | 30 | 13 ge | not_x6 | APU Control |
| `adad` | CH1 Freq Clock | 29 | 1 ge | not_x4 | APU CH1 (Square+Sweep) |
| `cunu` | System Reset Inv | 24 | 5 ge | not_x2 | PPU Control |
| `xymu` | Rendering Active (Mode 3) | 23 | 0 ge | nor_latch | STAT/LY |
| `bus:a1` | CPU addr bus A1 | 23 | 0 ge |  | Bus |

## APU Timing

The APU has 312 timing races (max diff=51). These are primarily
in the channel frequency counters and length timers, where the CPU data bus
write path races against the channel's internal clock. APU timing races are
less audible than PPU races are visible, but may affect cycle-accurate audio
emulation — particularly for games that modify channel registers mid-note.

## Implications for Emulator Developers

### What This Analysis Shows

Behavioral emulators resolve all combinatorial logic instantaneously within a
single tick. On real hardware, signals propagate through chains of gates with
finite delay. When two signals that should be sampled simultaneously arrive at
different depths, the hardware captures a value that differs from what an
emulator computes — typically by one dot (one T-cycle).

### What to Do About It

1. **CLKPIPE races**: The pixel pipe shift clock arrives ~19 gate-equivalents
   late. Consider delaying pipe shift by one dot relative to data loading.
2. **Sprite store races**: All 10 stores have identical races. If sprite
   position is off by one dot at scanline start, this is the likely cause.
3. **Scroll adder latency**: Mid-scanline SCX writes take 2+ dots to affect
   the VRAM address. Don't apply scroll changes instantly.
4. **Window activation**: Window trigger may fire one dot late. If window
   content is shifted right by one pixel, this is the likely cause.
5. **Mode transitions**: The mode 2→3 and mode 3→0 boundaries may shift by
   one dot due to OAM scan done and tile fetch completion races.
