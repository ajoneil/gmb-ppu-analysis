# GateBoy PPU Critical Combinatorial Paths

Static analysis of the GateBoy gate-level simulator to identify deep combinatorial
paths in the PPU that may exhibit propagation delay effects on real hardware.

## Timing Reference

- Game Boy master clock: 4.194304 MHz
- T-cycle period: ~238.4 ns (one full machine cycle = 4 T-cycles = ~953.7 ns)
- Half T-cycle: ~119.2 ns
- Estimated gate delay (Sharp SM83 CMOS process, ~5µm): **5-15 ns per gate**
- Paths exceeding ~8 gates (40-120 ns) approach the half T-cycle boundary

## Summary

| Category | Paths | Max Depth | Max Delay (worst) | Key Signals |
|----------|-------|-----------|-------------------|-------------|
| VRAM Bus | 51 | 14 | 210 ns | CPU→VRAM data transfer |
| Sprite System | 268 | 12 | 180 ns | Sprite match, SCX fine match |
| Scroll/Window | 23 | 12 | 180 ns | PAHO_X8_SYNC, fine scroll |
| Pixel Pipeline | 80 | 12 | 180 ns | Sprite pipe shift, palette |
| Pixel Counter | 100 | 12 | 180 ns | XEHO..SYBE (PX0-PX7) |
| Interrupts | 6 | 12 | 180 ns | STAT interrupt from PX match |
| Tile Fetcher | 30 | 11 | 165 ns | Window fetch trigger, BFETCH |
| OAM Bus | 86 | 11 | 165 ns | OAM write signals |
| DMA | 21 | 10 | 150 ns | DMA address registers |
| LCD/STAT Timing | 26 | 10 | 150 ns | LYC register writes, STAT |

## Analysis by Functional Area

### 1. VRAM Bus Data Path (depth 14)

The deepest PPU-relevant path is the CPU-to-VRAM data transfer:

```
[REG]  AFUR_ABCDxxxx         — Clock phase register
 [not1]  ATYP_ABCDxxxx       — Clock inversion
  [not1]  AJAX_xxxxEFGH      — Phase decode
   [or_and3] AGUT_xxCDEFGH   — Phase gating
    [nor2]  AWOD_ABxxxxxx     — Phase window
     [not1]  ABUZ_EXT_RAM_CS  — RAM chip select timing
      [nand2] TUCA_CPU_VRAM_RDp — VRAM read enable
       [not1]  TOLE_CPU_VRAM_RDp
        [and2]  SERE_CPU_VRAM_RDp — Combined VRAM read
         [and2]  SAZO_CBD_TO_VPDp — CPU-bus-to-VRAM-data enable
          [not1]  RYJE → [not1] REVO → [and2] ROCY → [not1] RAHU
           [tri10_np] TEME_CD0_TO_VD0 — Tri-state driver
            [BUS]  BUS_VRAM_D0-7p   — VRAM data bus
```

**Impact:** This path controls when CPU write data appears on the VRAM data bus. At 14 gates deep (70-210 ns), the data may not be stable on the VRAM bus before the write strobe closes. This could explain why VRAM writes during rendering have timing-sensitive effects — the data bus settling time competes with the rendering hardware's VRAM reads.

### 2. Pixel Pipe Clock & Fine Scroll (depth 12)

The pixel pipe shift clock (`CLKPIPE`) has a 12-gate path:

```
[REG]  ARYS_xBxDxFxH        — Clock source (registered)
  [nand2] AVET_AxCxExGx     — Phase gen
   [not1] ATAL → [not1] AZOF → [not1] ZAXY → [not1] ZEME → [not1] ALET
    — 5 inverter chain for clock buffering
     [not1] MYVO_AxCxExGx
      [nor3] VYBO_CLKPIPE    — Pipe clock gate (rendering + fetch state)
       [and3] TYFA_CLKPIPE   — Combined clock enable
        [not1] SEGU_CLKPIPE  — Pixel pipe shift clock
         [not1] ROXO_CLKPIPE — Inverted pipe clock
```

**Key sinks from CLKPIPE:**
- `PUXA_SCX_FINE_MATCH` (depth 12) — SCX fine scroll match detection
- `PAHO_X8_SYNC` (depth 12) — Pixel X=8 sync (left margin end)
- `XEHO_PX0p` through `SYBE_PX7p` (depth 12) — Pixel counter bits
- `NURO_SPR_PIPE_A0` etc. (depth 12) — Sprite pipe shift register
- `RYFA_WIN_FETCHn_A` (depth 11) — Window fetch trigger

**Impact:** The pixel pipe clock is the beating heart of the PPU's rendering phase. Every pixel's output timing depends on this 12-gate chain settling. A 60-180 ns delay here directly affects:
- When fine scroll comparison triggers (SCX low 3 bits)
- When the pixel counter crosses X=8 (left margin/window)
- When sprite pipe pixels shift out
- When window fetching begins

This is a prime candidate for one-dot timing discrepancies. In a behavioral emulator, CLKPIPE fires instantly, but on real hardware the 5-inverter clock buffer chain alone adds 25-75 ns of delay before the pipe clock is even generated.

### 3. Sprite X-Position Match (depth 12)

The sprite match system has depth-12 paths involving the pixel counter:

```
[CLKPIPE chain, depth 10] → XEHO_PX0p → ... → sprite X comparator
```

The pixel counter feeds into sprite X-position comparators (10 sprites × 8 bits each). The full path from clock register to sprite match decision is 12 gates deep. This means:
- Sprite match signals arrive late relative to the pixel pipe clock
- The "one-dot" offset for sprite rendering start could be partially explained by this propagation delay
- Different sprites at different X positions have the same depth (the comparator is parallel), but the match-priority encoder adds further depth

### 4. STAT Interrupt from Pixel Match (depth 12)

```
XEHO_PX0p → [mode transition logic] → LALU_FF0F_D1p (STAT interrupt)
```

The STAT interrupt for H-blank is generated from mode transition logic that depends on the pixel counter (which depends on CLKPIPE). At depth 12, the interrupt request arrives ~60-180 ns after the clock edge, which can shift the apparent timing of STAT interrupt relative to other events by one or more dots.

### 5. Window Fetch Trigger (depth 11)

```
[CLKPIPE chain] → RYFA_WIN_FETCHn_A
```

Window fetch start depends on CLKPIPE and the window position comparator. At depth 11 (55-165 ns), the window fetch trigger arrives after the pixel pipe has already shifted — the window's first pixel may appear one dot later than expected.

### 6. LCD/STAT Register Writes (depth 10)

CPU writes to LYC, SCX, SCY, and other PPU registers go through a 10-gate path from clock phase registers:

```
ADYK_xxxDEFGx → [clock decode] → [CPU write enable] → [register DFF]
```

The 10-gate depth (50-150 ns) means register write values settle late within the T-cycle. This can cause race conditions where a write to SCX during rendering might not take effect until the next dot.

## Paths of Special Interest for Emulator Timing

### The "One Dot" Candidates

These paths are most likely to cause signals to arrive one dot (one T-cycle = ~238 ns) late:

1. **CLKPIPE → Pixel Counter → Sprite Match** (depth 12, 60-180 ns)
   - If the worst-case delay exceeds half a T-cycle, the sprite match signal doesn't settle before the next clock edge, effectively delaying it by one dot.

2. **CLKPIPE → SCX Fine Match** (depth 12, 60-180 ns)
   - Fine scroll comparison result arrives late, potentially shifting the visible start of background tiles.

3. **CLKPIPE → Window Fetch Trigger** (depth 11, 55-165 ns)
   - Window appearance may be delayed by one dot due to late trigger.

4. **Clock → VRAM Bus Data** (depth 14, 70-210 ns)
   - CPU VRAM writes during rendering may not be visible to the PPU until one dot later.

### The Inverter Chain Tax

A significant portion of every deep path is clock buffering inverter chains (5-8 gates of just `not1 → not1 → not1`). In real silicon, these are deliberate clock tree buffers — they're there to drive the high fan-out clock signals. The delay they add is a real physical effect but it's a constant offset, not signal-dependent. A behavioral emulator could model this as a fixed clock skew rather than per-signal delay.

## Caveats

1. **Gate delay estimates are rough.** The 5-15 ns range assumes basic CMOS gates in Sharp's ~5µm process. Actual delays depend on fan-out, wire length, and VCC.

2. **Not all gates are equal.** NOR/NAND gates with 4+ inputs are slower than inverters. Our depth count treats all gates equally — a weighted model would give more accurate relative rankings.

3. **The parser captures ~85% of signals.** Some computed methods on state structs (e.g., `XAPO_VID_RSTn_new()`) are resolved but not all cross-function references are fully traced. The reported depths are lower bounds.

4. **Feedback loops were broken.** 62 edges were removed to create the DAG. These represent async set/reset paths through DFFs — real hardware feedback that we linearize for analysis. The removed edges are mostly in interrupt logic and bus arbitration.

5. **Temporal boundaries are respected.** Reads from `reg_old` (previous tick) are treated as registered boundaries. This is correct for synchronous paths but may undercount delays in asynchronous control paths.
