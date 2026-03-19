# GateBoy PPU Dependency Graph -- Statistics

| Metric | Value |
|--------|-------|
| Total nodes | 3141 |
| Total edges | 5573 |
| Registered nodes | 928 |
| Combinatorial nodes | 2213 |
| Connected components | 109 |
| Has cycles | True |
| Cycle-breaking edges removed | 70 |

## Node Type Breakdown

| Type | Count |
|------|-------|
| boundary | 35 |
| bus | 63 |
| combinatorial | 2213 |
| registered | 830 |

## Cycle-Breaking Edges

These edges were removed to create a DAG for path analysis.
They represent feedback loops (typically through async set/reset of DFFs).

- `TOKU_VD7_TO_CD7_new` -> `BUS_CPU_D07p`
- `YTUX_OLA_TO_CBD7_new` -> `BUS_CPU_D07p`
- `FYRA_OLB_TO_CBD7_new` -> `BUS_CPU_D07p`
- `PUSO_TIMA7_TO_CD7_new` -> `BUS_CPU_D07p`
- `RUPY_VD6_TO_CD6_new` -> `BUS_CPU_D06p`
- `XABU_OLA_TO_CBD6_new` -> `BUS_CPU_D06p`
- `ZEHA_OLB_TO_CBD6_new` -> `BUS_CPU_D06p`
- `ROWU_TIMA6_TO_CD6_new` -> `BUS_CPU_D06p`
- `REXU_VD5_TO_CD5_new` -> `BUS_CPU_D05p`
- `YWEG_OLA_TO_CBD5_new` -> `BUS_CPU_D05p`
- `DEVE_OLB_TO_CBD5_new` -> `BUS_CPU_D05p`
- `SURO_TIMA5_TO_CD5_new` -> `BUS_CPU_D05p`
- `PEGY_IF4_TO_CD4_new` -> `BUS_CPU_D04p`
- `TYJA_VD4_TO_CD4_new` -> `BUS_CPU_D04p`
- `ZYSA_OLA_TO_CBD4_new` -> `BUS_CPU_D04p`
- `XUNA_OLB_TO_CBD4_new` -> `BUS_CPU_D04p`
- `SOMU_TIMA4_TO_CD4_new` -> `BUS_CPU_D04p`
- `PADO_IF3_TO_CD3_new` -> `BUS_CPU_D03p`
- `RAJU_VD3_TO_CD3_new` -> `BUS_CPU_D03p`
- `XUVO_OLA_TO_CBD3_new` -> `BUS_CPU_D03p`
- `XYGU_OLB_TO_CBD3_new` -> `BUS_CPU_D03p`
- `SOSY_TIMA3_TO_CD3_new` -> `BUS_CPU_D03p`
- `ROVA_IF2_TO_CD2_new` -> `BUS_CPU_D02p`
- `RYBU_VD2_TO_CD2_new` -> `BUS_CPU_D02p`
- `YPON_OLA_TO_CBD2_new` -> `BUS_CPU_D02p`
- `XEPU_OLB_TO_CBD2_new` -> `BUS_CPU_D02p`
- `RAVY_TIMA2_TO_CD2_new` -> `BUS_CPU_D02p`
- `NABO_IF1_TO_CD1_new` -> `BUS_CPU_D01p`
- `ROTA_VD1_TO_CD1_new` -> `BUS_CPU_D01p`
- `XELE_OLA_TO_CBD1_new` -> `BUS_CPU_D01p`
- `XAGU_OLB_TO_CBD1_new` -> `BUS_CPU_D01p`
- `RACY_TIMA1_TO_CD1_new` -> `BUS_CPU_D01p`
- `NELA_IF0_TO_CD0_new` -> `BUS_CPU_D00p`
- `RUGA_VD0_TO_CD0_new` -> `BUS_CPU_D00p`
- `YFAP_OLA_TO_CBD0_new` -> `BUS_CPU_D00p`
- `XACA_OLB_TO_CBD0_new` -> `BUS_CPU_D00p`
- `SOKU_TIMA0_TO_CD0_new` -> `BUS_CPU_D00p`
- `PUKU_WIN_HITn_odd` -> `RYDY_WIN_HITp`
- `LAXU_BFETCH_S0p_odd` -> `MOCE_BFETCH_DONEn`
- `NYVA_BFETCH_S2p_odd` -> `MOCE_BFETCH_DONEn`
- `PABE_SPR_PIX_SET0_new` -> `NURO_SPR_PIPE_A0`
- `PYZU_SPR_PIX_RST0_new` -> `NURO_SPR_PIPE_A0`
- `NYLU_SPR_PIPE_B0` -> `MEFU_SPRITE_MASK0n_new`
- `MYTO_SPR_PIX_SET1_new` -> `MASO_SPR_PIPE_A1`
- `MADA_SPR_PIX_RST1_new` -> `MASO_SPR_PIPE_A1`
- `PEFU_SPR_PIPE_B1` -> `MEVE_SPRITE_MASK1n_new`
- `LELA_SPR_PIX_SET2_new` -> `LEFE_SPR_PIPE_A2`
- `LYDE_SPR_PIX_RST2_new` -> `LEFE_SPR_PIPE_A2`
- `NATY_SPR_PIPE_B2` -> `MYZO_SPRITE_MASK2n_new`
- `MAME_SPR_PIX_SET3_new` -> `LESU_SPR_PIPE_A3`
- `LUFY_SPR_PIX_RST3_new` -> `LESU_SPR_PIPE_A3`
- `PYJO_SPR_PIPE_B3` -> `RUDA_SPRITE_MASK3n_new`
- `VEXU_SPR_PIX_SET4_new` -> `WYHO_SPR_PIPE_A4`
- `XATO_SPR_PIX_RST4_new` -> `WYHO_SPR_PIPE_A4`
- `VARE_SPR_PIPE_B4` -> `VOTO_SPRITE_MASK4n_new`
- `VABY_SPR_PIX_SET5_new` -> `WORA_SPR_PIPE_A5`
- `XEXU_SPR_PIX_RST5_new` -> `WORA_SPR_PIPE_A5`
- `WEBA_SPR_PIPE_B5` -> `VYSA_SPRITE_MASK5n_new`
- `TUXA_SPR_PIX_SET6_new` -> `VAFO_SPR_PIPE_A6`
- `TUPE_SPR_PIX_RST6_new` -> `VAFO_SPR_PIPE_A6`
- `VANU_SPR_PIPE_B6` -> `TORY_SPRITE_MASK6n_new`
- `VUNE_SPR_PIX_SET7_new` -> `WUFY_SPR_PIPE_A7`
- `XYVE_SPR_PIX_RST7_new` -> `WUFY_SPR_PIPE_A7`
- `VUPY_SPR_PIPE_B7` -> `WOPE_SPRITE_MASK7n_new`
- `POME_X8_LATCH` -> `RUJU`
- `BAKY_SPRITES_FULL_new` -> `CAKE_COUNT_CLKp_new`
- `GAVA_SCAN_CLOCKp_odd` -> `YFEL_SCAN0_odd`
- `TOMA_SFETCH_evn` -> `TOXE_SFETCH_S0p_evn`
- `LOKY_DMA_LATCHp_odd` -> `LARA_DMA_LATCHn_odd`
- `ANOS_xBxDxFxH` -> `AVET_AxCxExGx`
