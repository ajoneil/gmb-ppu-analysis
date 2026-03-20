# Reset Paths

These paths only fire on system reset or LCDC bit 7 toggle. They all share
the VID_RST inverter chain prefix (8 gates from AFER_SYS_RSTp through XAPO/ATAR/ABEZ).

| Area | Paths | Max Depth | Deepest Sink |
|------|-------|-----------|-------------|
| Tile Fetcher | 6 | 19 | `LAXU_BFETCH_S0p_odd` |
| Sprite Scanner | 9 | 17 | `BESU_SCAN_DONEn_odd` |
| Sprite Store/Match | 90 | 17 | `XEPE_STORE0_X0p` |
| Mode/Rendering Control | 3 | 16 | `XYMU_RENDERING_LATCHn` |
| Scroll/Fine Timing | 4 | 16 | `PUXA_SCX_FINE_MATCH_evn` |
| Pixel Counter | 13 | 16 | `PAHO_X8_SYNC` |
| Pixel Pipeline | 48 | 16 | `NURO_SPR_PIPE_A0` |
| Window Logic | 12 | 16 | `PYCO_WIN_MATCHp_evn` |
| Sprite Fetcher | 4 | 13 | `TOXE_SFETCH_S0p_evn` |
| Other | 22 | 13 | `BESE_SPRITE_COUNT0_odd` |
| Line Timing | 2 | 10 | `RUTU_LINE_ENDp_odd ` |
| LX Counter | 7 | 10 | `SAXO_LX0p_odd` |
| LY Counter | 9 | 10 | `MUWY_LY0p_odd` |
| DMA | 14 | 7 | `NAKY_DMA_A00p_odd` |
| PPU Registers | 39 | 6 | `NESO_WY0p` |
| STAT/LY Match | 5 | 6 | `ROPO_LY_MATCH_SYNCp` |
| LYC Register | 8 | 6 | `SYRY_LYC0p` |
| VRAM Bus | 1 | 4 | `SOTO_DBG_VRAMp` |
| Timer | 1 | 2 | `MOBA_TIMER_OVERFLOWp` |
| Joypad | 4 | 2 | `BATU_JP_GLITCH0` |

**Deepest reset path** (depth 19): `AFER_SYS_RSTp` -> `LAXU_BFETCH_S0p_odd`

```
    [REGISTERED] AFER_SYS_RSTp (fan-out: 13)  (GateBoyReset.cpp:34)
      [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
        [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
          [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
            [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
              [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
                [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                  [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                    [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                      [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                        [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                          [or_and3] BYHA_LINE_RST_TRIGn_odd @ODD  (GateBoyLCD.cpp:121)
                            [not1] ATEJ_LINE_RST_TRIGp_odd @ODD  (GateBoyLCD.cpp:122)
                              [nor2] ANOM_LINE_RSTn_odd_new @ODD  (GateBoy.cpp:754)
                                [not1] BALU_LINE_RSTp_odd_new @ODD  (GateBoy.cpp:755)
                                  [or3] BEBU_SCAN_DONE_tn_odd_new @ODD  (GateBoy.cpp:767)
                                    [not1] AVAP_SCAN_DONE_tp_odd @ODD  (GateBoy.cpp:768)
                                      [nor3] NYXU_BFETCH_RSTn  (GateBoy.cpp:1181)
                                        [nand3] MOCE_BFETCH_DONEn  (GateBoy.cpp:1195)
                                          [nand2] LEBO_ODD  (GateBoy.cpp:1185)
                                            [REGISTERED] LAXU_BFETCH_S0p_odd @ODD  (GateBoy.cpp:1188)
```
