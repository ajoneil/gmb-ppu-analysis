# Game Boy PPU Propagation Delay Analysis

Static analysis of the Game Boy (DMG) PPU's gate-level netlist to identify deep combinatorial paths that cause propagation delay on real hardware. The analysis is derived from [msinger's dmg-schematics](https://github.com/msinger/dmg-schematics), which contains corrected reverse-engineered schematics and parsable netlists of the DMG-CPU B chip, traced from die photography.

## Motivation

Behavioral Game Boy emulators resolve all combinatorial logic instantaneously within a single tick. On real DMG silicon, signals propagate through chains of gates with finite delay (5–15 ns per gate on Sharp's ~5 µm CMOS process). When a signal chain exceeds ~8 gates, the total delay can consume a significant fraction of a half T-cycle (~119 ns at 4.194 MHz), causing the hardware to capture different values than an emulator expects.

This project extracts the PPU's netlist as a dependency graph, finds the longest combinatorial paths between clocked elements, and ranks them by depth — producing a guide for emulator developers investigating one-dot timing discrepancies.

## Key Results

- **4,102 nodes** (974 registered, 2,970 combinatorial, 83 bus, 70 I/O pad, 5 boundary) and **9,458 edges** extracted
- **2,368 paths** with depth > 1 gate-equivalent identified (1,687 operational, 681 reset-only)
- Deepest operational path: **32 gate-equivalents** (~480 ns worst-case, 403% of half T-cycle)
  - This is an 8-bit ripple carry adder (LY + SCY → VRAM address)
  - Gate-equivalent counting: NOT=1, AND/OR=2, MUX=3, XOR=3, full_add=4
- **864 signal race points** where inputs to a single register differ by ≥ 3 gate-equivalent depths
- **2,106 PPU nodes** across 15 functional categories with drive strength (x1–x6) annotations

The dominant sources of late-arriving signals:
1. **VRAM address adder** (half_add + 7 full_adds) — carry chain from LY/SCY through BG scroll computation
2. **Sprite Y comparator** — 4-stage full_adder carry chain through sprite control to sprite store (depth 28)
3. **SACU / CLKPIPE** (pixel pipe shift clock) — fan-out 53, drives BG/sprite FIFOs and all X matchers

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
- **Race Pairs** — sortable/filterable table with expandable detail panels showing observable effects
- **Critical Paths** — browse all 2,368 paths by category, depth; click to see full gate chain with drive strength and gate-equivalent annotations
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
- Each node carries its exact cell type, drive strength, gate-equivalent delay cost, physical coordinates, and functional category annotation from the schematic authors

Multi-driver wires (shared buses) are modeled as intermediate bus nodes to avoid O(n×m) edge inflation while preserving real data paths.

Feedback loops (916 back-edges) are broken to form a DAG. Longest-path analysis then ranks all register-to-register paths by gate-equivalent depth, giving more realistic delay estimates than simple gate counting.

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
