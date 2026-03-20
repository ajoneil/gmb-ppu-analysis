# Game Boy PPU Critical Combinatorial Paths

Static analysis of the Game Boy (DMG) PPU's gate-level netlist identifying deep
combinatorial paths that may cause propagation delay on real hardware.

## Timing Reference

- Game Boy master clock: 4.194304 MHz
- T-cycle period: ~238.4 ns (one dot)
- Half T-cycle: ~119.2 ns
- Estimated gate delay (Sharp SM83 CMOS, ~5um): 5-15 ns per gate
- Paths exceeding ~8 gates may cause signals to arrive late within a half T-cycle

## Overview

| Category | Count | Max Depth | Max Delay (worst case) |
|----------|-------|-----------|----------------------|
| **Operational** (per-dot/per-scanline) | 969 | 17 | 255 ns |
| Reset-only (LCDC toggle / system reset) | 301 | 19 | 285 ns |
| **Total** | 1270 | 19 | 285 ns |

> **Reset vs Operational:** Reset paths only fire when LCDC bit 7 is toggled or
> on system reset. They pass through the VID_RST inverter chain (8 gates). While
> they are the deepest paths overall, they don't affect per-dot rendering timing.
> Operational paths fire every dot or scanline during normal rendering and are
> the ones that cause observable timing discrepancies in emulators.

## Key Findings for Emulator Developers

### The Core Problem

A behavioral emulator resolves all combinatorial logic instantaneously within a
single tick. On real hardware, signals propagate through chains of gates with
finite delay. When two signals feed into the same flip-flop but arrive at
different times, the hardware may capture a different value than an emulator
that resolves both signals simultaneously.

This analysis identifies **554** signal race points where inputs to a single
decision point differ by 3 or more gate depths. The largest differentials
exceed a full half T-cycle, meaning the late signal may not settle before
the next clock edge.

### The Two Dominant Late-Arriving Signal Classes

Almost every significant race in the PPU involves one of two late-arriving signal types:

1. **CLKPIPE (pixel pipe shift clock)** — 52 fan-out, feeds every pixel-level
   decision. Arrives through a long clock buffer chain. The pipe shift clock is
   the latest signal to settle at every pixel pipeline DFF, meaning the pipe
   effectively shifts one propagation delay after the data it's shifting is ready.
   This affects: sprite pipe timing, fine scroll match, pixel counter, window fetch.

2. **Line/fetch reset signals** (NYXU_BFETCH_RSTn, ATEJ_LINE_RST_TRIGp) —
   these pass through the VID_RST chain (8 gates from AFER+LCDC) then through
   line-end and scan-done logic. They arrive 15-17 gates after the data signals
   they reset. This affects: tile fetch counter, scan done, sprite store reset.

### What This Means in Practice

| Emulator Assumption | Hardware Reality | Affected Behavior |
|---------------------|-----------------|-------------------|
| Pixel pipe shifts when CLKPIPE fires | Pipe data is ready ~80-240ns before CLKPIPE arrives | Sprite/BG pixel positioning may be off by one dot |
| Fine scroll match resolves same dot as pixel counter | SCX fine match (depth 3) is ready long before CLKPIPE (depth 16) | Fine scroll may effectively apply one dot late |
| Tile fetch resets instantly when conditions are met | BFETCH reset (depth 17) arrives after fetch counter clock (depth 7) | Fetch state machine may run one extra cycle before reset |
| Sprite store X regs reset on line reset | Store reset (depth 17) arrives long after sprite X data (depth 1) | Sprite position capture at line boundaries may be one dot off |
| Scan done immediately stops OAM scan | Scan done signal (depth 17) races against line end (depth 0) | OAM scan may run one dot longer than expected |

### Caveats

- Gate delay estimates (5-15ns) are rough. Actual delays depend on fan-out,
  wire length, and process variation. The relative rankings are more reliable
  than the absolute nanosecond estimates.
- Not all races produce observable effects. A race only matters if the late
  signal's arrival changes the captured value — which depends on the specific
  input data at that moment.
- The parser captures ~96% of signals (121 unresolved references remain,
  mostly CPU address bus bits). Reported depths are lower bounds.
- This analysis is structural, not temporal. It identifies *where* races
  exist, not *when* they fire during a frame. Cross-referencing with specific
  test ROM failures would validate which races produce observable effects.

## Report Files

- [Operational Paths](operational_paths.md) — per-dot/per-scanline paths grouped by functional area
- [Signal Race Pairs](race_pairs_report.md) — timing races with observable effects
- [Reset Paths](reset_paths.md) — paths that only fire on system reset / LCDC toggle
- [Depth Distribution](depth_distribution.md) — histogram of path depths