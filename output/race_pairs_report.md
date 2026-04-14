# Signal Race Pair Analysis

Total race pairs identified: 869

Race pairs are registered nodes where data inputs arrive at significantly
different combinatorial depths (diff >= 3 gates, max >= 4). On real hardware,
the late-arriving signal may not settle before the register samples, causing
behavior to differ from behavioral emulation by one dot.

PPU-related races: 462


## apu-ch1 (83 races)

### `cyto` (nor_latch) — diff=30, max=30
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bery` | 30 | or4 | apu-ch1 |
| `feku` | 0 | dffr | apu-ch1 |

### `hyka` (dffsr) — diff=26, max=31
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 31 | and2 | apu-ch1 |
| `efor` | 16 | nor2 | apu-ch1 |
| `gylu` | 14 | nand2 | apu-ch1 |
| `guxa` | 5 | full_add | apu-ch1 |

### `hyxu` (dffsr) — diff=23, max=31
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 31 | and2 | apu-ch1 |
| `eluf` | 16 | nor2 | apu-ch1 |
| `eler` | 14 | nand2 | apu-ch1 |
| `fego` | 8 | full_add | apu-ch1 |

### `jyka` (dffsr) — diff=22, max=31
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 31 | and2 | apu-ch1 |
| `gato` | 16 | nor2 | apu-ch1 |
| `geta` | 14 | nand2 | apu-ch1 |
| `halu` | 9 | full_add | apu-ch1 |

### `hopo` (dffsr) — diff=19, max=31
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 31 | and2 | apu-ch1 |
| `esel` | 16 | nor2 | apu-ch1 |
| `etol` | 14 | nand2 | apu-ch1 |
| `etek` | 12 | full_add | apu-ch1 |

### `havo` (dffsr) — diff=18, max=31
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 31 | and2 | apu-ch1 |
| `gyfu` | 16 | nor2 | apu-ch1 |
| `golo` | 14 | nand2 | apu-ch1 |
| `jule` | 13 | full_add | apu-ch1 |

### `fely` (dffsr) — diff=17, max=31
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 31 | and2 | apu-ch1 |
| `kapo` | 16 | nor2 | apu-ch1 |
| `kovu` | 14 | nand2 | apu-ch1 |

### `edul` (dffsr) — diff=17, max=31
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 31 | and2 | apu-ch1 |
| `jory` | 17 | full_add | apu-ch1 |
| `gamo` | 16 | nor2 | apu-ch1 |
| `gope` | 14 | nand2 | apu-ch1 |

### `dygy` (dffsr) — diff=15, max=29
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 29 | and3 | apu-ch1 |
| `boxu` | 16 | nor2 | apu-ch1 |
| `dyxe` | 16 | full_add | apu-ch1 |
| `bugu` | 14 | nand2 | apu-ch1 |

### `evab` (dffsr) — diff=15, max=29
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 29 | and3 | apu-ch1 |
| `dule` | 20 | full_add | apu-ch1 |
| `bovu` | 16 | nor2 | apu-ch1 |
| `budo` | 14 | nand2 | apu-ch1 |

### `axan` (dffsr) — diff=15, max=29
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 29 | and3 | apu-ch1 |
| `coru` | 24 | full_add | apu-ch1 |
| `apaj` | 16 | nor2 | apu-ch1 |
| `afeg` | 14 | nand2 | apu-ch1 |

### `boko` (drlatch_ee) — diff=15, max=15
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bamu` | 15 | not_x1 | apu-ch1 |
| `bage` | 14 | nand2 | apu-ch1 |
| `camy` | 9 | not_x1 | apu-ch1 |
| `bus:d6` | 0 |  | bus |

### `avaf` (drlatch_ee) — diff=14, max=14
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 14 | not_x2 | apu-ch1 |
| `cenu` | 13 | and2 | apu-ch1 |
| `agur` | 9 | not_x1 | apu-control |
| `bus:d3` | 0 |  | bus |

### `anaz` (drlatch_ee) — diff=14, max=14
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 14 | not_x2 | apu-ch1 |
| `cenu` | 13 | and2 | apu-ch1 |
| `agur` | 9 | not_x1 | apu-control |
| `bus:d2` | 0 |  | bus |

### `arax` (drlatch_ee) — diff=14, max=14
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 14 | not_x2 | apu-ch1 |
| `cenu` | 13 | and2 | apu-ch1 |
| `agur` | 9 | not_x1 | apu-control |
| `bus:d1` | 0 |  | bus |


## Sprite Store (99 races)

### `bozu` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `doby` | 28 | not_x1 | ppu-objctl |
| `enob` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |

### `fyhy` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `doby` | 28 | not_x1 | ppu-objctl |
| `enob` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store0` | 0 |  | bus |

### `cufo` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `doby` | 28 | not_x1 | ppu-objctl |
| `enob` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `gyho` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `doby` | 28 | not_x1 | ppu-objctl |
| `enob` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store3` | 0 |  | bus |

### `ygus` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xuxa` | 28 | not_x1 | ppu-objctl |
| `geny` | 27 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0 |  | bus |

### `azap` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byno` | 28 | not_x1 | ppu-objctl |
| `bymy` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store0` | 0 |  | bus |

### `afyx` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byno` | 28 | not_x1 | ppu-objctl |
| `bymy` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `afym` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byno` | 28 | not_x1 | ppu-objctl |
| `bymy` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store3` | 0 |  | bus |

### `afut` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byno` | 28 | not_x1 | ppu-objctl |
| `bymy` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |

### `byhe` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `avoz` | 28 | not_x1 | ppu-objreg |
| `akol` | 27 | not_x1 | ppu-objctl |
| `bus:oam_render_a2` | 0 |  | bus |

### `axuv` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `avoz` | 28 | not_x1 | ppu-objreg |
| `akol` | 27 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0 |  | bus |

### `abug` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bydy` | 28 | not_x1 | ppu-objctl |
| `ahof` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store3` | 0 |  | bus |

### `ames` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bydy` | 28 | not_x1 | ppu-objctl |
| `ahof` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store0` | 0 |  | bus |

### `arof` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bydy` | 28 | not_x1 | ppu-objctl |
| `ahof` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `abop` (dlatch_ee) — diff=28, max=28
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bydy` | 28 | not_x1 | ppu-objctl |
| `ahof` | 27 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |


## bus (42 races)

### `bus:~ma9` () — diff=27, max=32
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dafe` | 32 | not_if0 | ppu-bgscroll |
| `vulo` | 9 | not_if0 | ppu-window |
| `rese` | 7 | not_if0 | ppu-vram |
| `duve` | 6 | not_if0 | ppu-dma |
| `gotu` | 6 | not_if0 | ppu-ycomp |
| `reso` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma4` () — diff=27, max=32
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ajan` | 32 | not_if0 | ppu-bgscroll |
| `wuju` | 9 | not_if0 | ppu-window |
| `xeca` | 7 | not_if0 | ppu-vram |
| `famu` | 7 | not_if0 | ppu-ycomp |
| `damu` | 6 | not_if0 | ppu-dma |
| `vapy` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma8` () — diff=23, max=28
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ceta` | 28 | not_if0 | ppu-bgscroll |
| `vovo` | 9 | not_if0 | ppu-window |
| `rysu` | 7 | not_if0 | ppu-vram |
| `evax` | 6 | not_if0 | ppu-dma |
| `wune` | 6 | not_if0 | ppu-ycomp |
| `roha` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma3` () — diff=22, max=28
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `coly` | 28 | not_if0 | ppu-bgscroll |
| `dode` | 12 | not_if0 | ppu-bgscroll |
| `xulo` | 9 | not_if0 | ppu-window |
| `xody` | 7 | not_if0 | ppu-vram |
| `wolu` | 6 | not_if0 | ppu-window |
| `agag` | 6 | not_if0 | ppu-ycomp |
| `fyzy` | 6 | not_if0 | ppu-dma |

### `bus:~ma7` () — diff=19, max=24
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cypo` | 24 | not_if0 | ppu-bgscroll |
| `vace` | 9 | not_if0 | ppu-window |
| `xybo` | 7 | not_if0 | ppu-vram |
| `erew` | 6 | not_if0 | ppu-dma |
| `wyga` | 6 | not_if0 | ppu-ycomp |
| `rusa` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma2` () — diff=18, max=24
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `alel` | 24 | not_if0 | ppu-bgscroll |
| `xahe` | 9 | not_if0 | ppu-window |
| `dahu` | 8 | not_if0 | ppu-bgscroll |
| `xyne` | 7 | not_if0 | ppu-vram |
| `wawe` | 6 | not_if0 | ppu-window |
| `aras` | 6 | not_if0 | ppu-ycomp |
| `fuhe` | 6 | not_if0 | ppu-dma |

### `bus:d3` () — diff=17, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `asuz` | 18 | not_if0 |  |
| `taxo` | 17 | buf_if0 | bus-data |
| `rase` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `fose` | 1 | not_if0 | apu-ch2 |

### `bus:d7` () — diff=17, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `beda` | 18 | not_if0 |  |
| `tewa` | 17 | buf_if0 | bus-data |
| `raru` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `gazo` | 1 | not_if0 | apu-ch2 |

### `bus:d6` () — diff=17, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `arar` | 18 | not_if0 |  |
| `tazu` | 17 | buf_if0 | bus-data |
| `ryke` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `goje` | 1 | not_if0 | apu-ch1 |

### `bus:d1` () — diff=16, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataj` | 18 | not_if0 |  |
| `sosa` | 17 | buf_if0 | bus-data |
| `ryne` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `efus` | 2 | not_if0 | apu-control |

### `bus:d2` () — diff=16, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ajec` | 18 | not_if0 |  |
| `sedu` | 17 | buf_if0 | bus-data |
| `rejy` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `baty` | 2 | not_if1 | apu-ch3 |

### `bus:d4` () — diff=16, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `benu` | 18 | not_if0 |  |
| `tahy` | 17 | buf_if0 | bus-data |
| `reka` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `xuna` | 2 | buf_if0 | ppu-xcomp |

### `bus:~ma6` () — diff=15, max=20
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `case` | 20 | not_if0 | ppu-bgscroll |
| `veha` | 9 | not_if0 | ppu-window |
| `xopo` | 7 | not_if0 | ppu-vram |
| `eteg` | 6 | not_if0 | ppu-dma |
| `gavo` | 6 | not_if0 | ppu-ycomp |
| `vejy` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma1` () — diff=14, max=20
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `afeb` | 20 | not_if0 | ppu-bgscroll |
| `xamo` | 9 | not_if0 | ppu-window |
| `evad` | 8 | not_if0 | ppu-bgscroll |
| `xuxu` | 7 | not_if0 | ppu-vram |
| `wudo` | 6 | not_if0 | ppu-window |
| `baxe` | 6 | not_if0 | ppu-ycomp |
| `egez` | 6 | not_if0 | ppu-dma |

### `bus:d0` () — diff=14, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anoc` | 18 | not_if0 |  |
| `tovu` | 17 | buf_if0 | bus-data |
| `romy` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |


## Sprite X Match (110 races)

### `welo` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gery` | 28 | not_x1 | ppu-objctl |
| `fuxu` | 27 | not_x1 | ppu-objctl |
| `dyna` | 21 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `xuny` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gery` | 28 | not_x1 | ppu-objctl |
| `fuxu` | 27 | not_x1 | ppu-objctl |
| `dyna` | 21 | not_x1 | ppu-xprio |
| `arop` | 1 | not_x1 | ppu-xcomp |

### `yrop` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 28 | not_x1 | ppu-objctl |
| `weme` | 27 | not_x1 | ppu-objctl |
| `dosy` | 3 | not_x1 | ppu-xprio |
| `arop` | 1 | not_x1 | ppu-xcomp |

### `xako` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gery` | 28 | not_x1 | ppu-objctl |
| `fuxu` | 27 | not_x1 | ppu-objctl |
| `dyna` | 21 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `yzof` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 28 | not_x1 | ppu-objctl |
| `weme` | 27 | not_x1 | ppu-objctl |
| `dosy` | 3 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `ynep` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 28 | not_x1 | ppu-objctl |
| `weme` | 27 | not_x1 | ppu-objctl |
| `dosy` | 3 | not_x1 | ppu-xprio |
| `xatu` | 1 | not_x1 | ppu-xcomp |

### `wote` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gery` | 28 | not_x1 | ppu-objctl |
| `fuxu` | 27 | not_x1 | ppu-objctl |
| `dyna` | 21 | not_x1 | ppu-xprio |
| `xatu` | 1 | not_x1 | ppu-xcomp |

### `xuzo` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 28 | not_x1 | ppu-objctl |
| `weme` | 27 | not_x1 | ppu-objctl |
| `dosy` | 3 | not_x1 | ppu-xprio |
| `ypur` | 1 | not_x1 | ppu-xcomp |

### `zola` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gery` | 28 | not_x1 | ppu-objctl |
| `fuxu` | 27 | not_x1 | ppu-objctl |
| `dyna` | 21 | not_x1 | ppu-xprio |
| `ypur` | 1 | not_x1 | ppu-xcomp |

### `xexa` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 28 | not_x1 | ppu-objctl |
| `weme` | 27 | not_x1 | ppu-objctl |
| `dosy` | 3 | not_x1 | ppu-xprio |
| `yvok` | 1 | not_x1 | ppu-xcomp |

### `zulu` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gery` | 28 | not_x1 | ppu-objctl |
| `fuxu` | 27 | not_x1 | ppu-objctl |
| `dyna` | 21 | not_x1 | ppu-xprio |
| `yvok` | 1 | not_x1 | ppu-xcomp |

### `ylah` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gery` | 28 | not_x1 | ppu-objctl |
| `fuxu` | 27 | not_x1 | ppu-objctl |
| `dyna` | 21 | not_x1 | ppu-xprio |
| `zocy` | 1 | not_x1 | ppu-xcomp |

### `xere` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 28 | not_x1 | ppu-objctl |
| `weme` | 27 | not_x1 | ppu-objctl |
| `dosy` | 3 | not_x1 | ppu-xprio |
| `zocy` | 1 | not_x1 | ppu-xcomp |

### `eraz` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `deha` | 28 | not_x1 | ppu-objctl |
| `gecy` | 27 | not_x1 | ppu-objctl |
| `zago` | 1 | not_x1 | ppu-xcomp |

### `wedu` (drlatch_ee) — diff=27, max=28
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `weva` | 28 | not_x1 | ppu-objctl |
| `wofo` | 27 | not_x1 | ppu-objctl |
| `zago` | 1 | not_x1 | ppu-xcomp |


## Sprite Control (15 races)

### `besu` (nor_latch) — diff=21, max=21
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `asen` | 21 | or2 | ppu-objctl |
| `catu` | 0 | dffr | ppu-objctl |

### `dezy` (dffr) — diff=17, max=23
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyty` | 23 | not_x2 | ppu-objctl |
| `xapo` | 9 | not_x2 | ppu-control |
| `zeme` | 6 | not_x4 | ppu-control |

### `doba` (dffr) — diff=17, max=17
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bagy` | 17 | not_x1 | ppu-objctl |
| `alet` | 7 | not_x2 | ppu-control |
| `byba` | 0 | dffr | ppu-objctl |

### `byba` (dffr) — diff=16, max=17
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bagy` | 17 | not_x1 | ppu-objctl |
| `feto` | 2 | and4 | ppu-objctl |
| `xupy` | 1 | not_x2 | ppu-oam |

### `goso` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `wewy` | 0 | dffr | ppu-objctl |

### `dybe` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `bego` | 0 | dffr | ppu-objctl |

### `elyn` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `goso` | 0 | dffr | ppu-objctl |

### `faha` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `elyn` | 0 | dffr | ppu-objctl |

### `fony` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `faha` | 0 | dffr | ppu-objctl |

### `cuxy` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `bese` | 0 | dffr | ppu-objctl |

### `bese` (dffr) — diff=11, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `cake` | 4 | or2 | ppu-objctl |

### `yfel` (dffr) — diff=11, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `gava` | 4 | or2 | ppu-objctl |

### `anel` (dffr) — diff=11, max=11
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `abez` | 11 | not_x1 | ppu-objctl |
| `awoh` | 2 | not_x1 | ppu-objctl |
| `catu` | 0 | dffr | ppu-objctl |

### `ceno` (dffr) — diff=11, max=11
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `abez` | 11 | not_x1 | ppu-objctl |
| `xupy` | 1 | not_x2 | ppu-oam |
| `besu` | 0 | nor_latch | ppu-objctl |

### `catu` (dffr) — diff=10, max=11
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `abez` | 11 | not_x1 | ppu-objctl |
| `abov` | 5 | and2 | ppu-objctl |
| `xupy` | 1 | not_x2 | ppu-oam |


## Sprite X Priority (9 races)

### `exuq` (dffr) — diff=20, max=24
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `foxa` | 24 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `wapo` (dffr) — diff=18, max=22
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gutu` | 22 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `womy` (dffr) — diff=16, max=20
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xoja` | 20 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `wafy` (dffr) — diff=14, max=18
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gega` | 18 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `eboj` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `guva` | 7 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `cedy` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `enut` | 10 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `egav` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `emol` | 12 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `gota` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `gyfy` | 14 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `xudy` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `gono` | 16 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |


## BG/Win Cycles (16 races)

### `paho` (dffr) — diff=18, max=18
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roxo` | 18 | not_x1 | ppu-cycles |
| `xydo` | 0 | dffr | ppu-stat |
| `xymu` | 0 | nor_latch | ppu-stat |

### `ryfa` (dffr) — diff=17, max=17
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `segu` | 17 | not_x4 | ppu-cycles |
| `pany` | 8 | nor2 | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `nopa` (dffr) — diff=9, max=9
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xapo` | 9 | not_x2 | ppu-control |
| `alet` | 7 | not_x2 | ppu-control |
| `pynu` | 0 | nor_latch | ppu-cycles |

### `nunu` (dffr) — diff=8, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mehe` | 8 | not_x1 | ppu-cycles |
| `pyco` | 0 | dffr | ppu-cycles |

### `nyze` (dffr) — diff=8, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `moxe` | 8 | not_x1 | ppu-cycles |
| `puxa` | 0 | dffr | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `pory` (dffr) — diff=8, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myvo` | 8 | not_x1 | ppu-cycles |
| `nafy` | 5 | nor2 | ppu-cycles |
| `nyka` | 0 | dffr | ppu-cycles |

### `lyzu` (dffr) — diff=7, max=7
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `alet` | 7 | not_x2 | ppu-control |
| `laxu` | 0 | dffr | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `pygo` (dffr) — diff=7, max=7
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `alet` | 7 | not_x2 | ppu-control |
| `pory` | 0 | dffr | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `rene` (dffr) — diff=7, max=7
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `alet` | 7 | not_x2 | ppu-control |
| `ryfa` | 0 | dffr | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `mesu` (dffr) — diff=5, max=5
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 5 | nor3 | ppu-cycles |
| `laxu` | 0 | dffr | ppu-cycles |

### `nyva` (dffr) — diff=5, max=5
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 5 | nor3 | ppu-cycles |
| `mesu` | 0 | dffr | ppu-cycles |

### `rubu` (dffr) — diff=5, max=5
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 5 | nor2 | ppu-cycles |
| `roga` | 0 | dffr | ppu-cycles |

### `sovy` (dffr) — diff=4, max=11
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rydy` | 11 | nor3 | ppu-cycles |
| `xapo` | 9 | not_x2 | ppu-control |
| `alet` | 7 | not_x2 | ppu-control |

### `lovy` (dffr) — diff=3, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myvo` | 8 | not_x1 | ppu-cycles |
| `lyry` | 7 | not_x1 | ppu-cycles |
| `nyxu` | 5 | nor3 | ppu-cycles |

### `ryku` (dffr) — diff=3, max=5
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 5 | nor2 | ppu-cycles |
| `pecu` | 2 | nand2 | ppu-cycles |


## Window Logic (30 races)

### `wody` (dffr) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 17 | not_x1 | ppu-cycles |
| `wyka` | 0 | dffr | ppu-window |

### `wobo` (dffr) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 17 | not_x1 | ppu-cycles |
| `wody` | 0 | dffr | ppu-window |

### `wyko` (dffr) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 17 | not_x1 | ppu-cycles |
| `wobo` | 0 | dffr | ppu-window |

### `xolo` (dffr) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 17 | not_x1 | ppu-cycles |
| `wyko` | 0 | dffr | ppu-window |

### `meby` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d3` | 0 |  | bus |

### `mypu` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d4` | 0 |  | bus |

### `nofe` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d1` | 0 |  | bus |

### `noke` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d2` | 0 |  | bus |

### `myce` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d5` | 0 |  | bus |

### `mypa` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d0` | 0 |  | bus |

### `muvo` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d6` | 0 |  | bus |

### `mela` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 15 | not_x1 | ppu-window |
| `vefu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d3` | 0 |  | bus |

### `nuka` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 15 | not_x1 | ppu-window |
| `vefu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d6` | 0 |  | bus |

### `nene` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 15 | not_x1 | ppu-window |
| `vefu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d5` | 0 |  | bus |

### `nulo` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 15 | not_x1 | ppu-window |
| `vefu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d4` | 0 |  | bus |


## STAT/LY (31 races)

### `rupo` (nor_latch) — diff=16, max=16
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pago` | 16 | or2 | ppu-stat |
| `ropo` | 0 | dffr | ppu-stat |

### `refe` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 15 | not_x1 | ppu-stat |
| `ryve` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d5` | 0 |  | bus |

### `roxe` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 15 | not_x1 | ppu-stat |
| `ryve` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d3` | 0 |  | bus |

### `rugu` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 15 | not_x1 | ppu-stat |
| `ryve` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d6` | 0 |  | bus |

### `rufo` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 15 | not_x1 | ppu-stat |
| `ryve` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d4` | 0 |  | bus |

### `sedy` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d2` | 0 |  | bus |

### `sota` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d4` | 0 |  | bus |

### `vuce` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d1` | 0 |  | bus |

### `vevo` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d6` | 0 |  | bus |

### `raha` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d7` | 0 |  | bus |

### `syry` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d0` | 0 |  | bus |

### `salo` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d3` | 0 |  | bus |

### `vafa` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d5` | 0 |  | bus |

### `tako` (dffr) — diff=14, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 15 | nor2 | ppu-stat |
| `toca` | 1 | not_x1 | ppu-stat |

### `tuky` (dffr) — diff=14, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 15 | nor2 | ppu-stat |
| `toca` | 1 | not_x1 | ppu-stat |


## DMA (19 races)

### `nygy` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d4` | 0 |  | bus |

### `nydo` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d3` | 0 |  | bus |

### `nafa` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d0` | 0 |  | bus |

### `pyne` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d1` | 0 |  | bus |

### `para` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d2` | 0 |  | bus |

### `maru` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d7` | 0 |  | bus |

### `wuje` (nor_latch) — diff=10, max=13
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xuto` | 13 | and2 | ppu-oam |
| `xyny` | 3 | not_x1 | ppu-dma |

### `lyxe` (nor_latch) — diff=7, max=13
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavy` | 13 | and2 | ppu-dma |
| `loko` | 6 | nand2 | ppu-dma |

### `pyro` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `naky` | 0 | dffr | ppu-dma |

### `nefy` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `pyro` | 0 | dffr | ppu-dma |

### `muty` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `nefy` | 0 | dffr | ppu-dma |

### `nyko` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `muty` | 0 | dffr | ppu-dma |

### `pylo` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `nyko` | 0 | dffr | ppu-dma |

### `nuto` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `pylo` | 0 | dffr | ppu-dma |

### `mugu` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `nuto` | 0 | dffr | ppu-dma |


## PPU Control (8 races)

### `xylo` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `xafo` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d3` | 0 |  | bus |

### `wymo` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d5` | 0 |  | bus |

### `xona` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d7` | 0 |  | bus |

### `xymo` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d2` | 0 |  | bus |

### `woky` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `vyxe` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d0` | 0 |  | bus |

### `wexu` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d4` | 0 |  | bus |


## BG Scrolling (16 races)

### `bake` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d7` | 0 |  | bus |

### `duzu` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `cyxu` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d2` | 0 |  | bus |

### `bemy` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d4` | 0 |  | bus |

### `cuzy` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d5` | 0 |  | bus |

### `cabu` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `daty` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d0` | 0 |  | bus |

### `gubo` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d3` | 0 |  | bus |

### `gave` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d0` | 0 |  | bus |

### `fymo` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `dede` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d4` | 0 |  | bus |

### `funy` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d7` | 0 |  | bus |

### `fezu` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d2` | 0 |  | bus |

### `foha` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `foty` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d5` | 0 |  | bus |


## Palettes (24 races)

### `moru` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d5` | 0 |  | bus |

### `muke` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d4` | 0 |  | bus |

### `nusy` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d1` | 0 |  | bus |

### `pylu` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d2` | 0 |  | bus |

### `mogy` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d6` | 0 |  | bus |

### `pavo` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d0` | 0 |  | bus |

### `maxy` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d3` | 0 |  | bus |

### `mena` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d7` | 0 |  | bus |

### `luxo` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 15 | not_x1 | ppu-pal |
| `leho` | 14 | not_x1 | ppu-pal |
| `bus:d7` | 0 |  | bus |

### `lawo` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 15 | not_x1 | ppu-pal |
| `leho` | 14 | not_x1 | ppu-pal |
| `bus:d1` | 0 |  | bus |

### `lune` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 15 | not_x1 | ppu-pal |
| `leho` | 14 | not_x1 | ppu-pal |
| `bus:d4` | 0 |  | bus |

### `lugu` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 15 | not_x1 | ppu-pal |
| `leho` | 14 | not_x1 | ppu-pal |
| `bus:d5` | 0 |  | bus |

### `lose` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 15 | not_x1 | ppu-pal |
| `leho` | 14 | not_x1 | ppu-pal |
| `bus:d3` | 0 |  | bus |

### `lepu` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 15 | not_x1 | ppu-pal |
| `leho` | 14 | not_x1 | ppu-pal |
| `bus:d6` | 0 |  | bus |

### `moxy` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 15 | not_x1 | ppu-pal |
| `leho` | 14 | not_x1 | ppu-pal |
| `bus:d0` | 0 |  | bus |


## Other (4 races)

### `high_ram` (high_ram) — diff=15, max=15
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wuly` | 15 | not_x2 | hram |
| `abev` | 13 | not_x2 | hram |
| `apuh` | 11 | not_x2 | hram |
| `anyk` | 10 | not_x1 | hram |
| `apow` | 9 | not_x2 | hram |
| `wuta` | 4 | not_x2 | hram |
| `ajom` | 3 | and2 | hram |
| `axyc` | 3 | and2 | hram |
| `avub` | 3 | and2 | hram |
| `apul` | 2 | and2 | hram |
| `weju` | 1 | not_x1 | hram |
| `wady` | 1 | not_x1 | hram |
| `woce` | 1 | not_x1 | hram |
| `webe` | 1 | not_x1 | hram |
| `wehu` | 1 | not_x1 | hram |
| `bus:a6` | 0 |  | bus |
| `bus:a5` | 0 |  | bus |
| `bus:a4` | 0 |  | bus |
| `bus:a3` | 0 |  | bus |
| `bus:a2` | 0 |  | bus |

### `boot_rom` (boot_rom) — diff=12, max=12
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zoku` | 12 | not_x1 | bootrom |
| `zery` | 11 | not_x1 | bootrom |
| `zyro` | 4 | not_x1 | bootrom |
| `zefu` | 4 | not_x1 | bootrom |
| `zete` | 4 | not_x1 | bootrom |
| `zapa` | 3 | not_x1 | bootrom |
| `zovy` | 3 | and2 | bootrom |
| `zyga` | 3 | and2 | bootrom |
| `zyky` | 3 | and2 | bootrom |
| `zuko` | 2 | and2 | bootrom |
| `zoke` | 1 | not_x1 | bootrom |
| `zabu` | 1 | not_x1 | bootrom |
| `zage` | 1 | not_x1 | bootrom |
| `zyra` | 1 | not_x1 | bootrom |
| `bus:a7` | 0 |  | bus |
| `bus:a6` | 0 |  | bus |
| `bus:a3` | 0 |  | bus |
| `bus:a2` | 0 |  | bus |

### `wave_ram` (wave_ram) — diff=6, max=6
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ygef` | 6 | and2 | apu-ch3 |
| `bus:d0` | 0 |  | bus |
| `bus:d1` | 0 |  | bus |
| `bus:d3` | 0 |  | bus |

### `oam_a` (oam) — diff=3, max=4
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxy` | 4 | and2 | ppu-oam |
| `wuca` | 2 | not_x1 | ppu-oam |
| `yzet` | 1 | not_x1 | ppu-oam |


## apu-ch2 (44 races)

### `emer` (drlatch_ee) — diff=15, max=15
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `duso` | 15 | not_x1 | apu-ch2 |
| `evyf` | 14 | nand2 | apu-ch2 |
| `fazo` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |

### `fora` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d4` | 0 |  | bus |

### `gupu` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 14 | not_x1 | apu-ch2 |
| `exuc` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d7` | 0 |  | bus |

### `gumy` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 14 | not_x1 | apu-ch2 |
| `exuc` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |

### `fova` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d1` | 0 |  | bus |

### `fome` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d3` | 0 |  | bus |

### `fedy` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d2` | 0 |  | bus |

### `goda` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 14 | not_x1 | apu-ch2 |
| `exuc` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d5` | 0 |  | bus |

### `jany` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kysa` | 14 | not_x1 | apu-ch2 |
| `jenu` | 13 | and2 | apu-ch2 |
| `kypu` | 9 | not_x1 | apu-ch2 |
| `bus:d1` | 0 |  | bus |

### `jefu` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kysa` | 14 | not_x1 | apu-ch2 |
| `jenu` | 13 | and2 | apu-ch2 |
| `kypu` | 9 | not_x1 | apu-ch2 |
| `bus:d0` | 0 |  | bus |

### `gura` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |

### `gata` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d4` | 0 |  | bus |

### `hyfu` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `jede` | 14 | not_x1 | apu-ch2 |
| `gere` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d0` | 0 |  | bus |

### `hava` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `jede` | 14 | not_x1 | apu-ch2 |
| `gere` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d2` | 0 |  | bus |

### `gufe` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d5` | 0 |  | bus |


## apu-ch3 (44 races)

### `hoto` (drlatch_ee) — diff=15, max=15
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gygu` | 15 | not_x1 | apu-ch3 |
| `fovo` | 14 | nand2 | apu-ch3 |
| `heky` | 9 | not_x1 | apu-ch3 |
| `bus:d6` | 0 |  | bus |

### `guxe` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gucy` | 14 | not_x1 | apu-ch3 |
| `gejo` | 13 | and2 | apu-ch3 |
| `gove` | 9 | not_x1 | apu-ch3 |
| `bus:d7` | 0 |  | bus |

### `huky` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guzu` | 14 | not_x1 | apu-ch3 |
| `haga` | 13 | and2 | apu-ch3 |
| `guro` | 9 | not_x1 | apu-ch3 |
| `bus:d6` | 0 |  | bus |

### `hody` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guzu` | 14 | not_x1 | apu-ch3 |
| `haga` | 13 | and2 | apu-ch3 |
| `guro` | 9 | not_x1 | apu-ch3 |
| `bus:d5` | 0 |  | bus |

### `gage` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d7` | 0 |  | bus |

### `jety` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 14 | not_x1 | apu-ch3 |
| `huda` | 13 | and2 | apu-ch3 |
| `kopy` | 9 | not_x1 | apu-ch3 |
| `bus:d1` | 0 |  | bus |

### `jacy` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 14 | not_x1 | apu-ch3 |
| `huda` | 13 | and2 | apu-ch3 |
| `kopy` | 9 | not_x1 | apu-ch3 |
| `bus:d2` | 0 |  | bus |

### `jemo` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 14 | not_x1 | apu-ch3 |
| `huda` | 13 | and2 | apu-ch3 |
| `kopy` | 9 | not_x1 | apu-ch3 |
| `bus:d0` | 0 |  | bus |

### `kogu` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 14 | not_x1 | apu-ch3 |
| `kota` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d7` | 0 |  | bus |

### `jypo` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d4` | 0 |  | bus |

### `koga` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d0` | 0 |  | bus |

### `kana` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 14 | not_x1 | apu-ch3 |
| `kota` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d6` | 0 |  | bus |

### `jefe` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d3` | 0 |  | bus |

### `jove` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 14 | not_x1 | apu-ch3 |
| `kota` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d5` | 0 |  | bus |

### `jaxa` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d2` | 0 |  | bus |


## apu-ch4 (67 races)

### `cuny` (drlatch_ee) — diff=15, max=15
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cazo` | 15 | not_x1 | apu-ch4 |
| `dulu` | 14 | nand2 | apu-ch4 |
| `cabe` | 9 | not_x1 | apu-ch4 |
| `bus:d6` | 0 |  | bus |

### `feta` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 14 | not_x2 | apu-ch4 |
| `getu` | 13 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d4` | 0 |  | bus |

### `fyto` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 14 | not_x2 | apu-ch4 |
| `getu` | 13 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d5` | 0 |  | bus |

### `gafo` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 14 | not_x2 | apu-ch4 |
| `getu` | 13 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d7` | 0 |  | bus |

### `gogo` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 14 | not_x2 | apu-ch4 |
| `getu` | 13 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d6` | 0 |  | bus |

### `jare` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 14 | not_x2 | apu-ch4 |
| `humo` | 13 | and2 | apu-ch4 |
| `kame` | 9 | not_x1 | apu-control |
| `bus:d0` | 0 |  | bus |

### `jaky` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 14 | not_x2 | apu-ch4 |
| `humo` | 13 | and2 | apu-ch4 |
| `kame` | 9 | not_x1 | apu-control |
| `bus:d2` | 0 |  | bus |

### `jero` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 14 | not_x2 | apu-ch4 |
| `humo` | 13 | and2 | apu-ch4 |
| `kame` | 9 | not_x1 | apu-control |
| `bus:d1` | 0 |  | bus |

### `geky` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 14 | not_x2 | apu-ch4 |
| `goko` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d3` | 0 |  | bus |

### `emok` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 14 | not_x1 | apu-ch4 |
| `daco` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d0` | 0 |  | bus |

### `goky` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 14 | not_x2 | apu-ch4 |
| `goko` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d5` | 0 |  | bus |

### `etyj` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 14 | not_x1 | apu-ch4 |
| `daco` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d1` | 0 |  | bus |

### `ezyk` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 14 | not_x1 | apu-ch4 |
| `daco` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d2` | 0 |  | bus |

### `gozo` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 14 | not_x2 | apu-ch4 |
| `goko` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d6` | 0 |  | bus |

### `gedu` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 14 | not_x2 | apu-ch4 |
| `goko` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d7` | 0 |  | bus |


## Interrupts (10 races)

### `ubul` (dffsr) — diff=14, max=14
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuny` | 14 | and3 | int |
| `tome` | 12 | nand3 | int |
| `caly` | 0 | dffr | serial |

### `nybo` (dffsr) — diff=14, max=14
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pyga` | 14 | and3 | int |
| `pyhu` | 12 | nand3 | int |
| `moba` | 0 | dffr | timer |

### `ulak` (dffsr) — diff=12, max=14
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyme` | 14 | and3 | int |
| `toga` | 12 | nand3 | int |
| `asok` | 2 | and2 | joypad |

### `lope` (dffsr) — diff=11, max=14
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyta` | 14 | and3 | int |
| `myzu` | 12 | nand3 | int |
| `vypu` | 3 | not_x3 | ppu-stat |

### `nejy` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `ubul` | 0 | dffsr | int |

### `nuty` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `ulak` | 0 | dffsr | int |

### `pavy` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `nybo` | 0 | dffsr | int |

### `maty` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `lope` | 0 | dffsr | int |

### `mopo` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `lalu` | 0 | dffsr | int |

### `lalu` (dffsr) — diff=6, max=18
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voty` | 18 | not_x3 | ppu-stat |
| `movu` | 14 | and3 | int |
| `mody` | 12 | nand3 | int |


## apu-control (27 races)

### `bofa` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 14 | not_x2 | apu-control |
| `byfa` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d5` | 0 |  | bus |

### `bedu` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 14 | not_x2 | apu-control |
| `baxy` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d7` | 0 |  | bus |

### `bafo` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 14 | not_x2 | apu-control |
| `bono` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d2` | 0 |  | bus |

### `befo` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 14 | not_x2 | apu-control |
| `byfa` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d6` | 0 |  | bus |

### `bumo` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 14 | not_x2 | apu-control |
| `baxy` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d5` | 0 |  | bus |

### `cozu` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 14 | not_x2 | apu-control |
| `baxy` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d6` | 0 |  | bus |

### `atuf` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 14 | not_x2 | apu-control |
| `bono` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d3` | 0 |  | bus |

### `byga` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 14 | not_x2 | apu-control |
| `bowe` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d1` | 0 |  | bus |

### `byre` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 14 | not_x2 | apu-control |
| `baxy` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d4` | 0 |  | bus |

### `anev` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 14 | not_x2 | apu-control |
| `bono` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d0` | 0 |  | bus |

### `ager` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 14 | not_x2 | apu-control |
| `bowe` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d2` | 0 |  | bus |

### `apos` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 14 | not_x2 | apu-control |
| `bowe` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d3` | 0 |  | bus |

### `bepu` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 14 | not_x2 | apu-control |
| `byfa` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d7` | 0 |  | bus |

### `bogu` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 14 | not_x2 | apu-control |
| `bono` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d1` | 0 |  | bus |

### `bume` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 14 | not_x2 | apu-control |
| `byfa` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d4` | 0 |  | bus |


## Timer (20 races)

### `peda` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pyma` | 13 | nor2 | timer |
| `rage` | 0 | tffnl | timer |

### `nuga` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pagu` | 13 | nor2 | timer |
| `peda` | 0 | tffnl | timer |

### `povy` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 13 | nand3 | timer |
| `nero` | 13 | nor2 | timer |
| `rega` | 0 | tffnl | timer |

### `peru` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 13 | nand3 | timer |
| `nada` | 13 | nor2 | timer |
| `povy` | 0 | tffnl | timer |

### `rate` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 13 | nand3 | timer |
| `repa` | 13 | nor2 | timer |
| `peru` | 0 | tffnl | timer |

### `ruby` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 13 | nand3 | timer |
| `rolu` | 13 | nor2 | timer |
| `rate` | 0 | tffnl | timer |

### `muru` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d2` | 0 |  | bus |

### `tyva` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d3` | 0 |  | bus |

### `tyru` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d4` | 0 |  | bus |

### `sabu` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `seta` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d7` | 0 |  | bus |

### `nyke` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |

### `peto` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d6` | 0 |  | bus |

### `sufy` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d5` | 0 |  | bus |

### `samy` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sara` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |


## Sprite Y Compare (20 races)

### `zaxe` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d4` | 0 |  | bus |

### `xafu` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d5` | 0 |  | bus |

### `wone` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d3` | 0 |  | bus |

### `yses` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d6` | 0 |  | bus |

### `zeca` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d7` | 0 |  | bus |

### `yceb` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d1` | 0 |  | bus |

### `zuca` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d2` | 0 |  | bus |

### `ybog` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `zaxe` | 0 | dlatch | ppu-ycomp |

### `wyso` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `xafu` | 0 | dlatch | ppu-ycomp |

### `xyju` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `wone` | 0 | dlatch | ppu-ycomp |

### `xote` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `yses` | 0 | dlatch | ppu-ycomp |

### `yzab` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `zeca` | 0 | dlatch | ppu-ycomp |

### `xegu` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `yceb` | 0 | dlatch | ppu-ycomp |

### `yjex` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `zuca` | 0 | dlatch | ppu-ycomp |

### `tobu` (dffr) — diff=9, max=9
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tava` | 9 | not_x1 | ppu-ycomp |
| `tuly` | 0 | dffr | ppu-ycomp |
| `xymu` | 0 | nor_latch | ppu-stat |


## Serial (14 races)

### `caly` (dffr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 12 | and2 | serial |
| `cyde` | 0 | dffr | serial |

### `cylo` (dffr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 12 | and2 | serial |
| `cafa` | 0 | dffr | serial |

### `degu` (dffsr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dumo` | 12 | oa21 | serial |
| `docu` | 12 | nand2 | serial |
| `dawe` | 6 | not_x2 | serial |
| `cuba` | 0 | dffsr | serial |

### `dyra` (dffsr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dybo` | 12 | oa21 | serial |
| `dela` | 12 | nand2 | serial |
| `dawe` | 6 | not_x2 | serial |
| `degu` | 0 | dffsr | serial |

### `dojo` (dffsr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `daju` | 12 | oa21 | serial |
| `dyge` | 12 | nand2 | serial |
| `dawe` | 6 | not_x2 | serial |
| `dyra` | 0 | dffsr | serial |

### `dovu` (dffsr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyly` | 12 | oa21 | serial |
| `dola` | 12 | nand2 | serial |
| `epyt` | 4 | not_x2 | serial |
| `dojo` | 0 | dffsr | serial |

### `ejab` (dffsr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehuj` | 12 | oa21 | serial |
| `elok` | 12 | nand2 | serial |
| `epyt` | 4 | not_x2 | serial |
| `dovu` | 0 | dffsr | serial |

### `erod` (dffsr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efak` | 12 | oa21 | serial |
| `edel` | 12 | nand2 | serial |
| `epyt` | 4 | not_x2 | serial |
| `ejab` | 0 | dffsr | serial |

### `eder` (dffsr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `eguv` | 12 | oa21 | serial |
| `efef` | 12 | nand2 | serial |
| `epyt` | 4 | not_x2 | serial |
| `erod` | 0 | dffsr | serial |

### `cuba` (dffsr) — diff=11, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cohy` | 12 | oa21 | serial |
| `cufu` | 12 | nand2 | serial |
| `dawe` | 6 | not_x2 | serial |
| `cage` | 1 | not_x1 | serial |

### `cafa` (dffr) — diff=10, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 12 | and2 | serial |
| `dawa` | 2 | or2 | serial |

### `culy` (dffr) — diff=10, max=10
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 10 | nand4 | serial |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `etaf` (dffr) — diff=10, max=10
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 10 | nand4 | serial |
| `caby` | 5 | and2 | serial |
| `bus:d7` | 0 |  | bus |

### `coty` (dffr) — diff=9, max=10
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 10 | nand4 | serial |
| `uvyn` | 1 | not_x1 | clocks |


## Clock Distribution (10 races)

### `ufor` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `ukup` | 0 | dffr | clocks |

### `uner` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `ufor` | 0 | dffr | clocks |

### `tero` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `uner` | 0 | dffr | clocks |

### `unyk` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `tero` | 0 | dffr | clocks |

### `tama` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `unyk` | 0 | dffr | clocks |

### `afer` (dffr_cc) — diff=11, max=11
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boma` | 11 | not_x6 | clocks |
| `boga` | 10 | not_x6 | clocks |
| `upoj` | 2 | nand3 | test |
| `asol` | 0 | nor_latch | clocks |

### `apuk` (drlatch_ee) — diff=4, max=4
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `adeh` | 4 | not_x1 | clocks |
| `atal` | 3 | not_x2 | clocks |
| `upoj` | 2 | nand3 | test |
| `alef` | 0 | drlatch_ee | clocks |

### `adyk` (drlatch_ee) — diff=4, max=4
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `adeh` | 4 | not_x1 | clocks |
| `atal` | 3 | not_x2 | clocks |
| `upoj` | 2 | nand3 | test |
| `apuk` | 0 | drlatch_ee | clocks |

### `afur` (drlatch_ee) — diff=4, max=4
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `adeh` | 4 | not_x1 | clocks |
| `atal` | 3 | not_x2 | clocks |
| `upoj` | 2 | nand3 | test |
| `adyk` | 0 | drlatch_ee | clocks |

### `tubo` (nor_latch) — diff=3, max=7
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `upyf` | 7 | or2 | clocks |
| `cpu` | 4 | sm83 |  |


## LCD Output (17 races)

### `typo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `saxo` | 0 | dffr | ppu-lcd |

### `vyzo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `typo` | 0 | dffr | ppu-lcd |

### `telu` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `vyzo` | 0 | dffr | ppu-lcd |

### `sude` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `telu` | 0 | dffr | ppu-lcd |

### `taha` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `sude` | 0 | dffr | ppu-lcd |

### `tyry` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `taha` | 0 | dffr | ppu-lcd |

### `nype` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `talu` | 1 | not_x4 | ppu-lcd |
| `rutu` | 0 | dffr | ppu-lcd |

### `myta` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `noko` | 2 | and4 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `popu` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `xyvo` | 2 | and2 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `meda` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `neru` | 1 | nor8 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `napo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `popu` | 0 | dffr | ppu-lcd |

### `saxo` (dffr) — diff=10, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `talu` | 1 | not_x4 | ppu-lcd |

### `luca` (dffr) — diff=10, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `lofu` | 1 | not_x1 | ppu-lcd |

### `rutu` (dffr) — diff=9, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `sono` | 2 | not_x1 | ppu-lcd |
| `sanu` | 2 | and4 | ppu-lcd |

### `sygu` (dffr) — diff=9, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `tegy` | 3 | nand4 | ppu-lcd |
| `sono` | 2 | not_x1 | ppu-lcd |


## Address Bus (14 races)

### `lonu` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a13` | 0 |  | bus |

### `nyre` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a14` | 0 |  | bus |

### `alor` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a0` | 0 |  | bus |

### `pate` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a10` | 0 |  | bus |

### `lumy` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a11` | 0 |  | bus |

### `lysa` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a9` | 0 |  | bus |

### `luno` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a8` | 0 |  | bus |

### `apur` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a1` | 0 |  | bus |

### `alyr` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a2` | 0 |  | bus |

### `aret` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a3` | 0 |  | bus |

### `avys` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a4` | 0 |  | bus |

### `atev` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a5` | 0 |  | bus |

### `aros` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a6` | 0 |  | bus |

### `arym` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a7` | 0 |  | bus |


## test (8 races)

### `amut` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 10 | nand5 | test |
| `bus:d1` | 0 |  | bus |

### `buro` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 10 | nand5 | test |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `kecy` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |

### `kuko` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d6` | 0 |  | bus |

### `keru` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d7` | 0 |  | bus |

### `kyme` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d3` | 0 |  | bus |

### `jute` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `jale` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d2` | 0 |  | bus |


## Joypad (11 races)

### `kely` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d4` | 0 |  | bus |

### `cofy` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d5` | 0 |  | bus |

### `kapa` (dlatch) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 10 | not_x1 | joypad |
| `p11` | 0 | pad_bidir_pu | joypad |

### `kolo` (dlatch) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 10 | not_x1 | joypad |
| `p13` | 0 | pad_bidir_pu | joypad |

### `kevu` (dlatch) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 10 | not_x1 | joypad |
| `p10` | 0 | pad_bidir_pu | joypad |

### `keja` (dlatch) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 10 | not_x1 | joypad |
| `p12` | 0 | pad_bidir_pu | joypad |

### `acef` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `batu` | 0 | dffr | joypad |

### `agem` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `acef` | 0 | dffr | joypad |

### `apug` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `agem` | 0 | dffr | joypad |

### `awob` (dlatch) — diff=8, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `kery` | 2 | or4 | joypad |

### `batu` (dffr) — diff=8, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `kery` | 2 | or4 | joypad |


## Sprite Pixel Shifter (8 races)

### `pefu` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rusy` | 9 | nand2 | ppu-objfifo |
| `ruca` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nylu` | 0 | dffsr | ppu-objfifo |

### `naty` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myxa` | 9 | nand2 | ppu-objfifo |
| `majo` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `pefu` | 0 | dffsr | ppu-objfifo |

### `lesu` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lufy` | 9 | nand2 | ppu-objfifo |
| `mame` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `lefe` | 0 | dffsr | ppu-objfifo |

### `vare` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyga` | 9 | nand2 | ppu-objfifo |
| `waxo` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `pyjo` | 0 | dffsr | ppu-objfifo |

### `weba` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `vume` | 9 | nand2 | ppu-objfifo |
| `xole` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `vare` | 0 | dffsr | ppu-objfifo |

### `vanu` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `taby` | 9 | nand2 | ppu-objfifo |
| `tapo` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `weba` | 0 | dffsr | ppu-objfifo |

### `vupy` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `teso` | 9 | nand2 | ppu-objfifo |
| `tula` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `vanu` | 0 | dffsr | ppu-objfifo |

### `nylu` (dffsr) — diff=7, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mezu` | 9 | nand2 | ppu-objfifo |
| `mofy` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |


## bootrom (1 races)

### `tepu` (dffr) — diff=7, max=10
Category: bootrom

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuge` | 10 | nand4 | bootrom |
| `alur` | 3 | not_x2 | clocks |


## Data Bus (8 races)

### `raxy` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d2` | 0 | pad_bidir_pu | bus-data |

### `sody` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d4` | 0 | pad_bidir_pu | bus-data |

### `rony` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d1` | 0 | pad_bidir_pu | bus-data |

### `soma` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d0` | 0 | pad_bidir_pu | bus-data |

### `rupa` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d6` | 0 | pad_bidir_pu | bus-data |

### `sago` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d5` | 0 | pad_bidir_pu | bus-data |

### `sazy` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d7` | 0 | pad_bidir_pu | bus-data |

### `selo` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d3` | 0 | pad_bidir_pu | bus-data |


## BG Pixel Shifter (32 races)

### `pozo` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md1` | 0 |  | bus |

### `pyzo` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md2` | 0 |  | bus |

### `pyju` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md7` | 0 |  | bus |

### `poju` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md5` | 0 |  | bus |

### `pulo` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md4` | 0 |  | bus |

### `powy` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md6` | 0 |  | bus |

### `rawu` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md0` | 0 |  | bus |

### `poxa` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md3` | 0 |  | bus |

### `taca` (dffsr) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `seno` | 7 | nand2 | ppu-bgfifo |
| `soly` | 7 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `tomy` | 0 | dffsr | ppu-bgfifo |

### `nozo` (dffsr) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nexa` | 7 | nand2 | ppu-bgfifo |
| `nyxo` | 7 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `myde` | 0 | dffsr | ppu-bgfifo |

### `sady` (dffsr) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruce` | 7 | nand2 | ppu-bgfifo |
| `sure` | 7 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `taca` | 0 | dffsr | ppu-bgfifo |

### `moju` (dffsr) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lutu` | 7 | nand2 | ppu-bgfifo |
| `loto` | 7 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nozo` | 0 | dffsr | ppu-bgfifo |

### `rysa` (dffsr) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryja` | 7 | nand2 | ppu-bgfifo |
| `sebo` | 7 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `sady` | 0 | dffsr | ppu-bgfifo |

### `macu` (dffsr) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lydu` | 7 | nand2 | ppu-bgfifo |
| `luja` | 7 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `moju` | 0 | dffsr | ppu-bgfifo |

### `sobo` (dffsr) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruto` | 7 | nand2 | ppu-bgfifo |
| `suca` | 7 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `rysa` | 0 | dffsr | ppu-bgfifo |


## OAM Interface (1 races)

### `maka` (dffr) — diff=4, max=6
Category: ppu-oam

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zeme` | 6 | not_x4 | ppu-control |
| `cunu` | 5 | not_x2 | ppu-control |
| `caty` | 2 | not_x1 | ppu-oam |


## VRAM Interface (7 races)

### `md1` (pad_bidir_pu) — diff=3, max=26
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryky` | 26 | not_x2 | ppu-vram |
| `rofa` | 23 | not_x2 | ppu-vram |

### `md2` (pad_bidir_pu) — diff=3, max=26
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `razo` | 26 | not_x2 | ppu-vram |
| `rofa` | 23 | not_x2 | ppu-vram |

### `md4` (pad_bidir_pu) — diff=3, max=26
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryro` | 26 | not_x2 | ppu-vram |
| `rofa` | 23 | not_x2 | ppu-vram |

### `md6` (pad_bidir_pu) — diff=3, max=26
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `reku` | 26 | not_x2 | ppu-vram |
| `ryty` | 25 | not_x2 | ppu-vram |
| `rofa` | 23 | not_x2 | ppu-vram |

### `md3` (pad_bidir_pu) — diff=3, max=26
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rada` | 26 | not_x2 | ppu-vram |
| `rodu` | 25 | not_x2 | ppu-vram |
| `rofa` | 23 | not_x2 | ppu-vram |

### `md5` (pad_bidir_pu) — diff=3, max=26
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `revu` | 26 | not_x2 | ppu-vram |
| `rumu` | 25 | not_x2 | ppu-vram |
| `rofa` | 23 | not_x2 | ppu-vram |

### `md0` (pad_bidir_pu) — diff=3, max=26
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rege` | 26 | not_x2 | ppu-vram |
| `rura` | 25 | not_x2 | ppu-vram |
| `rofa` | 23 | not_x2 | ppu-vram |
