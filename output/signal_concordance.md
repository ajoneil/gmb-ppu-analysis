# Game Boy PPU Signal Concordance

Cross-reference between GateBoy's internal cell names and standard Game Boy
documentation (Pan Docs, Gekkio's gb-ctr, Furrtek's DMG-CPU-Inside).

## How to Read GateBoy Signal Names

```
MUWY_LY0p_odd
^^^^          4-char cell name (Furrtek die reference)
     ^^^      functional name (LY bit 0)
        ^     polarity: p = positive, n = negative/inverted
          ^^^ clock phase: odd/evn (which subcycle it's valid)
```

Additional suffixes: `_D0`-`_D7` (bit index), `_A00n`-`_A15p` (address bit),
`_CLK`/`_EN`/`_RST` (control role), `_old`/`_new` (temporal phase).

Die page references in comments: `/*#p21.MUWY*/` = page 21, cell MUWY.

---

## PPU Registers (Memory-Mapped)

### LCDC — LCD Control (FF40)

| Bit | GateBoy Cell | Signal Name | Pan Docs | Function |
|-----|-------------|-------------|----------|----------|
| 7 | VYXE | `LCDC_LCDENp` | LCDC.7 | LCD & PPU master enable |
| 6 | WOKY | `LCDC_WINMAPp` | LCDC.6 | Window tile map select (0=9800, 1=9C00) |
| 5 | WYMO | `LCDC_WINENp` | LCDC.5 | Window enable |
| 4 | WEXU | `LCDC_BGTILEp` | LCDC.4 | BG/Window tile data select (0=8800, 1=8000) |
| 3 | XAFO | `LCDC_BGMAPp` | LCDC.3 | BG tile map select (0=9800, 1=9C00) |
| 2 | XYMO | `LCDC_SPSIZEp` | LCDC.2 | Sprite size (0=8x8, 1=8x16) |
| 1 | XYLO | `LCDC_SPENp` | LCDC.1 | Sprite enable |
| 0 | PRENY | `LCDC_BGENp` | LCDC.0 | BG/Window enable (DMG) / priority (CGB) |

### STAT — LCD Status (FF41)

| Bit | GateBoy Cell | Signal Name | Pan Docs | Function |
|-----|-------------|-------------|----------|----------|
| 6 | RUGU | `STAT_LYI_ENp` | STAT.6 | LY=LYC interrupt enable |
| 5 | REFE | `STAT_OAI_ENp` | STAT.5 | Mode 2 (OAM scan) interrupt enable |
| 4 | RUFO | `STAT_VBI_ENp` | STAT.4 | Mode 1 (VBlank) interrupt enable |
| 3 | ROXE | `STAT_HBI_ENp` | STAT.3 | Mode 0 (HBlank) interrupt enable |
| 2 | — | `STAT_LYCp` | STAT.2 | LY=LYC match flag (read-only) |
| 1-0 | — | `STAT_MODEp` | STAT.1-0 | Mode flag (read-only) |

### SCY — Scroll Y (FF42)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0-7 | GAVE, FYMO, FEZU, FUJO, DEDE, FOTY, FOHA, FUNY | `SCY_D[0:7]p` | Background Y scroll position |

### SCX — Scroll X (FF43)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0-7 | DATY, DUZU, CYXU, GUBO, BEMY, CUZY, CABU, BAKE | `SCX_D[0:7]p` | Background X scroll position |

Fine scroll uses bits 0-2 of SCX (the sub-tile pixel offset).

### LY — LCD Y Coordinate (FF44, read-only)

| Bit | GateBoy Cell | Signal Name | Phase | Pan Docs |
|-----|-------------|-------------|-------|----------|
| 0 | MUWY | `LY0p_odd` | ODD | Current scanline (0-153) |
| 1 | MYRO | `LY1p_odd` | ODD | |
| 2 | LEXA | `LY2p_odd` | ODD | |
| 3 | LYDO | `LY3p_odd` | ODD | |
| 4 | LOVU | `LY4p_odd` | ODD | |
| 5 | LEMA | `LY5p_odd` | ODD | |
| 6 | MATO | `LY6p_odd` | ODD | |
| 7 | LAFO | `LY7p_odd` | ODD | VBlank begins at LY=144 |

### LYC — LY Compare (FF45)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0-7 | SYRY, VUCE, SEDY, SALO, SOTA, VAFA, VEVO, RAHA | `LYC[0:7]p` | LY comparison value |

### DMA — DMA Transfer (FF46)

| Byte | GateBoy Cells | Signal Name | Pan Docs |
|------|--------------|-------------|----------|
| High (A8-15) | NAFA-MARU | `DMA_A[08:15]p` | Source address high byte |
| Low (A0-7) | NAKY-MUGU | `DMA_A[00:07]p_odd` | Source address low byte |

### BGP — BG Palette Data (FF47)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0-7 | PAVO, NUSY, PYLU, MAXY, MUKE, MORU, MOGY, MENA | `BGP_D[0:7]p` | BG palette (4 x 2-bit colors) |

### OBP0 — Sprite Palette 0 (FF48)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0-7 | XUFU, XUKY, XOVA, XALO, XERU, XYZE, XUPO, XANA | `OBP0_D[0:7]p` | Sprite palette 0 |

### OBP1 — Sprite Palette 1 (FF49)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0-7 | MOXY, LAWO, MOSA, LOSE, LUNE, LUGU, LEPU, LUXO | `OBP1_D[0:7]p` | Sprite palette 1 |

### WY — Window Y Position (FF4A)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0-7 | NESO, NYRO, NAGA, MELA, NULO, NENE, NUKA, NAFU | `WY_D[0:7]p` | Window Y trigger position |

### WX — Window X Position (FF4B)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0-7 | MYPA, NOFE, NOKE, MEBY, MYPU, MYCE, MUVO, NUKU | `WX_D[0:7]p` | Window X trigger position (WX-7 = screen X) |

---

## Internal PPU Signals

### Timing & Counters

| Signal | GateBoy Cell(s) | Bits | Phase | Pan Docs Equivalent | Role in Critical Paths |
|--------|-----------------|------|-------|--------------------|-----------------------|
| Pixel X Counter | XEHO-SYBE (`PX[0:7]p_odd`) | 8 | ODD | X position (0-159 visible) | Races CLKPIPE at pixel pipe DFFs |
| Internal X (LX) | SAXO-TYRY (`LX[0:6]p_odd`) | 7 | ODD | Internal dot counter | Drives line-end detection |
| Line End | RUTU (`LINE_ENDp_odd`) | 1 | ODD | End of scanline | Fires at LX=113 |
| VBlank | POPU (`VBLANKp_odd`) | 1 | ODD | LY >= 144 | VBlank period flag |
| Frame End | MYTA (`FRAME_ENDp_odd`) | 1 | ODD | LY == 153 | Frame counter wrap |

### Pixel Pipe Shift Clock (CRITICAL)

| Signal | GateBoy Cell | Phase | Fan-out | Depth | Role |
|--------|-------------|-------|---------|-------|------|
| CLKPIPE | SACU | ODD/EVN | **52** | **16** | Master shift clock for all pixel pipelines |

This is the single most impactful signal for emulator timing. It drives every
pixel-level decision (BG pipe shift, sprite pipe shift, mask pipe, palette pipe,
pixel counter increment) but arrives through a 16-gate buffer chain. All pipe
data is ready at depth 3-8, meaning the pipe effectively shifts ~80-240 ns after
data settles.

### Rendering Mode Control

| Signal | GateBoy Cell | Type | Phase | Pan Docs Mode | Description |
|--------|-------------|------|-------|---------------|-------------|
| Rendering Active | XYMU (`RENDERING_LATCHn`) | NorLatch | — | Mode 3 gate | High during pixel output |
| HBlank Gate | WODU (`HBLANK_GATEp_odd`) | Gate | ODD | Mode 0 indicator | Active during H-blank |
| HBlank (even) | VOGA (`HBLANKp_evn`) | DFF17 | EVN | Mode 0 (even phase) | Even-phase H-blank copy |

### Tile Fetcher (Background/Window)

| Signal | GateBoy Cell | Type | Phase | Function |
|--------|-------------|------|-------|----------|
| Fetch State 0 | LAXU (`BFETCH_S0p_odd`) | DFF17 | ODD | Tile index fetch |
| Fetch State 1 | MESU (`BFETCH_S1p_odd`) | DFF17 | ODD | Tile data low byte |
| Fetch State 2 | NYVA (`BFETCH_S2p_odd`) | DFF17 | ODD | Tile data high byte |
| Fetch Done | LYRY (`BFETCH_DONEp_odd`) | Gate | ODD | 6-dot fetch complete |
| Fetching Active | LONY (`TFETCHINGp`) | NandLatch | — | Fetch pipeline running |
| **Fetch Reset** | NYXU (`BFETCH_RSTn`) | Comb | — | **Depth 17 — late arrival** |

The fetch reset signal (NYXU) is the deepest operational signal, passing through
the VID_RST chain and line-end logic before reaching the fetch state machine.

### Sprite Fetcher

| Signal | GateBoy Cell | Type | Phase | Function |
|--------|-------------|------|-------|----------|
| Fetch State 0 | TOXE (`SFETCH_S0p_evn`) | DFF17 | EVN | Sprite fetch phase 0 |
| Fetch State 1 | TULY (`SFETCH_S1p_evn`) | DFF17 | EVN | Sprite fetch phase 1 |
| Fetch State 2 | TESE (`SFETCH_S2p_evn`) | DFF17 | EVN | Sprite fetch phase 2 |
| Fetching Active | TEXY (`SFETCHINGp_evn`) | Gate | EVN | Sprite fetch running |
| Fetch Running | TAKA (`SFETCH_RUNNINGp_evn`) | NandLatch | EVN | Persist fetch state |
| Fetch Request | SOBU (`SFETCH_REQp_evn`) | DFF17 | EVN | Trigger sprite fetch |
| Fetch Done | WUTY (`SFETCH_DONE_TRIGp_odd`) | Gate | ODD | Sprite fetch complete |

### Sprite Scanner (OAM Search — Mode 2)

| Signal | GateBoy Cell | Type | Phase | Function |
|--------|-------------|------|-------|----------|
| Scan Counter | YFEL-FONY (`SCAN[0:5]_odd`) | DFF17 | ODD | OAM index (0-39) |
| Sprite Index | XADU-XECU (`SPRITE_IDX[0:5]p_odd`) | DFF17 | ODD | Store slot (0-9) |
| Sprite Count | BESE-DYBE (`SPRITE_COUNT[0:3]_odd`) | DFF17 | ODD | Found sprites (0-10) |
| **Scan Done** | BESU (`SCAN_DONEn_odd`) | NorLatch | ODD | **Depth 17 race — OAM scan may extend one dot** |
| Scan Done (even) | DOBA (`SCAN_DONEp_evn`) | DFF17 | EVN | Even phase copy |

### Sprite Store (10 Sprite Position Latches)

Each of 10 stores holds the sprite's X coordinate for scanline comparison.

| Store | X Position Cells | Index Cells | Line Cells | Critical Race |
|-------|-----------------|-------------|------------|---------------|
| 0 | XEPE-XAKO (`STORE0_X[0:7]p`) | YGUS-YWAK | GYHO-FYHY | Reset depth 17 vs data depth 1 |
| 1 | DANY-DUZE (`STORE1_X[0:7]p`) | — | — | Same pattern |
| 2 | FOKA-FOBY (`STORE2_X[0:7]p`) | — | — | Same pattern |
| 3 | XOLY-XYBA (`STORE3_X[0:7]p`) | — | — | Same pattern |
| 4 | WEDU-WAFY (`STORE4_X[0:7]p`) | — | — | Same pattern |
| 5 | FUSA-FEKA (`STORE5_X[0:7]p`) | — | — | Same pattern |
| 6 | YCOL-YBER (`STORE6_X[0:7]p`) | — | — | Same pattern |
| 7 | ERAZ-ENOL (`STORE7_X[0:7]p`) | — | — | Same pattern |
| 8 | EZUF-ENYM (`STORE8_X[0:7]p`) | — | — | Same pattern |
| 9 | CARO-CADO (`STORE9_X[0:7]p`) | — | — | Same pattern |

All 80 store X latches exhibit the same race: the line-end reset signal arrives
at depth 17 while sprite X data from OAM arrives at depth 1. This 16-gate
differential means sprites may capture stale X positions at scanline boundaries.

### Window Control

| Signal | GateBoy Cell | Type | Phase | Function |
|--------|-------------|------|-------|----------|
| WY Match | ROGE (`WY_MATCHp_odd`) | Gate | ODD | LY matches WY register |
| WX Match | NUKO (`WX_MATCHp_odd`) | Gate | ODD | Pixel X matches WX register |
| WY Latch | REJO (`WY_MATCH_LATCHp_odd`) | NorLatch | ODD | Window enabled for rest of frame |
| Window Hit | RYDY (`WIN_HITp`) | Gate | — | Both WX and WY conditions met |
| Window Mode | NOPA (`WIN_MODE_Bp_evn`) | DFF17 | EVN | Window rendering active |

### Fine Scroll (SCX bits 0-2)

| Signal | GateBoy Cell | Type | Phase | Depth | Function |
|--------|-------------|------|-------|-------|----------|
| Fine Count 0 | RYKU (`FINE_CNT0_odd`) | DFF17 | ODD | — | Fine scroll counter bit 0 |
| Fine Count 1 | ROGA (`FINE_CNT1_odd`) | DFF17 | ODD | — | Fine scroll counter bit 1 |
| Fine Count 2 | RUBU (`FINE_CNT2_odd`) | DFF17 | ODD | — | Fine scroll counter bit 2 |
| Fine Match (even) | PUXA (`SCX_FINE_MATCH_evn`) | Gate | EVN | **3** | SCX fine match ready |
| Fine Match (odd) | NYZE (`SCX_FINE_MATCH_odd`) | Gate | ODD | **3** | SCX fine match ready |
| Fine Done | ROXY (`FINE_SCROLL_DONEn`) | NorLatch | — | — | Fine scroll complete |

The fine match signals arrive at depth 3, but CLKPIPE (which they gate) arrives
at depth 16. This 13-gate differential means fine scroll effectively applies one
dot later than a behavioral emulator would predict.

### Pixel Pipelines (Shift Registers)

All pipelines shift on CLKPIPE. Each stage is 8 bits wide.

| Pipeline | Cells (bit 0-7) | Phase | Function |
|----------|-----------------|-------|----------|
| Mask (valid pixel) | VEZO-VAVA | AxCxExGx | Which pixels are visible |
| BG/Window A (low) | MYDE-PYBO | AxCxExGx | BG tile data plane 0 |
| BG/Window B (high) | TOMY-SOHU | AxCxExGx | BG tile data plane 1 |
| Sprite A (low) | NURO-WUFY | AxCxExGx | Sprite tile data plane 0 |
| Sprite B (high) | NYLU-VUPY | AxCxExGx | Sprite tile data plane 1 |
| Palette | RUGO-LYME | — | Sprite palette/priority bits |

### LY = LYC Match Chain

| Signal | GateBoy Cell | Type | Function |
|--------|-------------|------|----------|
| Per-bit XOR (8x) | RYME-SYFU | Comb | `LY_MATCH[0:7]n_old` — XOR each bit pair |
| Upper 4 NOR | SOVU (`LY_MATCHA_old`) | Comb | NOR of bits 4-7 match |
| Lower 4 NOR | SUBO (`LY_MATCHB_old`) | Comb | NOR of bits 0-3 match |
| Full Match | RAPE (`LY_MATCHn_old`) | Comb | NAND of A and B (all 8 match) |
| Match Inverted | PALY (`LY_MATCHa_old`) | Comb | NOT of RAPE |
| Synced Match | ROPO (`LY_MATCH_SYNCp`) | DFF17 | Synced to xxCDEFxx clock |
| Match Latch | RUPO (`LYC_MATCHn`) | NorLatch | Set by ROPO, cleared by FF41 write |

### Interrupt Flags (FF0F)

| Bit | GateBoy Cell | Signal Name | Pan Docs |
|-----|-------------|-------------|----------|
| 0 | LOPE | `FF0F_D0p` | INT_VBLANK |
| 1 | LALU | `FF0F_D1p` | INT_STAT |
| 2 | NYBO | `FF0F_D2p` | INT_TIMER |
| 3 | UBUL | `FF0F_D3p` | INT_SERIAL |
| 4 | ULAK | `FF0F_D4p` | INT_JOYPAD |

### DMA Control

| Signal | GateBoy Cell | Type | Phase | Function |
|--------|-------------|------|-------|----------|
| DMA Active | LYXE (`DMA_LATCHp`) | NorLatch | — | DMA transfer in progress |
| DMA Done | MYTE (`DMA_DONE_odd`) | DFF17 | ODD | Transfer complete |
| DMA Trigger d0 | LUVY (`DMA_TRIG_d0_odd`) | DFF17 | ODD | Initial trigger |
| DMA Trigger d4 | LENE (`DMA_TRIG_d4_odd`) | DFF17 | ODD | Delayed trigger |

### Clock Phases

| Signal | GateBoy Cell | Type | Active Subcycles | Function |
|--------|-------------|------|-----------------|----------|
| Phase ABCD | AFUR (`ABCDxxxx`) | DFF9 | A, B, C, D | CPU clock phase generator |
| Phase BCDE | ALEF (`xBCDExxx`) | DFF9 | B, C, D, E | CPU clock phase generator |
| Phase CDEF | APUK (`xxCDEFxx`) | DFF9 | C, D, E, F | CPU clock phase generator |
| Phase DEFG | ADYK (`xxxDEFGx`) | DFF9 | D, E, F, G | CPU clock phase generator |
| VID clock AB/EF | WUVU (`ABxxEFxx`) | DFF17 | A, B, E, F | PPU video clock |
| VID clock CDEF | VENA (`xxCDEFxx`) | DFF17 | C, D, E, F | PPU video clock |
| VID clock A/DE/H | WOSU (`AxxDExxH`) | DFF17 | A, D, E, H | PPU video clock |

**Phase mapping:**
- `_odd` signals activate on subcycles A, C, E, G (odd-numbered CPU subcycles)
- `_evn` signals activate on subcycles B, D, F, H (even-numbered CPU subcycles)
- The 8 subcycles (A-H) each last ~30 ns, together forming one T-cycle (~238 ns)

### Reset Chain (VID_RST)

The VID_RST chain is the longest inverter chain in the PPU, propagating system
reset and LCDC enable through 8 gates:

```
AFER_SYS_RSTp (registered)
  -> AVOR_SYS_RSTp -> ALUR_SYS_RSTn -> DULA_SYS_RSTp -> CUNU_SYS_RSTn
  -> XORE_SYS_RSTp -> XEBE_SYS_RSTn -> XODO_VID_RSTp -> XAPO_VID_RSTn
```

Branches from XAPO:
- `LYHA_VID_RSTp` -> `LYFE_VID_RSTn` (tile fetcher, sprite scanner)
- `TOFU_VID_RSTp` (pixel pipe resets)
- `ROSY_VID_RSTp` (rendering control)
- `ATAR_VID_RSTp` -> `ABEZ_VID_RSTn` (line timing)
- `PYRY_VID_RSTp` (sprite store resets)

All reset-only critical paths (depth 17-19) pass through this chain. These paths
only fire on system reset or LCDC bit 7 toggle and do not affect per-dot timing.

---

## Bus Signals

### CPU Data Bus

| Bit | GateBoy Node | Direction | Address Decode |
|-----|-------------|-----------|---------------|
| 0-7 | `BUS_CPU_D[00:07]p` | Bidirectional | Directly driven by register reads/writes |

### VRAM Data Bus

| Bit | GateBoy Node | Direction | Usage |
|-----|-------------|-----------|-------|
| 0-7 | `BUS_VRAM_D[0:7]p` | Bidirectional | Tile/map data during fetch |

### VRAM Address Bus

| Bit | GateBoy Node | Direction | Usage |
|-----|-------------|-----------|-------|
| 0-12 | `BUS_VRAM_A[00:12]p` | Output | Tile/map address during fetch |

### OAM Data Bus

| Byte | GateBoy Node | Usage |
|------|-------------|-------|
| A (Y/Tile) | `BUS_OAM_DA[0:7]n` | Sprite Y position, tile index |
| B (X/Attr) | `BUS_OAM_DB[0:7]n` | Sprite X position, attributes |

---

## Naming Convention Quick Reference

| Prefix/Suffix | Meaning | Example |
|---------------|---------|---------|
| `_p` | Positive polarity (active high) | `LCDC_LCDENp` |
| `_n` | Negative polarity (active low) | `BFETCH_RSTn` |
| `_odd` | Valid on odd PPU dots (subcycles A,C,E,G) | `LY0p_odd` |
| `_evn` | Valid on even PPU dots (subcycles B,D,F,H) | `SFETCH_S0p_evn` |
| `_old` | Read from previous clock state (reg_old) | `MUWY_LY0p_odd.qp_old()` |
| `_new` | Being computed this clock (reg_new) | `XAPO_VID_RSTn_new` |
| `@old` | Graph boundary node (register output at clock edge) | `MUWY_LY0p_odd@old` |
| `SIG_` | External signal boundary | `SIG_CPU_*` |
| `PIN_` | Physical pin | `PIN_LCD_*` |
| `BUS_` | Tri-state bus | `BUS_CPU_D00p` |
