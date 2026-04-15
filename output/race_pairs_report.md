# Signal Race Pair Analysis

Total race pairs identified: 1063

Race pairs are registered nodes where data inputs arrive at significantly
different combinatorial depths (diff >= 3 gates, max >= 4). On real hardware,
the late-arriving signal may not settle before the register samples, causing
behavior to differ from behavioral emulation by one dot.

PPU-related races: 510


## APU CH1 (Square+Sweep) (106 races)

### `hyka` (dffsr) — diff=113.52, max=122.1
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `efor` | 77.61 | nor2 | apu-ch1 |
| `gylu` | 64.74 | nand2 | apu-ch1 |
| `guxa` | 8.58 | full_add | apu-ch1 |

### `cyto` (nor_latch) — diff=110.51, max=110.51
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bery` | 110.51 | or4 | apu-ch1 |
| `feku` | 0.0 | dffr | apu-ch1 |

### `jyka` (dffsr) — diff=103.45, max=122.1
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `gato` | 66.34 | nor2 | apu-ch1 |
| `geta` | 63.82 | nand2 | apu-ch1 |
| `halu` | 18.65 | full_add | apu-ch1 |

### `havo` (dffsr) — diff=98.89, max=122.1
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `gyfu` | 66.01 | nor2 | apu-ch1 |
| `golo` | 63.94 | nand2 | apu-ch1 |
| `jule` | 23.21 | full_add | apu-ch1 |

### `edul` (dffsr) — diff=90.87, max=122.1
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `gamo` | 66.59 | nor2 | apu-ch1 |
| `gope` | 64.11 | nand2 | apu-ch1 |
| `jory` | 31.23 | full_add | apu-ch1 |

### `fely` (dffsr) — diff=85.35, max=122.1
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `kapo` | 74.14 | nor2 | apu-ch1 |
| `kovu` | 65.36 | nand2 | apu-ch1 |
| `hexo` | 36.75 | full_add | apu-ch1 |

### `holu` (dffsr) — diff=80.74, max=122.1
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `kaju` | 70.21 | nor2 | apu-ch1 |
| `kypa` | 64.76 | nand2 | apu-ch1 |
| `geva` | 41.36 | full_add | apu-ch1 |

### `adek` (drlatch_ee) — diff=70.48, max=70.48
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 70.48 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 29.99 | not_x1 | apu-control |
| `bus:d4` | 0.0 |  | bus |

### `anaz` (drlatch_ee) — diff=70.48, max=70.48
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 70.48 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 29.99 | not_x1 | apu-control |
| `bus:d2` | 0.0 |  | bus |

### `arax` (drlatch_ee) — diff=70.48, max=70.48
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 70.48 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 29.99 | not_x1 | apu-control |
| `bus:d1` | 0.0 |  | bus |

### `avaf` (drlatch_ee) — diff=70.48, max=70.48
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 70.48 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 29.99 | not_x1 | apu-control |
| `bus:d3` | 0.0 |  | bus |

### `bana` (drlatch_ee) — diff=70.48, max=70.48
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 70.48 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 29.99 | not_x1 | apu-control |
| `bus:d5` | 0.0 |  | bus |

### `bany` (drlatch_ee) — diff=70.48, max=70.48
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 70.48 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 29.99 | not_x1 | apu-control |
| `bus:d0` | 0.0 |  | bus |

### `botu` (drlatch_ee) — diff=70.48, max=70.48
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 70.48 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 29.99 | not_x1 | apu-control |
| `bus:d6` | 0.0 |  | bus |

### `gexu` (nand_latch) — diff=68.56, max=68.8
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `femy` | 68.8 | nor2 | apu-ch1 |
| `gepu` | 0.24 | not_x1 | apu-ch1 |


## Bus (79 races)

### `bus:d0` () — diff=103.08, max=103.08
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buzu` | 103.08 | not_if0 | apu-control |
| `atel` | 101.75 | not_if0 | apu-ch4 |
| `juvy` | 101.68 | not_if0 | apu-ch3 |
| `akod` | 99.22 | not_if0 | apu-control |
| `huna` | 98.97 | not_if0 | apu-ch2 |
| `xary` | 96.25 | not_if0 | ppu-pal |
| `amyd` | 96.23 | not_if0 | apu-ch1 |
| `demy` | 93.11 | not_if0 | apu-ch4 |
| `kamo` | 92.26 | not_if0 | apu-ch4 |
| `coto` | 90.7 | not_if0 | apu-control |
| `jyne` | 90.27 | not_if0 | apu-ch1 |
| `fava` | 88.87 | not_if0 | apu-ch2 |
| `cugy` | 88.43 | not_if1 | serial |
| `jofo` | 88.27 | not_if0 | apu-ch3 |
| `foru` | 88.08 | not_if0 | apu-ch1 |
| `huvu` | 87.89 | not_if0 | apu-ch2 |
| `dopa` | 87.81 | not_if0 | apu-ch1 |
| `poly` | 87.68 | not_if1 | ppu-dma |
| `raro` | 87.57 | not_if0 | ppu-pal |
| `fapy` | 86.46 | not_if0 | apu-ch3 |
| `kema` | 86.12 | not_if0 | joypad |
| `punu` | 84.34 | not_if0 | ppu-window |
| `ware` | 83.27 | not_if0 | ppu-bgscroll |
| `vega` | 82.82 | not_if0 | ppu-stat |
| `core` | 82.28 | not_if1 | serial |
| `lova` | 82.11 | not_if0 | ppu-window |
| `sete` | 82.02 | not_if1 | timer |
| `edos` | 81.27 | not_if0 | ppu-bgscroll |
| `laju` | 80.9 | not_if0 | ppu-pal |
| `nela` | 80.9 | not_if1 | int |
| `tawu` | 80.79 | not_if1 | clocks |
| `soku` | 80.72 | not_if1 | timer |
| `retu` | 80.69 | not_if0 | ppu-stat |
| `wypo` | 79.86 | not_if0 | ppu-control |
| `teby` | 79.2 | not_if1 | ppu-stat |
| `dugu` | 78.61 | not_if1 | apu-ch3 |
| `ryla` | 77.41 | not_if1 | timer |
| `ruga` | 71.77 | not_if1 | ppu-vram |
| `sypu` | 69.93 | not_if1 | bootrom |
| `xaca` | 69.05 | buf_if0 | ppu-xcomp |
| `yfap` | 67.19 | buf_if0 | ppu-ycomp |
| `ryma` | 65.5 | not_if0 | bus-data |
| `tuty` | 64.23 | buf_if0 | bus-data |
| `romy` | 49.69 | not_if1 | bus-data |
| `anoc` | 36.34 | not_if0 |  |
| `tovu` | 26.8 | buf_if0 | bus-data |
| `boot_rom` | 0.0 | boot_rom |  |
| `cpu` | 0.0 | sm83 |  |
| `high_ram` | 0.0 | high_ram |  |

### `bus:d1` () — diff=103.08, max=103.08
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `capu` | 103.08 | not_if0 | apu-control |
| `jura` | 101.68 | not_if0 | apu-ch3 |
| `awed` | 99.22 | not_if0 | apu-control |
| `jaro` | 98.97 | not_if0 | apu-ch2 |
| `xoke` | 96.25 | not_if0 | ppu-pal |
| `atax` | 96.23 | not_if0 | apu-ch1 |
| `coce` | 93.11 | not_if0 | apu-ch4 |
| `kaku` | 92.26 | not_if0 | apu-ch4 |
| `efus` | 91.01 | not_if0 | apu-control |
| `jaca` | 90.27 | not_if0 | apu-ch1 |
| `fajy` | 88.87 | not_if0 | apu-ch2 |
| `dude` | 88.43 | not_if1 | serial |
| `kafu` | 88.27 | not_if0 | apu-ch3 |
| `gefu` | 88.08 | not_if0 | apu-ch1 |
| `hyre` | 87.89 | not_if0 | apu-ch2 |
| `demu` | 87.81 | not_if0 | apu-ch1 |
| `rofo` | 87.68 | not_if1 | ppu-dma |
| `paba` | 87.57 | not_if0 | ppu-pal |
| `faro` | 86.46 | not_if0 | apu-ch3 |
| `kuro` | 86.12 | not_if0 | joypad |
| `poda` | 84.34 | not_if0 | ppu-window |
| `goba` | 83.27 | not_if0 | ppu-bgscroll |
| `wuva` | 82.82 | not_if0 | ppu-stat |
| `muka` | 82.11 | not_if0 | ppu-window |
| `pyre` | 82.02 | not_if1 | timer |
| `ekob` | 81.27 | not_if0 | ppu-bgscroll |
| `lepa` | 80.9 | not_if0 | ppu-pal |
| `nabo` | 80.9 | not_if1 | int |
| `taku` | 80.79 | not_if1 | clocks |
| `racy` | 80.72 | not_if1 | timer |
| `vojo` | 80.69 | not_if0 | ppu-stat |
| `xero` | 79.86 | not_if0 | ppu-control |
| `wuga` | 79.2 | not_if1 | ppu-stat |
| `desy` | 78.61 | not_if1 | apu-ch3 |
| `rote` | 77.41 | not_if1 | timer |
| `rota` | 71.77 | not_if1 | ppu-vram |
| `xagu` | 69.05 | buf_if0 | ppu-xcomp |
| `xele` | 67.19 | buf_if0 | ppu-ycomp |
| `ruvo` | 65.5 | not_if0 | bus-data |
| `sywa` | 64.23 | buf_if0 | bus-data |
| `ryne` | 49.69 | not_if1 | bus-data |
| `ataj` | 36.34 | not_if0 |  |
| `sosa` | 26.8 | buf_if0 | bus-data |
| `boot_rom` | 0.0 | boot_rom |  |
| `cpu` | 0.0 | sm83 |  |
| `high_ram` | 0.0 | high_ram |  |

### `bus:d2` () — diff=103.08, max=103.08
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caga` | 103.08 | not_if0 | apu-control |
| `hufo` | 101.68 | not_if0 | apu-ch3 |
| `avud` | 99.22 | not_if0 | apu-control |
| `jeke` | 98.97 | not_if0 | apu-ch2 |
| `xuno` | 96.25 | not_if0 | ppu-pal |
| `azyp` | 96.23 | not_if0 | apu-ch1 |
| `cuzu` | 93.11 | not_if0 | apu-ch4 |
| `kyro` | 92.26 | not_if0 | apu-ch4 |
| `fate` | 91.17 | not_if0 | apu-control |
| `joku` | 90.27 | not_if0 | apu-ch1 |
| `fegu` | 88.87 | not_if0 | apu-ch2 |
| `detu` | 88.43 | not_if1 | serial |
| `kesy` | 88.27 | not_if0 | apu-ch3 |
| `kyvu` | 88.08 | not_if0 | apu-ch1 |
| `havu` | 87.89 | not_if0 | apu-ch2 |
| `dexo` | 87.81 | not_if0 | apu-ch1 |
| `rema` | 87.68 | not_if1 | ppu-dma |
| `redo` | 87.57 | not_if0 | ppu-pal |
| `fote` | 86.46 | not_if0 | apu-ch3 |
| `kuve` | 86.12 | not_if0 | joypad |
| `pygu` | 84.34 | not_if0 | ppu-window |
| `gonu` | 83.27 | not_if0 | ppu-bgscroll |
| `lyco` | 82.82 | not_if0 | ppu-stat |
| `moko` | 82.11 | not_if0 | ppu-window |
| `nola` | 82.02 | not_if1 | timer |
| `cuga` | 81.27 | not_if0 | ppu-bgscroll |
| `lode` | 80.9 | not_if0 | ppu-pal |
| `rova` | 80.9 | not_if1 | int |
| `temu` | 80.79 | not_if1 | clocks |
| `ravy` | 80.72 | not_if1 | timer |
| `razu` | 80.69 | not_if0 | ppu-stat |
| `wyju` | 79.86 | not_if0 | ppu-decode |
| `sego` | 79.2 | not_if1 | ppu-stat |
| `baty` | 78.61 | not_if1 | apu-ch3 |
| `supe` | 77.41 | not_if1 | timer |
| `rybu` | 71.77 | not_if1 | ppu-vram |
| `xepu` | 69.05 | buf_if0 | ppu-xcomp |
| `ypon` | 67.19 | buf_if0 | ppu-ycomp |
| `ryko` | 65.5 | not_if0 | bus-data |
| `sugu` | 64.23 | buf_if0 | bus-data |
| `rejy` | 49.69 | not_if1 | bus-data |
| `ajec` | 36.34 | not_if0 |  |
| `sedu` | 26.8 | buf_if0 | bus-data |
| `boot_rom` | 0.0 | boot_rom |  |
| `cpu` | 0.0 | sm83 |  |
| `high_ram` | 0.0 | high_ram |  |

### `bus:d3` () — diff=103.08, max=103.08
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boca` | 103.08 | not_if0 | apu-control |
| `gome` | 99.54 | not_if0 | apu-ch4 |
| `axem` | 99.22 | not_if0 | apu-control |
| `xuby` | 96.25 | not_if0 | ppu-pal |
| `afox` | 96.23 | not_if0 | apu-ch1 |
| `hono` | 91.76 | not_if0 | apu-ch1 |
| `koge` | 90.88 | not_if0 | apu-control |
| `keta` | 90.71 | not_if0 | apu-ch4 |
| `fose` | 88.87 | not_if0 | apu-ch2 |
| `daso` | 88.43 | not_if1 | serial |
| `jude` | 88.27 | not_if0 | apu-ch3 |
| `kumo` | 88.08 | not_if0 | apu-ch1 |
| `pane` | 87.68 | not_if1 | ppu-dma |
| `lobe` | 87.57 | not_if0 | ppu-pal |
| `gene` | 87.0 | not_if0 | apu-ch2 |
| `fana` | 86.46 | not_if0 | apu-ch3 |
| `jeku` | 86.12 | not_if0 | joypad |
| `loka` | 84.34 | not_if0 | ppu-window |
| `godo` | 83.27 | not_if0 | ppu-bgscroll |
| `wojy` | 82.82 | not_if0 | ppu-stat |
| `puzo` | 82.39 | not_if0 | ppu-stat |
| `lole` | 82.11 | not_if0 | ppu-window |
| `salu` | 82.02 | not_if1 | timer |
| `wony` | 81.27 | not_if0 | ppu-bgscroll |
| `lyza` | 80.9 | not_if0 | ppu-pal |
| `pado` | 80.9 | not_if1 | int |
| `tuse` | 80.79 | not_if1 | clocks |
| `sosy` | 80.72 | not_if1 | timer |
| `redy` | 80.69 | not_if0 | ppu-stat |
| `wuka` | 79.86 | not_if0 | ppu-control |
| `bade` | 78.61 | not_if1 | apu-ch3 |
| `raju` | 71.77 | not_if1 | ppu-vram |
| `xygu` | 69.05 | buf_if0 | ppu-xcomp |
| `xuvo` | 67.19 | buf_if0 | ppu-ycomp |
| `tavo` | 65.5 | not_if0 | bus-data |
| `tawo` | 64.23 | buf_if0 | bus-data |
| `rase` | 49.69 | not_if1 | bus-data |
| `asuz` | 36.34 | not_if0 |  |
| `taxo` | 26.8 | buf_if0 | bus-data |
| `boot_rom` | 0.0 | boot_rom |  |
| `cpu` | 0.0 | sm83 |  |
| `high_ram` | 0.0 | high_ram |  |

### `bus:d4` () — diff=103.08, max=103.08
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cavu` | 103.08 | not_if0 | apu-control |
| `heda` | 99.54 | not_if0 | apu-ch4 |
| `amad` | 99.22 | not_if0 | apu-control |
| `xaju` | 96.25 | not_if0 | ppu-pal |
| `avek` | 96.23 | not_if0 | apu-ch1 |
| `geda` | 93.91 | not_if0 | apu-ch4 |
| `howu` | 91.76 | not_if0 | apu-ch1 |
| `gero` | 88.87 | not_if0 | apu-ch2 |
| `dame` | 88.43 | not_if1 | serial |
| `juke` | 88.27 | not_if0 | apu-ch3 |
| `kary` | 88.08 | not_if0 | apu-ch1 |
| `pare` | 87.68 | not_if1 | ppu-dma |
| `lace` | 87.57 | not_if0 | ppu-pal |
| `hupe` | 87.0 | not_if0 | apu-ch2 |
| `fera` | 86.46 | not_if0 | apu-ch3 |
| `koce` | 86.12 | not_if0 | joypad |
| `mega` | 84.34 | not_if0 | ppu-window |
| `cusa` | 83.27 | not_if0 | ppu-bgscroll |
| `vyne` | 82.82 | not_if0 | ppu-stat |
| `pofo` | 82.39 | not_if0 | ppu-stat |
| `mele` | 82.11 | not_if0 | ppu-window |
| `supo` | 82.02 | not_if1 | timer |
| `cedu` | 81.27 | not_if0 | ppu-bgscroll |
| `luky` | 80.9 | not_if0 | ppu-pal |
| `pegy` | 80.9 | not_if1 | int |
| `upug` | 80.79 | not_if1 | clocks |
| `somu` | 80.72 | not_if1 | timer |
| `race` | 80.69 | not_if0 | ppu-stat |
| `voke` | 79.86 | not_if0 | ppu-control |
| `bune` | 78.61 | not_if1 | apu-ch3 |
| `tyja` | 71.77 | not_if1 | ppu-vram |
| `xuna` | 69.05 | buf_if0 | ppu-xcomp |
| `zysa` | 67.19 | buf_if0 | ppu-ycomp |
| `tepe` | 65.5 | not_if0 | bus-data |
| `tute` | 64.23 | buf_if0 | bus-data |
| `reka` | 49.69 | not_if1 | bus-data |
| `benu` | 36.34 | not_if0 |  |
| `tahy` | 26.8 | buf_if0 | bus-data |
| `boot_rom` | 0.0 | boot_rom |  |
| `cpu` | 0.0 | sm83 |  |
| `high_ram` | 0.0 | high_ram |  |

### `bus:d5` () — diff=103.08, max=103.08
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cudu` | 103.08 | not_if0 | apu-control |
| `godu` | 99.54 | not_if0 | apu-ch4 |
| `arux` | 99.22 | not_if0 | apu-control |
| `xobo` | 96.25 | not_if0 | ppu-pal |
| `akux` | 96.23 | not_if0 | apu-ch1 |
| `gype` | 93.91 | not_if0 | apu-ch4 |
| `hewa` | 91.76 | not_if0 | apu-ch1 |
| `gaky` | 88.87 | not_if0 | apu-ch2 |
| `evok` | 88.43 | not_if1 | serial |
| `jeza` | 88.27 | not_if0 | apu-ch3 |
| `gode` | 88.08 | not_if0 | apu-ch1 |
| `raly` | 87.68 | not_if1 | ppu-dma |
| `lyka` | 87.57 | not_if0 | ppu-pal |
| `here` | 87.0 | not_if0 | apu-ch2 |
| `cudy` | 86.12 | not_if0 | joypad |
| `pela` | 84.34 | not_if0 | ppu-window |
| `gyzo` | 83.27 | not_if0 | ppu-bgscroll |
| `wama` | 82.82 | not_if0 | ppu-stat |
| `sasy` | 82.39 | not_if0 | ppu-stat |
| `mufe` | 82.11 | not_if0 | ppu-window |
| `sotu` | 82.02 | not_if1 | timer |
| `cata` | 81.27 | not_if0 | ppu-bgscroll |
| `luga` | 80.9 | not_if0 | ppu-pal |
| `sepu` | 80.79 | not_if1 | clocks |
| `suro` | 80.72 | not_if1 | timer |
| `vazu` | 80.69 | not_if0 | ppu-stat |
| `hamu` | 80.38 | not_if0 | apu-ch3 |
| `vato` | 79.86 | not_if0 | ppu-control |
| `bava` | 78.61 | not_if1 | apu-ch3 |
| `rexu` | 71.77 | not_if1 | ppu-vram |
| `deve` | 69.05 | buf_if0 | ppu-xcomp |
| `yweg` | 67.19 | buf_if0 | ppu-ycomp |
| `safo` | 65.5 | not_if0 | bus-data |
| `sajo` | 64.23 | buf_if0 | bus-data |
| `rowe` | 49.69 | not_if1 | bus-data |
| `akaj` | 36.34 | not_if0 |  |
| `tesu` | 26.8 | buf_if0 | bus-data |
| `boot_rom` | 0.0 | boot_rom |  |
| `cpu` | 0.0 | sm83 |  |
| `high_ram` | 0.0 | high_ram |  |

### `bus:d6` () — diff=103.08, max=103.08
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cada` | 103.08 | not_if0 | apu-control |
| `cury` | 103.03 | not_if0 | apu-ch4 |
| `hoge` | 99.54 | not_if0 | apu-ch4 |
| `bocy` | 99.22 | not_if0 | apu-control |
| `xaxa` | 96.25 | not_if0 | ppu-pal |
| `awos` | 96.23 | not_if0 | apu-ch1 |
| `haca` | 95.38 | not_if0 | apu-ch3 |
| `gojy` | 94.8 | not_if0 | apu-ch2 |
| `gaka` | 93.91 | not_if0 | apu-ch4 |
| `heve` | 91.76 | not_if0 | apu-ch1 |
| `gadu` | 88.87 | not_if0 | apu-ch2 |
| `efab` | 88.43 | not_if1 | serial |
| `kora` | 88.27 | not_if0 | apu-ch3 |
| `goje` | 88.08 | not_if0 | apu-ch1 |
| `resu` | 87.68 | not_if1 | ppu-dma |
| `lody` | 87.57 | not_if0 | ppu-pal |
| `horo` | 87.0 | not_if0 | apu-ch2 |
| `bytu` | 85.97 | not_if0 | apu-ch1 |
| `polo` | 84.34 | not_if0 | ppu-window |
| `gune` | 83.27 | not_if0 | ppu-bgscroll |
| `wavo` | 82.82 | not_if0 | ppu-stat |
| `bowo` | 82.67 | not_if0 | apu-ch1 |
| `pote` | 82.39 | not_if0 | ppu-stat |
| `cecy` | 82.26 | not_if0 | apu-ch2 |
| `muly` | 82.11 | not_if0 | ppu-window |
| `reva` | 82.02 | not_if1 | timer |
| `doxe` | 81.27 | not_if0 | ppu-bgscroll |
| `leba` | 80.9 | not_if0 | ppu-pal |
| `sawa` | 80.79 | not_if1 | clocks |
| `rowu` | 80.72 | not_if1 | timer |
| `vafe` | 80.69 | not_if0 | ppu-stat |
| `huco` | 80.38 | not_if0 | apu-ch3 |
| `vaha` | 79.86 | not_if0 | ppu-control |
| `desa` | 78.61 | not_if1 | apu-ch3 |
| `rupy` | 71.77 | not_if1 | ppu-vram |
| `zeha` | 69.05 | buf_if0 | ppu-xcomp |
| `xabu` | 67.19 | buf_if0 | ppu-ycomp |
| `sevu` | 65.5 | not_if0 | bus-data |
| `temy` | 64.23 | buf_if0 | bus-data |
| `ryke` | 49.69 | not_if1 | bus-data |
| `arar` | 36.34 | not_if0 |  |
| `tazu` | 26.8 | buf_if0 | bus-data |
| `boot_rom` | 0.0 | boot_rom |  |
| `cpu` | 0.0 | sm83 |  |
| `high_ram` | 0.0 | high_ram |  |

### `bus:d7` () — diff=103.08, max=103.08
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cere` | 103.08 | not_if0 | apu-control |
| `hacu` | 99.54 | not_if0 | apu-ch4 |
| `atum` | 99.22 | not_if0 | apu-control |
| `xawo` | 96.25 | not_if0 | ppu-pal |
| `hapy` | 93.91 | not_if0 | apu-ch4 |
| `jyse` | 91.76 | not_if0 | apu-ch1 |
| `hope` | 91.01 | not_if0 | apu-control |
| `gazo` | 88.87 | not_if0 | apu-ch2 |
| `etak` | 88.43 | not_if1 | serial |
| `kamy` | 88.27 | not_if0 | apu-ch3 |
| `foze` | 88.08 | not_if0 | apu-ch1 |
| `nuvy` | 87.68 | not_if1 | ppu-dma |
| `lary` | 87.57 | not_if0 | ppu-pal |
| `hyry` | 87.0 | not_if0 | apu-ch2 |
| `mera` | 84.34 | not_if0 | ppu-window |
| `geko` | 83.81 | not_if0 | apu-ch3 |
| `gyza` | 83.27 | not_if0 | ppu-bgscroll |
| `weze` | 82.82 | not_if0 | ppu-stat |
| `cuda` | 82.67 | not_if0 | apu-ch1 |
| `eluv` | 82.28 | not_if1 | serial |
| `ceka` | 82.26 | not_if0 | apu-ch2 |
| `mara` | 82.11 | not_if0 | ppu-window |
| `sapu` | 82.02 | not_if1 | timer |
| `casy` | 81.27 | not_if0 | ppu-bgscroll |
| `lelu` | 80.9 | not_if0 | ppu-pal |
| `tatu` | 80.79 | not_if1 | clocks |
| `puso` | 80.72 | not_if1 | timer |
| `pufy` | 80.69 | not_if0 | ppu-stat |
| `xebu` | 79.86 | not_if0 | ppu-control |
| `bezu` | 78.61 | not_if1 | apu-ch3 |
| `toku` | 71.77 | not_if1 | ppu-vram |
| `fyra` | 69.05 | buf_if0 | ppu-xcomp |
| `ytux` | 67.19 | buf_if0 | ppu-ycomp |
| `taju` | 65.5 | not_if0 | bus-data |
| `ropa` | 64.23 | buf_if0 | bus-data |
| `raru` | 49.69 | not_if1 | bus-data |
| `beda` | 36.34 | not_if0 |  |
| `tewa` | 26.8 | buf_if0 | bus-data |
| `boot_rom` | 0.0 | boot_rom |  |
| `cpu` | 0.0 | sm83 |  |
| `high_ram` | 0.0 | high_ram |  |

### `bus:~oam_a_d3` () — diff=91.53, max=91.53
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zozo` | 91.53 | not_if0 | ppu-oam |
| `cetu` | 54.47 | not_if0 | ppu-oam |
| `cyme` | 53.11 | not_if0 | ppu-dma |
| `oam_a` | 0.0 | oam |  |

### `bus:~oam_a_d4` () — diff=91.53, max=91.53
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zufo` | 91.53 | not_if0 | ppu-oam |
| `aryn` | 54.47 | not_if0 | ppu-oam |
| `baxu` | 53.11 | not_if0 | ppu-dma |
| `oam_a` | 0.0 | oam |  |

### `bus:~oam_a_d5` () — diff=91.53, max=91.53
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zato` | 91.53 | not_if0 | ppu-oam |
| `acot` | 54.47 | not_if0 | ppu-oam |
| `bupy` | 53.11 | not_if0 | ppu-dma |
| `oam_a` | 0.0 | oam |  |

### `bus:~oam_a_d6` () — diff=91.53, max=91.53
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `yvuc` | 91.53 | not_if0 | ppu-oam |
| `cuje` | 54.47 | not_if0 | ppu-oam |
| `byny` | 53.11 | not_if0 | ppu-dma |
| `oam_a` | 0.0 | oam |  |

### `bus:~oam_a_d7` () — diff=91.53, max=91.53
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zufe` | 91.53 | not_if0 | ppu-oam |
| `ater` | 54.47 | not_if0 | ppu-oam |
| `bypy` | 53.11 | not_if0 | ppu-dma |
| `oam_a` | 0.0 | oam |  |

### `bus:~oam_b_d0` () — diff=91.53, max=91.53
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zamy` | 91.53 | not_if0 | ppu-oam |
| `wowa` | 54.47 | not_if0 | ppu-oam |
| `wejo` | 53.11 | not_if0 | ppu-dma |
| `oam_b` | 0.0 | oam |  |

### `bus:~oam_b_d1` () — diff=91.53, max=91.53
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zopu` | 91.53 | not_if0 | ppu-oam |
| `aveb` | 54.47 | not_if0 | ppu-oam |
| `bomo` | 53.11 | not_if0 | ppu-dma |
| `oam_b` | 0.0 | oam |  |


## BG Pixel Shifter (32 races)

### `taca` (dffsr) — diff=98.77, max=98.77
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `soly` | 98.77 | nand2 | ppu-bgfifo |
| `seno` | 97.67 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `tomy` | 0.0 | dffsr | ppu-bgfifo |

### `sohu` (dffsr) — diff=98.65, max=98.65
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `raga` | 98.65 | nand2 | ppu-bgfifo |
| `ryjy` | 97.9 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `ralu` | 0.0 | dffsr | ppu-bgfifo |

### `rysa` (dffsr) — diff=98.43, max=98.43
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryja` | 98.43 | nand2 | ppu-bgfifo |
| `sebo` | 98.31 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `sady` | 0.0 | dffsr | ppu-bgfifo |

### `setu` (dffsr) — diff=98.4, max=98.4
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `raja` | 98.4 | nand2 | ppu-bgfifo |
| `sywe` | 97.91 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `sobo` | 0.0 | dffsr | ppu-bgfifo |

### `ralu` (dffsr) — diff=98.28, max=98.28
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rajo` | 98.28 | nand2 | ppu-bgfifo |
| `supu` | 97.88 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `setu` | 0.0 | dffsr | ppu-bgfifo |

### `sobo` (dffsr) — diff=98.17, max=98.17
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruto` | 98.17 | nand2 | ppu-bgfifo |
| `suca` | 98.16 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `rysa` | 0.0 | dffsr | ppu-bgfifo |

### `sady` (dffsr) — diff=98.12, max=98.12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruce` | 98.12 | nand2 | ppu-bgfifo |
| `sure` | 97.97 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `taca` | 0.0 | dffsr | ppu-bgfifo |

### `neda` (dffsr) — diff=97.64, max=97.64
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nute` | 97.64 | nand2 | ppu-bgfifo |
| `nyha` | 96.68 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `modu` | 0.0 | dffsr | ppu-bgfifo |

### `nozo` (dffsr) — diff=97.5, max=97.5
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxo` | 97.5 | nand2 | ppu-bgfifo |
| `nexa` | 96.98 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `myde` | 0.0 | dffsr | ppu-bgfifo |

### `macu` (dffsr) — diff=97.24, max=97.24
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lydu` | 97.24 | nand2 | ppu-bgfifo |
| `luja` | 97.04 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `moju` | 0.0 | dffsr | ppu-bgfifo |

### `modu` (dffsr) — diff=97.24, max=97.24
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lodo` | 97.24 | nand2 | ppu-bgfifo |
| `leru` | 97.16 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `nepo` | 0.0 | dffsr | ppu-bgfifo |

### `nepo` (dffsr) — diff=97.22, max=97.22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myvy` | 97.22 | nand2 | ppu-bgfifo |
| `mosy` | 97.12 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `macu` | 0.0 | dffsr | ppu-bgfifo |

### `moju` (dffsr) — diff=97.11, max=97.11
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `loto` | 97.11 | nand2 | ppu-bgfifo |
| `lutu` | 96.96 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `nozo` | 0.0 | dffsr | ppu-bgfifo |

### `pybo` (dffsr) — diff=97.11, max=97.11
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `naja` | 97.11 | nand2 | ppu-bgfifo |
| `nady` | 97.0 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `neda` | 0.0 | dffsr | ppu-bgfifo |

### `tomy` (dffsr) — diff=34.64, max=98.41
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuxe` | 98.41 | nand2 | ppu-bgfifo |
| `seja` | 97.82 | nand2 | ppu-bgfifo |
| `sacu` | 63.77 | or2 | ppu-cycles |


## BG/Win Cycles (20 races)

### `nyka` (dffr) — diff=92.92, max=99.1
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyry` | 99.1 | not_x1 | ppu-cycles |
| `alet` | 16.28 | not_x2 | ppu-control |
| `nafy` | 6.18 | nor2 | ppu-cycles |

### `mesu` (dffr) — diff=92.9, max=92.9
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 92.9 | nor3 | ppu-cycles |
| `laxu` | 0.0 | dffr | ppu-cycles |

### `nyva` (dffr) — diff=92.9, max=92.9
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 92.9 | nor3 | ppu-cycles |
| `mesu` | 0.0 | dffr | ppu-cycles |

### `lony` (nand_latch) — diff=91.69, max=92.9
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 92.9 | nor3 | ppu-cycles |
| `lury` | 1.21 | and2 | ppu-cycles |

### `lovy` (dffr) — diff=76.94, max=99.1
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyry` | 99.1 | not_x1 | ppu-cycles |
| `nyxu` | 92.9 | nor3 | ppu-cycles |
| `myvo` | 22.16 | not_x1 | ppu-cycles |

### `pynu` (nor_latch) — diff=53.27, max=53.27
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xofo` | 53.27 | nand3 | ppu-cycles |
| `nunu` | 0.0 | dffr | ppu-cycles |

### `paho` (dffr) — diff=52.13, max=52.13
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roxo` | 52.13 | not_x1 | ppu-cycles |
| `xydo` | 0.0 | dffr | ppu-stat |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `puxa` (dffr) — diff=52.13, max=52.13
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roxo` | 52.13 | not_x1 | ppu-cycles |
| `pohu` | 3.5 | not_x1 | ppu-cycles |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `roga` (dffr) — diff=51.98, max=51.98
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 51.98 | nor2 | ppu-cycles |
| `ryku` | 0.0 | dffr | ppu-cycles |

### `rubu` (dffr) — diff=51.98, max=51.98
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 51.98 | nor2 | ppu-cycles |
| `roga` | 0.0 | dffr | ppu-cycles |

### `ryfa` (dffr) — diff=49.4, max=49.4
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `segu` | 49.4 | not_x4 | ppu-cycles |
| `pany` | 9.37 | nor2 | ppu-cycles |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `pyco` (dffr) — diff=44.35, max=49.95
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roco` | 49.95 | not_x1 | ppu-cycles |
| `xapo` | 29.35 | not_x2 | ppu-control |
| `nuko` | 5.6 | not_x1 | ppu-window |

### `nopa` (dffr) — diff=29.35, max=29.35
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xapo` | 29.35 | not_x2 | ppu-control |
| `alet` | 16.28 | not_x2 | ppu-control |
| `pynu` | 0.0 | nor_latch | ppu-cycles |

### `nunu` (dffr) — diff=29.35, max=29.35
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xapo` | 29.35 | not_x2 | ppu-control |
| `mehe` | 16.69 | not_x1 | ppu-cycles |
| `pyco` | 0.0 | dffr | ppu-cycles |

### `sovy` (dffr) — diff=22.38, max=38.66
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rydy` | 38.66 | nor3 | ppu-cycles |
| `xapo` | 29.35 | not_x2 | ppu-control |
| `alet` | 16.28 | not_x2 | ppu-control |


## Other (6 races)

### `oam_a` (oam) — diff=89.15, max=100.99
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wame` | 100.99 | not_x2 | ppu-oam |
| `wory` | 93.58 | not_x2 | ppu-oam |
| `wejy` | 89.24 | not_x2 | ppu-oam |
| `wahe` | 85.66 | not_x3 | ppu-oam |
| `wovu` | 69.97 | not_x2 | ppu-oam |
| `wafa` | 23.14 | and2 | ppu-oam |
| `wyxy` | 23.14 | and2 | ppu-oam |
| `wexe` | 22.6 | and2 | ppu-oam |
| `wadu` | 22.38 | not_x1 | ppu-oam |
| `wazu` | 21.91 | and2 | ppu-oam |
| `wuca` | 21.14 | not_x1 | ppu-oam |
| `woso` | 20.85 | not_x1 | ppu-oam |
| `wade` | 20.78 | not_x1 | ppu-oam |
| `wawy` | 20.17 | not_x1 | ppu-oam |
| `yfoc` | 14.09 | not_x1 | ppu-oam |
| `yzet` | 12.68 | not_x1 | ppu-oam |
| `ymev` | 12.47 | not_x1 | ppu-oam |
| `xemu` | 12.36 | not_x1 | ppu-oam |
| `yvom` | 11.84 | not_x1 | ppu-oam |

### `oam_b` (oam) — diff=89.15, max=100.99
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wame` | 100.99 | not_x2 | ppu-oam |
| `wory` | 93.58 | not_x2 | ppu-oam |
| `wexa` | 92.34 | not_x2 | ppu-oam |
| `wahe` | 85.66 | not_x3 | ppu-oam |
| `wovu` | 69.97 | not_x2 | ppu-oam |
| `wafa` | 23.14 | and2 | ppu-oam |
| `wyxy` | 23.14 | and2 | ppu-oam |
| `wexe` | 22.6 | and2 | ppu-oam |
| `wadu` | 22.38 | not_x1 | ppu-oam |
| `wazu` | 21.91 | and2 | ppu-oam |
| `wuca` | 21.14 | not_x1 | ppu-oam |
| `woso` | 20.85 | not_x1 | ppu-oam |
| `wade` | 20.78 | not_x1 | ppu-oam |
| `wawy` | 20.17 | not_x1 | ppu-oam |
| `yfoc` | 14.09 | not_x1 | ppu-oam |
| `yzet` | 12.68 | not_x1 | ppu-oam |
| `ymev` | 12.47 | not_x1 | ppu-oam |
| `xemu` | 12.36 | not_x1 | ppu-oam |
| `yvom` | 11.84 | not_x1 | ppu-oam |

### `wave_ram` (wave_ram) — diff=72.46, max=72.46
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ymul` | 72.46 | or2 | apu-ch3 |
| `yrar` | 67.14 | not_x1 | apu-ch3 |
| `ydez` | 54.86 | not_x1 | apu-ch3 |
| `ygef` | 20.79 | and2 | apu-ch3 |
| `yjej` | 20.55 | and2 | apu-ch3 |
| `yvop` | 20.53 | and2 | apu-ch3 |
| `yfux` | 20.29 | and2 | apu-ch3 |
| `yzeg` | 14.89 | not_x1 | apu-ch3 |
| `ynur` | 14.52 | not_x1 | apu-ch3 |
| `afum` | 14.15 | mux | apu-ch3 |
| `axol` | 13.78 | mux | apu-ch3 |
| `bus:d0` | 0.0 |  | bus |
| `bus:d1` | 0.0 |  | bus |
| `bus:d2` | 0.0 |  | bus |
| `bus:d3` | 0.0 |  | bus |
| `bus:d4` | 0.0 |  | bus |
| `bus:d5` | 0.0 |  | bus |
| `bus:d6` | 0.0 |  | bus |
| `bus:d7` | 0.0 |  | bus |

### `high_ram` (high_ram) — diff=59.14, max=59.14
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wuly` | 59.14 | not_x2 | hram |
| `abev` | 55.17 | not_x2 | hram |
| `anyk` | 52.33 | not_x1 | hram |
| `apow` | 49.26 | not_x2 | hram |
| `apuh` | 49.2 | not_x2 | hram |
| `wuta` | 43.38 | not_x2 | hram |
| `ajom` | 4.36 | and2 | hram |
| `avub` | 4.16 | and2 | hram |
| `axyc` | 4.05 | and2 | hram |
| `apul` | 3.48 | and2 | hram |
| `wady` | 3.43 | not_x1 | hram |
| `weju` | 3.42 | not_x1 | hram |
| `webe` | 3.4 | not_x1 | hram |
| `woce` | 3.4 | not_x1 | hram |
| `wehu` | 3.38 | not_x1 | hram |
| `bus:a2` | 0.0 |  | bus |
| `bus:a3` | 0.0 |  | bus |
| `bus:a4` | 0.0 |  | bus |
| `bus:a5` | 0.0 |  | bus |
| `bus:a6` | 0.0 |  | bus |

### `boot_rom` (boot_rom) — diff=45.86, max=45.86
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zoku` | 45.86 | not_x1 | bootrom |
| `zery` | 40.82 | not_x1 | bootrom |
| `zyky` | 8.08 | and2 | bootrom |
| `zyga` | 8.01 | and2 | bootrom |
| `zovy` | 7.75 | and2 | bootrom |
| `zuko` | 7.07 | and2 | bootrom |
| `zabu` | 5.23 | not_x1 | bootrom |
| `zete` | 5.18 | not_x1 | bootrom |
| `zefu` | 4.93 | not_x1 | bootrom |
| `zoke` | 4.91 | not_x1 | bootrom |
| `zyro` | 4.76 | not_x1 | bootrom |
| `zage` | 3.95 | not_x1 | bootrom |
| `zyra` | 3.93 | not_x1 | bootrom |
| `zapa` | 3.78 | not_x1 | bootrom |
| `bus:a2` | 0.0 |  | bus |
| `bus:a3` | 0.0 |  | bus |
| `bus:a6` | 0.0 |  | bus |
| `bus:a7` | 0.0 |  | bus |

### `cpu` (sm83) — diff=30.01, max=30.01
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `taba` | 30.01 | or3 | clocks |
| `syro` | 27.39 | not_x1 | sys-decode |
| `tutu` | 23.11 | and2 | bootrom |
| `bowa` | 15.68 | not_x6 | clocks |
| `unor` | 15.61 | and2 | test |
| `umut` | 15.41 | and2 | test |
| `boma` | 14.47 | not_x6 | clocks |
| `bedo` | 12.72 | not_x6 | clocks |
| `boga` | 11.51 | not_x6 | clocks |
| `buke` | 7.84 | not_x6 | clocks |
| `afer` | 0.0 | dffr_cc | clocks |
| `awob` | 0.0 | dlatch | joypad |
| `bus:clk_t4` | 0.0 |  | bus |
| `bus:data_phase` | 0.0 |  | bus |
| `bus:~clk_t4` | 0.0 |  | bus |
| `bus:~data_phase` | 0.0 |  | bus |
| `lalu` | 0.0 | dffsr | int |
| `lope` | 0.0 | dffsr | int |
| `nybo` | 0.0 | dffsr | int |
| `supply` | 0.0 | tie |  |
| `ubul` | 0.0 | dffsr | int |
| `ulak` | 0.0 | dffsr | int |


## Clock Distribution (21 races)

### `sola` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `teru` | 0.0 | dffr | clocks |

### `subu` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `sola` | 0.0 | dffr | clocks |

### `tama` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `unyk` | 0.0 | dffr | clocks |

### `teka` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `subu` | 0.0 | dffr | clocks |

### `tero` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `uner` | 0.0 | dffr | clocks |

### `teru` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `tofe` | 0.0 | dffr | clocks |

### `tofe` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `tugo` | 0.0 | dffr | clocks |

### `tugo` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `tulu` | 0.0 | dffr | clocks |

### `tulu` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `ugot` | 0.0 | dffr | clocks |

### `ufor` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `ukup` | 0.0 | dffr | clocks |

### `uket` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `teka` | 0.0 | dffr | clocks |

### `uner` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `ufor` | 0.0 | dffr | clocks |

### `unyk` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `tero` | 0.0 | dffr | clocks |

### `upof` (dffr) — diff=87.78, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `uket` | 0.0 | dffr | clocks |

### `ukup` (dffr) — diff=76.27, max=87.78
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 87.78 | nor3 | clocks |
| `boga` | 11.51 | not_x6 | clocks |


## APU CH4 (Noise) (71 races)

### `cuny` (drlatch_ee) — diff=83.22, max=83.22
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cazo` | 83.22 | not_x1 | apu-ch4 |
| `dulu` | 82.82 | nand2 | apu-ch4 |
| `cabe` | 21.61 | not_x1 | apu-ch4 |
| `bus:d6` | 0.0 |  | bus |

### `hoga` (drlatch_ee) — diff=75.24, max=75.24
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `goxo` | 75.24 | not_x1 | apu-ch4 |
| `foxe` | 74.76 | nand2 | apu-ch4 |
| `guzy` | 22.8 | nor2 | apu-ch4 |
| `bus:d7` | 0.0 |  | bus |

### `garu` (drlatch_ee) — diff=73.17, max=73.17
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 73.17 | not_x2 | apu-ch4 |
| `goko` | 72.15 | and2 | apu-ch4 |
| `fexo` | 33.71 | not_x1 | apu-ch4 |
| `bus:d4` | 0.0 |  | bus |

### `gedu` (drlatch_ee) — diff=73.17, max=73.17
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 73.17 | not_x2 | apu-ch4 |
| `goko` | 72.15 | and2 | apu-ch4 |
| `fexo` | 33.71 | not_x1 | apu-ch4 |
| `bus:d7` | 0.0 |  | bus |

### `geky` (drlatch_ee) — diff=73.17, max=73.17
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 73.17 | not_x2 | apu-ch4 |
| `goko` | 72.15 | and2 | apu-ch4 |
| `fexo` | 33.71 | not_x1 | apu-ch4 |
| `bus:d3` | 0.0 |  | bus |

### `goky` (drlatch_ee) — diff=73.17, max=73.17
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 73.17 | not_x2 | apu-ch4 |
| `goko` | 72.15 | and2 | apu-ch4 |
| `fexo` | 33.71 | not_x1 | apu-ch4 |
| `bus:d5` | 0.0 |  | bus |

### `gozo` (drlatch_ee) — diff=73.17, max=73.17
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 73.17 | not_x2 | apu-ch4 |
| `goko` | 72.15 | and2 | apu-ch4 |
| `fexo` | 33.71 | not_x1 | apu-ch4 |
| `bus:d6` | 0.0 |  | bus |

### `gena` (nor_latch) — diff=69.93, max=69.93
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fegy` | 69.93 | or3 | apu-ch4 |
| `gone` | 0.0 | dffr | apu-ch4 |

### `jery` (nand_latch) — diff=67.85, max=68.32
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hery` | 68.32 | nor2 | apu-ch4 |
| `hapu` | 0.47 | not_x1 | apu-ch4 |

### `emok` (drlatch_ee) — diff=66.52, max=66.52
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 66.52 | not_x1 | apu-ch4 |
| `daco` | 64.85 | and2 | apu-ch4 |
| `fexo` | 33.71 | not_x1 | apu-ch4 |
| `bus:d0` | 0.0 |  | bus |

### `etyj` (drlatch_ee) — diff=66.52, max=66.52
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 66.52 | not_x1 | apu-ch4 |
| `daco` | 64.85 | and2 | apu-ch4 |
| `fexo` | 33.71 | not_x1 | apu-ch4 |
| `bus:d1` | 0.0 |  | bus |

### `ezyk` (drlatch_ee) — diff=66.52, max=66.52
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 66.52 | not_x1 | apu-ch4 |
| `daco` | 64.85 | and2 | apu-ch4 |
| `fexo` | 33.71 | not_x1 | apu-ch4 |
| `bus:d2` | 0.0 |  | bus |

### `feta` (drlatch_ee) — diff=66.25, max=66.25
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 66.25 | not_x2 | apu-ch4 |
| `getu` | 65.35 | and2 | apu-ch4 |
| `dapa` | 28.64 | not_x2 | apu-control |
| `bus:d4` | 0.0 |  | bus |

### `fyto` (drlatch_ee) — diff=66.25, max=66.25
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 66.25 | not_x2 | apu-ch4 |
| `getu` | 65.35 | and2 | apu-ch4 |
| `dapa` | 28.64 | not_x2 | apu-control |
| `bus:d5` | 0.0 |  | bus |

### `gafo` (drlatch_ee) — diff=66.25, max=66.25
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 66.25 | not_x2 | apu-ch4 |
| `getu` | 65.35 | and2 | apu-ch4 |
| `dapa` | 28.64 | not_x2 | apu-control |
| `bus:d7` | 0.0 |  | bus |


## Sprite Control (17 races)

### `besu` (nor_latch) — diff=81.51, max=81.51
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `asen` | 81.51 | or2 | ppu-objctl |
| `catu` | 0.0 | dffr | ppu-objctl |

### `doba` (dffr) — diff=69.87, max=69.87
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bagy` | 69.87 | not_x1 | ppu-objctl |
| `alet` | 16.28 | not_x2 | ppu-control |
| `byba` | 0.0 | dffr | ppu-objctl |

### `elyn` (dffr) — diff=67.33, max=67.33
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 67.33 | nor2 | ppu-objctl |
| `goso` | 0.0 | dffr | ppu-objctl |

### `faha` (dffr) — diff=67.33, max=67.33
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 67.33 | nor2 | ppu-objctl |
| `elyn` | 0.0 | dffr | ppu-objctl |

### `fony` (dffr) — diff=67.33, max=67.33
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 67.33 | nor2 | ppu-objctl |
| `faha` | 0.0 | dffr | ppu-objctl |

### `goso` (dffr) — diff=67.33, max=67.33
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 67.33 | nor2 | ppu-objctl |
| `wewy` | 0.0 | dffr | ppu-objctl |

### `wewy` (dffr) — diff=67.33, max=67.33
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 67.33 | nor2 | ppu-objctl |
| `yfel` | 0.0 | dffr | ppu-objctl |

### `byba` (dffr) — diff=64.61, max=69.87
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bagy` | 69.87 | not_x1 | ppu-objctl |
| `feto` | 6.03 | and4 | ppu-objctl |
| `xupy` | 5.26 | not_x2 | ppu-oam |

### `yfel` (dffr) — diff=59.44, max=67.33
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 67.33 | nor2 | ppu-objctl |
| `gava` | 7.89 | or2 | ppu-objctl |

### `bego` (dffr) — diff=49.87, max=49.87
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 49.87 | not_x1 | ppu-objctl |
| `cuxy` | 0.0 | dffr | ppu-objctl |

### `cuxy` (dffr) — diff=49.87, max=49.87
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 49.87 | not_x1 | ppu-objctl |
| `bese` | 0.0 | dffr | ppu-objctl |

### `dybe` (dffr) — diff=49.87, max=49.87
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 49.87 | not_x1 | ppu-objctl |
| `bego` | 0.0 | dffr | ppu-objctl |

### `bese` (dffr) — diff=47.61, max=49.87
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 49.87 | not_x1 | ppu-objctl |
| `cake` | 2.26 | or2 | ppu-objctl |

### `dezy` (dffr) — diff=45.48, max=54.35
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyty` | 54.35 | not_x2 | ppu-objctl |
| `xapo` | 29.35 | not_x2 | ppu-control |
| `zeme` | 8.87 | not_x4 | ppu-control |

### `anel` (dffr) — diff=36.07, max=36.07
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `abez` | 36.07 | not_x1 | ppu-objctl |
| `awoh` | 5.79 | not_x1 | ppu-objctl |
| `catu` | 0.0 | dffr | ppu-objctl |


## Sprite X Match (112 races)

### `baxo` (dlatch_ee) — diff=75.49, max=75.49
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wajy` | 75.49 | not_x1 | ppu-xcomp |
| `xega` | 69.26 | not_x1 | ppu-xcomp |
| `cyra` | 0.0 | dlatch | ppu-xcomp |

### `depo` (dlatch_ee) — diff=75.49, max=75.49
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wajy` | 75.49 | not_x1 | ppu-xcomp |
| `xega` | 69.26 | not_x1 | ppu-xcomp |
| `eced` | 0.0 | dlatch | ppu-xcomp |

### `gomo` (dlatch_ee) — diff=75.49, max=75.49
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wajy` | 75.49 | not_x1 | ppu-xcomp |
| `xega` | 69.26 | not_x1 | ppu-xcomp |
| `wyno` | 0.0 | dlatch | ppu-xcomp |

### `ylor` (dlatch_ee) — diff=75.49, max=75.49
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wajy` | 75.49 | not_x1 | ppu-xcomp |
| `xega` | 69.26 | not_x1 | ppu-xcomp |
| `xyky` | 0.0 | dlatch | ppu-xcomp |

### `yzos` (dlatch_ee) — diff=75.49, max=75.49
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wajy` | 75.49 | not_x1 | ppu-xcomp |
| `xega` | 69.26 | not_x1 | ppu-xcomp |
| `zuve` | 0.0 | dlatch | ppu-xcomp |

### `zezy` (dlatch_ee) — diff=75.49, max=75.49
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wajy` | 75.49 | not_x1 | ppu-xcomp |
| `xega` | 69.26 | not_x1 | ppu-xcomp |
| `yvel` | 0.0 | dlatch | ppu-xcomp |

### `zyty` (dlatch_ee) — diff=75.49, max=75.49
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wajy` | 75.49 | not_x1 | ppu-xcomp |
| `xega` | 69.26 | not_x1 | ppu-xcomp |
| `yrum` | 0.0 | dlatch | ppu-xcomp |

### `zyve` (dlatch_ee) — diff=75.49, max=75.49
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wajy` | 75.49 | not_x1 | ppu-xcomp |
| `xega` | 69.26 | not_x1 | ppu-xcomp |
| `ysex` | 0.0 | dlatch | ppu-xcomp |

### `cyra` (dlatch) — diff=73.19, max=73.19
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_a_d5` | 0.0 |  | bus |

### `eced` (dlatch) — diff=73.19, max=73.19
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_a_d7` | 0.0 |  | bus |

### `wyno` (dlatch) — diff=73.19, max=73.19
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_a_d4` | 0.0 |  | bus |

### `xyky` (dlatch) — diff=73.19, max=73.19
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_a_d0` | 0.0 |  | bus |

### `yrum` (dlatch) — diff=73.19, max=73.19
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_a_d1` | 0.0 |  | bus |

### `ysex` (dlatch) — diff=73.19, max=73.19
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_a_d2` | 0.0 |  | bus |

### `yvel` (dlatch) — diff=73.19, max=73.19
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_a_d3` | 0.0 |  | bus |


## Palettes (24 races)

### `xalo` (dlatch_ee) — diff=74.54, max=74.54
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 74.54 | not_x1 | ppu-pal |
| `xelo` | 69.22 | not_x1 | ppu-pal |
| `bus:d3` | 0.0 |  | bus |

### `xana` (dlatch_ee) — diff=74.54, max=74.54
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 74.54 | not_x1 | ppu-pal |
| `xelo` | 69.22 | not_x1 | ppu-pal |
| `bus:d7` | 0.0 |  | bus |

### `xeru` (dlatch_ee) — diff=74.54, max=74.54
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 74.54 | not_x1 | ppu-pal |
| `xelo` | 69.22 | not_x1 | ppu-pal |
| `bus:d4` | 0.0 |  | bus |

### `xova` (dlatch_ee) — diff=74.54, max=74.54
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 74.54 | not_x1 | ppu-pal |
| `xelo` | 69.22 | not_x1 | ppu-pal |
| `bus:d2` | 0.0 |  | bus |

### `xufu` (dlatch_ee) — diff=74.54, max=74.54
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 74.54 | not_x1 | ppu-pal |
| `xelo` | 69.22 | not_x1 | ppu-pal |
| `bus:d0` | 0.0 |  | bus |

### `xuky` (dlatch_ee) — diff=74.54, max=74.54
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 74.54 | not_x1 | ppu-pal |
| `xelo` | 69.22 | not_x1 | ppu-pal |
| `bus:d1` | 0.0 |  | bus |

### `xupo` (dlatch_ee) — diff=74.54, max=74.54
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 74.54 | not_x1 | ppu-pal |
| `xelo` | 69.22 | not_x1 | ppu-pal |
| `bus:d6` | 0.0 |  | bus |

### `xyze` (dlatch_ee) — diff=74.54, max=74.54
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 74.54 | not_x1 | ppu-pal |
| `xelo` | 69.22 | not_x1 | ppu-pal |
| `bus:d5` | 0.0 |  | bus |

### `maxy` (dlatch_ee) — diff=62.91, max=62.91
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 62.91 | not_x1 | ppu-pal |
| `tepo` | 59.91 | not_x1 | ppu-pal |
| `bus:d3` | 0.0 |  | bus |

### `mena` (dlatch_ee) — diff=62.91, max=62.91
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 62.91 | not_x1 | ppu-pal |
| `tepo` | 59.91 | not_x1 | ppu-pal |
| `bus:d7` | 0.0 |  | bus |

### `mogy` (dlatch_ee) — diff=62.91, max=62.91
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 62.91 | not_x1 | ppu-pal |
| `tepo` | 59.91 | not_x1 | ppu-pal |
| `bus:d6` | 0.0 |  | bus |

### `moru` (dlatch_ee) — diff=62.91, max=62.91
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 62.91 | not_x1 | ppu-pal |
| `tepo` | 59.91 | not_x1 | ppu-pal |
| `bus:d5` | 0.0 |  | bus |

### `muke` (dlatch_ee) — diff=62.91, max=62.91
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 62.91 | not_x1 | ppu-pal |
| `tepo` | 59.91 | not_x1 | ppu-pal |
| `bus:d4` | 0.0 |  | bus |

### `nusy` (dlatch_ee) — diff=62.91, max=62.91
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 62.91 | not_x1 | ppu-pal |
| `tepo` | 59.91 | not_x1 | ppu-pal |
| `bus:d1` | 0.0 |  | bus |

### `pavo` (dlatch_ee) — diff=62.91, max=62.91
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 62.91 | not_x1 | ppu-pal |
| `tepo` | 59.91 | not_x1 | ppu-pal |
| `bus:d0` | 0.0 |  | bus |


## APU CH2 (Square) (60 races)

### `buta` (nand_latch) — diff=73.58, max=73.88
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ares` | 73.88 | nor2 | apu-ch2 |
| `bodo` | 0.3 | not_x1 | apu-ch2 |

### `jany` (drlatch_ee) — diff=72.61, max=72.61
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kysa` | 72.61 | not_x1 | apu-ch2 |
| `jenu` | 70.97 | and2 | apu-ch2 |
| `kypu` | 22.75 | not_x1 | apu-ch2 |
| `bus:d1` | 0.0 |  | bus |

### `jefu` (drlatch_ee) — diff=72.61, max=72.61
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kysa` | 72.61 | not_x1 | apu-ch2 |
| `jenu` | 70.97 | and2 | apu-ch2 |
| `kypu` | 22.75 | not_x1 | apu-ch2 |
| `bus:d0` | 0.0 |  | bus |

### `jupy` (drlatch_ee) — diff=72.61, max=72.61
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kysa` | 72.61 | not_x1 | apu-ch2 |
| `jenu` | 70.97 | and2 | apu-ch2 |
| `kypu` | 22.75 | not_x1 | apu-ch2 |
| `bus:d2` | 0.0 |  | bus |

### `dane` (nor_latch) — diff=69.69, max=69.69
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esyk` | 69.69 | or3 | apu-ch2 |
| `elox` | 0.0 | dffr | apu-ch2 |

### `etap` (drlatch_ee) — diff=69.63, max=69.63
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `daxu` | 69.63 | not_x1 | apu-ch2 |
| `deta` | 69.22 | nand2 | apu-ch2 |
| `dera` | 27.19 | nor2 | apu-ch2 |
| `bus:d7` | 0.0 |  | bus |

### `emer` (drlatch_ee) — diff=67.62, max=67.62
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `duso` | 67.62 | not_x1 | apu-ch2 |
| `evyf` | 67.15 | nand2 | apu-ch2 |
| `fazo` | 21.9 | not_x1 | apu-ch2 |
| `bus:d6` | 0.0 |  | bus |

### `fore` (drlatch_ee) — diff=61.32, max=61.32
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 61.32 | not_x2 | apu-ch2 |
| `enuf` | 59.68 | and2 | apu-ch2 |
| `jybu` | 25.59 | not_x1 | apu-ch2 |
| `bus:d3` | 0.0 |  | bus |

### `gata` (drlatch_ee) — diff=61.32, max=61.32
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 61.32 | not_x2 | apu-ch2 |
| `enuf` | 59.68 | and2 | apu-ch2 |
| `jybu` | 25.59 | not_x1 | apu-ch2 |
| `bus:d4` | 0.0 |  | bus |

### `gufe` (drlatch_ee) — diff=61.32, max=61.32
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 61.32 | not_x2 | apu-ch2 |
| `enuf` | 59.68 | and2 | apu-ch2 |
| `jybu` | 25.59 | not_x1 | apu-ch2 |
| `bus:d5` | 0.0 |  | bus |

### `gura` (drlatch_ee) — diff=61.32, max=61.32
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 61.32 | not_x2 | apu-ch2 |
| `enuf` | 59.68 | and2 | apu-ch2 |
| `jybu` | 25.59 | not_x1 | apu-ch2 |
| `bus:d6` | 0.0 |  | bus |

### `came` (tffnl) — diff=60.7, max=60.7
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bymo` | 60.7 | not_x1 | apu-ch2 |
| `bus:d3` | 0.0 |  | bus |
| `conu` | 0.0 | tffnl | apu-ch2 |

### `cera` (tffnl) — diff=60.7, max=60.7
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bymo` | 60.7 | not_x1 | apu-ch2 |
| `bus:d1` | 0.0 |  | bus |
| `eryc` | 0.0 | tffnl | apu-ch2 |

### `conu` (tffnl) — diff=60.7, max=60.7
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bymo` | 60.7 | not_x1 | apu-ch2 |
| `bus:d2` | 0.0 |  | bus |
| `cera` | 0.0 | tffnl | apu-ch2 |

### `eryc` (tffnl) — diff=60.7, max=60.7
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bymo` | 60.7 | not_x1 | apu-ch2 |
| `dyro` | 18.51 | not_x1 | apu-ch1 |
| `bus:d0` | 0.0 |  | bus |


## Sprite Y Compare (26 races)

### `sobu` (dffr) — diff=73.46, max=100.79
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `teky` | 100.79 | and4 | ppu-ycomp |
| `tava` | 27.33 | not_x1 | ppu-ycomp |

### `wone` (dlatch) — diff=73.19, max=73.19
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_b_d3` | 0.0 |  | bus |

### `xafu` (dlatch) — diff=73.19, max=73.19
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_b_d5` | 0.0 |  | bus |

### `yceb` (dlatch) — diff=73.19, max=73.19
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_b_d1` | 0.0 |  | bus |

### `ydyv` (dlatch) — diff=73.19, max=73.19
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_b_d0` | 0.0 |  | bus |

### `yses` (dlatch) — diff=73.19, max=73.19
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_b_d6` | 0.0 |  | bus |

### `zaxe` (dlatch) — diff=73.19, max=73.19
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_b_d4` | 0.0 |  | bus |

### `zeca` (dlatch) — diff=73.19, max=73.19
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_b_d7` | 0.0 |  | bus |

### `zuca` (dlatch) — diff=73.19, max=73.19
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 73.19 | not_x1 | ppu-oam |
| `bus:~oam_b_d2` | 0.0 |  | bus |

### `wyso` (dlatch_ee) — diff=70.25, max=70.25
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 70.25 | not_x1 | ppu-ycomp |
| `ywok` | 66.77 | not_x1 | ppu-ycomp |
| `xafu` | 0.0 | dlatch | ppu-ycomp |

### `xegu` (dlatch_ee) — diff=70.25, max=70.25
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 70.25 | not_x1 | ppu-ycomp |
| `ywok` | 66.77 | not_x1 | ppu-ycomp |
| `yceb` | 0.0 | dlatch | ppu-ycomp |

### `xote` (dlatch_ee) — diff=70.25, max=70.25
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 70.25 | not_x1 | ppu-ycomp |
| `ywok` | 66.77 | not_x1 | ppu-ycomp |
| `yses` | 0.0 | dlatch | ppu-ycomp |

### `xuso` (dlatch_ee) — diff=70.25, max=70.25
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 70.25 | not_x1 | ppu-ycomp |
| `ywok` | 66.77 | not_x1 | ppu-ycomp |
| `ydyv` | 0.0 | dlatch | ppu-ycomp |

### `xyju` (dlatch_ee) — diff=70.25, max=70.25
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 70.25 | not_x1 | ppu-ycomp |
| `ywok` | 66.77 | not_x1 | ppu-ycomp |
| `wone` | 0.0 | dlatch | ppu-ycomp |

### `ybog` (dlatch_ee) — diff=70.25, max=70.25
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 70.25 | not_x1 | ppu-ycomp |
| `ywok` | 66.77 | not_x1 | ppu-ycomp |
| `zaxe` | 0.0 | dlatch | ppu-ycomp |


## Serial (18 races)

### `eder` (dffsr) — diff=72.99, max=72.99
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efef` | 72.99 | nand2 | serial |
| `eguv` | 65.9 | oa21 | serial |
| `epyt` | 21.55 | not_x2 | serial |
| `erod` | 0.0 | dffsr | serial |

### `ejab` (dffsr) — diff=72.99, max=72.99
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elok` | 72.99 | nand2 | serial |
| `ehuj` | 65.9 | oa21 | serial |
| `epyt` | 21.55 | not_x2 | serial |
| `dovu` | 0.0 | dffsr | serial |

### `erod` (dffsr) — diff=72.99, max=72.99
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `edel` | 72.99 | nand2 | serial |
| `efak` | 65.9 | oa21 | serial |
| `epyt` | 21.55 | not_x2 | serial |
| `ejab` | 0.0 | dffsr | serial |

### `degu` (dffsr) — diff=72.98, max=72.98
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `docu` | 72.98 | nand2 | serial |
| `dumo` | 65.9 | oa21 | serial |
| `dawe` | 23.22 | not_x2 | serial |
| `cuba` | 0.0 | dffsr | serial |

### `dojo` (dffsr) — diff=72.98, max=72.98
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyge` | 72.98 | nand2 | serial |
| `daju` | 65.9 | oa21 | serial |
| `dawe` | 23.22 | not_x2 | serial |
| `dyra` | 0.0 | dffsr | serial |

### `dovu` (dffsr) — diff=72.98, max=72.98
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dola` | 72.98 | nand2 | serial |
| `dyly` | 65.9 | oa21 | serial |
| `epyt` | 21.55 | not_x2 | serial |
| `dojo` | 0.0 | dffsr | serial |

### `dyra` (dffsr) — diff=72.98, max=72.98
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dela` | 72.98 | nand2 | serial |
| `dybo` | 65.9 | oa21 | serial |
| `dawe` | 23.22 | not_x2 | serial |
| `degu` | 0.0 | dffsr | serial |

### `cuba` (dffsr) — diff=72.23, max=72.98
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cufu` | 72.98 | nand2 | serial |
| `cohy` | 65.9 | oa21 | serial |
| `dawe` | 23.22 | not_x2 | serial |
| `cage` | 0.75 | not_x1 | serial |

### `caly` (dffr) — diff=65.36, max=65.36
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 65.36 | and2 | serial |
| `cyde` | 0.0 | dffr | serial |

### `cyde` (dffr) — diff=65.36, max=65.36
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 65.36 | and2 | serial |
| `cylo` | 0.0 | dffr | serial |

### `cylo` (dffr) — diff=65.36, max=65.36
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 65.36 | and2 | serial |
| `cafa` | 0.0 | dffr | serial |

### `culy` (dffr) — diff=62.64, max=62.64
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 62.64 | nand4 | serial |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d0` | 0.0 |  | bus |

### `etaf` (dffr) — diff=62.64, max=62.64
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 62.64 | nand4 | serial |
| `caby` | 10.81 | and2 | serial |
| `bus:d7` | 0.0 |  | bus |

### `coty` (dffr) — diff=57.45, max=62.64
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 62.64 | nand4 | serial |
| `uvyn` | 5.19 | not_x1 | clocks |

### `cafa` (dffr) — diff=46.82, max=65.36
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 65.36 | and2 | serial |
| `dawa` | 18.54 | or2 | serial |


## APU CH3 (Wave) (64 races)

### `jacy` (drlatch_ee) — diff=72.78, max=72.78
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 72.78 | not_x1 | apu-ch3 |
| `huda` | 71.86 | and2 | apu-ch3 |
| `kopy` | 23.04 | not_x1 | apu-ch3 |
| `bus:d2` | 0.0 |  | bus |

### `jemo` (drlatch_ee) — diff=72.78, max=72.78
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 72.78 | not_x1 | apu-ch3 |
| `huda` | 71.86 | and2 | apu-ch3 |
| `kopy` | 23.04 | not_x1 | apu-ch3 |
| `bus:d0` | 0.0 |  | bus |

### `jety` (drlatch_ee) — diff=72.78, max=72.78
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 72.78 | not_x1 | apu-ch3 |
| `huda` | 71.86 | and2 | apu-ch3 |
| `kopy` | 23.04 | not_x1 | apu-ch3 |
| `bus:d1` | 0.0 |  | bus |

### `gavu` (drlatch_ee) — diff=70.35, max=70.35
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fene` | 70.35 | not_x1 | apu-ch3 |
| `epyx` | 69.94 | nand2 | apu-ch3 |
| `fako` | 22.21 | nor2 | apu-ch3 |
| `bus:d7` | 0.0 |  | bus |

### `hoto` (drlatch_ee) — diff=69.07, max=69.07
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gygu` | 69.07 | not_x1 | apu-ch3 |
| `fovo` | 68.64 | nand2 | apu-ch3 |
| `heky` | 22.92 | not_x1 | apu-ch3 |
| `bus:d6` | 0.0 |  | bus |

### `gage` (drlatch_ee) — diff=61.32, max=61.32
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 61.32 | not_x2 | apu-ch2 |
| `enuf` | 59.68 | and2 | apu-ch2 |
| `jybu` | 25.59 | not_x1 | apu-ch2 |
| `bus:d7` | 0.0 |  | bus |

### `jaxa` (drlatch_ee) — diff=59.59, max=59.59
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 59.59 | not_x2 | apu-ch3 |
| `jafa` | 58.24 | and2 | apu-ch3 |
| `kuha` | 25.44 | not_x1 | apu-ch3 |
| `bus:d2` | 0.0 |  | bus |

### `jefe` (drlatch_ee) — diff=59.59, max=59.59
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 59.59 | not_x2 | apu-ch3 |
| `jafa` | 58.24 | and2 | apu-ch3 |
| `kuha` | 25.44 | not_x1 | apu-ch3 |
| `bus:d3` | 0.0 |  | bus |

### `jovy` (drlatch_ee) — diff=59.59, max=59.59
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 59.59 | not_x2 | apu-ch3 |
| `jafa` | 58.24 | and2 | apu-ch3 |
| `kuha` | 25.44 | not_x1 | apu-ch3 |
| `bus:d1` | 0.0 |  | bus |

### `jypo` (drlatch_ee) — diff=59.59, max=59.59
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 59.59 | not_x2 | apu-ch3 |
| `jafa` | 58.24 | and2 | apu-ch3 |
| `kuha` | 25.44 | not_x1 | apu-ch3 |
| `bus:d4` | 0.0 |  | bus |

### `koga` (drlatch_ee) — diff=59.59, max=59.59
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 59.59 | not_x2 | apu-ch3 |
| `jafa` | 58.24 | and2 | apu-ch3 |
| `kuha` | 25.44 | not_x1 | apu-ch3 |
| `bus:d0` | 0.0 |  | bus |

### `guxe` (drlatch_ee) — diff=59.33, max=59.33
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gucy` | 59.33 | not_x1 | apu-ch3 |
| `gejo` | 59.05 | and2 | apu-ch3 |
| `gove` | 21.69 | not_x1 | apu-ch3 |
| `bus:d7` | 0.0 |  | bus |

### `fexu` (dffr) — diff=58.69, max=58.69
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guda` | 58.69 | nor3 | apu-ch3 |
| `fyru` | 0.0 | tffnl | apu-ch3 |

### `jove` (drlatch_ee) — diff=58.57, max=58.57
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 58.57 | not_x1 | apu-ch3 |
| `kota` | 57.18 | and2 | apu-ch3 |
| `kuha` | 25.44 | not_x1 | apu-ch3 |
| `bus:d5` | 0.0 |  | bus |

### `kana` (drlatch_ee) — diff=58.57, max=58.57
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 58.57 | not_x1 | apu-ch3 |
| `kota` | 57.18 | and2 | apu-ch3 |
| `kuha` | 25.44 | not_x1 | apu-ch3 |
| `bus:d6` | 0.0 |  | bus |


## Timer (21 races)

### `nydu` (dffr) — diff=72.08, max=72.08
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mugy` | 72.08 | not_x1 | timer |
| `boga` | 11.51 | not_x6 | clocks |
| `nuga` | 0.0 | tffnl | timer |

### `nuga` (tffnl) — diff=70.96, max=70.96
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 70.96 | nand3 | timer |
| `pagu` | 66.8 | nor2 | timer |
| `peda` | 0.0 | tffnl | timer |

### `peda` (tffnl) — diff=70.96, max=70.96
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 70.96 | nand3 | timer |
| `pyma` | 65.55 | nor2 | timer |
| `rage` | 0.0 | tffnl | timer |

### `peru` (tffnl) — diff=70.96, max=70.96
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 70.96 | nand3 | timer |
| `nada` | 65.94 | nor2 | timer |
| `povy` | 0.0 | tffnl | timer |

### `povy` (tffnl) — diff=70.96, max=70.96
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 70.96 | nand3 | timer |
| `nero` | 66.05 | nor2 | timer |
| `rega` | 0.0 | tffnl | timer |

### `rage` (tffnl) — diff=70.96, max=70.96
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 70.96 | nand3 | timer |
| `rugy` | 65.78 | nor2 | timer |
| `ruby` | 0.0 | tffnl | timer |

### `rate` (tffnl) — diff=70.96, max=70.96
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 70.96 | nand3 | timer |
| `repa` | 64.95 | nor2 | timer |
| `peru` | 0.0 | tffnl | timer |

### `ruby` (tffnl) — diff=70.96, max=70.96
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 70.96 | nand3 | timer |
| `rolu` | 64.1 | nor2 | timer |
| `rate` | 0.0 | tffnl | timer |

### `muru` (dffr) — diff=59.73, max=59.73
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 59.73 | nand4 | timer |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d2` | 0.0 |  | bus |

### `nyke` (dffr) — diff=59.73, max=59.73
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 59.73 | nand4 | timer |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d1` | 0.0 |  | bus |

### `peto` (dffr) — diff=59.73, max=59.73
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 59.73 | nand4 | timer |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d6` | 0.0 |  | bus |

### `sabu` (dffr) — diff=59.73, max=59.73
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 59.73 | nand4 | timer |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d0` | 0.0 |  | bus |

### `seta` (dffr) — diff=59.73, max=59.73
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 59.73 | nand4 | timer |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d7` | 0.0 |  | bus |

### `sufy` (dffr) — diff=59.73, max=59.73
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 59.73 | nand4 | timer |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d5` | 0.0 |  | bus |

### `tyru` (dffr) — diff=59.73, max=59.73
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 59.73 | nand4 | timer |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d4` | 0.0 |  | bus |


## Sprite Store (100 races)

### `dafu` (dlatch_ee) — diff=71.23, max=71.23
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ebeb` | 71.23 | not_x1 | ppu-objctl |
| `feka` | 68.36 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0.0 |  | bus |

### `deba` (dlatch_ee) — diff=71.23, max=71.23
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ebeb` | 71.23 | not_x1 | ppu-objctl |
| `feka` | 68.36 | not_x1 | ppu-objctl |
| `bus:oam_render_a6` | 0.0 |  | bus |

### `dese` (dlatch_ee) — diff=71.23, max=71.23
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ebeb` | 71.23 | not_x1 | ppu-objctl |
| `feka` | 68.36 | not_x1 | ppu-objctl |
| `bus:oam_render_a3` | 0.0 |  | bus |

### `devy` (dlatch_ee) — diff=71.23, max=71.23
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ebeb` | 71.23 | not_x1 | ppu-objctl |
| `feka` | 68.36 | not_x1 | ppu-objctl |
| `bus:oam_render_a2` | 0.0 |  | bus |

### `duha` (dlatch_ee) — diff=71.23, max=71.23
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ebeb` | 71.23 | not_x1 | ppu-objctl |
| `feka` | 68.36 | not_x1 | ppu-objctl |
| `bus:oam_render_a5` | 0.0 |  | bus |

### `duny` (dlatch_ee) — diff=71.23, max=71.23
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ebeb` | 71.23 | not_x1 | ppu-objctl |
| `feka` | 68.36 | not_x1 | ppu-objctl |
| `bus:oam_render_a4` | 0.0 |  | bus |

### `wanu` (dlatch_ee) — diff=70.63, max=70.63
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wude` | 70.63 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a4` | 0.0 |  | bus |

### `xabo` (dlatch_ee) — diff=70.63, max=70.63
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wude` | 70.63 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a5` | 0.0 |  | bus |

### `xave` (dlatch_ee) — diff=70.63, max=70.63
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wude` | 70.63 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a2` | 0.0 |  | bus |

### `xefe` (dlatch_ee) — diff=70.63, max=70.63
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wude` | 70.63 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a3` | 0.0 |  | bus |

### `xege` (dlatch_ee) — diff=70.63, max=70.63
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wude` | 70.63 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a6` | 0.0 |  | bus |

### `xynu` (dlatch_ee) — diff=70.63, max=70.63
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wude` | 70.63 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0.0 |  | bus |

### `caju` (dlatch_ee) — diff=70.5, max=70.5
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `baba` | 70.5 | not_x1 | ppu-objctl |
| `ewot` | 68.19 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0.0 |  | bus |

### `capo` (dlatch_ee) — diff=70.5, max=70.5
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `baba` | 70.5 | not_x1 | ppu-objctl |
| `ewot` | 68.19 | not_x1 | ppu-objctl |
| `bus:sprite_y_store0` | 0.0 |  | bus |

### `cono` (dlatch_ee) — diff=70.5, max=70.5
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `baba` | 70.5 | not_x1 | ppu-objctl |
| `ewot` | 68.19 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0.0 |  | bus |


## APU Control (31 races)

### `anev` (drlatch_ee) — diff=71.16, max=71.16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 71.16 | not_x2 | apu-control |
| `bono` | 69.8 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d0` | 0.0 |  | bus |

### `atuf` (drlatch_ee) — diff=71.16, max=71.16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 71.16 | not_x2 | apu-control |
| `bono` | 69.8 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d3` | 0.0 |  | bus |

### `bafo` (drlatch_ee) — diff=71.16, max=71.16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 71.16 | not_x2 | apu-control |
| `bono` | 69.8 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d2` | 0.0 |  | bus |

### `bogu` (drlatch_ee) — diff=71.16, max=71.16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 71.16 | not_x2 | apu-control |
| `bono` | 69.8 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d1` | 0.0 |  | bus |

### `befo` (drlatch_ee) — diff=70.57, max=70.57
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 70.57 | not_x2 | apu-control |
| `byfa` | 69.52 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d6` | 0.0 |  | bus |

### `bepu` (drlatch_ee) — diff=70.57, max=70.57
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 70.57 | not_x2 | apu-control |
| `byfa` | 69.52 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d7` | 0.0 |  | bus |

### `bofa` (drlatch_ee) — diff=70.57, max=70.57
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 70.57 | not_x2 | apu-control |
| `byfa` | 69.52 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d5` | 0.0 |  | bus |

### `bume` (drlatch_ee) — diff=70.57, max=70.57
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 70.57 | not_x2 | apu-control |
| `byfa` | 69.52 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d4` | 0.0 |  | bus |

### `bedu` (drlatch_ee) — diff=65.9, max=65.9
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 65.9 | not_x2 | apu-control |
| `baxy` | 64.59 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d7` | 0.0 |  | bus |

### `bumo` (drlatch_ee) — diff=65.9, max=65.9
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 65.9 | not_x2 | apu-control |
| `baxy` | 64.59 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d5` | 0.0 |  | bus |

### `byre` (drlatch_ee) — diff=65.9, max=65.9
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 65.9 | not_x2 | apu-control |
| `baxy` | 64.59 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d4` | 0.0 |  | bus |

### `cozu` (drlatch_ee) — diff=65.9, max=65.9
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 65.9 | not_x2 | apu-control |
| `baxy` | 64.59 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d6` | 0.0 |  | bus |

### `ager` (drlatch_ee) — diff=65.26, max=65.26
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 65.26 | not_x2 | apu-control |
| `bowe` | 64.19 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d2` | 0.0 |  | bus |

### `apeg` (drlatch_ee) — diff=65.26, max=65.26
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 65.26 | not_x2 | apu-control |
| `bowe` | 64.19 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d0` | 0.0 |  | bus |

### `apos` (drlatch_ee) — diff=65.26, max=65.26
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 65.26 | not_x2 | apu-control |
| `bowe` | 64.19 | not_x2 | apu-control |
| `kepy` | 23.11 | not_x3 | apu-control |
| `bus:d3` | 0.0 |  | bus |


## Joypad (15 races)

### `cofy` (dffr) — diff=70.06, max=70.06
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 70.06 | nand4 | joypad |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d5` | 0.0 |  | bus |

### `kely` (dffr) — diff=70.06, max=70.06
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 70.06 | nand4 | joypad |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d4` | 0.0 |  | bus |

### `kapa` (dlatch) — diff=58.67, max=58.67
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 58.67 | not_x1 | joypad |
| `p11` | 0.0 | pad_bidir_pu | joypad |

### `keja` (dlatch) — diff=58.67, max=58.67
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 58.67 | not_x1 | joypad |
| `p12` | 0.0 | pad_bidir_pu | joypad |

### `kevu` (dlatch) — diff=58.67, max=58.67
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 58.67 | not_x1 | joypad |
| `p10` | 0.0 | pad_bidir_pu | joypad |

### `kolo` (dlatch) — diff=58.67, max=58.67
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 58.67 | not_x1 | joypad |
| `p13` | 0.0 | pad_bidir_pu | joypad |

### `p13` (pad_bidir_pu) — diff=25.47, max=35.33
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kale` | 35.33 | nor2 | test |
| `kory` | 9.86 | nand2 | test |

### `p14` (pad_out_diff) — diff=25.43, max=25.43
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `karu` | 25.43 | or2 | joypad |
| `kely` | 0.0 | dffr | joypad |

### `p15` (pad_out_diff) — diff=21.83, max=21.83
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cela` | 21.83 | or2 | joypad |
| `cofy` | 0.0 | dffr | joypad |

### `p11` (pad_bidir_pu) — diff=21.18, max=25.7
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kabu` | 25.7 | nor2 | test |
| `kyto` | 4.52 | nand2 | test |

### `p12` (pad_bidir_pu) — diff=20.48, max=25.44
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kasy` | 25.44 | nor2 | test |
| `kyhu` | 4.96 | nand2 | test |

### `p10` (pad_bidir_pu) — diff=20.15, max=24.16
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kybu` | 24.16 | nor2 | test |
| `kole` | 4.01 | nand2 | test |

### `acef` (dffr) — diff=11.51, max=11.51
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 11.51 | not_x6 | clocks |
| `alur` | 8.64 | not_x2 | clocks |
| `batu` | 0.0 | dffr | joypad |

### `agem` (dffr) — diff=11.51, max=11.51
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 11.51 | not_x6 | clocks |
| `alur` | 8.64 | not_x2 | clocks |
| `acef` | 0.0 | dffr | joypad |

### `apug` (dffr) — diff=11.51, max=11.51
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 11.51 | not_x6 | clocks |
| `alur` | 8.64 | not_x2 | clocks |
| `agem` | 0.0 | dffr | joypad |


## Test Mode (8 races)

### `jale` (dffr) — diff=70.06, max=70.06
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 70.06 | nand4 | joypad |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d2` | 0.0 |  | bus |

### `jute` (dffr) — diff=70.06, max=70.06
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 70.06 | nand4 | joypad |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d0` | 0.0 |  | bus |

### `kecy` (dffr) — diff=70.06, max=70.06
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 70.06 | nand4 | joypad |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d1` | 0.0 |  | bus |

### `keru` (dffr) — diff=70.06, max=70.06
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 70.06 | nand4 | joypad |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d7` | 0.0 |  | bus |

### `kuko` (dffr) — diff=70.06, max=70.06
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 70.06 | nand4 | joypad |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d6` | 0.0 |  | bus |

### `kyme` (dffr) — diff=70.06, max=70.06
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 70.06 | nand4 | joypad |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d3` | 0.0 |  | bus |

### `amut` (dffr) — diff=48.52, max=48.52
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 48.52 | nand5 | test |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d1` | 0.0 |  | bus |

### `buro` (dffr) — diff=48.52, max=48.52
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 48.52 | nand5 | test |
| `alur` | 8.64 | not_x2 | clocks |
| `bus:d0` | 0.0 |  | bus |


## DMA (22 races)

### `maru` (dlatch_ee) — diff=65.51, max=65.51
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 65.51 | not_x1 | ppu-dma |
| `loru` | 61.21 | not_x1 | ppu-dma |
| `bus:d7` | 0.0 |  | bus |

### `nafa` (dlatch_ee) — diff=65.51, max=65.51
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 65.51 | not_x1 | ppu-dma |
| `loru` | 61.21 | not_x1 | ppu-dma |
| `bus:d0` | 0.0 |  | bus |

### `nydo` (dlatch_ee) — diff=65.51, max=65.51
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 65.51 | not_x1 | ppu-dma |
| `loru` | 61.21 | not_x1 | ppu-dma |
| `bus:d3` | 0.0 |  | bus |

### `nygy` (dlatch_ee) — diff=65.51, max=65.51
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 65.51 | not_x1 | ppu-dma |
| `loru` | 61.21 | not_x1 | ppu-dma |
| `bus:d4` | 0.0 |  | bus |

### `para` (dlatch_ee) — diff=65.51, max=65.51
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 65.51 | not_x1 | ppu-dma |
| `loru` | 61.21 | not_x1 | ppu-dma |
| `bus:d2` | 0.0 |  | bus |

### `poku` (dlatch_ee) — diff=65.51, max=65.51
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 65.51 | not_x1 | ppu-dma |
| `loru` | 61.21 | not_x1 | ppu-dma |
| `bus:d6` | 0.0 |  | bus |

### `pula` (dlatch_ee) — diff=65.51, max=65.51
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 65.51 | not_x1 | ppu-dma |
| `loru` | 61.21 | not_x1 | ppu-dma |
| `bus:d5` | 0.0 |  | bus |

### `pyne` (dlatch_ee) — diff=65.51, max=65.51
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 65.51 | not_x1 | ppu-dma |
| `loru` | 61.21 | not_x1 | ppu-dma |
| `bus:d1` | 0.0 |  | bus |

### `luvy` (dffr) — diff=55.26, max=57.6
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lupa` | 57.6 | nor2 | ppu-dma |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `uvyt` | 2.34 | not_x2 | clocks |

### `wuje` (nor_latch) — diff=39.76, max=51.53
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xuto` | 51.53 | and2 | ppu-oam |
| `xyny` | 11.77 | not_x1 | ppu-dma |

### `lyxe` (nor_latch) — diff=38.5, max=56.03
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavy` | 56.03 | and2 | ppu-dma |
| `loko` | 17.53 | nand2 | ppu-dma |

### `mugu` (dffr) — diff=23.75, max=23.75
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 23.75 | not_x1 | ppu-dma |
| `nuto` | 0.0 | dffr | ppu-dma |

### `muty` (dffr) — diff=23.75, max=23.75
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 23.75 | not_x1 | ppu-dma |
| `nefy` | 0.0 | dffr | ppu-dma |

### `nefy` (dffr) — diff=23.75, max=23.75
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 23.75 | not_x1 | ppu-dma |
| `pyro` | 0.0 | dffr | ppu-dma |

### `nuto` (dffr) — diff=23.75, max=23.75
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 23.75 | not_x1 | ppu-dma |
| `pylo` | 0.0 | dffr | ppu-dma |


## Interrupts (10 races)

### `ubul` (dffsr) — diff=64.97, max=64.97
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tome` | 64.97 | nand3 | int |
| `tuny` | 58.55 | and3 | int |
| `caly` | 0.0 | dffr | serial |

### `nybo` (dffsr) — diff=64.45, max=64.45
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pyhu` | 64.45 | nand3 | int |
| `pyga` | 58.78 | and3 | int |
| `moba` | 0.0 | dffr | timer |

### `ulak` (dffsr) — diff=53.37, max=64.47
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `toga` | 64.47 | nand3 | int |
| `tyme` | 59.55 | and3 | int |
| `asok` | 11.1 | and2 | joypad |

### `maty` (dlatch) — diff=51.36, max=51.36
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 51.36 | nand4 | int |
| `lope` | 0.0 | dffsr | int |

### `mopo` (dlatch) — diff=51.36, max=51.36
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 51.36 | nand4 | int |
| `lalu` | 0.0 | dffsr | int |

### `nejy` (dlatch) — diff=51.36, max=51.36
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 51.36 | nand4 | int |
| `ubul` | 0.0 | dffsr | int |

### `nuty` (dlatch) — diff=51.36, max=51.36
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 51.36 | nand4 | int |
| `ulak` | 0.0 | dffsr | int |

### `pavy` (dlatch) — diff=51.36, max=51.36
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 51.36 | nand4 | int |
| `nybo` | 0.0 | dffsr | int |

### `lope` (dffsr) — diff=46.15, max=64.4
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myzu` | 64.4 | nand3 | int |
| `lyta` | 59.1 | and3 | int |
| `vypu` | 18.25 | not_x3 | ppu-stat |

### `lalu` (dffsr) — diff=5.85, max=64.81
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voty` | 64.81 | not_x3 | ppu-stat |
| `mody` | 64.49 | nand3 | int |
| `movu` | 58.96 | and3 | int |


## STAT/LY (32 races)

### `tuky` (dffr) — diff=64.66, max=66.29
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 66.29 | nor2 | ppu-stat |
| `toca` | 2.22 | not_x1 | ppu-stat |
| `sake` | 1.63 | xor | ppu-stat |

### `savy` (dffr) — diff=64.58, max=66.29
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 66.29 | nor2 | ppu-stat |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `rybo` | 1.71 | xor | ppu-stat |

### `sybe` (dffr) — diff=64.07, max=66.29
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 66.29 | nor2 | ppu-stat |
| `roku` | 4.98 | xor | ppu-stat |
| `toca` | 2.22 | not_x1 | ppu-stat |

### `tako` (dffr) — diff=64.07, max=66.29
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 66.29 | nor2 | ppu-stat |
| `tyge` | 3.69 | xor | ppu-stat |
| `toca` | 2.22 | not_x1 | ppu-stat |

### `tuhu` (dffr) — diff=64.07, max=66.29
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 66.29 | nor2 | ppu-stat |
| `toca` | 2.22 | not_x1 | ppu-stat |

### `xodu` (dffr) — diff=63.22, max=66.29
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 66.29 | nor2 | ppu-stat |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `xegy` | 3.07 | xor | ppu-stat |

### `xydo` (dffr) — diff=60.78, max=66.29
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 66.29 | nor2 | ppu-stat |
| `sacu` | 63.77 | or2 | ppu-cycles |
| `xora` | 5.51 | xor | ppu-stat |

### `raha` (drlatch_ee) — diff=57.76, max=57.76
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 57.76 | not_x1 | ppu-stat |
| `wane` | 53.84 | not_x1 | ppu-stat |
| `wesy` | 24.82 | not_x2 | ppu-stat |
| `bus:d7` | 0.0 |  | bus |

### `salo` (drlatch_ee) — diff=57.76, max=57.76
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 57.76 | not_x1 | ppu-stat |
| `wane` | 53.84 | not_x1 | ppu-stat |
| `wesy` | 24.82 | not_x2 | ppu-stat |
| `bus:d3` | 0.0 |  | bus |

### `sedy` (drlatch_ee) — diff=57.76, max=57.76
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 57.76 | not_x1 | ppu-stat |
| `wane` | 53.84 | not_x1 | ppu-stat |
| `wesy` | 24.82 | not_x2 | ppu-stat |
| `bus:d2` | 0.0 |  | bus |

### `sota` (drlatch_ee) — diff=57.76, max=57.76
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 57.76 | not_x1 | ppu-stat |
| `wane` | 53.84 | not_x1 | ppu-stat |
| `wesy` | 24.82 | not_x2 | ppu-stat |
| `bus:d4` | 0.0 |  | bus |

### `syry` (drlatch_ee) — diff=57.76, max=57.76
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 57.76 | not_x1 | ppu-stat |
| `wane` | 53.84 | not_x1 | ppu-stat |
| `wesy` | 24.82 | not_x2 | ppu-stat |
| `bus:d0` | 0.0 |  | bus |

### `vafa` (drlatch_ee) — diff=57.76, max=57.76
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 57.76 | not_x1 | ppu-stat |
| `wane` | 53.84 | not_x1 | ppu-stat |
| `wesy` | 24.82 | not_x2 | ppu-stat |
| `bus:d5` | 0.0 |  | bus |

### `vevo` (drlatch_ee) — diff=57.76, max=57.76
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 57.76 | not_x1 | ppu-stat |
| `wane` | 53.84 | not_x1 | ppu-stat |
| `wesy` | 24.82 | not_x2 | ppu-stat |
| `bus:d6` | 0.0 |  | bus |

### `vuce` (drlatch_ee) — diff=57.76, max=57.76
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 57.76 | not_x1 | ppu-stat |
| `wane` | 53.84 | not_x1 | ppu-stat |
| `wesy` | 24.82 | not_x2 | ppu-stat |
| `bus:d1` | 0.0 |  | bus |


## Sprite Pixel Shifter (32 races)

### `lefe` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `lela` | 32.29 | nand2 | ppu-objfifo |
| `lyde` | 31.77 | nand2 | ppu-objfifo |
| `maso` | 0.0 | dffsr | ppu-objfifo |

### `lesu` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `mame` | 32.87 | nand2 | ppu-objfifo |
| `lufy` | 32.07 | nand2 | ppu-objfifo |
| `lefe` | 0.0 | dffsr | ppu-objfifo |

### `maso` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `myto` | 32.85 | nand2 | ppu-objfifo |
| `mada` | 32.51 | nand2 | ppu-objfifo |
| `nuro` | 0.0 | dffsr | ppu-objfifo |

### `naty` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `myxa` | 31.8 | nand2 | ppu-objfifo |
| `majo` | 31.6 | nand2 | ppu-objfifo |
| `pefu` | 0.0 | dffsr | ppu-objfifo |

### `pefu` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `rusy` | 32.81 | nand2 | ppu-objfifo |
| `ruca` | 32.32 | nand2 | ppu-objfifo |
| `nylu` | 0.0 | dffsr | ppu-objfifo |

### `pyjo` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `rano` | 32.5 | nand2 | ppu-objfifo |
| `rehu` | 31.99 | nand2 | ppu-objfifo |
| `naty` | 0.0 | dffsr | ppu-objfifo |

### `vafo` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `tuxa` | 28.96 | nand2 | ppu-objfifo |
| `tupe` | 28.85 | nand2 | ppu-objfifo |
| `wora` | 0.0 | dffsr | ppu-objfifo |

### `vanu` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `tapo` | 29.06 | nand2 | ppu-objfifo |
| `taby` | 28.56 | nand2 | ppu-objfifo |
| `weba` | 0.0 | dffsr | ppu-objfifo |

### `vare` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `tyga` | 30.41 | nand2 | ppu-objfifo |
| `waxo` | 30.28 | nand2 | ppu-objfifo |
| `pyjo` | 0.0 | dffsr | ppu-objfifo |

### `vupy` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `teso` | 32.76 | nand2 | ppu-objfifo |
| `tula` | 32.38 | nand2 | ppu-objfifo |
| `vanu` | 0.0 | dffsr | ppu-objfifo |

### `weba` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `vume` | 32.74 | nand2 | ppu-objfifo |
| `xole` | 32.31 | nand2 | ppu-objfifo |
| `vare` | 0.0 | dffsr | ppu-objfifo |

### `wora` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `vaby` | 32.69 | nand2 | ppu-objfifo |
| `xexu` | 31.96 | nand2 | ppu-objfifo |
| `wyho` | 0.0 | dffsr | ppu-objfifo |

### `wufy` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `xyve` | 32.65 | nand2 | ppu-objfifo |
| `vune` | 32.42 | nand2 | ppu-objfifo |
| `vafo` | 0.0 | dffsr | ppu-objfifo |

### `wyho` (dffsr) — diff=63.77, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `vexu` | 30.99 | nand2 | ppu-objfifo |
| `xato` | 30.53 | nand2 | ppu-objfifo |
| `lesu` | 0.0 | dffsr | ppu-objfifo |

### `nuro` (dffsr) — diff=30.89, max=63.77
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 63.77 | or2 | ppu-cycles |
| `pabe` | 33.23 | nand2 | ppu-objfifo |
| `pyzu` | 32.88 | nand2 | ppu-objfifo |


## Window Logic (31 races)

### `wobo` (dffr) — diff=59.92, max=59.92
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 59.92 | not_x1 | ppu-cycles |
| `wody` | 0.0 | dffr | ppu-window |

### `wody` (dffr) — diff=59.92, max=59.92
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 59.92 | not_x1 | ppu-cycles |
| `wyka` | 0.0 | dffr | ppu-window |

### `wyko` (dffr) — diff=59.92, max=59.92
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 59.92 | not_x1 | ppu-cycles |
| `wobo` | 0.0 | dffr | ppu-window |

### `xolo` (dffr) — diff=59.92, max=59.92
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 59.92 | not_x1 | ppu-cycles |
| `wyko` | 0.0 | dffr | ppu-window |

### `mela` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 59.57 | not_x1 | ppu-window |
| `vefu` | 56.07 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d3` | 0.0 |  | bus |

### `nafu` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 59.57 | not_x1 | ppu-window |
| `vefu` | 56.07 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d7` | 0.0 |  | bus |

### `naga` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 59.57 | not_x1 | ppu-window |
| `vefu` | 56.07 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d2` | 0.0 |  | bus |

### `nene` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 59.57 | not_x1 | ppu-window |
| `vefu` | 56.07 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d5` | 0.0 |  | bus |

### `neso` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 59.57 | not_x1 | ppu-window |
| `vefu` | 56.07 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d0` | 0.0 |  | bus |

### `nuka` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 59.57 | not_x1 | ppu-window |
| `vefu` | 56.07 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d6` | 0.0 |  | bus |

### `nulo` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 59.57 | not_x1 | ppu-window |
| `vefu` | 56.07 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d4` | 0.0 |  | bus |

### `nyro` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 59.57 | not_x1 | ppu-window |
| `vefu` | 56.07 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d1` | 0.0 |  | bus |

### `meby` (drlatch_ee) — diff=58.67, max=58.67
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 58.67 | not_x1 | ppu-window |
| `voxu` | 55.39 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d3` | 0.0 |  | bus |

### `muvo` (drlatch_ee) — diff=58.67, max=58.67
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 58.67 | not_x1 | ppu-window |
| `voxu` | 55.39 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d6` | 0.0 |  | bus |

### `myce` (drlatch_ee) — diff=58.67, max=58.67
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 58.67 | not_x1 | ppu-window |
| `voxu` | 55.39 | not_x1 | ppu-window |
| `walu` | 25.83 | not_x2 | ppu-window |
| `bus:d5` | 0.0 |  | bus |


## PPU Control (8 races)

### `vyxe` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 59.57 | not_x1 | ppu-control |
| `xubo` | 54.83 | not_x1 | ppu-control |
| `xare` | 27.38 | not_x1 | ppu-control |
| `bus:d0` | 0.0 |  | bus |

### `wexu` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 59.57 | not_x1 | ppu-control |
| `xubo` | 54.83 | not_x1 | ppu-control |
| `xare` | 27.38 | not_x1 | ppu-control |
| `bus:d4` | 0.0 |  | bus |

### `woky` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 59.57 | not_x1 | ppu-control |
| `xubo` | 54.83 | not_x1 | ppu-control |
| `xare` | 27.38 | not_x1 | ppu-control |
| `bus:d6` | 0.0 |  | bus |

### `wymo` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 59.57 | not_x1 | ppu-control |
| `xubo` | 54.83 | not_x1 | ppu-control |
| `xare` | 27.38 | not_x1 | ppu-control |
| `bus:d5` | 0.0 |  | bus |

### `xafo` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 59.57 | not_x1 | ppu-control |
| `xubo` | 54.83 | not_x1 | ppu-control |
| `xare` | 27.38 | not_x1 | ppu-control |
| `bus:d3` | 0.0 |  | bus |

### `xona` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 59.57 | not_x1 | ppu-control |
| `xubo` | 54.83 | not_x1 | ppu-control |
| `xare` | 27.38 | not_x1 | ppu-control |
| `bus:d7` | 0.0 |  | bus |

### `xylo` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 59.57 | not_x1 | ppu-control |
| `xubo` | 54.83 | not_x1 | ppu-control |
| `xare` | 27.38 | not_x1 | ppu-control |
| `bus:d1` | 0.0 |  | bus |

### `xymo` (drlatch_ee) — diff=59.57, max=59.57
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 59.57 | not_x1 | ppu-control |
| `xubo` | 54.83 | not_x1 | ppu-control |
| `xare` | 27.38 | not_x1 | ppu-control |
| `bus:d2` | 0.0 |  | bus |


## BG Scrolling (16 races)

### `bake` (drlatch_ee) — diff=59.55, max=59.55
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 59.55 | not_x1 | ppu-bgscroll |
| `amun` | 54.63 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d7` | 0.0 |  | bus |

### `bemy` (drlatch_ee) — diff=59.55, max=59.55
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 59.55 | not_x1 | ppu-bgscroll |
| `amun` | 54.63 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d4` | 0.0 |  | bus |

### `cabu` (drlatch_ee) — diff=59.55, max=59.55
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 59.55 | not_x1 | ppu-bgscroll |
| `amun` | 54.63 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d6` | 0.0 |  | bus |

### `cuzy` (drlatch_ee) — diff=59.55, max=59.55
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 59.55 | not_x1 | ppu-bgscroll |
| `amun` | 54.63 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d5` | 0.0 |  | bus |

### `cyxu` (drlatch_ee) — diff=59.55, max=59.55
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 59.55 | not_x1 | ppu-bgscroll |
| `amun` | 54.63 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d2` | 0.0 |  | bus |

### `daty` (drlatch_ee) — diff=59.55, max=59.55
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 59.55 | not_x1 | ppu-bgscroll |
| `amun` | 54.63 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d0` | 0.0 |  | bus |

### `duzu` (drlatch_ee) — diff=59.55, max=59.55
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 59.55 | not_x1 | ppu-bgscroll |
| `amun` | 54.63 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d1` | 0.0 |  | bus |

### `gubo` (drlatch_ee) — diff=59.55, max=59.55
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 59.55 | not_x1 | ppu-bgscroll |
| `amun` | 54.63 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d3` | 0.0 |  | bus |

### `dede` (drlatch_ee) — diff=58.49, max=58.49
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 58.49 | not_x1 | ppu-bgscroll |
| `cavo` | 54.05 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d4` | 0.0 |  | bus |

### `fezu` (drlatch_ee) — diff=58.49, max=58.49
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 58.49 | not_x1 | ppu-bgscroll |
| `cavo` | 54.05 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d2` | 0.0 |  | bus |

### `foha` (drlatch_ee) — diff=58.49, max=58.49
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 58.49 | not_x1 | ppu-bgscroll |
| `cavo` | 54.05 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d6` | 0.0 |  | bus |

### `foty` (drlatch_ee) — diff=58.49, max=58.49
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 58.49 | not_x1 | ppu-bgscroll |
| `cavo` | 54.05 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d5` | 0.0 |  | bus |

### `fujo` (drlatch_ee) — diff=58.49, max=58.49
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 58.49 | not_x1 | ppu-bgscroll |
| `cavo` | 54.05 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d3` | 0.0 |  | bus |

### `funy` (drlatch_ee) — diff=58.49, max=58.49
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 58.49 | not_x1 | ppu-bgscroll |
| `cavo` | 54.05 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d7` | 0.0 |  | bus |

### `fymo` (drlatch_ee) — diff=58.49, max=58.49
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 58.49 | not_x1 | ppu-bgscroll |
| `cavo` | 54.05 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d1` | 0.0 |  | bus |


## Sprite X Priority (10 races)

### `cedy` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `enut` | 31.19 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `eboj` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `guva` | 34.17 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `egav` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `emol` | 31.98 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `exuq` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `foxa` | 44.56 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `fono` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `guze` | 52.44 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `gota` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `gyfy` | 34.73 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `wafy` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `gega` | 36.99 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `wapo` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `gutu` | 41.78 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `womy` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `xoja` | 40.23 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |

### `xudy` (dffr) — diff=48.7, max=58.38
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 58.38 | not_x1 | ppu-xprio |
| `gono` | 41.14 | nor2 | ppu-xprio |
| `wuty` | 9.68 | not_x2 | ppu-ycomp |


## LCD Output (18 races)

### `sude` (dffr) — diff=47.39, max=47.39
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 47.39 | nor2 | ppu-lcd |
| `telu` | 0.0 | dffr | ppu-lcd |

### `taha` (dffr) — diff=47.39, max=47.39
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 47.39 | nor2 | ppu-lcd |
| `sude` | 0.0 | dffr | ppu-lcd |

### `telu` (dffr) — diff=47.39, max=47.39
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 47.39 | nor2 | ppu-lcd |
| `vyzo` | 0.0 | dffr | ppu-lcd |

### `typo` (dffr) — diff=47.39, max=47.39
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 47.39 | nor2 | ppu-lcd |
| `saxo` | 0.0 | dffr | ppu-lcd |

### `tyry` (dffr) — diff=47.39, max=47.39
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 47.39 | nor2 | ppu-lcd |
| `taha` | 0.0 | dffr | ppu-lcd |

### `vyzo` (dffr) — diff=47.39, max=47.39
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 47.39 | nor2 | ppu-lcd |
| `typo` | 0.0 | dffr | ppu-lcd |

### `saxo` (dffr) — diff=45.98, max=47.39
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 47.39 | nor2 | ppu-lcd |
| `talu` | 1.41 | not_x4 | ppu-lcd |

### `meda` (dffr) — diff=43.72, max=43.72
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 43.72 | not_x1 | ppu-lcd |
| `neru` | 8.18 | nor8 | ppu-lcd |
| `nype` | 0.0 | dffr | ppu-lcd |

### `myta` (dffr) — diff=43.72, max=43.72
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 43.72 | not_x1 | ppu-lcd |
| `noko` | 2.48 | and4 | ppu-lcd |
| `nype` | 0.0 | dffr | ppu-lcd |

### `napo` (dffr) — diff=43.72, max=43.72
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 43.72 | not_x1 | ppu-lcd |
| `popu` | 0.0 | dffr | ppu-lcd |

### `nype` (dffr) — diff=43.72, max=43.72
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 43.72 | not_x1 | ppu-lcd |
| `talu` | 1.41 | not_x4 | ppu-lcd |
| `rutu` | 0.0 | dffr | ppu-lcd |

### `popu` (dffr) — diff=43.72, max=43.72
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 43.72 | not_x1 | ppu-lcd |
| `xyvo` | 8.37 | and2 | ppu-lcd |
| `nype` | 0.0 | dffr | ppu-lcd |

### `luca` (dffr) — diff=43.53, max=43.72
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 43.72 | not_x1 | ppu-lcd |
| `lofu` | 0.19 | not_x1 | ppu-lcd |

### `rutu` (dffr) — diff=41.28, max=43.72
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 43.72 | not_x1 | ppu-lcd |
| `sanu` | 3.25 | and4 | ppu-lcd |
| `sono` | 2.44 | not_x1 | ppu-lcd |

### `sygu` (dffr) — diff=41.28, max=43.72
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 43.72 | not_x1 | ppu-lcd |
| `tegy` | 7.93 | nand4 | ppu-lcd |
| `sono` | 2.44 | not_x1 | ppu-lcd |


## Boot ROM (1 races)

### `tepu` (dffr) — diff=40.33, max=42.16
Category: bootrom

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuge` | 42.16 | nand4 | bootrom |
| `alur` | 8.64 | not_x2 | clocks |
| `sato` | 1.83 | or2 | bootrom |


## Data Bus (16 races)

### `raxy` (dlatch) — diff=38.05, max=38.05
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 38.05 | nand3 | bus-data |
| `d2` | 0.0 | pad_bidir_pu | bus-data |

### `rony` (dlatch) — diff=38.05, max=38.05
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 38.05 | nand3 | bus-data |
| `d1` | 0.0 | pad_bidir_pu | bus-data |

### `rupa` (dlatch) — diff=38.05, max=38.05
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 38.05 | nand3 | bus-data |
| `d6` | 0.0 | pad_bidir_pu | bus-data |

### `sago` (dlatch) — diff=38.05, max=38.05
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 38.05 | nand3 | bus-data |
| `d5` | 0.0 | pad_bidir_pu | bus-data |

### `sazy` (dlatch) — diff=38.05, max=38.05
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 38.05 | nand3 | bus-data |
| `d7` | 0.0 | pad_bidir_pu | bus-data |

### `selo` (dlatch) — diff=38.05, max=38.05
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 38.05 | nand3 | bus-data |
| `d3` | 0.0 | pad_bidir_pu | bus-data |

### `sody` (dlatch) — diff=38.05, max=38.05
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 38.05 | nand3 | bus-data |
| `d4` | 0.0 | pad_bidir_pu | bus-data |

### `soma` (dlatch) — diff=38.05, max=38.05
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 38.05 | nand3 | bus-data |
| `d0` | 0.0 | pad_bidir_pu | bus-data |

### `d5` (pad_bidir_pu) — diff=11.56, max=58.65
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryvo` | 58.65 | nand2 | bus-data |
| `lula` | 56.13 | not_x1 | bus-data |
| `tamu` | 47.09 | nor2 | bus-data |

### `d7` (pad_bidir_pu) — diff=9.46, max=58.21
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ravu` | 58.21 | nand2 | bus-data |
| `lula` | 56.13 | not_x1 | bus-data |
| `ryda` | 48.75 | nor2 | bus-data |

### `d3` (pad_bidir_pu) — diff=8.47, max=60.94
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rera` | 60.94 | nand2 | bus-data |
| `lula` | 56.13 | not_x1 | bus-data |
| `seze` | 52.47 | nor2 | bus-data |

### `d0` (pad_bidir_pu) — diff=8.36, max=64.49
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruxa` | 64.49 | nand2 | bus-data |
| `rune` | 61.01 | nor2 | bus-data |
| `lula` | 56.13 | not_x1 | bus-data |

### `d4` (pad_bidir_pu) — diff=8.35, max=59.75
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rory` | 59.75 | nand2 | bus-data |
| `lula` | 56.13 | not_x1 | bus-data |
| `resy` | 51.4 | nor2 | bus-data |

### `d6` (pad_bidir_pu) — diff=8.09, max=59.46
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rafy` | 59.46 | nand2 | bus-data |
| `lula` | 56.13 | not_x1 | bus-data |
| `rogy` | 51.37 | nor2 | bus-data |

### `d2` (pad_bidir_pu) — diff=7.43, max=61.7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `raby` | 61.7 | nand2 | bus-data |
| `lula` | 56.13 | not_x1 | bus-data |
| `suly` | 54.27 | nor2 | bus-data |


## Address Bus (26 races)

### `alor` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a0` | 0.0 |  | bus |

### `alyr` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a2` | 0.0 |  | bus |

### `apur` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a1` | 0.0 |  | bus |

### `aret` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a3` | 0.0 |  | bus |

### `aros` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a6` | 0.0 |  | bus |

### `arym` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a7` | 0.0 |  | bus |

### `atev` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a5` | 0.0 |  | bus |

### `avys` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a4` | 0.0 |  | bus |

### `lobu` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a12` | 0.0 |  | bus |

### `lonu` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a13` | 0.0 |  | bus |

### `lumy` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a11` | 0.0 |  | bus |

### `luno` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a8` | 0.0 |  | bus |

### `lysa` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a9` | 0.0 |  | bus |

### `nyre` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a14` | 0.0 |  | bus |

### `pate` (dlatch) — diff=33.0, max=33.0
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a10` | 0.0 |  | bus |


## OAM Interface (3 races)

### `maka` (dffr) — diff=10.09, max=16.5
Category: ppu-oam

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cunu` | 16.5 | not_x2 | ppu-control |
| `zeme` | 8.87 | not_x4 | ppu-control |
| `caty` | 6.41 | not_x1 | ppu-oam |

### `xedy` (dffr_cc) — diff=5.47, max=14.09
Category: ppu-oam

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `yfoc` | 14.09 | not_x1 | ppu-oam |
| `wuda` | 10.4 | not_x2 | ppu-oam |
| `cyke` | 8.62 | not_x2 | ppu-oam |

### `xecu` (dffr_cc) — diff=4.06, max=12.68
Category: ppu-oam

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `yzet` | 12.68 | not_x1 | ppu-oam |
| `wuda` | 10.4 | not_x2 | ppu-oam |
| `cyke` | 8.62 | not_x2 | ppu-oam |


## VRAM Interface (7 races)

### `md4` (pad_bidir_pu) — diff=7.54, max=56.34
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rofa` | 56.34 | not_x2 | ppu-vram |
| `ryro` | 53.84 | not_x2 | ppu-vram |
| `rube` | 48.8 | not_x2 | ppu-vram |

### `md6` (pad_bidir_pu) — diff=7.52, max=56.34
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rofa` | 56.34 | not_x2 | ppu-vram |
| `reku` | 51.54 | not_x2 | ppu-vram |
| `ryty` | 48.82 | not_x2 | ppu-vram |

### `md5` (pad_bidir_pu) — diff=7.03, max=56.34
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rofa` | 56.34 | not_x2 | ppu-vram |
| `revu` | 52.62 | not_x2 | ppu-vram |
| `rumu` | 49.31 | not_x2 | ppu-vram |

### `md3` (pad_bidir_pu) — diff=6.87, max=56.34
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rofa` | 56.34 | not_x2 | ppu-vram |
| `rada` | 52.43 | not_x2 | ppu-vram |
| `rodu` | 49.47 | not_x2 | ppu-vram |

### `md7` (pad_bidir_pu) — diff=6.77, max=56.34
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rofa` | 56.34 | not_x2 | ppu-vram |
| `ryze` | 51.09 | not_x2 | ppu-vram |
| `rady` | 49.57 | not_x2 | ppu-vram |

### `md2` (pad_bidir_pu) — diff=6.55, max=56.34
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rofa` | 56.34 | not_x2 | ppu-vram |
| `razo` | 53.04 | not_x2 | ppu-vram |
| `rare` | 49.79 | not_x2 | ppu-vram |

### `md1` (pad_bidir_pu) — diff=4.91, max=56.34
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rofa` | 56.34 | not_x2 | ppu-vram |
| `ryky` | 53.91 | not_x2 | ppu-vram |
| `ruly` | 51.43 | not_x2 | ppu-vram |
