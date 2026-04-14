#!/usr/bin/env python3
"""Build the interactive DMG-CPU B Explorer HTML page.

Reads the analysis JSON outputs and signal concordance, then generates
a single self-contained HTML file at docs/index.html for GitHub Pages.
"""

import json
import re
from pathlib import Path

# dmg-schematics: source netlist repository
SCHEMATICS_BASE = 'https://github.com/msinger/dmg-schematics/tree/master'

# Pan Docs register page mapping
PANDOCS_BASE = 'https://gbdev.io/pandocs'
PANDOCS_URLS = {
    'LCDC': f'{PANDOCS_BASE}/LCDC.html',
    'STAT': f'{PANDOCS_BASE}/STAT.html',
    'SCY': f'{PANDOCS_BASE}/Scrolling.html',
    'SCX': f'{PANDOCS_BASE}/Scrolling.html',
    'LY': f'{PANDOCS_BASE}/STAT.html',
    'LYC': f'{PANDOCS_BASE}/STAT.html',
    'DMA': f'{PANDOCS_BASE}/OAM_DMA_Transfer.html',
    'BGP': f'{PANDOCS_BASE}/Palettes.html',
    'OBP0': f'{PANDOCS_BASE}/Palettes.html',
    'OBP1': f'{PANDOCS_BASE}/Palettes.html',
    'WY': f'{PANDOCS_BASE}/Scrolling.html',
    'WX': f'{PANDOCS_BASE}/Scrolling.html',
    'IF': f'{PANDOCS_BASE}/Interrupt_Sources.html',
    'FF0F': f'{PANDOCS_BASE}/Interrupt_Sources.html',
    'OAM': f'{PANDOCS_BASE}/OAM.html',
    'VRAM': f'{PANDOCS_BASE}/Tile_Data.html',
    'INT': f'{PANDOCS_BASE}/Interrupt_Sources.html',
    'SPRITE': f'{PANDOCS_BASE}/OAM.html',
    'TILE': f'{PANDOCS_BASE}/Tile_Data.html',
    'WINDOW': f'{PANDOCS_BASE}/Scrolling.html',
    'PIXEL_FIFO': f'{PANDOCS_BASE}/pixel_fifo.html',
}


def parse_concordance(md_path: Path) -> dict:
    """Parse signal_concordance.md into a lookup dictionary.

    Returns a dict mapping die cell names and signal names to their
    Pan Docs equivalents, and vice versa.
    """
    entries = []
    text = md_path.read_text()

    # Extract table rows — look for lines with | that contain signal info
    # Match patterns like: | 7 | VYXE | `LCDC_LCDENp` | LCDC.7 | ...
    for line in text.split('\n'):
        if not line.startswith('|') or '---' in line:
            continue
        cols = [c.strip().strip('`') for c in line.split('|')[1:-1]]
        if len(cols) >= 3:
            entries.append(cols)

    # Build lookup: cell_name -> info, signal_name -> info, pandocs_name -> signals
    lookup = {}
    for cols in entries:
        # Try to extract cell name (4-char uppercase)
        for col in cols:
            # 4-char cell names
            for word in col.replace(',', ' ').split():
                word = word.strip()
                if re.match(r'^[A-Z]{4}$', word):
                    lookup[word] = ' | '.join(cols)
            # Signal names with underscores
            if '_' in col and any(c.isupper() for c in col):
                clean = col.strip('`').split('(')[0].strip()
                if clean and len(clean) > 3:
                    lookup[clean] = ' | '.join(cols)
            # Pan Docs references like LCDC.7, STAT.3, FF44
            if re.match(r'(LCDC|STAT|SCY|SCX|LY|LYC|DMA|BGP|OBP[01]|WY|WX|FF[0-9A-F]{2})', col):
                lookup[col] = ' | '.join(cols)

    return lookup


def build_friendly_map(md_path: Path) -> dict:
    """Build a die_name -> friendly description map from signal_concordance.md.

    Extracts 4-char cell names from table rows and pairs them with the most
    descriptive column (function, Pan Docs reference, or signal name).
    """
    friendly = {}
    text = md_path.read_text()

    for line in text.split('\n'):
        if not line.startswith('|') or '---' in line:
            continue
        cols = [c.strip().strip('`') for c in line.split('|')[1:-1]]
        if len(cols) < 3:
            continue

        # Find 4-char cell names and their descriptions
        cell_names = []
        for col in cols:
            for word in col.replace(',', ' ').replace('-', ' ').split():
                word = word.strip()
                if re.match(r'^[A-Z]{4}$', word):
                    cell_names.append(word)

        if not cell_names:
            continue

        # Find the best description: prefer Function column, then Pan Docs, then Signal Name
        desc = ''
        for col in reversed(cols):
            col = col.strip()
            if not col or col == '—' or re.match(r'^[A-Z]{4}$', col):
                continue
            if re.match(r'^\d+$', col):  # skip bit numbers
                continue
            if re.match(r'^(ODD|EVN|—|DFF\d+|Gate|Comb|NorLatch|NandLatch)$', col):
                continue
            # Skip columns that are just cell ranges like "XEHO-SYBE"
            if re.match(r'^[A-Z]{4}-[A-Z]{4}$', col):
                continue
            desc = col
            break

        if desc:
            # Clean up
            desc = desc.strip('`').strip()
            desc = desc.strip('*')  # remove markdown bold
            # Skip useless descriptions
            if desc in ('Same pattern', 'Same pattern '):
                continue
            if re.match(r'^[A-Z]{4}_', desc):  # signal suffix like "LY1p_odd"
                continue
            if re.match(r'^NOT of [A-Z]{4}$', desc):  # "NOT of RAPE" etc.
                continue
            if len(desc) < 3:
                continue
            for name in cell_names:
                friendly[name.lower()] = desc

    return friendly


def build_graph_friendly(graph_path: Path) -> dict:
    """Derive friendly names from graph structure for cells that lack concordance entries.

    Uses bus node names and category annotations to describe what each cell does.
    """
    import json
    graph = json.loads(graph_path.read_text())
    nodes = {n['name']: n for n in graph['nodes']}
    friendly = {}

    # Map all cells (registered and combinatorial) to their data bus source
    cell_to_bus = {}
    for e in graph['edges']:
        if e['edge_type'] == 'data':
            src = nodes.get(e['src'], {})
            if src.get('node_type') == 'bus':
                cell_to_bus[e['dst']] = e['src']

    # Map sprite store cells to their store number via enable signal grouping.
    # Cells sharing the same clock/enable signals belong to the same store.
    sprite_bus_cells = {}  # cell -> (bus_type, data_bit)
    for cell, bus in cell_to_bus.items():
        bus_name = bus.replace('bus:', '')
        if bus_name.startswith('sprite_y_store'):
            sprite_bus_cells[cell] = ('Y offset', bus_name.replace('sprite_y_store', ''))
        elif bus_name.startswith('oam_render_a'):
            sprite_bus_cells[cell] = ('OAM data', bus_name.replace('oam_render_a', ''))

    for cell, (bus_type, data_bit) in sprite_bus_cells.items():
        friendly[cell] = f'Sprite store {bus_type} bit {data_bit}'

    # For cells fed by the CPU data bus, use category + bit for a useful name
    cat_labels = {
        'apu-ch1': 'CH1 (square+sweep)',
        'apu-ch2': 'CH2 (square)',
        'apu-ch3': 'CH3 (wave)',
        'apu-ch4': 'CH4 (noise)',
        'apu-control': 'APU control (NR50-NR52)',
        'apu-decode': 'APU address decode',
        'timer': 'Timer',
        'serial': 'Serial link',
        'int': 'Interrupt flags (FF0F)',
        'joypad': 'Joypad (FF00)',
        'test': 'Test mode (FF60)',
        'bootrom': 'Boot ROM',
        'bus-data': 'Data bus',
        'bus-adr': 'Address bus',
    }
    for cell, bus in cell_to_bus.items():
        if cell in friendly:
            continue  # already mapped above
        bus_name = bus.replace('bus:', '')
        # CPU data bus: d0-d7
        m = re.match(r'^d(\d)$', bus_name)
        if m:
            bit = m.group(1)
            node = nodes.get(cell, {})
            cat = node.get('category', '')
            label = cat_labels.get(cat, cat)
            if label:
                friendly[cell] = f'{label} register bit {bit}'

    # For registered cells with no bus source, use category as fallback
    for n in graph['nodes']:
        name = n['name']
        if name in friendly:
            continue
        if n.get('node_type') != 'registered':
            continue
        cat = n.get('category', '')
        label = cat_labels.get(cat)
        if label:
            friendly[name] = f'{label} counter/state'

    return friendly


def build_html(graph_json: str, paths_json: str, races_json: str,
               concordance_json: str, config_json: str,
               extra_friendly_json: str = '{}') -> str:
    """Build the complete HTML page with embedded data."""

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Game Boy Propagation Explorer</title>
<style>
:root {{
  --bg: #0d1117;
  --surface: #161b22;
  --surface2: #1c2333;
  --border: #30363d;
  --text: #e6edf3;
  --text-muted: #8b949e;
  --accent: #58a6ff;
  --accent2: #3fb950;
  --warn: #f85149;
  --orange: #d29922;
  --purple: #bc8cff;
  --teal: #39d353;
  --font-mono: 'SF Mono', 'Cascadia Code', 'Fira Code', Consolas, monospace;
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--text);
  font-size: 14px;
  line-height: 1.5;
}}
a {{ color: var(--accent); text-decoration: none; cursor: pointer; }}
a:hover {{ text-decoration: underline; }}

/* Header */
.header {{
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  gap: 24px;
  position: sticky;
  top: 0;
  z-index: 100;
}}
.header h1 {{
  font-size: 16px;
  font-weight: 600;
  white-space: nowrap;
}}
.tabs {{
  display: flex;
  gap: 4px;
}}
.tab-btn {{
  background: transparent;
  border: 1px solid transparent;
  border-radius: 6px;
  color: var(--text-muted);
  padding: 6px 14px;
  cursor: pointer;
  font-size: 13px;
  font-family: var(--font-sans);
  transition: all 0.15s;
}}
.tab-btn:hover {{ color: var(--text); background: var(--surface2); }}
.tab-btn.active {{
  color: var(--text);
  background: var(--surface2);
  border-color: var(--border);
}}
.header-stats {{
  margin-left: auto;
  color: var(--text-muted);
  font-size: 12px;
  white-space: nowrap;
}}

/* Filter bar */
.filter-bar {{
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 10px 24px;
  display: flex;
  gap: 12px;
  align-items: center;
  flex-wrap: wrap;
}}
.filter-group {{
  display: flex;
  align-items: center;
  gap: 6px;
}}
.filter-group label {{
  color: var(--text-muted);
  font-size: 12px;
  white-space: nowrap;
}}
select, input[type="text"], input[type="search"] {{
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text);
  padding: 5px 10px;
  font-size: 13px;
  font-family: var(--font-sans);
  outline: none;
}}
select:focus, input:focus {{
  border-color: var(--accent);
}}
input[type="search"] {{ width: 260px; }}
.toggle-group {{
  display: flex;
  border: 1px solid var(--border);
  border-radius: 6px;
  overflow: hidden;
}}
.toggle-btn {{
  background: transparent;
  border: none;
  border-right: 1px solid var(--border);
  color: var(--text-muted);
  padding: 5px 12px;
  cursor: pointer;
  font-size: 12px;
  font-family: var(--font-sans);
}}
.toggle-btn:last-child {{ border-right: none; }}
.toggle-btn.active {{ background: var(--surface2); color: var(--text); }}
.toggle-btn:hover {{ color: var(--text); }}
.result-count {{
  color: var(--text-muted);
  font-size: 12px;
  margin-left: auto;
}}

/* Content */
.content {{
  padding: 0;
  max-width: 100%;
}}
.tab-content {{
  display: none;
}}
.tab-content.active {{
  display: block;
}}

/* Tables */
.data-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}}
.data-table th {{
  background: var(--surface);
  border-bottom: 2px solid var(--border);
  padding: 8px 12px;
  text-align: left;
  font-weight: 600;
  font-size: 12px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  white-space: nowrap;
  position: sticky;
  top: 50px;
  z-index: 10;
}}
.data-table th:hover {{ color: var(--text); }}
.data-table th.sorted-asc::after {{ content: ' \\2191'; }}
.data-table th.sorted-desc::after {{ content: ' \\2193'; }}
.data-table td {{
  padding: 6px 12px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}}
.data-table tr.data-row {{ cursor: pointer; }}
.data-table tr.data-row:hover {{ background: var(--surface2); }}
.data-table tr.expanded {{ background: var(--surface); }}

/* Badges */
.badge {{
  display: inline-block;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 11px;
  font-weight: 500;
  white-space: nowrap;
}}
.badge-phase {{
  background: #1f3a5f;
  color: #79c0ff;
}}
.badge-phase-evn {{
  background: #3b2f1a;
  color: #e3b341;
}}
.badge-cat {{
  background: #1a2f1a;
  color: #7ee787;
}}
.badge-depth {{
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 13px;
}}
.badge-depth.high {{ color: var(--warn); }}
.badge-depth.mid {{ color: var(--orange); }}
.badge-depth.low {{ color: var(--text-muted); }}
.badge-reset {{
  background: #2d1a1a;
  color: #f8514f;
  font-size: 10px;
}}
.badge-operational {{
  background: #1a2d1a;
  color: #3fb950;
  font-size: 10px;
}}

/* Detail panel (expanded row) */
.detail-row td {{
  padding: 0 !important;
  border-bottom: 2px solid var(--accent) !important;
}}
.detail-panel {{
  background: var(--surface2);
  padding: 16px 24px;
}}
.detail-section {{
  margin-bottom: 16px;
}}
.detail-section h4 {{
  font-size: 12px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}}
.detail-section p {{
  color: var(--text);
  font-size: 13px;
  line-height: 1.6;
  max-width: 80ch;
}}
.inputs-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
  font-family: var(--font-mono);
}}
.inputs-table th {{
  background: var(--bg);
  padding: 4px 8px;
  text-align: left;
  font-weight: 600;
  color: var(--text-muted);
  font-size: 11px;
  border-bottom: 1px solid var(--border);
  position: static;
}}
.inputs-table td {{
  padding: 4px 8px;
  border-bottom: 1px solid var(--border);
}}
.inputs-table tr.late td {{ color: var(--warn); }}
.inputs-table tr.early td {{ color: var(--accent2); }}

/* Gate chain trace */
.chain {{
  font-family: var(--font-mono);
  font-size: 12px;
  padding: 8px 0;
}}
.chain-node {{
  display: flex;
  align-items: center;
  padding: 3px 0;
  gap: 8px;
}}
.chain-connector {{
  width: 20px;
  text-align: center;
  color: var(--border);
}}
.chain-type {{
  font-size: 11px;
  padding: 1px 6px;
  border-radius: 3px;
  min-width: 60px;
  text-align: center;
}}
.chain-type.registered {{ background: #1a3a1a; color: var(--accent2); }}
.chain-type.combinatorial {{ background: #2f2a1a; color: var(--orange); }}
.chain-type.bus {{ background: #1a2a3a; color: var(--accent); }}
.chain-type.boundary {{ background: #2a2a2a; color: var(--text-muted); }}
.chain-name {{ color: var(--text); }}
.chain-name .signal-link {{ color: var(--accent); cursor: pointer; }}
.chain-name .signal-link:hover {{ text-decoration: underline; }}
.chain-phase {{ color: var(--purple); font-size: 11px; }}
.chain-fanout {{ color: var(--orange); font-size: 11px; }}
.chain-loc {{ color: var(--text-muted); font-size: 11px; margin-left: auto; }}

/* Depth bar */
.depth-bar {{
  display: flex;
  align-items: center;
  gap: 6px;
  margin: 8px 0;
}}
.depth-bar-track {{
  flex: 1;
  height: 6px;
  background: var(--bg);
  border-radius: 3px;
  position: relative;
  max-width: 300px;
}}
.depth-bar-fill {{
  height: 100%;
  border-radius: 3px;
  position: absolute;
  left: 0;
  top: 0;
}}
.depth-bar-fill.early {{ background: var(--accent2); }}
.depth-bar-fill.late {{ background: var(--warn); }}
.depth-bar-label {{
  font-size: 11px;
  color: var(--text-muted);
  font-family: var(--font-mono);
  min-width: 80px;
}}

/* Search */
.search-container {{
  padding: 24px;
  max-width: 1000px;
}}
.search-input {{
  width: 100%;
  font-size: 16px;
  padding: 12px 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  font-family: var(--font-mono);
  margin-bottom: 24px;
}}
.search-input:focus {{ border-color: var(--accent); outline: none; }}
.search-results {{ display: flex; flex-direction: column; gap: 16px; }}
.search-result {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
}}
.search-result h3 {{
  font-family: var(--font-mono);
  font-size: 14px;
  margin-bottom: 8px;
}}
.search-result .meta {{
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}}
.search-result .related {{
  font-size: 12px;
  color: var(--text-muted);
}}
.search-result .related a {{
  margin-right: 8px;
}}

/* Graph explorer */
.graph-container {{
  padding: 24px;
}}
.node-header {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
}}
.node-header h2 {{
  font-family: var(--font-mono);
  font-size: 18px;
  margin-bottom: 12px;
}}
.node-props {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 8px;
}}
.node-prop {{
  font-size: 12px;
}}
.node-prop .label {{ color: var(--text-muted); }}
.node-prop .value {{ color: var(--text); font-family: var(--font-mono); }}
.neighbors {{
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 16px;
  margin-bottom: 20px;
}}
.neighbor-col {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
}}
.neighbor-col h3 {{
  font-size: 12px;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 12px;
}}
.neighbor-center {{
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: var(--border);
}}
.neighbor-list {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}
.neighbor-item {{
  font-family: var(--font-mono);
  font-size: 12px;
  padding: 4px 8px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.neighbor-item:hover {{ background: var(--surface2); }}
.neighbor-item .ntype {{
  font-size: 10px;
  color: var(--text-muted);
}}
.paths-through {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
}}
.paths-through h3 {{
  font-size: 12px;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 12px;
}}
.path-entry {{
  font-size: 12px;
  padding: 6px 0;
  border-bottom: 1px solid var(--border);
  display: flex;
  gap: 12px;
  align-items: center;
}}
.path-entry:last-child {{ border-bottom: none; }}
.node-nav {{
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}}
.node-nav-input {{
  flex: 1;
  font-family: var(--font-mono);
}}

/* Utility */
.mono {{ font-family: var(--font-mono); }}
.muted {{ color: var(--text-muted); }}
.text-warn {{ color: var(--warn); }}
.text-accent {{ color: var(--accent); }}
.text-green {{ color: var(--accent2); }}
.badge-die {{
  background: #2d1f3d;
  color: #d2a8ff;
  font-size: 10px;
  cursor: pointer;
}}
.badge-die:hover, .badge-netlist:hover {{
  background: #3d2f4d;
  text-decoration: none;
}}
.badge-netlist {{
  background: #1d2f3d;
  color: #79c0ff;
  font-size: 10px;
  cursor: pointer;
}}
.badge-celltype {{
  background: #1a2d1a;
  color: #7ee787;
  font-size: 10px;
  cursor: pointer;
}}
.badge-celltype:hover {{
  background: #2a3d2a;
  text-decoration: none;
}}
.friendly-name {{
  display: block;
  font-size: 11px;
  color: var(--purple);
  font-family: var(--font-sans);
  font-weight: normal;
  line-height: 1.3;
}}
.empty-state {{
  padding: 60px 24px;
  text-align: center;
  color: var(--text-muted);
}}
</style>
</head>
<body>

<div class="header">
  <h1>Game Boy Propagation Explorer</h1>
  <div class="tabs">
    <button class="tab-btn active" data-tab="races">Race Pairs</button>
    <button class="tab-btn" data-tab="paths">Critical Paths</button>
    <button class="tab-btn" data-tab="search">Search</button>
    <button class="tab-btn" data-tab="graph">Graph</button>
  </div>
  <div class="header-stats" id="header-stats"></div>
  <a href="https://github.com/msinger/dmg-schematics" target="_blank" rel="noopener"
     style="color:var(--text-muted);font-size:11px;white-space:nowrap"
     title="Gate-level netlist from corrected die tracing">dmg-schematics</a>
</div>

<!-- RACE PAIRS TAB -->
<div class="tab-content active" id="tab-races">
  <div class="filter-bar">
    <div class="filter-group">
      <label>Category</label>
      <select id="race-cat-filter"><option value="">All</option><option value="ppu">PPU only</option></select>
    </div>
    <div class="filter-group">
      <label>Min Diff</label>
      <select id="race-diff-filter">
        <option value="0">All</option>
        <option value="5">5+</option>
        <option value="8">8+</option>
        <option value="10" selected>10+</option>
        <option value="13">13+</option>
        <option value="15">15+</option>
      </select>
    </div>
    <div class="filter-group" style="display:none">
      <select id="race-phase-filter"><option value="">All</option></select>
    </div>
    <div class="filter-group">
      <input type="search" id="race-search" placeholder="Filter by signal name...">
    </div>
    <span class="result-count" id="race-count"></span>
  </div>
  <table class="data-table" id="race-table">
    <thead><tr>
      <th data-sort="display_name">Node</th>
      <th data-sort="category">Category</th>
      <th data-sort="reg_type">Type</th>
      <th data-sort="depth_diff" class="sorted-desc">Diff</th>
      <th data-sort="max_depth">Max</th>
      <th data-sort="min_depth">Min</th>
      <th>Effect</th>
    </tr></thead>
    <tbody id="race-tbody"></tbody>
  </table>
</div>

<!-- CRITICAL PATHS TAB -->
<div class="tab-content" id="tab-paths">
  <div class="filter-bar">
    <div class="filter-group">
      <label>Category</label>
      <select id="path-cat-filter"><option value="">All</option><option value="ppu">PPU only</option></select>
    </div>
    <div class="filter-group">
      <label>Min Depth</label>
      <select id="path-depth-filter">
        <option value="1">All</option>
        <option value="5">5+</option>
        <option value="8" selected>8+</option>
        <option value="10">10+</option>
        <option value="12">12+</option>
        <option value="15">15+</option>
      </select>
    </div>
    <div class="filter-group">
      <div class="toggle-group">
        <button class="toggle-btn active" data-filter="path-reset" data-value="all">All</button>
        <button class="toggle-btn" data-filter="path-reset" data-value="operational">Operational</button>
        <button class="toggle-btn" data-filter="path-reset" data-value="reset">Reset</button>
      </div>
    </div>
    <div class="filter-group">
      <input type="search" id="path-search" placeholder="Filter by source or sink...">
    </div>
    <span class="result-count" id="path-count"></span>
  </div>
  <table class="data-table" id="path-table">
    <thead><tr>
      <th data-sort="depth" class="sorted-desc">Depth</th>
      <th data-sort="source">Source</th>
      <th data-sort="sink">Sink</th>
      <th>Delay (ns)</th>
      <th data-sort="pct_half_tcycle">% T/2</th>
      <th data-sort="category">Category</th>
      <th>Reset?</th>
    </tr></thead>
    <tbody id="path-tbody"></tbody>
  </table>
</div>

<!-- SEARCH TAB -->
<div class="tab-content" id="tab-search">
  <div class="search-container">
    <input type="search" class="search-input" id="search-input"
           placeholder="Search by die name, register, or Pan Docs name (sacu, muwy, LCDC, SCX, LY...)">
    <div class="search-results" id="search-results">
      <div class="empty-state">
        Type a signal name to search across the graph, critical paths, and race pairs.
      </div>
    </div>
  </div>
</div>

<!-- GRAPH TAB -->
<div class="tab-content" id="tab-graph">
  <div class="graph-container">
    <div class="node-nav">
      <input type="search" class="search-input node-nav-input" id="graph-nav-input"
             placeholder="Enter a signal name to explore..." style="margin-bottom:0; font-size:14px; padding:8px 12px;">
    </div>
    <div id="graph-content">
      <div class="empty-state">
        Enter a signal name above, or click any signal name in the Race Pairs or Critical Paths tabs.
      </div>
    </div>
  </div>
</div>

<!-- Embedded data -->
<script id="data-graph" type="application/json">{graph_json}</script>
<script id="data-paths" type="application/json">{paths_json}</script>
<script id="data-races" type="application/json">{races_json}</script>
<script id="data-concordance" type="application/json">{concordance_json}</script>
<script id="data-config" type="application/json">{config_json}</script>
<script id="data-friendly" type="application/json">{extra_friendly_json}</script>

<script>
"use strict";

// =====================================================================
// Data loading & index building
// =====================================================================
const graph = JSON.parse(document.getElementById("data-graph").textContent);
const paths = JSON.parse(document.getElementById("data-paths").textContent);
const races = JSON.parse(document.getElementById("data-races").textContent);
const concordance = JSON.parse(document.getElementById("data-concordance").textContent);
const config = JSON.parse(document.getElementById("data-config").textContent);
const extraFriendly = JSON.parse(document.getElementById("data-friendly").textContent);

// Node lookup by name and display_name
const nodeMap = new Map();
const nodeByDisplay = new Map();
for (const n of graph.nodes) {{
  nodeMap.set(n.name, n);
  nodeByDisplay.set(n.display_name, n);
}}

// Edge indexes
const inEdges = new Map();
const outEdges = new Map();
for (const e of graph.edges) {{
  if (!inEdges.has(e.dst)) inEdges.set(e.dst, []);
  inEdges.get(e.dst).push(e.src);
  if (!outEdges.has(e.src)) outEdges.set(e.src, []);
  outEdges.get(e.src).push(e.dst);
}}

// Path index: which paths contain each node
const nodeToPathIdx = new Map();
for (let i = 0; i < paths.length; i++) {{
  for (const nd of paths[i].nodes) {{
    const key = nd.display_name;
    if (!nodeToPathIdx.has(key)) nodeToPathIdx.set(key, []);
    nodeToPathIdx.get(key).push(i);
  }}
}}

// Race index: which races involve each node
const nodeToRaceIdx = new Map();
for (let i = 0; i < races.length; i++) {{
  const r = races[i];
  if (!nodeToRaceIdx.has(r.display_name)) nodeToRaceIdx.set(r.display_name, []);
  nodeToRaceIdx.get(r.display_name).push(i);
  for (const inp of r.inputs) {{
    if (!nodeToRaceIdx.has(inp.name)) nodeToRaceIdx.set(inp.name, []);
    nodeToRaceIdx.get(inp.name).push(i);
  }}
}}

// Stats
document.getElementById("header-stats").textContent =
  `${{graph.nodes.length}} nodes / ${{graph.edges.length}} edges / ${{paths.length}} paths / ${{races.length}} races`;

// =====================================================================
// Utility functions
// =====================================================================
function escHtml(s) {{
  return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}}

function phaseBadge(phase) {{
  if (!phase) return '';
  const cls = phase === 'EVN' ? 'badge-phase-evn' : 'badge-phase';
  return `<span class="badge ${{cls}}">${{escHtml(phase)}}</span>`;
}}

function depthBadge(d) {{
  const cls = d >= 12 ? 'high' : d >= 8 ? 'mid' : 'low';
  return `<span class="badge-depth ${{cls}}">${{d}}</span>`;
}}

function catBadge(cat) {{
  return `<span class="badge badge-cat">${{escHtml(cat)}}</span>`;
}}

function signalLink(name, showFriendly) {{
  const friendly = friendlyName(name);
  const tip = friendly ? ` title="${{escHtml(friendly)}}"` : '';
  const sub = (showFriendly && friendly) ? `<span class="friendly-name">${{escHtml(friendly)}}</span>` : '';
  return `<a class="signal-link" onclick="navigateGraph('${{escHtml(name)}}')"${{tip}}>${{escHtml(name)}}</a>${{sub}}`;
}}

function srcLink(file, line) {{
  if (!file) return '';
  const cleanPath = file.replace(/^dmg-schematics\//, '');
  const url = `${{config.source_base}}/${{cleanPath}}`;
  const display = cleanPath.replace(/^netlist\//, '');
  return `<a href="${{url}}" target="_blank" rel="noopener" class="muted">${{escHtml(display)}}</a>`;
}}

function dieLink(displayName) {{
  if (!displayName) return '';
  const m = displayName.match(/^([a-zA-Z]{{4}})/);
  if (!m) return '';
  const cell = m[1].toLowerCase();
  const dieUrl = `https://iceboy.a-singer.de/dmg_cpu_b_map/?view=c:${{cell}}`;
  const netUrl = `https://iceboy.a-singer.de/doc/dmg_cpu_b_netlist.html#c_${{cell}}`;
  return `<a href="${{dieUrl}}" target="_blank" rel="noopener" class="badge badge-die" title="View ${{m[1]}} on die photo">Die</a>`
       + `<a href="${{netUrl}}" target="_blank" rel="noopener" class="badge badge-netlist" title="View ${{m[1]}} netlist connections">Netlist</a>`;
}}

const cellTypeAnchors = {{
  'dffr': 'dffr', 'dffr_cc': 'dffr_cc', 'dffr_cc_q': 'dffr_cc_q', 'dffsr': 'dffsr',
  'tffnl': 'tffnl',
  'dlatch': 'dlatch', 'dlatch_ee': 'dlatch_ee', 'dlatch_ee_q': 'dlatch_ee_q',
  'drlatch_ee': 'drlatch_ee',
  'nor_latch': 'nor_latch', 'nand_latch': 'nand_latch',
}};

const gateFuncAnchors = {{
  'not_x1': 'not_x1', 'not_x2': 'not_x1', 'not_x3': 'not_x1',
  'not_x4': 'not_x1', 'not_x6': 'not_x1',
  'and2': 'and2', 'and3': 'and3', 'and4': 'and4',
  'or2': 'or2', 'or3': 'or3', 'or4': 'or4',
  'nand2': 'nand2', 'nand3': 'nand3', 'nand4': 'nand4',
  'nand5': 'nand5', 'nand6': 'nand6', 'nand7': 'nand7',
  'eco_nand2': 'nand2',
  'nor2': 'nor2', 'nor3': 'nor3', 'nor4': 'nor4',
  'nor5': 'nor5', 'nor6': 'nor6', 'nor8': 'nor8',
  'xor': 'xor', 'xnor': 'xnor',
  'muxi': 'muxi', 'mux': 'mux',
  'ao21': 'ao21', 'ao22': 'ao22', 'ao222': 'ao222', 'ao2222': 'ao2222',
  'oai21': 'oai21', 'oa21': 'oa21',
  'half_add': 'half_add', 'full_add': 'full_add',
  'not_if0': 'not_if0', 'not_if1': 'not_if1', 'buf_if0': 'buf_if0',
}};

function cellTypeLink(regType) {{
  if (!regType) return '';
  const anchor = cellTypeAnchors[regType];
  if (!anchor) return '';
  const url = `https://iceboy.a-singer.de/doc/dmg_cells.html#${{anchor}}`;
  return `<a href="${{url}}" target="_blank" rel="noopener" class="badge badge-celltype" title="Cell type: ${{regType}}">${{escHtml(regType)}}</a>`;
}}

function gateFuncLink(gateFunc) {{
  if (!gateFunc) return '';
  const anchor = gateFuncAnchors[gateFunc];
  if (!anchor) return '';
  const url = `https://iceboy.a-singer.de/doc/dmg_cells.html#${{anchor}}`;
  return `<a href="${{url}}" target="_blank" rel="noopener" class="badge badge-celltype" title="Gate: ${{gateFunc}}">${{escHtml(gateFunc)}}</a>`;
}}

function pandocsLink(signalName) {{
  if (!signalName) return '';
  const upper = signalName.toUpperCase();
  for (const [key, url] of Object.entries(config.pandocs_urls)) {{
    if (upper.includes(key)) {{
      return `<a href="${{url}}" target="_blank" rel="noopener" class="badge badge-phase" style="font-size:10px" title="Pan Docs: ${{key}}">Pan Docs</a>`;
    }}
  }}
  return '';
}}

// =====================================================================
// Tab management
// =====================================================================
const tabBtns = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

tabBtns.forEach(btn => {{
  btn.addEventListener('click', () => {{
    tabBtns.forEach(b => b.classList.remove('active'));
    tabContents.forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
  }});
}});

function switchTab(tabId) {{
  tabBtns.forEach(b => {{
    b.classList.toggle('active', b.dataset.tab === tabId);
  }});
  tabContents.forEach(c => {{
    c.classList.toggle('active', c.id === 'tab-' + tabId);
  }});
}}

// =====================================================================
// Friendly signal names — die name lookup
// =====================================================================
const friendlyMap = {{
  'sacu': 'Pixel Shift Clock (CLKPIPE)',
  'xymu': 'Rendering Active (Mode 3)', 'poky': 'Pixel Pipe Done',
  'roxy': 'Fine Scroll Done', 'nyka': 'BG Fetch Clock', 'atej': 'Line Strobe',
  'vyxe': 'LCDC.0', 'vogu': 'LCDC.1', 'vyno': 'LCDC.2', 'vyre': 'LCDC.3',
  'veku': 'LCDC.4', 'vevy': 'LCDC.5', 'voky': 'LCDC.6', 'vapa': 'LCDC.7 LCD Enable',
  'roxe': 'STAT.3 HBI', 'rufo': 'STAT.4 VBI', 'refe': 'STAT.5 OAM', 'rugu': 'STAT.6 LYC',
  'muwy': 'LY.0', 'myro': 'LY.1', 'lexa': 'LY.2', 'lydo': 'LY.3',
  'lovu': 'LY.4', 'lema': 'LY.5', 'mato': 'LY.6', 'lafo': 'LY.7',
  'syry': 'LYC.0', 'vuce': 'LYC.1', 'sedy': 'LYC.2', 'salo': 'LYC.3',
  'sota': 'LYC.4', 'vafa': 'LYC.5', 'vevo': 'LYC.6', 'raha': 'LYC.7',
  'gave': 'SCY.0', 'fymo': 'SCY.1', 'fezu': 'SCY.2', 'fujo': 'SCY.3',
  'dede': 'SCY.4', 'foty': 'SCY.5', 'foha': 'SCY.6', 'funy': 'SCY.7',
  'daty': 'SCX.0', 'duzu': 'SCX.1', 'cyxu': 'SCX.2', 'gubo': 'SCX.3',
  'bemy': 'SCX.4', 'cuzy': 'SCX.5', 'cabu': 'SCX.6', 'bake': 'SCX.7',
  'neso': 'WY.0', 'nyro': 'WY.1', 'naga': 'WY.2', 'mela': 'WY.3',
  'nulo': 'WY.4', 'nene': 'WY.5', 'nuka': 'WY.6', 'nafu': 'WY.7',
  'mypa': 'WX.0', 'nofe': 'WX.1', 'noke': 'WX.2', 'meby': 'WX.3',
  'mypu': 'WX.4', 'myce': 'WX.5', 'muvo': 'WX.6', 'nuku': 'WX.7',
  'xeho': 'PX.0', 'savy': 'PX.1', 'xodu': 'PX.2', 'xydo': 'PX.3',
  'tuhu': 'PX.4', 'tuky': 'PX.5', 'tako': 'PX.6', 'sybe': 'PX.7',
  'saxo': 'LX.0', 'typo': 'LX.1', 'vyzo': 'LX.2', 'telu': 'LX.3',
  'sude': 'LX.4', 'taha': 'LX.5', 'tyry': 'LX.6',
  'laxu': 'BG Fetch S0', 'mesu': 'BG Fetch S1', 'nyva': 'BG Fetch S2',
  'lovy': 'Tile Fetch Done', 'lony': 'Tile Fetching',
  'besu': 'OAM Scan Done', 'ceno': 'Scan Active',
  'taka': 'Sprite Fetch Gate', 'sobu': 'Sprite Fetch Req',
  'texy': 'Sprite Fetching', 'wuty': 'Sprite Fetch Done',
  'ryfa': 'Window Y Match', 'rene': 'Window Active',
  'pyco': 'Window Hit', 'sovy': 'Window Mode', 'nopa': 'Window Fetch Req',
  'afer': 'System Reset', 'asol': 'POR Done', 'xapo': 'Video Reset',
  'pavo': 'BGP.0', 'nusy': 'BGP.1', 'pylu': 'BGP.2', 'maxy': 'BGP.3',
  'muke': 'BGP.4', 'moru': 'BGP.5', 'mogy': 'BGP.6', 'mena': 'BGP.7',
  // Sprite store X latches (stores 1-9, concordance had "Same pattern")
  'dany': 'Sprite 1 X latch', 'duze': 'Sprite 1 X latch',
  'foka': 'Sprite 2 X latch', 'foby': 'Sprite 2 X latch',
  'xoly': 'Sprite 3 X latch', 'xyba': 'Sprite 3 X latch',
  'wedu': 'Sprite 4 X latch', 'wafy': 'Sprite 4 X latch',
  'fusa': 'Sprite 5 X latch', 'feka': 'Sprite 5 X latch',
  'ycol': 'Sprite 6 X latch', 'yber': 'Sprite 6 X latch',
  'eraz': 'Sprite 7 X latch', 'enol': 'Sprite 7 X latch',
  'ezuf': 'Sprite 8 X latch', 'enym': 'Sprite 8 X latch',
  'caro': 'Sprite 9 X latch', 'cado': 'Sprite 9 X latch',
  // Memory blocks
  'high_ram': 'High RAM (HRAM)', 'boot_rom': 'Boot ROM', 'wave_ram': 'Wave RAM (CH3)',
  // Buses — CPU address
  'bus:a0': 'CPU addr bus A0', 'bus:a1': 'CPU addr bus A1', 'bus:a2': 'CPU addr bus A2',
  'bus:a3': 'CPU addr bus A3', 'bus:a4': 'CPU addr bus A4', 'bus:a5': 'CPU addr bus A5',
  'bus:a6': 'CPU addr bus A6', 'bus:a7': 'CPU addr bus A7', 'bus:a8': 'CPU addr bus A8',
  'bus:a9': 'CPU addr bus A9', 'bus:a10': 'CPU addr bus A10', 'bus:a11': 'CPU addr bus A11',
  'bus:a12': 'CPU addr bus A12', 'bus:a13': 'CPU addr bus A13',
  'bus:a14': 'CPU addr bus A14', 'bus:a15': 'CPU addr bus A15',
  // Buses — CPU data
  'bus:d0': 'CPU data bus D0', 'bus:d1': 'CPU data bus D1', 'bus:d2': 'CPU data bus D2',
  'bus:d3': 'CPU data bus D3', 'bus:d4': 'CPU data bus D4', 'bus:d5': 'CPU data bus D5',
  'bus:d6': 'CPU data bus D6', 'bus:d7': 'CPU data bus D7',
  // Buses — VRAM data
  'bus:md0': 'VRAM data bus MD0', 'bus:md1': 'VRAM data bus MD1',
  'bus:md2': 'VRAM data bus MD2', 'bus:md3': 'VRAM data bus MD3',
  'bus:md4': 'VRAM data bus MD4', 'bus:md5': 'VRAM data bus MD5',
  'bus:md6': 'VRAM data bus MD6', 'bus:md7': 'VRAM data bus MD7',
  // Buses — VRAM address
  'bus:~ma0': 'VRAM addr bus MA0', 'bus:~ma1': 'VRAM addr bus MA1',
  'bus:~ma2': 'VRAM addr bus MA2', 'bus:~ma3': 'VRAM addr bus MA3',
  'bus:~ma4': 'VRAM addr bus MA4', 'bus:~ma5': 'VRAM addr bus MA5',
  'bus:~ma6': 'VRAM addr bus MA6', 'bus:~ma7': 'VRAM addr bus MA7',
  'bus:~ma8': 'VRAM addr bus MA8', 'bus:~ma9': 'VRAM addr bus MA9',
  'bus:~ma10': 'VRAM addr bus MA10', 'bus:~ma11': 'VRAM addr bus MA11',
  'bus:~ma12': 'VRAM addr bus MA12',
  // Buses — OAM data
  'bus:~oam_a_d0': 'OAM data A bus D0 (Y/tile)', 'bus:~oam_a_d1': 'OAM data A bus D1 (Y/tile)',
  'bus:~oam_a_d2': 'OAM data A bus D2 (Y/tile)', 'bus:~oam_a_d3': 'OAM data A bus D3 (Y/tile)',
  'bus:~oam_a_d4': 'OAM data A bus D4 (Y/tile)', 'bus:~oam_a_d5': 'OAM data A bus D5 (Y/tile)',
  'bus:~oam_a_d6': 'OAM data A bus D6 (Y/tile)', 'bus:~oam_a_d7': 'OAM data A bus D7 (Y/tile)',
  'bus:~oam_b_d0': 'OAM data B bus D0 (X/attr)', 'bus:~oam_b_d1': 'OAM data B bus D1 (X/attr)',
  'bus:~oam_b_d2': 'OAM data B bus D2 (X/attr)', 'bus:~oam_b_d3': 'OAM data B bus D3 (X/attr)',
  'bus:~oam_b_d4': 'OAM data B bus D4 (X/attr)', 'bus:~oam_b_d5': 'OAM data B bus D5 (X/attr)',
  'bus:~oam_b_d6': 'OAM data B bus D6 (X/attr)', 'bus:~oam_b_d7': 'OAM data B bus D7 (X/attr)',
  // Buses — OAM address & sprite render
  'bus:oam_~{{a0}}_tri': 'OAM addr bus A0', 'bus:oam_~{{a1}}_tri': 'OAM addr bus A1',
  'bus:oam_~{{a2}}_tri': 'OAM addr bus A2', 'bus:oam_~{{a3}}_tri': 'OAM addr bus A3',
  'bus:oam_~{{a4}}_tri': 'OAM addr bus A4', 'bus:oam_~{{a5}}_tri': 'OAM addr bus A5',
  'bus:oam_~{{a6}}_tri': 'OAM addr bus A6', 'bus:oam_~{{a7}}_tri': 'OAM addr bus A7',
  'bus:oam_render_a2': 'Sprite render data bit 2', 'bus:oam_render_a3': 'Sprite render data bit 3',
  'bus:oam_render_a4': 'Sprite render data bit 4', 'bus:oam_render_a5': 'Sprite render data bit 5',
  'bus:oam_render_a6': 'Sprite render data bit 6', 'bus:oam_render_a7': 'Sprite render data bit 7',
  'bus:sprite_y_store0': 'Sprite Y store bit 0', 'bus:sprite_y_store1': 'Sprite Y store bit 1',
  'bus:sprite_y_store2': 'Sprite Y store bit 2', 'bus:sprite_y_store3': 'Sprite Y store bit 3',
  // Buses — clock
  'bus:clk_t4': 'T-cycle clock T4', 'bus:~clk_t4': 'T-cycle clock ~T4',
  'bus:data_phase': 'CPU data phase', 'bus:~data_phase': 'CPU ~data phase',
  // Sprite store 0
  'xepe': 'Sprite 0 X latch', 'xako': 'Sprite 0 X latch',
  // LY match / reset chain
  'rape': 'LY=LYC full match (NAND)', 'paly': 'LY=LYC match (inverted)',
  'nyxu': 'BG fetch reset (depth 17, late arrival)',
}};

const categoryNames = {{
  'ppu-bgfifo': 'BG FIFO', 'ppu-bgscroll': 'BG Scroll',
  'ppu-control': 'PPU Control', 'ppu-cycles': 'BG/Win Cycles',
  'ppu-decode': 'PPU Decode', 'ppu-dma': 'DMA',
  'ppu-lcd': 'LCD', 'ppu-mux': 'Pixel Mux',
  'ppu-oam': 'OAM', 'ppu-objctl': 'Sprite Control',
  'ppu-objfifo': 'Sprite FIFO', 'ppu-objreg': 'Sprite Store',
  'ppu-pal': 'Palettes', 'ppu-stat': 'STAT/LY',
  'ppu-vram': 'VRAM', 'ppu-window': 'Window',
  'ppu-xcomp': 'Sprite X Match', 'ppu-xprio': 'Sprite X Priority',
  'ppu-ycomp': 'Sprite Y Compare',
  'clocks': 'Clocks', 'int': 'Interrupts', 'timer': 'Timer',
}};

function friendlyName(displayName) {{
  if (!displayName) return '';
  const name = displayName.toLowerCase();
  // Hand-curated die name map (highest priority)
  if (friendlyMap[name]) return friendlyMap[name];
  // Auto-extracted from signal_concordance.md
  if (extraFriendly[name]) return extraFriendly[name];
  // Fall back to raw concordance lookup
  const upper = displayName.toUpperCase();
  if (concordance[upper]) return concordance[upper];
  // Show category as fallback for nodes in the graph
  const node = nodeByDisplay.get(displayName);
  if (node && node.category && categoryNames[node.category]) {{
    return categoryNames[node.category];
  }}
  return '';
}}

// =====================================================================
// Observable effects — maps races to emulator-visible symptoms
// =====================================================================
function observableEffect(r) {{
  const name = r.display_name.toLowerCase();
  const cat = r.category || '';
  const diff = r.depth_diff;
  const maxD = r.max_depth;
  const minD = r.min_depth;

  // === Specific die-name matches (known critical signals) ===

  // Tile fetch state machine — reset arrives late
  if (['laxu','mesu','nyva'].some(x => name === x))
    return `Tile fetch state machine runs one extra cycle before reset. The fetch counter reset arrives at depth ${{maxD}} while the fetch clock arrives at depth ${{minD}}. The state machine advances one extra state before resetting, causing a corrupted tile at the left screen edge or at window/BG boundary transitions.`;
  if (['lovy','lony'].some(x => name === x))
    return `Tile fetch pipeline stays active one dot too long. The fetch-done/fetching flag reset (depth ${{maxD}}) arrives late, consuming an additional VRAM cycle. This shifts the mode 3/mode 0 boundary by one dot, affecting H-blank timing and any mid-scanline register writes.`;

  // OAM scan done — extends past boundary
  if (['besu','ceno'].some(x => name === x))
    return `OAM scan extends one dot past expected boundary. The scan-done signal (depth ${{maxD}}) races against line-end (depth ${{minD}}), potentially including one extra sprite in the scanline buffer. Affects the mode 2→3 transition timing, most visible with exactly 10 sprites on a line.`;

  // Window control — late activation
  if (['ryfa','roge'].some(x => name === x))
    return `Window Y match fires one dot late. The WY comparison (depth ${{maxD}}) races against rendering control, potentially delaying window activation by one dot. Affects games with split-screen effects using the window.`;
  if (['rene','nuko','pyco','nopa','sovy'].some(x => name === x))
    return `Window trigger fires one dot late (${{diff}}-gate differential). Window content may shift one pixel right, affecting status bars and dialogue boxes in games that use the window layer.`;

  // Sprite fetcher
  if (['taka','sobu','texy','wuty'].some(x => name === x))
    return `Sprite fetch timing shifted by one dot (${{diff}}-gate differential). May cause sprite fetch to start or complete one dot off, affecting mode 3 duration and sprite X positioning.`;

  // Pixel counter vs CLKPIPE
  if (['xeho','savy','xodu','xydo','tuhu','tuky','tako','sybe'].some(x => name === x))
    return `Pixel counter races CLKPIPE (${{diff}}-gate differential). The pixel X counter increments late relative to the pipe shift clock, shifting the X coordinate at which sprite/window comparisons trigger by one dot.`;

  // Mode transitions
  if (['xymu'].includes(name))
    return `Rendering mode latch (mode 3) transitions one dot off. Affects when the CPU can access VRAM/OAM and when H-blank begins. Games using mid-scanline STAT tricks are most affected.`;
  if (['voga','wodu'].some(x => name === x))
    return `H-blank/mode flag transitions one dot off (${{diff}}-gate differential). Shifts when the CPU regains VRAM/OAM access.`;

  // DMA
  if (['matu','lara','loky'].some(x => name === x))
    return `DMA transfer timing off by one cycle. May affect when DMA releases the OAM bus back to the PPU.`;

  // LY match
  if (['ropo','rupo'].some(x => name === x))
    return `LY=LYC match fires one dot early/late (${{diff}}-gate differential). The STAT interrupt may trigger at a different dot than expected, affecting raster effects (palette changes, wobble).`;

  // === Category-based matches with detailed descriptions ===

  if (cat === 'ppu-objreg') {{
    const what = friendlyName(name) || 'sprite store latch';
    return `${{what}} — reset arrives late at line boundary. Line-end reset (depth ${{maxD}}) arrives long after OAM data (depth ${{minD}}). At scanline boundaries, the latch may hold stale data instead of clearing. Visible as wrong sprite position, tile, or attributes at the start of a scanline.`;
  }}
  if (cat === 'ppu-xcomp')
    return `Sprite X match off by one dot (${{diff}}-gate differential). The X comparison that triggers sprite fetching settles at a different time than CLKPIPE, causing the sprite to appear one pixel left or right of its correct position.`;
  if (cat === 'ppu-bgfifo')
    return `BG pixel data shifted one dot late relative to CLKPIPE. The pixel pipe effectively shifts one propagation delay after data settles. BG pixels may appear one dot to the right.`;
  if (cat === 'ppu-objfifo')
    return `Sprite pixel data shifted one dot late relative to CLKPIPE. Sprite pixels may appear one dot offset from their correct position.`;
  if (cat === 'ppu-bgscroll')
    return `Scroll address computation delayed (${{diff}}-gate differential). The BG scroll adder (LY+SCY or pixel+SCX) carry chain propagates through ${{maxD}} gate-equivalents. VRAM address may be ready late.`;
  if (cat === 'ppu-stat')
    return `STAT/LY timing off by one dot (${{diff}}-gate differential). May affect STAT interrupt timing or LY match flag, causing raster effects to trigger at the wrong position.`;
  if (cat === 'ppu-window')
    return `Window trigger fires one dot late (${{diff}}-gate differential). Window content may shift one pixel right, affecting games with status bars or dialogue boxes.`;
  if (cat === 'ppu-cycles')
    return `BG/window fetch cycle timing race (${{diff}}-gate differential). May cause one extra or one fewer fetch cycle, shifting all subsequent pixel output timing.`;
  if (cat === 'ppu-objctl')
    return `Sprite control timing race (${{diff}}-gate differential). May affect which sprite store slot captures OAM data, or when sprite fetch begins.`;
  if (cat === 'ppu-ycomp')
    return `Sprite Y comparison delayed (${{diff}}-gate differential). The 8-bit Y comparator carry chain takes ${{maxD}} gate-equivalents. At line boundaries, the wrong sprites may pass the Y test.`;
  if (cat === 'ppu-vram')
    return `VRAM interface timing race (${{diff}}-gate differential). May affect VRAM address/data bus timing during tile fetch.`;
  if (cat === 'ppu-oam')
    return `OAM access timing race (${{diff}}-gate differential). May affect OAM data latch timing during sprite scan.`;
  if (cat === 'ppu-dma')
    return `DMA timing off by one cycle (${{diff}}-gate differential). May affect when DMA releases the OAM bus back to the PPU.`;
  if (cat === 'ppu-lcd')
    return `LCD pixel output timing race (${{diff}}-gate differential). May affect the LCD data/clock signal timing.`;
  if (cat === 'ppu-pal')
    return `Palette latch timing race (${{diff}}-gate differential). May affect which palette value is applied to the current pixel.`;
  if (cat === 'ppu-mux')
    return `Pixel mux timing race (${{diff}}-gate differential). May affect sprite/BG priority decision for the current pixel.`;
  if (cat === 'ppu-xprio')
    return `Sprite X priority timing race (${{diff}}-gate differential). May affect which sprite wins when multiple sprites overlap at the same X position.`;
  if (cat === 'ppu-decode')
    return `PPU address decode timing race (${{diff}}-gate differential). May affect register read/write timing.`;

  // Bus node races — these are real: the address/data must settle before the bus is sampled
  if (cat === 'bus' || name.startsWith('bus:')) {{
    if (name.includes('ma') || name.includes('~ma'))
      return `VRAM address bus bit — carry chain from scroll adder (depth ${{maxD}}) means the address may not settle within one dot. The VRAM may read from the wrong tile/map address for one cycle.`;
    if (name.includes('oam'))
      return `OAM bus — data arrives at different depths (${{diff}}-gate differential). May affect which sprite data is latched during OAM scan.`;
    if (name.startsWith('bus:d'))
      return `CPU data bus — register read data from multiple sources arrives at different depths (${{diff}}-gate differential). May affect CPU read timing for memory-mapped registers.`;
    return `Bus timing race (${{diff}}-gate differential). Multiple drivers settle at different times.`;
  }}

  // Non-PPU categories
  if (cat.startsWith('apu-'))
    return `APU timing race (${{diff}}-gate differential). Audio channel register/counter may sample stale data.`;
  if (cat === 'clocks')
    return `Clock distribution timing race (${{diff}}-gate differential). Clock phase signal may arrive late relative to the data it gates.`;
  if (cat === 'timer')
    return `Timer timing race (${{diff}}-gate differential). DIV/TIMA counter may increment or overflow one cycle off.`;
  if (cat === 'serial')
    return `Serial link timing race (${{diff}}-gate differential). Shift clock or data may be sampled one cycle off.`;
  if (cat === 'int')
    return `Interrupt flag timing race (${{diff}}-gate differential). IRQ flag may be set or cleared one cycle off, affecting interrupt timing.`;
  if (cat === 'joypad')
    return `Joypad read timing race (${{diff}}-gate differential). Button state may be sampled one cycle off.`;
  if (cat === 'bus-adr')
    return `Address bus timing race (${{diff}}-gate differential). Address decode may settle late, affecting which register is accessed.`;
  if (cat === 'bus-data')
    return `Data bus timing race (${{diff}}-gate differential). Read data from multiple sources settles at different times.`;
  if (cat === 'test')
    return `Test mode register timing race (${{diff}}-gate differential). Only affects debug/test hardware.`;
  if (cat === 'bootrom')
    return `Boot ROM timing race (${{diff}}-gate differential). Only affects the boot sequence.`;

  const catName = categoryNames[cat] || cat;
  return catName ? catName + ` timing race (${{diff}}-gate differential)` : `timing race (${{diff}}-gate differential)`;
}}

// =====================================================================
// Race Pairs Tab
// =====================================================================
let raceSortKey = 'depth_diff', raceSortDir = -1;
let raceExpandedId = null;

function populateRaceFilters() {{
  const cats = [...new Set(races.map(r => r.category))].sort();
  const phases = [...new Set(races.map(r => r.phase).filter(Boolean))].sort();
  const catSel = document.getElementById('race-cat-filter');
  cats.forEach(c => {{
    const o = document.createElement('option');
    o.value = c; o.textContent = c;
    catSel.appendChild(o);
  }});
  const phaseSel = document.getElementById('race-phase-filter');
  phases.forEach(p => {{
    const o = document.createElement('option');
    o.value = p; o.textContent = p;
    phaseSel.appendChild(o);
  }});
}}

function getFilteredRaces() {{
  const cat = document.getElementById('race-cat-filter').value;
  const minDiff = parseInt(document.getElementById('race-diff-filter').value) || 0;
  const phase = document.getElementById('race-phase-filter').value;
  const search = document.getElementById('race-search').value.toUpperCase();

  let filtered = races.filter(r => {{
    if (cat === 'ppu' && !r.category.startsWith('ppu-')) return false;
    if (cat && cat !== 'ppu' && r.category !== cat) return false;
    if (r.depth_diff < minDiff) return false;
    if (phase && r.phase !== phase) return false;
    if (search && !r.display_name.toUpperCase().includes(search)) return false;
    return true;
  }});

  // Group races with same functional role:
  // Same friendly name pattern (with bit number stripped) + same depth_diff.
  // e.g. "Sprite OAM data bit 2" and "bit 7" group together,
  // but "Sprite Y offset" stays separate from "Sprite OAM data".
  const groupMap = new Map();
  for (const r of filtered) {{
    const fname = friendlyName(r.display_name) || r.display_name;
    // Strip trailing bit/store numbers to get the pattern
    const pattern = fname.replace(/\s*(?:bit\s*)?\d+(?:\s*\(.*\))?\s*$/, '').trim();
    const key = `${{pattern}}|${{r.depth_diff}}`;
    if (!groupMap.has(key)) {{
      groupMap.set(key, {{ representative: r, members: [], key, pattern }});
    }}
    groupMap.get(key).members.push(r);
  }}

  let groups = [...groupMap.values()];
  groups.sort((a, b) => {{
    const ar = a.representative, br = b.representative;
    const av = ar[raceSortKey], bv = br[raceSortKey];
    if (typeof av === 'string') return raceSortDir * av.localeCompare(bv);
    return raceSortDir * (av - bv);
  }});

  return {{ filtered, groups }};
}}

function renderRaceDetail(r) {{
  const maxDepth = Math.max(...r.inputs.map(i => i.depth), 1);
  let inputRows = r.inputs.map(inp => {{
    const isLate = inp.depth === r.max_depth;
    const isEarly = inp.depth === r.min_depth;
    const cls = isLate ? 'late' : isEarly ? 'early' : '';
    const role = isLate ? 'LATE' : isEarly ? 'early' : 'mid';
    const delay = inp.depth > 0 ? `${{inp.depth*5}}-${{inp.depth*15}} ns` : '0 ns';
    return `<tr class="${{cls}}">
      <td>${{signalLink(inp.name, true)}}</td>
      <td>${{inp.depth}}</td>
      <td>${{delay}}</td>
      <td>${{gateFuncLink(inp.gate_func) || escHtml(inp.gate_func || inp.node_type)}}</td>
      <td>${{role}}</td>
    </tr>`;
  }}).join('');

  const effect = observableEffect(r);
  const diffMin = r.depth_diff * 5, diffMax = r.depth_diff * 15;
  const pct = (diffMax / 119.2 * 100).toFixed(0);
  const earlyPct = (r.min_depth / maxDepth * 100).toFixed(0);
  const latePct = (r.max_depth / maxDepth * 100).toFixed(0);

  return `<div class="detail-panel">
    <div class="detail-section">
      <h4>Observable Effect</h4>
      <p><strong>${{escHtml(effect)}}</strong></p>
      <p class="muted" style="margin-top:4px">
        Late signal arrives <strong>${{diffMin}}-${{diffMax}} ns</strong> after earliest input
        (${{pct}}% of half T-cycle).
      </p>
    </div>
    <div class="detail-section">
      <h4>Depth Comparison</h4>
      <div class="depth-bar">
        <span class="depth-bar-label text-green">Early: ${{r.min_depth}}</span>
        <div class="depth-bar-track">
          <div class="depth-bar-fill early" style="width:${{earlyPct}}%"></div>
        </div>
      </div>
      <div class="depth-bar">
        <span class="depth-bar-label text-warn">Late: ${{r.max_depth}}</span>
        <div class="depth-bar-track">
          <div class="depth-bar-fill late" style="width:${{latePct}}%"></div>
        </div>
      </div>
    </div>
    <div class="detail-section">
      <h4>Inputs</h4>
      <table class="inputs-table">
        <thead><tr><th>Signal</th><th>Depth</th><th>Delay</th><th>Gate</th><th>Role</th></tr></thead>
        <tbody>${{inputRows}}</tbody>
      </table>
    </div>
    <div class="detail-section" style="display:flex;gap:12px;align-items:center">
      ${{srcLink(r.source_file, r.source_line)}}
      ${{dieLink(r.display_name)}}
      ${{pandocsLink(r.display_name)}}
    </div>
  </div>`;
}}

function renderRaces() {{
  const {{ filtered, groups }} = getFilteredRaces();
  document.getElementById('race-count').textContent = `${{filtered.length}} races in ${{groups.length}} groups`;

  const tbody = document.getElementById('race-tbody');
  tbody.innerHTML = '';

  for (const group of groups) {{
    const r = group.representative;
    const count = group.members.length;
    const countBadge = count > 1 ? `<span class="badge badge-cat" style="font-size:10px">${{count}} cells</span>` : '';
    const groupLabel = count > 1 ? `<span class="friendly-name">${{escHtml(group.pattern)}}</span>` : '';

    const tr = document.createElement('tr');
    tr.className = 'data-row';
    tr.innerHTML = `
      <td class="mono">${{count > 1 ? groupLabel : signalLink(r.display_name, true)}} ${{countBadge}}</td>
      <td>${{catBadge(r.category)}}</td>
      <td class="mono">${{cellTypeLink(r.reg_type) || escHtml(r.reg_type)}}</td>
      <td>${{depthBadge(r.depth_diff)}}</td>
      <td class="mono muted">${{r.max_depth}}</td>
      <td class="mono muted">${{r.min_depth}}</td>
      <td class="muted" style="font-size:12px">${{escHtml(observableEffect(r))}}</td>
    `;
    const detailTr = document.createElement('tr');
    detailTr.className = 'detail-row';
    detailTr.style.display = 'none';

    // Build detail: show representative's full detail + list of all members
    const memberList = count > 1 ? `<div class="detail-section">
      <h4>All cells in this group (${{count}})</h4>
      <table class="inputs-table">
        <thead><tr><th>Cell</th><th>Description</th></tr></thead>
        <tbody>${{group.members.map(m => `<tr>
          <td class="mono">${{signalLink(m.display_name)}}</td>
          <td style="font-size:12px">${{escHtml(friendlyName(m.display_name) || m.category)}}</td>
        </tr>`).join('')}}</tbody>
      </table>
    </div>` : '';

    detailTr.innerHTML = `<td colspan="7">${{renderRaceDetail(r)}}${{memberList}}</td>`;

    tr.addEventListener('click', (e) => {{
      if (e.target.closest('.signal-link')) return;
      const wasOpen = detailTr.style.display !== 'none';
      // Close all
      tbody.querySelectorAll('.detail-row').forEach(d => d.style.display = 'none');
      tbody.querySelectorAll('.data-row').forEach(d => d.classList.remove('expanded'));
      if (!wasOpen) {{
        detailTr.style.display = '';
        tr.classList.add('expanded');
      }}
    }});

    tbody.appendChild(tr);
    tbody.appendChild(detailTr);
  }}
}}

// Sort handler for races
document.querySelectorAll('#race-table th[data-sort]').forEach(th => {{
  th.addEventListener('click', () => {{
    const key = th.dataset.sort;
    if (raceSortKey === key) raceSortDir *= -1;
    else {{ raceSortKey = key; raceSortDir = -1; }}
    document.querySelectorAll('#race-table th').forEach(h => {{
      h.classList.remove('sorted-asc', 'sorted-desc');
    }});
    th.classList.add(raceSortDir > 0 ? 'sorted-asc' : 'sorted-desc');
    renderRaces();
  }});
}});

['race-cat-filter', 'race-diff-filter', 'race-phase-filter', 'race-search'].forEach(id => {{
  document.getElementById(id).addEventListener('input', renderRaces);
  document.getElementById(id).addEventListener('change', renderRaces);
}});

// =====================================================================
// Critical Paths Tab
// =====================================================================
let pathSortKey = 'depth', pathSortDir = -1;
let pathResetFilter = 'all';

function populatePathFilters() {{
  const cats = [...new Set(paths.map(p => p.category))].sort();
  const sel = document.getElementById('path-cat-filter');
  cats.forEach(c => {{
    const o = document.createElement('option');
    o.value = c; o.textContent = c;
    sel.appendChild(o);
  }});
}}

function getFilteredPaths() {{
  const cat = document.getElementById('path-cat-filter').value;
  const minDepth = parseInt(document.getElementById('path-depth-filter').value) || 1;
  const search = document.getElementById('path-search').value.toUpperCase();

  let filtered = paths.filter(p => {{
    if (cat && p.category !== cat) return false;
    if (p.depth < minDepth) return false;
    if (pathResetFilter === 'operational' && p.is_reset) return false;
    if (pathResetFilter === 'reset' && !p.is_reset) return false;
    if (search && !p.source.toUpperCase().includes(search) && !p.sink.toUpperCase().includes(search)) return false;
    return true;
  }});

  filtered.sort((a, b) => {{
    const av = a[pathSortKey], bv = b[pathSortKey];
    if (typeof av === 'string') return pathSortDir * av.localeCompare(bv);
    return pathSortDir * (av - bv);
  }});

  return filtered;
}}

function renderChain(nodes) {{
  return nodes.map((nd, i) => {{
    const typeClass = nd.node_type || 'combinatorial';
    const label = nd.gate_func || nd.node_type || '?';
    const connector = i === 0 ? '' : '<div class="chain-connector">\\u2193</div>';
    const fo = nd.fan_out >= 10 ? `<span class="chain-fanout">(fan-out: ${{nd.fan_out}})</span>` : '';
    const ds = nd.drive_strength > 1 ? `<span class="badge badge-cat" style="font-size:9px">x${{nd.drive_strength}}</span>` : '';
    const ge = nd.gate_equiv > 1 ? `<span class="chain-fanout">ge=${{nd.gate_equiv}}</span>` : '';
    return `${{connector}}
      <div class="chain-node">
        <span class="chain-type ${{typeClass}}">${{escHtml(label)}}</span>
        <span class="chain-name">${{signalLink(nd.display_name, true)}}</span>
        ${{dieLink(nd.display_name)}} ${{ds}} ${{ge}} ${{fo}}
      </div>`;
  }}).join('');
}}

function renderPathDetail(p) {{
  return `<div class="detail-panel">
    <div class="detail-section">
      <h4>Gate Chain (${{p.depth}} combinatorial gates)</h4>
      <div class="chain">${{renderChain(p.nodes)}}</div>
    </div>
  </div>`;
}}

function renderPaths() {{
  const filtered = getFilteredPaths();
  document.getElementById('path-count').textContent = `${{filtered.length}} paths`;

  const tbody = document.getElementById('path-tbody');
  tbody.innerHTML = '';

  for (const p of filtered) {{
    const pctClass = p.pct_half_tcycle > 100 ? 'text-warn' : p.pct_half_tcycle > 50 ? 'text-accent' : 'muted';
    const tr = document.createElement('tr');
    tr.className = 'data-row';
    tr.innerHTML = `
      <td>${{depthBadge(p.depth)}}</td>
      <td class="mono">${{signalLink(p.source, true)}}</td>
      <td class="mono">${{signalLink(p.sink, true)}}</td>
      <td class="mono muted">${{p.min_delay_ns}}-${{p.max_delay_ns}}</td>
      <td class="${{pctClass}} mono">${{p.pct_half_tcycle}}%</td>
      <td>${{catBadge(p.category)}}</td>
      <td>${{p.is_reset ? '<span class="badge badge-reset">reset</span>' : '<span class="badge badge-operational">op</span>'}}</td>
    `;
    const detailTr = document.createElement('tr');
    detailTr.className = 'detail-row';
    detailTr.style.display = 'none';
    detailTr.innerHTML = `<td colspan="7">${{renderPathDetail(p)}}</td>`;

    tr.addEventListener('click', (e) => {{
      if (e.target.closest('.signal-link')) return;
      const wasOpen = detailTr.style.display !== 'none';
      tbody.querySelectorAll('.detail-row').forEach(d => d.style.display = 'none');
      tbody.querySelectorAll('.data-row').forEach(d => d.classList.remove('expanded'));
      if (!wasOpen) {{
        detailTr.style.display = '';
        tr.classList.add('expanded');
      }}
    }});

    tbody.appendChild(tr);
    tbody.appendChild(detailTr);
  }}
}}

// Sort handler for paths
document.querySelectorAll('#path-table th[data-sort]').forEach(th => {{
  th.addEventListener('click', () => {{
    const key = th.dataset.sort;
    if (pathSortKey === key) pathSortDir *= -1;
    else {{ pathSortKey = key; pathSortDir = -1; }}
    document.querySelectorAll('#path-table th').forEach(h => {{
      h.classList.remove('sorted-asc', 'sorted-desc');
    }});
    th.classList.add(pathSortDir > 0 ? 'sorted-asc' : 'sorted-desc');
    renderPaths();
  }});
}});

// Toggle buttons for reset/operational
document.querySelectorAll('.toggle-btn[data-filter="path-reset"]').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.toggle-btn[data-filter="path-reset"]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    pathResetFilter = btn.dataset.value;
    renderPaths();
  }});
}});

['path-cat-filter', 'path-depth-filter', 'path-search'].forEach(id => {{
  document.getElementById(id).addEventListener('input', renderPaths);
  document.getElementById(id).addEventListener('change', renderPaths);
}});

// =====================================================================
// Search Tab
// =====================================================================
let searchDebounce = null;

function runSearch(query) {{
  const results = document.getElementById('search-results');
  if (!query || query.length < 2) {{
    results.innerHTML = '<div class="empty-state">Type at least 2 characters to search.</div>';
    return;
  }}

  const q = query.toUpperCase();
  const matches = [];

  // Search graph nodes
  for (const n of graph.nodes) {{
    if (n.display_name.toUpperCase().includes(q) || n.name.toUpperCase().includes(q)) {{
      matches.push(n);
    }}
  }}

  // Search concordance
  const concordanceHits = [];
  for (const [key, val] of Object.entries(concordance)) {{
    if (key.toUpperCase().includes(q) || val.toUpperCase().includes(q)) {{
      concordanceHits.push({{ key, val }});
    }}
  }}

  if (matches.length === 0 && concordanceHits.length === 0) {{
    results.innerHTML = '<div class="empty-state">No signals found.</div>';
    return;
  }}

  // Limit display
  const shown = matches.slice(0, 50);
  let html = '';

  if (concordanceHits.length > 0) {{
    html += `<div class="search-result">
      <h3>Pan Docs References (${{concordanceHits.length}})</h3>
      ${{concordanceHits.slice(0, 20).map(h =>
        `<div style="font-size:12px;padding:2px 0;font-family:var(--font-mono)">
          <strong>${{escHtml(h.key)}}</strong>: ${{escHtml(h.val)}}
        </div>`
      ).join('')}}
    </div>`;
  }}

  for (const n of shown) {{
    const pathIdxs = nodeToPathIdx.get(n.display_name) || [];
    const raceIdxs = nodeToRaceIdx.get(n.display_name) || [];
    const friendly = friendlyName(n.display_name);

    html += `<div class="search-result">
      <h3>${{signalLink(n.display_name)}}${{friendly ? ` <span class="friendly-name" style="display:inline;font-size:13px">${{escHtml(friendly)}}</span>` : ''}}</h3>
      <div class="meta">
        <span class="badge badge-cat">${{escHtml(n.node_type)}}</span>
        ${{n.gate_func ? (gateFuncLink(n.gate_func) || `<span class="badge badge-phase">${{escHtml(n.gate_func)}}</span>`) : ''}}
        ${{n.phase ? phaseBadge(n.phase) : ''}}
        ${{n.source_file ? srcLink(n.source_file, n.source_line) : ''}}
        ${{dieLink(n.display_name)}}
        ${{pandocsLink(n.display_name)}}
      </div>
      <div class="related">
        ${{pathIdxs.length > 0 ? `In <strong>${{pathIdxs.length}}</strong> critical paths` : ''}}
        ${{raceIdxs.length > 0 ? ` | In <strong>${{raceIdxs.length}}</strong> race pairs` : ''}}
        ${{pathIdxs.length === 0 && raceIdxs.length === 0 ? 'No critical paths or race pairs' : ''}}
      </div>
    </div>`;
  }}

  if (matches.length > 50) {{
    html += `<div class="empty-state">Showing 50 of ${{matches.length}} matches. Refine your search.</div>`;
  }}

  results.innerHTML = html;
}}

document.getElementById('search-input').addEventListener('input', (e) => {{
  clearTimeout(searchDebounce);
  searchDebounce = setTimeout(() => runSearch(e.target.value.trim()), 200);
}});

// =====================================================================
// Graph Explorer Tab
// =====================================================================
function navigateGraph(displayName) {{
  switchTab('graph');
  document.getElementById('graph-nav-input').value = displayName;
  renderGraphNode(displayName);
}}

function renderGraphNode(displayName) {{
  const container = document.getElementById('graph-content');

  // Find node by display_name or scoped name
  let node = nodeByDisplay.get(displayName);
  if (!node) {{
    // Try partial match
    for (const [dn, n] of nodeByDisplay) {{
      if (dn.toUpperCase() === displayName.toUpperCase()) {{ node = n; break; }}
    }}
  }}
  if (!node) {{
    // Try as scoped name
    node = nodeMap.get(displayName);
  }}
  if (!node) {{
    container.innerHTML = `<div class="empty-state">Signal "${{escHtml(displayName)}}" not found in graph.</div>`;
    return;
  }}

  const dn = node.display_name;

  // Neighbors
  const preds = (inEdges.get(node.name) || []).map(n => nodeMap.get(n)).filter(Boolean);
  const succs = (outEdges.get(node.name) || []).map(n => nodeMap.get(n)).filter(Boolean);

  // Paths through
  const pathIdxs = nodeToPathIdx.get(dn) || [];
  const raceIdxs = [...new Set(nodeToRaceIdx.get(dn) || [])];

  // Concordance
  const concHits = [];
  for (const [key, val] of Object.entries(concordance)) {{
    if (dn.toUpperCase().includes(key.toUpperCase()) || key.toUpperCase().includes(dn.substring(0, 4).toUpperCase())) {{
      concHits.push({{ key, val }});
    }}
  }}

  container.innerHTML = `
    <div class="node-header">
      <h2>${{escHtml(dn)}}${{(() => {{ const f = friendlyName(dn); return f ? ` <span class="friendly-name" style="font-size:14px;display:inline">${{escHtml(f)}}</span>` : ''; }})()}}</h2>
      <div class="node-props">
        <div class="node-prop"><span class="label">Type: </span><span class="value">${{escHtml(node.node_type)}}</span></div>
        ${{node.gate_func ? `<div class="node-prop"><span class="label">Gate: </span><span class="value">${{gateFuncLink(node.gate_func) || escHtml(node.gate_func)}}</span></div>` : ''}}
        ${{node.reg_type ? `<div class="node-prop"><span class="label">Reg: </span><span class="value">${{cellTypeLink(node.reg_type) || escHtml(node.reg_type)}}</span></div>` : ''}}
        ${{node.category ? `<div class="node-prop"><span class="label">Category: </span><span class="value">${{catBadge(node.category)}}</span></div>` : ''}}
        ${{node.drive_strength > 1 ? `<div class="node-prop"><span class="label">Drive: </span><span class="value">x${{node.drive_strength}}</span></div>` : ''}}
        ${{node.source_file ? `<div class="node-prop"><span class="label">Source: </span><span class="value">${{srcLink(node.source_file, node.source_line)}}</span></div>` : ''}}
        <div class="node-prop">${{dieLink(dn)}} ${{pandocsLink(dn)}}</div>
        <div class="node-prop"><span class="label">Fan-in: </span><span class="value">${{preds.length}}</span></div>
        <div class="node-prop"><span class="label">Fan-out: </span><span class="value">${{succs.length}}</span></div>
      </div>
      ${{concHits.length > 0 ? `<div style="margin-top:12px;font-size:12px;color:var(--text-muted)">
        <strong>Concordance:</strong> ${{concHits.slice(0,3).map(h => escHtml(h.val)).join(' | ')}}
        ${{pandocsLink(dn)}}
      </div>` : pandocsLink(dn)}}
    </div>

    <div class="neighbors">
      <div class="neighbor-col">
        <h3>Inputs (${{preds.length}})</h3>
        <div class="neighbor-list">
          ${{preds.slice(0, 30).map(p => `
            <div class="neighbor-item" onclick="navigateGraph('${{escHtml(p.display_name)}}')">
              <span>${{escHtml(p.display_name)}}</span>
              <span class="ntype">${{escHtml(p.node_type)}}</span>
            </div>
          `).join('')}}
          ${{preds.length > 30 ? `<div class="muted" style="padding:4px 8px;font-size:11px">...and ${{preds.length - 30}} more</div>` : ''}}
          ${{preds.length === 0 ? '<div class="muted" style="padding:4px 8px;font-size:11px">No inputs (source node)</div>' : ''}}
        </div>
      </div>
      <div class="neighbor-center">\\u2192</div>
      <div class="neighbor-col">
        <h3>Outputs (${{succs.length}})</h3>
        <div class="neighbor-list">
          ${{succs.slice(0, 30).map(s => `
            <div class="neighbor-item" onclick="navigateGraph('${{escHtml(s.display_name)}}')">
              <span>${{escHtml(s.display_name)}}</span>
              <span class="ntype">${{escHtml(s.node_type)}}</span>
            </div>
          `).join('')}}
          ${{succs.length > 30 ? `<div class="muted" style="padding:4px 8px;font-size:11px">...and ${{succs.length - 30}} more</div>` : ''}}
          ${{succs.length === 0 ? '<div class="muted" style="padding:4px 8px;font-size:11px">No outputs (sink node)</div>' : ''}}
        </div>
      </div>
    </div>

    ${{raceIdxs.length > 0 ? `
    <div class="paths-through" style="margin-bottom:20px">
      <h3>Race Pairs (${{raceIdxs.length}})</h3>
      ${{raceIdxs.slice(0, 20).map(i => {{
        const r = races[i];
        return `<div class="path-entry">
          ${{depthBadge(r.depth_diff)}}
          <span class="mono">${{signalLink(r.display_name)}}</span>
          <span class="muted" style="font-size:12px">${{escHtml(observableEffect(r))}}</span>
          ${{catBadge(r.category)}}
        </div>`;
      }}).join('')}}
    </div>` : ''}}

    <div class="paths-through">
      <h3>Critical Paths Through This Node (${{pathIdxs.length}})</h3>
      ${{pathIdxs.length === 0 ? '<div class="muted" style="padding:8px 0">No critical paths pass through this node.</div>' : ''}}
      ${{pathIdxs.slice(0, 30).map(i => {{
        const p = paths[i];
        return `<div class="path-entry">
          ${{depthBadge(p.depth)}}
          <span class="mono">${{signalLink(p.source)}}</span>
          <span class="muted">\\u2192</span>
          <span class="mono">${{signalLink(p.sink)}}</span>
          ${{catBadge(p.category)}}
          <span class="muted mono" style="font-size:11px">${{p.max_delay_ns}}ns (${{p.pct_half_tcycle}}%)</span>
        </div>`;
      }}).join('')}}
      ${{pathIdxs.length > 30 ? `<div class="muted" style="padding:8px 0;font-size:12px">...and ${{pathIdxs.length - 30}} more paths</div>` : ''}}
    </div>
  `;
}}

document.getElementById('graph-nav-input').addEventListener('keydown', (e) => {{
  if (e.key === 'Enter') {{
    renderGraphNode(e.target.value.trim());
  }}
}});

// =====================================================================
// Initialize
// =====================================================================
populateRaceFilters();
populatePathFilters();
renderRaces();
renderPaths();

</script>
</body>
</html>'''


def main():
    out_dir = Path('output')
    docs_dir = Path('docs')

    graph_json = (out_dir / 'ppu_graph.json').read_text()
    paths_json = (out_dir / 'critical_paths.json').read_text()
    races_json = (out_dir / 'race_pairs.json').read_text()

    concordance = parse_concordance(out_dir / 'signal_concordance.md')
    concordance_json = json.dumps(concordance)

    extra_friendly = build_friendly_map(out_dir / 'signal_concordance.md')
    graph_friendly = build_graph_friendly(out_dir / 'ppu_graph.json')
    # Graph-derived sprite/register labels override concordance when the
    # concordance entry is generic (e.g. "Same pattern", "Reset depth...")
    merged = {**extra_friendly}
    for k, v in graph_friendly.items():
        existing = merged.get(k, '')
        if not existing or existing.startswith('Reset depth') or existing == 'Same pattern':
            merged[k] = v
    extra_friendly_json = json.dumps(merged)
    print(f'  {len(extra_friendly)} from concordance + {len(graph_friendly)} from graph = {len(merged)} friendly names')

    config = {
        'source_base': SCHEMATICS_BASE,
        'pandocs_urls': PANDOCS_URLS,
    }
    config_json = json.dumps(config)

    html = build_html(graph_json, paths_json, races_json, concordance_json, config_json, extra_friendly_json)

    output_path = docs_dir / 'index.html'
    output_path.write_text(html)
    print(f'Built {output_path} ({len(html) / 1024 / 1024:.1f} MB)')


if __name__ == '__main__':
    main()
