# Signal Race Pair Analysis

Total race pairs identified: 975

Race pairs are registered nodes where data inputs arrive at significantly
different combinatorial depths (diff >= 3 gates, max >= 4). On real hardware,
the late-arriving signal may not settle before the register samples, causing
behavior to differ from behavioral emulation by one dot.

PPU-related races: 491


## apu-ch1 (102 races)

### `cyto` (nor_latch) — diff=51, max=51
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bery` | 51 | or4 | apu-ch1 |
| `feku` | 0 | dffr | apu-ch1 |

### `hyka` (dffsr) — diff=47, max=52
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 52 | and2 | apu-ch1 |
| `efor` | 18 | nor2 | apu-ch1 |
| `gylu` | 16 | nand2 | apu-ch1 |
| `guxa` | 5 | full_add | apu-ch1 |

### `jyka` (dffsr) — diff=43, max=52
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 52 | and2 | apu-ch1 |
| `gato` | 18 | nor2 | apu-ch1 |
| `geta` | 16 | nand2 | apu-ch1 |
| `halu` | 9 | full_add | apu-ch1 |

### `havo` (dffsr) — diff=39, max=52
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 52 | and2 | apu-ch1 |
| `gyfu` | 18 | nor2 | apu-ch1 |
| `golo` | 16 | nand2 | apu-ch1 |
| `jule` | 13 | full_add | apu-ch1 |

### `edul` (dffsr) — diff=36, max=52
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 52 | and2 | apu-ch1 |
| `gamo` | 18 | nor2 | apu-ch1 |
| `jory` | 17 | full_add | apu-ch1 |
| `gope` | 16 | nand2 | apu-ch1 |

### `fely` (dffsr) — diff=36, max=52
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 52 | and2 | apu-ch1 |
| `hexo` | 21 | full_add | apu-ch1 |
| `kapo` | 18 | nor2 | apu-ch1 |
| `kovu` | 16 | nand2 | apu-ch1 |

### `hyxu` (dffsr) — diff=36, max=52
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 52 | and2 | apu-ch1 |
| `fego` | 29 | full_add | apu-ch1 |
| `eluf` | 18 | nor2 | apu-ch1 |
| `eler` | 16 | nand2 | apu-ch1 |

### `hopo` (dffsr) — diff=36, max=52
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 52 | and2 | apu-ch1 |
| `etek` | 33 | full_add | apu-ch1 |
| `esel` | 18 | nor2 | apu-ch1 |
| `etol` | 16 | nand2 | apu-ch1 |

### `holu` (dffsr) — diff=36, max=52
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 52 | and2 | apu-ch1 |
| `geva` | 25 | full_add | apu-ch1 |
| `kaju` | 18 | nor2 | apu-ch1 |
| `kypa` | 16 | nand2 | apu-ch1 |

### `axan` (dffsr) — diff=34, max=50
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 50 | and3 | apu-ch1 |
| `coru` | 45 | full_add | apu-ch1 |
| `apaj` | 18 | nor2 | apu-ch1 |
| `afeg` | 16 | nand2 | apu-ch1 |

### `dygy` (dffsr) — diff=34, max=50
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 50 | and3 | apu-ch1 |
| `dyxe` | 37 | full_add | apu-ch1 |
| `boxu` | 18 | nor2 | apu-ch1 |
| `bugu` | 16 | nand2 | apu-ch1 |

### `evab` (dffsr) — diff=34, max=50
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 50 | and3 | apu-ch1 |
| `dule` | 41 | full_add | apu-ch1 |
| `bovu` | 18 | nor2 | apu-ch1 |
| `budo` | 16 | nand2 | apu-ch1 |

### `boko` (drlatch_ee) — diff=17, max=17
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bamu` | 17 | not_x1 | apu-ch1 |
| `bage` | 16 | nand2 | apu-ch1 |
| `camy` | 9 | not_x1 | apu-ch1 |
| `bus:d6` | 0 |  | bus |

### `adek` (drlatch_ee) — diff=16, max=16
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 16 | not_x2 | apu-ch1 |
| `cenu` | 15 | and2 | apu-ch1 |
| `agur` | 9 | not_x1 | apu-control |
| `bus:d4` | 0 |  | bus |

### `avaf` (drlatch_ee) — diff=16, max=16
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 16 | not_x2 | apu-ch1 |
| `cenu` | 15 | and2 | apu-ch1 |
| `agur` | 9 | not_x1 | apu-control |
| `bus:d3` | 0 |  | bus |


## Sprite Store (100 races)

### `apev` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `avoz` | 44 | not_x1 | ppu-objreg |
| `akol` | 43 | not_x1 | ppu-objctl |
| `bus:oam_render_a5` | 0 |  | bus |

### `axuv` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `avoz` | 44 | not_x1 | ppu-objreg |
| `akol` | 43 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0 |  | bus |

### `arof` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bydy` | 44 | not_x1 | ppu-objctl |
| `ahof` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `abop` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bydy` | 44 | not_x1 | ppu-objctl |
| `ahof` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |

### `ames` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bydy` | 44 | not_x1 | ppu-objctl |
| `ahof` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store0` | 0 |  | bus |

### `abug` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bydy` | 44 | not_x1 | ppu-objctl |
| `ahof` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store3` | 0 |  | bus |

### `afut` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byno` | 44 | not_x1 | ppu-objctl |
| `bymy` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |

### `afym` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byno` | 44 | not_x1 | ppu-objctl |
| `bymy` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store3` | 0 |  | bus |

### `azap` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byno` | 44 | not_x1 | ppu-objctl |
| `bymy` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store0` | 0 |  | bus |

### `afyx` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byno` | 44 | not_x1 | ppu-objctl |
| `bymy` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `aned` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bejy` | 44 | not_x1 | ppu-objctl |
| `bucy` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store3` | 0 |  | bus |

### `acep` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bejy` | 44 | not_x1 | ppu-objctl |
| `bucy` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store0` | 0 |  | bus |

### `abeg` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bejy` | 44 | not_x1 | ppu-objctl |
| `bucy` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `abux` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bejy` | 44 | not_x1 | ppu-objctl |
| `bucy` | 43 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |

### `buna` (dlatch_ee) — diff=44, max=44
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `beke` | 44 | not_x1 | ppu-objctl |
| `buzy` | 43 | not_x1 | ppu-objctl |
| `bus:oam_render_a6` | 0 |  | bus |


## Sprite X Match (112 races)

### `cusy` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 21 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `ceso` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 21 | not_x1 | ppu-xprio |
| `arop` | 1 | not_x1 | ppu-xcomp |

### `cywe` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `exyr` | 44 | not_x1 | ppu-objctl |
| `cyla` | 43 | not_x1 | ppu-objctl |
| `ejad` | 21 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `cuvy` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `exyr` | 44 | not_x1 | ppu-objctl |
| `cyla` | 43 | not_x1 | ppu-objctl |
| `ejad` | 21 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `dake` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 21 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `dyfu` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 21 | not_x1 | ppu-xprio |
| `xatu` | 1 | not_x1 | ppu-xcomp |

### `dazo` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 21 | not_x1 | ppu-xprio |
| `yvok` | 1 | not_x1 | ppu-xcomp |

### `dury` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `exyr` | 44 | not_x1 | ppu-objctl |
| `cyla` | 43 | not_x1 | ppu-objctl |
| `ejad` | 21 | not_x1 | ppu-xprio |
| `xatu` | 1 | not_x1 | ppu-xcomp |

### `desu` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 21 | not_x1 | ppu-xprio |
| `ypur` | 1 | not_x1 | ppu-xcomp |

### `duko` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 21 | not_x1 | ppu-xprio |
| `zocy` | 1 | not_x1 | ppu-xcomp |

### `dany` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 21 | not_x1 | ppu-xprio |
| `zago` | 1 | not_x1 | ppu-xcomp |

### `dyby` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `exyr` | 44 | not_x1 | ppu-objctl |
| `cyla` | 43 | not_x1 | ppu-objctl |
| `ejad` | 21 | not_x1 | ppu-xprio |
| `arop` | 1 | not_x1 | ppu-xcomp |

### `depy` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 44 | not_x1 | ppu-objctl |
| `cacu` | 43 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `duhy` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 44 | not_x1 | ppu-objctl |
| `cacu` | 43 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `epum` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `deha` | 44 | not_x1 | ppu-objctl |
| `gecy` | 43 | not_x1 | ppu-objctl |
| `gafy` | 21 | not_x1 | ppu-xprio |
| `zocy` | 1 | not_x1 | ppu-xcomp |


## Sprite Control (17 races)

### `dezy` (dffr) — diff=33, max=39
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyty` | 39 | not_x2 | ppu-objctl |
| `xapo` | 9 | not_x2 | ppu-control |
| `zeme` | 6 | not_x4 | ppu-control |

### `besu` (nor_latch) — diff=21, max=21
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `asen` | 21 | or2 | ppu-objctl |
| `catu` | 0 | dffr | ppu-objctl |

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

### `bego` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `cuxy` | 0 | dffr | ppu-objctl |

### `cuxy` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `bese` | 0 | dffr | ppu-objctl |

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

### `fony` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `faha` | 0 | dffr | ppu-objctl |

### `faha` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `elyn` | 0 | dffr | ppu-objctl |

### `goso` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `wewy` | 0 | dffr | ppu-objctl |

### `wewy` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `yfel` | 0 | dffr | ppu-objctl |

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


## Other (5 races)

### `wave_ram` (wave_ram) — diff=32, max=32
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ymul` | 32 | or2 | apu-ch3 |
| `yrar` | 24 | not_x1 | apu-ch3 |
| `ydez` | 17 | not_x1 | apu-ch3 |
| `ygef` | 7 | and2 | apu-ch3 |
| `yfux` | 7 | and2 | apu-ch3 |
| `yvop` | 7 | and2 | apu-ch3 |
| `yjej` | 6 | and2 | apu-ch3 |
| `ynur` | 5 | not_x1 | apu-ch3 |
| `yzeg` | 5 | not_x1 | apu-ch3 |
| `afum` | 4 | mux | apu-ch3 |
| `axol` | 4 | mux | apu-ch3 |
| `bus:d0` | 0 |  | bus |
| `bus:d1` | 0 |  | bus |
| `bus:d2` | 0 |  | bus |
| `bus:d3` | 0 |  | bus |
| `bus:d4` | 0 |  | bus |
| `bus:d5` | 0 |  | bus |
| `bus:d6` | 0 |  | bus |
| `bus:d7` | 0 |  | bus |

### `oam_a` (oam) — diff=25, max=26
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wame` | 26 | not_x2 | ppu-oam |
| `wory` | 25 | not_x2 | ppu-oam |
| `wejy` | 25 | not_x2 | ppu-oam |
| `wahe` | 23 | not_x3 | ppu-oam |
| `wovu` | 10 | not_x2 | ppu-oam |
| `wafa` | 4 | and2 | ppu-oam |
| `wyxy` | 4 | and2 | ppu-oam |
| `wexe` | 4 | and2 | ppu-oam |
| `wazu` | 3 | and2 | ppu-oam |
| `wuca` | 2 | not_x1 | ppu-oam |
| `wade` | 2 | not_x1 | ppu-oam |
| `woso` | 2 | not_x1 | ppu-oam |
| `wawy` | 2 | not_x1 | ppu-oam |
| `wadu` | 2 | not_x1 | ppu-oam |
| `xemu` | 1 | not_x1 | ppu-oam |
| `yfoc` | 1 | not_x1 | ppu-oam |
| `yzet` | 1 | not_x1 | ppu-oam |
| `ymev` | 1 | not_x1 | ppu-oam |
| `yvom` | 1 | not_x1 | ppu-oam |

### `oam_b` (oam) — diff=25, max=26
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wame` | 26 | not_x2 | ppu-oam |
| `wory` | 25 | not_x2 | ppu-oam |
| `wexa` | 25 | not_x2 | ppu-oam |
| `wahe` | 23 | not_x3 | ppu-oam |
| `wovu` | 10 | not_x2 | ppu-oam |
| `wafa` | 4 | and2 | ppu-oam |
| `wyxy` | 4 | and2 | ppu-oam |
| `wexe` | 4 | and2 | ppu-oam |
| `wazu` | 3 | and2 | ppu-oam |
| `wuca` | 2 | not_x1 | ppu-oam |
| `wade` | 2 | not_x1 | ppu-oam |
| `woso` | 2 | not_x1 | ppu-oam |
| `wawy` | 2 | not_x1 | ppu-oam |
| `wadu` | 2 | not_x1 | ppu-oam |
| `xemu` | 1 | not_x1 | ppu-oam |
| `yfoc` | 1 | not_x1 | ppu-oam |
| `yzet` | 1 | not_x1 | ppu-oam |
| `ymev` | 1 | not_x1 | ppu-oam |
| `yvom` | 1 | not_x1 | ppu-oam |

### `high_ram` (high_ram) — diff=17, max=17
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wuly` | 17 | not_x2 | hram |
| `abev` | 15 | not_x2 | hram |
| `apuh` | 13 | not_x2 | hram |
| `anyk` | 12 | not_x1 | hram |
| `apow` | 11 | not_x2 | hram |
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

### `boot_rom` (boot_rom) — diff=14, max=14
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zoku` | 14 | not_x1 | bootrom |
| `zery` | 13 | not_x1 | bootrom |
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


## bus (55 races)

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
| `famu` | 7 | not_if0 | ppu-ycomp |
| `xeca` | 7 | not_if0 | ppu-vram |
| `damu` | 6 | not_if0 | ppu-dma |
| `vapy` | 5 | not_if1 | ppu-bgfifo |

### `bus:oam_render_a2` () — diff=26, max=29
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zaro` | 29 | not_if0 | ppu-objreg |
| `apoc` | 27 | not_if0 | ppu-objreg |
| `wako` | 25 | not_if0 | ppu-objreg |
| `wato` | 23 | not_if0 | ppu-objreg |
| `dobo` | 21 | not_if0 | ppu-objreg |
| `wuxu` | 19 | not_if0 | ppu-objreg |
| `enap` | 17 | not_if0 | ppu-objreg |
| `cube` | 15 | not_if0 | ppu-objreg |
| `cubo` | 13 | not_if0 | ppu-objreg |
| `zedy` | 10 | not_if0 | ppu-objreg |
| `wuzy` | 3 | not_if0 | ppu-oam |

### `bus:oam_render_a3` () — diff=26, max=29
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zojy` | 29 | not_if0 | ppu-objreg |
| `akyh` | 27 | not_if0 | ppu-objreg |
| `wygo` | 25 | not_if0 | ppu-objreg |
| `wywy` | 23 | not_if0 | ppu-objreg |
| `dyny` | 21 | not_if0 | ppu-objreg |
| `wepy` | 19 | not_if0 | ppu-objreg |
| `dygo` | 17 | not_if0 | ppu-objreg |
| `afoz` | 15 | not_if0 | ppu-objreg |
| `celu` | 13 | not_if0 | ppu-objreg |
| `zumu` | 10 | not_if0 | ppu-objreg |
| `wyse` | 3 | not_if0 | ppu-oam |

### `bus:oam_render_a4` () — diff=26, max=29
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ynev` | 29 | not_if0 | ppu-objreg |
| `afen` | 27 | not_if0 | ppu-objreg |
| `elep` | 25 | not_if0 | ppu-objreg |
| `ezoc` | 23 | not_if0 | ppu-objreg |
| `waga` | 21 | not_if0 | ppu-objreg |
| `weru` | 19 | not_if0 | ppu-objreg |
| `dowa` | 17 | not_if0 | ppu-objreg |
| `apon` | 15 | not_if0 | ppu-objreg |
| `cegy` | 13 | not_if0 | ppu-objreg |
| `woko` | 10 | not_if0 | ppu-objreg |
| `zysu` | 3 | not_if0 | ppu-oam |

### `bus:oam_render_a5` () — diff=26, max=29
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xyra` | 29 | not_if0 | ppu-objreg |
| `apyv` | 27 | not_if0 | ppu-objreg |
| `etad` | 25 | not_if0 | ppu-objreg |
| `wabo` | 23 | not_if0 | ppu-objreg |
| `duza` | 21 | not_if0 | ppu-objreg |
| `xyre` | 19 | not_if0 | ppu-objreg |
| `dony` | 17 | not_if0 | ppu-objreg |
| `cuvu` | 15 | not_if0 | ppu-objreg |
| `bety` | 13 | not_if0 | ppu-objreg |
| `zave` | 10 | not_if0 | ppu-objreg |
| `wyda` | 3 | not_if0 | ppu-oam |

### `bus:oam_render_a6` () — diff=26, max=29
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `yrad` | 29 | not_if0 | ppu-objreg |
| `apob` | 27 | not_if0 | ppu-objreg |
| `waba` | 25 | not_if0 | ppu-objreg |
| `elyc` | 23 | not_if0 | ppu-objreg |
| `daly` | 21 | not_if0 | ppu-objreg |
| `woxy` | 19 | not_if0 | ppu-objreg |
| `efud` | 17 | not_if0 | ppu-objreg |
| `cyro` | 15 | not_if0 | ppu-objreg |
| `cyby` | 13 | not_if0 | ppu-objreg |
| `zece` | 10 | not_if0 | ppu-objreg |
| `wuco` | 3 | not_if0 | ppu-oam |

### `bus:oam_render_a7` () — diff=26, max=29
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `yhal` | 29 | not_if0 | ppu-objreg |
| `adyb` | 27 | not_if0 | ppu-objreg |
| `evyt` | 25 | not_if0 | ppu-objreg |
| `wocy` | 23 | not_if0 | ppu-objreg |
| `dalo` | 21 | not_if0 | ppu-objreg |
| `waja` | 19 | not_if0 | ppu-objreg |
| `dezu` | 17 | not_if0 | ppu-objreg |
| `axec` | 15 | not_if0 | ppu-objreg |
| `bemo` | 13 | not_if0 | ppu-objreg |
| `zetu` | 10 | not_if0 | ppu-objreg |
| `weza` | 3 | not_if0 | ppu-oam |

### `bus:~ma8` () — diff=23, max=28
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ceta` | 28 | not_if0 | ppu-bgscroll |
| `vovo` | 9 | not_if0 | ppu-window |
| `rysu` | 7 | not_if0 | ppu-vram |
| `wune` | 6 | not_if0 | ppu-ycomp |
| `evax` | 6 | not_if0 | ppu-dma |
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

### `bus:d0` () — diff=21, max=21
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruga` | 21 | not_if1 | ppu-vram |
| `tuty` | 20 | buf_if0 | bus-data |
| `anoc` | 19 | not_if0 |  |
| `xaca` | 18 | buf_if0 | ppu-xcomp |
| `tovu` | 18 | buf_if0 | bus-data |
| `yfap` | 18 | buf_if0 | ppu-ycomp |
| `romy` | 16 | not_if1 | bus-data |
| `poly` | 16 | not_if1 | ppu-dma |
| `foru` | 15 | not_if0 | apu-ch1 |
| `dopa` | 15 | not_if0 | apu-ch1 |
| `fapy` | 15 | not_if0 | apu-ch3 |
| `lova` | 15 | not_if0 | ppu-window |
| `punu` | 15 | not_if0 | ppu-window |
| `xary` | 15 | not_if0 | ppu-pal |
| `juvy` | 15 | not_if0 | apu-ch3 |
| `atel` | 15 | not_if0 | apu-ch4 |
| `fava` | 15 | not_if0 | apu-ch2 |
| `edos` | 15 | not_if0 | ppu-bgscroll |
| `vega` | 15 | not_if0 | ppu-stat |
| `retu` | 15 | not_if0 | ppu-stat |
| `raro` | 15 | not_if0 | ppu-pal |
| `wypo` | 15 | not_if0 | ppu-control |
| `huna` | 15 | not_if0 | apu-ch2 |
| `ware` | 15 | not_if0 | ppu-bgscroll |
| `jofo` | 15 | not_if0 | apu-ch3 |
| `laju` | 15 | not_if0 | ppu-pal |
| `teby` | 14 | not_if1 | ppu-stat |
| `dugu` | 14 | not_if1 | apu-ch3 |
| `jyne` | 13 | not_if0 | apu-ch1 |
| `buzu` | 13 | not_if0 | apu-control |
| `coto` | 13 | not_if0 | apu-control |
| `demy` | 13 | not_if0 | apu-ch4 |
| `huvu` | 13 | not_if0 | apu-ch2 |
| `akod` | 13 | not_if0 | apu-control |
| `kamo` | 13 | not_if0 | apu-ch4 |
| `kema` | 13 | not_if0 | joypad |
| `amyd` | 13 | not_if0 | apu-ch1 |
| `nela` | 12 | not_if1 | int |
| `soku` | 12 | not_if1 | timer |
| `tawu` | 12 | not_if1 | clocks |
| `cugy` | 12 | not_if1 | serial |
| `sete` | 12 | not_if1 | timer |
| `sypu` | 12 | not_if1 | bootrom |
| `ryla` | 12 | not_if1 | timer |
| `core` | 12 | not_if1 | serial |
| `ryma` | 10 | not_if0 | bus-data |
| `cpu` | 6 | sm83 |  |
| `boot_rom` | 0 | boot_rom |  |
| `high_ram` | 0 | high_ram |  |

### `bus:d1` () — diff=21, max=21
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rota` | 21 | not_if1 | ppu-vram |
| `sywa` | 20 | buf_if0 | bus-data |
| `ataj` | 19 | not_if0 |  |
| `xele` | 18 | buf_if0 | ppu-ycomp |
| `xagu` | 18 | buf_if0 | ppu-xcomp |
| `sosa` | 18 | buf_if0 | bus-data |
| `rofo` | 16 | not_if1 | ppu-dma |
| `ryne` | 16 | not_if1 | bus-data |
| `jura` | 15 | not_if0 | apu-ch3 |
| `paba` | 15 | not_if0 | ppu-pal |
| `goba` | 15 | not_if0 | ppu-bgscroll |
| `vojo` | 15 | not_if0 | ppu-stat |
| `lepa` | 15 | not_if0 | ppu-pal |
| `jaro` | 15 | not_if0 | apu-ch2 |
| `poda` | 15 | not_if0 | ppu-window |
| `kafu` | 15 | not_if0 | apu-ch3 |
| `wuva` | 15 | not_if0 | ppu-stat |
| `muka` | 15 | not_if0 | ppu-window |
| `faro` | 15 | not_if0 | apu-ch3 |
| `xero` | 15 | not_if0 | ppu-control |
| `fajy` | 15 | not_if0 | apu-ch2 |
| `ekob` | 15 | not_if0 | ppu-bgscroll |
| `xoke` | 15 | not_if0 | ppu-pal |
| `gefu` | 15 | not_if0 | apu-ch1 |
| `demu` | 15 | not_if0 | apu-ch1 |
| `wuga` | 14 | not_if1 | ppu-stat |
| `desy` | 14 | not_if1 | apu-ch3 |
| `hyre` | 13 | not_if0 | apu-ch2 |
| `atax` | 13 | not_if0 | apu-ch1 |
| `coce` | 13 | not_if0 | apu-ch4 |
| `efus` | 13 | not_if0 | apu-control |
| `kaku` | 13 | not_if0 | apu-ch4 |
| `awed` | 13 | not_if0 | apu-control |
| `kuro` | 13 | not_if0 | joypad |
| `capu` | 13 | not_if0 | apu-control |
| `jaca` | 13 | not_if0 | apu-ch1 |
| `dude` | 12 | not_if1 | serial |
| `rote` | 12 | not_if1 | timer |
| `racy` | 12 | not_if1 | timer |
| `pyre` | 12 | not_if1 | timer |
| `taku` | 12 | not_if1 | clocks |
| `nabo` | 12 | not_if1 | int |
| `ruvo` | 10 | not_if0 | bus-data |
| `cpu` | 6 | sm83 |  |
| `high_ram` | 0 | high_ram |  |
| `boot_rom` | 0 | boot_rom |  |

### `bus:d2` () — diff=21, max=21
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rybu` | 21 | not_if1 | ppu-vram |
| `sugu` | 20 | buf_if0 | bus-data |
| `ajec` | 19 | not_if0 |  |
| `xepu` | 18 | buf_if0 | ppu-xcomp |
| `ypon` | 18 | buf_if0 | ppu-ycomp |
| `sedu` | 18 | buf_if0 | bus-data |
| `rema` | 16 | not_if1 | ppu-dma |
| `rejy` | 16 | not_if1 | bus-data |
| `fegu` | 15 | not_if0 | apu-ch2 |
| `moko` | 15 | not_if0 | ppu-window |
| `lyco` | 15 | not_if0 | ppu-stat |
| `xuno` | 15 | not_if0 | ppu-pal |
| `cuga` | 15 | not_if0 | ppu-bgscroll |
| `gonu` | 15 | not_if0 | ppu-bgscroll |
| `fote` | 15 | not_if0 | apu-ch3 |
| `dexo` | 15 | not_if0 | apu-ch1 |
| `kyvu` | 15 | not_if0 | apu-ch1 |
| `lode` | 15 | not_if0 | ppu-pal |
| `razu` | 15 | not_if0 | ppu-stat |
| `redo` | 15 | not_if0 | ppu-pal |
| `pygu` | 15 | not_if0 | ppu-window |
| `wyju` | 15 | not_if0 | ppu-decode |
| `hufo` | 15 | not_if0 | apu-ch3 |
| `kesy` | 15 | not_if0 | apu-ch3 |
| `jeke` | 15 | not_if0 | apu-ch2 |
| `sego` | 14 | not_if1 | ppu-stat |
| `baty` | 14 | not_if1 | apu-ch3 |
| `cuzu` | 13 | not_if0 | apu-ch4 |
| `fate` | 13 | not_if0 | apu-control |
| `azyp` | 13 | not_if0 | apu-ch1 |
| `avud` | 13 | not_if0 | apu-control |
| `caga` | 13 | not_if0 | apu-control |
| `joku` | 13 | not_if0 | apu-ch1 |
| `havu` | 13 | not_if0 | apu-ch2 |
| `kyro` | 13 | not_if0 | apu-ch4 |
| `kuve` | 13 | not_if0 | joypad |
| `nola` | 12 | not_if1 | timer |
| `detu` | 12 | not_if1 | serial |
| `rova` | 12 | not_if1 | int |
| `ravy` | 12 | not_if1 | timer |
| `temu` | 12 | not_if1 | clocks |
| `supe` | 12 | not_if1 | timer |
| `ryko` | 10 | not_if0 | bus-data |
| `cpu` | 6 | sm83 |  |
| `high_ram` | 0 | high_ram |  |
| `boot_rom` | 0 | boot_rom |  |

### `bus:d3` () — diff=21, max=21
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `raju` | 21 | not_if1 | ppu-vram |
| `tawo` | 20 | buf_if0 | bus-data |
| `asuz` | 19 | not_if0 |  |
| `taxo` | 18 | buf_if0 | bus-data |
| `xygu` | 18 | buf_if0 | ppu-xcomp |
| `xuvo` | 18 | buf_if0 | ppu-ycomp |
| `rase` | 16 | not_if1 | bus-data |
| `pane` | 16 | not_if1 | ppu-dma |
| `xuby` | 15 | not_if0 | ppu-pal |
| `lobe` | 15 | not_if0 | ppu-pal |
| `fose` | 15 | not_if0 | apu-ch2 |
| `loka` | 15 | not_if0 | ppu-window |
| `godo` | 15 | not_if0 | ppu-bgscroll |
| `redy` | 15 | not_if0 | ppu-stat |
| `wojy` | 15 | not_if0 | ppu-stat |
| `jude` | 15 | not_if0 | apu-ch3 |
| `fana` | 15 | not_if0 | apu-ch3 |
| `lole` | 15 | not_if0 | ppu-window |
| `kumo` | 15 | not_if0 | apu-ch1 |
| `wony` | 15 | not_if0 | ppu-bgscroll |
| `puzo` | 15 | not_if0 | ppu-stat |
| `lyza` | 15 | not_if0 | ppu-pal |
| `wuka` | 15 | not_if0 | ppu-control |
| `bade` | 14 | not_if1 | apu-ch3 |
| `jeku` | 13 | not_if0 | joypad |
| `hono` | 13 | not_if0 | apu-ch1 |
| `keta` | 13 | not_if0 | apu-ch4 |
| `koge` | 13 | not_if0 | apu-control |
| `boca` | 13 | not_if0 | apu-control |
| `axem` | 13 | not_if0 | apu-control |
| `gome` | 13 | not_if0 | apu-ch4 |
| `afox` | 13 | not_if0 | apu-ch1 |
| `gene` | 13 | not_if0 | apu-ch2 |
| `salu` | 12 | not_if1 | timer |
| `sosy` | 12 | not_if1 | timer |
| `tuse` | 12 | not_if1 | clocks |
| `pado` | 12 | not_if1 | int |
| `daso` | 12 | not_if1 | serial |
| `tavo` | 10 | not_if0 | bus-data |
| `cpu` | 6 | sm83 |  |
| `high_ram` | 0 | high_ram |  |
| `boot_rom` | 0 | boot_rom |  |

### `bus:d4` () — diff=21, max=21
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyja` | 21 | not_if1 | ppu-vram |
| `tute` | 20 | buf_if0 | bus-data |
| `benu` | 19 | not_if0 |  |
| `zysa` | 18 | buf_if0 | ppu-ycomp |
| `tahy` | 18 | buf_if0 | bus-data |
| `xuna` | 18 | buf_if0 | ppu-xcomp |
| `reka` | 16 | not_if1 | bus-data |
| `pare` | 16 | not_if1 | ppu-dma |
| `cedu` | 15 | not_if0 | ppu-bgscroll |
| `pofo` | 15 | not_if0 | ppu-stat |
| `cusa` | 15 | not_if0 | ppu-bgscroll |
| `luky` | 15 | not_if0 | ppu-pal |
| `kary` | 15 | not_if0 | apu-ch1 |
| `fera` | 15 | not_if0 | apu-ch3 |
| `juke` | 15 | not_if0 | apu-ch3 |
| `lace` | 15 | not_if0 | ppu-pal |
| `vyne` | 15 | not_if0 | ppu-stat |
| `voke` | 15 | not_if0 | ppu-control |
| `race` | 15 | not_if0 | ppu-stat |
| `gero` | 15 | not_if0 | apu-ch2 |
| `mele` | 15 | not_if0 | ppu-window |
| `mega` | 15 | not_if0 | ppu-window |
| `xaju` | 15 | not_if0 | ppu-pal |
| `bune` | 14 | not_if1 | apu-ch3 |
| `avek` | 13 | not_if0 | apu-ch1 |
| `heda` | 13 | not_if0 | apu-ch4 |
| `geda` | 13 | not_if0 | apu-ch4 |
| `koce` | 13 | not_if0 | joypad |
| `howu` | 13 | not_if0 | apu-ch1 |
| `hupe` | 13 | not_if0 | apu-ch2 |
| `cavu` | 13 | not_if0 | apu-control |
| `amad` | 13 | not_if0 | apu-control |
| `supo` | 12 | not_if1 | timer |
| `pegy` | 12 | not_if1 | int |
| `upug` | 12 | not_if1 | clocks |
| `dame` | 12 | not_if1 | serial |
| `somu` | 12 | not_if1 | timer |
| `tepe` | 10 | not_if0 | bus-data |
| `cpu` | 6 | sm83 |  |
| `boot_rom` | 0 | boot_rom |  |
| `high_ram` | 0 | high_ram |  |


## Sprite X Priority (10 races)

### `fono` (dffr) — diff=23, max=27
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guze` | 27 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `exuq` (dffr) — diff=21, max=25
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `foxa` | 25 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `wapo` (dffr) — diff=19, max=23
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gutu` | 23 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `womy` (dffr) — diff=17, max=21
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xoja` | 21 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `wafy` (dffr) — diff=15, max=19
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gega` | 19 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `cedy` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `enut` | 11 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `egav` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `emol` | 13 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `eboj` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `guva` | 8 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `gota` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `gyfy` | 15 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `xudy` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `gono` | 17 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |


## BG Pixel Shifter (32 races)

### `macu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lydu` | 22 | nand2 | ppu-bgfifo |
| `luja` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `moju` | 0 | dffsr | ppu-bgfifo |

### `modu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lodo` | 22 | nand2 | ppu-bgfifo |
| `leru` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `nepo` | 0 | dffsr | ppu-bgfifo |

### `moju` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lutu` | 22 | nand2 | ppu-bgfifo |
| `loto` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `nozo` | 0 | dffsr | ppu-bgfifo |

### `nepo` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myvy` | 22 | nand2 | ppu-bgfifo |
| `mosy` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `macu` | 0 | dffsr | ppu-bgfifo |

### `neda` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyha` | 22 | nand2 | ppu-bgfifo |
| `nute` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `modu` | 0 | dffsr | ppu-bgfifo |

### `nozo` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nexa` | 22 | nand2 | ppu-bgfifo |
| `nyxo` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `myde` | 0 | dffsr | ppu-bgfifo |

### `pybo` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nady` | 22 | nand2 | ppu-bgfifo |
| `naja` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `neda` | 0 | dffsr | ppu-bgfifo |

### `ralu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rajo` | 22 | nand2 | ppu-bgfifo |
| `supu` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `setu` | 0 | dffsr | ppu-bgfifo |

### `rysa` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryja` | 22 | nand2 | ppu-bgfifo |
| `sebo` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `sady` | 0 | dffsr | ppu-bgfifo |

### `setu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `raja` | 22 | nand2 | ppu-bgfifo |
| `sywe` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `sobo` | 0 | dffsr | ppu-bgfifo |

### `sady` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruce` | 22 | nand2 | ppu-bgfifo |
| `sure` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `taca` | 0 | dffsr | ppu-bgfifo |

### `sohu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryjy` | 22 | nand2 | ppu-bgfifo |
| `raga` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `ralu` | 0 | dffsr | ppu-bgfifo |

### `sobo` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruto` | 22 | nand2 | ppu-bgfifo |
| `suca` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `rysa` | 0 | dffsr | ppu-bgfifo |

### `taca` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `seno` | 22 | nand2 | ppu-bgfifo |
| `soly` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 19 | or2 | ppu-cycles |
| `tomy` | 0 | dffsr | ppu-bgfifo |

### `poju` (dffr_cc_q) — diff=7, max=7
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `labu` | 7 | not_x2 | ppu-bgfifo |
| `luve` | 6 | not_x2 | ppu-bgfifo |
| `bus:md5` | 0 |  | bus |


## BG/Win Cycles (20 races)

### `mesu` (dffr) — diff=20, max=20
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 20 | nor3 | ppu-cycles |
| `laxu` | 0 | dffr | ppu-cycles |

### `nyva` (dffr) — diff=20, max=20
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 20 | nor3 | ppu-cycles |
| `mesu` | 0 | dffr | ppu-cycles |

### `lony` (nand_latch) — diff=18, max=20
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 20 | nor3 | ppu-cycles |
| `lury` | 2 | and2 | ppu-cycles |

### `puxa` (dffr) — diff=18, max=18
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roxo` | 18 | not_x1 | ppu-cycles |
| `pohu` | 5 | not_x1 | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `paho` (dffr) — diff=18, max=18
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roxo` | 18 | not_x1 | ppu-cycles |
| `xydo` | 0 | dffr | ppu-stat |
| `xymu` | 0 | nor_latch | ppu-stat |

### `nyka` (dffr) — diff=17, max=22
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyry` | 22 | not_x1 | ppu-cycles |
| `alet` | 7 | not_x2 | ppu-control |
| `nafy` | 5 | nor2 | ppu-cycles |

### `ryfa` (dffr) — diff=17, max=17
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `segu` | 17 | not_x4 | ppu-cycles |
| `pany` | 8 | nor2 | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `rubu` (dffr) — diff=17, max=17
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 17 | nor2 | ppu-cycles |
| `roga` | 0 | dffr | ppu-cycles |

### `roga` (dffr) — diff=17, max=17
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 17 | nor2 | ppu-cycles |
| `ryku` | 0 | dffr | ppu-cycles |

### `pynu` (nor_latch) — diff=16, max=16
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xofo` | 16 | nand3 | ppu-cycles |
| `nunu` | 0 | dffr | ppu-cycles |

### `lovy` (dffr) — diff=14, max=22
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyry` | 22 | not_x1 | ppu-cycles |
| `nyxu` | 20 | nor3 | ppu-cycles |
| `myvo` | 8 | not_x1 | ppu-cycles |

### `pyco` (dffr) — diff=11, max=18
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roco` | 18 | not_x1 | ppu-cycles |
| `xapo` | 9 | not_x2 | ppu-control |
| `nuko` | 7 | not_x1 | ppu-window |

### `nunu` (dffr) — diff=9, max=9
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xapo` | 9 | not_x2 | ppu-control |
| `mehe` | 8 | not_x1 | ppu-cycles |
| `pyco` | 0 | dffr | ppu-cycles |

### `nopa` (dffr) — diff=9, max=9
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xapo` | 9 | not_x2 | ppu-control |
| `alet` | 7 | not_x2 | ppu-control |
| `pynu` | 0 | nor_latch | ppu-cycles |

### `nyze` (dffr) — diff=8, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `moxe` | 8 | not_x1 | ppu-cycles |
| `puxa` | 0 | dffr | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |


## Sprite Pixel Shifter (16 races)

### `lefe` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `lela` | 9 | nand2 | ppu-objfifo |
| `lyde` | 9 | nand2 | ppu-objfifo |
| `maso` | 0 | dffsr | ppu-objfifo |

### `lesu` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `lufy` | 9 | nand2 | ppu-objfifo |
| `mame` | 9 | nand2 | ppu-objfifo |
| `lefe` | 0 | dffsr | ppu-objfifo |

### `maso` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `myto` | 9 | nand2 | ppu-objfifo |
| `mada` | 9 | nand2 | ppu-objfifo |
| `nuro` | 0 | dffsr | ppu-objfifo |

### `naty` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `myxa` | 9 | nand2 | ppu-objfifo |
| `majo` | 9 | nand2 | ppu-objfifo |
| `pefu` | 0 | dffsr | ppu-objfifo |

### `pefu` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `rusy` | 9 | nand2 | ppu-objfifo |
| `ruca` | 9 | nand2 | ppu-objfifo |
| `nylu` | 0 | dffsr | ppu-objfifo |

### `pyjo` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `rano` | 9 | nand2 | ppu-objfifo |
| `rehu` | 9 | nand2 | ppu-objfifo |
| `naty` | 0 | dffsr | ppu-objfifo |

### `vupy` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `teso` | 9 | nand2 | ppu-objfifo |
| `tula` | 9 | nand2 | ppu-objfifo |
| `vanu` | 0 | dffsr | ppu-objfifo |

### `vanu` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `taby` | 9 | nand2 | ppu-objfifo |
| `tapo` | 9 | nand2 | ppu-objfifo |
| `weba` | 0 | dffsr | ppu-objfifo |

### `vafo` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `tuxa` | 9 | nand2 | ppu-objfifo |
| `tupe` | 9 | nand2 | ppu-objfifo |
| `wora` | 0 | dffsr | ppu-objfifo |

### `vare` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `tyga` | 9 | nand2 | ppu-objfifo |
| `waxo` | 9 | nand2 | ppu-objfifo |
| `pyjo` | 0 | dffsr | ppu-objfifo |

### `wufy` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `vune` | 9 | nand2 | ppu-objfifo |
| `xyve` | 9 | nand2 | ppu-objfifo |
| `vafo` | 0 | dffsr | ppu-objfifo |

### `weba` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `vume` | 9 | nand2 | ppu-objfifo |
| `xole` | 9 | nand2 | ppu-objfifo |
| `vare` | 0 | dffsr | ppu-objfifo |

### `wora` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `vaby` | 9 | nand2 | ppu-objfifo |
| `xexu` | 9 | nand2 | ppu-objfifo |
| `wyho` | 0 | dffsr | ppu-objfifo |

### `wyho` (dffsr) — diff=19, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `vexu` | 9 | nand2 | ppu-objfifo |
| `xato` | 9 | nand2 | ppu-objfifo |
| `lesu` | 0 | dffsr | ppu-objfifo |

### `nylu` (dffsr) — diff=10, max=19
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `mezu` | 9 | nand2 | ppu-objfifo |
| `mofy` | 9 | nand2 | ppu-objfifo |


## STAT/LY (33 races)

### `rupo` (nor_latch) — diff=18, max=18
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pago` | 18 | or2 | ppu-stat |
| `ropo` | 0 | dffr | ppu-stat |

### `raha` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d7` | 0 |  | bus |

### `rugu` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 17 | not_x1 | ppu-stat |
| `ryve` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d6` | 0 |  | bus |

### `roxe` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 17 | not_x1 | ppu-stat |
| `ryve` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d3` | 0 |  | bus |

### `rufo` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 17 | not_x1 | ppu-stat |
| `ryve` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d4` | 0 |  | bus |

### `refe` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 17 | not_x1 | ppu-stat |
| `ryve` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d5` | 0 |  | bus |

### `sedy` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d2` | 0 |  | bus |

### `syry` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d0` | 0 |  | bus |

### `salo` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d3` | 0 |  | bus |

### `sota` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d4` | 0 |  | bus |

### `vuce` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d1` | 0 |  | bus |

### `vafa` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d5` | 0 |  | bus |

### `vevo` (drlatch_ee) — diff=17, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d6` | 0 |  | bus |

### `savy` (dffr) — diff=16, max=19
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `tady` | 15 | nor2 | ppu-stat |
| `rybo` | 3 | xor | ppu-stat |

### `xodu` (dffr) — diff=14, max=19
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sacu` | 19 | or2 | ppu-cycles |
| `tady` | 15 | nor2 | ppu-stat |
| `xegy` | 5 | xor | ppu-stat |


## DMA (21 races)

### `maru` (dlatch_ee) — diff=17, max=17
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 17 | not_x1 | ppu-dma |
| `loru` | 16 | not_x1 | ppu-dma |
| `bus:d7` | 0 |  | bus |

### `nafa` (dlatch_ee) — diff=17, max=17
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 17 | not_x1 | ppu-dma |
| `loru` | 16 | not_x1 | ppu-dma |
| `bus:d0` | 0 |  | bus |

### `nydo` (dlatch_ee) — diff=17, max=17
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 17 | not_x1 | ppu-dma |
| `loru` | 16 | not_x1 | ppu-dma |
| `bus:d3` | 0 |  | bus |

### `nygy` (dlatch_ee) — diff=17, max=17
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 17 | not_x1 | ppu-dma |
| `loru` | 16 | not_x1 | ppu-dma |
| `bus:d4` | 0 |  | bus |

### `poku` (dlatch_ee) — diff=17, max=17
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 17 | not_x1 | ppu-dma |
| `loru` | 16 | not_x1 | ppu-dma |
| `bus:d6` | 0 |  | bus |

### `pula` (dlatch_ee) — diff=17, max=17
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 17 | not_x1 | ppu-dma |
| `loru` | 16 | not_x1 | ppu-dma |
| `bus:d5` | 0 |  | bus |

### `pyne` (dlatch_ee) — diff=17, max=17
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 17 | not_x1 | ppu-dma |
| `loru` | 16 | not_x1 | ppu-dma |
| `bus:d1` | 0 |  | bus |

### `para` (dlatch_ee) — diff=17, max=17
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 17 | not_x1 | ppu-dma |
| `loru` | 16 | not_x1 | ppu-dma |
| `bus:d2` | 0 |  | bus |

### `luvy` (dffr) — diff=15, max=16
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lupa` | 16 | nor2 | ppu-dma |
| `cunu` | 5 | not_x2 | ppu-control |
| `uvyt` | 1 | not_x2 | clocks |

### `wuje` (nor_latch) — diff=12, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xuto` | 15 | and2 | ppu-oam |
| `xyny` | 3 | not_x1 | ppu-dma |

### `lyxe` (nor_latch) — diff=9, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavy` | 15 | and2 | ppu-dma |
| `loko` | 6 | nand2 | ppu-dma |

### `mugu` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `nuto` | 0 | dffr | ppu-dma |

### `muty` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `nefy` | 0 | dffr | ppu-dma |

### `nuto` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `pylo` | 0 | dffr | ppu-dma |

### `nyko` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `muty` | 0 | dffr | ppu-dma |


## Palettes (24 races)

### `lugu` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 17 | not_x1 | ppu-pal |
| `leho` | 16 | not_x1 | ppu-pal |
| `bus:d5` | 0 |  | bus |

### `luxo` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 17 | not_x1 | ppu-pal |
| `leho` | 16 | not_x1 | ppu-pal |
| `bus:d7` | 0 |  | bus |

### `lepu` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 17 | not_x1 | ppu-pal |
| `leho` | 16 | not_x1 | ppu-pal |
| `bus:d6` | 0 |  | bus |

### `lose` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 17 | not_x1 | ppu-pal |
| `leho` | 16 | not_x1 | ppu-pal |
| `bus:d3` | 0 |  | bus |

### `lune` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 17 | not_x1 | ppu-pal |
| `leho` | 16 | not_x1 | ppu-pal |
| `bus:d4` | 0 |  | bus |

### `lawo` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 17 | not_x1 | ppu-pal |
| `leho` | 16 | not_x1 | ppu-pal |
| `bus:d1` | 0 |  | bus |

### `moxy` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 17 | not_x1 | ppu-pal |
| `leho` | 16 | not_x1 | ppu-pal |
| `bus:d0` | 0 |  | bus |

### `mosa` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `luxu` | 17 | not_x1 | ppu-pal |
| `leho` | 16 | not_x1 | ppu-pal |
| `bus:d2` | 0 |  | bus |

### `maxy` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 17 | not_x1 | ppu-pal |
| `tepo` | 16 | not_x1 | ppu-pal |
| `bus:d3` | 0 |  | bus |

### `muke` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 17 | not_x1 | ppu-pal |
| `tepo` | 16 | not_x1 | ppu-pal |
| `bus:d4` | 0 |  | bus |

### `mena` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 17 | not_x1 | ppu-pal |
| `tepo` | 16 | not_x1 | ppu-pal |
| `bus:d7` | 0 |  | bus |

### `moru` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 17 | not_x1 | ppu-pal |
| `tepo` | 16 | not_x1 | ppu-pal |
| `bus:d5` | 0 |  | bus |

### `mogy` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 17 | not_x1 | ppu-pal |
| `tepo` | 16 | not_x1 | ppu-pal |
| `bus:d6` | 0 |  | bus |

### `nusy` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 17 | not_x1 | ppu-pal |
| `tepo` | 16 | not_x1 | ppu-pal |
| `bus:d1` | 0 |  | bus |

### `pavo` (dlatch_ee) — diff=17, max=17
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 17 | not_x1 | ppu-pal |
| `tepo` | 16 | not_x1 | ppu-pal |
| `bus:d0` | 0 |  | bus |


## Window Logic (30 races)

### `mypu` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d4` | 0 |  | bus |

### `muvo` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d6` | 0 |  | bus |

### `mypa` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d0` | 0 |  | bus |

### `myce` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d5` | 0 |  | bus |

### `meby` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d3` | 0 |  | bus |

### `mela` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d3` | 0 |  | bus |

### `nofe` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d1` | 0 |  | bus |

### `nuku` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d7` | 0 |  | bus |

### `noke` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d2` | 0 |  | bus |

### `nafu` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d7` | 0 |  | bus |

### `nyro` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d1` | 0 |  | bus |

### `naga` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d2` | 0 |  | bus |

### `nulo` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d4` | 0 |  | bus |

### `nuka` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d6` | 0 |  | bus |

### `nene` (drlatch_ee) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d5` | 0 |  | bus |


## PPU Control (8 races)

### `vyxe` (drlatch_ee) — diff=17, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d0` | 0 |  | bus |

### `woky` (drlatch_ee) — diff=17, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `wexu` (drlatch_ee) — diff=17, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d4` | 0 |  | bus |

### `wymo` (drlatch_ee) — diff=17, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d5` | 0 |  | bus |

### `xona` (drlatch_ee) — diff=17, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d7` | 0 |  | bus |

### `xylo` (drlatch_ee) — diff=17, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `xafo` (drlatch_ee) — diff=17, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d3` | 0 |  | bus |

### `xymo` (drlatch_ee) — diff=17, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d2` | 0 |  | bus |


## BG Scrolling (16 races)

### `bemy` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d4` | 0 |  | bus |

### `bake` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d7` | 0 |  | bus |

### `cuzy` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d5` | 0 |  | bus |

### `cabu` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `cyxu` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d2` | 0 |  | bus |

### `duzu` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `daty` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d0` | 0 |  | bus |

### `dede` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d4` | 0 |  | bus |

### `foha` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `funy` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d7` | 0 |  | bus |

### `fujo` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d3` | 0 |  | bus |

### `foty` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d5` | 0 |  | bus |

### `fezu` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d2` | 0 |  | bus |

### `fymo` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `gubo` (drlatch_ee) — diff=17, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d3` | 0 |  | bus |


## apu-ch4 (68 races)

### `cuny` (drlatch_ee) — diff=17, max=17
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cazo` | 17 | not_x1 | apu-ch4 |
| `dulu` | 16 | nand2 | apu-ch4 |
| `cabe` | 9 | not_x1 | apu-ch4 |
| `bus:d6` | 0 |  | bus |

### `etyj` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 16 | not_x1 | apu-ch4 |
| `daco` | 15 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d1` | 0 |  | bus |

### `ezyk` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 16 | not_x1 | apu-ch4 |
| `daco` | 15 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d2` | 0 |  | bus |

### `emok` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 16 | not_x1 | apu-ch4 |
| `daco` | 15 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d0` | 0 |  | bus |

### `fugo` (dffr) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gapy` | 16 | nor3 | apu-ch4 |
| `edop` | 0 | tffnl | apu-ch4 |

### `fyto` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 16 | not_x2 | apu-ch4 |
| `getu` | 15 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d5` | 0 |  | bus |

### `feta` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 16 | not_x2 | apu-ch4 |
| `getu` | 15 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d4` | 0 |  | bus |

### `gafo` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 16 | not_x2 | apu-ch4 |
| `getu` | 15 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d7` | 0 |  | bus |

### `gogo` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 16 | not_x2 | apu-ch4 |
| `getu` | 15 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d6` | 0 |  | bus |

### `garu` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d4` | 0 |  | bus |

### `geky` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d3` | 0 |  | bus |

### `gedu` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d7` | 0 |  | bus |

### `goky` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d5` | 0 |  | bus |

### `gozo` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d6` | 0 |  | bus |

### `jero` (drlatch_ee) — diff=16, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 16 | not_x2 | apu-ch4 |
| `humo` | 15 | and2 | apu-ch4 |
| `kame` | 9 | not_x1 | apu-control |
| `bus:d1` | 0 |  | bus |


## apu-ch2 (56 races)

### `emer` (drlatch_ee) — diff=17, max=17
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `duso` | 17 | not_x1 | apu-ch2 |
| `evyf` | 16 | nand2 | apu-ch2 |
| `fazo` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |

### `bamy` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `budu` | 16 | not_x1 | apu-ch2 |
| `bacu` | 15 | and2 | apu-ch2 |
| `afat` | 9 | not_x1 | apu-control |
| `bus:d7` | 0 |  | bus |

### `bera` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `budu` | 16 | not_x1 | apu-ch2 |
| `bacu` | 15 | and2 | apu-ch2 |
| `afat` | 9 | not_x1 | apu-control |
| `bus:d6` | 0 |  | bus |

### `cyre` (dffr) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `beny` | 16 | nor3 | apu-ch2 |
| `akyd` | 0 | tffnl | apu-ch2 |

### `fofe` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d0` | 0 |  | bus |

### `fova` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d1` | 0 |  | bus |

### `fedy` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d2` | 0 |  | bus |

### `fome` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d3` | 0 |  | bus |

### `fora` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d4` | 0 |  | bus |

### `fore` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d3` | 0 |  | bus |

### `goda` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 16 | not_x1 | apu-ch2 |
| `exuc` | 15 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d5` | 0 |  | bus |

### `gumy` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 16 | not_x1 | apu-ch2 |
| `exuc` | 15 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |

### `gupu` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 16 | not_x1 | apu-ch2 |
| `exuc` | 15 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d7` | 0 |  | bus |

### `gata` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d4` | 0 |  | bus |

### `gura` (drlatch_ee) — diff=16, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |


## apu-ch3 (59 races)

### `hoto` (drlatch_ee) — diff=17, max=17
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gygu` | 17 | not_x1 | apu-ch3 |
| `fovo` | 16 | nand2 | apu-ch3 |
| `heky` | 9 | not_x1 | apu-ch3 |
| `bus:d6` | 0 |  | bus |

### `fexu` (dffr) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guda` | 16 | nor3 | apu-ch3 |
| `fyru` | 0 | tffnl | apu-ch3 |

### `gage` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d7` | 0 |  | bus |

### `guxe` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gucy` | 16 | not_x1 | apu-ch3 |
| `gejo` | 15 | and2 | apu-ch3 |
| `gove` | 9 | not_x1 | apu-ch3 |
| `bus:d7` | 0 |  | bus |

### `hody` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guzu` | 16 | not_x1 | apu-ch3 |
| `haga` | 15 | and2 | apu-ch3 |
| `guro` | 9 | not_x1 | apu-ch3 |
| `bus:d5` | 0 |  | bus |

### `huky` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guzu` | 16 | not_x1 | apu-ch3 |
| `haga` | 15 | and2 | apu-ch3 |
| `guro` | 9 | not_x1 | apu-ch3 |
| `bus:d6` | 0 |  | bus |

### `jety` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 16 | not_x1 | apu-ch3 |
| `huda` | 15 | and2 | apu-ch3 |
| `kopy` | 9 | not_x1 | apu-ch3 |
| `bus:d1` | 0 |  | bus |

### `jemo` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 16 | not_x1 | apu-ch3 |
| `huda` | 15 | and2 | apu-ch3 |
| `kopy` | 9 | not_x1 | apu-ch3 |
| `bus:d0` | 0 |  | bus |

### `jacy` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 16 | not_x1 | apu-ch3 |
| `huda` | 15 | and2 | apu-ch3 |
| `kopy` | 9 | not_x1 | apu-ch3 |
| `bus:d2` | 0 |  | bus |

### `jovy` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d1` | 0 |  | bus |

### `jypo` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d4` | 0 |  | bus |

### `jefe` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d3` | 0 |  | bus |

### `jaxa` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d2` | 0 |  | bus |

### `jove` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 16 | not_x1 | apu-ch3 |
| `kota` | 15 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d5` | 0 |  | bus |

### `koga` (drlatch_ee) — diff=16, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d0` | 0 |  | bus |


## Timer (21 races)

### `nydu` (dffr) — diff=16, max=16
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mugy` | 16 | not_x1 | timer |
| `boga` | 11 | not_x6 | clocks |
| `nuga` | 0 | tffnl | timer |

### `nuga` (tffnl) — diff=15, max=15
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 15 | nand3 | timer |
| `pagu` | 15 | nor2 | timer |
| `peda` | 0 | tffnl | timer |

### `peru` (tffnl) — diff=15, max=15
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 15 | nand3 | timer |
| `nada` | 15 | nor2 | timer |
| `povy` | 0 | tffnl | timer |

### `povy` (tffnl) — diff=15, max=15
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 15 | nand3 | timer |
| `nero` | 15 | nor2 | timer |
| `rega` | 0 | tffnl | timer |

### `peda` (tffnl) — diff=15, max=15
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 15 | nand3 | timer |
| `pyma` | 15 | nor2 | timer |
| `rage` | 0 | tffnl | timer |

### `rate` (tffnl) — diff=15, max=15
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 15 | nand3 | timer |
| `repa` | 15 | nor2 | timer |
| `peru` | 0 | tffnl | timer |

### `rage` (tffnl) — diff=15, max=15
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 15 | nand3 | timer |
| `rugy` | 15 | nor2 | timer |
| `ruby` | 0 | tffnl | timer |

### `ruby` (tffnl) — diff=15, max=15
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 15 | nand3 | timer |
| `rolu` | 15 | nor2 | timer |
| `rate` | 0 | tffnl | timer |

### `muru` (dffr) — diff=12, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d2` | 0 |  | bus |

### `nyke` (dffr) — diff=12, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |

### `peto` (dffr) — diff=12, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d6` | 0 |  | bus |

### `sufy` (dffr) — diff=12, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d5` | 0 |  | bus |

### `sabu` (dffr) — diff=12, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `seta` (dffr) — diff=12, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d7` | 0 |  | bus |

### `samy` (dffr) — diff=12, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sara` | 12 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |


## Interrupts (10 races)

### `nybo` (dffsr) — diff=16, max=16
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pyga` | 16 | and3 | int |
| `pyhu` | 14 | nand3 | int |
| `moba` | 0 | dffr | timer |

### `ubul` (dffsr) — diff=16, max=16
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuny` | 16 | and3 | int |
| `tome` | 14 | nand3 | int |
| `caly` | 0 | dffr | serial |

### `ulak` (dffsr) — diff=14, max=16
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyme` | 16 | and3 | int |
| `toga` | 14 | nand3 | int |
| `asok` | 2 | and2 | joypad |

### `lope` (dffsr) — diff=13, max=16
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyta` | 16 | and3 | int |
| `myzu` | 14 | nand3 | int |
| `vypu` | 3 | not_x3 | ppu-stat |

### `mopo` (dlatch) — diff=10, max=10
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 10 | nand4 | int |
| `lalu` | 0 | dffsr | int |

### `maty` (dlatch) — diff=10, max=10
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 10 | nand4 | int |
| `lope` | 0 | dffsr | int |

### `nejy` (dlatch) — diff=10, max=10
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 10 | nand4 | int |
| `ubul` | 0 | dffsr | int |

### `nuty` (dlatch) — diff=10, max=10
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 10 | nand4 | int |
| `ulak` | 0 | dffsr | int |

### `pavy` (dlatch) — diff=10, max=10
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 10 | nand4 | int |
| `nybo` | 0 | dffsr | int |

### `lalu` (dffsr) — diff=5, max=19
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voty` | 19 | not_x3 | ppu-stat |
| `movu` | 16 | and3 | int |
| `mody` | 14 | nand3 | int |


## apu-control (27 races)

### `anev` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 16 | not_x2 | apu-control |
| `bono` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d0` | 0 |  | bus |

### `atuf` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 16 | not_x2 | apu-control |
| `bono` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d3` | 0 |  | bus |

### `apeg` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 16 | not_x2 | apu-control |
| `bowe` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d0` | 0 |  | bus |

### `apos` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 16 | not_x2 | apu-control |
| `bowe` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d3` | 0 |  | bus |

### `ager` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 16 | not_x2 | apu-control |
| `bowe` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d2` | 0 |  | bus |

### `bepu` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 16 | not_x2 | apu-control |
| `byfa` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d7` | 0 |  | bus |

### `befo` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 16 | not_x2 | apu-control |
| `byfa` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d6` | 0 |  | bus |

### `bume` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 16 | not_x2 | apu-control |
| `byfa` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d4` | 0 |  | bus |

### `bofa` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 16 | not_x2 | apu-control |
| `byfa` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d5` | 0 |  | bus |

### `byre` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 16 | not_x2 | apu-control |
| `baxy` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d4` | 0 |  | bus |

### `bedu` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 16 | not_x2 | apu-control |
| `baxy` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d7` | 0 |  | bus |

### `bumo` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 16 | not_x2 | apu-control |
| `baxy` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d5` | 0 |  | bus |

### `bafo` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 16 | not_x2 | apu-control |
| `bono` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d2` | 0 |  | bus |

### `bogu` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 16 | not_x2 | apu-control |
| `bono` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d1` | 0 |  | bus |

### `byga` (drlatch_ee) — diff=16, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 16 | not_x2 | apu-control |
| `bowe` | 15 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d1` | 0 |  | bus |


## Sprite Y Compare (26 races)

### `sobu` (dffr) — diff=15, max=24
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `teky` | 24 | and4 | ppu-ycomp |
| `tava` | 9 | not_x1 | ppu-ycomp |

### `tese` (dffr) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `seca` | 15 | nor3 | ppu-ycomp |
| `tuly` | 0 | dffr | ppu-ycomp |

### `tuly` (dffr) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `seca` | 15 | nor3 | ppu-ycomp |
| `toxe` | 0 | dffr | ppu-ycomp |

### `wone` (dlatch) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 15 | not_x1 | ppu-oam |
| `bus:~oam_b_d3` | 0 |  | bus |

### `xafu` (dlatch) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 15 | not_x1 | ppu-oam |
| `bus:~oam_b_d5` | 0 |  | bus |

### `yses` (dlatch) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 15 | not_x1 | ppu-oam |
| `bus:~oam_b_d6` | 0 |  | bus |

### `ydyv` (dlatch) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 15 | not_x1 | ppu-oam |
| `bus:~oam_b_d0` | 0 |  | bus |

### `yceb` (dlatch) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 15 | not_x1 | ppu-oam |
| `bus:~oam_b_d1` | 0 |  | bus |

### `zeca` (dlatch) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 15 | not_x1 | ppu-oam |
| `bus:~oam_b_d7` | 0 |  | bus |

### `zuca` (dlatch) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 15 | not_x1 | ppu-oam |
| `bus:~oam_b_d2` | 0 |  | bus |

### `zaxe` (dlatch) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 15 | not_x1 | ppu-oam |
| `bus:~oam_b_d4` | 0 |  | bus |

### `wyso` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `xafu` | 0 | dlatch | ppu-ycomp |

### `xote` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `yses` | 0 | dlatch | ppu-ycomp |

### `xyju` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `wone` | 0 | dlatch | ppu-ycomp |

### `xuso` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `ydyv` | 0 | dlatch | ppu-ycomp |


## Clock Distribution (21 races)

### `subu` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `sola` | 0 | dffr | clocks |

### `sola` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `teru` | 0 | dffr | clocks |

### `teka` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `subu` | 0 | dffr | clocks |

### `tama` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `unyk` | 0 | dffr | clocks |

### `tero` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `uner` | 0 | dffr | clocks |

### `teru` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `tofe` | 0 | dffr | clocks |

### `tofe` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `tugo` | 0 | dffr | clocks |

### `tulu` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `ugot` | 0 | dffr | clocks |

### `tugo` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `tulu` | 0 | dffr | clocks |

### `upof` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `uket` | 0 | dffr | clocks |

### `uket` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `teka` | 0 | dffr | clocks |

### `unyk` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `tero` | 0 | dffr | clocks |

### `uner` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `ufor` | 0 | dffr | clocks |

### `ufor` (dffr) — diff=14, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `ukup` | 0 | dffr | clocks |

### `afer` (dffr_cc) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boma` | 12 | not_x6 | clocks |
| `boga` | 11 | not_x6 | clocks |
| `upoj` | 2 | nand3 | test |
| `asol` | 0 | nor_latch | clocks |


## Serial (17 races)

### `caly` (dffr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 14 | and2 | serial |
| `cyde` | 0 | dffr | serial |

### `cyde` (dffr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 14 | and2 | serial |
| `cylo` | 0 | dffr | serial |

### `cylo` (dffr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 14 | and2 | serial |
| `cafa` | 0 | dffr | serial |

### `dovu` (dffsr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyly` | 14 | oa21 | serial |
| `dola` | 14 | nand2 | serial |
| `epyt` | 6 | not_x2 | serial |
| `dojo` | 0 | dffsr | serial |

### `dojo` (dffsr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `daju` | 14 | oa21 | serial |
| `dyge` | 14 | nand2 | serial |
| `dawe` | 8 | not_x2 | serial |
| `dyra` | 0 | dffsr | serial |

### `dyra` (dffsr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dybo` | 14 | oa21 | serial |
| `dela` | 14 | nand2 | serial |
| `dawe` | 8 | not_x2 | serial |
| `degu` | 0 | dffsr | serial |

### `degu` (dffsr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dumo` | 14 | oa21 | serial |
| `docu` | 14 | nand2 | serial |
| `dawe` | 8 | not_x2 | serial |
| `cuba` | 0 | dffsr | serial |

### `ejab` (dffsr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehuj` | 14 | oa21 | serial |
| `elok` | 14 | nand2 | serial |
| `epyt` | 6 | not_x2 | serial |
| `dovu` | 0 | dffsr | serial |

### `erod` (dffsr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efak` | 14 | oa21 | serial |
| `edel` | 14 | nand2 | serial |
| `epyt` | 6 | not_x2 | serial |
| `ejab` | 0 | dffsr | serial |

### `eder` (dffsr) — diff=14, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `eguv` | 14 | oa21 | serial |
| `efef` | 14 | nand2 | serial |
| `epyt` | 6 | not_x2 | serial |
| `erod` | 0 | dffsr | serial |

### `cuba` (dffsr) — diff=13, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cohy` | 14 | oa21 | serial |
| `cufu` | 14 | nand2 | serial |
| `dawe` | 8 | not_x2 | serial |
| `cage` | 1 | not_x1 | serial |

### `culy` (dffr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 12 | nand4 | serial |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `etaf` (dffr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 12 | nand4 | serial |
| `caby` | 5 | and2 | serial |
| `bus:d7` | 0 |  | bus |

### `coty` (dffr) — diff=11, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 12 | nand4 | serial |
| `uvyn` | 1 | not_x1 | clocks |

### `cafa` (dffr) — diff=10, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 14 | and2 | serial |
| `dawa` | 4 | or2 | serial |


## Address Bus (15 races)

### `lobu` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a12` | 0 |  | bus |

### `lumy` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a11` | 0 |  | bus |

### `luno` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a8` | 0 |  | bus |

### `lonu` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a13` | 0 |  | bus |

### `lysa` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a9` | 0 |  | bus |

### `nyre` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a14` | 0 |  | bus |

### `pate` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a10` | 0 |  | bus |

### `apur` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a1` | 0 |  | bus |

### `atev` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a5` | 0 |  | bus |

### `aros` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a6` | 0 |  | bus |

### `aret` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a3` | 0 |  | bus |

### `arym` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a7` | 0 |  | bus |

### `avys` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a4` | 0 |  | bus |

### `alor` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a0` | 0 |  | bus |

### `alyr` (dlatch) — diff=12, max=12
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 12 | not_x1 | bus-adr |
| `bus:a2` | 0 |  | bus |


## test (8 races)

### `amut` (dffr) — diff=12, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 12 | nand5 | test |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |

### `buro` (dffr) — diff=12, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 12 | nand5 | test |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `jute` (dffr) — diff=12, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `jale` (dffr) — diff=12, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d2` | 0 |  | bus |

### `kuko` (dffr) — diff=12, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d6` | 0 |  | bus |

### `kyme` (dffr) — diff=12, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d3` | 0 |  | bus |

### `keru` (dffr) — diff=12, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d7` | 0 |  | bus |

### `kecy` (dffr) — diff=12, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |


## Joypad (11 races)

### `cofy` (dffr) — diff=12, max=12
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d5` | 0 |  | bus |

### `kely` (dffr) — diff=12, max=12
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d4` | 0 |  | bus |

### `kolo` (dlatch) — diff=12, max=12
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 12 | not_x1 | joypad |
| `p13` | 0 | pad_bidir_pu | joypad |

### `kapa` (dlatch) — diff=12, max=12
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 12 | not_x1 | joypad |
| `p11` | 0 | pad_bidir_pu | joypad |

### `kevu` (dlatch) — diff=12, max=12
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 12 | not_x1 | joypad |
| `p10` | 0 | pad_bidir_pu | joypad |

### `keja` (dlatch) — diff=12, max=12
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 12 | not_x1 | joypad |
| `p12` | 0 | pad_bidir_pu | joypad |

### `apug` (dffr) — diff=11, max=11
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 11 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `agem` | 0 | dffr | joypad |

### `agem` (dffr) — diff=11, max=11
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 11 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `acef` | 0 | dffr | joypad |

### `acef` (dffr) — diff=11, max=11
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 11 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `batu` | 0 | dffr | joypad |

### `awob` (dlatch) — diff=9, max=11
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 11 | not_x6 | clocks |
| `kery` | 2 | or4 | joypad |

### `batu` (dffr) — diff=9, max=11
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 11 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `kery` | 2 | or4 | joypad |


## LCD Output (17 races)

### `meda` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `neru` | 1 | nor8 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `myta` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `noko` | 2 | and4 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `nype` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `talu` | 1 | not_x4 | ppu-lcd |
| `rutu` | 0 | dffr | ppu-lcd |

### `napo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `popu` | 0 | dffr | ppu-lcd |

### `popu` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `xyvo` | 2 | and2 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `sude` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `telu` | 0 | dffr | ppu-lcd |

### `typo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `saxo` | 0 | dffr | ppu-lcd |

### `tyry` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `taha` | 0 | dffr | ppu-lcd |

### `taha` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `sude` | 0 | dffr | ppu-lcd |

### `telu` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `vyzo` | 0 | dffr | ppu-lcd |

### `vyzo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `typo` | 0 | dffr | ppu-lcd |

### `luca` (dffr) — diff=10, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `lofu` | 1 | not_x1 | ppu-lcd |

### `saxo` (dffr) — diff=10, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `talu` | 1 | not_x4 | ppu-lcd |

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


## bootrom (1 races)

### `tepu` (dffr) — diff=10, max=12
Category: bootrom

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuge` | 12 | nand4 | bootrom |
| `alur` | 3 | not_x2 | clocks |
| `sato` | 2 | or2 | bootrom |


## Data Bus (8 races)

### `rony` (dlatch) — diff=9, max=9
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 9 | nand3 | bus-data |
| `d1` | 0 | pad_bidir_pu | bus-data |

### `raxy` (dlatch) — diff=9, max=9
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 9 | nand3 | bus-data |
| `d2` | 0 | pad_bidir_pu | bus-data |

### `rupa` (dlatch) — diff=9, max=9
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 9 | nand3 | bus-data |
| `d6` | 0 | pad_bidir_pu | bus-data |

### `selo` (dlatch) — diff=9, max=9
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 9 | nand3 | bus-data |
| `d3` | 0 | pad_bidir_pu | bus-data |

### `soma` (dlatch) — diff=9, max=9
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 9 | nand3 | bus-data |
| `d0` | 0 | pad_bidir_pu | bus-data |

### `sody` (dlatch) — diff=9, max=9
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 9 | nand3 | bus-data |
| `d4` | 0 | pad_bidir_pu | bus-data |

### `sago` (dlatch) — diff=9, max=9
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 9 | nand3 | bus-data |
| `d5` | 0 | pad_bidir_pu | bus-data |

### `sazy` (dlatch) — diff=9, max=9
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 9 | nand3 | bus-data |
| `d7` | 0 | pad_bidir_pu | bus-data |


## OAM Interface (1 races)

### `maka` (dffr) — diff=4, max=6
Category: ppu-oam

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zeme` | 6 | not_x4 | ppu-control |
| `cunu` | 5 | not_x2 | ppu-control |
| `caty` | 2 | not_x1 | ppu-oam |


## VRAM Interface (8 races)

### `md7` (pad_bidir_pu) — diff=3, max=29
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryze` | 29 | not_x2 | ppu-vram |
| `rady` | 28 | not_x2 | ppu-vram |
| `rofa` | 26 | not_x2 | ppu-vram |

### `md6` (pad_bidir_pu) — diff=3, max=29
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `reku` | 29 | not_x2 | ppu-vram |
| `ryty` | 28 | not_x2 | ppu-vram |
| `rofa` | 26 | not_x2 | ppu-vram |

### `md5` (pad_bidir_pu) — diff=3, max=29
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `revu` | 29 | not_x2 | ppu-vram |
| `rumu` | 28 | not_x2 | ppu-vram |
| `rofa` | 26 | not_x2 | ppu-vram |

### `md4` (pad_bidir_pu) — diff=3, max=29
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryro` | 29 | not_x2 | ppu-vram |
| `rube` | 28 | not_x2 | ppu-vram |
| `rofa` | 26 | not_x2 | ppu-vram |

### `md3` (pad_bidir_pu) — diff=3, max=29
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rada` | 29 | not_x2 | ppu-vram |
| `rodu` | 28 | not_x2 | ppu-vram |
| `rofa` | 26 | not_x2 | ppu-vram |

### `md2` (pad_bidir_pu) — diff=3, max=29
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `razo` | 29 | not_x2 | ppu-vram |
| `rare` | 28 | not_x2 | ppu-vram |
| `rofa` | 26 | not_x2 | ppu-vram |

### `md1` (pad_bidir_pu) — diff=3, max=29
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryky` | 29 | not_x2 | ppu-vram |
| `ruly` | 28 | not_x2 | ppu-vram |
| `rofa` | 26 | not_x2 | ppu-vram |

### `md0` (pad_bidir_pu) — diff=3, max=29
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rege` | 29 | not_x2 | ppu-vram |
| `rura` | 28 | not_x2 | ppu-vram |
| `rofa` | 26 | not_x2 | ppu-vram |
