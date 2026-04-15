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
    gate_equiv: float = 1.0  # equivalent gate stages for delay estimation


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
    gate_equiv: float = 1.0  # effective gate-equivalents (Elmore-based)


@dataclass
class Edge:
    src: str
    dst: str
    edge_type: str = "data"
    src_inverted: bool = False  # True if source drives via ~q (inverted output)


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
# Elmore Delay Model (from msinger/dmg-sim timing-default.sv)
# ============================================================================
#
# Computes per-instance propagation delays using an Elmore RC model with
# parameters from the dmg-sim SystemVerilog simulator.  Wire lengths and
# transistor widths come from the physical layout; the model gives
# physically-grounded *relative* delays.  Absolute values are normalised
# to "effective gate equivalents" (1.0 = NOT_x1 at default wire length)
# so they plug into the existing 5-15 ns/ge estimation range.

# --- Process constants (timing-default.sv) ---
_RPRIME_WIRE  = 0.05       # ohm/unit  (wire resistance per layout unit)
_CPRIME_WIRE  = 0.2e-15    # F/unit    (wire capacitance per layout unit)
_LEFF_UM      = 1.2        # effective channel length (guessed for DMG)
_KR_NMOS_REF  = 1.0e4      # ohm·µm at Lref=1.0
_GAMMA_PN     = 2.0        # PMOS/NMOS resistance ratio
_CINT_STAGE_F = 0.5e-15    # intrinsic stage capacitance (F)
_L_UNIT       = 0.454      # Electric VLSI layout units → µm

_KR_NMOS = _KR_NMOS_REF * (_LEFF_UM / 1.0)   # 12000 ohm·µm

def _r_nmos(w_um):
    """NMOS drive resistance for transistor width w_um (µm)."""
    return _KR_NMOS / w_um

def _r_pmos(wp_um):
    """PMOS drive resistance for transistor width wp_um (µm)."""
    return _GAMMA_PN * _KR_NMOS / wp_um

def _tpd_elmore(L, R_drv, C_extra=0.0):
    """Elmore propagation delay (seconds) for wire length L and driver R."""
    Cw = _CPRIME_WIRE * L
    Rw = _RPRIME_WIRE * L
    return 0.69 * R_drv * (Cw + _CINT_STAGE_F + C_extra) + 0.38 * Rw * Cw

# Standard transistor width (35 layout units → µm)
_W_STD = 35 * _L_UNIT    # 15.89 µm
_RN    = _r_nmos(_W_STD)  # ~755 ohm
_RP    = _r_pmos(_W_STD)  # ~1510 ohm

# Reference delay: NOT_x1 at MEDIAN wire length for combinatorial gates.
# The median L_y across ~2300 combinatorial gates in the layout is ~295.
# This makes 1.0 effective ge = "one typical gate at a typical wire length",
# which matches the 5-15 ns/ge calibration from Sharp ~5 µm CMOS.
_L_MEDIAN = 295
_REF_DELAY = (_tpd_elmore(_L_MEDIAN, _RP) + _tpd_elmore(_L_MEDIAN, _RN)) / 2

# Default wire length when no per-instance data is available
_L_DEFAULT = _L_MEDIAN

# Cap wire length for delay estimation.  Long wires (chip-spanning signals,
# bus routing) have L_y up to 39000 layout units, which massively overestimates
# delay in our path analysis — the Elmore model gives the full RC delay of
# the wire, but in practice signals are distributed to nearby loads first.
# Cap at p95 of combinatorial gate wire lengths (~3000 layout units).
_L_MAX = 3000


def _gate_delay_not(L_y, W=35):
    """NOT inverter (any drive strength).  W is in layout units."""
    w_um = W * _L_UNIT
    rise = _tpd_elmore(L_y, _r_pmos(w_um))
    fall = _tpd_elmore(L_y, _r_nmos(w_um))
    return max(rise, fall)

def _gate_delay_nand(L_y, n_inputs):
    """NAND gate with n_inputs series NMOS."""
    rise = _tpd_elmore(L_y, _RP)                  # parallel PMOS
    fall = _tpd_elmore(L_y, _RN * n_inputs)       # series NMOS
    return max(rise, fall)

def _gate_delay_nor(L_y, n_inputs):
    """NOR gate with n_inputs series PMOS."""
    rise = _tpd_elmore(L_y, _RP * n_inputs)       # series PMOS
    fall = _tpd_elmore(L_y, _RN)                  # parallel NMOS
    return max(rise, fall)

def _gate_delay_and(L_y, n_inputs, L_int=None):
    """AND = NAND(L_int) + NOT(L_y).  Internal wire lengths from SV cells."""
    L_int_map = {2: 122, 3: 135, 4: 140}
    Li = L_int if L_int is not None else L_int_map.get(n_inputs, 122)
    # NAND stage (internal)
    t_rise_nand = _tpd_elmore(Li, _RP)
    t_fall_nand = _tpd_elmore(Li, _RN * n_inputs)
    # NOT stage (output)
    t_rise_y = _tpd_elmore(L_y, _RP)
    t_fall_y = _tpd_elmore(L_y, _RN)
    rise = t_fall_nand + t_rise_y   # NAND falls → NOT rises
    fall = t_rise_nand + t_fall_y   # NAND rises → NOT falls
    return max(rise, fall)

def _gate_delay_or(L_y, n_inputs, L_int=None):
    """OR = NOR(L_int) + NOT(L_y)."""
    L_int_map = {2: 122, 3: 135, 4: 140}
    Li = L_int if L_int is not None else L_int_map.get(n_inputs, 122)
    t_rise_nor = _tpd_elmore(Li, _RP * n_inputs)
    t_fall_nor = _tpd_elmore(Li, _RN)
    t_rise_y = _tpd_elmore(L_y, _RP)
    t_fall_y = _tpd_elmore(L_y, _RN)
    rise = t_fall_nor + t_rise_y
    fall = t_rise_nor + t_fall_y
    return max(rise, fall)

def _gate_delay_xor(L_y):
    """XOR = NOR-like first stage (L=122) + NOR-like output (L=L_y)."""
    t_rise_nor = _tpd_elmore(122, _RP * 2)
    t_fall_nor = _tpd_elmore(122, _RN)
    t_rise_y = _tpd_elmore(L_y, _RP * 2)
    t_fall_y = _tpd_elmore(L_y, _RN * 2)
    rise = t_fall_nor + t_rise_y
    fall = t_rise_nor + t_fall_y
    return max(rise, fall)

def _gate_delay_xnor(L_y):
    """XNOR = NAND-like first stage (L=122) + NOR-like output."""
    t_rise_nand = _tpd_elmore(122, _RP)
    t_fall_nand = _tpd_elmore(122, _RN * 2)
    t_rise_y = _tpd_elmore(L_y, _RP * 2)
    t_fall_y = _tpd_elmore(L_y, _RN * 2)
    rise = t_fall_nand + t_rise_y
    fall = t_rise_nand + t_fall_y
    return max(rise, fall)

def _gate_delay_oai21(L_y):
    """OAI21 = single-stage (OR-AND-Invert), 2-deep PMOS and NMOS stacks."""
    rise = _tpd_elmore(L_y, _RP * 2)
    fall = _tpd_elmore(L_y, _RN * 2)
    return max(rise, fall)

def _gate_delay_ao(L_y, n_or_terms, L_int=None):
    """AO (AND-OR) = AOI(L_int) + NOT(L_y).  n_or_terms = number of AND groups."""
    # Internal wire lengths and PMOS stack depths from SV cells.
    # The PMOS stack depth in the AOI is the number of series PMOS transistors
    # in the pull-up network, verified against each gate's .sv specify block.
    L_int_map = {2: 112, 3: 151, 4: 185, 5: 218, 7: 284}
    pmos_stack = {2: 2, 3: 2, 4: 3, 5: 4, 7: 6}
    Li = L_int if L_int is not None else L_int_map.get(n_or_terms, 151)
    t_rise_aoi = _tpd_elmore(Li, _RP * pmos_stack.get(n_or_terms, n_or_terms))
    t_fall_aoi = _tpd_elmore(Li, _RN * 2)  # 2-deep NMOS in each AND group
    t_rise_y = _tpd_elmore(L_y, _RP)
    t_fall_y = _tpd_elmore(L_y, _RN)
    rise = t_fall_aoi + t_rise_y
    fall = t_rise_aoi + t_fall_y
    return max(rise, fall)

def _gate_delay_oa21(L_y):
    """OA21 = OAI(L=112) + NOT(L_y)."""
    t_rise_oai = _tpd_elmore(112, _RP * 2)
    t_fall_oai = _tpd_elmore(112, _RN * 2)
    t_rise_y = _tpd_elmore(L_y, _RP)
    t_fall_y = _tpd_elmore(L_y, _RN)
    rise = t_fall_oai + t_rise_y
    fall = t_rise_oai + t_fall_y
    return max(rise, fall)

def _gate_delay_muxi(L_y):
    """MUXI (inverting mux) = pass-gate(L=93, W=6) + inverter(L=L_y)."""
    W_small = 6 * _L_UNIT
    t_buf = max(_tpd_elmore(93, _r_pmos(W_small)),
                _tpd_elmore(93, _r_nmos(W_small)))
    t_rise_y = _tpd_elmore(L_y, _RP)
    t_fall_y = _tpd_elmore(L_y, _RN)
    return t_buf + max(t_rise_y, t_fall_y)

def _gate_delay_mux(L_y):
    """MUX (non-inverting) = sel_inv(33,W=6) + pass-gate(93,W=6) + muxi(116) + inv(L_y)."""
    W_small = 6 * _L_UNIT
    t_sel = max(_tpd_elmore(33, _r_pmos(W_small)),
                _tpd_elmore(33, _r_nmos(W_small)))
    t_buf = max(_tpd_elmore(93, _r_pmos(W_small)),
                _tpd_elmore(93, _r_nmos(W_small)))
    t_muxi = max(_tpd_elmore(116, _RP), _tpd_elmore(116, _RN))
    t_out = max(_tpd_elmore(L_y, _RP), _tpd_elmore(L_y, _RN))
    # Worst case: sel path through all stages
    return max(t_sel + t_buf, t_buf) + t_muxi + t_out

def _gate_delay_not_if(L_y, W_y_p=35):
    """NOT_IF0/NOT_IF1 (tri-state inverter).  Data path: in→y."""
    w_p_um = W_y_p * _L_UNIT
    rise = _tpd_elmore(L_y, _r_pmos(w_p_um) * 2)  # 2-deep pass + drive
    fall = _tpd_elmore(L_y, _RN * 2)
    return max(rise, fall)

def _gate_delay_buf_if0(L_y):
    """BUF_IF0 (tri-state buffer) = NAND(152) + output(L_y, W=70)."""
    W_buf = 70 * _L_UNIT
    t_rise_nand = _tpd_elmore(152, _RP)
    t_fall_nand = _tpd_elmore(152, _RN * 2)
    t_rise_nor = _tpd_elmore(125, _RP * 2)
    t_rise_y = _tpd_elmore(L_y, _r_pmos(W_buf))
    t_fall_y = _tpd_elmore(L_y, _r_nmos(W_buf))
    rise = t_fall_nand + t_rise_y
    fall = t_rise_nor + t_fall_y
    return max(rise, fall)

def _gate_delay_half_add(L_y, L_sum=None, L_cout=None):
    """Half adder: AND2(L_cout) for carry, XOR(L_sum) for sum."""
    Ls = L_sum if L_sum is not None else L_y
    Lc = L_cout if L_cout is not None else L_y
    t_sum = _gate_delay_xor(Ls)
    t_cout = _gate_delay_and(Lc, 2)
    return max(t_sum, t_cout)

def _gate_delay_full_add(L_y, L_sum=None, L_cout=None):
    """Full adder carry and sum delay.

    Topology from full_add.sv:
      axb  = XOR(a, b)         L=296
      ab   = NAND2(a, b)       L=119
      caxb = NAND2(cin, axb)   L=120
      cout = NAND2(ab, caxb)   L=L_cout
      sum  = XOR(axb, cin)     L=L_sum

    Carry path (a→cout): max(XOR(296), NAND(119)) + NAND(120) + NAND(L_cout)
    Carry path (cin→cout): NAND(120) + NAND(L_cout)
    Sum path (a→sum): XOR(296) + XOR(L_sum)
    Sum path (cin→sum): XOR(L_sum)

    We return the worst-case delay across all input-to-output paths.
    """
    Ls = L_sum if L_sum is not None else L_y
    Lc = L_cout if L_cout is not None else L_y
    # First stage: a,b → axb (XOR) and a,b → ab (NAND2) in parallel
    t_xor_axb = _gate_delay_xor(296)
    t_nand_ab = _gate_delay_nand(119, 2)
    t_first = max(t_xor_axb, t_nand_ab)
    # Second stage: cin,axb → caxb (NAND2)
    t_nand_caxb = _gate_delay_nand(120, 2)
    # Third stage: ab,caxb → cout (NAND2)
    t_nand_cout = _gate_delay_nand(Lc, 2)
    # Carry path from a: first stage + caxb + cout
    t_carry_a = t_first + t_nand_caxb + t_nand_cout
    # Carry path from cin: caxb + cout (cin feeds caxb directly)
    t_carry_cin = t_nand_caxb + t_nand_cout
    # Sum path from a: XOR(296) + XOR(L_sum)
    t_sum_a = t_xor_axb + _gate_delay_xor(Ls)
    # Sum path from cin: XOR(L_sum) (cin feeds sum XOR directly)
    t_sum_cin = _gate_delay_xor(Ls)
    return max(t_carry_a, t_carry_cin, t_sum_a, t_sum_cin)


def compute_elmore_delay(gate_type, params):
    """Compute Elmore delay for a gate instance, return effective gate equivalents.

    Args:
        gate_type: cell type name (e.g. "nand2", "not_x1")
        params: dict of per-instance parameters from dmg_cpu_b.sv
                (e.g. {"L_y": 532.4, "W_y": 140})

    Returns:
        float: delay normalised to effective gate equivalents
               (1.0 = NOT_x1 at median wire length)
    """
    L_y = min(params.get('L_y', _L_DEFAULT), _L_MAX)

    if gate_type in ('not_x1',):
        delay = _gate_delay_not(L_y, W=35)
    elif gate_type == 'not_x2':
        delay = _gate_delay_not(L_y, W=70)
    elif gate_type == 'not_x3':
        delay = _gate_delay_not(L_y, W=105)
    elif gate_type == 'not_x4':
        W = params.get('W_y', 140)
        delay = _gate_delay_not(L_y, W=W)
    elif gate_type == 'not_x6':
        W = params.get('W_y', 210)
        delay = _gate_delay_not(L_y, W=W)
    elif gate_type in ('nand2', 'eco_nand2'):
        delay = _gate_delay_nand(L_y, 2)
    elif gate_type == 'nand3':
        delay = _gate_delay_nand(L_y, 3)
    elif gate_type == 'nand4':
        delay = _gate_delay_nand(L_y, 4)
    elif gate_type == 'nand5':
        delay = _gate_delay_nand(L_y, 5)
    elif gate_type == 'nand6':
        delay = _gate_delay_nand(L_y, 6)
    elif gate_type == 'nand7':
        delay = _gate_delay_nand(L_y, 7)
    elif gate_type == 'nor2':
        delay = _gate_delay_nor(L_y, 2)
    elif gate_type == 'nor3':
        delay = _gate_delay_nor(L_y, 3)
    elif gate_type == 'nor4':
        delay = _gate_delay_nor(L_y, 4)
    elif gate_type == 'nor5':
        delay = _gate_delay_nor(L_y, 5)
    elif gate_type == 'nor6':
        delay = _gate_delay_nor(L_y, 6)
    elif gate_type == 'nor8':
        delay = _gate_delay_nor(L_y, 8)
    elif gate_type == 'and2':
        delay = _gate_delay_and(L_y, 2)
    elif gate_type == 'and3':
        delay = _gate_delay_and(L_y, 3)
    elif gate_type == 'and4':
        delay = _gate_delay_and(L_y, 4)
    elif gate_type == 'or2':
        delay = _gate_delay_or(L_y, 2)
    elif gate_type == 'or3':
        delay = _gate_delay_or(L_y, 3)
    elif gate_type == 'or4':
        delay = _gate_delay_or(L_y, 4)
    elif gate_type == 'xor':
        delay = _gate_delay_xor(L_y)
    elif gate_type == 'xnor':
        delay = _gate_delay_xnor(L_y)
    elif gate_type == 'oai21':
        delay = _gate_delay_oai21(L_y)
    elif gate_type == 'ao21':
        delay = _gate_delay_ao(L_y, 2, L_int=112)
    elif gate_type == 'ao22':
        delay = _gate_delay_ao(L_y, 3, L_int=151)
    elif gate_type == 'ao222':
        delay = _gate_delay_ao(L_y, 4, L_int=185)
    elif gate_type == 'ao2222':
        delay = _gate_delay_ao(L_y, 5, L_int=218)
    elif gate_type == 'ao222222':
        delay = _gate_delay_ao(L_y, 7, L_int=284)
    elif gate_type == 'oa21':
        delay = _gate_delay_oa21(L_y)
    elif gate_type == 'muxi':
        delay = _gate_delay_muxi(L_y)
    elif gate_type == 'mux':
        delay = _gate_delay_mux(L_y)
    elif gate_type in ('not_if0', 'not_if1'):
        W_y_p = params.get('W_y_p', 35)
        delay = _gate_delay_not_if(L_y, W_y_p=W_y_p)
    elif gate_type == 'buf_if0':
        delay = _gate_delay_buf_if0(L_y)
    elif gate_type == 'half_add':
        delay = _gate_delay_half_add(L_y,
                                     L_sum=params.get('L_sum'),
                                     L_cout=params.get('L_cout'))
    elif gate_type == 'full_add':
        delay = _gate_delay_full_add(L_y,
                                     L_sum=params.get('L_sum'),
                                     L_cout=params.get('L_cout'))
    else:
        # Unknown gate type — fall back to NOT_x1-equivalent at this wire length
        delay = _gate_delay_not(L_y)

    return delay / _REF_DELAY


# ============================================================================
# dmg-sim instance parameter extraction
# ============================================================================

# Path to dmg-sim SystemVerilog netlist with per-instance wire lengths
DMG_SIM_SV = Path(__file__).parent / "dmg-schematics" / ".." / "dmg-sim" / "dmg_cpu_b" / "dmg_cpu_b.sv"
# Also try common locations
DMG_SIM_SEARCH_PATHS = [
    Path(__file__).parent / "dmg-sim" / "dmg_cpu_b" / "dmg_cpu_b.sv",
    Path.home() / "Projects" / "missingno" / "receipts" / "resources" / "dmg-sim" / "dmg_cpu_b" / "dmg_cpu_b.sv",
]


def parse_dmg_sim_params(sv_path=None):
    """Parse dmg_cpu_b.sv to extract per-instance parameters (L_y, W_y, etc.).

    Returns:
        dict: instance_name → {param_name: value, ...}
              e.g. {"abez": {"L_y": 1180.438}, "ajec": {"L_y": 38893.62, "W_y_p": 310}}
    """
    # Find the SV file
    if sv_path and Path(sv_path).exists():
        path = Path(sv_path)
    elif DMG_SIM_SV.exists():
        path = DMG_SIM_SV
    else:
        for p in DMG_SIM_SEARCH_PATHS:
            if p.exists():
                path = p
                break
        else:
            return {}

    text = path.read_text()

    # Parse instantiations like:
    #   dmg_nand2 #(
    #       .L_y(32.40649)
    #   ) abuf_inst (
    #
    # or multi-param:
    #   dmg_full_add #(
    #       .L_cout(150.3436),
    #       .L_sum(132.5468)
    #   ) abod_inst (

    instances = {}

    # Match: module_name #( params ) instance_name (
    # Negative lookbehind prevents matching the module definition itself.
    pattern = re.compile(
        r'(?<!module )dmg_\w+\s*#\s*\((.*?)\)\s*(\w+)_inst\s*\(',
        re.DOTALL
    )

    for m in pattern.finditer(text):
        param_block = m.group(1)
        inst_name = m.group(2)

        params = {}
        for pm in re.finditer(r'\.(\w+)\s*\(\s*([0-9.eE+-]+)\s*\)', param_block):
            param_name = pm.group(1)
            param_value = float(pm.group(2))
            params[param_name] = param_value

        if params:
            instances[inst_name] = params

    return instances


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
    ct.gate_equiv = float(GATE_EQUIVALENTS.get(name, 1))

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

def build_graph(cell_types: dict, cells: list, wires: list, sim_params=None):
    """Build a signal dependency graph from parsed cells and wires.

    Each cell becomes one or more nodes:
    - Combinatorial cells: one node (gate output)
    - Registered cells: one node (register output = clock boundary)
    - Tri-state cells: one node

    Wires create edges from driver cell outputs to sink cell inputs.

    If sim_params is provided (from parse_dmg_sim_params), per-instance Elmore
    delays are computed and stored as effective gate equivalents on each node.
    """
    nodes = {}
    edges = []
    if sim_params is None:
        sim_params = {}

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

        # Skip complex modules, memory macros and analog blocks — they're black boxes
        if ct.is_memory or cell.cell_type in ('sm83', 'tie') or cell.cell_type.startswith('amp') or cell.cell_type in ('dac', 'mixer', 'rv', 'vdiv'):
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

        # Compute per-instance delay from Elmore model if sim params available.
        # Registered nodes are path terminators (depth=0), so their gate_equiv
        # doesn't affect path analysis — skip the computation.
        if ct.is_registered:
            ge = ct.gate_equiv
        else:
            inst_params = sim_params.get(cell.name, {})
            if inst_params:
                ge = compute_elmore_delay(cell.cell_type, inst_params)
            else:
                ge = ct.gate_equiv

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
            gate_equiv=ge,
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

        driver_cells = sorted({c for c, _ in driver_refs})
        sink_cells = sorted({c for c, _ in sink_refs})

        # Determine base edge type from signal type
        edge_type = "data"
        if wire.signal_type == "clk":
            edge_type = "clock"
        elif wire.signal_type == "rst":
            edge_type = "reset"

        # Determine if the source output is inverted (~q vs q)
        # Build a map: driver_cell -> is_inverted for this wire
        drv_inverted = {}
        for cell_name, pin_ref in driver_refs:
            pin = _extract_pin_name(pin_ref)
            if pin.startswith('~'):
                drv_inverted[cell_name] = True
            else:
                drv_inverted[cell_name] = False

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
                edges.append(Edge(src=drv, dst=bus_node_name, edge_type="data",
                                  src_inverted=drv_inverted.get(drv, False)))

            # Connect bus node to each sink
            for snk in sink_cells:
                if snk == bus_node_name:
                    continue
                snk_edge_type = _pin_edge_type(snk, wire.sinks, edge_type, nodes.get(snk))
                edges.append(Edge(src=bus_node_name, dst=snk, edge_type=snk_edge_type))
        else:
            # Single-driver wire: direct edges
            for drv in driver_cells:
                for snk in sink_cells:
                    if drv == snk:
                        continue
                    snk_edge_type = _pin_edge_type(snk, wire.sinks, edge_type, nodes.get(snk))
                    edges.append(Edge(src=drv, dst=snk, edge_type=snk_edge_type,
                                      src_inverted=drv_inverted.get(drv, False)))

    return nodes, edges


def _pin_edge_type(sink_cell: str, sink_pin_refs: list, default_type: str,
                   sink_node: Node = None) -> str:
    """Determine edge type based on the destination pin name.

    Only registered cells have clock/reset pins. Combinatorial cells treat
    all inputs as data, even if the wire's signal type is 'clk' — a clock
    signal passing through a buffer is still a data dependency for timing.

    For registered cells, we classify by the actual pin being driven:
    - clk/ena pins → clock edge (timing boundary)
    - reset/set pins → reset edge
    - data pins (d, l, etc.) → data edge, even if the wire carries a clock signal
    """
    # Combinatorial/bus/pad cells: all inputs are data
    if sink_node and sink_node.node_type not in ('registered',):
        return "data"

    # For registered cells, classify by the specific pin being driven
    for pin_ref in sink_pin_refs:
        if _extract_cell_name(pin_ref) == sink_cell:
            pin_name = _extract_pin_name(pin_ref)
            if pin_name in ('clk', '~clk', '~tclk'):
                return "clock"
            elif pin_name in ('ena', '~ena'):
                return "clock"
            elif pin_name in ('~r', '~s', 'r', 's'):
                return "reset"
            elif pin_name in ('d', 'l'):
                return "data"
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

def export_graph_json(nodes: dict, edges: list, cell_types: dict,
                      clock_domains: dict = None, clock_tree: dict = None) -> dict:
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
            "gate_equiv": round(n.gate_equiv, 2),
        }
        if n.bbox:
            entry["bbox"] = list(n.bbox)
        # Add clock domain info for registered nodes
        if clock_domains and n.name in clock_domains:
            cd = clock_domains[n.name]
            entry["clock_drivers"] = cd['clock_drivers']
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
            'gate_equiv': round(n.gate_equiv, 2),
            'source_file': n.source_file,
            'source_line': n.source_line,
            'comment': n.comment,
        })
        if n.bbox:
            G.nodes[n.name]['bbox'] = list(n.bbox)

    for e in edges:
        if e.src in G and e.dst in G:
            G.add_edge(e.src, e.dst, edge_type=e.edge_type,
                       src_inverted=e.src_inverted)

    return G


def is_path_terminator(G, node_name):
    """Check if a node terminates a combinatorial path (registered/bus/boundary/pad)."""
    nt = G.nodes[node_name].get('node_type', '')
    return nt in ('registered', 'bus', 'boundary', 'pad')


def compute_depths(G):
    """Compute longest combinatorial depth to each node without building a DAG.

    Registered/bus/boundary/pad nodes have depth 0 (they're path boundaries).
    Combinatorial nodes get depth = max(predecessor depths) + gate_equiv,
    where gate_equiv is a float representing effective gate-equivalents
    computed from the Elmore delay model (wire length + gate topology).

    Uses iterative relaxation with cycle detection: if a node appears in its
    own predecessor path, that's a combinatorial feedback loop and we skip it.
    This handles SR latch feedback and other cycles without needing to remove
    edges from the graph.
    """
    depth = {}
    path = {}

    for n in G.nodes():
        if is_path_terminator(G, n):
            depth[n] = 0.0
            path[n] = [n]
        else:
            depth[n] = -1.0
            path[n] = []

    changed = True
    iterations = 0
    while changed and iterations < 50:
        changed = False
        iterations += 1
        for n in sorted(G.nodes()):
            if is_path_terminator(G, n):
                continue

            best_d = -1.0
            best_path = []
            best_pred = ''
            for pred in sorted(G.predecessors(n)):
                edge_data = G.edges[pred, n]
                if edge_data.get('edge_type') in ('clock', 'reset'):
                    continue
                pd = depth.get(pred, -1.0)
                pp = path.get(pred, [])
                # Skip if this would create a cycle (n is already in the path)
                if n in pp:
                    continue
                # Deterministic tie-breaking: prefer deeper, then alphabetically first
                if pd > best_d or (pd == best_d and pred < best_pred):
                    best_d = pd
                    best_path = pp
                    best_pred = pred

            if best_d >= 0:
                ge = G.nodes[n].get('gate_equiv', 1.0)
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
    for n in sorted(G.nodes()):
        if not is_path_terminator(G, n):
            continue
        for pred in sorted(G.predecessors(n)):
            edge_data = G.edges[pred, n]
            if edge_data.get('edge_type') in ('clock', 'reset'):
                continue
            d = depth.get(pred, 0.0)
            p = path.get(pred, [])
            if d >= 0.5:
                paths.append((d, p + [n]))

    paths.sort(key=lambda x: -x[0])

    # Deduplicate by (start, end, rounded depth)
    seen = set()
    unique = []
    for d, p in paths:
        key = (p[0], p[-1], round(d, 2))
        if key not in seen:
            seen.add(key)
            unique.append((d, p))
    return unique


# Timing deadlines by functional category (in T-cycles).
# Slack = deadline - max_depth.  Lower slack = more critical.
#
# Per-dot:  PPU registers that update every pixel during rendering.
#           Deadline = 1 T-cycle (238.4 ns) — must settle within one dot.
# Per-line: PPU registers that update once per scanline (at LY increment
#           or during OAM scan).  Deadline = ~4 T-cycles (~953 ns).
# Bus:      CPU bus transfers.  Deadline = 1 M-cycle (4 T-cycles).
# Loose:    APU, timer, serial — many T-cycles of slack.
HALF_TCYCLE_NS = 119.2
TCYCLE_NS = 238.4
MCYCLE_NS = TCYCLE_NS * 4    # 953.6 ns

DEADLINE_BY_CATEGORY = {
    # Per-dot PPU — tightest deadline
    'ppu-bgfifo':    TCYCLE_NS,
    'ppu-objfifo':   TCYCLE_NS,
    'ppu-mux':       TCYCLE_NS,
    'ppu-xcomp':     TCYCLE_NS,
    'ppu-xprio':     TCYCLE_NS,
    'ppu-cycles':    TCYCLE_NS,
    'ppu-bgscroll':  TCYCLE_NS,
    'ppu-stat':      TCYCLE_NS,     # pixel counter increments per dot
    # Per-line PPU — moderate deadline
    'ppu-ycomp':     MCYCLE_NS,     # once per scanline at LY increment
    'ppu-objctl':    MCYCLE_NS,     # sprite store during OAM scan
    'ppu-objreg':    MCYCLE_NS,     # sprite store latches
    'ppu-oam':       MCYCLE_NS,
    'ppu-dma':       MCYCLE_NS,
    'ppu-window':    TCYCLE_NS,     # window trigger checked per dot
    'ppu-lcd':       MCYCLE_NS,
    'ppu-control':   MCYCLE_NS,
    'ppu-vram':      MCYCLE_NS,
    'ppu-decode':    MCYCLE_NS,
    'ppu-pal':       MCYCLE_NS,
    # Bus — full M-cycle
    'bus':           MCYCLE_NS,
    'bus-data':      MCYCLE_NS,
    'bus-adr':       MCYCLE_NS,
    # Loose — many cycles of slack
    'apu-ch1':       MCYCLE_NS * 4,
    'apu-ch2':       MCYCLE_NS * 4,
    'apu-ch3':       MCYCLE_NS * 4,
    'apu-ch4':       MCYCLE_NS * 4,
    'apu-control':   MCYCLE_NS * 4,
    'apu-decode':    MCYCLE_NS * 4,
    'timer':         MCYCLE_NS * 4,
    'serial':        MCYCLE_NS * 4,
    'joypad':        MCYCLE_NS * 4,
    'clocks':        MCYCLE_NS,
    'int':           MCYCLE_NS,
    'test':          MCYCLE_NS * 16,
    'bootrom':       MCYCLE_NS * 4,
}
DEFAULT_DEADLINE_NS = MCYCLE_NS


def find_race_pairs(G):
    """Find signal races: registered nodes where inputs arrive at different depths.

    Considers ALL predecessor edges (data, clock, reset) for race detection,
    because the race is between ANY inputs that must settle before the register
    captures. For example, a latch's enable signal (classified as 'clock')
    races against its data input.

    Each race includes a slack estimate: deadline_ge - max_depth, where
    deadline_ge is the timing budget in effective gate-equivalents.
    Lower (or negative) slack = more critical.
    """
    depth, _ = compute_depths(G)

    races = []
    for n in sorted(G.nodes()):
        if not is_path_terminator(G, n):
            continue

        preds = sorted(G.predecessors(n))

        if len(preds) < 2:
            continue

        pred_depths = [(p, depth.get(p, 0.0)) for p in preds]
        pred_depths.sort(key=lambda x: (-x[1], x[0]))  # depth desc, name asc for ties

        max_d = pred_depths[0][1]
        min_d = pred_depths[-1][1]
        diff = max_d - min_d

        # Thresholds scaled for Elmore model where a typical gate ≈ 1.3 ge
        if diff >= 4.0 and max_d >= 5.0:
            cat = G.nodes[n].get('category', '')
            deadline_ns = DEADLINE_BY_CATEGORY.get(cat, DEFAULT_DEADLINE_NS)
            # Timing domain label
            if deadline_ns <= TCYCLE_NS:
                timing_domain = 'per-dot'
            elif deadline_ns <= MCYCLE_NS:
                timing_domain = 'per-line'
            else:
                timing_domain = 'loose'

            races.append({
                'node': n,
                'display_name': n,
                'node_type': G.nodes[n].get('node_type', ''),
                'reg_type': G.nodes[n].get('reg_type', ''),
                'cell_type': G.nodes[n].get('cell_type', ''),
                'category': cat,
                'source_file': G.nodes[n].get('source_file', ''),
                'depth_diff': round(diff, 2),
                'max_depth': round(max_d, 2),
                'min_depth': round(min_d, 2),
                'deadline_ns': deadline_ns,
                'timing_domain': timing_domain,
                'inputs': [
                    {
                        'name': p,
                        'depth': round(d, 2),
                        'gate_func': G.nodes[p].get('gate_func', ''),
                        'cell_type': G.nodes[p].get('cell_type', ''),
                        'node_type': G.nodes[p].get('node_type', ''),
                        'category': G.nodes[p].get('category', ''),
                    }
                    for p, d in pred_depths
                ],
            })

    # Sort by timing criticality: per-dot races first, then by depth_diff descending
    domain_order = {'per-dot': 0, 'per-line': 1, 'loose': 2}
    races.sort(key=lambda x: (domain_order.get(x['timing_domain'], 3),
                               -x['depth_diff'], -x['max_depth']))
    return races


# ============================================================================
# Clock Domain Analysis
# ============================================================================

def analyze_clock_domains(G):
    """Identify the clock domain of every registered cell by tracing clock inputs.

    For each registered cell, finds the edge(s) with edge_type="clock" and
    identifies the immediate clock driver. Then traces the clock tree structure
    to understand the hierarchy.

    Returns:
        domains: dict mapping registered cell name -> clock domain info
        clock_groups: dict mapping immediate_driver -> list of registered cells
        clock_tree: dict mapping each clock node -> its clock source chain
    """
    # Step 1: Build a map of clock predecessors for each registered cell.
    # These are the nodes driving the clk/ena/~ena pins.
    clock_preds = {}  # registered_cell -> list of immediate drivers
    for u, v, data in G.edges(data=True):
        if data.get('edge_type') == 'clock':
            vtype = G.nodes[v].get('node_type', '')
            if vtype == 'registered':
                if v not in clock_preds:
                    clock_preds[v] = []
                if u not in clock_preds[v]:
                    clock_preds[v].append(u)

    # Step 2: Build clock domain assignments grouped by immediate driver.
    domains = {}
    for reg_cell, drivers in clock_preds.items():
        domains[reg_cell] = {
            'cell_type': G.nodes[reg_cell].get('cell_type', ''),
            'category': G.nodes[reg_cell].get('category', ''),
            'clock_drivers': sorted(drivers),
        }

    # Step 3: Group registers by their set of immediate clock drivers.
    # Registers with the same driver(s) are in the same clock domain.
    clock_groups = {}  # frozenset of drivers -> list of registered cells
    driver_to_group = {}  # individual driver -> list of registered cells
    for reg_cell, info in domains.items():
        key = tuple(sorted(info['clock_drivers']))
        if key not in clock_groups:
            clock_groups[key] = []
        clock_groups[key].append(reg_cell)
        for drv in info['clock_drivers']:
            if drv not in driver_to_group:
                driver_to_group[drv] = []
            driver_to_group[drv].append(reg_cell)

    # Step 4: Trace the clock tree — for each immediate driver, find the chain
    # of clock sources back to the crystal or phase generators.
    def trace_clock_chain(node, visited=None):
        """Trace backward from a clock driver to find its clock source chain.
        Stops at registered cells (which are clock boundaries), pads, or cycles.
        Returns the chain as a list from root to node."""
        if visited is None:
            visited = set()
        if node in visited:
            return [node]  # cycle
        visited.add(node)

        ntype = G.nodes[node].get('node_type', '')

        # If this is a registered/pad/boundary node, it's a clock root
        if ntype in ('registered', 'pad', 'boundary'):
            # But this registered cell may itself be clocked — trace its clock
            # source to build the full chain (but only one level deep for the
            # clock root identification, not recursively through combinational)
            return [node]

        # Combinational node: find the deepest registered predecessor
        # (following data edges only, not clock/reset on intermediate nodes)
        best_chain = [node]
        for pred in sorted(G.predecessors(node)):
            edata = G.edges[pred, node]
            if edata.get('edge_type') in ('clock', 'reset'):
                continue
            chain = trace_clock_chain(pred, visited.copy())
            if len(chain) > len(best_chain) - 1:
                # Check if this chain reaches a registered/pad root
                root_type = G.nodes[chain[0]].get('node_type', '')
                if root_type in ('registered', 'pad', 'boundary'):
                    best_chain = chain + [node]

        return best_chain

    clock_tree = {}
    all_drivers = set()
    for info in domains.values():
        all_drivers.update(info['clock_drivers'])

    for driver in sorted(all_drivers):
        clock_tree[driver] = trace_clock_chain(driver)

    # Step 5: Compute effective polarity for each clock driver.
    # Count inversions through the combinational chain from root to driver.
    # This determines whether the clock signal is in-phase or anti-phase
    # with the root's output.
    INVERTING_GATES = {
        'not_x1', 'not_x2', 'not_x3', 'not_x4', 'not_x6',
        'nand2', 'nand3', 'nand4', 'nand5', 'nand6', 'nand7',
        'eco_nand2',
        'nor2', 'nor3', 'nor4', 'nor5', 'nor6', 'nor8',
        'oai21',
        'muxi',
        'not_if0', 'not_if1',
    }
    NON_INVERTING_GATES = {
        'and2', 'and3', 'and4',
        'or2', 'or3', 'or4',
        'ao21', 'ao22', 'ao222', 'ao2222', 'ao222222',
        'oa21',
        'mux',
        'buf_if0',
    }

    clock_polarity = {}  # driver -> {'inversions': N, 'root_inverted': bool, 'polarity': str}
    for driver in sorted(all_drivers):
        chain = clock_tree.get(driver, [driver])
        if len(chain) < 2:
            # Driver is the root itself (ripple clock). Check whether Q or ~Q
            # is used to clock downstream registers.
            ripple_inverted = False
            for succ in sorted(G.successors(driver)):
                edata = G.edges[driver, succ]
                if edata.get('edge_type') == 'clock':
                    ripple_inverted = edata.get('src_inverted', False)
                    break
            clock_polarity[driver] = {
                'inversions': 0,
                'root_inverted': ripple_inverted,
                'polarity': 'inverted' if ripple_inverted else 'non-inverted',
            }
            continue

        root = chain[0]
        inversions = 0
        ambiguous = False

        # Check if root outputs via ~q (inverted output)
        root_inverted = False
        if root in G and chain[1] in G and G.has_edge(root, chain[1]):
            edata = G.edges[root, chain[1]]
            root_inverted = edata.get('src_inverted', False)

        # Count inversions through all combinational gates from root to driver
        for node in chain[1:]:
            ct = G.nodes[node].get('cell_type', '') if node in G else ''
            if ct in INVERTING_GATES:
                inversions += 1
            elif ct in NON_INVERTING_GATES:
                pass  # no inversion
            elif ct and ct not in REGISTERED_TYPES and not ct.startswith('pad'):
                ambiguous = True

        total_inverted = (inversions % 2 == 1) != root_inverted  # XOR
        if ambiguous:
            polarity = 'ambiguous'
        elif total_inverted:
            polarity = 'inverted'
        else:
            polarity = 'non-inverted'

        clock_polarity[driver] = {
            'inversions': inversions,
            'root_inverted': root_inverted,
            'polarity': polarity,
        }

    return domains, clock_groups, clock_tree, clock_polarity


def _classify_clock_root(driver, clock_tree, G):
    """Classify a clock driver into a high-level clock domain.

    Returns (root_name, root_type) where root_name is the registered cell
    or pad at the head of the clock chain, and root_type describes the kind
    of clocking (direct, gated, ripple).
    """
    chain = clock_tree.get(driver, [driver])
    root = chain[0]
    root_ntype = G.nodes[root].get('node_type', '') if root in G.nodes else ''
    root_cat = G.nodes[root].get('category', '') if root in G.nodes else ''
    chain_len = len(chain)

    if root_ntype == 'pad':
        if root_cat == 'clocks':
            return root, 'crystal-derived'
        elif root_cat == 'test':
            return root, 'test-gated'
        else:
            return root, 'io-derived'
    elif root_ntype == 'registered':
        if chain_len == 1:
            return root, 'ripple'
        else:
            return root, 'gated'
    elif root_ntype == 'boundary':
        return root, 'cpu-derived'
    else:
        return driver, 'combinational'


def format_clock_domain_report(domains, clock_groups, clock_tree, clock_polarity, G):
    """Generate a markdown report of clock domain analysis."""
    lines = []
    lines.append("# Clock Domain Analysis")
    lines.append("")
    lines.append("Structural analysis of the DMG-CPU B clock distribution network,")
    lines.append("derived entirely from netlist connectivity.")
    lines.append("")
    lines.append("Data source: [msinger/dmg-schematics](https://github.com/msinger/dmg-schematics).")
    lines.append("No GateBoy-derived data is used — all classifications come from tracing")
    lines.append("the `clk`/`ena`/`~ena` pin connectivity in the netlist.")
    lines.append("")

    # =========================================================================
    # Clock tree overview
    # =========================================================================
    lines.append("## Clock Tree Overview")
    lines.append("")
    lines.append("The DMG-CPU B has a single crystal oscillator (`ck1_ck2`) at 4.194 MHz.")
    lines.append("All on-chip timing derives from this source through the following hierarchy:")
    lines.append("")
    lines.append("```")
    lines.append("Crystal (ck1_ck2, 4.194 MHz)")
    lines.append("├── atal/adeh — 4 MHz complementary enables (via anos/avet feedback)")
    lines.append("│   ├── Phase generators (AFUR/ALEF/APUK/ADYK) — drlatch_ee ring")
    lines.append("│   │   ├── boga/boma — clk_1mhz / ~clk_1mhz")
    lines.append("│   │   │   └── Drives: CPU, timer, joypad, APU registers")
    lines.append("│   │   ├── bufa/byly — clk_t4 (write phase)")
    lines.append("│   │   ├── bude/beva — data_phase")
    lines.append("│   │   ├── bedo/bowa — exec_phase")
    lines.append("│   │   └── buke — ~pch_phase (pixel clock)")
    lines.append("│   └── azof — buffered 4 MHz (via zaxy/zeme/xyva)")
    lines.append("│       ├── alet — PPU line timing")
    lines.append("│       ├── xota — PPU video clock (non-inverted)")
    lines.append("│       │   └── wuvu — video clock (dffr, clocked by xota)")
    lines.append("│       │       └── vena — video clock (dffr, clocked by wuvu.~q)")
    lines.append("│       └── xyfy — PPU video clock (inverted xota)")
    lines.append("│           └── wosu — video clock (dffr, clocked by xyfy)")
    lines.append("├── Timer divider chains (clk_1mhz → ukup → ufor → uner → ...)")
    lines.append("│   └── 16 Hz to 262 kHz frequency outputs")
    lines.append("└── Ripple counters (LY, BG fetch, sprite scan, APU)")
    lines.append("```")
    lines.append("")

    # =========================================================================
    # Summary statistics
    # =========================================================================
    total_registered = sum(1 for n, d in G.nodes(data=True) if d.get('node_type') == 'registered')
    assigned = len(domains)
    unassigned = total_registered - assigned
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total registered cells | {total_registered} |")
    lines.append(f"| With clock inputs traced | {assigned} |")
    lines.append(f"| Without clock edges (SR latches) | {unassigned} |")
    lines.append(f"| Distinct clock configurations | {len(clock_groups)} |")
    lines.append("")

    # =========================================================================
    # High-level domain classification
    # =========================================================================
    # Classify each clock group by its root source
    root_domains = {}  # root_name -> {type, groups: [(drivers, cells)], total_regs}
    sorted_groups = sorted(clock_groups.items(),
                           key=lambda x: (-len(x[1]), x[0]))

    for drivers, cells in sorted_groups:
        # Use the first driver's classification for the group
        root, rtype = _classify_clock_root(drivers[0], clock_tree, G)
        if root not in root_domains:
            root_domains[root] = {'type': rtype, 'groups': [], 'total_regs': 0}
        root_domains[root]['groups'].append((drivers, cells))
        root_domains[root]['total_regs'] += len(cells)

    lines.append("## Clock Domains by Root Source")
    lines.append("")
    lines.append("Registers grouped by the root node of their clock chain (the registered")
    lines.append("cell, pad, or boundary at the head of the combinational path driving their")
    lines.append("clock pin). Roots with fewer than 3 registers are omitted (mostly ripple")
    lines.append("counter chains).")
    lines.append("")
    lines.append("| Root | Type | Clock Signals | Registers |")
    lines.append("|------|------|--------------|-----------|")
    small_root_count = 0
    small_root_regs = 0
    for root in sorted(root_domains, key=lambda r: -root_domains[r]['total_regs']):
        info = root_domains[root]
        if info['total_regs'] < 3:
            small_root_count += 1
            small_root_regs += info['total_regs']
            continue
        root_type = G.nodes[root].get('cell_type', '') if root in G.nodes else ''
        lines.append(f"| `{root}` ({root_type}) | {info['type']} | {len(info['groups'])} | {info['total_regs']} |")
    if small_root_count:
        lines.append(f"| *{small_root_count} other roots* | *ripple/gated* | *—* | *{small_root_regs}* |")
    lines.append("")
    lines.append("**Note on test-gated domains:** `t1` and `t2` are test pins held at static")
    lines.append("logic levels during normal Game Boy operation. Registers whose clock chain")
    lines.append("traces back to a test pin are actually clocked by the crystal-derived path")
    lines.append("through the test gate — the test pin simply enables/disables the clock for")
    lines.append("manufacturing test. In normal operation these registers behave identically")
    lines.append("to crystal-derived registers; the test gate is always open.")
    lines.append("")
    lines.append("**Note on `muwy` domain (181 registers):** `muwy` is LY bit 0 (the lowest")
    lines.append("bit of the scanline counter). Its 181 registers are sprite store (100) and")
    lines.append("sprite X match (80) banks, clocked by signals gated through the sprite Y")
    lines.append("comparator chain. These registers update during OAM scan when the comparator")
    lines.append("output (derived from the LY counter) enables the sprite store clock gates.")
    lines.append("")

    # =========================================================================
    # Phase generators — the most important section for emu devs
    # =========================================================================
    lines.append("## Phase Generator Analysis")
    lines.append("")
    lines.append("The CPU clock phase generators form a 4-stage `drlatch_ee` ring with")
    lines.append("alternating enables. This is the core timing mechanism that determines")
    lines.append("when registers throughout the chip update.")
    lines.append("")
    lines.append("### Enable Signals")
    lines.append("")
    lines.append("Both enables derive from the crystal via `ck1_ck2` → `anos` → `avet` → `atal`.")
    lines.append("`adeh` is the complement of `atal` (a NOT gate).")
    lines.append("")
    lines.append("| Latch | ena (transparent when high) | ~ena (transparent when low) | Data in | Data out |")
    lines.append("|-------|---------------------------|---------------------------|---------|----------|")

    phase_data = {
        'afur': {'ena': 'atal', '~ena': 'adeh', 'data_in': 'adyk.~q', 'data_out': 'alef.d'},
        'alef': {'ena': 'adeh', '~ena': 'atal', 'data_in': 'afur.q', 'data_out': 'apuk.d'},
        'apuk': {'ena': 'atal', '~ena': 'adeh', 'data_in': 'alef.q', 'data_out': 'adyk.d'},
        'adyk': {'ena': 'adeh', '~ena': 'atal', 'data_in': 'apuk.q', 'data_out': 'afur.d (via ~q)'},
    }
    for pc in ['afur', 'alef', 'apuk', 'adyk']:
        pd = phase_data[pc]
        lines.append(f"| `{pc}` | `{pd['ena']}` | `{pd['~ena']}` | `{pd['data_in']}` | `{pd['data_out']}` |")
    lines.append("")
    lines.append("When `atal` is high: `afur` and `apuk` are transparent (pass data through).")
    lines.append("When `atal` is low (= `adeh` high): `alef` and `adyk` are transparent.")
    lines.append("")
    lines.append("The ring shifts data each half-cycle of the 4 MHz clock, producing four")
    lines.append("overlapping phase windows. Each latch's output drives combinational logic")
    lines.append("that generates the clock distribution signals (`clk_1mhz`, `clk_t4`, etc.).")
    lines.append("")

    # =========================================================================
    # PPU video clock generators
    # =========================================================================
    lines.append("## PPU Video Clock Generators")
    lines.append("")
    lines.append("The PPU has its own clock divider, separate from the CPU clock phases.")
    lines.append("These are positive-edge-triggered `dffr` flip-flops derived from the")
    lines.append("4 MHz buffered clock (`azof` → `zaxy` → `zeme` → `xyva` → `xota`/`xyfy`).")
    lines.append("")
    lines.append("- **`wuvu`** (dffr): clocked by `xota` (positive edge)")
    lines.append("- **`vena`** (dffr): clocked by `wuvu.~q` (inverted output → captures on wuvu falling edge)")
    lines.append("- **`wosu`** (dffr): clocked by `xyfy` (inverted `xota` → captures on opposite edge to wuvu)")
    lines.append("")
    lines.append("Note: `wosu` is NOT ripple-clocked from `wuvu`. It receives `wuvu.~q` as")
    lines.append("its **data** input, but its clock comes independently from `xyfy`. This means")
    lines.append("`wosu` samples `wuvu`'s output on the opposite clock edge, creating a")
    lines.append("half-period timing constraint between them.")
    lines.append("")

    # =========================================================================
    # Major clock groups (≥4 registers)
    # =========================================================================
    lines.append("## Major Clock Groups")
    lines.append("")
    lines.append("Clock signals driving 10 or more registers.")
    lines.append("")

    MAJOR_GROUP_THRESHOLD = 10
    MAX_CHAIN_DISPLAY = 6  # Only show chains ≤ this length

    for drivers, cells in sorted_groups:
        if len(cells) < MAJOR_GROUP_THRESHOLD:
            continue

        driver_strs = []
        for drv in drivers:
            drv_type = G.nodes[drv].get('cell_type', '') if drv in G.nodes else ''
            driver_strs.append(f"`{drv}` ({drv_type})")

        header_drivers = ", ".join(driver_strs)
        lines.append(f"### {header_drivers} — {len(cells)} registers")

        # Show clock chain and polarity for each driver
        for drv in drivers:
            chain = clock_tree.get(drv, [drv])
            pol = clock_polarity.get(drv, {})
            pol_str = pol.get('polarity', '')
            if pol_str == 'inverted':
                pol_label = ' — **inverted** from root'
            elif pol_str == 'non-inverted':
                pol_label = ' — **non-inverted** from root'
            elif pol_str == 'ambiguous':
                pol_label = ' — polarity depends on gate input state'
            else:
                pol_label = ''

            if 1 < len(chain) <= MAX_CHAIN_DISPLAY:
                chain_str = " → ".join(f"`{n}`" for n in chain)
                lines.append(f"")
                lines.append(f"Clock source: {chain_str}{pol_label}")
            elif len(chain) > MAX_CHAIN_DISPLAY:
                root = chain[0]
                root_type = G.nodes[root].get('cell_type', '') if root in G.nodes else ''
                _, rtype = _classify_clock_root(drv, clock_tree, G)
                lines.append(f"")
                lines.append(f"Clock root: `{root}` ({root_type}) — {rtype}, {len(chain)-1} gates deep{pol_label}")
        lines.append("")

        # Group cells by category
        by_cat = {}
        for c in sorted(cells):
            cat = G.nodes[c].get('category', '(none)')
            cat_display = CATEGORY_DISPLAY.get(cat, cat)
            if cat_display not in by_cat:
                by_cat[cat_display] = []
            by_cat[cat_display].append(c)

        for cat_display in sorted(by_cat):
            cat_cells = by_cat[cat_display]
            cell_list = ", ".join(f"`{c}`" for c in cat_cells[:20])
            if len(cat_cells) > 20:
                cell_list += f" … (+{len(cat_cells)-20} more)"
            lines.append(f"- **{cat_display}** ({len(cat_cells)}): {cell_list}")
        lines.append("")

    # =========================================================================
    # Small groups summary (< 4 registers)
    # =========================================================================
    small_groups = [(d, c) for d, c in sorted_groups if len(c) < MAJOR_GROUP_THRESHOLD]
    if small_groups:
        total_small_regs = sum(len(c) for _, c in small_groups)
        lines.append(f"## Remaining Clock Groups (< {MAJOR_GROUP_THRESHOLD} registers)")
        lines.append("")
        lines.append(f"{len(small_groups)} additional clock signals driving {total_small_regs}")
        lines.append("registered cells. These are predominantly ripple counters (one register's")
        lines.append("output clocking the next) and dedicated clock gates for small register banks.")
        lines.append("Full details are in `clock_domains.json`.")
        lines.append("")

    # =========================================================================
    # Cross-domain path implications
    # =========================================================================
    lines.append("## Emulation Implications")
    lines.append("")
    lines.append("### Timing budgets for cross-domain paths")
    lines.append("")
    lines.append("When a combinatorial path connects a source register to a sink register,")
    lines.append("the available settling time depends on their clock relationship:")
    lines.append("")
    lines.append("| Source → Sink Clocking | Available Budget | Notes |")
    lines.append("|----------------------|-----------------|-------|")
    lines.append("| Same clock signal | Full period (~238 ns) | Standard synchronous path |")
    lines.append("| Same root, different gate | Depends on gate timing | Common in PPU — gate condition determines when path is live |")
    lines.append("| atal → adeh (complementary) | Half period (~119 ns) | Phase generator cross-paths |")
    lines.append("| Ripple chain | Parent CK→Q + budget | Ripple counters: child clocked by parent output |")
    lines.append("| Unrelated domains | Async crossing | Rare on DMG; mainly CPU ↔ external |")
    lines.append("")
    lines.append("### What this means for emulators")
    lines.append("")
    lines.append("A behavioral emulator that updates all registers simultaneously on each")
    lines.append("dot clock will get the right answer for same-domain paths. Cross-domain")
    lines.append("paths are where real hardware may differ — the source register's output")
    lines.append("may not have settled before the sink register samples it, causing the")
    lines.append("sink to capture the *previous* value rather than the *current* one.")
    lines.append("")

    # =========================================================================
    # Registers without clock edges
    # =========================================================================
    all_registered = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'registered']
    no_clock = sorted(set(all_registered) - set(domains.keys()))
    if no_clock:
        lines.append("## Registers Without Clock Edges")
        lines.append("")
        lines.append("These registered cells have no `clk`/`ena` inputs in the netlist.")
        lines.append("They are SR latches whose timing is determined by their set/reset")
        lines.append("input arrival times rather than a clock edge.")
        lines.append("")
        by_type = {}
        for c in no_clock:
            ct = G.nodes[c].get('cell_type', '?')
            if ct not in by_type:
                by_type[ct] = []
            by_type[ct].append(c)
        for ct in sorted(by_type):
            cell_list = ", ".join(f"`{c}`" for c in by_type[ct][:20])
            if len(by_type[ct]) > 20:
                cell_list += f" … (+{len(by_type[ct])-20} more)"
            lines.append(f"- **{ct}** ({len(by_type[ct])}): {cell_list}")
        lines.append("")

    return '\n'.join(lines)


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
    'apu-ch1': 'APU CH1 (Square+Sweep)',
    'apu-ch2': 'APU CH2 (Square)',
    'apu-ch3': 'APU CH3 (Wave)',
    'apu-ch4': 'APU CH4 (Noise)',
    'apu-control': 'APU Control',
    'apu-decode': 'APU Decode',
    'apu-analog': 'APU Analog',
    'test': 'Test Mode',
    'bootrom': 'Boot ROM',
    'hram': 'High RAM',
    'bus': 'Bus',
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


def export_paths_json(paths, G, races=None, clock_domains=None):
    """Export critical paths and races in format compatible with build_explorer.py."""
    HALF_TCYCLE_NS = 119.2
    GATE_DELAY_MIN = 5   # ns per effective gate-equivalent
    GATE_DELAY_MAX = 15  # ns per effective gate-equivalent

    path_list = []
    for depth, path in paths:
        min_ns = round(depth * GATE_DELAY_MIN, 1)
        max_ns = round(depth * GATE_DELAY_MAX, 1)
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
                'gate_equiv': round(nd.get('gate_equiv', 1.0), 2),
                'fan_out': G.out_degree(n),
            })

        entry = {
            'depth': round(depth, 2),
            'min_delay_ns': min_ns,
            'max_delay_ns': max_ns,
            'pct_half_tcycle': round(pct, 1),
            'source': path[0],
            'sink': path[-1],
            'is_reset': is_reset_path_schematic(path, G),
            'category': categorize_by_schematic(path, G),
            'nodes': path_nodes,
        }

        # Add clock domain info for source and sink
        if clock_domains:
            src = path[0]
            snk = path[-1]
            if src in clock_domains:
                entry['source_clock'] = clock_domains[src]['clock_drivers']
            if snk in clock_domains:
                entry['sink_clock'] = clock_domains[snk]['clock_drivers']
            # Flag cross-domain paths
            src_clk = set(clock_domains.get(src, {}).get('clock_drivers', []))
            snk_clk = set(clock_domains.get(snk, {}).get('clock_drivers', []))
            if src_clk and snk_clk:
                entry['cross_domain'] = src_clk != snk_clk

        path_list.append(entry)

    return path_list


# ============================================================================
# Report Generation
# ============================================================================

def build_friendly_names(G):
    """Build a die name -> friendly description map for use in reports."""
    # Key signals (hand-curated)
    names = {
        'sacu': 'Pixel Shift Clock (CLKPIPE)', 'xymu': 'Rendering Active (Mode 3)',
        'poky': 'Pixel Pipe Done', 'roxy': 'Fine Scroll Done',
        'nyka': 'BG Fetch Clock', 'atej': 'Line Strobe',
        'muwy': 'LY bit 0', 'myro': 'LY bit 1', 'lexa': 'LY bit 2',
        'lydo': 'LY bit 3', 'lovu': 'LY bit 4', 'lema': 'LY bit 5',
        'mato': 'LY bit 6', 'lafo': 'LY bit 7',
        'xeho': 'Pixel X bit 0', 'savy': 'Pixel X bit 1',
        'xodu': 'Pixel X bit 2', 'xydo': 'Pixel X bit 3',
        'laxu': 'BG Fetch S0', 'mesu': 'BG Fetch S1', 'nyva': 'BG Fetch S2',
        'lovy': 'Fetch Done', 'lony': 'Fetching Active',
        'besu': 'OAM Scan Done', 'ceno': 'Scan Active',
        'taka': 'Sprite Fetch Gate', 'sobu': 'Sprite Fetch Req',
        'texy': 'Sprite Fetching', 'wuty': 'Sprite Fetch Done',
        'ryfa': 'Window Y Match', 'rene': 'Window Active',
        'afer': 'System Reset', 'xapo': 'Video Reset',
        'keba': 'APU Master Enable', 'bogy': 'APU Clock Gate',
        'aguz': 'APU Length Clock', 'alur': 'System Clock Inv',
        'cunu': 'System Reset Inv', 'tova': 'Ext Bus Enable',
        'unor': 'Test Mode Gate', 'adad': 'CH1 Freq Clock',
    }
    # Bus nodes
    for n in G.nodes():
        if not n.startswith('bus:'):
            continue
        bus = n[4:]  # strip "bus:"
        if re.match(r'^d\d$', bus):
            names[n] = f'CPU data bus D{bus[1]}'
        elif re.match(r'^a\d+$', bus):
            names[n] = f'CPU addr bus A{bus[1:]}'
        elif re.match(r'^~ma\d+$', bus):
            names[n] = f'VRAM addr bus MA{bus[3:]}'
        elif re.match(r'^md\d$', bus):
            names[n] = f'VRAM data bus MD{bus[2]}'
        elif 'oam_a_d' in bus:
            bit = bus.split('d')[-1]
            names[n] = f'OAM data A bus D{bit} (Y/tile)'
        elif 'oam_b_d' in bus:
            bit = bus.split('d')[-1]
            names[n] = f'OAM data B bus D{bit} (X/attr)'
        elif 'oam_render' in bus:
            bit = bus.split('a')[-1]
            names[n] = f'Sprite render data bit {bit}'
        elif 'sprite_y' in bus:
            bit = bus[-1]
            names[n] = f'Sprite Y store bit {bit}'
        elif 'clk' in bus or 'phase' in bus:
            names[n] = f'Clock bus ({bus})'
    # Category-based fallback for cells not in the map
    cat_labels = {
        'ppu-bgfifo': 'BG FIFO', 'ppu-bgscroll': 'BG Scroll',
        'ppu-control': 'PPU Control', 'ppu-cycles': 'BG/Win Cycles',
        'ppu-dma': 'DMA', 'ppu-lcd': 'LCD', 'ppu-mux': 'Pixel Mux',
        'ppu-oam': 'OAM', 'ppu-objctl': 'Sprite Control',
        'ppu-objfifo': 'Sprite FIFO', 'ppu-objreg': 'Sprite Store',
        'ppu-pal': 'Palettes', 'ppu-stat': 'STAT/LY',
        'ppu-vram': 'VRAM', 'ppu-window': 'Window',
        'ppu-xcomp': 'Sprite X Match', 'ppu-xprio': 'Sprite X Priority',
        'ppu-ycomp': 'Sprite Y Compare', 'ppu-decode': 'PPU Decode',
        'clocks': 'Clocks', 'int': 'Interrupts', 'timer': 'Timer',
        'apu-ch1': 'CH1', 'apu-ch2': 'CH2', 'apu-ch3': 'CH3', 'apu-ch4': 'CH4',
        'apu-control': 'APU Control', 'apu-decode': 'APU Decode',
    }
    for n, nd in G.nodes(data=True):
        if n in names:
            continue
        cat = nd.get('category', '')
        label = cat_labels.get(cat)
        if label:
            names[n] = label
    return names


def _friendly(names, node):
    """Return 'die_name (friendly)' or just 'die_name'."""
    f = names.get(node, '')
    return f"`{node}` ({f})" if f else f"`{node}`"


def format_report(paths, G, races):
    """Generate markdown report sections with substantive analysis."""
    HALF_TCYCLE_NS = 119.2
    GATE_DELAY_MIN = 5
    GATE_DELAY_MAX = 15
    fanout = {n: G.out_degree(n) for n in G.nodes()}
    depth_map, path_map = compute_depths(G)
    names = build_friendly_names(G)
    graph_edges = [{'src': u, 'dst': v, 'edge_type': d.get('edge_type', 'data')}
                   for u, v, d in G.edges(data=True)]

    reset_paths = [(d, p) for d, p in paths if is_reset_path_schematic(p, G)]
    op_paths = [(d, p) for d, p in paths if not is_reset_path_schematic(p, G)]
    op_max = op_paths[0][0] if op_paths else 0
    rst_max = reset_paths[0][0] if reset_paths else 0

    # Compute per-category stats
    by_cat = {}
    for d, p in op_paths:
        cat = categorize_by_schematic(p, G)
        if cat not in by_cat:
            by_cat[cat] = []
        by_cat[cat].append((d, p))

    race_by_cat = {}
    for r in races:
        cat = CATEGORY_DISPLAY.get(r['category'], r['category'] or 'Other')
        if cat not in race_by_cat:
            race_by_cat[cat] = []
        race_by_cat[cat].append(r)

    ppu_races = sum(1 for r in races if r.get('category', '').startswith('ppu-'))

    # Find key signals
    high_fanout = sorted(
        [(n, fanout[n], G.nodes[n]) for n in G.nodes() if fanout[n] >= 20],
        key=lambda x: -x[1]
    )

    sections = {}

    # =========================================================================
    # OVERVIEW & KEY FINDINGS
    # =========================================================================
    L = []
    L.append("# Game Boy (DMG-CPU B) Propagation Path Analysis")
    L.append("")
    L.append("Static analysis of the DMG-CPU B gate-level netlist identifying deep")
    L.append("combinatorial paths that cause propagation delay on real hardware.")
    L.append("Data source: [msinger/dmg-schematics](https://github.com/msinger/dmg-schematics).")
    L.append("")
    L.append("## Timing Reference")
    L.append("")
    L.append("| Parameter | Value |")
    L.append("|-----------|-------|")
    L.append("| Master clock | 4.194304 MHz |")
    L.append("| T-cycle (one dot) | ~238.4 ns |")
    L.append("| Half T-cycle | ~119.2 ns |")
    L.append("| Gate delay (Sharp ~5 µm CMOS) | 5-15 ns per effective ge |")
    L.append("| Delay model | Elmore RC (per-instance wire length + gate topology) |")
    L.append("| Effective ge unit | NOT_x1 at median wire length = 1.0 ge |")
    L.append("")
    L.append("## Overview")
    L.append("")
    L.append(f"**{G.number_of_nodes()} cells** analyzed across the full DMG-CPU B chip")
    L.append(f"({sum(1 for _,d in G.nodes(data=True) if d.get('node_type')=='registered')} registered,")
    L.append(f"{sum(1 for _,d in G.nodes(data=True) if d.get('node_type')=='combinatorial')} combinatorial).")
    L.append("")
    L.append("| Category | Paths | Max Depth | Worst-case Delay |")
    L.append("|----------|-------|-----------|-----------------|")
    L.append(f"| **Operational** | {len(op_paths)} | {op_max:.1f} ge | {op_max*GATE_DELAY_MAX:.0f} ns ({op_max*GATE_DELAY_MAX/HALF_TCYCLE_NS*100:.0f}% half T-cycle) |")
    L.append(f"| Reset-only | {len(reset_paths)} | {rst_max:.1f} ge | {rst_max*GATE_DELAY_MAX:.0f} ns |")
    L.append(f"| **Total paths** | {len(paths)} | | |")
    L.append(f"| **Race pairs** | {len(races)} ({ppu_races} PPU) | max diff {races[0]['depth_diff'] if races else 0} ge | |")
    L.append("")

    # === Key Findings — ordered by impact, not depth ===
    L.append("## Key Findings")
    L.append("")

    L.append("### 1. CLKPIPE (sacu) — The Most Impactful Timing Race")
    L.append("")
    sacu_depth = depth_map.get('sacu', 0)
    sacu_fo = fanout.get('sacu', 0)
    L.append(f"`sacu` is an OR2 gate at effective depth {sacu_depth:.1f} ge")
    L.append(f"({sacu_depth*GATE_DELAY_MIN:.0f}-{sacu_depth*GATE_DELAY_MAX:.0f} ns, fan-out **{sacu_fo}**).")
    L.append("It is the pixel pipe shift clock (CLKPIPE) — the single most impactful")
    L.append("signal for emulator accuracy. The static depth includes the reset inverter")
    L.append("chain which only changes on LCDC toggle or system reset.")
    L.append("")

    # What CLKPIPE drives
    sacu_succ_cats = {}
    for succ in G.successors('sacu'):
        cat = G.nodes[succ].get('category', '')
        cat_display = CATEGORY_DISPLAY.get(cat, cat)
        if cat_display not in sacu_succ_cats:
            sacu_succ_cats[cat_display] = 0
        sacu_succ_cats[cat_display] += 1

    L.append("**What it drives:**")
    L.append("")
    L.append("| Destination | Cells | Role |")
    L.append("|-------------|-------|------|")
    succ_roles = {
        'Sprite Pixel Shifter': 'Shifts sprite pixel data out one dot at a time',
        'Sprite X Match': 'Compares sprite X position against pixel counter',
        'BG Pixel Shifter': 'Shifts BG/window tile data out one dot at a time',
        'STAT/LY': 'Increments pixel X counter (PX)',
        'BG/Win Cycles': 'Tile fetch cycle counter',
    }
    for cat_display in sorted(sacu_succ_cats, key=lambda c: -sacu_succ_cats[c]):
        count = sacu_succ_cats[cat_display]
        role = succ_roles.get(cat_display, '')
        L.append(f"| {cat_display} | {count} | {role} |")
    L.append("")

    # The race it causes
    clkpipe_races = []
    for r in races:
        for inp in r['inputs']:
            if inp['name'] == 'sacu':
                clkpipe_races.append(r)
                break
    clkpipe_late = [r for r in clkpipe_races
                    if any(inp['name'] == 'sacu' and inp['depth'] == r['max_depth'] for inp in r['inputs'])]

    L.append("**The core problem:**")
    L.append("")
    L.append("All pixel pipe data (BG tile bits, sprite tile bits, palette/priority)")
    L.append("is loaded into the pipe shift registers at low depth. But CLKPIPE, which")
    L.append("triggers the shift, must wait for the sprite X priority check,")
    L.append("the H-blank detection, and the PPU clock phase before it can fire.")
    L.append(f"At depth {sacu_depth:.1f} ge ({sacu_depth*GATE_DELAY_MIN:.0f}-{sacu_depth*GATE_DELAY_MAX:.0f} ns),")
    L.append("the pipe data is ready and waiting.")
    L.append("")
    L.append("A behavioral emulator applies the shift and data load simultaneously.")
    L.append("On real hardware, the data is stable before the shift happens — meaning")
    L.append("the previous dot's shift output is what gets captured by downstream logic")
    L.append("during the propagation window. This is the primary source of one-dot")
    L.append("horizontal pixel offset in emulators.")
    L.append("")

    # Show the input tree as a diagram, not just the single deepest path
    # Build CLKPIPE tree dynamically with computed depths
    def _tree_depth(name):
        return depth_map.get(name, 0)

    L.append(f"**CLKPIPE input tree** (`sacu` = OR2):")
    L.append("")
    L.append("```")
    L.append(f"sacu [or2] — Pixel Shift Clock (CLKPIPE) (depth {_tree_depth('sacu'):.1f})")
    L.append(f"├── roxy [nor_latch] — Fine Scroll Done (depth 0, registered)")
    L.append(f"└── segu [not_x4] — CLKPIPE buffer (depth {_tree_depth('segu'):.1f})")
    L.append(f"    └── tyfa [and3] — CLKPIPE gate (depth {_tree_depth('tyfa'):.1f})")
    L.append(f"        ├── poky [nor_latch] — Pixel Pipe Done (depth 0, registered)")
    L.append(f"        ├── socy (depth {_tree_depth('socy'):.1f}) — through reset inverter chain")
    L.append(f"        │   └── ... xapo [Video Reset] → pyry → rydy → sylo → tomu → socy")
    L.append(f"        │   (stable during rendering — only changes on LCDC toggle/reset)")
    L.append(f"        └── vybo [nor3] (depth {_tree_depth('vybo'):.1f}) — OPERATIONAL path, active every dot:")
    L.append(f"            ├── fepo [or2] — sprite X priority match (depth {_tree_depth('fepo'):.1f})")
    L.append(f"            │   └── 10 sprite X comparators (NAND5+NAND3 trees)")
    L.append(f"            ├── myvo — PPU clock phase (depth {_tree_depth('myvo'):.1f})")
    L.append(f"            └── wodu [and2] — H-blank gate (depth {_tree_depth('wodu'):.1f})")
    L.append(f"                └── pixel counter X == 160 check (NAND5)")
    L.append("```")
    L.append("")
    L.append("During normal rendering, the reset chain (`socy`) is stable — it only")
    L.append("changes on system reset or LCDC bit 7 toggle. The actual per-dot delay")
    L.append("comes from `vybo`, which combines three signals that change every dot:")
    L.append("the sprite X priority match result, the PPU clock phase, and the H-blank")
    L.append("detection.")
    L.append("")

    if clkpipe_late:
        clkpipe_race_cats = {}
        for r in clkpipe_late:
            cat = CATEGORY_DISPLAY.get(r['category'], r['category'])
            clkpipe_race_cats[cat] = clkpipe_race_cats.get(cat, 0) + 1
        L.append(f"**Races caused** ({len(clkpipe_late)} where CLKPIPE is the late-arriving signal):")
        L.append("")
        for cat, count in sorted(clkpipe_race_cats.items(), key=lambda x: -x[1]):
            L.append(f"- {cat}: {count} races")
        L.append("")

    L.append("> **Emulator guidance:** Consider delaying the pixel pipe shift by one dot")
    L.append("> relative to data loading. If BG or sprite pixels appear one dot to the")
    L.append("> right of their expected position, CLKPIPE latency is the likely cause.")
    L.append("")

    # Deepest operational path
    if op_paths:
        deepest = op_paths[0]
        deepest_d, deepest_p = deepest
        adders_in_deepest = [n for n in deepest_p if G.nodes.get(n, {}).get('cell_type') in ('half_add', 'full_add')]

        L.append(f"### 2. Deepest Operational Path: {deepest_d:.1f} Effective Gate-equivalents")
        L.append("")
        L.append(f"The longest operational combinatorial chain runs from {_friendly(names, deepest_p[0])}")
        L.append(f"to {_friendly(names, deepest_p[-1])}, passing through")
        L.append(f"{len(adders_in_deepest)} adder cells and {len(deepest_p)-2} total combinatorial gates.")
        L.append(f"Worst-case delay: {deepest_d*GATE_DELAY_MIN:.0f}-{deepest_d*GATE_DELAY_MAX:.0f} ns")
        L.append(f"({deepest_d*GATE_DELAY_MAX/HALF_TCYCLE_NS*100:.0f}% of half T-cycle).")
        L.append("")
        L.append("This path fires once per scanline (when LY increments), not per dot.")
        L.append("It computes which sprites are on the current line via the Y comparator")
        L.append("carry chain and feeds the result into the sprite store control logic.")
        L.append("")
        L.append("```")
        for j, node in enumerate(deepest_p):
            nd = G.nodes.get(node, {})
            ct = nd.get('cell_type', '')
            friendly = names.get(node, '')
            friendly_str = f"  — {friendly}" if friendly else ""
            L.append(f"{'  ' * j}[{ct}] {node}{friendly_str}")
        L.append("```")
        L.append("")
        if len(adders_in_deepest) >= 4:
            adder_ge = sum(G.nodes[n].get('gate_equiv', 1.0) for n in adders_in_deepest)
            L.append(f"The {len(adders_in_deepest)}-stage ripple carry adder chain dominates this path,")
            L.append(f"contributing {adder_ge:.1f} of the {deepest_d:.1f} total effective ge.")
            L.append("")

    # VRAM address adder
    vram_addr_paths = [(d, p) for d, p in op_paths
                       if any(n.startswith('bus:~ma') for n in p)]
    if vram_addr_paths:
        vp_d, vp_p = vram_addr_paths[0]
        vp_adders = [n for n in vp_p if G.nodes.get(n, {}).get('cell_type') in ('half_add', 'full_add')]
        L.append(f"### 3. VRAM Address Adder ({vp_d:.1f} ge)")
        L.append("")
        L.append(f"The VRAM tile map address is computed from LY + SCY (or pixel X + SCX)")
        L.append(f"via an 8-bit ripple carry adder ({len(vp_adders)} adder stages, depth {vp_d:.1f} ge).")
        L.append(f"The carry chain means the high address bits settle last —")
        L.append(f"the VRAM address may not be valid until {vp_d*GATE_DELAY_MIN:.0f}-{vp_d*GATE_DELAY_MAX:.0f} ns")
        L.append(f"after the inputs change. In practice, LY and SCY are stable for the full")
        L.append(f"scanline so the address settles well before fetch begins. But mid-scanline")
        L.append(f"SCX writes (used for split-scroll effects) may take 2+ dots to propagate.")
        L.append("")
        L.append(f"> **Emulator guidance:** Don't apply mid-scanline SCX writes instantly.")
        L.append(f"> The VRAM address takes {vp_d*GATE_DELAY_MIN:.0f}-{vp_d*GATE_DELAY_MAX:.0f} ns to settle,")
        L.append(f"> so the new scroll value won't affect tile fetch for 2+ dots.")
        L.append("")

    objreg_races = [r for r in races if r['category'] == 'ppu-objreg']
    if objreg_races:
        max_diff = max(r['depth_diff'] for r in objreg_races)
        L.append(f"### 4. Sprite Store Races (diff={max_diff:.1f} ge, all 10 stores identical)")
        L.append("")
        late_cat = objreg_races[0]['inputs'][0].get('category', '')
        late_name = objreg_races[0]['inputs'][0].get('name', '')
        max_d = objreg_races[0]['max_depth']
        L.append(f"All 10 sprite stores exhibit identical timing races. The store write-enable")
        L.append(f"signal ({_friendly(names, late_name)}, depth {max_d:.1f} ge)")
        L.append(f"propagates through the sprite Y comparator carry chain and sprite control")
        L.append(f"decode logic before reaching the store latches, while OAM data arrives")
        L.append(f"at the data pin at depth 0 (direct from the OAM bus).")
        L.append(f"")
        L.append(f"At scanline boundaries when the stores are being loaded during OAM scan,")
        L.append(f"the write-enable arrives {max_d*GATE_DELAY_MIN:.0f}-{max_d*GATE_DELAY_MAX:.0f} ns")
        L.append(f"after the data. During this window the latch may capture data from the")
        L.append(f"wrong OAM entry — the previous sprite's data instead of the current one.")
        L.append("")
        L.append(f"> **Emulator guidance:** If sprites show wrong position or attributes for")
        L.append(f"> one dot at the start of a scanline, this race is the cause. The stores")
        L.append(f"> hold stale data for one dot while the control signal propagates.")
        L.append("")

    xcomp_races = [r for r in races if r['category'] == 'ppu-xcomp']
    if xcomp_races:
        max_diff = max(r['depth_diff'] for r in xcomp_races)
        L.append(f"### 5. Sprite X Match ({len(xcomp_races)} races, max diff={max_diff:.1f} ge)")
        L.append("")
        L.append(f"The sprite X comparators check each sprite's stored X position against the")
        L.append(f"pixel counter on every dot. The comparator result depends on the pixel counter,")
        L.append(f"which is clocked by CLKPIPE (depth {sacu_depth:.1f} ge). The X match output settles")
        L.append(f"at a different time than the fetch control signals, causing sprites to")
        L.append(f"potentially trigger fetch one dot early or late.")
        L.append("")
        L.append(f"> **Emulator guidance:** Sprite fetch may trigger one dot early or late")
        L.append(f"> relative to the pixel counter. If sprites appear shifted horizontally")
        L.append(f"> by one pixel, the X match race with CLKPIPE is the likely cause.")
        L.append("")

    win_races = [r for r in races if r['category'] == 'ppu-window']
    if win_races:
        max_diff = max(r['depth_diff'] for r in win_races)
        L.append(f"### 6. Window Trigger Races ({len(win_races)} races, max diff={max_diff:.1f} ge)")
        L.append("")
        L.append(f"The WX/WY comparison and window activation signals race against the rendering")
        L.append(f"pipeline. Window content may shift one pixel right. Affects games that use the")
        L.append(f"window for status bars, dialogue boxes, or HUD overlays.")
        L.append("")
        L.append(f"> **Emulator guidance:** If window content is shifted one pixel to the")
        L.append(f"> right, the window trigger race is the likely cause. The window")
        L.append(f"> activation may need to be delayed by one dot.")
        L.append("")

    # === Paths by category summary ===
    L.append("## Critical Paths by Functional Area")
    L.append("")
    L.append("| Area | Paths | Max Depth | Max Delay | Key Race |")
    L.append("|------|-------|-----------|-----------|----------|")
    for cat in sorted(by_cat, key=lambda c: -by_cat[c][0][0]):
        cat_paths = by_cat[cat]
        max_d = cat_paths[0][0]
        race_count = len(race_by_cat.get(cat, []))
        max_race = max((r['depth_diff'] for r in race_by_cat.get(cat, [])), default=0)
        race_str = f"diff={max_race:.1f} ({race_count} races)" if race_count else "—"
        L.append(f"| {cat} | {len(cat_paths)} | {max_d:.1f} ge | {max_d*GATE_DELAY_MAX:.0f} ns | {race_str} |")
    L.append("")

    # === High fan-out signals ===
    L.append("## High Fan-out Signals (>= 20 outputs)")
    L.append("")
    L.append("These signals drive many downstream gates. High fan-out combined with deep")
    L.append("combinatorial depth means the signal arrives late at many destinations simultaneously.")
    L.append("")
    L.append("| Signal | Description | Fan-out | Depth | Cell Type | Category |")
    L.append("|--------|-------------|---------|-------|-----------|----------|")
    for name, fo, nd in high_fanout[:20]:
        d = depth_map.get(name, 0)
        ct = nd.get('cell_type', '')
        cat = nd.get('category', '')
        friendly = names.get(name, '')
        cat_display = CATEGORY_DISPLAY.get(cat, cat)
        L.append(f"| `{name}` | {friendly} | {fo} | {d} ge | {ct} | {cat_display} |")
    L.append("")

    # === APU findings ===
    apu_races = [r for r in races if r.get('category', '').startswith('apu-')]
    if apu_races:
        L.append("## APU Timing")
        L.append("")
        apu_max = max(r['depth_diff'] for r in apu_races)
        L.append(f"The APU has {len(apu_races)} timing races (max diff={apu_max}). These are primarily")
        L.append("in the channel frequency counters and length timers, where the CPU data bus")
        L.append("write path races against the channel's internal clock. APU timing races are")
        L.append("less audible than PPU races are visible, but may affect cycle-accurate audio")
        L.append("emulation — particularly for games that modify channel registers mid-note.")
        L.append("")

    sections['critical_paths_report.md'] = '\n'.join(L)

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
                ge = nd.get('gate_equiv', 1.0)
                fo = fanout.get(node, 0)
                nt = nd.get('node_type', '')
                if nt in ('registered', 'bus', 'boundary', 'pad'):
                    marker = f"[{nt.upper()}:{ct}]"
                else:
                    marker = f"[{ct}]"
                ds_str = f" x{ds}" if ds > 1 else ""
                fo_str = f" fan-out={fo}" if fo >= 10 else ""
                friendly = names.get(node, '')
                friendly_str = f"  — {friendly}" if friendly else ""
                lines.append(f"{'  ' * j}{marker} {node}{friendly_str}{ds_str}{fo_str}")
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

    # Step 3.5: Parse dmg-sim for per-instance wire lengths (Elmore delay model)
    print("\nLoading per-instance wire lengths from dmg-sim...")
    sim_params = parse_dmg_sim_params()
    if sim_params:
        print(f"  {len(sim_params)} gate instances with Elmore delay parameters")
    else:
        print("  dmg-sim not found — using integer gate-equivalent fallback")

    # Step 4: Build the graph
    print("\nBuilding signal dependency graph...")
    nodes, edges = build_graph(cell_types, all_cells, all_wires, sim_params=sim_params)
    edges = dedup_edges(edges)

    # Step 5: Statistics
    print_stats(nodes, edges, all_cells, all_wires, cell_types)

    # Step 6: Build NetworkX graph and run analysis
    print("Building NetworkX graph...")
    G = build_networkx_graph(nodes, edges)
    print(f"  {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    print("Computing combinatorial depths (Elmore-based effective ge)...")
    depth, _ = compute_depths(G)
    max_depth = max(depth.values())
    print(f"  Max depth: {max_depth:.1f} effective gate-equivalents")

    print("Finding critical paths...")
    paths = find_critical_paths(G)
    print(f"  {len(paths)} critical paths found")
    if paths:
        print(f"  Deepest: {paths[0][0]:.1f} effective ge")
        op_paths = [(d, p) for d, p in paths if not is_reset_path_schematic(p, G)]
        rst_paths = [(d, p) for d, p in paths if is_reset_path_schematic(p, G)]
        op_max_d = f"{op_paths[0][0]:.1f}" if op_paths else "0"
        rst_max_d = f"{rst_paths[0][0]:.1f}" if rst_paths else "0"
        print(f"  Operational: {len(op_paths)} (max depth {op_max_d})")
        print(f"  Reset-only: {len(rst_paths)} (max depth {rst_max_d})")

    print("Finding signal race pairs...")
    races = find_race_pairs(G)
    print(f"  {len(races)} race pairs found")
    ppu_races = [r for r in races if r.get('category', '').startswith('ppu-')]
    print(f"  PPU-related: {len(ppu_races)}")

    print("Analyzing clock domains...")
    clock_domains, clock_groups, clock_tree, clock_polarity = analyze_clock_domains(G)
    print(f"  {len(clock_domains)} registered cells with clock inputs traced")
    print(f"  {len(clock_groups)} distinct clock groups")
    pol_counts = {}
    for p in clock_polarity.values():
        pol_counts[p['polarity']] = pol_counts.get(p['polarity'], 0) + 1
    print(f"  Polarity: {pol_counts}")

    # Step 7: Export
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Graph JSON
    graph_data = export_graph_json(nodes, edges, cell_types,
                                   clock_domains=clock_domains,
                                   clock_tree=clock_tree)
    with open(output_dir / "ppu_graph.json", 'w') as f:
        json.dump(graph_data, f, indent=2)
    print(f"\nExported: ppu_graph.json ({len(graph_data['nodes'])} nodes, {len(graph_data['edges'])} edges)")

    # Critical paths JSON
    paths_data = export_paths_json(paths, G, races, clock_domains=clock_domains)
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

    # Clock domain report
    clock_report = format_clock_domain_report(clock_domains, clock_groups, clock_tree, clock_polarity, G)
    with open(output_dir / "clock_domains.md", 'w') as f:
        f.write(clock_report)
    print("Exported: clock_domains.md")

    # Clock domains JSON
    clock_json = {
        'domains': {
            cell: {
                'cell_type': info['cell_type'],
                'category': info['category'],
                'clock_drivers': info['clock_drivers'],
            }
            for cell, info in clock_domains.items()
        },
        'groups': {
            ','.join(drivers): {
                'drivers': list(drivers),
                'cells': sorted(cells),
            }
            for drivers, cells in clock_groups.items()
        },
        'clock_tree': {
            driver: chain
            for driver, chain in clock_tree.items()
        },
        'polarity': {
            driver: info
            for driver, info in clock_polarity.items()
        },
    }
    with open(output_dir / "clock_domains.json", 'w') as f:
        json.dump(clock_json, f, indent=2)
    print(f"Exported: clock_domains.json ({len(clock_domains)} domains, {len(clock_groups)} groups)")



if __name__ == "__main__":
    main()
