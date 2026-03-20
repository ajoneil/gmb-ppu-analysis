# Game Boy PPU Propagation Delay Analysis

Static analysis of the Game Boy (DMG) PPU's gate-level netlist to identify deep combinatorial paths that cause propagation delay on real hardware. The analysis is derived from [aappleby's GateBoy](https://github.com/aappleby/metroboy) simulator, which models the actual silicon gates traced from Furrtek's die photos.

## Motivation

Behavioral Game Boy emulators resolve all combinatorial logic instantaneously within a single tick. On real DMG silicon, signals propagate through chains of gates with finite delay (5–15 ns per gate on Sharp's ~5 µm CMOS process). When a signal chain exceeds ~8 gates, the total delay can consume a significant fraction of a half T-cycle (~119 ns at 4.194 MHz), causing the hardware to capture different values than an emulator expects.

This project extracts the PPU's netlist as a dependency graph, finds the longest combinatorial paths between clocked elements, and ranks them by depth — producing a guide for emulator developers investigating one-dot timing discrepancies.

## Key Results

- **3,141 nodes** (928 registered, 2,213 combinatorial) and **5,573 edges** extracted
- **1,270 paths** with depth > 8 gates identified (969 operational, 301 reset-only)
- Deepest operational path: **17 gates** (~255 ns worst-case delay)
- **547 signal race points** where inputs to a single flip-flop differ by ≥ 3 gate depths

The two dominant sources of late-arriving signals:
1. **CLKPIPE** (pixel pipe shift clock) — 52 fan-out, depth 16, arrives after every pixel pipeline decision
2. **Line/fetch reset signals** — depth 15–17, arrive long after the data they reset

See [`output/critical_paths_report.md`](output/critical_paths_report.md) for the full findings.

## Project Structure

```
parse_gateboy.py              # Parser & graph builder (~2000 lines)
build_explorer.py             # Builds interactive HTML explorer
metroboy/                     # GateBoy source (analysis input)
docs/
  index.html                  # Interactive explorer (GitHub Pages)
output/
  critical_paths_report.md    # Overview & key findings (start here)
  operational_paths.md        # Operational paths by functional area
  race_pairs_report.md        # Signal race pairs with observable effects
  reset_paths.md              # Reset-only paths (LCDC toggle / sys reset)
  depth_distribution.md       # Path depth histogram
  signal_concordance.md       # Signal name ↔ Pan Docs register mapping
  ppu_graph.json              # Full dependency graph (nodes + edges)
  critical_paths.json         # All ranked critical paths
  race_pairs.json             # Signal race pair detection results
  gateboy-structure.md        # GateBoy type system & naming conventions
  graph-stats.md              # Graph extraction statistics
  critical_paths.dot/.svg     # Graphviz visualization of top paths
```

## Interactive Explorer

Browse the analysis interactively at **[ajoneil.github.io/gmb-ppu-analysis](https://ajoneil.github.io/gmb-ppu-analysis/)**.

Features:
- **Race Pairs** — sortable/filterable table with expandable detail panels showing observable effects
- **Critical Paths** — browse all 1,270 paths by category, depth, phase; click to see full gate chain trace
- **Search** — find any signal by cell name or Pan Docs register name (LCDC, SCX, LY, etc.)
- **Graph Explorer** — click any signal to see its inputs, outputs, and all paths flowing through it
- **External links** — each signal links to the [GateBoy source](https://github.com/aappleby/metroboy), [die photo viewer](https://iceboy.a-singer.de/dmg_cpu_b_map/), [netlist](https://iceboy.a-singer.de/doc/dmg_cpu_b_netlist.html), and [Pan Docs](https://gbdev.io/pandocs/)

## Usage

```bash
git clone <this-repo>
cd gmb-ppu-analysis

# Set up environment
python -m venv .venv
source .venv/bin/activate
pip install networkx

# Run analysis (reads from metroboy/src/GateBoyLib/)
python parse_gateboy.py

# Build interactive explorer (writes docs/index.html)
python build_explorer.py
```

Outputs are written to `output/` and `docs/`.

## How It Works

The parser uses regex-based extraction on GateBoy's C++ source to build a directed graph where:

- **Nodes** are signals — flip-flop outputs, latch outputs, bus lines, combinatorial gate outputs, and wire variables
- **Edges** represent data dependencies (signal A feeds into gate B)
- Each node is tagged as **registered** (DFF, latch, bus) or **combinatorial** (wire, gate)

Feedback loops (70 edges, mostly async set/reset and sprite pipe writeback) are broken to form a DAG. Longest-path analysis then ranks all register-to-register paths by combinatorial depth.

## Dependencies

- Python 3.10+
- [NetworkX](https://networkx.org/) for graph analysis
- [Graphviz](https://graphviz.org/) (optional, for rendering DOT files)

## Pinned GateBoy Version

This analysis is built against GateBoy commit [`36797ad4`](https://github.com/aappleby/metroboy/tree/36797ad4cf77b3e04ffe45716218a79b5280076a).
All source file references and line numbers in the reports and explorer link to this commit.

## Acknowledgments

This project builds on the remarkable work of several people in the Game Boy reverse engineering community:

- **[aappleby](https://github.com/aappleby)** for [MetroBoy/GateBoy](https://github.com/aappleby/metroboy) — the gate-level Game Boy simulator whose C++ source is the primary input to this analysis
- **[Furrtek](https://github.com/furrtek)** for [DMG-CPU-Inside](https://github.com/furrtek/DMG-CPU-Inside) — the original die photo tracing of the DMG-CPU B that GateBoy implements
- **[Michael Singer (msinger)](https://github.com/msinger)** for the [interactive die photo viewer](https://iceboy.a-singer.de/dmg_cpu_b_map/), [cell netlist documentation](https://iceboy.a-singer.de/doc/dmg_cpu_b_netlist.html), and [cleaned-up KiCad schematics](https://github.com/msinger/dmg-schematics) — the explorer links directly to these resources
- **[siliconpr0n](https://siliconpr0n.org/)** for the high-resolution die imagery
- The [Pan Docs](https://gbdev.io/pandocs/) contributors for the Game Boy technical reference that the signal concordance maps to

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
