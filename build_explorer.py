#!/usr/bin/env python3
"""Build the interactive GateBoy PPU Explorer HTML page.

Reads the analysis JSON outputs and signal concordance, then generates
a single self-contained HTML file at docs/index.html for GitHub Pages.
"""

import json
import re
from pathlib import Path


def parse_concordance(md_path: Path) -> dict:
    """Parse signal_concordance.md into a lookup dictionary.

    Returns a dict mapping GateBoy cell names and signal names to their
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


def build_html(graph_json: str, paths_json: str, races_json: str,
               concordance_json: str) -> str:
    """Build the complete HTML page with embedded data."""

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GateBoy PPU Explorer</title>
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
.empty-state {{
  padding: 60px 24px;
  text-align: center;
  color: var(--text-muted);
}}
</style>
</head>
<body>

<div class="header">
  <h1>GateBoy PPU Explorer</h1>
  <div class="tabs">
    <button class="tab-btn active" data-tab="races">Race Pairs</button>
    <button class="tab-btn" data-tab="paths">Critical Paths</button>
    <button class="tab-btn" data-tab="search">Search</button>
    <button class="tab-btn" data-tab="graph">Graph</button>
  </div>
  <div class="header-stats" id="header-stats"></div>
</div>

<!-- RACE PAIRS TAB -->
<div class="tab-content active" id="tab-races">
  <div class="filter-bar">
    <div class="filter-group">
      <label>Category</label>
      <select id="race-cat-filter"><option value="">All</option></select>
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
    <div class="filter-group">
      <label>Phase</label>
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
      <th data-sort="phase">Phase</th>
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
      <select id="path-cat-filter"><option value="">All</option></select>
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
      <th>Phase</th>
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
           placeholder="Search by signal name, cell name, or Pan Docs name (LCDC, SCX, LY, CLKPIPE, BESU...)">
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

<script>
"use strict";

// =====================================================================
// Data loading & index building
// =====================================================================
const graph = JSON.parse(document.getElementById("data-graph").textContent);
const paths = JSON.parse(document.getElementById("data-paths").textContent);
const races = JSON.parse(document.getElementById("data-races").textContent);
const concordance = JSON.parse(document.getElementById("data-concordance").textContent);

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

function signalLink(name) {{
  return `<a class="signal-link" onclick="navigateGraph('${{escHtml(name)}}')">${{escHtml(name)}}</a>`;
}}

function srcLink(file, line) {{
  if (!file) return '';
  return `<span class="muted">${{escHtml(file)}}:${{line}}</span>`;
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
// Observable effects (matching parse_gateboy.py logic)
// =====================================================================
function observableEffect(r) {{
  const name = r.display_name.toUpperCase();
  const cat = r.category || '';

  if (name.includes('STORE') && name.includes('_X'))
    return 'Sprite store X-position off by one dot';
  if (name.includes('STORE') && (name.includes('_I') || name.includes('_L')))
    return 'Sprite store index/line data stale at reset';
  if (['BFETCH_S0','BFETCH_S1','BFETCH_S2','LAXU','MESU','NYVA'].some(x => name.includes(x)))
    return 'Tile fetch runs one extra cycle before reset';
  if (['TFETCH_DONE','LOVY','TFETCHING','LONY'].some(x => name.includes(x)))
    return 'Tile fetch pipeline active one dot too long';
  if (['SCAN_DONE','BESU','CENO'].some(x => name.includes(x)))
    return 'OAM scan extends one dot past boundary';
  if (['PIPE_A','PIPE_B','PAL_PIPE','MASK_PIPE','CLKPIPE'].some(x => name.includes(x)))
    return 'Pixel data shifted one dot late (CLKPIPE race)';
  if (['FINE','SCX_FINE','PUXA','NYZE','ROXY'].some(x => name.includes(x)))
    return 'Fine scroll match applies one dot late';
  if (['WIN_','RYFA','RENE','NUKO','ROGE','PYCO','NOPA','SOVY'].some(x => name.includes(x)))
    return 'Window trigger fires one dot late';
  if (['PX','XEHO','SAVY','XODU','XYDO'].some(x => name.includes(x)))
    return 'Pixel counter races pipe clock';
  if (['STAT','RUPO','ROPO','LY_MATCH'].some(x => name.includes(x)))
    return 'STAT interrupt one dot early/late';
  if (['HBLANK','VBLANK','VOGA','WODU','XYMU','RENDERING'].some(x => name.includes(x)))
    return 'Mode transition shifted one dot';
  if (['SFETCH','TAKA','SOBU','TEXY','WUTY'].some(x => name.includes(x)))
    return 'Sprite fetch timing shifted one dot';
  if (['DMA','MATU','LARA','LOKY'].some(x => name.includes(x)))
    return 'DMA timing off by one cycle';
  return cat + ' timing race';
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
    if (cat && r.category !== cat) return false;
    if (r.depth_diff < minDiff) return false;
    if (phase && r.phase !== phase) return false;
    if (search && !r.display_name.toUpperCase().includes(search)) return false;
    return true;
  }});

  filtered.sort((a, b) => {{
    const av = a[raceSortKey], bv = b[raceSortKey];
    if (typeof av === 'string') return raceSortDir * av.localeCompare(bv);
    return raceSortDir * (av - bv);
  }});

  return filtered;
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
      <td>${{signalLink(inp.name)}}</td>
      <td>${{inp.depth}}</td>
      <td>${{delay}}</td>
      <td>${{escHtml(inp.gate_func || inp.node_type)}}</td>
      <td>${{phaseBadge(inp.phase)}}</td>
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
        <thead><tr><th>Signal</th><th>Depth</th><th>Delay</th><th>Gate</th><th>Phase</th><th>Role</th></tr></thead>
        <tbody>${{inputRows}}</tbody>
      </table>
    </div>
    <div class="detail-section">
      <p class="muted">${{srcLink(r.source_file, r.source_line)}}</p>
    </div>
  </div>`;
}}

function renderRaces() {{
  const filtered = getFilteredRaces();
  document.getElementById('race-count').textContent = `${{filtered.length}} races`;

  const tbody = document.getElementById('race-tbody');
  tbody.innerHTML = '';

  for (const r of filtered) {{
    const tr = document.createElement('tr');
    tr.className = 'data-row';
    tr.innerHTML = `
      <td class="mono">${{signalLink(r.display_name)}}</td>
      <td>${{catBadge(r.category)}}</td>
      <td class="mono muted">${{escHtml(r.reg_type)}}</td>
      <td>${{phaseBadge(r.phase)}}</td>
      <td>${{depthBadge(r.depth_diff)}}</td>
      <td class="mono muted">${{r.max_depth}}</td>
      <td class="mono muted">${{r.min_depth}}</td>
      <td class="muted" style="font-size:12px">${{escHtml(observableEffect(r))}}</td>
    `;
    const detailTr = document.createElement('tr');
    detailTr.className = 'detail-row';
    detailTr.style.display = 'none';
    detailTr.innerHTML = `<td colspan="8">${{renderRaceDetail(r)}}</td>`;

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
    const phase = nd.phase ? `<span class="chain-phase">@${{escHtml(nd.phase)}}</span>` : '';
    const fo = nd.fan_out >= 10 ? `<span class="chain-fanout">(fan-out: ${{nd.fan_out}})</span>` : '';
    return `${{connector}}
      <div class="chain-node">
        <span class="chain-type ${{typeClass}}">${{escHtml(label)}}</span>
        <span class="chain-name">${{signalLink(nd.display_name)}}</span>
        ${{phase}} ${{fo}}
        <span class="chain-loc">${{escHtml(nd.source_file || '')}}${{nd.source_line ? ':' + nd.source_line : ''}}</span>
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
    const phaseStr = [p.source_phase, p.sink_phase].filter(Boolean).join('\\u2192');
    const tr = document.createElement('tr');
    tr.className = 'data-row';
    tr.innerHTML = `
      <td>${{depthBadge(p.depth)}}</td>
      <td class="mono">${{signalLink(p.source)}}</td>
      <td class="mono">${{signalLink(p.sink)}}</td>
      <td class="mono muted">${{p.min_delay_ns}}-${{p.max_delay_ns}}</td>
      <td class="${{pctClass}} mono">${{p.pct_half_tcycle}}%</td>
      <td>${{phaseStr ? phaseBadge(phaseStr) : ''}}</td>
      <td>${{catBadge(p.category)}}</td>
      <td>${{p.is_reset ? '<span class="badge badge-reset">reset</span>' : '<span class="badge badge-operational">op</span>'}}</td>
    `;
    const detailTr = document.createElement('tr');
    detailTr.className = 'detail-row';
    detailTr.style.display = 'none';
    detailTr.innerHTML = `<td colspan="8">${{renderPathDetail(p)}}</td>`;

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

    html += `<div class="search-result">
      <h3>${{signalLink(n.display_name)}}</h3>
      <div class="meta">
        <span class="badge badge-cat">${{escHtml(n.node_type)}}</span>
        ${{n.gate_func ? `<span class="badge badge-phase">${{escHtml(n.gate_func)}}</span>` : ''}}
        ${{n.phase ? phaseBadge(n.phase) : ''}}
        ${{n.source_file ? `<span class="muted" style="font-size:12px">${{escHtml(n.source_file)}}:${{n.source_line}}</span>` : ''}}
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
      <h2>${{escHtml(dn)}}</h2>
      <div class="node-props">
        <div class="node-prop"><span class="label">Type: </span><span class="value">${{escHtml(node.node_type)}}</span></div>
        ${{node.gate_func ? `<div class="node-prop"><span class="label">Gate: </span><span class="value">${{escHtml(node.gate_func)}}</span></div>` : ''}}
        ${{node.reg_type ? `<div class="node-prop"><span class="label">Reg: </span><span class="value">${{escHtml(node.reg_type)}}</span></div>` : ''}}
        ${{node.phase ? `<div class="node-prop"><span class="label">Phase: </span><span class="value">${{phaseBadge(node.phase)}}</span></div>` : ''}}
        ${{node.source_file ? `<div class="node-prop"><span class="label">Source: </span><span class="value">${{escHtml(node.source_file)}}:${{node.source_line}}</span></div>` : ''}}
        <div class="node-prop"><span class="label">Fan-in: </span><span class="value">${{preds.length}}</span></div>
        <div class="node-prop"><span class="label">Fan-out: </span><span class="value">${{succs.length}}</span></div>
      </div>
      ${{concHits.length > 0 ? `<div style="margin-top:12px;font-size:12px;color:var(--text-muted)">
        <strong>Concordance:</strong> ${{concHits.slice(0,3).map(h => escHtml(h.val)).join(' | ')}}
      </div>` : ''}}
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

    html = build_html(graph_json, paths_json, races_json, concordance_json)

    output_path = docs_dir / 'index.html'
    output_path.write_text(html)
    print(f'Built {output_path} ({len(html) / 1024 / 1024:.1f} MB)')


if __name__ == '__main__':
    main()
