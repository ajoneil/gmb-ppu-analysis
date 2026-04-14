# Signal Race Pair Analysis

Total race pairs identified: 781

Race pairs are registered nodes where data inputs arrive at significantly
different combinatorial depths (diff >= 3 gates, max >= 4). On real hardware,
the late-arriving signal may not settle before the register samples, causing
behavior to differ from behavioral emulation by one dot.

PPU-related races: 439


## apu-ch1 (72 races)

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

### `boko` (drlatch_ee) — diff=18, max=17
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bamu` | 17 | not_x1 | apu-ch1 |
| `bage` | 16 | nand2 | apu-ch1 |
| `bus:d6` | 0 |  | bus |
| `camy` | -1 | not_x1 | apu-ch1 |

### `adek` (drlatch_ee) — diff=17, max=16
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 16 | not_x2 | apu-ch1 |
| `cenu` | 15 | and2 | apu-ch1 |
| `bus:d4` | 0 |  | bus |
| `agur` | -1 | not_x1 | apu-control |

### `avaf` (drlatch_ee) — diff=17, max=16
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ahyc` | 16 | not_x2 | apu-ch1 |
| `cenu` | 15 | and2 | apu-ch1 |
| `bus:d3` | 0 |  | bus |
| `agur` | -1 | not_x1 | apu-control |


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
| `doku` | 11 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `ceso` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 11 | not_x1 | ppu-xprio |
| `arop` | 1 | not_x1 | ppu-xcomp |

### `cywe` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `exyr` | 44 | not_x1 | ppu-objctl |
| `cyla` | 43 | not_x1 | ppu-objctl |
| `ejad` | 11 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `cuvy` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `exyr` | 44 | not_x1 | ppu-objctl |
| `cyla` | 43 | not_x1 | ppu-objctl |
| `ejad` | 11 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `dake` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 11 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `dyfu` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 11 | not_x1 | ppu-xprio |
| `xatu` | 1 | not_x1 | ppu-xcomp |

### `dazo` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 11 | not_x1 | ppu-xprio |
| `yvok` | 1 | not_x1 | ppu-xcomp |

### `dury` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `exyr` | 44 | not_x1 | ppu-objctl |
| `cyla` | 43 | not_x1 | ppu-objctl |
| `ejad` | 11 | not_x1 | ppu-xprio |
| `xatu` | 1 | not_x1 | ppu-xcomp |

### `desu` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 11 | not_x1 | ppu-xprio |
| `ypur` | 1 | not_x1 | ppu-xcomp |

### `duko` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 11 | not_x1 | ppu-xprio |
| `zocy` | 1 | not_x1 | ppu-xcomp |

### `dany` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `camo` | 44 | not_x1 | ppu-objctl |
| `asys` | 43 | not_x1 | ppu-objctl |
| `doku` | 11 | not_x1 | ppu-xprio |
| `zago` | 1 | not_x1 | ppu-xcomp |

### `dyby` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `exyr` | 44 | not_x1 | ppu-objctl |
| `cyla` | 43 | not_x1 | ppu-objctl |
| `ejad` | 11 | not_x1 | ppu-xprio |
| `arop` | 1 | not_x1 | ppu-xcomp |

### `depy` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 44 | not_x1 | ppu-objctl |
| `cacu` | 43 | not_x1 | ppu-objctl |
| `gamy` | 11 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `duhy` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 44 | not_x1 | ppu-objctl |
| `cacu` | 43 | not_x1 | ppu-objctl |
| `gamy` | 11 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `epum` (drlatch_ee) — diff=43, max=44
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `deha` | 44 | not_x1 | ppu-objctl |
| `gecy` | 43 | not_x1 | ppu-objctl |
| `gafy` | 11 | not_x1 | ppu-xprio |
| `zocy` | 1 | not_x1 | ppu-xcomp |


## Sprite Control (13 races)

### `dezy` (dffr) — diff=40, max=39
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyty` | 39 | not_x2 | ppu-objctl |
| `xapo` | -1 | not_x2 | ppu-control |
| `zeme` | -1 | not_x4 | ppu-control |

### `besu` (nor_latch) — diff=11, max=11
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `asen` | 11 | or2 | ppu-objctl |
| `catu` | 0 | dffr | ppu-objctl |

### `byba` (dffr) — diff=8, max=7
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bagy` | 7 | not_x1 | ppu-objctl |
| `feto` | 2 | and4 | ppu-objctl |
| `xupy` | -1 | not_x2 | ppu-oam |

### `doba` (dffr) — diff=8, max=7
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bagy` | 7 | not_x1 | ppu-objctl |
| `byba` | 0 | dffr | ppu-objctl |
| `alet` | -1 | not_x2 | ppu-control |

### `catu` (dffr) — diff=6, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `abov` | 5 | and2 | ppu-objctl |
| `xupy` | -1 | not_x2 | ppu-oam |
| `abez` | -1 | not_x1 | ppu-objctl |

### `bego` (dffr) — diff=5, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 5 | not_x1 | ppu-objctl |
| `cuxy` | 0 | dffr | ppu-objctl |

### `cuxy` (dffr) — diff=5, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 5 | not_x1 | ppu-objctl |
| `bese` | 0 | dffr | ppu-objctl |

### `dybe` (dffr) — diff=5, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 5 | not_x1 | ppu-objctl |
| `bego` | 0 | dffr | ppu-objctl |

### `elyn` (dffr) — diff=5, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 5 | nor2 | ppu-objctl |
| `goso` | 0 | dffr | ppu-objctl |

### `fony` (dffr) — diff=5, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 5 | nor2 | ppu-objctl |
| `faha` | 0 | dffr | ppu-objctl |

### `faha` (dffr) — diff=5, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 5 | nor2 | ppu-objctl |
| `elyn` | 0 | dffr | ppu-objctl |

### `goso` (dffr) — diff=5, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 5 | nor2 | ppu-objctl |
| `wewy` | 0 | dffr | ppu-objctl |

### `wewy` (dffr) — diff=5, max=5
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 5 | nor2 | ppu-objctl |
| `yfel` | 0 | dffr | ppu-objctl |


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
| `wovu` | 8 | not_x2 | ppu-oam |
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
| `wovu` | 8 | not_x2 | ppu-oam |
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


## bus (38 races)

### `bus:~ma9` () — diff=31, max=32
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dafe` | 32 | not_if0 | ppu-bgscroll |
| `rese` | 1 | not_if0 | ppu-vram |
| `vulo` | 1 | not_if0 | ppu-window |
| `reso` | 1 | not_if1 | ppu-bgfifo |
| `gotu` | 1 | not_if0 | ppu-ycomp |
| `duve` | 1 | not_if0 | ppu-dma |

### `bus:~ma4` () — diff=31, max=32
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ajan` | 32 | not_if0 | ppu-bgscroll |
| `famu` | 7 | not_if0 | ppu-ycomp |
| `xeca` | 1 | not_if0 | ppu-vram |
| `damu` | 1 | not_if0 | ppu-dma |
| `vapy` | 1 | not_if1 | ppu-bgfifo |
| `wuju` | 1 | not_if0 | ppu-window |

### `bus:~ma8` () — diff=27, max=28
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ceta` | 28 | not_if0 | ppu-bgscroll |
| `wune` | 1 | not_if0 | ppu-ycomp |
| `rysu` | 1 | not_if0 | ppu-vram |
| `roha` | 1 | not_if1 | ppu-bgfifo |
| `vovo` | 1 | not_if0 | ppu-window |
| `evax` | 1 | not_if0 | ppu-dma |

### `bus:~ma3` () — diff=27, max=28
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `coly` | 28 | not_if0 | ppu-bgscroll |
| `dode` | 12 | not_if0 | ppu-bgscroll |
| `agag` | 5 | not_if0 | ppu-ycomp |
| `xody` | 1 | not_if0 | ppu-vram |
| `fyzy` | 1 | not_if0 | ppu-dma |
| `xulo` | 1 | not_if0 | ppu-window |
| `wolu` | 1 | not_if0 | ppu-window |

### `bus:~ma7` () — diff=23, max=24
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cypo` | 24 | not_if0 | ppu-bgscroll |
| `rusa` | 1 | not_if1 | ppu-bgfifo |
| `xybo` | 1 | not_if0 | ppu-vram |
| `erew` | 1 | not_if0 | ppu-dma |
| `vace` | 1 | not_if0 | ppu-window |
| `wyga` | 1 | not_if0 | ppu-ycomp |

### `bus:~ma2` () — diff=23, max=24
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `alel` | 24 | not_if0 | ppu-bgscroll |
| `dahu` | 8 | not_if0 | ppu-bgscroll |
| `aras` | 5 | not_if0 | ppu-ycomp |
| `fuhe` | 1 | not_if0 | ppu-dma |
| `xahe` | 1 | not_if0 | ppu-window |
| `wawe` | 1 | not_if0 | ppu-window |
| `xyne` | 1 | not_if0 | ppu-vram |

### `bus:~ma6` () — diff=19, max=20
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `case` | 20 | not_if0 | ppu-bgscroll |
| `vejy` | 1 | not_if1 | ppu-bgfifo |
| `gavo` | 1 | not_if0 | ppu-ycomp |
| `xopo` | 1 | not_if0 | ppu-vram |
| `eteg` | 1 | not_if0 | ppu-dma |
| `veha` | 1 | not_if0 | ppu-window |

### `bus:~ma1` () — diff=19, max=20
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `afeb` | 20 | not_if0 | ppu-bgscroll |
| `baxe` | 5 | not_if0 | ppu-ycomp |
| `evad` | 4 | not_if0 | ppu-bgscroll |
| `egez` | 1 | not_if0 | ppu-dma |
| `wudo` | 1 | not_if0 | ppu-window |
| `xamo` | 1 | not_if0 | ppu-window |
| `xuxu` | 1 | not_if0 | ppu-vram |

### `bus:sprite_y_store3` () — diff=18, max=19
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wenu` | 19 | not_if0 | ppu-ycomp |
| `zudo` | 1 | not_if0 | ppu-objreg |
| `cawo` | 1 | not_if0 | ppu-objreg |
| `awat` | 1 | not_if0 | ppu-objreg |
| `zaby` | 1 | not_if0 | ppu-objreg |
| `wehe` | 1 | not_if0 | ppu-objreg |
| `bujy` | 1 | not_if0 | ppu-objreg |
| `wana` | 1 | not_if0 | ppu-objreg |
| `befe` | 1 | not_if0 | ppu-objreg |
| `zypo` | 1 | not_if0 | ppu-objreg |
| `bydo` | 1 | not_if0 | ppu-objreg |

### `bus:~ma5` () — diff=15, max=16
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `duho` | 16 | not_if0 | ppu-bgscroll |
| `fugy` | 1 | not_if0 | ppu-ycomp |
| `dava` | 1 | not_if0 | ppu-dma |
| `vyto` | 1 | not_if0 | ppu-window |
| `xoba` | 1 | not_if0 | ppu-vram |
| `sezu` | 1 | not_if1 | ppu-bgfifo |

### `bus:~ma0` () — diff=15, max=16
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `axep` | 16 | not_if0 | ppu-bgscroll |
| `asum` | 3 | not_if0 | ppu-bgscroll |
| `xonu` | 3 | not_if0 | ppu-window |
| `abem` | 2 | not_if0 | ppu-ycomp |
| `xeja` | 1 | not_if0 | ppu-window |
| `ecal` | 1 | not_if0 | ppu-dma |
| `xaky` | 1 | not_if0 | ppu-vram |

### `bus:sprite_y_store2` () — diff=14, max=15
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cega` | 15 | not_if0 | ppu-ycomp |
| `ajal` | 1 | not_if0 | ppu-objreg |
| `zyto` | 1 | not_if0 | ppu-objreg |
| `bove` | 1 | not_if0 | ppu-objreg |
| `yjem` | 1 | not_if0 | ppu-objreg |
| `wuxe` | 1 | not_if0 | ppu-objreg |
| `bodu` | 1 | not_if0 | ppu-objreg |
| `baco` | 1 | not_if0 | ppu-objreg |
| `wabu` | 1 | not_if0 | ppu-objreg |
| `ahac` | 1 | not_if0 | ppu-objreg |
| `coho` | 1 | not_if0 | ppu-objreg |

### `bus:sprite_y_store1` () — diff=10, max=11
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cuca` | 11 | not_if0 | ppu-ycomp |
| `gate` | 1 | not_if0 | ppu-objreg |
| `were` | 1 | not_if0 | ppu-objreg |
| `buky` | 1 | not_if0 | ppu-objreg |
| `ahum` | 1 | not_if0 | ppu-objreg |
| `buja` | 1 | not_if0 | ppu-objreg |
| `bevy` | 1 | not_if0 | ppu-objreg |
| `ypoz` | 1 | not_if0 | ppu-objreg |
| `ykoz` | 1 | not_if0 | ppu-objreg |
| `ywav` | 1 | not_if0 | ppu-objreg |
| `bazu` | 1 | not_if0 | ppu-objreg |

### `bus:d0` () — diff=7, max=6
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cpu` | 6 | sm83 |  |
| `tuty` | 3 | buf_if0 | bus-data |
| `teby` | 3 | not_if1 | ppu-stat |
| `xaca` | 2 | buf_if0 | ppu-xcomp |
| `dugu` | 2 | not_if1 | apu-ch3 |
| `ruga` | 2 | not_if1 | ppu-vram |
| `coto` | 2 | not_if0 | apu-control |
| `yfap` | 2 | buf_if0 | ppu-ycomp |
| `vega` | 2 | not_if0 | ppu-stat |
| `sete` | 1 | not_if1 | timer |
| `dopa` | 1 | not_if0 | apu-ch1 |
| `ware` | 1 | not_if0 | ppu-bgscroll |
| `amyd` | 1 | not_if0 | apu-ch1 |
| `xary` | 1 | not_if0 | ppu-pal |
| `soku` | 1 | not_if1 | timer |
| `edos` | 1 | not_if0 | ppu-bgscroll |
| `raro` | 1 | not_if0 | ppu-pal |
| `foru` | 1 | not_if0 | apu-ch1 |
| `buzu` | 1 | not_if0 | apu-control |
| `laju` | 1 | not_if0 | ppu-pal |
| `punu` | 1 | not_if0 | ppu-window |
| `retu` | 1 | not_if0 | ppu-stat |
| `nela` | 1 | not_if1 | int |
| `ryma` | 1 | not_if0 | bus-data |
| `jyne` | 1 | not_if0 | apu-ch1 |
| `fava` | 1 | not_if0 | apu-ch2 |
| `jofo` | 1 | not_if0 | apu-ch3 |
| `poly` | 1 | not_if1 | ppu-dma |
| `cugy` | 1 | not_if1 | serial |
| `core` | 1 | not_if1 | serial |
| `kamo` | 1 | not_if0 | apu-ch4 |
| `akod` | 1 | not_if0 | apu-control |
| `fapy` | 1 | not_if0 | apu-ch3 |
| `sypu` | 1 | not_if1 | bootrom |
| `juvy` | 1 | not_if0 | apu-ch3 |
| `lova` | 1 | not_if0 | ppu-window |
| `huna` | 1 | not_if0 | apu-ch2 |
| `kema` | 1 | not_if0 | joypad |
| `huvu` | 1 | not_if0 | apu-ch2 |
| `ryla` | 1 | not_if1 | timer |
| `wypo` | 1 | not_if0 | ppu-control |
| `demy` | 1 | not_if0 | apu-ch4 |
| `high_ram` | 0 | high_ram |  |
| `boot_rom` | 0 | boot_rom |  |
| `tovu` | -1 | buf_if0 | bus-data |
| `tawu` | -1 | not_if1 | clocks |
| `romy` | -1 | not_if1 | bus-data |
| `atel` | -1 | not_if0 | apu-ch4 |
| `anoc` | -1 | not_if0 |  |

### `bus:d1` () — diff=7, max=6
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cpu` | 6 | sm83 |  |
| `wuga` | 5 | not_if1 | ppu-stat |
| `sywa` | 3 | buf_if0 | bus-data |
| `wuva` | 2 | not_if0 | ppu-stat |
| `desy` | 2 | not_if1 | apu-ch3 |
| `efus` | 2 | not_if0 | apu-control |
| `xagu` | 2 | buf_if0 | ppu-xcomp |
| `rota` | 2 | not_if1 | ppu-vram |
| `xele` | 2 | buf_if0 | ppu-ycomp |
| `hyre` | 1 | not_if0 | apu-ch2 |
| `nabo` | 1 | not_if1 | int |
| `rote` | 1 | not_if1 | timer |
| `ruvo` | 1 | not_if0 | bus-data |
| `capu` | 1 | not_if0 | apu-control |
| `kuro` | 1 | not_if0 | joypad |
| `jura` | 1 | not_if0 | apu-ch3 |
| `ekob` | 1 | not_if0 | ppu-bgscroll |
| `jaro` | 1 | not_if0 | apu-ch2 |
| `fajy` | 1 | not_if0 | apu-ch2 |
| `jaca` | 1 | not_if0 | apu-ch1 |
| `dude` | 1 | not_if1 | serial |
| `gefu` | 1 | not_if0 | apu-ch1 |
| `xoke` | 1 | not_if0 | ppu-pal |
| `muka` | 1 | not_if0 | ppu-window |
| `goba` | 1 | not_if0 | ppu-bgscroll |
| `coce` | 1 | not_if0 | apu-ch4 |
| `awed` | 1 | not_if0 | apu-control |
| `kaku` | 1 | not_if0 | apu-ch4 |
| `racy` | 1 | not_if1 | timer |
| `rofo` | 1 | not_if1 | ppu-dma |
| `pyre` | 1 | not_if1 | timer |
| `kafu` | 1 | not_if0 | apu-ch3 |
| `lepa` | 1 | not_if0 | ppu-pal |
| `vojo` | 1 | not_if0 | ppu-stat |
| `paba` | 1 | not_if0 | ppu-pal |
| `xero` | 1 | not_if0 | ppu-control |
| `poda` | 1 | not_if0 | ppu-window |
| `demu` | 1 | not_if0 | apu-ch1 |
| `faro` | 1 | not_if0 | apu-ch3 |
| `atax` | 1 | not_if0 | apu-ch1 |
| `high_ram` | 0 | high_ram |  |
| `boot_rom` | 0 | boot_rom |  |
| `ryne` | -1 | not_if1 | bus-data |
| `ataj` | -1 | not_if0 |  |
| `sosa` | -1 | buf_if0 | bus-data |
| `taku` | -1 | not_if1 | clocks |


## Sprite X Priority (10 races)

### `fono` (dffr) — diff=23, max=27
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guze` | 27 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `exuq` (dffr) — diff=21, max=25
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `foxa` | 25 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `wapo` (dffr) — diff=19, max=23
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gutu` | 23 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `womy` (dffr) — diff=17, max=21
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xoja` | 21 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `wafy` (dffr) — diff=15, max=19
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gega` | 19 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `xudy` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gono` | 17 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `gota` (dffr) — diff=11, max=15
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gyfy` | 15 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `egav` (dffr) — diff=9, max=13
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `emol` | 13 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `cedy` (dffr) — diff=7, max=11
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `enut` | 11 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `eboj` (dffr) — diff=4, max=8
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guva` | 8 | nor2 | ppu-xprio |
| `byva` | 7 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |


## STAT/LY (24 races)

### `rupo` (nor_latch) — diff=18, max=18
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pago` | 18 | or2 | ppu-stat |
| `ropo` | 0 | dffr | ppu-stat |

### `raha` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `bus:d7` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `rugu` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 17 | not_x1 | ppu-stat |
| `ryve` | 16 | not_x1 | ppu-stat |
| `bus:d6` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `roxe` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 17 | not_x1 | ppu-stat |
| `ryve` | 16 | not_x1 | ppu-stat |
| `bus:d3` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `rufo` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 17 | not_x1 | ppu-stat |
| `ryve` | 16 | not_x1 | ppu-stat |
| `bus:d4` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `refe` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 17 | not_x1 | ppu-stat |
| `ryve` | 16 | not_x1 | ppu-stat |
| `bus:d5` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `sedy` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `bus:d2` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `syry` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `bus:d0` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `salo` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `bus:d3` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `sota` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `bus:d4` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `vuce` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `bus:d1` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `vafa` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `bus:d5` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `vevo` (drlatch_ee) — diff=18, max=17
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 17 | not_x1 | ppu-stat |
| `wane` | 16 | not_x1 | ppu-stat |
| `bus:d6` | 0 |  | bus |
| `wesy` | -1 | not_x2 | ppu-stat |

### `voga` (dffr) — diff=14, max=13
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wodu` | 13 | and2 | ppu-stat |
| `tady` | 5 | nor2 | ppu-stat |
| `alet` | -1 | not_x2 | ppu-control |

### `xymu` (nor_latch) — diff=7, max=9
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `avap` | 9 | not_x2 | ppu-objctl |
| `wego` | 2 | or2 | ppu-stat |


## Window Logic (29 races)

### `mypu` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `bus:d4` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `muvo` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `bus:d6` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `mypa` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `bus:d0` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `myce` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `bus:d5` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `meby` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `bus:d3` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `mela` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `bus:d3` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `nofe` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `bus:d1` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `nuku` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `bus:d7` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `noke` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 17 | not_x1 | ppu-window |
| `voxu` | 16 | not_x1 | ppu-window |
| `bus:d2` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `nafu` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `bus:d7` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `nyro` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `bus:d1` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `naga` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `bus:d2` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `nulo` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `bus:d4` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `nuka` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `bus:d6` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |

### `nene` (drlatch_ee) — diff=18, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 17 | not_x1 | ppu-window |
| `vefu` | 16 | not_x1 | ppu-window |
| `bus:d5` | 0 |  | bus |
| `walu` | -1 | not_x2 | ppu-window |


## PPU Control (8 races)

### `vyxe` (drlatch_ee) — diff=18, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `bus:d0` | 0 |  | bus |
| `xare` | -1 | not_x1 | ppu-control |

### `woky` (drlatch_ee) — diff=18, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `bus:d6` | 0 |  | bus |
| `xare` | -1 | not_x1 | ppu-control |

### `wexu` (drlatch_ee) — diff=18, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `bus:d4` | 0 |  | bus |
| `xare` | -1 | not_x1 | ppu-control |

### `wymo` (drlatch_ee) — diff=18, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `bus:d5` | 0 |  | bus |
| `xare` | -1 | not_x1 | ppu-control |

### `xona` (drlatch_ee) — diff=18, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `bus:d7` | 0 |  | bus |
| `xare` | -1 | not_x1 | ppu-control |

### `xylo` (drlatch_ee) — diff=18, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `bus:d1` | 0 |  | bus |
| `xare` | -1 | not_x1 | ppu-control |

### `xafo` (drlatch_ee) — diff=18, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `bus:d3` | 0 |  | bus |
| `xare` | -1 | not_x1 | ppu-control |

### `xymo` (drlatch_ee) — diff=18, max=17
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 17 | not_x1 | ppu-control |
| `xubo` | 16 | not_x1 | ppu-control |
| `bus:d2` | 0 |  | bus |
| `xare` | -1 | not_x1 | ppu-control |


## BG Scrolling (16 races)

### `bemy` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `bus:d4` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `bake` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `bus:d7` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `cuzy` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `bus:d5` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `cabu` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `bus:d6` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `cyxu` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `bus:d2` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `duzu` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `bus:d1` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `daty` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `bus:d0` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `dede` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `bus:d4` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `foha` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `bus:d6` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `funy` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `bus:d7` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `fujo` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `bus:d3` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `foty` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `bus:d5` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `fezu` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `bus:d2` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `fymo` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 17 | not_x1 | ppu-bgscroll |
| `cavo` | 16 | not_x1 | ppu-bgscroll |
| `bus:d1` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |

### `gubo` (drlatch_ee) — diff=18, max=17
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 17 | not_x1 | ppu-bgscroll |
| `amun` | 16 | not_x1 | ppu-bgscroll |
| `bus:d3` | 0 |  | bus |
| `cunu` | -1 | not_x2 | ppu-control |


## apu-ch4 (27 races)

### `cuny` (drlatch_ee) — diff=18, max=17
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cazo` | 17 | not_x1 | apu-ch4 |
| `dulu` | 16 | nand2 | apu-ch4 |
| `bus:d6` | 0 |  | bus |
| `cabe` | -1 | not_x1 | apu-ch4 |

### `etyj` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 16 | not_x1 | apu-ch4 |
| `daco` | 15 | and2 | apu-ch4 |
| `bus:d1` | 0 |  | bus |
| `fexo` | -1 | not_x1 | apu-ch4 |

### `ezyk` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 16 | not_x1 | apu-ch4 |
| `daco` | 15 | and2 | apu-ch4 |
| `bus:d2` | 0 |  | bus |
| `fexo` | -1 | not_x1 | apu-ch4 |

### `emok` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 16 | not_x1 | apu-ch4 |
| `daco` | 15 | and2 | apu-ch4 |
| `bus:d0` | 0 |  | bus |
| `fexo` | -1 | not_x1 | apu-ch4 |

### `fyto` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 16 | not_x2 | apu-ch4 |
| `getu` | 15 | and2 | apu-ch4 |
| `bus:d5` | 0 |  | bus |
| `dapa` | -1 | not_x2 | apu-control |

### `feta` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 16 | not_x2 | apu-ch4 |
| `getu` | 15 | and2 | apu-ch4 |
| `bus:d4` | 0 |  | bus |
| `dapa` | -1 | not_x2 | apu-control |

### `gafo` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 16 | not_x2 | apu-ch4 |
| `getu` | 15 | and2 | apu-ch4 |
| `bus:d7` | 0 |  | bus |
| `dapa` | -1 | not_x2 | apu-control |

### `gogo` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 16 | not_x2 | apu-ch4 |
| `getu` | 15 | and2 | apu-ch4 |
| `bus:d6` | 0 |  | bus |
| `dapa` | -1 | not_x2 | apu-control |

### `garu` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `bus:d4` | 0 |  | bus |
| `fexo` | -1 | not_x1 | apu-ch4 |

### `geky` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `bus:d3` | 0 |  | bus |
| `fexo` | -1 | not_x1 | apu-ch4 |

### `gedu` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `bus:d7` | 0 |  | bus |
| `fexo` | -1 | not_x1 | apu-ch4 |

### `goky` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `bus:d5` | 0 |  | bus |
| `fexo` | -1 | not_x1 | apu-ch4 |

### `gozo` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 16 | not_x2 | apu-ch4 |
| `goko` | 15 | and2 | apu-ch4 |
| `bus:d6` | 0 |  | bus |
| `fexo` | -1 | not_x1 | apu-ch4 |

### `jero` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 16 | not_x2 | apu-ch4 |
| `humo` | 15 | and2 | apu-ch4 |
| `bus:d1` | 0 |  | bus |
| `kame` | -1 | not_x1 | apu-control |

### `jaky` (drlatch_ee) — diff=17, max=16
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 16 | not_x2 | apu-ch4 |
| `humo` | 15 | and2 | apu-ch4 |
| `bus:d2` | 0 |  | bus |
| `kame` | -1 | not_x1 | apu-control |


## apu-ch2 (42 races)

### `emer` (drlatch_ee) — diff=18, max=17
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `duso` | 17 | not_x1 | apu-ch2 |
| `evyf` | 16 | nand2 | apu-ch2 |
| `bus:d6` | 0 |  | bus |
| `fazo` | -1 | not_x1 | apu-ch2 |

### `bamy` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `budu` | 16 | not_x1 | apu-ch2 |
| `bacu` | 15 | and2 | apu-ch2 |
| `bus:d7` | 0 |  | bus |
| `afat` | -1 | not_x1 | apu-control |

### `bera` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `budu` | 16 | not_x1 | apu-ch2 |
| `bacu` | 15 | and2 | apu-ch2 |
| `bus:d6` | 0 |  | bus |
| `afat` | -1 | not_x1 | apu-control |

### `fofe` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `bus:d0` | 0 |  | bus |
| `hude` | -1 | not_x1 | apu-ch2 |

### `fova` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `bus:d1` | 0 |  | bus |
| `hude` | -1 | not_x1 | apu-ch2 |

### `fedy` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `bus:d2` | 0 |  | bus |
| `hude` | -1 | not_x1 | apu-ch2 |

### `fome` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `bus:d3` | 0 |  | bus |
| `hude` | -1 | not_x1 | apu-ch2 |

### `fora` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 16 | not_x2 | apu-ch2 |
| `dosa` | 15 | and2 | apu-ch2 |
| `bus:d4` | 0 |  | bus |
| `hude` | -1 | not_x1 | apu-ch2 |

### `fore` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `bus:d3` | 0 |  | bus |
| `jybu` | -1 | not_x1 | apu-ch2 |

### `goda` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 16 | not_x1 | apu-ch2 |
| `exuc` | 15 | and2 | apu-ch2 |
| `bus:d5` | 0 |  | bus |
| `hude` | -1 | not_x1 | apu-ch2 |

### `gumy` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 16 | not_x1 | apu-ch2 |
| `exuc` | 15 | and2 | apu-ch2 |
| `bus:d6` | 0 |  | bus |
| `hude` | -1 | not_x1 | apu-ch2 |

### `gupu` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 16 | not_x1 | apu-ch2 |
| `exuc` | 15 | and2 | apu-ch2 |
| `bus:d7` | 0 |  | bus |
| `hude` | -1 | not_x1 | apu-ch2 |

### `gata` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `bus:d4` | 0 |  | bus |
| `jybu` | -1 | not_x1 | apu-ch2 |

### `gura` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `bus:d6` | 0 |  | bus |
| `jybu` | -1 | not_x1 | apu-ch2 |

### `gufe` (drlatch_ee) — diff=17, max=16
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `bus:d5` | 0 |  | bus |
| `jybu` | -1 | not_x1 | apu-ch2 |


## apu-ch3 (39 races)

### `hoto` (drlatch_ee) — diff=18, max=17
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gygu` | 17 | not_x1 | apu-ch3 |
| `fovo` | 16 | nand2 | apu-ch3 |
| `bus:d6` | 0 |  | bus |
| `heky` | -1 | not_x1 | apu-ch3 |

### `gage` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 16 | not_x2 | apu-ch2 |
| `enuf` | 15 | and2 | apu-ch2 |
| `bus:d7` | 0 |  | bus |
| `jybu` | -1 | not_x1 | apu-ch2 |

### `guxe` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gucy` | 16 | not_x1 | apu-ch3 |
| `gejo` | 15 | and2 | apu-ch3 |
| `bus:d7` | 0 |  | bus |
| `gove` | -1 | not_x1 | apu-ch3 |

### `hody` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guzu` | 16 | not_x1 | apu-ch3 |
| `haga` | 15 | and2 | apu-ch3 |
| `bus:d5` | 0 |  | bus |
| `guro` | -1 | not_x1 | apu-ch3 |

### `huky` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guzu` | 16 | not_x1 | apu-ch3 |
| `haga` | 15 | and2 | apu-ch3 |
| `bus:d6` | 0 |  | bus |
| `guro` | -1 | not_x1 | apu-ch3 |

### `jety` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 16 | not_x1 | apu-ch3 |
| `huda` | 15 | and2 | apu-ch3 |
| `bus:d1` | 0 |  | bus |
| `kopy` | -1 | not_x1 | apu-ch3 |

### `jemo` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 16 | not_x1 | apu-ch3 |
| `huda` | 15 | and2 | apu-ch3 |
| `bus:d0` | 0 |  | bus |
| `kopy` | -1 | not_x1 | apu-ch3 |

### `jacy` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 16 | not_x1 | apu-ch3 |
| `huda` | 15 | and2 | apu-ch3 |
| `bus:d2` | 0 |  | bus |
| `kopy` | -1 | not_x1 | apu-ch3 |

### `jovy` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `bus:d1` | 0 |  | bus |
| `kuha` | -1 | not_x1 | apu-ch3 |

### `jypo` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `bus:d4` | 0 |  | bus |
| `kuha` | -1 | not_x1 | apu-ch3 |

### `jefe` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `bus:d3` | 0 |  | bus |
| `kuha` | -1 | not_x1 | apu-ch3 |

### `jaxa` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `bus:d2` | 0 |  | bus |
| `kuha` | -1 | not_x1 | apu-ch3 |

### `jove` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 16 | not_x1 | apu-ch3 |
| `kota` | 15 | and2 | apu-ch3 |
| `bus:d5` | 0 |  | bus |
| `kuha` | -1 | not_x1 | apu-ch3 |

### `koga` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 16 | not_x2 | apu-ch3 |
| `jafa` | 15 | and2 | apu-ch3 |
| `bus:d0` | 0 |  | bus |
| `kuha` | -1 | not_x1 | apu-ch3 |

### `kogu` (drlatch_ee) — diff=17, max=16
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 16 | not_x1 | apu-ch3 |
| `kota` | 15 | and2 | apu-ch3 |
| `bus:d7` | 0 |  | bus |
| `kuha` | -1 | not_x1 | apu-ch3 |


## DMA (12 races)

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

### `luvy` (dffr) — diff=17, max=16
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lupa` | 16 | nor2 | ppu-dma |
| `uvyt` | -1 | not_x2 | clocks |
| `cunu` | -1 | not_x2 | ppu-control |

### `wuje` (nor_latch) — diff=16, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xuto` | 15 | and2 | ppu-oam |
| `xyny` | -1 | not_x1 | ppu-dma |

### `lyxe` (nor_latch) — diff=14, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavy` | 15 | and2 | ppu-dma |
| `loko` | 1 | nand2 | ppu-dma |

### `naky` (dffr) — diff=5, max=4
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `meta` | 4 | and2 | ppu-dma |
| `lapa` | -1 | not_x1 | ppu-dma |


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


## Timer (20 races)

### `nydu` (dffr) — diff=17, max=16
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mugy` | 16 | not_x1 | timer |
| `nuga` | 0 | tffnl | timer |
| `boga` | -1 | not_x6 | clocks |

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

### `rega` (tffnl) — diff=14, max=15
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 15 | nand3 | timer |
| `puxy` | 15 | nor2 | timer |
| `sogu` | 1 | nor2 | timer |

### `muru` (dffr) — diff=13, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `bus:d2` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `nyke` (dffr) — diff=13, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `bus:d1` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `peto` (dffr) — diff=13, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `bus:d6` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `sufy` (dffr) — diff=13, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `bus:d5` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `sabu` (dffr) — diff=13, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `bus:d0` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `seta` (dffr) — diff=13, max=12
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 12 | nand4 | timer |
| `bus:d7` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |


## apu-control (19 races)

### `anev` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 16 | not_x2 | apu-control |
| `bono` | 15 | not_x2 | apu-control |
| `bus:d0` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `atuf` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 16 | not_x2 | apu-control |
| `bono` | 15 | not_x2 | apu-control |
| `bus:d3` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `apeg` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 16 | not_x2 | apu-control |
| `bowe` | 15 | not_x2 | apu-control |
| `bus:d0` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `apos` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 16 | not_x2 | apu-control |
| `bowe` | 15 | not_x2 | apu-control |
| `bus:d3` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `ager` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 16 | not_x2 | apu-control |
| `bowe` | 15 | not_x2 | apu-control |
| `bus:d2` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `bepu` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 16 | not_x2 | apu-control |
| `byfa` | 15 | not_x2 | apu-control |
| `bus:d7` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `befo` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 16 | not_x2 | apu-control |
| `byfa` | 15 | not_x2 | apu-control |
| `bus:d6` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `bume` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 16 | not_x2 | apu-control |
| `byfa` | 15 | not_x2 | apu-control |
| `bus:d4` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `bofa` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 16 | not_x2 | apu-control |
| `byfa` | 15 | not_x2 | apu-control |
| `bus:d5` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `byre` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 16 | not_x2 | apu-control |
| `baxy` | 15 | not_x2 | apu-control |
| `bus:d4` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `bedu` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 16 | not_x2 | apu-control |
| `baxy` | 15 | not_x2 | apu-control |
| `bus:d7` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `bumo` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 16 | not_x2 | apu-control |
| `baxy` | 15 | not_x2 | apu-control |
| `bus:d5` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `bafo` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 16 | not_x2 | apu-control |
| `bono` | 15 | not_x2 | apu-control |
| `bus:d2` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `bogu` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 16 | not_x2 | apu-control |
| `bono` | 15 | not_x2 | apu-control |
| `bus:d1` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |

### `byga` (drlatch_ee) — diff=17, max=16
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 16 | not_x2 | apu-control |
| `bowe` | 15 | not_x2 | apu-control |
| `bus:d1` | 0 |  | bus |
| `kepy` | -1 | not_x3 | apu-control |


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


## Sprite Y Compare (20 races)

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

### `sobu` (dffr) — diff=15, max=14
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `teky` | 14 | and4 | ppu-ycomp |
| `tava` | -1 | not_x1 | ppu-ycomp |

### `wyso` (dlatch_ee) — diff=9, max=9
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 9 | not_x1 | ppu-ycomp |
| `ywok` | 8 | not_x1 | ppu-ycomp |
| `xafu` | 0 | dlatch | ppu-ycomp |

### `xote` (dlatch_ee) — diff=9, max=9
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 9 | not_x1 | ppu-ycomp |
| `ywok` | 8 | not_x1 | ppu-ycomp |
| `yses` | 0 | dlatch | ppu-ycomp |

### `xyju` (dlatch_ee) — diff=9, max=9
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 9 | not_x1 | ppu-ycomp |
| `ywok` | 8 | not_x1 | ppu-ycomp |
| `wone` | 0 | dlatch | ppu-ycomp |

### `xuso` (dlatch_ee) — diff=9, max=9
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 9 | not_x1 | ppu-ycomp |
| `ywok` | 8 | not_x1 | ppu-ycomp |
| `ydyv` | 0 | dlatch | ppu-ycomp |

### `xegu` (dlatch_ee) — diff=9, max=9
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 9 | not_x1 | ppu-ycomp |
| `ywok` | 8 | not_x1 | ppu-ycomp |
| `yceb` | 0 | dlatch | ppu-ycomp |

### `yzab` (dlatch_ee) — diff=9, max=9
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 9 | not_x1 | ppu-ycomp |
| `ywok` | 8 | not_x1 | ppu-ycomp |
| `zeca` | 0 | dlatch | ppu-ycomp |


## Clock Distribution (17 races)

### `ukup` (dffr) — diff=15, max=14
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 14 | nor3 | clocks |
| `boga` | -1 | not_x6 | clocks |

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


## Serial (15 races)

### `cuba` (dffsr) — diff=15, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cohy` | 14 | oa21 | serial |
| `cufu` | 14 | nand2 | serial |
| `cage` | 1 | not_x1 | serial |
| `dawe` | -1 | not_x2 | serial |

### `dovu` (dffsr) — diff=15, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyly` | 14 | oa21 | serial |
| `dola` | 14 | nand2 | serial |
| `dojo` | 0 | dffsr | serial |
| `epyt` | -1 | not_x2 | serial |

### `dojo` (dffsr) — diff=15, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `daju` | 14 | oa21 | serial |
| `dyge` | 14 | nand2 | serial |
| `dyra` | 0 | dffsr | serial |
| `dawe` | -1 | not_x2 | serial |

### `dyra` (dffsr) — diff=15, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dybo` | 14 | oa21 | serial |
| `dela` | 14 | nand2 | serial |
| `degu` | 0 | dffsr | serial |
| `dawe` | -1 | not_x2 | serial |

### `degu` (dffsr) — diff=15, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dumo` | 14 | oa21 | serial |
| `docu` | 14 | nand2 | serial |
| `cuba` | 0 | dffsr | serial |
| `dawe` | -1 | not_x2 | serial |

### `ejab` (dffsr) — diff=15, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehuj` | 14 | oa21 | serial |
| `elok` | 14 | nand2 | serial |
| `dovu` | 0 | dffsr | serial |
| `epyt` | -1 | not_x2 | serial |

### `erod` (dffsr) — diff=15, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efak` | 14 | oa21 | serial |
| `edel` | 14 | nand2 | serial |
| `ejab` | 0 | dffsr | serial |
| `epyt` | -1 | not_x2 | serial |

### `eder` (dffsr) — diff=15, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `eguv` | 14 | oa21 | serial |
| `efef` | 14 | nand2 | serial |
| `erod` | 0 | dffsr | serial |
| `epyt` | -1 | not_x2 | serial |

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

### `coty` (dffr) — diff=13, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 12 | nand4 | serial |
| `uvyn` | -1 | not_x1 | clocks |

### `culy` (dffr) — diff=13, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 12 | nand4 | serial |
| `bus:d0` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `cafa` (dffr) — diff=12, max=14
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 14 | and2 | serial |
| `dawa` | 2 | or2 | serial |

### `etaf` (dffr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 12 | nand4 | serial |
| `caby` | 3 | and2 | serial |
| `bus:d7` | 0 |  | bus |


## bootrom (1 races)

### `tepu` (dffr) — diff=13, max=12
Category: bootrom

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuge` | 12 | nand4 | bootrom |
| `sato` | 2 | or2 | bootrom |
| `alur` | -1 | not_x2 | clocks |


## BG/Win Cycles (14 races)

### `lovy` (dffr) — diff=13, max=12
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyry` | 12 | not_x1 | ppu-cycles |
| `nyxu` | 10 | nor3 | ppu-cycles |
| `myvo` | -1 | not_x1 | ppu-cycles |

### `nyka` (dffr) — diff=13, max=12
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyry` | 12 | not_x1 | ppu-cycles |
| `nafy` | 5 | nor2 | ppu-cycles |
| `alet` | -1 | not_x2 | ppu-control |

### `mesu` (dffr) — diff=10, max=10
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 10 | nor3 | ppu-cycles |
| `laxu` | 0 | dffr | ppu-cycles |

### `nyva` (dffr) — diff=10, max=10
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 10 | nor3 | ppu-cycles |
| `mesu` | 0 | dffr | ppu-cycles |

### `rubu` (dffr) — diff=10, max=10
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 10 | nor2 | ppu-cycles |
| `roga` | 0 | dffr | ppu-cycles |

### `roga` (dffr) — diff=10, max=10
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 10 | nor2 | ppu-cycles |
| `ryku` | 0 | dffr | ppu-cycles |

### `ryfa` (dffr) — diff=9, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pany` | 8 | nor2 | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |
| `segu` | -1 | not_x4 | ppu-cycles |

### `lony` (nand_latch) — diff=8, max=10
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 10 | nor3 | ppu-cycles |
| `lury` | 2 | and2 | ppu-cycles |

### `ryku` (dffr) — diff=8, max=10
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `paso` | 10 | nor2 | ppu-cycles |
| `pecu` | 2 | nand2 | ppu-cycles |

### `pyco` (dffr) — diff=8, max=7
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuko` | 7 | not_x1 | ppu-window |
| `roco` | -1 | not_x1 | ppu-cycles |
| `xapo` | -1 | not_x2 | ppu-control |

### `pynu` (nor_latch) — diff=6, max=6
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xofo` | 6 | nand3 | ppu-cycles |
| `nunu` | 0 | dffr | ppu-cycles |

### `pory` (dffr) — diff=6, max=5
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nafy` | 5 | nor2 | ppu-cycles |
| `nyka` | 0 | dffr | ppu-cycles |
| `myvo` | -1 | not_x1 | ppu-cycles |

### `puxa` (dffr) — diff=6, max=5
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pohu` | 5 | not_x1 | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |
| `roxo` | -1 | not_x1 | ppu-cycles |

### `sovy` (dffr) — diff=5, max=4
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rydy` | 4 | nor3 | ppu-cycles |
| `xapo` | -1 | not_x2 | ppu-control |
| `alet` | -1 | not_x2 | ppu-control |


## test (8 races)

### `amut` (dffr) — diff=13, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 12 | nand5 | test |
| `bus:d1` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `buro` (dffr) — diff=13, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 12 | nand5 | test |
| `bus:d0` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `jute` (dffr) — diff=13, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `bus:d0` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `jale` (dffr) — diff=13, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `bus:d2` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `kuko` (dffr) — diff=13, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `bus:d6` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `kyme` (dffr) — diff=13, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `bus:d3` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `keru` (dffr) — diff=13, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `bus:d7` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `kecy` (dffr) — diff=13, max=12
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `bus:d1` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |


## Joypad (6 races)

### `cofy` (dffr) — diff=13, max=12
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `bus:d5` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

### `kely` (dffr) — diff=13, max=12
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 12 | nand4 | joypad |
| `bus:d4` | 0 |  | bus |
| `alur` | -1 | not_x2 | clocks |

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


## BG Pixel Shifter (32 races)

### `macu` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lydu` | 12 | nand2 | ppu-bgfifo |
| `luja` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `moju` | 0 | dffsr | ppu-bgfifo |

### `modu` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lodo` | 12 | nand2 | ppu-bgfifo |
| `leru` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nepo` | 0 | dffsr | ppu-bgfifo |

### `moju` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lutu` | 12 | nand2 | ppu-bgfifo |
| `loto` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nozo` | 0 | dffsr | ppu-bgfifo |

### `nepo` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myvy` | 12 | nand2 | ppu-bgfifo |
| `mosy` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `macu` | 0 | dffsr | ppu-bgfifo |

### `neda` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyha` | 12 | nand2 | ppu-bgfifo |
| `nute` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `modu` | 0 | dffsr | ppu-bgfifo |

### `nozo` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nexa` | 12 | nand2 | ppu-bgfifo |
| `nyxo` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `myde` | 0 | dffsr | ppu-bgfifo |

### `pybo` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nady` | 12 | nand2 | ppu-bgfifo |
| `naja` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `neda` | 0 | dffsr | ppu-bgfifo |

### `ralu` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rajo` | 12 | nand2 | ppu-bgfifo |
| `supu` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `setu` | 0 | dffsr | ppu-bgfifo |

### `rysa` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryja` | 12 | nand2 | ppu-bgfifo |
| `sebo` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `sady` | 0 | dffsr | ppu-bgfifo |

### `setu` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `raja` | 12 | nand2 | ppu-bgfifo |
| `sywe` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `sobo` | 0 | dffsr | ppu-bgfifo |

### `sady` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruce` | 12 | nand2 | ppu-bgfifo |
| `sure` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `taca` | 0 | dffsr | ppu-bgfifo |

### `sohu` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryjy` | 12 | nand2 | ppu-bgfifo |
| `raga` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `ralu` | 0 | dffsr | ppu-bgfifo |

### `sobo` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruto` | 12 | nand2 | ppu-bgfifo |
| `suca` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `rysa` | 0 | dffsr | ppu-bgfifo |

### `taca` (dffsr) — diff=12, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `seno` | 12 | nand2 | ppu-bgfifo |
| `soly` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `tomy` | 0 | dffsr | ppu-bgfifo |

### `myde` (dffsr) — diff=10, max=12
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `laky` | 12 | nand2 | ppu-bgfifo |
| `loty` | 12 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |


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


## Sprite Pixel Shifter (16 races)

### `lefe` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lela` | 9 | nand2 | ppu-objfifo |
| `lyde` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `maso` | 0 | dffsr | ppu-objfifo |

### `lesu` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lufy` | 9 | nand2 | ppu-objfifo |
| `mame` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `lefe` | 0 | dffsr | ppu-objfifo |

### `maso` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myto` | 9 | nand2 | ppu-objfifo |
| `mada` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nuro` | 0 | dffsr | ppu-objfifo |

### `naty` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myxa` | 9 | nand2 | ppu-objfifo |
| `majo` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `pefu` | 0 | dffsr | ppu-objfifo |

### `pefu` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rusy` | 9 | nand2 | ppu-objfifo |
| `ruca` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nylu` | 0 | dffsr | ppu-objfifo |

### `pyjo` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rano` | 9 | nand2 | ppu-objfifo |
| `rehu` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `naty` | 0 | dffsr | ppu-objfifo |

### `vupy` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `teso` | 9 | nand2 | ppu-objfifo |
| `tula` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `vanu` | 0 | dffsr | ppu-objfifo |

### `vanu` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `taby` | 9 | nand2 | ppu-objfifo |
| `tapo` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `weba` | 0 | dffsr | ppu-objfifo |

### `vafo` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuxa` | 9 | nand2 | ppu-objfifo |
| `tupe` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `wora` | 0 | dffsr | ppu-objfifo |

### `vare` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyga` | 9 | nand2 | ppu-objfifo |
| `waxo` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `pyjo` | 0 | dffsr | ppu-objfifo |

### `wufy` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `vune` | 9 | nand2 | ppu-objfifo |
| `xyve` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `vafo` | 0 | dffsr | ppu-objfifo |

### `weba` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `vume` | 9 | nand2 | ppu-objfifo |
| `xole` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `vare` | 0 | dffsr | ppu-objfifo |

### `wora` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `vaby` | 9 | nand2 | ppu-objfifo |
| `xexu` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `wyho` | 0 | dffsr | ppu-objfifo |

### `wyho` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `vexu` | 9 | nand2 | ppu-objfifo |
| `xato` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `lesu` | 0 | dffsr | ppu-objfifo |

### `nylu` (dffsr) — diff=7, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mezu` | 9 | nand2 | ppu-objfifo |
| `mofy` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |


## VRAM Interface (9 races)

### `soto` (dffr) — diff=5, max=4
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sycy` | 4 | not_x1 | ppu-vram |
| `cunu` | -1 | not_x2 | ppu-control |

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
