# Game Boy Propagation Delay Analysis

Static analysis of the Game Boy's DMG-CPU B gate-level netlist to identify deep combinatorial paths that cause propagation delay on real hardware. The analysis covers the entire chip — PPU, APU, CPU bus interface, timer, serial, DMA, interrupts, and clock distribution. The data is derived from [msinger's dmg-schematics](https://github.com/msinger/dmg-schematics), which contains corrected reverse-engineered schematics and parsable netlists of the DMG-CPU B chip, traced from die photography.

## Motivation

Behavioral Game Boy emulators resolve all combinatorial logic instantaneously within a single tick. On real DMG silicon, signals propagate through chains of gates with finite delay. When a signal chain is deep enough, the total delay can consume a significant fraction of a T-cycle (~238 ns at 4.194 MHz), causing the hardware to capture different values than an emulator expects.

This project extracts the chip's netlist as a dependency graph, computes per-instance propagation delays using an Elmore RC model (with wire lengths and transistor sizing from [msinger/dmg-sim](https://github.com/msinger/dmg-sim)), and identifies which signal races actually matter for emulator accuracy by classifying each race by its effective timing domain.

## Key Results

- **4,102 nodes** (974 registered, 2,968 combinatorial, 83 bus, 70 I/O pad, 7 boundary) and **9,458 edges** extracted
- **1,063 signal race pairs** where inputs to a register arrive at significantly different depths
- Races classified by effective timing domain (based on how often the critical path's source register changes):
  - **13 truly per-dot** — critical path fed by registers that change every pixel (fetch state, FIFO shift). These are the races that directly affect emulator pixel accuracy.
  - **224 per-line** — critical path fed by registers that change once per scanline (LY counter, mode transitions). Races fire at line boundaries only.
  - **473 per-frame** — bus transfers, APU. Plenty of slack.
  - **353 static** — critical path through reset/LCDC logic. Never races during rendering.

The most timing-critical signals (truly per-dot, tightest deadline):
1. **BG fetch cycle races** (ppu-cycles) — max diff 22.2 effective ge, deadline 238 ns
2. **BG FIFO shift races** (ppu-bgfifo) — max diff 16.2 effective ge, deadline 238 ns
3. **SACU / CLKPIPE** (pixel pipe shift clock) — fan-out 53, depth 63.8 ge, but critical path is through static reset chain (effectively settled before rendering begins)

See [`output/critical_paths_report.md`](output/critical_paths_report.md) for the full findings.

## Project Structure

```
parse_schematics.py           # Netlist parser & graph builder
build_explorer.py             # Builds interactive HTML explorer
dmg-schematics/               # Die-traced netlists (git submodule)
docs/
  index.html                  # Interactive explorer (GitHub Pages)
output/
  critical_paths_report.md    # Overview & key findings (start here)
  operational_paths.md        # Operational paths by functional area
  race_pairs_report.md        # Signal race pairs with observable effects
  reset_paths.md              # Reset-only paths (LCDC toggle / sys reset)
  signal_concordance.md       # Signal name ↔ Pan Docs register mapping
  ppu_graph.json              # Full dependency graph (nodes + edges)
  critical_paths.json         # All ranked critical paths
  race_pairs.json             # Signal race pair detection results
```

## Interactive Explorer

Browse the analysis interactively at **[ajoneil.github.io/gmb-ppu-analysis](https://ajoneil.github.io/gmb-ppu-analysis/)**.

Features:
- **Race Pairs** — sortable/filterable table with timing domain classification, expandable detail panels showing observable effects
- **Critical Paths** — browse all paths by category, depth; click to see full gate chain with per-instance Elmore delays and drive strength annotations
- **Search** — find any signal by die name or Pan Docs register name (LCDC, SCX, LY, etc.)
- **Graph Explorer** — click any signal to see its inputs, outputs, category, drive strength, and all paths flowing through it
- **External links** — each signal links to the [die photo viewer](https://iceboy.a-singer.de/dmg_cpu_b_map/), [netlist](https://iceboy.a-singer.de/doc/dmg_cpu_b_netlist.html), [cell type docs](https://iceboy.a-singer.de/doc/dmg_cells.html), and [Pan Docs](https://gbdev.io/pandocs/)

## Usage

```bash
git clone <this-repo>
cd gmb-ppu-analysis
git submodule update --init

# Set up environment
python -m venv .venv
source .venv/bin/activate
pip install networkx

# Run analysis (reads from dmg-schematics/netlist/)
python parse_schematics.py

# Build interactive explorer (writes docs/index.html)
python build_explorer.py
```

Outputs are written to `output/` and `docs/`.

## How It Works

The parser reads the machine-readable netlists from `dmg-schematics/netlist/` to build a directed graph where:

- **Nodes** are cell instances — flip-flops, latches, combinatorial gates, tri-state buffers, bus nodes, and I/O pads
- **Edges** represent signal connections with explicit types (data, clock, reset) derived from destination pin names
- Each node carries its exact cell type, drive strength, physical coordinates, and functional category annotation from the schematic authors

**Delay model:** Per-instance propagation delays are computed using an Elmore RC model matching [msinger/dmg-sim](https://github.com/msinger/dmg-sim)'s `timing-default.sv`. Each gate's delay accounts for its transistor sizing (NMOS/PMOS stack depth, driver width) and physical wire length from the layout. Delays are normalized to "effective gate equivalents" where 1.0 ge = one minimum inverter at median wire length, preserving compatibility with a 5–15 ns per ge estimation range for Sharp's ~5 µm CMOS process.

**Slack-aware ranking:** Race pairs are classified by *effective* timing domain — not just how often the destination register samples, but how often the source register on the critical path actually changes. A path through the reset chain has effectively infinite slack even if the destination samples every dot, because the reset signal is static during rendering.

## Data Source

This analysis uses the netlists from [msinger/dmg-schematics](https://github.com/msinger/dmg-schematics), which contain corrections not present in the original [DMG-CPU-Inside](https://github.com/furrtek/DMG-CPU-Inside) schematics. Key advantages of this data source:

- Ground-truth cell types with drive strength variants (not_x1 through not_x6)
- Physical cell coordinates and wire routing paths for layout-aware delay estimation
- Explicit pin-level connectivity (clock, enable, reset, data pins identified by name)
- Functional category annotations for all cells (ppu-bgfifo, ppu-xcomp, clocks, etc.)

An earlier version of this project derived its data from [aappleby's GateBoy](https://github.com/aappleby/metroboy) C++ simulator using regex extraction. The schematics-based approach produces 31% more nodes, 70% more edges, and more accurate delay estimates.

## Dependencies

- Python 3.10+
- [NetworkX](https://networkx.org/) for graph analysis

## Acknowledgments

This project builds on the remarkable work of several people in the Game Boy reverse engineering community:

- **[Michael Singer (msinger)](https://github.com/msinger)** and **[Régis Galland](https://github.com/rgalland)** for [dmg-schematics](https://github.com/msinger/dmg-schematics) — the corrected KiCad schematics and parsable netlists that are the primary input to this analysis — and for the [interactive die photo viewer](https://iceboy.a-singer.de/dmg_cpu_b_map/), [cell netlist documentation](https://iceboy.a-singer.de/doc/dmg_cpu_b_netlist.html), and [cell type reference](https://iceboy.a-singer.de/doc/dmg_cells.html)
- **[Furrtek](https://github.com/furrtek)** for [DMG-CPU-Inside](https://github.com/furrtek/DMG-CPU-Inside) — the original die photo tracing of the DMG-CPU B
- **[aappleby](https://github.com/aappleby)** for [MetroBoy/GateBoy](https://github.com/aappleby/metroboy) — the gate-level Game Boy simulator that informed the earlier version of this analysis
- **[siliconpr0n](https://siliconpr0n.org/)** for the high-resolution die imagery
- The [Pan Docs](https://gbdev.io/pandocs/) contributors for the Game Boy technical reference

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
