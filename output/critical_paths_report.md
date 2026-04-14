# DMG-CPU B PPU Propagation Path Analysis

Static analysis of the DMG-CPU B gate-level netlist from
[msinger/dmg-schematics](https://github.com/msinger/dmg-schematics),
identifying deep combinatorial paths that cause propagation delays
on real Game Boy hardware.

## Source Data

This analysis uses the corrected die-traced netlists from the
dmg-schematics project, which contain fixes not present in the
original DMG-CPU-Inside schematics. Key advantages over behavioral
simulator analysis:
- Ground-truth cell types with drive strength (x1 through x6)
- Physical cell coordinates and wire routing for delay estimation
- Gate-equivalent depth counting (AND=2, MUX=3, XOR=3, etc.)
- Explicit clock/reset/enable pin classification

## Timing Reference

- Game Boy master clock: 4.194304 MHz
- T-cycle period: ~238.4 ns (one dot)
- Half T-cycle: ~119.2 ns
- Estimated gate delay (Sharp SM83 CMOS, ~5 um): 5-15 ns per gate
- Depths use gate-equivalent counting (NOT=1, AND/OR=2, MUX=3, XOR=3)

## Overview

| Category | Count | Max Depth | Worst-case Delay |
|----------|-------|-----------|-----------------|
| **Operational** (per-dot/scanline) | 1665 | 32 | 480 ns (403% half T-cycle) |
| Reset-only | 723 | 31 | 465 ns |
| **Total** | 2388 | 32 | |
