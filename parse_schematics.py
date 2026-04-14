#!/usr/bin/env python3
"""
DMG-CPU B Netlist Parser — Graph Builder for Propagation Delay Analysis

Parses the machine-readable netlists from msinger/dmg-schematics to build a
signal dependency graph for critical path and race pair analysis.

Data source advantages:
- Ground-truth netlist from corrected die tracing
- Drive strength information (not_x1 vs not_x6, etc.)
- Physical coordinates for cells and wire routing
- Explicit cell types with pin definitions
- Functional category annotations from the schematic authors

Outputs: ppu_graph.json, critical_paths.json, race_pairs.json, and markdown reports.
"""

import re
import json
import math
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


# ============================================================================
# Configuration
# ============================================================================

NETLIST_DIR = Path("dmg-schematics/netlist")

# Netlist files to parse (order: types first, then cells/wires)
# types.nl and categories.nl are parsed for metadata; all .nl files in
# subdirectories contain actual cells and wires.
CELL_DIRS = [
    "top-left-col",
    "top-center-col",
    "top-center-row",
    "bottom-left-col",
    "bottom-center-col",
    "right-col",
    "io",
]

# Top-level files with cells/wires (not in subdirectories)
TOP_LEVEL_FILES = [
    "pwr.nl",
    "bus.nl",
    "port.nl",
    "cpu-mem.nl",
    "analog-audio.nl",
    "analog-col-t.nl",
    "ram-col-a.nl",
    "ram-row-w.nl",
]


# ============================================================================
# Data structures
# ============================================================================

@dataclass
class CellType:
    """Definition of a standard cell type from types.nl."""
    name: str               # e.g. "not_x1", "nand2", "dffr"
    color: str = ""         # visual category color
    inputs: list = field(default_factory=list)    # input pin names
    outputs: list = field(default_factory=list)   # output pin names (marked :out)
    tri_outputs: list = field(default_factory=list)  # tri-state outputs (:tri)
    inouts: list = field(default_factory=list)    # bidirectional pins (:inout)
    description: str = ""   # docstring
    is_registered: bool = False   # DFF or latch
    is_combinatorial: bool = False  # pure logic gate
    is_tristate: bool = False      # has tri-state outputs
    is_memory: bool = False        # RAM/ROM block
    is_pad: bool = False           # I/O pad
    drive_strength: int = 1        # relative drive strength (from _xN suffix)
    gate_equiv: int = 1    # equivalent gate count for delay estimation


@dataclass
class CellInstance:
    """A placed cell instance from the netlist."""
    name: str               # 4-char die name, e.g. "navo"
    cell_type: str          # type name, e.g. "nand6"
    orientation: str = ""   # rot0, rot90, etc.
    flip: bool = False
    bbox: tuple = ()        # (x1, y1, x2, y2) physical coordinates
    category: str = ""      # functional category, e.g. "ppu-dma"
    source_file: str = ""   # which .nl file
    is_spare: bool = False  # marked as spare
    is_trivial: bool = False  # marked as trivial


@dataclass
class Wire:
    """A wire connecting cell pins."""
    name: str               # wire name, e.g. "navo:ctl"
    signal_type: str = ""   # signal category: data, ctl, clk, rst, adr, etc.
    drivers: list = field(default_factory=list)    # list of "cell.pin" driving this wire
    sinks: list = field(default_factory=list)      # list of "cell.pin" receiving this wire
    route_coords: list = field(default_factory=list)  # physical routing paths
    source_file: str = ""


@dataclass
class Node:
    """Graph node for the dependency graph."""
    name: str
    node_type: str          # "combinatorial", "registered", "bus", "boundary", "pad"
    reg_type: str = ""      # specific DFF/latch type if registered
    source_file: str = ""
    source_line: int = 0
    gate_func: str = ""     # gate function
    state_path: str = ""
    comment: str = ""
    display_name: str = ""
    cell_type: str = ""     # full cell type name from schematics
    category: str = ""      # functional category
    drive_strength: int = 1
    bbox: tuple = ()        # physical coordinates
    gate_equiv: int = 1     # equivalent gate stages for delay


@dataclass
class Edge:
    src: str
    dst: str
    edge_type: str = "data"


# ============================================================================
# Cell type classification
# ============================================================================

# Cell types that are registered (clock-edge or level-sensitive storage)
REGISTERED_TYPES = {
    "dffr", "dffr_cc", "dffr_cc_q", "dffsr", "tffnl",
    "dlatch", "dlatch_ee", "dlatch_ee_q", "drlatch_ee",
    "nand_latch", "nor_latch",
}

# Cell types that are purely combinatorial
COMBINATORIAL_TYPES = {
    "not_x1", "not_x2", "not_x3", "not_x4", "not_x6",
    "nand2", "nand3", "nand4", "nand5", "nand6", "nand7",
    "eco_nand2",
    "nor2", "nor3", "nor4", "nor5", "nor6", "nor8",
    "and2", "and3", "and4",
    "or2", "or3", "or4",
    "xor", "xnor",
    "ao21", "ao22", "ao222", "ao2222", "ao222222",
    "oai21", "oa21",
    "muxi", "mux",
    "half_add", "full_add",
}

# Tri-state buffer types
TRISTATE_TYPES = {
    "not_if0", "not_if1", "buf_if0",
}

# Memory macro types
MEMORY_TYPES = {
    "wave_ram", "boot_rom", "high_ram", "oam",
}

# I/O pad types
PAD_TYPES = {
    "pad_bidir", "pad_bidir_pu", "pad_bidir_pu_latch",
    "pad_in", "pad_in_pu", "pad_out", "pad_out_diff",
    "pad_xtal", "pad_pass", "pad_pass_tg",
}

# Gate equivalents for delay estimation (how many gate delays this cell costs)
GATE_EQUIVALENTS = {
    "not_x1": 1, "not_x2": 1, "not_x3": 1, "not_x4": 1, "not_x6": 1,
    "nand2": 1, "nand3": 1, "nand4": 1, "nand5": 1, "nand6": 1, "nand7": 1,
    "eco_nand2": 1,
    "nor2": 1, "nor3": 1, "nor4": 1, "nor5": 1, "nor6": 1, "nor8": 1,
    "and2": 2, "and3": 2, "and4": 2,   # NAND + INV
    "or2": 2, "or3": 2, "or4": 2,      # NOR + INV
    "xor": 3, "xnor": 3,               # complex gate
    "ao21": 2, "ao22": 2, "ao222": 2, "ao2222": 2, "ao222222": 2,
    "oai21": 2, "oa21": 2,
    "muxi": 2, "mux": 3,               # muxi is inverting (one stage), mux is non-inverting
    "half_add": 3, "full_add": 4,
    "not_if0": 1, "not_if1": 1, "buf_if0": 2,
}

# Drive strength extracted from type name
def get_drive_strength(type_name: str) -> int:
    m = re.search(r'_x(\d+)$', type_name)
    return int(m.group(1)) if m else 1


# ============================================================================
# Parsing: types.nl
# ============================================================================

def parse_types(path: Path) -> dict:
    """Parse cell type definitions from types.nl. Returns dict of name -> CellType."""
    types = {}
    text = path.read_text()

    # Match type definitions - they span multiple lines ending with semicolon
    # Format: type name:color pin1 pin2:out ... @coords ... "description";
    # Some types have :-codegen prefix meaning they're analog/special
    current_type = None
    current_text = []

    for line in text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith('#'):
            continue

        if line_stripped.startswith('type'):
            if current_type and current_text:
                _finalize_type(types, current_type, ' '.join(current_text))
            current_type = line_stripped
            current_text = [line_stripped]
        elif line_stripped.startswith('signal '):
            # Signal type definitions at end of file
            if current_type and current_text:
                _finalize_type(types, current_type, ' '.join(current_text))
            current_type = None
            current_text = []
        elif current_type:
            current_text.append(line_stripped)

    if current_type and current_text:
        _finalize_type(types, current_type, ' '.join(current_text))

    return types


def _finalize_type(types: dict, first_line: str, full_text: str):
    """Parse a complete type definition into a CellType."""
    # Extract type name and color
    # Format: type name:color pins... or type:-codegen name pins...
    m = re.match(r'type(?::-codegen)?\s+(\S+)', first_line)
    if not m:
        return

    name_part = m.group(1)
    if ':' in name_part:
        name, color = name_part.split(':', 1)
    else:
        name = name_part
        color = ""

    ct = CellType(name=name, color=color)

    # Extract description from quotes
    desc_m = re.search(r'"([^"]*)"', full_text)
    if desc_m:
        ct.description = desc_m.group(1)

    # Extract pins from the first line (between name and first @)
    # Pins are words optionally followed by :out, :tri, :inout, :in, or :outN
    header = re.sub(r'@.*', '', full_text)  # remove coordinates
    header = re.sub(r'"[^"]*"', '', header)  # remove description
    header = re.sub(r';', '', header)  # remove semicolons

    # Skip the "type name:color" prefix
    pin_text = re.sub(r'^type(?::-codegen)?\s+\S+\s+', '', header).strip()

    for token in pin_text.split():
        # Skip coordinate annotations like rot0, flip, etc.
        if token.startswith('@') or token.startswith('"'):
            continue
        if ':' in token:
            pin_name, pin_dir = token.rsplit(':', 1)
            if pin_dir == 'out' or pin_dir.startswith('out'):
                ct.outputs.append(pin_name)
            elif pin_dir == 'tri':
                ct.tri_outputs.append(pin_name)
            elif pin_dir == 'inout':
                ct.inouts.append(pin_name)
            elif pin_dir == 'in':
                ct.inputs.append(pin_name)
            else:
                ct.inputs.append(token)  # unknown qualifier, treat as input
        else:
            ct.inputs.append(token)

    # Classify
    if name in REGISTERED_TYPES:
        ct.is_registered = True
    elif name in COMBINATORIAL_TYPES:
        ct.is_combinatorial = True
    elif name in TRISTATE_TYPES:
        ct.is_tristate = True
    elif name in MEMORY_TYPES:
        ct.is_memory = True
    elif name in PAD_TYPES:
        ct.is_pad = True

    ct.drive_strength = get_drive_strength(name)
    ct.gate_equiv = GATE_EQUIVALENTS.get(name, 1)

    types[name] = ct


# ============================================================================
# Parsing: categories.nl
# ============================================================================

def parse_categories(path: Path) -> dict:
    """Parse category definitions. Returns dict of name -> color."""
    categories = {}
    for line in path.read_text().split('\n'):
        m = re.match(r'category\s+(\S+)\s+:(\w+)\s*;', line)
        if m:
            categories[m.group(1)] = m.group(2)
    return categories


# ============================================================================
# Parsing: cell and wire definitions
# ============================================================================

def parse_netlist_file(path: Path, cell_types: dict) -> tuple:
    """Parse a single .nl file for cell instances and wire definitions.

    Returns (cells: list[CellInstance], wires: list[Wire])
    """
    cells = []
    wires = []
    text = path.read_text()
    lines = text.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        # Skip comments and blank lines
        if not stripped or stripped.startswith('#'):
            i += 1
            continue

        # Cell instance
        if stripped.startswith('cell '):
            cell = _parse_cell(stripped, str(path))
            if cell:
                cells.append(cell)
            i += 1
            continue

        # Wire definition (may span multiple lines)
        if stripped.startswith('wire '):
            wire, consumed = _parse_wire(lines, i, str(path))
            if wire:
                wires.append(wire)
            i += consumed
            continue

        i += 1

    return cells, wires


def _parse_cell(line: str, source_file: str) -> Optional[CellInstance]:
    """Parse a cell instance line.

    Format: cell name:type orient @x1,y1,x2,y2 [spare] [trivial] [->category];
    """
    # Match: cell name:type
    m = re.match(r'cell\s+(\w+):(\w+)', line)
    if not m:
        return None

    cell = CellInstance(
        name=m.group(1),
        cell_type=m.group(2),
        source_file=source_file,
    )

    # Orientation
    orient_m = re.search(r'\b(rot\d+(?:,flip)?)\b', line)
    if orient_m:
        orient = orient_m.group(1)
        cell.flip = ',flip' in orient
        cell.orientation = orient.replace(',flip', '')

    # Bounding box
    bbox_m = re.search(r'@(-?[\d.]+),(-?[\d.]+),(-?[\d.]+),(-?[\d.]+)', line)
    if bbox_m:
        cell.bbox = tuple(float(bbox_m.group(i)) for i in range(1, 5))

    # Category
    cat_m = re.search(r'->\s*(\S+)\s*;', line)
    if cat_m:
        cell.category = cat_m.group(1)

    # Spare/trivial flags
    cell.is_spare = 'spare' in line.split('#')[0]  # ignore comments
    cell.is_trivial = 'trivial' in line.split('#')[0]

    return cell


def _parse_wire(lines: list, start: int, source_file: str) -> tuple:
    """Parse a wire definition which may span multiple lines.

    Returns (Wire, num_lines_consumed).

    Wire format:
        wire name:signal_type
            driver1.pin driver2.pin ... -> sink1.pin sink2.pin ...
            @x1,y1,x2,y2,...
            @x1,y1,...

    Or single-line:
        wire name:signal_type driver.pin -> sink.pin;

    Or multi-driver bus:
        wire name:signal_type
            drv1.pin drv2.pin ...
            -> sink1.pin sink2.pin ...
    """
    first_line = lines[start].strip()

    # Handle commented-out wires: "# name.pin is not connected"
    if first_line.startswith('#'):
        return None, 1

    # Parse wire header
    m = re.match(r'wire\s+([^\s:]+)(?::(\w[\w-]*))?(?:\s+(.*))?', first_line)
    if not m:
        return None, 1

    wire_name = m.group(1)
    signal_type = m.group(2) or ""
    rest = (m.group(3) or "").rstrip(';').strip()

    wire = Wire(
        name=wire_name,
        signal_type=signal_type,
        source_file=source_file,
    )

    # Collect all connection/routing lines
    # A wire definition continues on indented lines (starting with tab or spaces)
    # or on the same line
    all_text = rest
    consumed = 1
    i = start + 1
    while i < len(lines):
        line = lines[i]
        if line and (line[0] == '\t' or (line[0] == ' ' and line.startswith('  '))):
            all_text += " " + line.strip().rstrip(';')
            consumed += 1
            i += 1
        else:
            break

    # Parse connections and coordinates from combined text
    # Split on @ to separate connection text from coordinates
    parts = all_text.split('@')
    connection_text = parts[0].strip()

    # Collect routing coordinates
    for coord_part in parts[1:]:
        coord_str = coord_part.strip().rstrip(';')
        if coord_str:
            wire.route_coords.append(coord_str)

    # Parse drivers and sinks from connection text
    # Format: driver1.pin driver2.pin -> sink1.pin sink2.pin
    if '->' in connection_text:
        driver_part, sink_part = connection_text.split('->', 1)
        wire.drivers = _parse_pin_refs(driver_part.strip())
        wire.sinks = _parse_pin_refs(sink_part.strip())
    else:
        # No explicit direction — all pins are connected (bus/short)
        # For multi-driver buses, everything before -> is a driver
        wire.drivers = _parse_pin_refs(connection_text)

    return wire, consumed


def _parse_pin_refs(text: str) -> list:
    """Parse pin references from connection text.

    Handles formats like:
        cell.pin
        cell.pin[N]
        cell.~pin
        cell.~{name}_suffix
    """
    refs = []
    if not text:
        return refs

    # Split on whitespace, each token is a pin reference
    for token in text.split():
        token = token.strip().rstrip(';')
        if not token or token.startswith('@') or token.startswith('"'):
            continue
        # Should contain a dot for cell.pin
        if '.' in token:
            refs.append(token)
    return refs


# ============================================================================
# Graph construction
# ============================================================================

def build_graph(cell_types: dict, cells: list, wires: list):
    """Build a signal dependency graph from parsed cells and wires.

    Each cell becomes one or more nodes:
    - Combinatorial cells: one node (gate output)
    - Registered cells: one node (register output = clock boundary)
    - Tri-state cells: one node

    Wires create edges from driver cell outputs to sink cell inputs.
    """
    nodes = {}
    edges = []

    # Index cells by name
    cell_index = {}
    for cell in cells:
        cell_index[cell.name] = cell

    # Create nodes for each cell
    for cell in cells:
        if cell.is_spare or cell.is_trivial:
            continue

        ct = cell_types.get(cell.cell_type)
        if not ct:
            # Unknown type — skip virtual/special cells
            if cell.cell_type in ('port', 'tie'):
                continue
            continue

        # Skip memory macros and analog blocks — they're black boxes
        if ct.is_memory or cell.cell_type.startswith('amp') or cell.cell_type in ('dac', 'mixer', 'rv', 'vdiv'):
            # Create a boundary node for memory I/O
            node = Node(
                name=cell.name,
                node_type="boundary",
                display_name=cell.name,
                cell_type=cell.cell_type,
                category=cell.category,
                source_file=cell.source_file,
                bbox=cell.bbox,
                comment=f"Memory/analog: {ct.description}" if ct else "",
            )
            nodes[cell.name] = node
            continue

        if ct.is_pad:
            node = Node(
                name=cell.name,
                node_type="pad",
                display_name=cell.name,
                cell_type=cell.cell_type,
                category=cell.category,
                source_file=cell.source_file,
                bbox=cell.bbox,
                comment=f"I/O pad: {ct.description}" if ct else "",
            )
            nodes[cell.name] = node
            continue

        # Determine node type
        if ct.is_registered:
            node_type = "registered"
            reg_type = cell.cell_type
        elif ct.is_combinatorial or ct.is_tristate:
            node_type = "combinatorial"
            reg_type = ""
        else:
            node_type = "combinatorial"
            reg_type = ""

        node = Node(
            name=cell.name,
            node_type=node_type,
            reg_type=reg_type,
            display_name=cell.name,
            cell_type=cell.cell_type,
            category=cell.category,
            source_file=cell.source_file,
            bbox=cell.bbox,
            gate_func=cell.cell_type,
            drive_strength=ct.drive_strength,
            gate_equiv=ct.gate_equiv,
        )
        nodes[cell.name] = node

    # Process wires to create edges
    # A wire connects drivers (cell outputs) to sinks (cell inputs).
    #
    # For multi-driver wires (shared buses like the 8-bit data bus), we create
    # an intermediate BUS node. This avoids O(n*m) cross-product edges while
    # preserving real paths: driver -> bus_node -> sink. The bus node is marked
    # as node_type="bus" so the analysis can track bus-mediated paths separately
    # from direct combinatorial chains.
    for wire in wires:
        driver_refs = []  # (cell_name, pin_ref)
        sink_refs = []    # (cell_name, pin_ref)

        for pin_ref in wire.drivers:
            cell_name = _extract_cell_name(pin_ref)
            if cell_name and cell_name in nodes:
                driver_refs.append((cell_name, pin_ref))

        for pin_ref in wire.sinks:
            cell_name = _extract_cell_name(pin_ref)
            if cell_name and cell_name in nodes:
                sink_refs.append((cell_name, pin_ref))

        driver_cells = {c for c, _ in driver_refs}
        sink_cells = {c for c, _ in sink_refs}

        # Determine base edge type from signal type
        edge_type = "data"
        if wire.signal_type == "clk":
            edge_type = "clock"
        elif wire.signal_type == "rst":
            edge_type = "reset"

        # For multi-driver wires, create an intermediate bus node
        if len(driver_cells) > 1 and sink_cells:
            bus_node_name = f"bus:{wire.name}"
            if bus_node_name not in nodes:
                nodes[bus_node_name] = Node(
                    name=bus_node_name,
                    node_type="bus",
                    display_name=wire.name,
                    category="bus",
                    gate_func="bus",
                    comment=f"Shared bus: {len(driver_cells)} drivers, {len(sink_cells)} sinks",
                )

            # Connect each driver to the bus node
            for drv in driver_cells:
                if drv == bus_node_name:
                    continue
                edges.append(Edge(src=drv, dst=bus_node_name, edge_type="data"))

            # Connect bus node to each sink
            for snk in sink_cells:
                if snk == bus_node_name:
                    continue
                snk_edge_type = _pin_edge_type(snk, wire.sinks, edge_type)
                edges.append(Edge(src=bus_node_name, dst=snk, edge_type=snk_edge_type))
        else:
            # Single-driver wire: direct edges
            for drv in driver_cells:
                for snk in sink_cells:
                    if drv == snk:
                        continue
                    snk_edge_type = _pin_edge_type(snk, wire.sinks, edge_type)
                    edges.append(Edge(src=drv, dst=snk, edge_type=snk_edge_type))

    return nodes, edges


def _pin_edge_type(sink_cell: str, sink_pin_refs: list, default_type: str) -> str:
    """Determine edge type based on the destination pin name."""
    for pin_ref in sink_pin_refs:
        if _extract_cell_name(pin_ref) == sink_cell:
            pin_name = _extract_pin_name(pin_ref)
            if pin_name in ('clk', '~clk', '~tclk'):
                return "clock"
            elif pin_name in ('ena', '~ena'):
                return "clock"
            elif pin_name in ('~r', '~s', 'r', 's'):
                return "reset"
    return default_type


def _extract_cell_name(pin_ref: str) -> Optional[str]:
    """Extract cell name from a pin reference like 'navo.y' or 'cpu.d[0]'."""
    if '.' not in pin_ref:
        return None
    return pin_ref.split('.')[0]


def _extract_pin_name(pin_ref: str) -> str:
    """Extract pin name from a pin reference like 'navo.y' or 'nybo.~s'."""
    if '.' not in pin_ref:
        return ""
    return pin_ref.split('.', 1)[1]


# ============================================================================
# Wire length estimation
# ============================================================================

def estimate_wire_length(wire: Wire) -> float:
    """Estimate total wire length from routing coordinates.

    Coordinates are Manhattan-routed paths: x1,y1,x2,y2,...
    Returns total wire length in die coordinate units.
    """
    total = 0.0
    for route in wire.route_coords:
        coords = []
        for c in route.split(','):
            c = c.strip()
            if c:
                try:
                    coords.append(float(c))
                except ValueError:
                    continue
        # Pairs of (x, y) coordinates forming path segments
        if len(coords) < 4 or len(coords) % 2 != 0:
            continue
        for i in range(0, len(coords) - 2, 2):
            x1, y1 = coords[i], coords[i+1]
            x2, y2 = coords[i+2], coords[i+3]
            total += abs(x2 - x1) + abs(y2 - y1)
    return total


# ============================================================================
# Post-processing: dedup edges, compute stats
# ============================================================================

def dedup_edges(edges: list) -> list:
    """Remove duplicate edges, keeping the most specific edge_type."""
    seen = {}
    for e in edges:
        key = (e.src, e.dst)
        if key not in seen:
            seen[key] = e
        else:
            # Prefer clock/reset over data
            if e.edge_type in ("clock", "reset"):
                seen[key] = e
    return list(seen.values())


# ============================================================================
# Export
# ============================================================================

def export_graph_json(nodes: dict, edges: list, cell_types: dict) -> dict:
    """Export graph as JSON for the web viewer."""
    node_list = []
    for n in nodes.values():
        entry = {
            "name": n.name,
            "display_name": n.display_name,
            "node_type": n.node_type,
            "reg_type": n.reg_type,
            "source_file": n.source_file,
            "source_line": n.source_line,
            "gate_func": n.gate_func,
            "state_path": n.state_path,
            "comment": n.comment,
            "cell_type": n.cell_type,
            "category": n.category,
            "drive_strength": n.drive_strength,
            "gate_equiv": n.gate_equiv,
        }
        if n.bbox:
            entry["bbox"] = list(n.bbox)
        node_list.append(entry)

    edge_list = []
    for e in edges:
        edge_list.append({
            "src": e.src,
            "dst": e.dst,
            "edge_type": e.edge_type,
        })

    return {"nodes": node_list, "edges": edge_list}


# ============================================================================
# Statistics
# ============================================================================

def print_stats(nodes: dict, edges: list, cells: list, wires: list, cell_types: dict):
    """Print extraction statistics."""
    print(f"\n{'='*60}")
    print("DMG-CPU B Netlist — Extraction Statistics")
    print(f"{'='*60}\n")

    # Cell counts
    total_cells = len(cells)
    by_type = {}
    for c in cells:
        ct_name = c.cell_type
        by_type[ct_name] = by_type.get(ct_name, 0) + 1
    print(f"Total cell instances parsed: {total_cells}")
    print(f"Unique cell types used: {len(by_type)}")

    # Node counts by type
    type_counts = {}
    for n in nodes.values():
        type_counts[n.node_type] = type_counts.get(n.node_type, 0) + 1
    print(f"\nGraph nodes: {len(nodes)}")
    for nt, count in sorted(type_counts.items()):
        print(f"  {nt}: {count}")

    print(f"\nGraph edges: {len(edges)}")
    edge_type_counts = {}
    for e in edges:
        edge_type_counts[e.edge_type] = edge_type_counts.get(e.edge_type, 0) + 1
    for et, count in sorted(edge_type_counts.items()):
        print(f"  {et}: {count}")

    # Category breakdown
    cat_counts = {}
    for n in nodes.values():
        cat = n.category or "(uncategorized)"
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    print(f"\nNodes by category:")
    ppu_total = 0
    for cat, count in sorted(cat_counts.items()):
        marker = " *" if cat.startswith("ppu-") else ""
        if cat.startswith("ppu-"):
            ppu_total += count
        print(f"  {cat}: {count}{marker}")
    print(f"  PPU total: {ppu_total}")

    # Wire statistics
    print(f"\nTotal wires parsed: {len(wires)}")
    wire_lengths = []
    for w in wires:
        length = estimate_wire_length(w)
        if length > 0:
            wire_lengths.append(length)
    if wire_lengths:
        print(f"Wires with routing data: {len(wire_lengths)}")
        print(f"Wire length range: {min(wire_lengths):.1f} — {max(wire_lengths):.1f} units")
        print(f"Median wire length: {sorted(wire_lengths)[len(wire_lengths)//2]:.1f} units")

    # Drive strength distribution
    strength_counts = {}
    for n in nodes.values():
        if n.node_type == "combinatorial":
            ds = n.drive_strength
            strength_counts[ds] = strength_counts.get(ds, 0) + 1
    if strength_counts:
        print(f"\nDrive strength distribution (combinatorial gates):")
        for ds, count in sorted(strength_counts.items()):
            print(f"  x{ds}: {count}")

    print()


# ============================================================================
# Critical Path Analysis
# ============================================================================

def build_networkx_graph(nodes: dict, edges: list):
    """Build a NetworkX directed graph from parsed nodes and edges."""
    import networkx as nx

    G = nx.DiGraph()
    for n in nodes.values():
        G.add_node(n.name, **{
            'node_type': n.node_type,
            'reg_type': n.reg_type,
            'display_name': n.display_name,
            'gate_func': n.gate_func,
            'cell_type': n.cell_type,
            'category': n.category,
            'drive_strength': n.drive_strength,
            'gate_equiv': n.gate_equiv,
            'source_file': n.source_file,
            'source_line': n.source_line,
            'comment': n.comment,
        })
        if n.bbox:
            G.nodes[n.name]['bbox'] = list(n.bbox)

    for e in edges:
        if e.src in G and e.dst in G:
            G.add_edge(e.src, e.dst, edge_type=e.edge_type)

    return G


def is_path_terminator(G, node_name):
    """Check if a node terminates a combinatorial path (registered/bus/boundary/pad)."""
    nt = G.nodes[node_name].get('node_type', '')
    return nt in ('registered', 'bus', 'boundary', 'pad')


def compute_depths(G):
    """Compute longest combinatorial depth to each node without building a DAG.

    Registered/bus/boundary/pad nodes have depth 0 (they're path boundaries).
    Combinatorial nodes get depth = max(predecessor depths) + gate_equiv.

    Uses iterative relaxation with cycle detection: if a node appears in its
    own predecessor path, that's a combinatorial feedback loop and we skip it.
    This handles SR latch feedback and other cycles without needing to remove
    edges from the graph.
    """
    depth = {}
    path = {}

    for n in G.nodes():
        if is_path_terminator(G, n):
            depth[n] = 0
            path[n] = [n]
        else:
            depth[n] = -1
            path[n] = []

    changed = True
    iterations = 0
    while changed and iterations < 50:
        changed = False
        iterations += 1
        for n in G.nodes():
            if is_path_terminator(G, n):
                continue

            best_d = -1
            best_path = []
            for pred in G.predecessors(n):
                edge_data = G.edges[pred, n]
                if edge_data.get('edge_type') in ('clock', 'reset'):
                    continue
                pd = depth.get(pred, -1)
                pp = path.get(pred, [])
                # Skip if this would create a cycle (n is already in the path)
                if n in pp:
                    continue
                if pd > best_d:
                    best_d = pd
                    best_path = pp

            if best_d >= 0:
                ge = G.nodes[n].get('gate_equiv', 1)
                new_d = best_d + ge
                if new_d > depth[n]:
                    depth[n] = new_d
                    path[n] = best_path + [n]
                    changed = True

    return depth, path


def find_critical_paths(G):
    """Find longest combinatorial paths between registered nodes.

    Uses iterative depth computation on the original graph — no DAG needed.
    """
    depth, path = compute_depths(G)

    # Collect paths terminating at registered sinks
    paths = []
    for n in G.nodes():
        if not is_path_terminator(G, n):
            continue
        for pred in G.predecessors(n):
            edge_data = G.edges[pred, n]
            if edge_data.get('edge_type') in ('clock', 'reset'):
                continue
            d = depth.get(pred, 0)
            p = path.get(pred, [])
            if d >= 1:
                paths.append((d, p + [n]))

    paths.sort(key=lambda x: -x[0])

    # Deduplicate by (start, end, depth)
    seen = set()
    unique = []
    for d, p in paths:
        key = (p[0], p[-1], d)
        if key not in seen:
            seen.add(key)
            unique.append((d, p))
    return unique


def find_race_pairs(G):
    """Find signal races: registered nodes where inputs arrive at different depths.

    Considers ALL predecessor edges (data, clock, reset) for race detection,
    because the race is between ANY inputs that must settle before the register
    captures. For example, a latch's enable signal (classified as 'clock')
    races against its data input.
    """
    depth, _ = compute_depths(G)

    races = []
    for n in G.nodes():
        if not is_path_terminator(G, n):
            continue

        preds = list(G.predecessors(n))

        if len(preds) < 2:
            continue

        pred_depths = [(p, depth.get(p, 0)) for p in preds]
        pred_depths.sort(key=lambda x: -x[1])

        max_d = pred_depths[0][1]
        min_d = pred_depths[-1][1]
        diff = max_d - min_d

        if diff >= 3 and max_d >= 4:
            races.append({
                'node': n,
                'display_name': n,
                'node_type': G.nodes[n].get('node_type', ''),
                'reg_type': G.nodes[n].get('reg_type', ''),
                'cell_type': G.nodes[n].get('cell_type', ''),
                'category': G.nodes[n].get('category', ''),
                'source_file': G.nodes[n].get('source_file', ''),
                'depth_diff': diff,
                'max_depth': max_d,
                'min_depth': min_d,
                'inputs': [
                    {
                        'name': p,
                        'depth': d,
                        'gate_func': G.nodes[p].get('gate_func', ''),
                        'cell_type': G.nodes[p].get('cell_type', ''),
                        'node_type': G.nodes[p].get('node_type', ''),
                        'category': G.nodes[p].get('category', ''),
                    }
                    for p, d in pred_depths
                ],
            })

    races.sort(key=lambda x: (-x['depth_diff'], -x['max_depth']))
    return races


CATEGORY_DISPLAY = {
    'ppu-bgfifo': 'BG Pixel Shifter',
    'ppu-bgscroll': 'BG Scrolling',
    'ppu-control': 'PPU Control',
    'ppu-cycles': 'BG/Win Cycles',
    'ppu-decode': 'PPU Decode',
    'ppu-dma': 'DMA',
    'ppu-lcd': 'LCD Output',
    'ppu-mux': 'Pixel Mux',
    'ppu-oam': 'OAM Interface',
    'ppu-objctl': 'Sprite Control',
    'ppu-objfifo': 'Sprite Pixel Shifter',
    'ppu-objreg': 'Sprite Store',
    'ppu-pal': 'Palettes',
    'ppu-stat': 'STAT/LY',
    'ppu-vram': 'VRAM Interface',
    'ppu-window': 'Window Logic',
    'ppu-xcomp': 'Sprite X Match',
    'ppu-xprio': 'Sprite X Priority',
    'ppu-ycomp': 'Sprite Y Compare',
    'clocks': 'Clock Distribution',
    'int': 'Interrupts',
    'timer': 'Timer',
    'bus-adr': 'Address Bus',
    'bus-data': 'Data Bus',
    'serial': 'Serial',
    'joypad': 'Joypad',
    'sys-decode': 'System Decode',
}


def categorize_by_schematic(path, G):
    """Categorize a path using the schematic category annotations."""
    # Use sink category primarily
    sink_cat = G.nodes[path[-1]].get('category', '')
    if sink_cat:
        return CATEGORY_DISPLAY.get(sink_cat, sink_cat)
    # Fall back to source category
    src_cat = G.nodes[path[0]].get('category', '')
    if src_cat:
        return CATEGORY_DISPLAY.get(src_cat, src_cat)
    # Check intermediate nodes
    for node in path:
        cat = G.nodes[node].get('category', '')
        if cat:
            return CATEGORY_DISPLAY.get(cat, cat)
    return 'Other'


def is_reset_path_schematic(path, G):
    """Check if a path is reset-only (not operational during normal rendering).

    Uses the schematic category and reset edge types to identify paths
    that only fire on LCDC toggle or system reset.
    """
    # Check if path passes through known reset infrastructure
    reset_count = 0
    for node in path:
        cat = G.nodes[node].get('category', '')
        # Check if incoming edges to this node are reset type
        for _, _, edata in G.in_edges(node, data=True):
            if edata.get('edge_type') == 'reset':
                reset_count += 1
    # Path dominated by reset signals
    if reset_count >= 3:
        return True
    # Check if source is in clocks/reset category
    src_cat = G.nodes[path[0]].get('category', '')
    if src_cat == 'clocks' and reset_count >= 1:
        return True
    return False


def export_paths_json(paths, G, races=None):
    """Export critical paths and races in format compatible with build_explorer.py."""
    HALF_TCYCLE_NS = 119.2
    GATE_DELAY_MIN = 5   # ns
    GATE_DELAY_MAX = 15  # ns

    path_list = []
    for depth, path in paths:
        min_ns = depth * GATE_DELAY_MIN
        max_ns = depth * GATE_DELAY_MAX
        pct = max_ns / HALF_TCYCLE_NS * 100

        path_nodes = []
        for n in path:
            nd = G.nodes.get(n, {})
            path_nodes.append({
                'name': n,
                'display_name': n,
                'node_type': nd.get('node_type', ''),
                'gate_func': nd.get('gate_func', ''),
                'cell_type': nd.get('cell_type', ''),
                'category': nd.get('category', ''),
                'drive_strength': nd.get('drive_strength', 1),
                'gate_equiv': nd.get('gate_equiv', 1),
                'fan_out': G.out_degree(n),
            })

        path_list.append({
            'depth': depth,
            'min_delay_ns': min_ns,
            'max_delay_ns': max_ns,
            'pct_half_tcycle': round(pct, 1),
            'source': path[0],
            'sink': path[-1],
            'is_reset': is_reset_path_schematic(path, G),
            'category': categorize_by_schematic(path, G),
            'nodes': path_nodes,
        })

    return path_list


# ============================================================================
# Report Generation
# ============================================================================

def format_report(paths, G, races):
    """Generate markdown report sections."""
    HALF_TCYCLE_NS = 119.2
    fanout = {n: G.out_degree(n) for n in G.nodes()}

    reset_paths = [(d, p) for d, p in paths if is_reset_path_schematic(p, G)]
    op_paths = [(d, p) for d, p in paths if not is_reset_path_schematic(p, G)]

    sections = {}

    # === Overview ===
    lines = []
    lines.append("# Game Boy (DMG-CPU B) Propagation Path Analysis")
    lines.append("")
    lines.append("Static analysis of the DMG-CPU B gate-level netlist from")
    lines.append("[msinger/dmg-schematics](https://github.com/msinger/dmg-schematics),")
    lines.append("identifying deep combinatorial paths that cause propagation delays")
    lines.append("on real Game Boy hardware.")
    lines.append("")
    lines.append("## Source Data")
    lines.append("")
    lines.append("This analysis uses the corrected die-traced netlists from the")
    lines.append("dmg-schematics project, which contain fixes not present in the")
    lines.append("original DMG-CPU-Inside schematics. Key advantages over behavioral")
    lines.append("simulator analysis:")
    lines.append("- Ground-truth cell types with drive strength (x1 through x6)")
    lines.append("- Physical cell coordinates and wire routing for delay estimation")
    lines.append("- Gate-equivalent depth counting (AND=2, MUX=3, XOR=3, etc.)")
    lines.append("- Explicit clock/reset/enable pin classification")
    lines.append("")
    lines.append("## Timing Reference")
    lines.append("")
    lines.append("- Game Boy master clock: 4.194304 MHz")
    lines.append("- T-cycle period: ~238.4 ns (one dot)")
    lines.append("- Half T-cycle: ~119.2 ns")
    lines.append("- Estimated gate delay (Sharp SM83 CMOS, ~5 um): 5-15 ns per gate")
    lines.append("- Depths use gate-equivalent counting (NOT=1, AND/OR=2, MUX=3, XOR=3)")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append("| Category | Count | Max Depth | Worst-case Delay |")
    lines.append("|----------|-------|-----------|-----------------|")
    op_max = op_paths[0][0] if op_paths else 0
    rst_max = reset_paths[0][0] if reset_paths else 0
    lines.append(f"| **Operational** (per-dot/scanline) | {len(op_paths)} | {op_max} | {op_max*15} ns ({op_max*15/HALF_TCYCLE_NS*100:.0f}% half T-cycle) |")
    lines.append(f"| Reset-only | {len(reset_paths)} | {rst_max} | {rst_max*15} ns |")
    lines.append(f"| **Total** | {len(paths)} | {paths[0][0] if paths else 0} | |")
    lines.append("")
    sections['critical_paths_report.md'] = '\n'.join(lines)

    # === Operational paths by category ===
    lines = []
    lines.append("# Operational Critical Paths by Functional Area\n")
    by_cat = {}
    for d, p in op_paths:
        cat = categorize_by_schematic(p, G)
        if cat not in by_cat:
            by_cat[cat] = []
        by_cat[cat].append((d, p))

    for cat in sorted(by_cat, key=lambda c: -by_cat[c][0][0]):
        cat_paths = by_cat[cat]
        lines.append(f"\n## {cat} ({len(cat_paths)} paths, max depth {cat_paths[0][0]})\n")
        for i, (depth, path) in enumerate(cat_paths[:10]):
            min_ns = depth * 5
            max_ns = depth * 15
            pct = max_ns / HALF_TCYCLE_NS * 100
            lines.append(f"### Path {i+1}: depth {depth} ({min_ns}-{max_ns} ns, {pct:.0f}% half T-cycle)")
            lines.append("```")
            for j, node in enumerate(path):
                nd = G.nodes.get(node, {})
                ct = nd.get('cell_type', '')
                cat_n = nd.get('category', '')
                ds = nd.get('drive_strength', 1)
                ge = nd.get('gate_equiv', 1)
                fo = fanout.get(node, 0)
                nt = nd.get('node_type', '')
                if nt in ('registered', 'bus', 'boundary', 'pad'):
                    marker = f"[{nt.upper()}:{ct}]"
                else:
                    marker = f"[{ct}]"
                ds_str = f" x{ds}" if ds > 1 else ""
                fo_str = f" fan-out={fo}" if fo >= 10 else ""
                lines.append(f"{'  ' * j}{marker} {node} ({cat_n}){ds_str}{fo_str}")
            lines.append("```\n")
    sections['operational_paths.md'] = '\n'.join(lines)

    # === Race pairs ===
    lines = []
    lines.append("# Signal Race Pair Analysis\n")
    lines.append(f"Total race pairs identified: {len(races)}\n")
    lines.append("Race pairs are registered nodes where data inputs arrive at significantly")
    lines.append("different combinatorial depths (diff >= 3 gates, max >= 4). On real hardware,")
    lines.append("the late-arriving signal may not settle before the register samples, causing")
    lines.append("behavior to differ from behavioral emulation by one dot.\n")

    # Group by category
    race_by_cat = {}
    for r in races:
        cat = CATEGORY_DISPLAY.get(r['category'], r['category'] or 'Other')
        if cat not in race_by_cat:
            race_by_cat[cat] = []
        race_by_cat[cat].append(r)

    ppu_races = 0
    for r in races:
        if r.get('category', '').startswith('ppu-'):
            ppu_races += 1
    lines.append(f"PPU-related races: {ppu_races}\n")

    for cat in sorted(race_by_cat, key=lambda c: -max(r['depth_diff'] for r in race_by_cat[c])):
        cat_races = race_by_cat[cat]
        lines.append(f"\n## {cat} ({len(cat_races)} races)\n")
        for r in cat_races[:15]:
            lines.append(f"### `{r['display_name']}` ({r['cell_type']}) — diff={r['depth_diff']}, max={r['max_depth']}")
            lines.append(f"Category: {r['category']}\n")
            lines.append("| Input | Depth | Type | Category |")
            lines.append("|-------|-------|------|----------|")
            for inp in r['inputs']:
                lines.append(f"| `{inp['name']}` | {inp['depth']} | {inp['cell_type']} | {inp.get('category','')} |")
            lines.append("")
    sections['race_pairs_report.md'] = '\n'.join(lines)

    # === Reset paths ===
    lines = []
    lines.append("# Reset-Only Paths\n")
    lines.append(f"Total: {len(reset_paths)} paths (max depth {rst_max})\n")
    lines.append("These paths only fire on LCDC toggle or system reset, not during")
    lines.append("normal per-dot rendering.\n")
    for i, (depth, path) in enumerate(reset_paths[:20]):
        cat = categorize_by_schematic(path, G)
        lines.append(f"### Path {i+1}: depth {depth} — {cat}")
        lines.append(f"`{path[0]}` → `{path[-1]}`\n")
    sections['reset_paths.md'] = '\n'.join(lines)

    return sections


# ============================================================================
# Main
# ============================================================================

def main():
    if not NETLIST_DIR.exists():
        print(f"Error: Netlist directory not found: {NETLIST_DIR}")
        print("Make sure dmg-schematics submodule is initialized:")
        print("  git submodule update --init")
        sys.exit(1)

    # Step 1: Parse cell type definitions
    print("Parsing cell types...")
    cell_types = parse_types(NETLIST_DIR / "types.nl")
    print(f"  {len(cell_types)} cell types defined")

    # Step 2: Parse categories
    categories = parse_categories(NETLIST_DIR / "categories.nl")
    print(f"  {len(categories)} functional categories")

    # Step 3: Parse all cell instances and wires
    all_cells = []
    all_wires = []

    # Top-level files
    for fname in TOP_LEVEL_FILES:
        fpath = NETLIST_DIR / fname
        if fpath.exists():
            cells, wires = parse_netlist_file(fpath, cell_types)
            all_cells.extend(cells)
            all_wires.extend(wires)
            print(f"  {fname}: {len(cells)} cells, {len(wires)} wires")

    # Subdirectory files
    for dirname in CELL_DIRS:
        dirpath = NETLIST_DIR / dirname
        if not dirpath.exists():
            continue
        for fpath in sorted(dirpath.glob("*.nl")):
            cells, wires = parse_netlist_file(fpath, cell_types)
            all_cells.extend(cells)
            all_wires.extend(wires)
            print(f"  {dirname}/{fpath.name}: {len(cells)} cells, {len(wires)} wires")

    # Step 4: Build the graph
    print("\nBuilding signal dependency graph...")
    nodes, edges = build_graph(cell_types, all_cells, all_wires)
    edges = dedup_edges(edges)

    # Step 5: Statistics
    print_stats(nodes, edges, all_cells, all_wires, cell_types)

    # Step 6: Build NetworkX graph and run analysis
    print("Building NetworkX graph...")
    G = build_networkx_graph(nodes, edges)
    print(f"  {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    print("Computing combinatorial depths...")
    depth, _ = compute_depths(G)
    max_depth = max(depth.values())
    print(f"  Max depth: {max_depth} gate-equivalents")

    print("Finding critical paths...")
    paths = find_critical_paths(G)
    print(f"  {len(paths)} critical paths found")
    if paths:
        print(f"  Deepest: {paths[0][0]} gate-equivalents")
        op_paths = [(d, p) for d, p in paths if not is_reset_path_schematic(p, G)]
        rst_paths = [(d, p) for d, p in paths if is_reset_path_schematic(p, G)]
        print(f"  Operational: {len(op_paths)} (max depth {op_paths[0][0] if op_paths else 0})")
        print(f"  Reset-only: {len(rst_paths)} (max depth {rst_paths[0][0] if rst_paths else 0})")

    print("Finding signal race pairs...")
    races = find_race_pairs(G)
    print(f"  {len(races)} race pairs found")
    ppu_races = [r for r in races if r.get('category', '').startswith('ppu-')]
    print(f"  PPU-related: {len(ppu_races)}")

    # Step 7: Export
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Graph JSON
    graph_data = export_graph_json(nodes, edges, cell_types)
    with open(output_dir / "ppu_graph.json", 'w') as f:
        json.dump(graph_data, f, indent=2)
    print(f"\nExported: ppu_graph.json ({len(graph_data['nodes'])} nodes, {len(graph_data['edges'])} edges)")

    # Critical paths JSON
    paths_data = export_paths_json(paths, G, races)
    with open(output_dir / "critical_paths.json", 'w') as f:
        json.dump(paths_data, f, indent=2)
    print(f"Exported: critical_paths.json ({len(paths_data)} paths)")

    # Race pairs JSON
    with open(output_dir / "race_pairs.json", 'w') as f:
        json.dump(races, f, indent=2)
    print(f"Exported: race_pairs.json ({len(races)} races)")

    # Markdown reports
    sections = format_report(paths, G, races)
    for fname, content in sections.items():
        with open(output_dir / f"{fname}", 'w') as f:
            f.write(content)
        print(f"Exported: {fname}")



if __name__ == "__main__":
    main()
