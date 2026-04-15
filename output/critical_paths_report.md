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
| Gate delay (Sharp ~5 µm CMOS) | 5-15 ns per effective ge |
| Delay model | Elmore RC (per-instance wire length + gate topology) |
| Effective ge unit | NOT_x1 at median wire length = 1.0 ge |

## Overview

**4102 cells** analyzed across the full DMG-CPU B chip
(974 registered,
2968 combinatorial).

| Category | Paths | Max Depth | Worst-case Delay |
|----------|-------|-----------|-----------------|
| **Operational** | 1076 | 103.1 ge | 1546 ns (1297% half T-cycle) |
| Reset-only | 33 | 101.6 ge | 1524 ns |
| **Total paths** | 1109 | | |
| **Race pairs** | 1063 (510 PPU) | max diff 98.77 ge | |

## Key Findings

### 1. CLKPIPE (sacu) — The Most Impactful Timing Race

`sacu` is an OR2 gate at effective depth 63.8 ge
(319-957 ns, fan-out **53**).
It is the pixel pipe shift clock (CLKPIPE) — the single most impactful
signal for emulator accuracy. The static depth includes the reset inverter
chain which only changes on LCDC toggle or system reset.

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
is loaded into the pipe shift registers at low depth. But CLKPIPE, which
triggers the shift, must wait for the sprite X priority check,
the H-blank detection, and the PPU clock phase before it can fire.
At depth 63.8 ge (319-957 ns),
the pipe data is ready and waiting.

A behavioral emulator applies the shift and data load simultaneously.
On real hardware, the data is stable before the shift happens — meaning
the previous dot's shift output is what gets captured by downstream logic
during the propagation window. This is the primary source of one-dot
horizontal pixel offset in emulators.

**CLKPIPE input tree** (`sacu` = OR2):

```
sacu [or2] — Pixel Shift Clock (CLKPIPE) (depth 63.8)
├── roxy [nor_latch] — Fine Scroll Done (depth 0, registered)
└── segu [not_x4] — CLKPIPE buffer (depth 49.4)
    └── tyfa [and3] — CLKPIPE gate (depth 48.5)
        ├── poky [nor_latch] — Pixel Pipe Done (depth 0, registered)
        ├── socy (depth 41.2) — through reset inverter chain
        │   └── ... xapo [Video Reset] → pyry → rydy → sylo → tomu → socy
        │   (stable during rendering — only changes on LCDC toggle/reset)
        └── vybo [nor3] (depth 46.9) — OPERATIONAL path, active every dot:
            ├── fepo [or2] — sprite X priority match (depth 41.9)
            │   └── 10 sprite X comparators (NAND5+NAND3 trees)
            ├── myvo — PPU clock phase (depth 22.2)
            └── wodu [and2] — H-blank gate (depth 45.5)
                └── pixel counter X == 160 check (NAND5)
```

During normal rendering, the reset chain (`socy`) is stable — it only
changes on system reset or LCDC bit 7 toggle. The actual per-dot delay
comes from `vybo`, which combines three signals that change every dot:
the sprite X priority match result, the PPU clock phase, and the H-blank
detection.

**Races caused** (32 where CLKPIPE is the late-arriving signal):

- Sprite Pixel Shifter: 16 races
- Sprite X Match: 16 races

> **Emulator guidance:** Consider delaying the pixel pipe shift by one dot
> relative to data loading. If BG or sprite pixels appear one dot to the
> right of their expected position, CLKPIPE latency is the likely cause.

### 2. Deepest Operational Path: 103.1 Effective Gate-equivalents

The longest operational combinatorial chain runs from `bus:a10` (CPU addr bus A10)
to `bus:d0` (CPU data bus D0), passing through
0 adder cells and 9 total combinatorial gates.
Worst-case delay: 515-1546 ns
(1297% of half T-cycle).

This path fires once per scanline (when LY increments), not per dot.
It computes which sprites are on the current line via the Y comparator
carry chain and feeds the result into the sprite store control logic.

```
[] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control
                  [not_if0] buzu  — APU Control
                    [] bus:d0  — CPU data bus D0
```

### 3. VRAM Address Adder (66.2 ge)

The VRAM tile map address is computed from LY + SCY (or pixel X + SCX)
via an 8-bit ripple carry adder (8 adder stages, depth 66.2 ge).
The carry chain means the high address bits settle last —
the VRAM address may not be valid until 331-994 ns
after the inputs change. In practice, LY and SCY are stable for the full
scanline so the address settles well before fetch begins. But mid-scanline
SCX writes (used for split-scroll effects) may take 2+ dots to propagate.

> **Emulator guidance:** Don't apply mid-scanline SCX writes instantly.
> The VRAM address takes 331-994 ns to settle,
> so the new scroll value won't affect tile fetch for 2+ dots.

### 4. Sprite Store Races (diff=71.2 ge, all 10 stores identical)

All 10 sprite stores exhibit identical timing races. The store write-enable
signal (`ebeb` (Sprite Control), depth 71.2 ge)
propagates through the sprite Y comparator carry chain and sprite control
decode logic before reaching the store latches, while OAM data arrives
at the data pin at depth 0 (direct from the OAM bus).

At scanline boundaries when the stores are being loaded during OAM scan,
the write-enable arrives 356-1068 ns
after the data. During this window the latch may capture data from the
wrong OAM entry — the previous sprite's data instead of the current one.

> **Emulator guidance:** If sprites show wrong position or attributes for
> one dot at the start of a scanline, this race is the cause. The stores
> hold stale data for one dot while the control signal propagates.

### 5. Sprite X Match (112 races, max diff=75.5 ge)

The sprite X comparators check each sprite's stored X position against the
pixel counter on every dot. The comparator result depends on the pixel counter,
which is clocked by CLKPIPE (depth 63.8 ge). The X match output settles
at a different time than the fetch control signals, causing sprites to
potentially trigger fetch one dot early or late.

> **Emulator guidance:** Sprite fetch may trigger one dot early or late
> relative to the pixel counter. If sprites appear shifted horizontally
> by one pixel, the X match race with CLKPIPE is the likely cause.

### 6. Window Trigger Races (31 races, max diff=59.9 ge)

The WX/WY comparison and window activation signals race against the rendering
pipeline. Window content may shift one pixel right. Affects games that use the
window for status bars, dialogue boxes, or HUD overlays.

> **Emulator guidance:** If window content is shifted one pixel to the
> right, the window trigger race is the likely cause. The window
> activation may need to be delayed by one dot.

## Critical Paths by Functional Area

| Area | Paths | Max Depth | Max Delay | Key Race |
|------|-------|-----------|-----------|----------|
| Bus | 689 | 103.1 ge | 1546 ns | diff=103.1 (79 races) |
| LCD Output | 10 | 71.2 ge | 1069 ns | diff=47.4 (18 races) |
| Timer | 17 | 71.0 ge | 1064 ns | diff=72.1 (21 races) |
| APU CH4 (Noise) | 17 | 66.2 ge | 992 ns | diff=83.2 (71 races) |
| Data Bus | 24 | 64.5 ge | 967 ns | diff=38.0 (16 races) |
| APU CH2 (Square) | 23 | 60.7 ge | 910 ns | diff=73.6 (60 races) |
| APU CH1 (Square+Sweep) | 42 | 59.6 ge | 894 ns | diff=113.5 (106 races) |
| DMA | 2 | 57.6 ge | 864 ns | diff=65.5 (22 races) |
| VRAM Interface | 37 | 56.3 ge | 845 ns | diff=7.5 (7 races) |
| Address Bus | 32 | 55.8 ge | 837 ns | diff=33.0 (26 races) |
| APU CH3 (Wave) | 28 | 55.3 ge | 829 ns | diff=72.8 (64 races) |
| Sprite Control | 3 | 54.4 ge | 815 ns | diff=81.5 (17 races) |
| Sprite X Priority | 10 | 52.4 ge | 787 ns | diff=48.7 (10 races) |
| Test Mode | 5 | 45.9 ge | 688 ns | diff=70.1 (8 races) |
| STAT/LY | 8 | 45.5 ge | 683 ns | diff=64.7 (32 races) |
| Sprite Pixel Shifter | 16 | 36.4 ge | 545 ns | diff=63.8 (32 races) |
| Joypad | 12 | 35.3 ge | 530 ns | diff=70.1 (15 races) |
| Serial | 6 | 32.2 ge | 484 ns | diff=73.0 (18 races) |
| APU Control | 1 | 16.7 ge | 250 ns | diff=71.2 (31 races) |
| Sprite X Match | 80 | 14.1 ge | 211 ns | diff=75.5 (112 races) |
| Other | 1 | 14.1 ge | 211 ns | diff=89.2 (6 races) |
| OAM Interface | 7 | 14.1 ge | 211 ns | diff=10.1 (3 races) |
| BG/Win Cycles | 3 | 9.4 ge | 141 ns | diff=92.9 (20 races) |
| Clock Distribution | 1 | 7.8 ge | 118 ns | diff=87.8 (21 races) |
| Window Logic | 1 | 6.7 ge | 100 ns | diff=59.9 (31 races) |
| Boot ROM | 1 | 1.8 ge | 27 ns | diff=40.3 (1 races) |

## High Fan-out Signals (>= 20 outputs)

These signals drive many downstream gates. High fan-out combined with deep
combinatorial depth means the signal arrives late at many destinations simultaneously.

| Signal | Description | Fan-out | Depth | Cell Type | Category |
|--------|-------------|---------|-------|-----------|----------|
| `keba` | APU Master Enable | 100 | 21.240000000000002 ge | not_x6 | APU Control |
| `sacu` | Pixel Shift Clock (CLKPIPE) | 53 | 63.769999999999996 ge | or2 | BG/Win Cycles |
| `alur` | System Clock Inv | 48 | 8.64 ge | not_x2 | Clock Distribution |
| `bus:d0` | CPU data bus D0 | 46 | 0.0 ge |  | Bus |
| `bus:d1` | CPU data bus D1 | 44 | 0.0 ge |  | Bus |
| `bus:d2` | CPU data bus D2 | 43 | 0.0 ge |  | Bus |
| `cpu` |  | 42 | 0.0 ge | sm83 |  |
| `bus:d6` | CPU data bus D6 | 41 | 0.0 ge |  | Bus |
| `bus:d7` | CPU data bus D7 | 41 | 0.0 ge |  | Bus |
| `bus:d4` | CPU data bus D4 | 40 | 0.0 ge |  | Bus |
| `bus:d3` | CPU data bus D3 | 39 | 0.0 ge |  | Bus |
| `bus:d5` | CPU data bus D5 | 39 | 0.0 ge |  | Bus |
| `bogy` | APU Clock Gate | 37 | 26.93 ge | not_x6 | APU Control |
| `unor` | Test Mode Gate | 34 | 15.61 ge | and2 | Test Mode |
| `tova` | Ext Bus Enable | 32 | 29.7 ge | not_x1 | Address Bus |
| `aguz` | APU Length Clock | 30 | 26.58 ge | not_x6 | APU Control |
| `adad` | CH1 Freq Clock | 29 | 4.07 ge | not_x4 | APU CH1 (Square+Sweep) |
| `cunu` | System Reset Inv | 24 | 16.5 ge | not_x2 | PPU Control |
| `xymu` | Rendering Active (Mode 3) | 23 | 0.0 ge | nor_latch | STAT/LY |
| `bus:a1` | CPU addr bus A1 | 23 | 0.0 ge |  | Bus |

## APU Timing

The APU has 332 timing races (max diff=113.52). These are primarily
in the channel frequency counters and length timers, where the CPU data bus
write path races against the channel's internal clock. APU timing races are
less audible than PPU races are visible, but may affect cycle-accurate audio
emulation — particularly for games that modify channel registers mid-note.
