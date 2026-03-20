#!/usr/bin/env python3
"""
Game Boy PPU Combinatorial Path Analysis — Parser & Graph Builder

Extracts a signal dependency graph from the GateBoy gate-level simulator source.
Identifies registered (clocked) vs combinatorial nodes and builds a directed graph
suitable for critical path analysis.

Key design decisions:
- Wire/triwire local variables are scoped by source file ("file_stem:WIRE_NAME")
  because 726+ wire names appear in multiple files. Without scoping, the last
  definition wins and cross-file edges silently connect to the wrong node.
- Nodes from reg_new paths (DFF updates, gate assigns, bus writes, sig_in/sig_out)
  are global since their names come from unique state struct field names.
- Computed methods (GateBoyState.cpp, GateBoyCpuBus.cpp, GateBoyPins.cpp) are
  parsed as gate chains with the method name as a global combinatorial node.
"""

import re
import json
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# ============================================================================
# Configuration
# ============================================================================

GATEBOY_SRC = Path("metroboy/src/GateBoyLib")

# Files to parse — all gate logic files (PPU + system integration)
GATE_FILES = [
    "GateBoy.cpp",           # Main tock_gates() — bulk of the logic
    "GateBoyLCD.cpp",        # LY, LYC match, LCD timing
    "GateBoyPixPipe.cpp",    # Pixel pipelines, window logic
    "GateBoyTileFetcher.cpp",
    "GateBoySpriteFetcher.cpp",
    "GateBoySpriteScanner.cpp",
    "GateBoySpriteStore.cpp",
    "GateBoyRegisters.cpp",  # LCDC, STAT, palette regs
    "GateBoyClocks.cpp",     # Clock generation
    "GateBoyDMA.cpp",        # DMA (shares OAM bus)
    "GateBoyInterrupts.cpp", # STAT/VBlank interrupts
    "GateBoyCpuBus.cpp",     # CPU bus, bootrom
    "GateBoyVramBus.cpp",    # VRAM bus
    "GateBoyOamBus.cpp",     # OAM bus
    "GateBoyTimer.cpp",      # DIV, TIMA
    "GateBoyReset.cpp",      # Reset logic
    "GateBoyJoypad.cpp",     # Joypad (minimal PPU relevance)
    "GateBoySerial.cpp",     # Serial (minimal PPU relevance)
    "GateBoyExtBus.cpp",     # External bus
    "GateBoyPins.cpp",       # Pin logic
]

# Additional files with computed methods (parsed separately)
COMPUTED_METHOD_FILES = [
    "GateBoyState.cpp",
    "GateBoyCpuBus.cpp",
    "GateBoyPins.cpp",
]

# Gate functions — these are combinatorial
GATE_FUNCTIONS = {
    "not1", "and2", "and3", "and4", "and5", "and6", "and7",
    "or2", "or3", "or4", "or5", "or6",
    "nor2", "nor3", "nor4", "nor5", "nor6", "nor8",
    "nand2", "nand3", "nand4", "nand5", "nand6", "nand7",
    "xor2", "xnor2",
    "mux2p", "mux2n",
    "amux2", "amux3", "amux4", "amux6",
    "and_or3", "or_and3", "not_or_and3",
    "add3",
    "tri6_nn", "tri6_pn", "tri10_np", "tri_pp",
}

# DFF/latch methods — these indicate registered (clocked) elements
REGISTERED_METHODS = {
    "dff", "dff8", "dff9", "dff11", "dff13",
    "dff17", "dff17_any", "dff17_clk", "dff17_rst",
    "dff20", "dff20_any", "dff20_clk", "dff20_async",
    "dff22", "dff22_any", "dff22_sync", "dff22_async",
    "dff_r", "dff_pp",
    "nor_latch", "nand_latch",
    "tp_latchn", "tp_latchp",
}

# Bus methods
BUS_METHODS = {"tri_bus"}

# Signal output accessors — map back to registered source
OUTPUT_ACCESSORS = {
    "qp_old", "qn_old", "qp_new", "qn_new",
    "qp_mid", "qn_mid", "qp_any", "qn_any",
    "out_old", "out_new", "out_any", "out_mid",
    "qp_int_old", "qp_int_new", "qp_int_any",
    "qp_ext_old", "qp_ext_new", "qn_ext_new",
}

# Methods to skip when matching computed method calls
SKIP_METHODS = (
    REGISTERED_METHODS | BUS_METHODS |
    {'hold', 'sig_in', 'sig_out', 'set_data', 'set_addr', 'pin_in',
     'pin_out', 'pin_io', 'pin_io_any', 'pin_clk', 'rst', 'set',
     'clkgood_new', 'clkgood_old', 'clk_new', 'clk_old',
     'reset', 'poweron', 'check_old', 'check_new'}
)


# ============================================================================
# Data structures
# ============================================================================

@dataclass
class Node:
    name: str                          # Signal name (e.g., PALY_LY_MATCHa_old)
    node_type: str                     # "combinatorial", "registered", "bus", "boundary", "gate_output"
    reg_type: str = ""                 # DFF type if registered (dff9, dff17, etc.)
    source_file: str = ""
    source_line: int = 0
    gate_func: str = ""                # Gate function if combinatorial (not1, and2, etc.)
    state_path: str = ""               # Full path in GateBoyState if applicable
    comment: str = ""                  # Die page reference comment
    display_name: str = ""             # Short name for display (without file scope prefix)


@dataclass
class Edge:
    src: str    # source signal name
    dst: str    # destination signal name
    edge_type: str = "data"  # "data", "clock", "reset", "set"


@dataclass
class ParseResult:
    nodes: dict = field(default_factory=dict)   # name -> Node
    edges: list = field(default_factory=list)    # list of Edge
    # Maps bare wire name -> set of scoped names (file_stem:WIRE_NAME)
    wire_scopes: dict = field(default_factory=lambda: {})
    # Set of global node names (registered, gate_output, bus, boundary, computed methods)
    global_names: set = field(default_factory=set)
    # Set of known computed method names (from GateBoyState, GateBoyCpuABus, PinsSys)
    computed_methods: set = field(default_factory=set)


# ============================================================================
# Scoping helpers
# ============================================================================

def file_stem(fname: str) -> str:
    """Get file stem for scoping: 'GateBoy.cpp' -> 'GateBoy'."""
    return Path(fname).stem


def scoped_name(fname: str, wire_name: str) -> str:
    """Create a file-scoped wire name: 'GateBoy:AVOR_SYS_RSTp'."""
    return f"{file_stem(fname)}:{wire_name}"


def display_name_from_scoped(name: str) -> str:
    """Strip file scope prefix for display: 'GateBoy:AVOR_SYS_RSTp' -> 'AVOR_SYS_RSTp'."""
    if ':' in name:
        return name.split(':', 1)[1]
    return name


def register_scoped_wire(result: ParseResult, fname: str, wire_name: str):
    """Register a wire name in the scope tracking structures."""
    sname = scoped_name(fname, wire_name)
    if wire_name not in result.wire_scopes:
        result.wire_scopes[wire_name] = set()
    result.wire_scopes[wire_name].add(sname)


# ============================================================================
# Parsing
# ============================================================================

def extract_comment(line: str) -> str:
    """Extract the die-page comment like /*#p21.MUWY*/ from a line."""
    m = re.match(r'\s*/\*[#_]?(p\d+\.\w+)\*/', line)
    return m.group(1) if m else ""


def extract_state_path(expr: str) -> str:
    """Extract a state path like 'reg_ly.MUWY_LY0p_odd' from reg_old/reg_new references."""
    # Match reg_old.xxx.yyy.accessor() or reg_new.xxx.yyy.accessor()
    m = re.search(r'reg_(?:old|new)\.(.+?)\.(?:' + '|'.join(OUTPUT_ACCESSORS) + r')\(\)', expr)
    if m:
        return m.group(1)
    # Match reg_new.xxx.yyy.method(...)  (for DFF calls)
    m = re.search(r'reg_new\.(.+?)\.(?:' + '|'.join(REGISTERED_METHODS | BUS_METHODS) + r')\(', expr)
    if m:
        return m.group(1)
    # Match reg_new.xxx.yyy <<= ...
    m = re.search(r'reg_new\.(.+?)\s*<<=', expr)
    if m:
        return m.group(1)
    return ""


def extract_signal_refs(expr: str, result: ParseResult = None) -> list:
    """Extract all signal references from an expression.

    Returns list of (signal_name, is_registered_read, temporal_phase) tuples.

    When is_registered_read=True and temporal_phase="old", this represents a read
    from the previous tick -- a clock boundary. The edge should come from a
    special "@old" boundary node, not the current-tick computation.
    """
    refs = []

    # Track which parts of the expression are already matched by reg_old/reg_new
    # patterns so we don't double-count them in the local wire pattern
    matched_spans = []

    # Pattern 1: reg_old.path.accessor() -- reading a registered output from previous phase
    for m in re.finditer(
        r'reg_old\.(.+?)\.(' + '|'.join(OUTPUT_ACCESSORS) + r')\(\)',
        expr
    ):
        path = m.group(1)
        parts = path.split('.')
        sig_name = parts[-1]
        refs.append((sig_name, True, "old"))
        matched_spans.append(m.span())

    # Pattern 2: reg_new.path.accessor() -- reading a registered/gate output from current phase
    for m in re.finditer(
        r'reg_new\.(.+?)\.(' + '|'.join(OUTPUT_ACCESSORS) + r')\(\)',
        expr
    ):
        path = m.group(1)
        parts = path.split('.')
        sig_name = parts[-1]
        refs.append((sig_name, True, "new"))
        matched_spans.append(m.span())

    # Pattern 2b: reg_new.path.method_name() -- calling a computed method
    # e.g. reg_new.XAPO_VID_RSTn_new(), reg_new.cpu_abus.SYRO_FE00_FFFF_new()
    for m in re.finditer(
        r'reg_new\.(.+?)\b(\w+)\(\)',
        expr
    ):
        full_path = m.group(1) + m.group(2)
        method_name = m.group(2)
        # Skip if this is an accessor we already matched
        if method_name in OUTPUT_ACCESSORS:
            continue
        # Skip DFF/latch methods and other non-signal methods
        if method_name in SKIP_METHODS:
            continue
        # This is a computed method call -- reference the global method node
        refs.append((method_name, True, "new"))
        matched_spans.append(m.span())

    # Pattern 2c: pins.sys.method_name() -- calling PinsSys computed methods
    # e.g. pins.sys.UCOB_CLKBADp_new(), pins.sys.UPOJ_MODE_PRODn_new()
    for m in re.finditer(
        r'pins\.sys\.(\w+)\(\)',
        expr
    ):
        method_name = m.group(1)
        if method_name in OUTPUT_ACCESSORS | SKIP_METHODS:
            continue
        refs.append((method_name, True, "new"))
        matched_spans.append(m.span())

    # Pattern 2d: pins.sys.FIELD.accessor() -- reading a pin register
    # e.g. pins.sys.PIN_71_RST.qp_int_new(), pins.sys.PIN_74_CLK.clkgood_new()
    for m in re.finditer(
        r'pins\.sys\.(\w+)\.(' + '|'.join(OUTPUT_ACCESSORS) + r'|clkgood_new|clkgood_old|clk_new|clk_old)\(\)',
        expr
    ):
        sig_name = m.group(1)
        accessor = m.group(2)
        phase = "old" if accessor.endswith("_old") else "new"
        refs.append((sig_name, True, phase))
        matched_spans.append(m.span())

    # Pattern 2e: Direct or nested member access FIELD.accessor() -- used inside computed
    # methods where `this->` members are accessed without reg_new prefix.
    # Handles both one-level (BUS_CPU_A15p.out_new()) and two-level
    # (sys_rst.AFER_SYS_RSTp.qp_new(), reg_lcdc.XONA_LCDC_LCDENp.qp_new())
    accessor_pat = '|'.join(OUTPUT_ACCESSORS) + r'|clkgood_new|clkgood_old|clk_new|clk_old'
    # Two-level: struct.FIELD.accessor()
    for m in re.finditer(
        r'\b(\w+)\.(\w+)\.(' + accessor_pat + r')\(\)',
        expr
    ):
        struct_name = m.group(1)
        field_name = m.group(2)
        accessor = m.group(3)
        # Skip if already matched
        in_matched = False
        for start, end in matched_spans:
            if start <= m.start() < end:
                in_matched = True
                break
        if in_matched:
            continue
        if struct_name in ('reg_old', 'reg_new', 'pins'):
            continue
        phase = "old" if accessor.endswith("_old") else "new"
        refs.append((field_name, True, phase))
        matched_spans.append(m.span())

    # One-level: FIELD.accessor() -- only at word boundary, not after a dot
    for m in re.finditer(
        r'(?<!\.)(\b\w+)\.(' + accessor_pat + r')\(\)',
        expr
    ):
        field_name = m.group(1)
        accessor = m.group(2)
        # Skip if already matched by any previous pattern
        in_matched = False
        for start, end in matched_spans:
            if start <= m.start() < end:
                in_matched = True
                break
        if in_matched:
            continue
        # Skip struct names
        if field_name in ('reg_old', 'reg_new', 'pins', 'sys'):
            continue
        phase = "old" if accessor.endswith("_old") else "new"
        refs.append((field_name, True, phase))
        matched_spans.append(m.span())

    # Pattern 3: Local wire references -- just variable names that match known signal patterns
    for m in re.finditer(r'\b([A-Z][A-Z0-9]{3,}_\w+)\b', expr):
        candidate = m.group(1)
        pos = m.start()

        # Skip if this position was already matched by a reg_old/reg_new pattern
        in_matched = False
        for start, end in matched_spans:
            if start <= pos < end:
                in_matched = True
                break
        if in_matched:
            continue

        # Skip things that are clearly not signals
        if candidate.startswith(('BIT_', 'TRI_', 'DELTA_', 'SIM_', 'CHECK_', 'LOG_')):
            continue
        if candidate in ('BIT_DATA', 'BIT_CLOCK', 'BIT_DRIVEN', 'BIT_PULLED',
                         'BIT_OLD', 'BIT_NEW', 'TRI_DRIVEN', 'TRI_NEW'):
            continue
        refs.append((candidate, False, None))

    return refs


def add_edge_for_ref(ref_name: str, is_reg: bool, phase: str, dst_name: str,
                     result: ParseResult, file: str, lineno: int):
    """Add an edge from a signal reference to a destination node.

    For reg_old reads (phase="old"), creates a boundary node representing
    the clock-edge output. This prevents false combinatorial cycles across
    temporal boundaries.
    """
    if ref_name == dst_name:
        return  # no self-loops

    if is_reg and phase == "old":
        # This is a read from the previous tick. Create a boundary node
        # named "SIGNAL@old" that represents the registered output.
        # The combinatorial path terminates here.
        boundary_name = f"{ref_name}@old"
        if boundary_name not in result.nodes:
            result.nodes[boundary_name] = Node(
                name=boundary_name,
                display_name=f"{ref_name}@old",
                node_type="registered",  # acts as path terminator
                reg_type="clock_boundary",
                source_file=file,
                source_line=lineno,
                state_path=f"reg_old.{ref_name}",
                comment=f"Clock boundary read of {ref_name}",
            )
            result.global_names.add(boundary_name)
        result.edges.append(Edge(src=boundary_name, dst=dst_name))
    else:
        result.edges.append(Edge(src=ref_name, dst=dst_name))


def parse_wire_assignment(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: wire NAME = gate_func(args...) or wire NAME = expr

    Wire/triwire local variables are scoped by file to avoid collisions
    when the same wire name appears in multiple files.
    """
    # Match wire declarations with gate function calls
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?(?:wire|triwire)\s+(\w+)\s*=\s*(.+?)\s*;',
        line
    )
    if not m:
        return False

    bare_name = m.group(1)
    expr = m.group(2)
    comment = extract_comment(line)

    # Scope the wire name by file
    name = scoped_name(file, bare_name)
    register_scoped_wire(result, file, bare_name)

    # Determine the gate function
    gate_func = ""
    for gf in GATE_FUNCTIONS:
        if re.search(rf'\b{gf}\s*\(', expr):
            gate_func = gf
            break

    # Also check for Adder (add3 returns struct)
    if 'add3(' in expr:
        gate_func = "add3"

    node = Node(
        name=name,
        display_name=bare_name,
        node_type="combinatorial",
        source_file=file,
        source_line=lineno,
        gate_func=gate_func,
        comment=comment,
    )
    result.nodes[name] = node

    # Extract dependencies from the expression
    refs = extract_signal_refs(expr, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, name, result, file, lineno)

    return True


def parse_reg_update(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path.dffXX(args...) -- registered element update."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\.(' + '|'.join(REGISTERED_METHODS) + r')\s*\((.+?)\)\s*;',
        line
    )
    if not m:
        return False

    path = m.group(1)
    method = m.group(2)
    args_str = m.group(3)
    comment = extract_comment(line)

    parts = path.split('.')
    sig_name = parts[-1]

    node = Node(
        name=sig_name,
        display_name=sig_name,
        node_type="registered",
        reg_type=method,
        state_path=path,
        source_file=file,
        source_line=lineno,
        comment=comment,
    )
    result.nodes[sig_name] = node
    result.global_names.add(sig_name)

    # Parse arguments -- typically (CLK, RST, D) or (CLK, D) or (SET, RST) etc.
    # All arguments are dependencies
    refs = extract_signal_refs(args_str, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, sig_name, result, file, lineno)

    return True


def parse_gate_assign(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path <<= expr -- Gate type assignment (combinatorial stored in state)."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\s*<<=\s*(.+?)\s*;',
        line
    )
    if not m:
        return False

    path = m.group(1)
    expr = m.group(2)
    comment = extract_comment(line)

    parts = path.split('.')
    sig_name = parts[-1]

    gate_func = ""
    for gf in GATE_FUNCTIONS:
        if re.search(rf'\b{gf}\s*\(', expr):
            gate_func = gf
            break

    node = Node(
        name=sig_name,
        display_name=sig_name,
        node_type="gate_output",  # combinatorial but stored in state
        state_path=path,
        source_file=file,
        source_line=lineno,
        gate_func=gate_func,
        comment=comment,
    )
    result.nodes[sig_name] = node
    result.global_names.add(sig_name)

    refs = extract_signal_refs(expr, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, sig_name, result, file, lineno)

    return True


def parse_bus_write(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path.tri_bus(triwire_name) -- bus write."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\.tri_bus\s*\((.+?)\)\s*;',
        line
    )
    if not m:
        return False

    path = m.group(1)
    args_str = m.group(2)
    comment = extract_comment(line)

    parts = path.split('.')
    sig_name = parts[-1]

    # Only create the node if not already defined
    if sig_name not in result.nodes:
        node = Node(
            name=sig_name,
            display_name=sig_name,
            node_type="bus",
            state_path=path,
            source_file=file,
            source_line=lineno,
            comment=comment,
        )
        result.nodes[sig_name] = node
        result.global_names.add(sig_name)

    refs = extract_signal_refs(args_str, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, sig_name, result, file, lineno)

    return True


def parse_sig_assign(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path.sig_in(expr) or sig_out(expr) -- boundary signals."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\.(sig_in|sig_out)\s*\((.+?)\)\s*;',
        line
    )
    if not m:
        return False

    path = m.group(1)
    method = m.group(2)
    args_str = m.group(3)
    comment = extract_comment(line)

    parts = path.split('.')
    sig_name = parts[-1]

    node = Node(
        name=sig_name,
        display_name=sig_name,
        node_type="boundary",
        state_path=path,
        source_file=file,
        source_line=lineno,
        comment=comment,
    )
    result.nodes[sig_name] = node
    result.global_names.add(sig_name)

    refs = extract_signal_refs(args_str, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, sig_name, result, file, lineno)

    return True


def parse_hold(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path.hold() -- hold current value."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\.hold\s*\(\)\s*;',
        line
    )
    if not m:
        return False
    # Just note the node exists -- hold doesn't create new dependencies
    return True


def parse_file(filepath: Path, result: ParseResult):
    """Parse a single GateBoy source file."""
    if not filepath.exists():
        print(f"  [SKIP] {filepath.name} -- not found")
        return

    text = filepath.read_text()
    lines = text.split('\n')
    fname = filepath.name

    parsed = 0

    # Join continuation lines (lines ending with a comma or opening paren
    # followed by more args on the next line)
    joined_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        orig_lineno = i + 1

        # Detect multi-line statements: line has unbalanced parens
        open_count = line.count('(') - line.count(')')
        while open_count > 0 and i + 1 < len(lines):
            i += 1
            line += ' ' + lines[i].strip()
            open_count = line.count('(') - line.count(')')

        joined_lines.append((line, orig_lineno))
        i += 1

    for line, lineno in joined_lines:
        # Skip comments, preprocessor, blank lines
        stripped = line.strip()
        if not stripped or stripped.startswith('//') or stripped.startswith('#'):
            continue
        # Skip lines that are inside comments
        if stripped.startswith('/*') and '*/' not in stripped:
            continue

        if parse_wire_assignment(line, fname, lineno, result):
            parsed += 1
        elif parse_reg_update(line, fname, lineno, result):
            parsed += 1
        elif parse_gate_assign(line, fname, lineno, result):
            parsed += 1
        elif parse_bus_write(line, fname, lineno, result):
            parsed += 1
        elif parse_sig_assign(line, fname, lineno, result):
            parsed += 1
        elif parse_hold(line, fname, lineno, result):
            parsed += 1

    print(f"  {fname}: {parsed} statements parsed")


# ============================================================================
# Computed method parsing
# ============================================================================

def parse_computed_methods(filepath: Path, result: ParseResult):
    """Parse computed methods from GateBoyState.cpp, GateBoyCpuBus.cpp, GateBoyPins.cpp.

    These files define methods like:
        wire GateBoyState::XAPO_VID_RSTn_new() const { ... }
        wire GateBoyCpuABus::TUNA_0000_FDFF_new() const { ... }
        wire PinsSys::UCOB_CLKBADp_new() const { ... }

    The method name becomes a global combinatorial node. Internal wires are
    scoped to the source file. References to other computed methods create
    edges to those global nodes.
    """
    if not filepath.exists():
        print(f"  [SKIP] {filepath.name} -- not found")
        return

    text = filepath.read_text()
    fname = filepath.name
    parsed = 0

    # Pattern for method declarations (both _new and _old variants)
    # Matches: wire ClassName::MethodName() const { ... }
    # Handle both single-line and multi-line method bodies
    method_pattern = re.compile(
        r'(?:/\*[^*]*\*/\s*)?wire\s+\w+::(\w+)\s*\(\)\s*const\s*\{',
    )

    pos = 0
    while pos < len(text):
        m = method_pattern.search(text, pos)
        if not m:
            break

        method_name = m.group(1)
        body_start = m.end()

        # Find the matching closing brace
        brace_depth = 1
        i = body_start
        while i < len(text) and brace_depth > 0:
            if text[i] == '{':
                brace_depth += 1
            elif text[i] == '}':
                brace_depth -= 1
            i += 1

        body = text[body_start:i - 1]  # exclude the closing brace
        lineno = text[:m.start()].count('\n') + 1

        pos = i  # advance past this method

        # Skip _old and _any variants -- we only care about _new for current-tick analysis
        # But also parse _old methods from PinsSys since they are called from other files
        # Actually, we should parse all of them since they may be referenced
        # Skip non-signal methods
        if method_name in ('reset', 'poweron', 'check_old', 'check_new'):
            continue

        # Determine the gate function from the return expression or last wire assignment
        gate_func = ""
        for gf in GATE_FUNCTIONS:
            if re.search(rf'\b{gf}\s*\(', body):
                gate_func = gf
                break

        # Create the global method node
        node = Node(
            name=method_name,
            display_name=method_name,
            node_type="combinatorial",
            source_file=fname,
            source_line=lineno,
            gate_func=gate_func,
            comment="",
        )
        result.nodes[method_name] = node
        result.global_names.add(method_name)
        result.computed_methods.add(method_name)

        # Parse internal wire declarations within the method body
        # These are scoped to the file
        internal_wires = []
        for wm in re.finditer(
            r'(?:/\*[^*]*\*/\s*)?(?:wire|triwire)\s+(\w+)\s*=\s*(.+?)\s*;',
            body
        ):
            wire_name = wm.group(1)
            wire_expr = wm.group(2)

            sname = scoped_name(fname, wire_name)
            register_scoped_wire(result, fname, wire_name)

            wire_gate_func = ""
            for gf in GATE_FUNCTIONS:
                if re.search(rf'\b{gf}\s*\(', wire_expr):
                    wire_gate_func = gf
                    break

            wire_node = Node(
                name=sname,
                display_name=wire_name,
                node_type="combinatorial",
                source_file=fname,
                source_line=lineno,
                gate_func=wire_gate_func,
                comment=extract_comment(wm.group(0)),
            )
            result.nodes[sname] = wire_node
            internal_wires.append((sname, wire_name, wire_expr))

            # Parse dependencies of this internal wire
            refs = extract_signal_refs(wire_expr, result)
            for ref_name, is_reg, phase in refs:
                add_edge_for_ref(ref_name, is_reg, phase, sname, result, fname, lineno)

        # Parse the return statement to connect internal wires to the method node.
        # If the return variable has the same name as the method, merge them:
        # replace the method node with the scoped wire (avoids double-counting).
        ret_match = re.search(r'return\s+(\w+)\s*;', body)
        if ret_match:
            ret_var = ret_match.group(1)
            ret_scoped = scoped_name(fname, ret_var)
            if ret_var == method_name and ret_scoped in result.nodes:
                # The internal wire IS the method output. Promote the scoped wire
                # to be the global method node instead of having two separate nodes.
                scoped_node = result.nodes[ret_scoped]
                # Remove the scoped wire node
                del result.nodes[ret_scoped]
                # Update the method node with the scoped wire's attributes
                result.nodes[method_name].gate_func = scoped_node.gate_func
                result.nodes[method_name].comment = scoped_node.comment
                # Redirect all edges that pointed to/from the scoped wire
                for edge in result.edges:
                    if edge.src == ret_scoped:
                        edge.src = method_name
                    if edge.dst == ret_scoped:
                        edge.dst = method_name
                # Remove from wire_scopes
                if ret_var in result.wire_scopes:
                    result.wire_scopes[ret_var].discard(ret_scoped)
            elif ret_scoped in result.nodes:
                result.edges.append(Edge(src=ret_scoped, dst=method_name))
            elif ret_var in result.nodes:
                result.edges.append(Edge(src=ret_var, dst=method_name))

        # If there are no internal wires (simple return of a function call),
        # parse dependencies directly on the method body
        if not internal_wires:
            refs = extract_signal_refs(body, result)
            for ref_name, is_reg, phase in refs:
                add_edge_for_ref(ref_name, is_reg, phase, method_name, result, fname, lineno)

        # Also handle calls to other computed methods within the body
        # e.g. XAPO_VID_RSTn_new() called as a bare function (within same class)
        for cm in re.finditer(r'\b(\w+_(?:new|old))\(\)', body):
            callee = cm.group(1)
            if callee == method_name:
                continue  # skip self
            if callee in OUTPUT_ACCESSORS | SKIP_METHODS:
                continue
            # Check if this is inside a wire assignment expression we already parsed
            # If so, the dependency is already captured via the wire's refs
            already_handled = False
            for sname, wire_name, wire_expr in internal_wires:
                if callee + '()' in wire_expr:
                    already_handled = True
                    break
            if not already_handled:
                # Direct method call not in a wire assignment -- connect to method node
                result.edges.append(Edge(src=callee, dst=method_name))

        # Handle member references like sys_rst.AFER_SYS_RSTp.qp_new() within method bodies
        # These resolve to registered elements. Already handled by extract_signal_refs
        # via the pattern matching on field.accessor() -- but we need to handle
        # the case where these are on `this` members (no reg_new prefix).
        for rm in re.finditer(
            r'(\w+)\.(\w+)\.(' + '|'.join(OUTPUT_ACCESSORS) + r'|clkgood_new|clkgood_old|clk_new|clk_old)\(\)',
            body
        ):
            struct_name = rm.group(1)
            field_name = rm.group(2)
            accessor = rm.group(3)
            # Skip if this was already matched inside a wire expression
            if struct_name in ('reg_old', 'reg_new', 'pins'):
                continue
            phase = "old" if accessor.endswith("_old") else "new"
            # field_name is the registered element
            # Find which internal wire (or method) this belongs to
            rm_start = rm.start()
            target = method_name  # default: edge to the method node
            for sname, wire_name, wire_expr in internal_wires:
                if field_name in wire_expr:
                    target = sname
                    break
            add_edge_for_ref(field_name, True, phase, target, result, fname, lineno)

        parsed += 1

    if parsed > 0:
        print(f"  {fname}: {parsed} computed methods parsed")


# ============================================================================
# Edge resolution with file scoping
# ============================================================================

def resolve_scoped_edges(result: ParseResult):
    """Resolve edges considering file-scoped wire names.

    For each edge, if the source is a bare wire name (not already scoped):
    1. If it exists as a global node, use it directly
    2. If it exists as a scoped wire in the same file as the destination, use that
    3. If it exists as a scoped wire in exactly one file, use that
    4. Otherwise, mark as unresolved

    For destination nodes, they are already resolved (scoped during parse).
    """
    known = set(result.nodes.keys())
    unknown_refs = set()

    resolved_edges = []
    seen = set()

    for edge in result.edges:
        src = edge.src
        dst = edge.dst

        # Resolve source if it's a bare name
        resolved_src = _resolve_ref(src, dst, result, known)

        if resolved_src is None:
            unknown_refs.add(src)
            continue

        key = (resolved_src, dst)
        if key in seen:
            continue
        seen.add(key)

        if resolved_src == dst:
            continue  # no self-loops

        resolved_edges.append(Edge(src=resolved_src, dst=dst, edge_type=edge.edge_type))

    result.edges = resolved_edges
    return unknown_refs


def _resolve_ref(src: str, dst: str, result: ParseResult, known: set) -> Optional[str]:
    """Resolve a signal reference to a known node name.

    Returns the resolved node name, or None if unresolvable.
    """
    # Already a known node (global or scoped)
    if src in known:
        return src

    # Check if src is a bare wire name that needs scoping
    if src in result.wire_scopes:
        scoped_candidates = result.wire_scopes[src]

        # Try same-file scope first: if dst is scoped, use the same file
        if ':' in dst:
            dst_stem = dst.split(':')[0]
            same_file = f"{dst_stem}:{src}"
            if same_file in scoped_candidates and same_file in known:
                return same_file
        else:
            # dst is a global name -- check its source file
            dst_node = result.nodes.get(dst)
            if dst_node and dst_node.source_file:
                dst_stem = file_stem(dst_node.source_file)
                same_file = f"{dst_stem}:{src}"
                if same_file in scoped_candidates and same_file in known:
                    return same_file

        # If only one scope exists, use it
        valid = [s for s in scoped_candidates if s in known]
        if len(valid) == 1:
            return valid[0]

        # If multiple scopes exist, we cannot disambiguate -- use any
        # This is a best-effort fallback; ideally all should be resolved above
        if valid:
            return valid[0]

    # Check if it's a computed method name
    if src in result.computed_methods and src in known:
        return src

    return None


def classify_gate_outputs(result: ParseResult):
    """Gate outputs (type 'gate_output') are combinatorial -- they just happen to be
    stored in state for cross-function visibility. For path analysis they should be
    treated as combinatorial (path continues through them)."""
    for node in result.nodes.values():
        if node.node_type == "gate_output":
            node.node_type = "combinatorial"


# ============================================================================
# Graph construction
# ============================================================================

def build_graph(result: ParseResult):
    """Build a networkx DiGraph from parsed results."""
    import networkx as nx

    G = nx.DiGraph()

    for name, node in result.nodes.items():
        G.add_node(name,
            node_type=node.node_type,
            reg_type=node.reg_type,
            source_file=node.source_file,
            source_line=node.source_line,
            gate_func=node.gate_func,
            state_path=node.state_path,
            comment=node.comment,
            display_name=node.display_name or display_name_from_scoped(name),
        )

    for edge in result.edges:
        if edge.src in G and edge.dst in G:
            G.add_edge(edge.src, edge.dst, edge_type=edge.edge_type)

    return G


def is_path_terminator(G, node):
    """Check if a node is a path terminator (registered, bus, or boundary)."""
    return G.nodes[node].get('node_type') in ('registered', 'bus', 'boundary')


def find_all_cycles(G):
    """Find all simple cycles, grouped by whether they pass through registered nodes."""
    import networkx as nx

    cycles = []
    try:
        # Find up to 100 cycles
        count = 0
        for cycle in nx.simple_cycles(G):
            cycles.append(cycle)
            count += 1
            if count >= 100:
                break
    except Exception:
        pass

    # Classify cycles
    feedback_cycles = []  # cycles through async set/reset of DFFs
    pure_comb_cycles = []  # cycles entirely in combinatorial logic (problematic)

    for cycle in cycles:
        has_reg = any(is_path_terminator(G, n) for n in cycle)
        if has_reg:
            feedback_cycles.append(cycle)
        else:
            pure_comb_cycles.append(cycle)

    return feedback_cycles, pure_comb_cycles


def build_dag_for_analysis(G):
    """Build a DAG suitable for critical path analysis.

    Removes edges that enter registered/bus/boundary nodes from combinatorial nodes
    when those registered nodes also have outgoing edges to combinatorial nodes.
    This breaks feedback cycles while preserving the combinatorial path structure.

    Returns a new graph where edges OUT of registered nodes are kept (they're sources)
    and edges INTO registered nodes are kept (they're sinks), but the registered nodes
    themselves act as path terminators.
    """
    import networkx as nx

    DAG = G.copy()

    # Find and break all cycles by removing back-edges found during DFS
    # We iteratively remove edges until the graph is acyclic
    removed_edges = []
    while True:
        try:
            cycle_edges = nx.find_cycle(DAG)
            # Remove the last edge in the cycle (arbitrary but consistent)
            edge = cycle_edges[-1]
            DAG.remove_edge(edge[0], edge[1])
            removed_edges.append((edge[0], edge[1]))
        except nx.NetworkXNoCycle:
            break

    return DAG, removed_edges


def graph_stats(G) -> dict:
    """Compute basic graph statistics."""
    import networkx as nx

    node_types = {}
    for _, data in G.nodes(data=True):
        t = data.get('node_type', 'unknown')
        node_types[t] = node_types.get(t, 0) + 1

    # Check for cycles
    has_cycles = False
    cycle_sample = []
    try:
        cycle = nx.find_cycle(G)
        has_cycles = True
        cycle_sample = [(str(e[0]), str(e[1])) for e in cycle[:10]]
    except nx.NetworkXNoCycle:
        pass

    n_components = nx.number_weakly_connected_components(G)

    reg_nodes = [n for n, d in G.nodes(data=True)
                 if d.get('node_type') in ('registered', 'bus', 'boundary')]
    comb_nodes = [n for n, d in G.nodes(data=True)
                  if d.get('node_type') == 'combinatorial']

    return {
        "total_nodes": G.number_of_nodes(),
        "total_edges": G.number_of_edges(),
        "node_types": node_types,
        "registered_nodes": len(reg_nodes),
        "combinatorial_nodes": len(comb_nodes),
        "weakly_connected_components": n_components,
        "has_cycles": has_cycles,
        "cycle_sample": cycle_sample,
    }


# ============================================================================
# Critical Path Analysis
# ============================================================================

def find_critical_paths(DAG, G_original):
    """Find the longest combinatorial paths between registered nodes.

    For each node, computes the longest path from any registered source
    through combinatorial logic to any registered sink.

    Returns sorted list of (depth, path) tuples.
    """
    import networkx as nx

    # Topological sort the DAG
    try:
        topo_order = list(nx.topological_sort(DAG))
    except nx.NetworkXUnfeasible:
        print("ERROR: DAG still has cycles after cycle-breaking!")
        return []

    # For each node, compute the longest path TO it from any registered source,
    # counting only combinatorial gates in the depth.
    # dist[n] = (depth, path) where depth is number of combinatorial gates
    dist = {}
    for n in topo_order:
        nt = DAG.nodes[n].get('node_type', '')

        if is_path_terminator(DAG, n):
            # Registered node -- path starts here with depth 0
            dist[n] = (0, [n])
        else:
            # Combinatorial node -- find longest incoming path + 1
            best_depth = -1
            best_path = []
            for pred in DAG.predecessors(n):
                if pred in dist:
                    d, p = dist[pred]
                    if d > best_depth:
                        best_depth = d
                        best_path = p
            if best_depth >= 0:
                dist[n] = (best_depth + 1, best_path + [n])
            else:
                # No predecessors with known distance -- this is a root
                dist[n] = (1, [n])

    # Now find paths that terminate at registered nodes.
    # For each registered sink, look at its predecessors' distances.
    critical_paths = []

    for n in topo_order:
        if not is_path_terminator(DAG, n):
            continue
        # This registered node is a sink. Check all predecessors.
        for pred in DAG.predecessors(n):
            if pred in dist:
                depth, path = dist[pred]
                if depth >= 1:  # at least one combinatorial gate
                    full_path = path + [n]
                    critical_paths.append((depth, full_path))

    # Sort by depth, descending
    critical_paths.sort(key=lambda x: -x[0])

    # Deduplicate paths that share the same start and end
    seen = set()
    unique_paths = []
    for depth, path in critical_paths:
        key = (path[0], path[-1], depth)
        if key not in seen:
            seen.add(key)
            unique_paths.append((depth, path))

    return unique_paths


def find_race_pairs(DAG, G):
    """Find signal race pairs: registered nodes where inputs arrive at significantly
    different combinatorial depths.

    A race pair indicates that a DFF/latch samples two signals that settle at
    different times after a clock edge. In a behavioral emulator these resolve
    instantly, but on real hardware the late-arriving signal may not be stable
    when the DFF samples — causing the hardware behavior to differ by one dot.

    Returns list of race dicts sorted by depth differential.
    """
    import networkx as nx

    topo_order = list(nx.topological_sort(DAG))

    # Compute depth to each node (same as find_critical_paths)
    dist = {}
    for n in topo_order:
        if is_path_terminator(DAG, n):
            dist[n] = 0
        else:
            best = -1
            for pred in DAG.predecessors(n):
                if pred in dist and dist[pred] > best:
                    best = dist[pred]
            dist[n] = best + 1 if best >= 0 else 0

    races = []
    for n in topo_order:
        if not is_path_terminator(DAG, n):
            continue

        preds = list(DAG.predecessors(n))
        if len(preds) < 2:
            continue

        pred_depths = [(p, dist.get(p, 0)) for p in preds]
        pred_depths.sort(key=lambda x: -x[1])

        max_d = pred_depths[0][1]
        min_d = pred_depths[-1][1]
        diff = max_d - min_d

        if diff >= 3 and max_d >= 4:
            races.append({
                'node': n,
                'display_name': _display(G, n),
                'node_type': DAG.nodes[n].get('node_type', ''),
                'reg_type': DAG.nodes[n].get('reg_type', ''),
                'phase': get_phase(G, n),
                'source_file': DAG.nodes[n].get('source_file', ''),
                'source_line': DAG.nodes[n].get('source_line', 0),
                'depth_diff': diff,
                'max_depth': max_d,
                'min_depth': min_d,
                'inputs': [
                    {
                        'name': _display(G, p),
                        'depth': d,
                        'gate_func': DAG.nodes[p].get('gate_func', ''),
                        'node_type': DAG.nodes[p].get('node_type', ''),
                        'phase': get_phase(G, p),
                    }
                    for p, d in pred_depths
                ],
                'category': categorize_path([n], G),  # rough category from sink
            })

    races.sort(key=lambda x: (-x['depth_diff'], -x['max_depth']))
    return races


def _display(G, node_name):
    """Get display name for a node, stripping file scope prefix."""
    return G.nodes[node_name].get('display_name', '') or display_name_from_scoped(node_name)


def get_phase(G, node_name):
    """Extract clock phase annotation from a signal name.

    Returns 'ODD', 'EVN', an 8-char clock subcycle pattern (e.g. 'AxCxExGx'),
    or '' if no phase information is present.
    """
    dn = _display(G, node_name)
    if '_odd' in dn: return 'ODD'
    if '_evn' in dn: return 'EVN'
    m = re.search(r'([AxBCDEFGHx]{8})', dn)
    return m.group(1) if m else ''


def compute_fanout(G) -> dict:
    """Compute fan-out (number of successor edges) for each node."""
    return {n: G.out_degree(n) for n in G.nodes()}


def is_reset_path(path, G):
    """Classify whether a path is reset-dominated (only fires on reset/LCDC toggle)
    vs operational (fires every dot/scanline during normal rendering)."""
    RESET_SOURCES = {'AFER_SYS_RSTp', 'ASOL_POR_DONEn'}
    RESET_CHAIN = {'AVOR_SYS_RSTp', 'ALUR_SYS_RSTn', 'DULA_SYS_RSTp', 'CUNU_SYS_RSTn',
                   'XORE_SYS_RSTp', 'XEBE_SYS_RSTn', 'XODO_VID_RSTp',
                   'XAPO_VID_RSTn_new', 'LYHA_VID_RSTp_new', 'LYFE_VID_RSTn_new',
                   'TOFU_VID_RSTp_new', 'ROSY_VID_RSTp_new', 'ATAR_VID_RSTp_new',
                   'ABEZ_VID_RSTn_new', 'PYRY_VID_RSTp_new'}

    src_display = _display(G, path[0])

    # Source is a reset register
    if src_display in RESET_SOURCES:
        return True

    # Check if first several nodes are in the reset chain
    reset_count = 0
    for node_name in path[:12]:
        dn = _display(G, node_name)
        if dn in RESET_CHAIN or dn in RESET_SOURCES:
            reset_count += 1
    return reset_count >= 4


def categorize_path(path, G):
    """Assign a PPU functional category to a path based on its sink and intermediate nodes."""
    sink = _display(G, path[-1]).upper()
    src = _display(G, path[0]).upper()
    all_names = [_display(G, n).upper() for n in path]
    all_text = ' '.join(all_names)

    # Categorize primarily by sink, with fallback to path content
    if any(x in sink for x in ['PIPE_A', 'PIPE_B', 'PAL_PIPE', 'MASK_PIPE', 'REMY_LD', 'RAVO_LD']):
        return 'Pixel Pipeline'
    if any(x in sink for x in ['CLKPIPE', 'FINE', 'SCX_FINE', 'PUXA', 'NYZE', 'ROXY']):
        return 'Scroll/Fine Timing'
    if any(x in sink for x in ['WIN_', 'RYFA', 'RENE', 'NUKO', 'ROGE', 'PYCO', 'NUNU', 'SARY', 'REJO', 'PYNU', 'NOPA', 'SOVY']):
        return 'Window Logic'
    if any(x in sink for x in ['STORE', 'SPRITE_MATCH', 'FEPO', 'SPRITE_RESET', 'SPRITE_IDX']):
        return 'Sprite Store/Match'
    if any(x in sink for x in ['SCAN', 'FETO', 'BESU', 'CENO', 'YFEL', 'WEWY', 'GOSO']):
        return 'Sprite Scanner'
    if any(x in sink for x in ['SPR_PIX', 'FLIPPED', 'SFETCH', 'TAKA', 'SOBU', 'TEXY', 'WUTY']):
        return 'Sprite Fetcher'
    if any(x in sink for x in ['BFETCH', 'TFETCH', 'LAXU', 'MESU', 'NYVA', 'LONY', 'LOVY', 'NYKA', 'PORY', 'PYGO', 'LYRY', 'POKY', 'LYZU']):
        return 'Tile Fetcher'
    if any(x in sink for x in ['TILE_TEMP', 'LEGU', 'LESO', 'LABU', 'LACE', 'LUJO', 'LEGU']):
        return 'Tile Fetcher'
    if any(x in sink for x in ['BUS_VRAM', 'VD0', 'VD1', 'VD2', 'VD3', 'VD4', 'VD5', 'VD6', 'VD7', 'VRAM_A']):
        return 'VRAM Bus'
    if any(x in sink for x in ['BUS_OAM', 'OAM_', 'SIG_OAM']):
        return 'OAM Bus'
    if any(x in sink for x in ['STAT', 'RUPO', 'ROPO', 'LY_MATCH']):
        return 'STAT/LY Match'
    if any(x in sink for x in ['HBLANK', 'VBLANK', 'VOGA', 'WODU', 'ACYL', 'XYMU', 'RENDERING']):
        return 'Mode/Rendering Control'
    if any(x in sink for x in ['ATEJ', 'LINE_RST', 'LINE_END', 'CATU']):
        return 'Line Timing'
    if any(x in sink for x in ['PX0', 'PX1', 'PX2', 'PX3', 'PX4', 'PX5', 'PX6', 'PX7', 'XEHO', 'SAVY', 'XODU', 'XYDO', 'TUHU', 'TUKY', 'TAKO', 'SYBE', 'PAHO', 'POME']):
        return 'Pixel Counter'
    if any(x in sink for x in ['LX', 'SAXO', 'TYPO', 'VYZO', 'TELU', 'SUDE', 'TAHA', 'TYRY']):
        return 'LX Counter'
    if any(x in sink for x in ['DMA', 'MATU']):
        return 'DMA'
    if any(x in sink for x in ['FF0F', 'INT', 'LOPE', 'LALU', 'NYBO', 'UBUL', 'ULAK']):
        return 'Interrupts'
    if any(x in sink for x in ['LYC', 'SYRY', 'VUCE', 'SEDY', 'SALO', 'SOTA', 'VAFA', 'VEVO', 'RAHA']):
        return 'LYC Register'
    if any(x in sink for x in ['LY', 'MUWY', 'MYRO', 'LEXA', 'LYDO', 'LOVU', 'LEMA', 'MATO', 'LAFO']):
        return 'LY Counter'
    if any(x in sink for x in ['LCDC', 'BGP', 'OBP', 'SCY', 'SCX', 'WY', 'WX']):
        return 'PPU Registers'
    if any(x in sink for x in ['SIG_CPU', 'BOWA', 'BEDO', 'BOMA', 'BOGA']):
        return 'Clock Distribution'
    if any(x in sink for x in ['DIV', 'TIMA', 'TIMER']):
        return 'Timer'
    if any(x in sink for x in ['JOYPAD', 'JP_', 'BATU', 'ACEF', 'AGEM', 'APUG', 'AWOB']):
        return 'Joypad'
    if any(x in sink for x in ['SERIAL', 'SB_', 'SC_']):
        return 'Serial'

    # Fallback: check path content
    if 'CLKPIPE' in all_text or 'PIX' in all_text:
        return 'Pixel Pipeline'
    if 'VRAM' in all_text:
        return 'VRAM Bus'
    if 'OAM' in all_text:
        return 'OAM Bus'

    return 'Other'


def format_path_trace(path, G, fanout, indent=2):
    """Format a single path as a readable trace."""
    lines = []
    lines.append("```")
    for j, node_name in enumerate(path):
        nd = G.nodes.get(node_name, {})
        nt = nd.get('node_type', '?')
        gf = nd.get('gate_func', '')
        sf = nd.get('source_file', '')
        sl = nd.get('source_line', '')
        dn = _display(G, node_name)
        fo = fanout.get(node_name, 0)
        phase = get_phase(G, node_name)

        if nt in ('registered', 'bus', 'boundary'):
            marker = f"[{nt.upper()}]"
        else:
            marker = f"[{gf}]" if gf else "[comb]"

        loc = f"{sf}:{sl}" if sf else ""
        fo_str = f" (fan-out: {fo})" if fo >= 10 else ""
        phase_str = f" @{phase}" if phase else ""
        lines.append(f"{'  ' * (indent + j)}{marker} {dn}{phase_str}{fo_str}  ({loc})")
    lines.append("```")
    return "\n".join(lines)


def observable_effect(race):
    """Describe the observable emulator symptom for a signal race.

    Returns (effect_summary, detail) for inclusion in the report.
    """
    name = race['display_name'].upper()
    cat = race.get('category', '')

    # Sprite Store X-position latches: reset arrives late, stale X captured
    if 'STORE' in name and '_X' in name:
        store_num = ''
        m = re.search(r'STORE(\d+)', name)
        if m:
            store_num = m.group(1)
        return (
            f"Sprite store {store_num} X-position off by one dot",
            f"The line-end reset signal (depth {race['max_depth']}) arrives long after "
            f"sprite X data from OAM (depth {race['min_depth']}). At scanline boundaries, "
            f"the store latch may capture the previous sprite's X coordinate instead of "
            f"clearing. Visible as sprites shifting one dot horizontally at the start "
            f"of a scanline, most noticeable with moving sprites near the left edge."
        )

    # Sprite Store index/line latches
    if 'STORE' in name and ('_I' in name or '_L' in name):
        return (
            "Sprite store index/line data captured with stale reset",
            f"Reset arrives {race['depth_diff']} gates after data. May cause wrong "
            f"tile or wrong line-within-sprite to render at scanline boundaries."
        )

    # Tile fetcher state machine
    if any(x in name for x in ['BFETCH_S0', 'BFETCH_S1', 'BFETCH_S2', 'LAXU', 'MESU', 'NYVA']):
        return (
            "Tile fetch state machine runs one extra cycle before reset",
            f"The fetch counter reset (NYXU_BFETCH_RSTn, depth {race['max_depth']}) "
            f"arrives after the fetch counter clock (depth {race['min_depth']}). "
            f"The state machine advances one extra state before resetting to S0. "
            f"Visible as a corrupted tile at the left edge of the screen or at "
            f"window/BG boundary transitions — the fetcher reads from the wrong "
            f"VRAM address for one cycle."
        )

    # Tile fetch done / fetching flag
    if any(x in name for x in ['TFETCH_DONE', 'LOVY', 'TFETCHING', 'LONY']):
        return (
            "Tile fetch pipeline stays active one dot too long",
            f"The fetch-done or fetching flag reset (depth {race['max_depth']}) "
            f"arrives late. The pipeline continues fetching for one extra dot, "
            f"consuming an additional VRAM cycle. Can shift the mode 3 / mode 0 "
            f"boundary by one dot, affecting H-blank timing and any mid-scanline "
            f"register writes that depend on precise mode transition timing."
        )

    # OAM scan done
    if any(x in name for x in ['SCAN_DONE', 'BESU', 'CENO']):
        return (
            "OAM scan extends one dot beyond expected boundary",
            f"The scan-done signal (depth {race['max_depth']}) races against "
            f"line-end (depth {race['min_depth']}). OAM evaluation continues for "
            f"one extra dot, potentially including one additional sprite in the "
            f"scanline sprite buffer. Affects the mode 2 → mode 3 transition point, "
            f"which shifts all subsequent mode timings by one dot. Most visible "
            f"with exactly 10 sprites on a line (the hardware limit)."
        )

    # Pixel pipe / CLKPIPE races
    if any(x in name for x in ['PIPE_A', 'PIPE_B', 'PAL_PIPE', 'MASK_PIPE', 'CLKPIPE']):
        return (
            "Pixel data shifted one dot late relative to pipe clock",
            f"CLKPIPE (the pixel pipe shift clock) arrives through a {race['max_depth']}-gate "
            f"buffer chain, well after the pipe input data is ready. The pipe effectively "
            f"shifts one propagation delay after data settles. Sprite and BG pixels may "
            f"appear one dot to the right of their correct position."
        )

    # Fine scroll / SCX match
    if any(x in name for x in ['FINE', 'SCX_FINE', 'PUXA', 'NYZE', 'ROXY']):
        return (
            "Fine scroll match applies one dot late",
            f"The SCX fine scroll match signal settles at depth {race['min_depth']}, "
            f"but the pixel clock it gates (CLKPIPE) arrives at depth {race['max_depth']}. "
            f"Fine scroll effectively skips one fewer pixel than expected, shifting "
            f"the background by one dot. Visible in games that use SCX fine scroll "
            f"for smooth horizontal scrolling (most platformers)."
        )

    # Window logic
    if any(x in name for x in ['WIN_', 'RYFA', 'RENE', 'NUKO', 'ROGE', 'PYCO', 'NOPA', 'SOVY']):
        return (
            "Window trigger fires one dot late",
            f"Window match/fetch signals race with a {race['depth_diff']}-gate differential. "
            f"The window may activate one dot later than expected, shifting all window "
            f"content one pixel to the right. Affects games with split-screen effects "
            f"using the window (status bars, dialogue boxes)."
        )

    # Pixel counter
    if any(x in name for x in ['PX', 'XEHO', 'SAVY', 'XODU', 'XYDO', 'TUHU', 'TUKY', 'TAKO', 'SYBE']):
        return (
            "Pixel counter increment races with pipe clock",
            f"The pixel X counter races against CLKPIPE with a {race['depth_diff']}-gate "
            f"differential. This shifts the X coordinate at which sprite/window "
            f"comparisons trigger, potentially causing one-dot horizontal offsets."
        )

    # STAT / LY match
    if any(x in name for x in ['STAT', 'RUPO', 'ROPO', 'LY_MATCH']):
        return (
            "STAT interrupt fires one dot early/late",
            f"LY/LYC match or STAT mode flag races with a {race['depth_diff']}-gate "
            f"differential. The STAT interrupt may trigger one dot earlier or later "
            f"than expected. Affects games that use mid-frame STAT interrupts for "
            f"raster effects (wobble, palette changes)."
        )

    # Mode/rendering control
    if any(x in name for x in ['HBLANK', 'VBLANK', 'VOGA', 'WODU', 'XYMU', 'RENDERING']):
        return (
            "Mode transition boundary shifted by one dot",
            f"Mode flag races with a {race['depth_diff']}-gate differential. "
            f"The mode 0/2/3 transition occurs one dot off from the expected position, "
            f"affecting when the CPU can access VRAM/OAM and when H-blank begins."
        )

    # Sprite fetcher
    if any(x in name for x in ['SFETCH', 'TAKA', 'SOBU', 'TEXY', 'WUTY']):
        return (
            "Sprite fetch timing shifted by one dot",
            f"Sprite fetch state machine races with a {race['depth_diff']}-gate differential. "
            f"May cause the sprite fetch to start or complete one dot off, affecting "
            f"mode 3 duration and sprite X positioning."
        )

    # DMA
    if any(x in name for x in ['DMA', 'MATU', 'LARA', 'LOKY']):
        return (
            "DMA transfer timing off by one cycle",
            f"DMA control signal races with a {race['depth_diff']}-gate differential. "
            f"May affect when DMA releases the OAM bus back to the PPU."
        )

    # LX counter
    if any(x in name for x in ['SAXO', 'TYPO', 'VYZO', 'TELU', 'SUDE', 'TAHA', 'TYRY']):
        return (
            "Internal line counter off by one dot",
            f"LX counter races with a {race['depth_diff']}-gate differential. "
            f"Shifts all LX-derived timing signals (line end, scan triggers) by one dot."
        )

    # Generic fallback
    return (
        f"{cat} timing off by one dot",
        f"Signal race with {race['depth_diff']}-gate differential at `{race['display_name']}`. "
        f"The late-arriving signal (depth {race['max_depth']}) may not settle before "
        f"the DFF samples, causing the captured value to differ from behavioral emulation."
    )


def format_report_sections(paths, G, races=None, max_paths=30):
    """Format critical paths into separate report sections.

    Returns a dict of {filename: content} for each report section.
    """
    fanout = compute_fanout(G)
    if races is None:
        races = []

    # Separate reset vs operational
    reset = [(d, p) for d, p in paths if is_reset_path(p, G)]
    operational = [(d, p) for d, p in paths if not is_reset_path(p, G)]

    sections = {}

    # =========================================================================
    # OVERVIEW & KEY FINDINGS
    # =========================================================================
    lines = []
    lines.append("# Game Boy PPU Critical Combinatorial Paths\n")
    lines.append("Static analysis of the Game Boy (DMG) PPU's gate-level netlist identifying deep")
    lines.append("combinatorial paths that may cause propagation delay on real hardware.\n")

    lines.append("## Timing Reference\n")
    lines.append("- Game Boy master clock: 4.194304 MHz")
    lines.append("- T-cycle period: ~238.4 ns (one dot)")
    lines.append("- Half T-cycle: ~119.2 ns")
    lines.append("- Estimated gate delay (Sharp SM83 CMOS, ~5um): 5-15 ns per gate")
    lines.append("- Paths exceeding ~8 gates may cause signals to arrive late within a half T-cycle\n")

    lines.append("## Overview\n")
    lines.append(f"| Category | Count | Max Depth | Max Delay (worst case) |")
    lines.append(f"|----------|-------|-----------|----------------------|")
    lines.append(f"| **Operational** (per-dot/per-scanline) | {len(operational)} | {operational[0][0] if operational else 0} | {operational[0][0]*15 if operational else 0} ns |")
    lines.append(f"| Reset-only (LCDC toggle / system reset) | {len(reset)} | {reset[0][0] if reset else 0} | {reset[0][0]*15 if reset else 0} ns |")
    lines.append(f"| **Total** | {len(paths)} | {paths[0][0] if paths else 0} | {paths[0][0]*15 if paths else 0} ns |")
    lines.append("")
    lines.append("> **Reset vs Operational:** Reset paths only fire when LCDC bit 7 is toggled or")
    lines.append("> on system reset. They pass through the VID_RST inverter chain (8 gates). While")
    lines.append("> they are the deepest paths overall, they don't affect per-dot rendering timing.")
    lines.append("> Operational paths fire every dot or scanline during normal rendering and are")
    lines.append("> the ones that cause observable timing discrepancies in emulators.\n")

    lines.append("## Key Findings for Emulator Developers\n")

    lines.append("### The Core Problem\n")
    lines.append("A behavioral emulator resolves all combinatorial logic instantaneously within a")
    lines.append("single tick. On real hardware, signals propagate through chains of gates with")
    lines.append("finite delay. When two signals feed into the same flip-flop but arrive at")
    lines.append("different times, the hardware may capture a different value than an emulator")
    lines.append("that resolves both signals simultaneously.\n")
    lines.append(f"This analysis identifies **{len(races)}** signal race points where inputs to a single")
    lines.append("decision point differ by 3 or more gate depths. The largest differentials")
    lines.append("exceed a full half T-cycle, meaning the late signal may not settle before")
    lines.append("the next clock edge.\n")

    lines.append("### The Two Dominant Late-Arriving Signal Classes\n")
    lines.append("Almost every significant race in the PPU involves one of two late-arriving signal types:\n")
    lines.append("1. **CLKPIPE (pixel pipe shift clock)** — 52 fan-out, feeds every pixel-level")
    lines.append("   decision. Arrives through a long clock buffer chain. The pipe shift clock is")
    lines.append("   the latest signal to settle at every pixel pipeline DFF, meaning the pipe")
    lines.append("   effectively shifts one propagation delay after the data it's shifting is ready.")
    lines.append("   This affects: sprite pipe timing, fine scroll match, pixel counter, window fetch.\n")
    lines.append("2. **Line/fetch reset signals** (NYXU_BFETCH_RSTn, ATEJ_LINE_RST_TRIGp) —")
    lines.append("   these pass through the VID_RST chain (8 gates from AFER+LCDC) then through")
    lines.append("   line-end and scan-done logic. They arrive 15-17 gates after the data signals")
    lines.append("   they reset. This affects: tile fetch counter, scan done, sprite store reset.\n")

    lines.append("### What This Means in Practice\n")
    lines.append("| Emulator Assumption | Hardware Reality | Affected Behavior |")
    lines.append("|---------------------|-----------------|-------------------|")
    lines.append("| Pixel pipe shifts when CLKPIPE fires | Pipe data is ready ~80-240ns before CLKPIPE arrives | Sprite/BG pixel positioning may be off by one dot |")
    lines.append("| Fine scroll match resolves same dot as pixel counter | SCX fine match (depth 3) is ready long before CLKPIPE (depth 16) | Fine scroll may effectively apply one dot late |")
    lines.append("| Tile fetch resets instantly when conditions are met | BFETCH reset (depth 17) arrives after fetch counter clock (depth 7) | Fetch state machine may run one extra cycle before reset |")
    lines.append("| Sprite store X regs reset on line reset | Store reset (depth 17) arrives long after sprite X data (depth 1) | Sprite position capture at line boundaries may be one dot off |")
    lines.append("| Scan done immediately stops OAM scan | Scan done signal (depth 17) races against line end (depth 0) | OAM scan may run one dot longer than expected |")
    lines.append("")
    lines.append("### Caveats\n")
    lines.append("- Gate delay estimates (5-15ns) are rough. Actual delays depend on fan-out,")
    lines.append("  wire length, and process variation. The relative rankings are more reliable")
    lines.append("  than the absolute nanosecond estimates.")
    lines.append("- Not all races produce observable effects. A race only matters if the late")
    lines.append("  signal's arrival changes the captured value — which depends on the specific")
    lines.append("  input data at that moment.")
    lines.append("- The parser captures ~96% of signals (121 unresolved references remain,")
    lines.append("  mostly CPU address bus bits). Reported depths are lower bounds.")
    lines.append("- This analysis is structural, not temporal. It identifies *where* races")
    lines.append("  exist, not *when* they fire during a frame. Cross-referencing with specific")
    lines.append("  test ROM failures would validate which races produce observable effects.\n")

    lines.append("## Report Files\n")
    lines.append("- [Operational Paths](operational_paths.md) — per-dot/per-scanline paths grouped by functional area")
    lines.append("- [Signal Race Pairs](race_pairs_report.md) — timing races with observable effects")
    lines.append("- [Reset Paths](reset_paths.md) — paths that only fire on system reset / LCDC toggle")
    lines.append("- [Depth Distribution](depth_distribution.md) — histogram of path depths")

    sections['critical_paths_report.md'] = "\n".join(lines)

    # =========================================================================
    # OPERATIONAL PATHS — grouped by category
    # =========================================================================
    lines = []
    lines.append("# Operational Paths (by functional area)\n")
    lines.append("Paths that fire every dot or scanline during normal rendering.")
    lines.append("These are the ones that cause observable timing discrepancies in emulators.\n")

    # Categorize operational paths
    categories = {}
    for depth, path in operational:
        cat = categorize_path(path, G)
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((depth, path))

    # Sort categories by max depth
    cat_order = sorted(categories.keys(), key=lambda c: -categories[c][0][0])

    # Summary table
    lines.append("| Functional Area | Paths | Max Depth | Max Delay | Key Sinks |")
    lines.append("|-----------------|-------|-----------|-----------|-----------|")
    for cat in cat_order:
        cat_paths = categories[cat]
        max_d = cat_paths[0][0]
        # Unique sinks for this category (top 3)
        sinks = []
        seen = set()
        for _, p in cat_paths:
            s = _display(G, p[-1])
            if s not in seen:
                sinks.append(s)
                seen.add(s)
            if len(sinks) >= 3:
                break
        sinks_str = ', '.join(f'`{s}`' for s in sinks)
        lines.append(f"| {cat} | {len(cat_paths)} | {max_d} | {max_d*15} ns | {sinks_str} |")
    lines.append("")

    # Top fan-out nodes (operational bottlenecks)
    lines.append("### Key Bottleneck Nodes (highest fan-out)\n")
    lines.append("These nodes drive the most downstream signals. Propagation delay")
    lines.append("at these nodes has the widest impact on timing.\n")
    lines.append("| Node | Fan-out | Type | Source |")
    lines.append("|------|---------|------|--------|")
    # Show all high fan-out nodes in the graph (not just operational path members)
    fo_ranked = sorted(
        [(n, fanout[n]) for n in G.nodes() if fanout.get(n, 0) >= 10],
        key=lambda x: -x[1]
    )
    for node_name, fo in fo_ranked[:20]:
        nd = G.nodes.get(node_name, {})
        dn = _display(G, node_name)
        sf = nd.get('source_file', '')
        sl = nd.get('source_line', '')
        nt = nd.get('node_type', '')
        gf = nd.get('gate_func', '')
        type_str = gf if gf else nt
        lines.append(f"| `{dn}` | {fo} | {type_str} | {sf}:{sl} |")
    lines.append("")

    # Detailed paths per category
    for cat in cat_order:
        cat_paths = categories[cat]
        max_d = cat_paths[0][0]
        lines.append(f"### {cat} (max depth {max_d}, {len(cat_paths)} paths)\n")

        # Show the deepest unique path per sink
        seen_sinks = set()
        shown = 0
        for depth, path in cat_paths:
            sink = _display(G, path[-1])
            if sink in seen_sinks:
                continue
            seen_sinks.add(sink)
            if shown >= 5:  # max 5 unique paths per category
                remaining = len(cat_paths) - shown
                if remaining > 0:
                    lines.append(f"*...and {remaining} more paths in this category.*\n")
                break

            src_node = G.nodes.get(path[0], {})
            dst_node = G.nodes.get(path[-1], {})
            min_delay = depth * 5
            max_delay = depth * 15
            pct = max_delay / 119.2 * 100

            src_phase = get_phase(G, path[0])
            sink_phase = get_phase(G, path[-1])
            phase_note = ""
            if src_phase or sink_phase:
                parts = []
                if src_phase: parts.append(f"src @{src_phase}")
                if sink_phase: parts.append(f"sink @{sink_phase}")
                phase_note = f" [{', '.join(parts)}]"

            lines.append(f"**Depth {depth}** ({min_delay}-{max_delay} ns, {pct:.0f}% half T-cycle): "
                         f"`{_display(G, path[0])}` -> `{sink}`{phase_note}\n")
            lines.append(format_path_trace(path, G, fanout))
            lines.append("")
            shown += 1

    sections['operational_paths.md'] = "\n".join(lines)

    # =========================================================================
    # RESET PATHS — summary only
    # =========================================================================
    lines = []
    lines.append("# Reset Paths\n")
    lines.append("These paths only fire on system reset or LCDC bit 7 toggle. They all share")
    lines.append("the VID_RST inverter chain prefix (8 gates from AFER_SYS_RSTp through XAPO/ATAR/ABEZ).\n")

    # Categorize reset paths
    reset_cats = {}
    for depth, path in reset:
        cat = categorize_path(path, G)
        if cat not in reset_cats:
            reset_cats[cat] = []
        reset_cats[cat].append((depth, path))

    reset_cat_order = sorted(reset_cats.keys(), key=lambda c: -reset_cats[c][0][0])

    lines.append("| Area | Paths | Max Depth | Deepest Sink |")
    lines.append("|------|-------|-----------|-------------|")
    for cat in reset_cat_order:
        rp = reset_cats[cat]
        lines.append(f"| {cat} | {len(rp)} | {rp[0][0]} | `{_display(G, rp[0][1][-1])}` |")
    lines.append("")

    # Show just the single deepest reset path as an example
    if reset:
        depth, path = reset[0]
        lines.append(f"**Deepest reset path** (depth {depth}): "
                     f"`{_display(G, path[0])}` -> `{_display(G, path[-1])}`\n")
        lines.append(format_path_trace(path, G, fanout))
        lines.append("")

    sections['reset_paths.md'] = "\n".join(lines)

    # =========================================================================
    # SIGNAL RACE PAIRS
    # =========================================================================
    lines = []
    if races:
        lines.append("# Signal Race Pairs\n")
        lines.append("A race pair occurs when a registered element (DFF/latch) has two or more inputs")
        lines.append("that arrive at significantly different combinatorial depths. In real hardware,")
        lines.append("the late-arriving signal may not be stable when the DFF samples. A behavioral")
        lines.append("emulator resolves all inputs instantly, hiding this timing asymmetry.\n")
        lines.append("> **How to read this:** A depth differential of N means one input passes through")
        lines.append("> N more gates than another before reaching the same decision point. At 5-15 ns")
        lines.append("> per gate, a differential of 10 means one signal arrives 50-150 ns later.\n")

        # Filter to PPU-relevant races, skip reset-dominated
        ppu_cats = {'Scroll/Fine Timing', 'Window Logic', 'Pixel Pipeline', 'Pixel Counter',
                    'Sprite Store/Match', 'Sprite Fetcher', 'Sprite Scanner', 'Tile Fetcher',
                    'STAT/LY Match', 'Mode/Rendering Control', 'OAM Bus', 'VRAM Bus',
                    'Line Timing', 'LX Counter', 'PPU Registers', 'Interrupts', 'DMA',
                    'LYC Register', 'LY Counter'}

        # Remove races whose late input comes through VID_RST (reset-only)
        def is_operational_race(r):
            for inp in r['inputs']:
                name = inp['name'].upper()
                if any(x in name for x in ['VID_RST', 'XAPO', 'ATAR', 'ABEZ', 'LYFE', 'TOFU', 'ROSY', 'PYRY']):
                    if inp['depth'] == r['max_depth']:  # the late signal is the reset chain
                        return False
            return True

        op_races = [r for r in races if is_operational_race(r)]

        lines.append(f"Found **{len(op_races)}** operational race points (depth diff >= 3, excluding reset chains).\n")

        # Summary table of top races with observable effects
        lines.append("### Top Race Pairs by Depth Differential\n")
        lines.append("| Decision Point | Type | Depth Diff | Phase | Late Signal (depth) | Early Signal (depth) | Observable Effect |")
        lines.append("|----------------|------|-----------|-------|--------------------|--------------------|-------------------|")

        seen_nodes = set()
        shown = 0
        for r in op_races:
            if r['display_name'] in seen_nodes:
                continue
            seen_nodes.add(r['display_name'])
            if shown >= 30:
                break

            late = r['inputs'][0]
            early = r['inputs'][-1]
            phase_str = ""
            if late['phase'] and early['phase'] and late['phase'] != early['phase']:
                phase_str = f"{late['phase']}/{early['phase']}"
            elif late['phase']:
                phase_str = late['phase']
            elif early['phase']:
                phase_str = early['phase']

            effect_summary, _ = observable_effect(r)

            lines.append(
                f"| `{r['display_name']}` | {r['reg_type']} | **{r['depth_diff']}** | "
                f"{phase_str} | "
                f"`{late['name']}` ({late['depth']}) | "
                f"`{early['name']}` ({early['depth']}) | "
                f"{effect_summary} |"
            )
            shown += 1
        lines.append("")

        # Observable effects guide — grouped by symptom
        lines.append("### Observable Effects Guide\n")
        lines.append("Grouped by the visible symptom an emulator would exhibit if it resolves")
        lines.append("these races instantaneously (as all behavioral emulators do).\n")

        # Group races by effect summary
        effect_groups = {}
        seen_for_effects = set()
        for r in op_races:
            if r['display_name'] in seen_for_effects:
                continue
            seen_for_effects.add(r['display_name'])
            effect_summary, effect_detail = observable_effect(r)
            if effect_summary not in effect_groups:
                effect_groups[effect_summary] = {
                    'detail': effect_detail,
                    'races': [],
                    'max_diff': 0,
                }
            effect_groups[effect_summary]['races'].append(r)
            effect_groups[effect_summary]['max_diff'] = max(
                effect_groups[effect_summary]['max_diff'], r['depth_diff']
            )

        # Sort by max depth differential
        sorted_effects = sorted(effect_groups.items(), key=lambda x: -x[1]['max_diff'])

        for effect_summary, group in sorted_effects:
            if group['max_diff'] < 5:
                continue  # skip low-differential races for readability
            race_count = len(group['races'])
            lines.append(f"#### {effect_summary}\n")
            lines.append(f"**Affected decision points:** {race_count} | "
                         f"**Max depth differential:** {group['max_diff']} gates "
                         f"({group['max_diff']*5}-{group['max_diff']*15} ns)\n")
            lines.append(f"{group['detail']}\n")

            # Show the specific DFFs involved
            if race_count <= 8:
                dff_list = ', '.join(f"`{r['display_name']}`" for r in group['races'])
                lines.append(f"Decision points: {dff_list}\n")
            else:
                sample = ', '.join(f"`{r['display_name']}`" for r in group['races'][:5])
                lines.append(f"Decision points (sample): {sample}, ... and {race_count - 5} more\n")
        lines.append("")

        # Detailed analysis of top 10 most interesting races
        lines.append("### Detailed Race Analysis\n")

        seen_nodes = set()
        shown = 0
        for r in op_races:
            if r['display_name'] in seen_nodes:
                continue
            seen_nodes.add(r['display_name'])
            if shown >= 10:
                break

            effect_summary, effect_detail = observable_effect(r)

            lines.append(f"#### `{r['display_name']}` (diff: {r['depth_diff']} gates, "
                         f"{r['source_file']}:{r['source_line']})\n")
            lines.append(f"Type: {r['node_type']} ({r['reg_type']})")
            # Show phase info for the decision point
            decision_phase = get_phase(G, r['node'])
            if decision_phase:
                lines.append(f" | Active phase: **{decision_phase}**")
            lines.append("")

            lines.append(f"**Observable effect:** {effect_summary}\n")

            lines.append("| Input | Depth | Gate | Phase | Role |")
            lines.append("|-------|-------|------|-------|------|")

            for inp in r['inputs']:
                role = "**LATE**" if inp['depth'] == r['max_depth'] else ("early" if inp['depth'] == r['min_depth'] else "mid")
                delay_est = f"{inp['depth']*5}-{inp['depth']*15} ns" if inp['depth'] > 0 else "0 ns"
                lines.append(
                    f"| `{inp['name']}` | {inp['depth']} ({delay_est}) | "
                    f"{inp['gate_func'] or inp['node_type']} | {inp['phase'] or '-'} | {role} |"
                )
            lines.append("")

            # Explain the consequence
            diff_min = r['depth_diff'] * 5
            diff_max = r['depth_diff'] * 15
            lines.append(f"The late-arriving signal reaches `{r['display_name']}` **{diff_min}-{diff_max} ns** "
                         f"after the earliest input. ")
            pct_ht = diff_max / 119.2 * 100
            if diff_max > 119:
                lines.append(f"This exceeds a half T-cycle ({pct_ht:.0f}%), meaning the late signal "
                             f"may not settle before the next clock edge.\n")
            elif diff_max > 60:
                lines.append(f"This is a significant fraction of a half T-cycle ({pct_ht:.0f}%), "
                             f"making this a likely source of one-dot timing discrepancies.\n")
            else:
                lines.append(f"This is {pct_ht:.0f}% of a half T-cycle.\n")

            lines.append(f"> {effect_detail}\n")

            shown += 1

    sections['race_pairs_report.md'] = "\n".join(lines)

    # =========================================================================
    # DEPTH DISTRIBUTION
    # =========================================================================
    lines = []
    lines.append("# Depth Distribution (all paths)\n")

    depth_counts_op = {}
    for depth, _ in operational:
        depth_counts_op[depth] = depth_counts_op.get(depth, 0) + 1
    depth_counts_rst = {}
    for depth, _ in reset:
        depth_counts_rst[depth] = depth_counts_rst.get(depth, 0) + 1

    all_depths = sorted(set(list(depth_counts_op.keys()) + list(depth_counts_rst.keys())), reverse=True)

    lines.append("| Depth | Operational | Reset | Total | Est. Delay (max) | % Half T-cycle |")
    lines.append("|-------|------------|-------|-------|------------------|----------------|")
    for d in all_depths:
        op_count = depth_counts_op.get(d, 0)
        rst_count = depth_counts_rst.get(d, 0)
        total = op_count + rst_count
        max_delay = d * 15
        pct = max_delay / 119.2 * 100
        flag = " **!**" if pct > 50 else ""
        lines.append(f"| {d} | {op_count} | {rst_count} | {total} | {max_delay} ns | {pct:.0f}%{flag} |")
    lines.append("")

    sections['depth_distribution.md'] = "\n".join(lines)

    return sections


# ============================================================================
# Serialization
# ============================================================================

def export_graph_json(G, filepath: Path):
    """Export graph to JSON format."""
    data = {
        "nodes": [],
        "edges": [],
    }

    for name, attrs in G.nodes(data=True):
        phase = get_phase(G, name)
        node_data = {
            "name": name,
            "display_name": attrs.get('display_name', display_name_from_scoped(name)),
            **{k: v for k, v in attrs.items() if v and k != 'display_name'},
        }
        if phase:
            node_data["phase"] = phase
        data["nodes"].append(node_data)

    for src, dst, attrs in G.edges(data=True):
        data["edges"].append({
            "src": src,
            "dst": dst,
            **{k: v for k, v in attrs.items() if v},
        })

    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nGraph exported to {filepath}")
    print(f"  {len(data['nodes'])} nodes, {len(data['edges'])} edges")


def export_paths_json(paths, G, filepath: Path):
    """Export critical paths to JSON with classification metadata."""
    fanout = compute_fanout(G)
    data = []
    for depth, path in paths:
        src_phase = get_phase(G, path[0])
        sink_phase = get_phase(G, path[-1])
        path_data = {
            "depth": depth,
            "min_delay_ns": depth * 5,
            "max_delay_ns": depth * 15,
            "pct_half_tcycle": round(depth * 15 / 119.2 * 100, 1),
            "source": _display(G, path[0]),
            "sink": _display(G, path[-1]),
            "source_phase": src_phase,
            "sink_phase": sink_phase,
            "is_reset": is_reset_path(path, G),
            "category": categorize_path(path, G),
            "nodes": [],
        }
        for node_name in path:
            nd = G.nodes.get(node_name, {})
            path_data["nodes"].append({
                "name": node_name,
                "display_name": _display(G, node_name),
                "node_type": nd.get('node_type', ''),
                "gate_func": nd.get('gate_func', ''),
                "source_file": nd.get('source_file', ''),
                "source_line": nd.get('source_line', 0),
                "fan_out": fanout.get(node_name, 0),
                "phase": get_phase(G, node_name),
            })
        data.append(path_data)

    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Critical paths exported to {filepath}")


def export_dot(paths, G, filepath: Path, max_paths=20):
    """Export top critical paths as a DOT graph for Graphviz visualization."""
    fanout = compute_fanout(G)

    # Collect unique nodes and edges from top operational paths
    operational = [(d, p) for d, p in paths if not is_reset_path(p, G)]

    # Take the deepest unique-sink path per category
    seen_sinks = set()
    selected = []
    for depth, path in operational:
        sink = _display(G, path[-1])
        if sink not in seen_sinks:
            seen_sinks.add(sink)
            selected.append((depth, path))
        if len(selected) >= max_paths:
            break

    dot_nodes = {}  # node_name -> attributes
    dot_edges = set()

    for depth, path in selected:
        for i, node_name in enumerate(path):
            nd = G.nodes.get(node_name, {})
            dn = _display(G, node_name)
            nt = nd.get('node_type', '')
            gf = nd.get('gate_func', '')
            fo = fanout.get(node_name, 0)

            if nt in ('registered', 'bus', 'boundary'):
                shape = 'box'
                color = '#4A90D9' if nt == 'registered' else ('#D4A44A' if nt == 'bus' else '#888888')
                style = 'filled'
            else:
                shape = 'ellipse'
                color = '#FF6B6B' if fo >= 20 else ('#FFB366' if fo >= 10 else '#DDDDDD')
                style = 'filled'

            label = dn
            if fo >= 10:
                label += f'\\n(fan-out: {fo})'

            dot_nodes[node_name] = {
                'label': label,
                'shape': shape,
                'fillcolor': color,
                'style': style,
            }

            if i > 0:
                dot_edges.add((path[i-1], node_name))

    lines = ['digraph ppu_critical_paths {']
    lines.append('  rankdir=TB;')
    lines.append('  node [fontname="Courier", fontsize=10];')
    lines.append('  edge [color="#666666"];')
    lines.append('')
    lines.append('  // Legend')
    lines.append('  subgraph cluster_legend {')
    lines.append('    label="Legend";')
    lines.append('    style=dashed;')
    lines.append('    leg_reg [label="Registered\\n(DFF/Latch)" shape=box fillcolor="#4A90D9" style=filled];')
    lines.append('    leg_bus [label="Bus" shape=box fillcolor="#D4A44A" style=filled];')
    lines.append('    leg_comb [label="Combinatorial" shape=ellipse fillcolor="#DDDDDD" style=filled];')
    lines.append('    leg_hot [label="High fan-out\\n(>=10)" shape=ellipse fillcolor="#FFB366" style=filled];')
    lines.append('    leg_crit [label="Critical fan-out\\n(>=20)" shape=ellipse fillcolor="#FF6B6B" style=filled];')
    lines.append('  }')
    lines.append('')

    for node_name, attrs in dot_nodes.items():
        safe_id = node_name.replace(':', '_').replace('.', '_').replace('@', '_at_')
        attr_str = ', '.join(f'{k}="{v}"' for k, v in attrs.items())
        lines.append(f'  "{safe_id}" [{attr_str}];')

    lines.append('')
    for src, dst in dot_edges:
        safe_src = src.replace(':', '_').replace('.', '_').replace('@', '_at_')
        safe_dst = dst.replace(':', '_').replace('.', '_').replace('@', '_at_')
        lines.append(f'  "{safe_src}" -> "{safe_dst}";')

    lines.append('}')

    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))

    print(f"DOT graph exported to {filepath}")
    print(f"  Render with: dot -Tsvg {filepath} -o {filepath.with_suffix('.svg')}")


# ============================================================================
# Main
# ============================================================================

def main():
    print("Game Boy PPU Signal Dependency Parser")
    print("=" * 50)

    result = ParseResult()

    # Phase 1: Parse computed methods first so their global nodes exist
    # when we parse the gate files
    print("\nParsing computed methods...")
    for fname in COMPUTED_METHOD_FILES:
        filepath = GATEBOY_SRC / fname
        parse_computed_methods(filepath, result)

    print(f"  Computed method nodes: {len(result.computed_methods)}")

    # Phase 2: Parse all gate logic files
    print("\nParsing source files...")
    for fname in GATE_FILES:
        filepath = GATEBOY_SRC / fname
        parse_file(filepath, result)

    print(f"\nRaw parse: {len(result.nodes)} nodes, {len(result.edges)} edges")
    scoped_wire_count = sum(len(v) for v in result.wire_scopes.values())
    dup_wire_names = sum(1 for v in result.wire_scopes.values() if len(v) > 1)
    print(f"  Scoped wires: {scoped_wire_count} ({dup_wire_names} wire names appear in multiple files)")

    # Classify gate_output nodes as combinatorial
    classify_gate_outputs(result)

    # Resolve edges with file-scoped lookup
    unknown = resolve_scoped_edges(result)
    print(f"Resolved edges: {len(result.edges)} (removed refs to {len(unknown)} unknown signals)")

    if unknown:
        sample = sorted(unknown)[:20]
        print(f"  Sample unknown refs: {', '.join(sample)}")

    # Build networkx graph
    print("\nBuilding graph...")
    G = build_graph(result)

    stats = graph_stats(G)
    print(f"\nGraph Statistics:")
    print(f"  Total nodes: {stats['total_nodes']}")
    print(f"  Total edges: {stats['total_edges']}")
    print(f"  Node types: {stats['node_types']}")
    print(f"  Registered: {stats['registered_nodes']}, Combinatorial: {stats['combinatorial_nodes']}")
    print(f"  Connected components: {stats['weakly_connected_components']}")
    print(f"  Has cycles: {stats['has_cycles']}")
    if stats['has_cycles']:
        print(f"  Cycle sample: {stats['cycle_sample']}")

    # Build DAG for analysis (break cycles)
    print("\nBuilding DAG (breaking cycles)...")
    DAG, removed_edges = build_dag_for_analysis(G)
    print(f"  Removed {len(removed_edges)} edges to break cycles")
    for src, dst in removed_edges[:10]:
        print(f"    {_display(G, src)} -> {_display(G, dst)}")

    # Critical path analysis
    print("\nFinding critical paths...")
    paths = find_critical_paths(DAG, G)
    print(f"  Found {len(paths)} paths")
    if paths:
        print(f"  Deepest: {paths[0][0]} gates")
        print(f"  Top 10 depths: {[p[0] for p in paths[:10]]}")

    # Race pair detection
    print("\nFinding signal race pairs...")
    races = find_race_pairs(DAG, G)
    print(f"  Found {len(races)} race points (depth diff >= 3)")
    if races:
        print(f"  Largest differential: {races[0]['depth_diff']} gates at {races[0]['display_name']}")

    # Export everything
    out_dir = Path("output")
    export_graph_json(G, out_dir / "ppu_graph.json")
    export_paths_json(paths, G, out_dir / "critical_paths.json")

    # Export race pairs
    race_path = out_dir / "race_pairs.json"
    with open(race_path, 'w') as f:
        json.dump(races, f, indent=2)
    print(f"Race pairs exported to {race_path}")

    # Write human-readable report (split into sections)
    report_sections = format_report_sections(paths, G, races)
    for filename, content in report_sections.items():
        report_path = out_dir / filename
        with open(report_path, 'w') as f:
            f.write(content)
        print(f"Report section written to {report_path}")

    # Export DOT graph
    export_dot(paths, G, out_dir / "critical_paths.dot")

    # Write stats
    stats_path = Path("output/graph-stats.md")
    with open(stats_path, 'w') as f:
        f.write("# Game Boy PPU Dependency Graph — Statistics\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total nodes | {stats['total_nodes']} |\n")
        f.write(f"| Total edges | {stats['total_edges']} |\n")
        f.write(f"| Registered nodes | {stats['registered_nodes']} |\n")
        f.write(f"| Combinatorial nodes | {stats['combinatorial_nodes']} |\n")
        f.write(f"| Connected components | {stats['weakly_connected_components']} |\n")
        f.write(f"| Has cycles | {stats['has_cycles']} |\n")
        f.write(f"| Cycle-breaking edges removed | {len(removed_edges)} |\n\n")
        f.write("## Node Type Breakdown\n\n")
        f.write("| Type | Count |\n")
        f.write("|------|-------|\n")
        for t, c in sorted(stats['node_types'].items()):
            f.write(f"| {t} | {c} |\n")
        if removed_edges:
            f.write(f"\n## Cycle-Breaking Edges\n\n")
            f.write("These edges were removed to create a DAG for path analysis.\n")
            f.write("They represent feedback loops (typically through async set/reset of DFFs).\n\n")
            for src, dst in removed_edges:
                f.write(f"- `{_display(G, src)}` -> `{_display(G, dst)}`\n")

    print(f"Stats written to {stats_path}")

    return G, DAG, paths


if __name__ == "__main__":
    G, DAG, paths = main()
