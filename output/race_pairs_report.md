# Signal Race Pair Analysis

Total race pairs identified: 1063

Race pairs are registered nodes where data inputs arrive at significantly
different combinatorial depths. On real hardware, the late-arriving signal
may not settle before the register samples, causing behavior to differ from
behavioral emulation.

Delays computed using Elmore RC model with per-instance wire lengths from
dmg-sim. Depths are in effective gate-equivalents (1.0 ge = NOT_x1 at
median wire length). Effective timing domain is based on how often the
critical path's source register actually changes during rendering.

## Timing Domain Summary

| Domain | Races | Max Diff | Deadline | Description |
|--------|-------|----------|----------|-------------|
| **per-dot** | 13 | 22.2 ge | 238 ns | Source changes every pixel — tightest timing |
| **per-line** | 224 | 71.2 ge | 954 ns | Source changes once per scanline |
| **per-frame** | 473 | 113.5 ge | 3814 ns | Bus transfers, APU — plenty of slack |
| **static** | 353 | 98.8 ge | 15258 ns | Reset/LCDC paths — never races during rendering |

PPU-related races: 510


## BG Pixel Shifter (32 races) — per-dot

### `legu` (dlatch_ee_q) — diff=16.2 ge, max=16.2 ge | source: `nyva` (per-dot)
Category: ppu-bgfifo | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `luna` | 16.2 | not_x1 | ppu-bgfifo |
| `loma` | 11.8 | not_x1 | ppu-bgfifo |
| `bus:md0` | 0.0 |  | bus |

### `luzo` (dlatch_ee_q) — diff=16.2 ge, max=16.2 ge | source: `nyva` (per-dot)
Category: ppu-bgfifo | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `luna` | 16.2 | not_x1 | ppu-bgfifo |
| `loma` | 11.8 | not_x1 | ppu-bgfifo |
| `bus:md3` | 0.0 |  | bus |

### `megu` (dlatch_ee_q) — diff=16.2 ge, max=16.2 ge | source: `nyva` (per-dot)
Category: ppu-bgfifo | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `luna` | 16.2 | not_x1 | ppu-bgfifo |
| `loma` | 11.8 | not_x1 | ppu-bgfifo |
| `bus:md4` | 0.0 |  | bus |

### `muku` (dlatch_ee_q) — diff=16.2 ge, max=16.2 ge | source: `nyva` (per-dot)
Category: ppu-bgfifo | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `luna` | 16.2 | not_x1 | ppu-bgfifo |
| `loma` | 11.8 | not_x1 | ppu-bgfifo |
| `bus:md2` | 0.0 |  | bus |

### `myjy` (dlatch_ee_q) — diff=16.2 ge, max=16.2 ge | source: `nyva` (per-dot)
Category: ppu-bgfifo | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `luna` | 16.2 | not_x1 | ppu-bgfifo |
| `loma` | 11.8 | not_x1 | ppu-bgfifo |
| `bus:md5` | 0.0 |  | bus |

### `nasa` (dlatch_ee_q) — diff=16.2 ge, max=16.2 ge | source: `nyva` (per-dot)
Category: ppu-bgfifo | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `luna` | 16.2 | not_x1 | ppu-bgfifo |
| `loma` | 11.8 | not_x1 | ppu-bgfifo |
| `bus:md6` | 0.0 |  | bus |

### `nefo` (dlatch_ee_q) — diff=16.2 ge, max=16.2 ge | source: `nyva` (per-dot)
Category: ppu-bgfifo | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `luna` | 16.2 | not_x1 | ppu-bgfifo |
| `loma` | 11.8 | not_x1 | ppu-bgfifo |
| `bus:md7` | 0.0 |  | bus |

### `nudu` (dlatch_ee_q) — diff=16.2 ge, max=16.2 ge | source: `nyva` (per-dot)
Category: ppu-bgfifo | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `luna` | 16.2 | not_x1 | ppu-bgfifo |
| `loma` | 11.8 | not_x1 | ppu-bgfifo |
| `bus:md1` | 0.0 |  | bus |

### `poju` (dffr_cc_q) — diff=13.9 ge, max=13.9 ge | source: `xymu` (per-line)
Category: ppu-bgfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `labu` | 13.9 | not_x2 | ppu-bgfifo |
| `luve` | 11.4 | not_x2 | ppu-bgfifo |
| `bus:md5` | 0.0 |  | bus |

### `powy` (dffr_cc_q) — diff=13.9 ge, max=13.9 ge | source: `xymu` (per-line)
Category: ppu-bgfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `labu` | 13.9 | not_x2 | ppu-bgfifo |
| `luve` | 11.4 | not_x2 | ppu-bgfifo |
| `bus:md6` | 0.0 |  | bus |

### `poxa` (dffr_cc_q) — diff=13.9 ge, max=13.9 ge | source: `xymu` (per-line)
Category: ppu-bgfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `labu` | 13.9 | not_x2 | ppu-bgfifo |
| `luve` | 11.4 | not_x2 | ppu-bgfifo |
| `bus:md3` | 0.0 |  | bus |

### `pozo` (dffr_cc_q) — diff=13.9 ge, max=13.9 ge | source: `xymu` (per-line)
Category: ppu-bgfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `labu` | 13.9 | not_x2 | ppu-bgfifo |
| `luve` | 11.4 | not_x2 | ppu-bgfifo |
| `bus:md1` | 0.0 |  | bus |

### `pulo` (dffr_cc_q) — diff=13.9 ge, max=13.9 ge | source: `xymu` (per-line)
Category: ppu-bgfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `labu` | 13.9 | not_x2 | ppu-bgfifo |
| `luve` | 11.4 | not_x2 | ppu-bgfifo |
| `bus:md4` | 0.0 |  | bus |

### `pyju` (dffr_cc_q) — diff=13.9 ge, max=13.9 ge | source: `xymu` (per-line)
Category: ppu-bgfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `labu` | 13.9 | not_x2 | ppu-bgfifo |
| `luve` | 11.4 | not_x2 | ppu-bgfifo |
| `bus:md7` | 0.0 |  | bus |

### `pyzo` (dffr_cc_q) — diff=13.9 ge, max=13.9 ge | source: `xymu` (per-line)
Category: ppu-bgfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `labu` | 13.9 | not_x2 | ppu-bgfifo |
| `luve` | 11.4 | not_x2 | ppu-bgfifo |
| `bus:md2` | 0.0 |  | bus |


## BG/Win Cycles (20 races) — per-dot

### `pory` (dffr) — diff=22.2 ge, max=22.2 ge | source: `ck1_ck2` (per-dot)
Category: ppu-cycles | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `myvo` | 22.2 | not_x1 | ppu-cycles |
| `nafy` | 6.2 | nor2 | ppu-cycles |
| `nyka` | 0.0 | dffr | ppu-cycles |

### `nyze` (dffr) — diff=16.7 ge, max=16.7 ge | source: `ck1_ck2` (per-dot)
Category: ppu-cycles | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `moxe` | 16.7 | not_x1 | ppu-cycles |
| `puxa` | 0.0 | dffr | ppu-cycles |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `lyzu` (dffr) — diff=16.3 ge, max=16.3 ge | source: `ck1_ck2` (per-dot)
Category: ppu-cycles | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `alet` | 16.3 | not_x2 | ppu-control |
| `laxu` | 0.0 | dffr | ppu-cycles |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `pygo` (dffr) — diff=16.3 ge, max=16.3 ge | source: `ck1_ck2` (per-dot)
Category: ppu-cycles | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `alet` | 16.3 | not_x2 | ppu-control |
| `pory` | 0.0 | dffr | ppu-cycles |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `rene` (dffr) — diff=16.3 ge, max=16.3 ge | source: `ck1_ck2` (per-dot)
Category: ppu-cycles | Effective: per-dot

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `alet` | 16.3 | not_x2 | ppu-control |
| `ryfa` | 0.0 | dffr | ppu-cycles |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `paho` (dffr) — diff=52.1 ge, max=52.1 ge | source: `ceno` (per-line)
Category: ppu-cycles | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `roxo` | 52.1 | not_x1 | ppu-cycles |
| `xydo` | 0.0 | dffr | ppu-stat |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `puxa` (dffr) — diff=52.1 ge, max=52.1 ge | source: `ceno` (per-line)
Category: ppu-cycles | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `roxo` | 52.1 | not_x1 | ppu-cycles |
| `pohu` | 3.5 | not_x1 | ppu-cycles |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `ryfa` (dffr) — diff=49.4 ge, max=49.4 ge | source: `ceno` (per-line)
Category: ppu-cycles | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `segu` | 49.4 | not_x4 | ppu-cycles |
| `pany` | 9.4 | nor2 | ppu-cycles |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `pyco` (dffr) — diff=44.4 ge, max=50.0 ge | source: `ceno` (per-line)
Category: ppu-cycles | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `roco` | 50.0 | not_x1 | ppu-cycles |
| `xapo` | 29.4 | not_x2 | ppu-control |
| `nuko` | 5.6 | not_x1 | ppu-window |

### `nyka` (dffr) — diff=92.9 ge, max=99.1 ge | source: `afer` (static)
Category: ppu-cycles | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyry` | 99.1 | not_x1 | ppu-cycles |
| `alet` | 16.3 | not_x2 | ppu-control |
| `nafy` | 6.2 | nor2 | ppu-cycles |

### `mesu` (dffr) — diff=92.9 ge, max=92.9 ge | source: `afer` (static)
Category: ppu-cycles | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nyxu` | 92.9 | nor3 | ppu-cycles |
| `laxu` | 0.0 | dffr | ppu-cycles |

### `nyva` (dffr) — diff=92.9 ge, max=92.9 ge | source: `afer` (static)
Category: ppu-cycles | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nyxu` | 92.9 | nor3 | ppu-cycles |
| `mesu` | 0.0 | dffr | ppu-cycles |

### `lony` (nand_latch) — diff=91.7 ge, max=92.9 ge | source: `afer` (static)
Category: ppu-cycles | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nyxu` | 92.9 | nor3 | ppu-cycles |
| `lury` | 1.2 | and2 | ppu-cycles |

### `lovy` (dffr) — diff=76.9 ge, max=99.1 ge | source: `afer` (static)
Category: ppu-cycles | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyry` | 99.1 | not_x1 | ppu-cycles |
| `nyxu` | 92.9 | nor3 | ppu-cycles |
| `myvo` | 22.2 | not_x1 | ppu-cycles |

### `pynu` (nor_latch) — diff=53.3 ge, max=53.3 ge | source: `afer` (static)
Category: ppu-cycles | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xofo` | 53.3 | nand3 | ppu-cycles |
| `nunu` | 0.0 | dffr | ppu-cycles |


## Bus (79 races) — per-line

### `bus:oam_render_a2` () — diff=49.1 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `zaro` | 84.9 | not_if0 | ppu-objreg |
| `apoc` | 75.2 | not_if0 | ppu-objreg |
| `wako` | 75.2 | not_if0 | ppu-objreg |
| `wato` | 72.6 | not_if0 | ppu-objreg |
| `wuxu` | 72.0 | not_if0 | ppu-objreg |
| `dobo` | 70.0 | not_if0 | ppu-objreg |
| `enap` | 67.2 | not_if0 | ppu-objreg |
| `zedy` | 65.9 | not_if0 | ppu-objreg |
| `cube` | 65.4 | not_if0 | ppu-objreg |
| `cubo` | 61.0 | not_if0 | ppu-objreg |
| `wuzy` | 35.8 | not_if0 | ppu-oam |

### `bus:oam_render_a3` () — diff=49.1 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `zojy` | 84.9 | not_if0 | ppu-objreg |
| `akyh` | 75.2 | not_if0 | ppu-objreg |
| `wygo` | 75.2 | not_if0 | ppu-objreg |
| `wywy` | 72.6 | not_if0 | ppu-objreg |
| `wepy` | 72.0 | not_if0 | ppu-objreg |
| `dyny` | 70.0 | not_if0 | ppu-objreg |
| `dygo` | 67.2 | not_if0 | ppu-objreg |
| `zumu` | 65.9 | not_if0 | ppu-objreg |
| `afoz` | 65.4 | not_if0 | ppu-objreg |
| `celu` | 61.0 | not_if0 | ppu-objreg |
| `wyse` | 35.8 | not_if0 | ppu-oam |

### `bus:oam_render_a4` () — diff=49.1 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ynev` | 84.9 | not_if0 | ppu-objreg |
| `afen` | 75.2 | not_if0 | ppu-objreg |
| `elep` | 75.2 | not_if0 | ppu-objreg |
| `ezoc` | 72.6 | not_if0 | ppu-objreg |
| `weru` | 72.0 | not_if0 | ppu-objreg |
| `waga` | 70.0 | not_if0 | ppu-objreg |
| `dowa` | 67.2 | not_if0 | ppu-objreg |
| `woko` | 65.9 | not_if0 | ppu-objreg |
| `apon` | 65.4 | not_if0 | ppu-objreg |
| `cegy` | 61.0 | not_if0 | ppu-objreg |
| `zysu` | 35.8 | not_if0 | ppu-oam |

### `bus:oam_render_a5` () — diff=49.1 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xyra` | 84.9 | not_if0 | ppu-objreg |
| `apyv` | 75.2 | not_if0 | ppu-objreg |
| `etad` | 75.2 | not_if0 | ppu-objreg |
| `wabo` | 72.6 | not_if0 | ppu-objreg |
| `xyre` | 72.0 | not_if0 | ppu-objreg |
| `duza` | 70.0 | not_if0 | ppu-objreg |
| `dony` | 67.2 | not_if0 | ppu-objreg |
| `zave` | 65.9 | not_if0 | ppu-objreg |
| `cuvu` | 65.4 | not_if0 | ppu-objreg |
| `bety` | 61.0 | not_if0 | ppu-objreg |
| `wyda` | 35.8 | not_if0 | ppu-oam |

### `bus:oam_render_a6` () — diff=49.1 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `yrad` | 84.9 | not_if0 | ppu-objreg |
| `apob` | 75.2 | not_if0 | ppu-objreg |
| `waba` | 75.2 | not_if0 | ppu-objreg |
| `elyc` | 72.6 | not_if0 | ppu-objreg |
| `woxy` | 72.0 | not_if0 | ppu-objreg |
| `daly` | 70.0 | not_if0 | ppu-objreg |
| `efud` | 67.2 | not_if0 | ppu-objreg |
| `zece` | 65.9 | not_if0 | ppu-objreg |
| `cyro` | 65.4 | not_if0 | ppu-objreg |
| `cyby` | 61.0 | not_if0 | ppu-objreg |
| `wuco` | 35.8 | not_if0 | ppu-oam |

### `bus:oam_render_a7` () — diff=49.1 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `yhal` | 84.9 | not_if0 | ppu-objreg |
| `adyb` | 75.2 | not_if0 | ppu-objreg |
| `evyt` | 75.2 | not_if0 | ppu-objreg |
| `wocy` | 72.6 | not_if0 | ppu-objreg |
| `waja` | 72.0 | not_if0 | ppu-objreg |
| `dalo` | 70.0 | not_if0 | ppu-objreg |
| `dezu` | 67.2 | not_if0 | ppu-objreg |
| `zetu` | 65.9 | not_if0 | ppu-objreg |
| `axec` | 65.4 | not_if0 | ppu-objreg |
| `bemo` | 61.0 | not_if0 | ppu-objreg |
| `weza` | 35.8 | not_if0 | ppu-oam |

### `bus:sprite_y_store0` () — diff=23.9 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byme` | 84.9 | not_if0 | ppu-objreg |
| `boso` | 75.2 | not_if0 | ppu-objreg |
| `waxe` | 75.2 | not_if0 | ppu-objreg |
| `ybuk` | 72.6 | not_if0 | ppu-objreg |
| `buce` | 72.0 | not_if0 | ppu-objreg |
| `bace` | 70.0 | not_if0 | ppu-objreg |
| `cucu` | 69.3 | not_if0 | ppu-ycomp |
| `zexe` | 67.2 | not_if0 | ppu-objreg |
| `gofo` | 65.9 | not_if0 | ppu-objreg |
| `zuke` | 65.4 | not_if0 | ppu-objreg |
| `byro` | 61.0 | not_if0 | ppu-objreg |

### `bus:sprite_y_store1` () — diff=23.9 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `gate` | 84.9 | not_if0 | ppu-objreg |
| `bazu` | 75.2 | not_if0 | ppu-objreg |
| `ypoz` | 75.2 | not_if0 | ppu-objreg |
| `ykoz` | 72.6 | not_if0 | ppu-objreg |
| `bevy` | 72.0 | not_if0 | ppu-objreg |
| `buja` | 70.0 | not_if0 | ppu-objreg |
| `cuca` | 69.3 | not_if0 | ppu-ycomp |
| `ywav` | 67.2 | not_if0 | ppu-objreg |
| `buky` | 65.9 | not_if0 | ppu-objreg |
| `were` | 65.4 | not_if0 | ppu-objreg |
| `ahum` | 61.0 | not_if0 | ppu-objreg |

### `bus:sprite_y_store2` () — diff=23.9 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `coho` | 84.9 | not_if0 | ppu-objreg |
| `ahac` | 75.2 | not_if0 | ppu-objreg |
| `wabu` | 75.2 | not_if0 | ppu-objreg |
| `zyto` | 72.6 | not_if0 | ppu-objreg |
| `bove` | 72.0 | not_if0 | ppu-objreg |
| `bodu` | 70.0 | not_if0 | ppu-objreg |
| `cega` | 69.3 | not_if0 | ppu-ycomp |
| `yjem` | 67.2 | not_if0 | ppu-objreg |
| `ajal` | 65.9 | not_if0 | ppu-objreg |
| `wuxe` | 65.4 | not_if0 | ppu-objreg |
| `baco` | 61.0 | not_if0 | ppu-objreg |

### `bus:sprite_y_store3` () — diff=23.9 ge, max=84.9 ge | source: `ceno` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `cawo` | 84.9 | not_if0 | ppu-objreg |
| `bujy` | 75.2 | not_if0 | ppu-objreg |
| `wana` | 75.2 | not_if0 | ppu-objreg |
| `zudo` | 72.6 | not_if0 | ppu-objreg |
| `bydo` | 72.0 | not_if0 | ppu-objreg |
| `awat` | 70.0 | not_if0 | ppu-objreg |
| `wenu` | 69.3 | not_if0 | ppu-ycomp |
| `zypo` | 67.2 | not_if0 | ppu-objreg |
| `wehe` | 65.9 | not_if0 | ppu-objreg |
| `zaby` | 65.4 | not_if0 | ppu-objreg |
| `befe` | 61.0 | not_if0 | ppu-objreg |

### `bus:~ma4` () — diff=18.5 ge, max=66.2 ge | source: `daty` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ajan` | 66.2 | not_if0 | ppu-bgscroll |
| `xeca` | 54.8 | not_if0 | ppu-vram |
| `damu` | 52.6 | not_if0 | ppu-dma |
| `famu` | 51.5 | not_if0 | ppu-ycomp |
| `wuju` | 50.5 | not_if0 | ppu-window |
| `vapy` | 47.8 | not_if1 | ppu-bgfifo |

### `bus:oam_~{a5}_tri` () — diff=16.7 ge, max=35.5 ge | source: `matu` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `gera` | 35.5 | not_if0 | ppu-oam |
| `faku` | 35.0 | not_if0 | ppu-oam |
| `faco` | 31.7 | not_if0 | ppu-oam |
| `edol` | 18.8 | not_if0 | ppu-oam |

### `bus:oam_~{a4}_tri` () — diff=16.7 ge, max=32.8 ge | source: `matu` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `fevu` | 32.8 | not_if0 | ppu-oam |
| `futo` | 32.3 | not_if0 | ppu-oam |
| `faby` | 28.9 | not_if0 | ppu-oam |
| `elug` | 16.1 | not_if0 | ppu-oam |

### `bus:oam_~{a7}_tri` () — diff=16.7 ge, max=32.3 ge | source: `matu` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `foby` | 32.3 | not_if0 | ppu-oam |
| `goby` | 31.8 | not_if0 | ppu-oam |
| `fyke` | 28.5 | not_if0 | ppu-oam |
| `fetu` | 15.6 | not_if0 | ppu-oam |

### `bus:oam_~{a6}_tri` () — diff=16.7 ge, max=31.3 ge | source: `matu` (per-line)
Category: bus | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `waxa` | 31.3 | not_if0 | ppu-oam |
| `gama` | 30.8 | not_if0 | ppu-oam |
| `fugu` | 27.5 | not_if0 | ppu-oam |
| `fydu` | 14.6 | not_if0 | ppu-oam |


## Sprite Control (17 races) — per-line

### `dezy` (dffr) — diff=45.5 ge, max=54.4 ge | source: `muwy` (per-line)
Category: ppu-objctl | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `dyty` | 54.4 | not_x2 | ppu-objctl |
| `xapo` | 29.4 | not_x2 | ppu-control |
| `zeme` | 8.9 | not_x4 | ppu-control |

### `besu` (nor_latch) — diff=81.5 ge, max=81.5 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `asen` | 81.5 | or2 | ppu-objctl |
| `catu` | 0.0 | dffr | ppu-objctl |

### `doba` (dffr) — diff=69.9 ge, max=69.9 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bagy` | 69.9 | not_x1 | ppu-objctl |
| `alet` | 16.3 | not_x2 | ppu-control |
| `byba` | 0.0 | dffr | ppu-objctl |

### `elyn` (dffr) — diff=67.3 ge, max=67.3 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `anom` | 67.3 | nor2 | ppu-objctl |
| `goso` | 0.0 | dffr | ppu-objctl |

### `faha` (dffr) — diff=67.3 ge, max=67.3 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `anom` | 67.3 | nor2 | ppu-objctl |
| `elyn` | 0.0 | dffr | ppu-objctl |

### `fony` (dffr) — diff=67.3 ge, max=67.3 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `anom` | 67.3 | nor2 | ppu-objctl |
| `faha` | 0.0 | dffr | ppu-objctl |

### `goso` (dffr) — diff=67.3 ge, max=67.3 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `anom` | 67.3 | nor2 | ppu-objctl |
| `wewy` | 0.0 | dffr | ppu-objctl |

### `wewy` (dffr) — diff=67.3 ge, max=67.3 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `anom` | 67.3 | nor2 | ppu-objctl |
| `yfel` | 0.0 | dffr | ppu-objctl |

### `byba` (dffr) — diff=64.6 ge, max=69.9 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bagy` | 69.9 | not_x1 | ppu-objctl |
| `feto` | 6.0 | and4 | ppu-objctl |
| `xupy` | 5.3 | not_x2 | ppu-oam |

### `yfel` (dffr) — diff=59.4 ge, max=67.3 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `anom` | 67.3 | nor2 | ppu-objctl |
| `gava` | 7.9 | or2 | ppu-objctl |

### `bego` (dffr) — diff=49.9 ge, max=49.9 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `azyb` | 49.9 | not_x1 | ppu-objctl |
| `cuxy` | 0.0 | dffr | ppu-objctl |

### `cuxy` (dffr) — diff=49.9 ge, max=49.9 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `azyb` | 49.9 | not_x1 | ppu-objctl |
| `bese` | 0.0 | dffr | ppu-objctl |

### `dybe` (dffr) — diff=49.9 ge, max=49.9 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `azyb` | 49.9 | not_x1 | ppu-objctl |
| `bego` | 0.0 | dffr | ppu-objctl |

### `bese` (dffr) — diff=47.6 ge, max=49.9 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `azyb` | 49.9 | not_x1 | ppu-objctl |
| `cake` | 2.3 | or2 | ppu-objctl |

### `anel` (dffr) — diff=36.1 ge, max=36.1 ge | source: `afer` (static)
Category: ppu-objctl | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `abez` | 36.1 | not_x1 | ppu-objctl |
| `awoh` | 5.8 | not_x1 | ppu-objctl |
| `catu` | 0.0 | dffr | ppu-objctl |


## Sprite X Match (112 races) — per-line

### `lyme` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `lamy` | 32.6 | nand2 | ppu-xcomp |
| `lunu` | 32.4 | nand2 | ppu-xcomp |
| `moda` | 0.0 | dffsr | ppu-xcomp |

### `moda` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `luke` | 28.8 | nand2 | ppu-xcomp |
| `lowa` | 28.7 | nand2 | ppu-xcomp |
| `nuke` | 0.0 | dffsr | ppu-xcomp |

### `nuke` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `mene` | 32.0 | nand2 | ppu-xcomp |
| `pazo` | 31.6 | nand2 | ppu-xcomp |
| `palu` | 0.0 | dffsr | ppu-xcomp |

### `palu` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `rudu` | 30.8 | nand2 | ppu-xcomp |
| `rora` | 30.4 | nand2 | ppu-xcomp |
| `somy` | 0.0 | dffsr | ppu-xcomp |

### `rosa` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `pamo` | 32.8 | nand2 | ppu-xcomp |
| `pyzy` | 31.6 | nand2 | ppu-xcomp |
| `sata` | 0.0 | dffsr | ppu-xcomp |

### `sata` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `tafa` | 32.6 | nand2 | ppu-xcomp |
| `soro` | 32.6 | nand2 | ppu-xcomp |
| `rugo` | 0.0 | dffsr | ppu-xcomp |

### `somy` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `suky` | 32.2 | nand2 | ppu-xcomp |
| `towa` | 32.0 | nand2 | ppu-xcomp |
| `rosa` | 0.0 | dffsr | ppu-xcomp |

### `vava` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `tuwu` | 34.0 | nand2 | ppu-xcomp |
| `wubu` | 32.8 | nand2 | ppu-xcomp |
| `vumo` | 0.0 | dffsr | ppu-xcomp |

### `vosa` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `tyra` | 31.9 | nand2 | ppu-xcomp |
| `tufo` | 31.9 | nand2 | ppu-xcomp |
| `wuru` | 0.0 | dffsr | ppu-xcomp |

### `vumo` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `tena` | 30.1 | nand2 | ppu-xcomp |
| `tyko` | 30.0 | nand2 | ppu-xcomp |
| `woda` | 0.0 | dffsr | ppu-xcomp |

### `woda` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `xely` | 32.6 | nand2 | ppu-xcomp |
| `wuja` | 32.2 | nand2 | ppu-xcomp |
| `xete` | 0.0 | dffsr | ppu-xcomp |

### `wuru` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `xala` | 34.5 | nand2 | ppu-xcomp |
| `wede` | 32.6 | nand2 | ppu-xcomp |
| `vezo` | 0.0 | dffsr | ppu-xcomp |

### `wyfu` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `xyru` | 32.8 | nand2 | ppu-xcomp |
| `wevo` | 32.8 | nand2 | ppu-xcomp |
| `vosa` | 0.0 | dffsr | ppu-xcomp |

### `xete` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `xuku` | 30.9 | nand2 | ppu-xcomp |
| `wedy` | 30.5 | nand2 | ppu-xcomp |
| `wyfu` | 0.0 | dffsr | ppu-xcomp |

### `cuvy` (drlatch_ee) — diff=58.5 ge, max=72.6 ge | source: `muwy` (per-line)
Category: ppu-xcomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `exyr` | 72.6 | not_x1 | ppu-objctl |
| `ejad` | 71.8 | not_x1 | ppu-xprio |
| `cyla` | 66.5 | not_x1 | ppu-objctl |
| `bady` | 14.1 | not_x1 | ppu-xcomp |


## Sprite Y Compare (26 races) — per-line

### `tobu` (dffr) — diff=27.3 ge, max=27.3 ge | source: `ck1_ck2` (per-dot)
Category: ppu-ycomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tava` | 27.3 | not_x1 | ppu-ycomp |
| `tuly` | 0.0 | dffr | ppu-ycomp |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `vonu` (dffr) — diff=27.3 ge, max=27.3 ge | source: `ck1_ck2` (per-dot)
Category: ppu-ycomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tava` | 27.3 | not_x1 | ppu-ycomp |
| `tobu` | 0.0 | dffr | ppu-ycomp |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `seba` (dffr) — diff=25.8 ge, max=25.8 ge | source: `ck1_ck2` (per-dot)
Category: ppu-ycomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lape` | 25.8 | not_x1 | ppu-ycomp |
| `vonu` | 0.0 | dffr | ppu-ycomp |
| `xymu` | 0.0 | nor_latch | ppu-stat |

### `suda` (dffr) — diff=25.8 ge, max=25.8 ge | source: `ck1_ck2` (per-dot)
Category: ppu-ycomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lape` | 25.8 | not_x1 | ppu-ycomp |
| `sobu` | 0.0 | dffr | ppu-ycomp |

### `tyfo` (dffr) — diff=25.8 ge, max=25.8 ge | source: `ck1_ck2` (per-dot)
Category: ppu-ycomp | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lape` | 25.8 | not_x1 | ppu-ycomp |
| `toxe` | 0.0 | dffr | ppu-ycomp |

### `wone` (dlatch) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bode` | 73.2 | not_x1 | ppu-oam |
| `bus:~oam_b_d3` | 0.0 |  | bus |

### `xafu` (dlatch) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bode` | 73.2 | not_x1 | ppu-oam |
| `bus:~oam_b_d5` | 0.0 |  | bus |

### `yceb` (dlatch) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bode` | 73.2 | not_x1 | ppu-oam |
| `bus:~oam_b_d1` | 0.0 |  | bus |

### `ydyv` (dlatch) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bode` | 73.2 | not_x1 | ppu-oam |
| `bus:~oam_b_d0` | 0.0 |  | bus |

### `yses` (dlatch) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bode` | 73.2 | not_x1 | ppu-oam |
| `bus:~oam_b_d6` | 0.0 |  | bus |

### `zaxe` (dlatch) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bode` | 73.2 | not_x1 | ppu-oam |
| `bus:~oam_b_d4` | 0.0 |  | bus |

### `zeca` (dlatch) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bode` | 73.2 | not_x1 | ppu-oam |
| `bus:~oam_b_d7` | 0.0 |  | bus |

### `zuca` (dlatch) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bode` | 73.2 | not_x1 | ppu-oam |
| `bus:~oam_b_d2` | 0.0 |  | bus |

### `wyso` (dlatch_ee) — diff=70.2 ge, max=70.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ysum` | 70.2 | not_x1 | ppu-ycomp |
| `ywok` | 66.8 | not_x1 | ppu-ycomp |
| `xafu` | 0.0 | dlatch | ppu-ycomp |

### `xegu` (dlatch_ee) — diff=70.2 ge, max=70.2 ge | source: `bus:a10` (per-frame)
Category: ppu-ycomp | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ysum` | 70.2 | not_x1 | ppu-ycomp |
| `ywok` | 66.8 | not_x1 | ppu-ycomp |
| `yceb` | 0.0 | dlatch | ppu-ycomp |


## Sprite Store (100 races) — per-line

### `dafu` (dlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ebeb` | 71.2 | not_x1 | ppu-objctl |
| `feka` | 68.4 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0.0 |  | bus |

### `deba` (dlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ebeb` | 71.2 | not_x1 | ppu-objctl |
| `feka` | 68.4 | not_x1 | ppu-objctl |
| `bus:oam_render_a6` | 0.0 |  | bus |

### `dese` (dlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ebeb` | 71.2 | not_x1 | ppu-objctl |
| `feka` | 68.4 | not_x1 | ppu-objctl |
| `bus:oam_render_a3` | 0.0 |  | bus |

### `devy` (dlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ebeb` | 71.2 | not_x1 | ppu-objctl |
| `feka` | 68.4 | not_x1 | ppu-objctl |
| `bus:oam_render_a2` | 0.0 |  | bus |

### `duha` (dlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ebeb` | 71.2 | not_x1 | ppu-objctl |
| `feka` | 68.4 | not_x1 | ppu-objctl |
| `bus:oam_render_a5` | 0.0 |  | bus |

### `duny` (dlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ebeb` | 71.2 | not_x1 | ppu-objctl |
| `feka` | 68.4 | not_x1 | ppu-objctl |
| `bus:oam_render_a4` | 0.0 |  | bus |

### `wanu` (dlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wude` | 70.6 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a4` | 0.0 |  | bus |

### `xabo` (dlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wude` | 70.6 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a5` | 0.0 |  | bus |

### `xave` (dlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wude` | 70.6 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a2` | 0.0 |  | bus |

### `xefe` (dlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wude` | 70.6 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a3` | 0.0 |  | bus |

### `xege` (dlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wude` | 70.6 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a6` | 0.0 |  | bus |

### `xynu` (dlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wude` | 70.6 | not_x1 | ppu-objctl |
| `wylu` | 67.9 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0.0 |  | bus |

### `caju` (dlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `baba` | 70.5 | not_x1 | ppu-objctl |
| `ewot` | 68.2 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0.0 |  | bus |

### `capo` (dlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `baba` | 70.5 | not_x1 | ppu-objctl |
| `ewot` | 68.2 | not_x1 | ppu-objctl |
| `bus:sprite_y_store0` | 0.0 |  | bus |

### `cono` (dlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `muwy` (per-line)
Category: ppu-objreg | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `baba` | 70.5 | not_x1 | ppu-objctl |
| `ewot` | 68.2 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0.0 |  | bus |


## Interrupts (10 races) — per-line

### `lalu` (dffsr) — diff=5.8 ge, max=64.8 ge | source: `ceno` (per-line)
Category: int | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voty` | 64.8 | not_x3 | ppu-stat |
| `mody` | 64.5 | nand3 | int |
| `movu` | 59.0 | and3 | int |

### `ubul` (dffsr) — diff=65.0 ge, max=65.0 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tome` | 65.0 | nand3 | int |
| `tuny` | 58.5 | and3 | int |
| `caly` | 0.0 | dffr | serial |

### `nybo` (dffsr) — diff=64.5 ge, max=64.5 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pyhu` | 64.5 | nand3 | int |
| `pyga` | 58.8 | and3 | int |
| `moba` | 0.0 | dffr | timer |

### `ulak` (dffsr) — diff=53.4 ge, max=64.5 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `toga` | 64.5 | nand3 | int |
| `tyme` | 59.5 | and3 | int |
| `asok` | 11.1 | and2 | joypad |

### `maty` (dlatch) — diff=51.4 ge, max=51.4 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rolo` | 51.4 | nand4 | int |
| `lope` | 0.0 | dffsr | int |

### `mopo` (dlatch) — diff=51.4 ge, max=51.4 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rolo` | 51.4 | nand4 | int |
| `lalu` | 0.0 | dffsr | int |

### `nejy` (dlatch) — diff=51.4 ge, max=51.4 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rolo` | 51.4 | nand4 | int |
| `ubul` | 0.0 | dffsr | int |

### `nuty` (dlatch) — diff=51.4 ge, max=51.4 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rolo` | 51.4 | nand4 | int |
| `ulak` | 0.0 | dffsr | int |

### `pavy` (dlatch) — diff=51.4 ge, max=51.4 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rolo` | 51.4 | nand4 | int |
| `nybo` | 0.0 | dffsr | int |

### `lope` (dffsr) — diff=46.1 ge, max=64.4 ge | source: `bus:a10` (per-frame)
Category: int | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `myzu` | 64.4 | nand3 | int |
| `lyta` | 59.1 | and3 | int |
| `vypu` | 18.2 | not_x3 | ppu-stat |


## Sprite Pixel Shifter (32 races) — per-line

### `lefe` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `lela` | 32.3 | nand2 | ppu-objfifo |
| `lyde` | 31.8 | nand2 | ppu-objfifo |
| `maso` | 0.0 | dffsr | ppu-objfifo |

### `lesu` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `mame` | 32.9 | nand2 | ppu-objfifo |
| `lufy` | 32.1 | nand2 | ppu-objfifo |
| `lefe` | 0.0 | dffsr | ppu-objfifo |

### `maso` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `myto` | 32.9 | nand2 | ppu-objfifo |
| `mada` | 32.5 | nand2 | ppu-objfifo |
| `nuro` | 0.0 | dffsr | ppu-objfifo |

### `naty` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `myxa` | 31.8 | nand2 | ppu-objfifo |
| `majo` | 31.6 | nand2 | ppu-objfifo |
| `pefu` | 0.0 | dffsr | ppu-objfifo |

### `pefu` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `rusy` | 32.8 | nand2 | ppu-objfifo |
| `ruca` | 32.3 | nand2 | ppu-objfifo |
| `nylu` | 0.0 | dffsr | ppu-objfifo |

### `pyjo` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `rano` | 32.5 | nand2 | ppu-objfifo |
| `rehu` | 32.0 | nand2 | ppu-objfifo |
| `naty` | 0.0 | dffsr | ppu-objfifo |

### `vafo` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `tuxa` | 29.0 | nand2 | ppu-objfifo |
| `tupe` | 28.9 | nand2 | ppu-objfifo |
| `wora` | 0.0 | dffsr | ppu-objfifo |

### `vanu` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `tapo` | 29.1 | nand2 | ppu-objfifo |
| `taby` | 28.6 | nand2 | ppu-objfifo |
| `weba` | 0.0 | dffsr | ppu-objfifo |

### `vare` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `tyga` | 30.4 | nand2 | ppu-objfifo |
| `waxo` | 30.3 | nand2 | ppu-objfifo |
| `pyjo` | 0.0 | dffsr | ppu-objfifo |

### `vupy` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `teso` | 32.8 | nand2 | ppu-objfifo |
| `tula` | 32.4 | nand2 | ppu-objfifo |
| `vanu` | 0.0 | dffsr | ppu-objfifo |

### `weba` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `vume` | 32.7 | nand2 | ppu-objfifo |
| `xole` | 32.3 | nand2 | ppu-objfifo |
| `vare` | 0.0 | dffsr | ppu-objfifo |

### `wora` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `vaby` | 32.7 | nand2 | ppu-objfifo |
| `xexu` | 32.0 | nand2 | ppu-objfifo |
| `wyho` | 0.0 | dffsr | ppu-objfifo |

### `wufy` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `xyve` | 32.6 | nand2 | ppu-objfifo |
| `vune` | 32.4 | nand2 | ppu-objfifo |
| `vafo` | 0.0 | dffsr | ppu-objfifo |

### `wyho` (dffsr) — diff=63.8 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `vexu` | 31.0 | nand2 | ppu-objfifo |
| `xato` | 30.5 | nand2 | ppu-objfifo |
| `lesu` | 0.0 | dffsr | ppu-objfifo |

### `nuro` (dffsr) — diff=30.9 ge, max=63.8 ge | source: `ceno` (per-line)
Category: ppu-objfifo | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `sacu` | 63.8 | or2 | ppu-cycles |
| `pabe` | 33.2 | nand2 | ppu-objfifo |
| `pyzu` | 32.9 | nand2 | ppu-objfifo |


## Address Bus (26 races) — per-line

### `a2` (pad_bidir) — diff=12.0 ge, max=54.3 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bajo` | 54.3 | nor2 | bus-adr |
| `boku` | 42.4 | nand2 | bus-adr |

### `a1` (pad_bidir) — diff=10.5 ge, max=50.1 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `cotu` | 50.1 | nor2 | bus-adr |
| `caba` | 39.6 | nand2 | bus-adr |

### `a0` (pad_bidir) — diff=10.2 ge, max=55.8 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `koty` | 55.8 | nor2 | bus-adr |
| `kupo` | 45.6 | nand2 | bus-adr |

### `a4` (pad_bidir) — diff=9.4 ge, max=49.4 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bevo` | 49.4 | nor2 | bus-adr |
| `byla` | 40.0 | nand2 | bus-adr |

### `a10` (pad_bidir) — diff=8.6 ge, max=45.0 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rore` | 45.0 | nor2 | bus-adr |
| `roxu` | 36.4 | nand2 | bus-adr |

### `a3` (pad_bidir) — diff=8.5 ge, max=47.8 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bola` | 47.8 | nor2 | bus-adr |
| `boty` | 39.4 | nand2 | bus-adr |

### `a8` (pad_bidir) — diff=7.3 ge, max=44.3 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mego` | 44.3 | nor2 | bus-adr |
| `myny` | 37.0 | nand2 | bus-adr |

### `a9` (pad_bidir) — diff=6.8 ge, max=42.9 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `meny` | 42.9 | nor2 | bus-adr |
| `mune` | 36.1 | nand2 | bus-adr |

### `a5` (pad_bidir) — diff=6.1 ge, max=40.4 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ajav` | 40.4 | nor2 | bus-adr |
| `badu` | 34.3 | nand2 | bus-adr |

### `a7` (pad_bidir) — diff=5.8 ge, max=49.5 ge | source: `maru` (per-line)
Category: bus-adr | Effective: per-line

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `colo` | 49.5 | nor2 | bus-adr |
| `defy` | 43.6 | nand2 | bus-adr |

### `alor` (dlatch) — diff=33.0 ge, max=33.0 ge | source: `bus:a15` (per-frame)
Category: bus-adr | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a0` | 0.0 |  | bus |

### `alyr` (dlatch) — diff=33.0 ge, max=33.0 ge | source: `bus:a15` (per-frame)
Category: bus-adr | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a2` | 0.0 |  | bus |

### `apur` (dlatch) — diff=33.0 ge, max=33.0 ge | source: `bus:a15` (per-frame)
Category: bus-adr | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a1` | 0.0 |  | bus |

### `aret` (dlatch) — diff=33.0 ge, max=33.0 ge | source: `bus:a15` (per-frame)
Category: bus-adr | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a3` | 0.0 |  | bus |

### `aros` (dlatch) — diff=33.0 ge, max=33.0 ge | source: `bus:a15` (per-frame)
Category: bus-adr | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mate` | 33.0 | not_x1 | bus-adr |
| `bus:a6` | 0.0 |  | bus |


## APU CH1 (Square+Sweep) (106 races) — per-frame

### `hyka` (dffsr) — diff=113.5 ge, max=122.1 ge | source: `avaf` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `efor` | 77.6 | nor2 | apu-ch1 |
| `gylu` | 64.7 | nand2 | apu-ch1 |
| `guxa` | 8.6 | full_add | apu-ch1 |

### `cyto` (nor_latch) — diff=110.5 ge, max=110.5 ge | source: `avaf` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bery` | 110.5 | or4 | apu-ch1 |
| `feku` | 0.0 | dffr | apu-ch1 |

### `jyka` (dffsr) — diff=103.5 ge, max=122.1 ge | source: `avaf` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `gato` | 66.3 | nor2 | apu-ch1 |
| `geta` | 63.8 | nand2 | apu-ch1 |
| `halu` | 18.6 | full_add | apu-ch1 |

### `havo` (dffsr) — diff=98.9 ge, max=122.1 ge | source: `avaf` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `gyfu` | 66.0 | nor2 | apu-ch1 |
| `golo` | 63.9 | nand2 | apu-ch1 |
| `jule` | 23.2 | full_add | apu-ch1 |

### `edul` (dffsr) — diff=90.9 ge, max=122.1 ge | source: `avaf` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `gamo` | 66.6 | nor2 | apu-ch1 |
| `gope` | 64.1 | nand2 | apu-ch1 |
| `jory` | 31.2 | full_add | apu-ch1 |

### `fely` (dffsr) — diff=85.3 ge, max=122.1 ge | source: `avaf` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `kapo` | 74.1 | nor2 | apu-ch1 |
| `kovu` | 65.4 | nand2 | apu-ch1 |
| `hexo` | 36.8 | full_add | apu-ch1 |

### `holu` (dffsr) — diff=80.7 ge, max=122.1 ge | source: `avaf` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boje` | 122.1 | and2 | apu-ch1 |
| `kaju` | 70.2 | nor2 | apu-ch1 |
| `kypa` | 64.8 | nand2 | apu-ch1 |
| `geva` | 41.4 | full_add | apu-ch1 |

### `adek` (drlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ahyc` | 70.5 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 30.0 | not_x1 | apu-control |
| `bus:d4` | 0.0 |  | bus |

### `anaz` (drlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ahyc` | 70.5 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 30.0 | not_x1 | apu-control |
| `bus:d2` | 0.0 |  | bus |

### `arax` (drlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ahyc` | 70.5 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 30.0 | not_x1 | apu-control |
| `bus:d1` | 0.0 |  | bus |

### `avaf` (drlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ahyc` | 70.5 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 30.0 | not_x1 | apu-control |
| `bus:d3` | 0.0 |  | bus |

### `bana` (drlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ahyc` | 70.5 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 30.0 | not_x1 | apu-control |
| `bus:d5` | 0.0 |  | bus |

### `bany` (drlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ahyc` | 70.5 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 30.0 | not_x1 | apu-control |
| `bus:d0` | 0.0 |  | bus |

### `botu` (drlatch_ee) — diff=70.5 ge, max=70.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ahyc` | 70.5 | not_x2 | apu-ch1 |
| `cenu` | 68.9 | and2 | apu-ch1 |
| `agur` | 30.0 | not_x1 | apu-control |
| `bus:d6` | 0.0 |  | bus |

### `gexu` (nand_latch) — diff=68.6 ge, max=68.8 ge | source: `jafy` (per-frame)
Category: apu-ch1 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `femy` | 68.8 | nor2 | apu-ch1 |
| `gepu` | 0.2 | not_x1 | apu-ch1 |


## Other (6 races) — per-frame

### `oam_a` (oam) — diff=89.2 ge, max=101.0 ge | source: `bus:a10` (per-frame)
Category:  | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wame` | 101.0 | not_x2 | ppu-oam |
| `wory` | 93.6 | not_x2 | ppu-oam |
| `wejy` | 89.2 | not_x2 | ppu-oam |
| `wahe` | 85.7 | not_x3 | ppu-oam |
| `wovu` | 70.0 | not_x2 | ppu-oam |
| `wafa` | 23.1 | and2 | ppu-oam |
| `wyxy` | 23.1 | and2 | ppu-oam |
| `wexe` | 22.6 | and2 | ppu-oam |
| `wadu` | 22.4 | not_x1 | ppu-oam |
| `wazu` | 21.9 | and2 | ppu-oam |
| `wuca` | 21.1 | not_x1 | ppu-oam |
| `woso` | 20.9 | not_x1 | ppu-oam |
| `wade` | 20.8 | not_x1 | ppu-oam |
| `wawy` | 20.2 | not_x1 | ppu-oam |
| `yfoc` | 14.1 | not_x1 | ppu-oam |
| `yzet` | 12.7 | not_x1 | ppu-oam |
| `ymev` | 12.5 | not_x1 | ppu-oam |
| `xemu` | 12.4 | not_x1 | ppu-oam |
| `yvom` | 11.8 | not_x1 | ppu-oam |

### `oam_b` (oam) — diff=89.2 ge, max=101.0 ge | source: `bus:a10` (per-frame)
Category:  | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wame` | 101.0 | not_x2 | ppu-oam |
| `wory` | 93.6 | not_x2 | ppu-oam |
| `wexa` | 92.3 | not_x2 | ppu-oam |
| `wahe` | 85.7 | not_x3 | ppu-oam |
| `wovu` | 70.0 | not_x2 | ppu-oam |
| `wafa` | 23.1 | and2 | ppu-oam |
| `wyxy` | 23.1 | and2 | ppu-oam |
| `wexe` | 22.6 | and2 | ppu-oam |
| `wadu` | 22.4 | not_x1 | ppu-oam |
| `wazu` | 21.9 | and2 | ppu-oam |
| `wuca` | 21.1 | not_x1 | ppu-oam |
| `woso` | 20.9 | not_x1 | ppu-oam |
| `wade` | 20.8 | not_x1 | ppu-oam |
| `wawy` | 20.2 | not_x1 | ppu-oam |
| `yfoc` | 14.1 | not_x1 | ppu-oam |
| `yzet` | 12.7 | not_x1 | ppu-oam |
| `ymev` | 12.5 | not_x1 | ppu-oam |
| `xemu` | 12.4 | not_x1 | ppu-oam |
| `yvom` | 11.8 | not_x1 | ppu-oam |

### `wave_ram` (wave_ram) — diff=72.5 ge, max=72.5 ge | source: `bus:a10` (per-frame)
Category:  | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ymul` | 72.5 | or2 | apu-ch3 |
| `yrar` | 67.1 | not_x1 | apu-ch3 |
| `ydez` | 54.9 | not_x1 | apu-ch3 |
| `ygef` | 20.8 | and2 | apu-ch3 |
| `yjej` | 20.6 | and2 | apu-ch3 |
| `yvop` | 20.5 | and2 | apu-ch3 |
| `yfux` | 20.3 | and2 | apu-ch3 |
| `yzeg` | 14.9 | not_x1 | apu-ch3 |
| `ynur` | 14.5 | not_x1 | apu-ch3 |
| `afum` | 14.2 | mux | apu-ch3 |
| `axol` | 13.8 | mux | apu-ch3 |
| `bus:d0` | 0.0 |  | bus |
| `bus:d1` | 0.0 |  | bus |
| `bus:d2` | 0.0 |  | bus |
| `bus:d3` | 0.0 |  | bus |
| `bus:d4` | 0.0 |  | bus |
| `bus:d5` | 0.0 |  | bus |
| `bus:d6` | 0.0 |  | bus |
| `bus:d7` | 0.0 |  | bus |

### `high_ram` (high_ram) — diff=59.1 ge, max=59.1 ge | source: `bus:a10` (per-frame)
Category:  | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `wuly` | 59.1 | not_x2 | hram |
| `abev` | 55.2 | not_x2 | hram |
| `anyk` | 52.3 | not_x1 | hram |
| `apow` | 49.3 | not_x2 | hram |
| `apuh` | 49.2 | not_x2 | hram |
| `wuta` | 43.4 | not_x2 | hram |
| `ajom` | 4.4 | and2 | hram |
| `avub` | 4.2 | and2 | hram |
| `axyc` | 4.0 | and2 | hram |
| `apul` | 3.5 | and2 | hram |
| `wady` | 3.4 | not_x1 | hram |
| `weju` | 3.4 | not_x1 | hram |
| `webe` | 3.4 | not_x1 | hram |
| `woce` | 3.4 | not_x1 | hram |
| `wehu` | 3.4 | not_x1 | hram |
| `bus:a2` | 0.0 |  | bus |
| `bus:a3` | 0.0 |  | bus |
| `bus:a4` | 0.0 |  | bus |
| `bus:a5` | 0.0 |  | bus |
| `bus:a6` | 0.0 |  | bus |

### `boot_rom` (boot_rom) — diff=45.9 ge, max=45.9 ge | source: `t1` (static)
Category:  | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `zoku` | 45.9 | not_x1 | bootrom |
| `zery` | 40.8 | not_x1 | bootrom |
| `zyky` | 8.1 | and2 | bootrom |
| `zyga` | 8.0 | and2 | bootrom |
| `zovy` | 7.8 | and2 | bootrom |
| `zuko` | 7.1 | and2 | bootrom |
| `zabu` | 5.2 | not_x1 | bootrom |
| `zete` | 5.2 | not_x1 | bootrom |
| `zefu` | 4.9 | not_x1 | bootrom |
| `zoke` | 4.9 | not_x1 | bootrom |
| `zyro` | 4.8 | not_x1 | bootrom |
| `zage` | 4.0 | not_x1 | bootrom |
| `zyra` | 3.9 | not_x1 | bootrom |
| `zapa` | 3.8 | not_x1 | bootrom |
| `bus:a2` | 0.0 |  | bus |
| `bus:a3` | 0.0 |  | bus |
| `bus:a6` | 0.0 |  | bus |
| `bus:a7` | 0.0 |  | bus |

### `cpu` (sm83) — diff=30.0 ge, max=30.0 ge | source: `t1` (static)
Category:  | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `taba` | 30.0 | or3 | clocks |
| `syro` | 27.4 | not_x1 | sys-decode |
| `tutu` | 23.1 | and2 | bootrom |
| `bowa` | 15.7 | not_x6 | clocks |
| `unor` | 15.6 | and2 | test |
| `umut` | 15.4 | and2 | test |
| `boma` | 14.5 | not_x6 | clocks |
| `bedo` | 12.7 | not_x6 | clocks |
| `boga` | 11.5 | not_x6 | clocks |
| `buke` | 7.8 | not_x6 | clocks |
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


## Clock Distribution (21 races) — per-frame

### `sola` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `teru` | 0.0 | dffr | clocks |

### `subu` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `sola` | 0.0 | dffr | clocks |

### `tama` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `unyk` | 0.0 | dffr | clocks |

### `teka` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `subu` | 0.0 | dffr | clocks |

### `tero` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `uner` | 0.0 | dffr | clocks |

### `teru` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `tofe` | 0.0 | dffr | clocks |

### `tofe` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `tugo` | 0.0 | dffr | clocks |

### `tugo` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `tulu` | 0.0 | dffr | clocks |

### `tulu` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `ugot` | 0.0 | dffr | clocks |

### `ufor` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `ukup` | 0.0 | dffr | clocks |

### `uket` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `teka` | 0.0 | dffr | clocks |

### `uner` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `ufor` | 0.0 | dffr | clocks |

### `unyk` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `tero` | 0.0 | dffr | clocks |

### `upof` (dffr) — diff=87.8 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `uket` | 0.0 | dffr | clocks |

### `ukup` (dffr) — diff=76.3 ge, max=87.8 ge | source: `bus:a10` (per-frame)
Category: clocks | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ufol` | 87.8 | nor3 | clocks |
| `boga` | 11.5 | not_x6 | clocks |


## APU CH4 (Noise) (71 races) — per-frame

### `cuny` (drlatch_ee) — diff=83.2 ge, max=83.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `cazo` | 83.2 | not_x1 | apu-ch4 |
| `dulu` | 82.8 | nand2 | apu-ch4 |
| `cabe` | 21.6 | not_x1 | apu-ch4 |
| `bus:d6` | 0.0 |  | bus |

### `hoga` (drlatch_ee) — diff=75.2 ge, max=75.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `goxo` | 75.2 | not_x1 | apu-ch4 |
| `foxe` | 74.8 | nand2 | apu-ch4 |
| `guzy` | 22.8 | nor2 | apu-ch4 |
| `bus:d7` | 0.0 |  | bus |

### `garu` (drlatch_ee) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `fupa` | 73.2 | not_x2 | apu-ch4 |
| `goko` | 72.2 | and2 | apu-ch4 |
| `fexo` | 33.7 | not_x1 | apu-ch4 |
| `bus:d4` | 0.0 |  | bus |

### `gedu` (drlatch_ee) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `fupa` | 73.2 | not_x2 | apu-ch4 |
| `goko` | 72.2 | and2 | apu-ch4 |
| `fexo` | 33.7 | not_x1 | apu-ch4 |
| `bus:d7` | 0.0 |  | bus |

### `geky` (drlatch_ee) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `fupa` | 73.2 | not_x2 | apu-ch4 |
| `goko` | 72.2 | and2 | apu-ch4 |
| `fexo` | 33.7 | not_x1 | apu-ch4 |
| `bus:d3` | 0.0 |  | bus |

### `goky` (drlatch_ee) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `fupa` | 73.2 | not_x2 | apu-ch4 |
| `goko` | 72.2 | and2 | apu-ch4 |
| `fexo` | 33.7 | not_x1 | apu-ch4 |
| `bus:d5` | 0.0 |  | bus |

### `gozo` (drlatch_ee) — diff=73.2 ge, max=73.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `fupa` | 73.2 | not_x2 | apu-ch4 |
| `goko` | 72.2 | and2 | apu-ch4 |
| `fexo` | 33.7 | not_x1 | apu-ch4 |
| `bus:d6` | 0.0 |  | bus |

### `gena` (nor_latch) — diff=69.9 ge, max=69.9 ge | source: `garu` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `fegy` | 69.9 | or3 | apu-ch4 |
| `gone` | 0.0 | dffr | apu-ch4 |

### `jery` (nand_latch) — diff=67.8 ge, max=68.3 ge | source: `garu` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `hery` | 68.3 | nor2 | apu-ch4 |
| `hapu` | 0.5 | not_x1 | apu-ch4 |

### `emok` (drlatch_ee) — diff=66.5 ge, max=66.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `dyke` | 66.5 | not_x1 | apu-ch4 |
| `daco` | 64.8 | and2 | apu-ch4 |
| `fexo` | 33.7 | not_x1 | apu-ch4 |
| `bus:d0` | 0.0 |  | bus |

### `etyj` (drlatch_ee) — diff=66.5 ge, max=66.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `dyke` | 66.5 | not_x1 | apu-ch4 |
| `daco` | 64.8 | and2 | apu-ch4 |
| `fexo` | 33.7 | not_x1 | apu-ch4 |
| `bus:d1` | 0.0 |  | bus |

### `ezyk` (drlatch_ee) — diff=66.5 ge, max=66.5 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `dyke` | 66.5 | not_x1 | apu-ch4 |
| `daco` | 64.8 | and2 | apu-ch4 |
| `fexo` | 33.7 | not_x1 | apu-ch4 |
| `bus:d2` | 0.0 |  | bus |

### `feta` (drlatch_ee) — diff=66.2 ge, max=66.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `efug` | 66.2 | not_x2 | apu-ch4 |
| `getu` | 65.3 | and2 | apu-ch4 |
| `dapa` | 28.6 | not_x2 | apu-control |
| `bus:d4` | 0.0 |  | bus |

### `fyto` (drlatch_ee) — diff=66.2 ge, max=66.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `efug` | 66.2 | not_x2 | apu-ch4 |
| `getu` | 65.3 | and2 | apu-ch4 |
| `dapa` | 28.6 | not_x2 | apu-control |
| `bus:d5` | 0.0 |  | bus |

### `gafo` (drlatch_ee) — diff=66.2 ge, max=66.2 ge | source: `bus:a10` (per-frame)
Category: apu-ch4 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `efug` | 66.2 | not_x2 | apu-ch4 |
| `getu` | 65.3 | and2 | apu-ch4 |
| `dapa` | 28.6 | not_x2 | apu-control |
| `bus:d7` | 0.0 |  | bus |


## Palettes (24 races) — per-frame

### `xalo` (dlatch_ee) — diff=74.5 ge, max=74.5 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xojo` | 74.5 | not_x1 | ppu-pal |
| `xelo` | 69.2 | not_x1 | ppu-pal |
| `bus:d3` | 0.0 |  | bus |

### `xana` (dlatch_ee) — diff=74.5 ge, max=74.5 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xojo` | 74.5 | not_x1 | ppu-pal |
| `xelo` | 69.2 | not_x1 | ppu-pal |
| `bus:d7` | 0.0 |  | bus |

### `xeru` (dlatch_ee) — diff=74.5 ge, max=74.5 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xojo` | 74.5 | not_x1 | ppu-pal |
| `xelo` | 69.2 | not_x1 | ppu-pal |
| `bus:d4` | 0.0 |  | bus |

### `xova` (dlatch_ee) — diff=74.5 ge, max=74.5 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xojo` | 74.5 | not_x1 | ppu-pal |
| `xelo` | 69.2 | not_x1 | ppu-pal |
| `bus:d2` | 0.0 |  | bus |

### `xufu` (dlatch_ee) — diff=74.5 ge, max=74.5 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xojo` | 74.5 | not_x1 | ppu-pal |
| `xelo` | 69.2 | not_x1 | ppu-pal |
| `bus:d0` | 0.0 |  | bus |

### `xuky` (dlatch_ee) — diff=74.5 ge, max=74.5 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xojo` | 74.5 | not_x1 | ppu-pal |
| `xelo` | 69.2 | not_x1 | ppu-pal |
| `bus:d1` | 0.0 |  | bus |

### `xupo` (dlatch_ee) — diff=74.5 ge, max=74.5 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xojo` | 74.5 | not_x1 | ppu-pal |
| `xelo` | 69.2 | not_x1 | ppu-pal |
| `bus:d6` | 0.0 |  | bus |

### `xyze` (dlatch_ee) — diff=74.5 ge, max=74.5 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xojo` | 74.5 | not_x1 | ppu-pal |
| `xelo` | 69.2 | not_x1 | ppu-pal |
| `bus:d5` | 0.0 |  | bus |

### `maxy` (dlatch_ee) — diff=62.9 ge, max=62.9 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfa` | 62.9 | not_x1 | ppu-pal |
| `tepo` | 59.9 | not_x1 | ppu-pal |
| `bus:d3` | 0.0 |  | bus |

### `mena` (dlatch_ee) — diff=62.9 ge, max=62.9 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfa` | 62.9 | not_x1 | ppu-pal |
| `tepo` | 59.9 | not_x1 | ppu-pal |
| `bus:d7` | 0.0 |  | bus |

### `mogy` (dlatch_ee) — diff=62.9 ge, max=62.9 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfa` | 62.9 | not_x1 | ppu-pal |
| `tepo` | 59.9 | not_x1 | ppu-pal |
| `bus:d6` | 0.0 |  | bus |

### `moru` (dlatch_ee) — diff=62.9 ge, max=62.9 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfa` | 62.9 | not_x1 | ppu-pal |
| `tepo` | 59.9 | not_x1 | ppu-pal |
| `bus:d5` | 0.0 |  | bus |

### `muke` (dlatch_ee) — diff=62.9 ge, max=62.9 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfa` | 62.9 | not_x1 | ppu-pal |
| `tepo` | 59.9 | not_x1 | ppu-pal |
| `bus:d4` | 0.0 |  | bus |

### `nusy` (dlatch_ee) — diff=62.9 ge, max=62.9 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfa` | 62.9 | not_x1 | ppu-pal |
| `tepo` | 59.9 | not_x1 | ppu-pal |
| `bus:d1` | 0.0 |  | bus |

### `pavo` (dlatch_ee) — diff=62.9 ge, max=62.9 ge | source: `bus:a10` (per-frame)
Category: ppu-pal | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfa` | 62.9 | not_x1 | ppu-pal |
| `tepo` | 59.9 | not_x1 | ppu-pal |
| `bus:d0` | 0.0 |  | bus |


## APU CH2 (Square) (60 races) — per-frame

### `buta` (nand_latch) — diff=73.6 ge, max=73.9 ge | source: `fore` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ares` | 73.9 | nor2 | apu-ch2 |
| `bodo` | 0.3 | not_x1 | apu-ch2 |

### `jany` (drlatch_ee) — diff=72.6 ge, max=72.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kysa` | 72.6 | not_x1 | apu-ch2 |
| `jenu` | 71.0 | and2 | apu-ch2 |
| `kypu` | 22.8 | not_x1 | apu-ch2 |
| `bus:d1` | 0.0 |  | bus |

### `jefu` (drlatch_ee) — diff=72.6 ge, max=72.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kysa` | 72.6 | not_x1 | apu-ch2 |
| `jenu` | 71.0 | and2 | apu-ch2 |
| `kypu` | 22.8 | not_x1 | apu-ch2 |
| `bus:d0` | 0.0 |  | bus |

### `jupy` (drlatch_ee) — diff=72.6 ge, max=72.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kysa` | 72.6 | not_x1 | apu-ch2 |
| `jenu` | 71.0 | and2 | apu-ch2 |
| `kypu` | 22.8 | not_x1 | apu-ch2 |
| `bus:d2` | 0.0 |  | bus |

### `dane` (nor_latch) — diff=69.7 ge, max=69.7 ge | source: `fore` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `esyk` | 69.7 | or3 | apu-ch2 |
| `elox` | 0.0 | dffr | apu-ch2 |

### `etap` (drlatch_ee) — diff=69.6 ge, max=69.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `daxu` | 69.6 | not_x1 | apu-ch2 |
| `deta` | 69.2 | nand2 | apu-ch2 |
| `dera` | 27.2 | nor2 | apu-ch2 |
| `bus:d7` | 0.0 |  | bus |

### `emer` (drlatch_ee) — diff=67.6 ge, max=67.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `duso` | 67.6 | not_x1 | apu-ch2 |
| `evyf` | 67.2 | nand2 | apu-ch2 |
| `fazo` | 21.9 | not_x1 | apu-ch2 |
| `bus:d6` | 0.0 |  | bus |

### `fore` (drlatch_ee) — diff=61.3 ge, max=61.3 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `elas` | 61.3 | not_x2 | apu-ch2 |
| `enuf` | 59.7 | and2 | apu-ch2 |
| `jybu` | 25.6 | not_x1 | apu-ch2 |
| `bus:d3` | 0.0 |  | bus |

### `gata` (drlatch_ee) — diff=61.3 ge, max=61.3 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `elas` | 61.3 | not_x2 | apu-ch2 |
| `enuf` | 59.7 | and2 | apu-ch2 |
| `jybu` | 25.6 | not_x1 | apu-ch2 |
| `bus:d4` | 0.0 |  | bus |

### `gufe` (drlatch_ee) — diff=61.3 ge, max=61.3 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `elas` | 61.3 | not_x2 | apu-ch2 |
| `enuf` | 59.7 | and2 | apu-ch2 |
| `jybu` | 25.6 | not_x1 | apu-ch2 |
| `bus:d5` | 0.0 |  | bus |

### `gura` (drlatch_ee) — diff=61.3 ge, max=61.3 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `elas` | 61.3 | not_x2 | apu-ch2 |
| `enuf` | 59.7 | and2 | apu-ch2 |
| `jybu` | 25.6 | not_x1 | apu-ch2 |
| `bus:d6` | 0.0 |  | bus |

### `came` (tffnl) — diff=60.7 ge, max=60.7 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bymo` | 60.7 | not_x1 | apu-ch2 |
| `bus:d3` | 0.0 |  | bus |
| `conu` | 0.0 | tffnl | apu-ch2 |

### `cera` (tffnl) — diff=60.7 ge, max=60.7 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bymo` | 60.7 | not_x1 | apu-ch2 |
| `bus:d1` | 0.0 |  | bus |
| `eryc` | 0.0 | tffnl | apu-ch2 |

### `conu` (tffnl) — diff=60.7 ge, max=60.7 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bymo` | 60.7 | not_x1 | apu-ch2 |
| `bus:d2` | 0.0 |  | bus |
| `cera` | 0.0 | tffnl | apu-ch2 |

### `eryc` (tffnl) — diff=60.7 ge, max=60.7 ge | source: `bus:a10` (per-frame)
Category: apu-ch2 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bymo` | 60.7 | not_x1 | apu-ch2 |
| `dyro` | 18.5 | not_x1 | apu-ch1 |
| `bus:d0` | 0.0 |  | bus |


## Serial (18 races) — per-frame

### `eder` (dffsr) — diff=73.0 ge, max=73.0 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `efef` | 73.0 | nand2 | serial |
| `eguv` | 65.9 | oa21 | serial |
| `epyt` | 21.6 | not_x2 | serial |
| `erod` | 0.0 | dffsr | serial |

### `ejab` (dffsr) — diff=73.0 ge, max=73.0 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `elok` | 73.0 | nand2 | serial |
| `ehuj` | 65.9 | oa21 | serial |
| `epyt` | 21.6 | not_x2 | serial |
| `dovu` | 0.0 | dffsr | serial |

### `erod` (dffsr) — diff=73.0 ge, max=73.0 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `edel` | 73.0 | nand2 | serial |
| `efak` | 65.9 | oa21 | serial |
| `epyt` | 21.6 | not_x2 | serial |
| `ejab` | 0.0 | dffsr | serial |

### `degu` (dffsr) — diff=73.0 ge, max=73.0 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `docu` | 73.0 | nand2 | serial |
| `dumo` | 65.9 | oa21 | serial |
| `dawe` | 23.2 | not_x2 | serial |
| `cuba` | 0.0 | dffsr | serial |

### `dojo` (dffsr) — diff=73.0 ge, max=73.0 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `dyge` | 73.0 | nand2 | serial |
| `daju` | 65.9 | oa21 | serial |
| `dawe` | 23.2 | not_x2 | serial |
| `dyra` | 0.0 | dffsr | serial |

### `dovu` (dffsr) — diff=73.0 ge, max=73.0 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `dola` | 73.0 | nand2 | serial |
| `dyly` | 65.9 | oa21 | serial |
| `epyt` | 21.6 | not_x2 | serial |
| `dojo` | 0.0 | dffsr | serial |

### `dyra` (dffsr) — diff=73.0 ge, max=73.0 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `dela` | 73.0 | nand2 | serial |
| `dybo` | 65.9 | oa21 | serial |
| `dawe` | 23.2 | not_x2 | serial |
| `degu` | 0.0 | dffsr | serial |

### `cuba` (dffsr) — diff=72.2 ge, max=73.0 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `cufu` | 73.0 | nand2 | serial |
| `cohy` | 65.9 | oa21 | serial |
| `dawe` | 23.2 | not_x2 | serial |
| `cage` | 0.8 | not_x1 | serial |

### `caly` (dffr) — diff=65.4 ge, max=65.4 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `caro` | 65.4 | and2 | serial |
| `cyde` | 0.0 | dffr | serial |

### `cyde` (dffr) — diff=65.4 ge, max=65.4 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `caro` | 65.4 | and2 | serial |
| `cylo` | 0.0 | dffr | serial |

### `cylo` (dffr) — diff=65.4 ge, max=65.4 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `caro` | 65.4 | and2 | serial |
| `cafa` | 0.0 | dffr | serial |

### `culy` (dffr) — diff=62.6 ge, max=62.6 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `uwam` | 62.6 | nand4 | serial |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d0` | 0.0 |  | bus |

### `etaf` (dffr) — diff=62.6 ge, max=62.6 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `uwam` | 62.6 | nand4 | serial |
| `caby` | 10.8 | and2 | serial |
| `bus:d7` | 0.0 |  | bus |

### `coty` (dffr) — diff=57.5 ge, max=62.6 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `uwam` | 62.6 | nand4 | serial |
| `uvyn` | 5.2 | not_x1 | clocks |

### `cafa` (dffr) — diff=46.8 ge, max=65.4 ge | source: `bus:a10` (per-frame)
Category: serial | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `caro` | 65.4 | and2 | serial |
| `dawa` | 18.5 | or2 | serial |


## APU CH3 (Wave) (64 races) — per-frame

### `jacy` (drlatch_ee) — diff=72.8 ge, max=72.8 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `hufa` | 72.8 | not_x1 | apu-ch3 |
| `huda` | 71.9 | and2 | apu-ch3 |
| `kopy` | 23.0 | not_x1 | apu-ch3 |
| `bus:d2` | 0.0 |  | bus |

### `jemo` (drlatch_ee) — diff=72.8 ge, max=72.8 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `hufa` | 72.8 | not_x1 | apu-ch3 |
| `huda` | 71.9 | and2 | apu-ch3 |
| `kopy` | 23.0 | not_x1 | apu-ch3 |
| `bus:d0` | 0.0 |  | bus |

### `jety` (drlatch_ee) — diff=72.8 ge, max=72.8 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `hufa` | 72.8 | not_x1 | apu-ch3 |
| `huda` | 71.9 | and2 | apu-ch3 |
| `kopy` | 23.0 | not_x1 | apu-ch3 |
| `bus:d1` | 0.0 |  | bus |

### `gavu` (drlatch_ee) — diff=70.3 ge, max=70.3 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `fene` | 70.3 | not_x1 | apu-ch3 |
| `epyx` | 69.9 | nand2 | apu-ch3 |
| `fako` | 22.2 | nor2 | apu-ch3 |
| `bus:d7` | 0.0 |  | bus |

### `hoto` (drlatch_ee) — diff=69.1 ge, max=69.1 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `gygu` | 69.1 | not_x1 | apu-ch3 |
| `fovo` | 68.6 | nand2 | apu-ch3 |
| `heky` | 22.9 | not_x1 | apu-ch3 |
| `bus:d6` | 0.0 |  | bus |

### `gage` (drlatch_ee) — diff=61.3 ge, max=61.3 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `elas` | 61.3 | not_x2 | apu-ch2 |
| `enuf` | 59.7 | and2 | apu-ch2 |
| `jybu` | 25.6 | not_x1 | apu-ch2 |
| `bus:d7` | 0.0 |  | bus |

### `jaxa` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kuly` | 59.6 | not_x2 | apu-ch3 |
| `jafa` | 58.2 | and2 | apu-ch3 |
| `kuha` | 25.4 | not_x1 | apu-ch3 |
| `bus:d2` | 0.0 |  | bus |

### `jefe` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kuly` | 59.6 | not_x2 | apu-ch3 |
| `jafa` | 58.2 | and2 | apu-ch3 |
| `kuha` | 25.4 | not_x1 | apu-ch3 |
| `bus:d3` | 0.0 |  | bus |

### `jovy` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kuly` | 59.6 | not_x2 | apu-ch3 |
| `jafa` | 58.2 | and2 | apu-ch3 |
| `kuha` | 25.4 | not_x1 | apu-ch3 |
| `bus:d1` | 0.0 |  | bus |

### `jypo` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kuly` | 59.6 | not_x2 | apu-ch3 |
| `jafa` | 58.2 | and2 | apu-ch3 |
| `kuha` | 25.4 | not_x1 | apu-ch3 |
| `bus:d4` | 0.0 |  | bus |

### `koga` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kuly` | 59.6 | not_x2 | apu-ch3 |
| `jafa` | 58.2 | and2 | apu-ch3 |
| `kuha` | 25.4 | not_x1 | apu-ch3 |
| `bus:d0` | 0.0 |  | bus |

### `guxe` (drlatch_ee) — diff=59.3 ge, max=59.3 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `gucy` | 59.3 | not_x1 | apu-ch3 |
| `gejo` | 59.0 | and2 | apu-ch3 |
| `gove` | 21.7 | not_x1 | apu-ch3 |
| `bus:d7` | 0.0 |  | bus |

### `fexu` (dffr) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `guda` | 58.7 | nor3 | apu-ch3 |
| `fyru` | 0.0 | tffnl | apu-ch3 |

### `jove` (drlatch_ee) — diff=58.6 ge, max=58.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kyho` | 58.6 | not_x1 | apu-ch3 |
| `kota` | 57.2 | and2 | apu-ch3 |
| `kuha` | 25.4 | not_x1 | apu-ch3 |
| `bus:d5` | 0.0 |  | bus |

### `kana` (drlatch_ee) — diff=58.6 ge, max=58.6 ge | source: `bus:a10` (per-frame)
Category: apu-ch3 | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kyho` | 58.6 | not_x1 | apu-ch3 |
| `kota` | 57.2 | and2 | apu-ch3 |
| `kuha` | 25.4 | not_x1 | apu-ch3 |
| `bus:d6` | 0.0 |  | bus |


## Timer (21 races) — per-frame

### `nydu` (dffr) — diff=72.1 ge, max=72.1 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mugy` | 72.1 | not_x1 | timer |
| `boga` | 11.5 | not_x6 | clocks |
| `nuga` | 0.0 | tffnl | timer |

### `nuga` (tffnl) — diff=71.0 ge, max=71.0 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mexu` | 71.0 | nand3 | timer |
| `pagu` | 66.8 | nor2 | timer |
| `peda` | 0.0 | tffnl | timer |

### `peda` (tffnl) — diff=71.0 ge, max=71.0 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mexu` | 71.0 | nand3 | timer |
| `pyma` | 65.5 | nor2 | timer |
| `rage` | 0.0 | tffnl | timer |

### `peru` (tffnl) — diff=71.0 ge, max=71.0 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mexu` | 71.0 | nand3 | timer |
| `nada` | 65.9 | nor2 | timer |
| `povy` | 0.0 | tffnl | timer |

### `povy` (tffnl) — diff=71.0 ge, max=71.0 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mexu` | 71.0 | nand3 | timer |
| `nero` | 66.0 | nor2 | timer |
| `rega` | 0.0 | tffnl | timer |

### `rage` (tffnl) — diff=71.0 ge, max=71.0 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mexu` | 71.0 | nand3 | timer |
| `rugy` | 65.8 | nor2 | timer |
| `ruby` | 0.0 | tffnl | timer |

### `rate` (tffnl) — diff=71.0 ge, max=71.0 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mexu` | 71.0 | nand3 | timer |
| `repa` | 65.0 | nor2 | timer |
| `peru` | 0.0 | tffnl | timer |

### `ruby` (tffnl) — diff=71.0 ge, max=71.0 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mexu` | 71.0 | nand3 | timer |
| `rolu` | 64.1 | nor2 | timer |
| `rate` | 0.0 | tffnl | timer |

### `muru` (dffr) — diff=59.7 ge, max=59.7 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tyju` | 59.7 | nand4 | timer |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d2` | 0.0 |  | bus |

### `nyke` (dffr) — diff=59.7 ge, max=59.7 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tyju` | 59.7 | nand4 | timer |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d1` | 0.0 |  | bus |

### `peto` (dffr) — diff=59.7 ge, max=59.7 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tyju` | 59.7 | nand4 | timer |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d6` | 0.0 |  | bus |

### `sabu` (dffr) — diff=59.7 ge, max=59.7 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tyju` | 59.7 | nand4 | timer |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d0` | 0.0 |  | bus |

### `seta` (dffr) — diff=59.7 ge, max=59.7 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tyju` | 59.7 | nand4 | timer |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d7` | 0.0 |  | bus |

### `sufy` (dffr) — diff=59.7 ge, max=59.7 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tyju` | 59.7 | nand4 | timer |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d5` | 0.0 |  | bus |

### `tyru` (dffr) — diff=59.7 ge, max=59.7 ge | source: `bus:a10` (per-frame)
Category: timer | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tyju` | 59.7 | nand4 | timer |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d4` | 0.0 |  | bus |


## APU Control (31 races) — per-frame

### `anev` (drlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `acup` | 71.2 | not_x2 | apu-control |
| `bono` | 69.8 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d0` | 0.0 |  | bus |

### `atuf` (drlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `acup` | 71.2 | not_x2 | apu-control |
| `bono` | 69.8 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d3` | 0.0 |  | bus |

### `bafo` (drlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `acup` | 71.2 | not_x2 | apu-control |
| `bono` | 69.8 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d2` | 0.0 |  | bus |

### `bogu` (drlatch_ee) — diff=71.2 ge, max=71.2 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `acup` | 71.2 | not_x2 | apu-control |
| `bono` | 69.8 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d1` | 0.0 |  | bus |

### `befo` (drlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `acyj` | 70.6 | not_x2 | apu-control |
| `byfa` | 69.5 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d6` | 0.0 |  | bus |

### `bepu` (drlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `acyj` | 70.6 | not_x2 | apu-control |
| `byfa` | 69.5 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d7` | 0.0 |  | bus |

### `bofa` (drlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `acyj` | 70.6 | not_x2 | apu-control |
| `byfa` | 69.5 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d5` | 0.0 |  | bus |

### `bume` (drlatch_ee) — diff=70.6 ge, max=70.6 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `acyj` | 70.6 | not_x2 | apu-control |
| `byfa` | 69.5 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d4` | 0.0 |  | bus |

### `bedu` (drlatch_ee) — diff=65.9 ge, max=65.9 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bubu` | 65.9 | not_x2 | apu-control |
| `baxy` | 64.6 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d7` | 0.0 |  | bus |

### `bumo` (drlatch_ee) — diff=65.9 ge, max=65.9 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bubu` | 65.9 | not_x2 | apu-control |
| `baxy` | 64.6 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d5` | 0.0 |  | bus |

### `byre` (drlatch_ee) — diff=65.9 ge, max=65.9 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bubu` | 65.9 | not_x2 | apu-control |
| `baxy` | 64.6 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d4` | 0.0 |  | bus |

### `cozu` (drlatch_ee) — diff=65.9 ge, max=65.9 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bubu` | 65.9 | not_x2 | apu-control |
| `baxy` | 64.6 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d6` | 0.0 |  | bus |

### `ager` (drlatch_ee) — diff=65.3 ge, max=65.3 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ataf` | 65.3 | not_x2 | apu-control |
| `bowe` | 64.2 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d2` | 0.0 |  | bus |

### `apeg` (drlatch_ee) — diff=65.3 ge, max=65.3 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ataf` | 65.3 | not_x2 | apu-control |
| `bowe` | 64.2 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d0` | 0.0 |  | bus |

### `apos` (drlatch_ee) — diff=65.3 ge, max=65.3 ge | source: `bus:a10` (per-frame)
Category: apu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ataf` | 65.3 | not_x2 | apu-control |
| `bowe` | 64.2 | not_x2 | apu-control |
| `kepy` | 23.1 | not_x3 | apu-control |
| `bus:d3` | 0.0 |  | bus |


## Joypad (15 races) — per-frame

### `cofy` (dffr) — diff=70.1 ge, max=70.1 ge | source: `bus:a10` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `atoz` | 70.1 | nand4 | joypad |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d5` | 0.0 |  | bus |

### `kely` (dffr) — diff=70.1 ge, max=70.1 ge | source: `bus:a10` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `atoz` | 70.1 | nand4 | joypad |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d4` | 0.0 |  | bus |

### `kapa` (dlatch) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byzo` | 58.7 | not_x1 | joypad |
| `p11` | 0.0 | pad_bidir_pu | joypad |

### `keja` (dlatch) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byzo` | 58.7 | not_x1 | joypad |
| `p12` | 0.0 | pad_bidir_pu | joypad |

### `kevu` (dlatch) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byzo` | 58.7 | not_x1 | joypad |
| `p10` | 0.0 | pad_bidir_pu | joypad |

### `kolo` (dlatch) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byzo` | 58.7 | not_x1 | joypad |
| `p13` | 0.0 | pad_bidir_pu | joypad |

### `acef` (dffr) — diff=11.5 ge, max=11.5 ge | source: `afur` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boga` | 11.5 | not_x6 | clocks |
| `alur` | 8.6 | not_x2 | clocks |
| `batu` | 0.0 | dffr | joypad |

### `agem` (dffr) — diff=11.5 ge, max=11.5 ge | source: `afur` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boga` | 11.5 | not_x6 | clocks |
| `alur` | 8.6 | not_x2 | clocks |
| `acef` | 0.0 | dffr | joypad |

### `apug` (dffr) — diff=11.5 ge, max=11.5 ge | source: `afur` (per-frame)
Category: joypad | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `boga` | 11.5 | not_x6 | clocks |
| `alur` | 8.6 | not_x2 | clocks |
| `agem` | 0.0 | dffr | joypad |

### `p13` (pad_bidir_pu) — diff=25.5 ge, max=35.3 ge | source: `buro` (static)
Category: joypad | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kale` | 35.3 | nor2 | test |
| `kory` | 9.9 | nand2 | test |

### `p14` (pad_out_diff) — diff=25.4 ge, max=25.4 ge | source: `buro` (static)
Category: joypad | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `karu` | 25.4 | or2 | joypad |
| `kely` | 0.0 | dffr | joypad |

### `p15` (pad_out_diff) — diff=21.8 ge, max=21.8 ge | source: `buro` (static)
Category: joypad | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `cela` | 21.8 | or2 | joypad |
| `cofy` | 0.0 | dffr | joypad |

### `p11` (pad_bidir_pu) — diff=21.2 ge, max=25.7 ge | source: `buro` (static)
Category: joypad | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kabu` | 25.7 | nor2 | test |
| `kyto` | 4.5 | nand2 | test |

### `p12` (pad_bidir_pu) — diff=20.5 ge, max=25.4 ge | source: `buro` (static)
Category: joypad | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kasy` | 25.4 | nor2 | test |
| `kyhu` | 5.0 | nand2 | test |

### `p10` (pad_bidir_pu) — diff=20.1 ge, max=24.2 ge | source: `buro` (static)
Category: joypad | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `kybu` | 24.2 | nor2 | test |
| `kole` | 4.0 | nand2 | test |


## DMA (22 races) — per-frame

### `maru` (dlatch_ee) — diff=65.5 ge, max=65.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pysu` | 65.5 | not_x1 | ppu-dma |
| `loru` | 61.2 | not_x1 | ppu-dma |
| `bus:d7` | 0.0 |  | bus |

### `nafa` (dlatch_ee) — diff=65.5 ge, max=65.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pysu` | 65.5 | not_x1 | ppu-dma |
| `loru` | 61.2 | not_x1 | ppu-dma |
| `bus:d0` | 0.0 |  | bus |

### `nydo` (dlatch_ee) — diff=65.5 ge, max=65.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pysu` | 65.5 | not_x1 | ppu-dma |
| `loru` | 61.2 | not_x1 | ppu-dma |
| `bus:d3` | 0.0 |  | bus |

### `nygy` (dlatch_ee) — diff=65.5 ge, max=65.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pysu` | 65.5 | not_x1 | ppu-dma |
| `loru` | 61.2 | not_x1 | ppu-dma |
| `bus:d4` | 0.0 |  | bus |

### `para` (dlatch_ee) — diff=65.5 ge, max=65.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pysu` | 65.5 | not_x1 | ppu-dma |
| `loru` | 61.2 | not_x1 | ppu-dma |
| `bus:d2` | 0.0 |  | bus |

### `poku` (dlatch_ee) — diff=65.5 ge, max=65.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pysu` | 65.5 | not_x1 | ppu-dma |
| `loru` | 61.2 | not_x1 | ppu-dma |
| `bus:d6` | 0.0 |  | bus |

### `pula` (dlatch_ee) — diff=65.5 ge, max=65.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pysu` | 65.5 | not_x1 | ppu-dma |
| `loru` | 61.2 | not_x1 | ppu-dma |
| `bus:d5` | 0.0 |  | bus |

### `pyne` (dlatch_ee) — diff=65.5 ge, max=65.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pysu` | 65.5 | not_x1 | ppu-dma |
| `loru` | 61.2 | not_x1 | ppu-dma |
| `bus:d1` | 0.0 |  | bus |

### `luvy` (dffr) — diff=55.3 ge, max=57.6 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lupa` | 57.6 | nor2 | ppu-dma |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `uvyt` | 2.3 | not_x2 | clocks |

### `wuje` (nor_latch) — diff=39.8 ge, max=51.5 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xuto` | 51.5 | and2 | ppu-oam |
| `xyny` | 11.8 | not_x1 | ppu-dma |

### `lyxe` (nor_latch) — diff=38.5 ge, max=56.0 ge | source: `bus:a10` (per-frame)
Category: ppu-dma | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavy` | 56.0 | and2 | ppu-dma |
| `loko` | 17.5 | nand2 | ppu-dma |

### `mugu` (dffr) — diff=23.8 ge, max=23.8 ge | source: `afer` (static)
Category: ppu-dma | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lapa` | 23.8 | not_x1 | ppu-dma |
| `nuto` | 0.0 | dffr | ppu-dma |

### `muty` (dffr) — diff=23.8 ge, max=23.8 ge | source: `afer` (static)
Category: ppu-dma | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lapa` | 23.8 | not_x1 | ppu-dma |
| `nefy` | 0.0 | dffr | ppu-dma |

### `nefy` (dffr) — diff=23.8 ge, max=23.8 ge | source: `afer` (static)
Category: ppu-dma | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lapa` | 23.8 | not_x1 | ppu-dma |
| `pyro` | 0.0 | dffr | ppu-dma |

### `nuto` (dffr) — diff=23.8 ge, max=23.8 ge | source: `afer` (static)
Category: ppu-dma | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lapa` | 23.8 | not_x1 | ppu-dma |
| `pylo` | 0.0 | dffr | ppu-dma |


## STAT/LY (32 races) — per-frame

### `raha` (drlatch_ee) — diff=57.8 ge, max=57.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voze` | 57.8 | not_x1 | ppu-stat |
| `wane` | 53.8 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d7` | 0.0 |  | bus |

### `salo` (drlatch_ee) — diff=57.8 ge, max=57.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voze` | 57.8 | not_x1 | ppu-stat |
| `wane` | 53.8 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d3` | 0.0 |  | bus |

### `sedy` (drlatch_ee) — diff=57.8 ge, max=57.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voze` | 57.8 | not_x1 | ppu-stat |
| `wane` | 53.8 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d2` | 0.0 |  | bus |

### `sota` (drlatch_ee) — diff=57.8 ge, max=57.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voze` | 57.8 | not_x1 | ppu-stat |
| `wane` | 53.8 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d4` | 0.0 |  | bus |

### `syry` (drlatch_ee) — diff=57.8 ge, max=57.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voze` | 57.8 | not_x1 | ppu-stat |
| `wane` | 53.8 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d0` | 0.0 |  | bus |

### `vafa` (drlatch_ee) — diff=57.8 ge, max=57.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voze` | 57.8 | not_x1 | ppu-stat |
| `wane` | 53.8 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d5` | 0.0 |  | bus |

### `vevo` (drlatch_ee) — diff=57.8 ge, max=57.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voze` | 57.8 | not_x1 | ppu-stat |
| `wane` | 53.8 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d6` | 0.0 |  | bus |

### `vuce` (drlatch_ee) — diff=57.8 ge, max=57.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `voze` | 57.8 | not_x1 | ppu-stat |
| `wane` | 53.8 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d1` | 0.0 |  | bus |

### `refe` (drlatch_ee) — diff=53.8 ge, max=53.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pupu` | 53.8 | not_x1 | ppu-stat |
| `ryve` | 52.0 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d5` | 0.0 |  | bus |

### `roxe` (drlatch_ee) — diff=53.8 ge, max=53.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pupu` | 53.8 | not_x1 | ppu-stat |
| `ryve` | 52.0 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d3` | 0.0 |  | bus |

### `rufo` (drlatch_ee) — diff=53.8 ge, max=53.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pupu` | 53.8 | not_x1 | ppu-stat |
| `ryve` | 52.0 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d4` | 0.0 |  | bus |

### `rugu` (drlatch_ee) — diff=53.8 ge, max=53.8 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pupu` | 53.8 | not_x1 | ppu-stat |
| `ryve` | 52.0 | not_x1 | ppu-stat |
| `wesy` | 24.8 | not_x2 | ppu-stat |
| `bus:d6` | 0.0 |  | bus |

### `rupo` (nor_latch) — diff=53.5 ge, max=53.5 ge | source: `bus:a10` (per-frame)
Category: ppu-stat | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `pago` | 53.5 | or2 | ppu-stat |
| `ropo` | 0.0 | dffr | ppu-stat |

### `tuky` (dffr) — diff=64.7 ge, max=66.3 ge | source: `afer` (static)
Category: ppu-stat | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tady` | 66.3 | nor2 | ppu-stat |
| `toca` | 2.2 | not_x1 | ppu-stat |
| `sake` | 1.6 | xor | ppu-stat |

### `savy` (dffr) — diff=64.6 ge, max=66.3 ge | source: `afer` (static)
Category: ppu-stat | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tady` | 66.3 | nor2 | ppu-stat |
| `sacu` | 63.8 | or2 | ppu-cycles |
| `rybo` | 1.7 | xor | ppu-stat |


## Window Logic (31 races) — per-frame

### `mela` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nuta` | 59.6 | not_x1 | ppu-window |
| `vefu` | 56.1 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d3` | 0.0 |  | bus |

### `nafu` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nuta` | 59.6 | not_x1 | ppu-window |
| `vefu` | 56.1 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d7` | 0.0 |  | bus |

### `naga` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nuta` | 59.6 | not_x1 | ppu-window |
| `vefu` | 56.1 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d2` | 0.0 |  | bus |

### `nene` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nuta` | 59.6 | not_x1 | ppu-window |
| `vefu` | 56.1 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d5` | 0.0 |  | bus |

### `neso` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nuta` | 59.6 | not_x1 | ppu-window |
| `vefu` | 56.1 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d0` | 0.0 |  | bus |

### `nuka` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nuta` | 59.6 | not_x1 | ppu-window |
| `vefu` | 56.1 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d6` | 0.0 |  | bus |

### `nulo` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nuta` | 59.6 | not_x1 | ppu-window |
| `vefu` | 56.1 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d4` | 0.0 |  | bus |

### `nyro` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `nuta` | 59.6 | not_x1 | ppu-window |
| `vefu` | 56.1 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d1` | 0.0 |  | bus |

### `meby` (drlatch_ee) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mare` | 58.7 | not_x1 | ppu-window |
| `voxu` | 55.4 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d3` | 0.0 |  | bus |

### `muvo` (drlatch_ee) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mare` | 58.7 | not_x1 | ppu-window |
| `voxu` | 55.4 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d6` | 0.0 |  | bus |

### `myce` (drlatch_ee) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mare` | 58.7 | not_x1 | ppu-window |
| `voxu` | 55.4 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d5` | 0.0 |  | bus |

### `mypa` (drlatch_ee) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mare` | 58.7 | not_x1 | ppu-window |
| `voxu` | 55.4 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d0` | 0.0 |  | bus |

### `mypu` (drlatch_ee) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mare` | 58.7 | not_x1 | ppu-window |
| `voxu` | 55.4 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d4` | 0.0 |  | bus |

### `nofe` (drlatch_ee) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mare` | 58.7 | not_x1 | ppu-window |
| `voxu` | 55.4 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d1` | 0.0 |  | bus |

### `noke` (drlatch_ee) — diff=58.7 ge, max=58.7 ge | source: `bus:a10` (per-frame)
Category: ppu-window | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mare` | 58.7 | not_x1 | ppu-window |
| `voxu` | 55.4 | not_x1 | ppu-window |
| `walu` | 25.8 | not_x2 | ppu-window |
| `bus:d2` | 0.0 |  | bus |


## PPU Control (8 races) — per-frame

### `vyxe` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xure` | 59.6 | not_x1 | ppu-control |
| `xubo` | 54.8 | not_x1 | ppu-control |
| `xare` | 27.4 | not_x1 | ppu-control |
| `bus:d0` | 0.0 |  | bus |

### `wexu` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xure` | 59.6 | not_x1 | ppu-control |
| `xubo` | 54.8 | not_x1 | ppu-control |
| `xare` | 27.4 | not_x1 | ppu-control |
| `bus:d4` | 0.0 |  | bus |

### `woky` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xure` | 59.6 | not_x1 | ppu-control |
| `xubo` | 54.8 | not_x1 | ppu-control |
| `xare` | 27.4 | not_x1 | ppu-control |
| `bus:d6` | 0.0 |  | bus |

### `wymo` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xure` | 59.6 | not_x1 | ppu-control |
| `xubo` | 54.8 | not_x1 | ppu-control |
| `xare` | 27.4 | not_x1 | ppu-control |
| `bus:d5` | 0.0 |  | bus |

### `xafo` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xure` | 59.6 | not_x1 | ppu-control |
| `xubo` | 54.8 | not_x1 | ppu-control |
| `xare` | 27.4 | not_x1 | ppu-control |
| `bus:d3` | 0.0 |  | bus |

### `xona` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xure` | 59.6 | not_x1 | ppu-control |
| `xubo` | 54.8 | not_x1 | ppu-control |
| `xare` | 27.4 | not_x1 | ppu-control |
| `bus:d7` | 0.0 |  | bus |

### `xylo` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xure` | 59.6 | not_x1 | ppu-control |
| `xubo` | 54.8 | not_x1 | ppu-control |
| `xare` | 27.4 | not_x1 | ppu-control |
| `bus:d1` | 0.0 |  | bus |

### `xymo` (drlatch_ee) — diff=59.6 ge, max=59.6 ge | source: `bus:a10` (per-frame)
Category: ppu-control | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `xure` | 59.6 | not_x1 | ppu-control |
| `xubo` | 54.8 | not_x1 | ppu-control |
| `xare` | 27.4 | not_x1 | ppu-control |
| `bus:d2` | 0.0 |  | bus |


## BG Scrolling (16 races) — per-frame

### `bake` (drlatch_ee) — diff=59.5 ge, max=59.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bofo` | 59.5 | not_x1 | ppu-bgscroll |
| `amun` | 54.6 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d7` | 0.0 |  | bus |

### `bemy` (drlatch_ee) — diff=59.5 ge, max=59.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bofo` | 59.5 | not_x1 | ppu-bgscroll |
| `amun` | 54.6 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d4` | 0.0 |  | bus |

### `cabu` (drlatch_ee) — diff=59.5 ge, max=59.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bofo` | 59.5 | not_x1 | ppu-bgscroll |
| `amun` | 54.6 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d6` | 0.0 |  | bus |

### `cuzy` (drlatch_ee) — diff=59.5 ge, max=59.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bofo` | 59.5 | not_x1 | ppu-bgscroll |
| `amun` | 54.6 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d5` | 0.0 |  | bus |

### `cyxu` (drlatch_ee) — diff=59.5 ge, max=59.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bofo` | 59.5 | not_x1 | ppu-bgscroll |
| `amun` | 54.6 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d2` | 0.0 |  | bus |

### `daty` (drlatch_ee) — diff=59.5 ge, max=59.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bofo` | 59.5 | not_x1 | ppu-bgscroll |
| `amun` | 54.6 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d0` | 0.0 |  | bus |

### `duzu` (drlatch_ee) — diff=59.5 ge, max=59.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bofo` | 59.5 | not_x1 | ppu-bgscroll |
| `amun` | 54.6 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d1` | 0.0 |  | bus |

### `gubo` (drlatch_ee) — diff=59.5 ge, max=59.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `bofo` | 59.5 | not_x1 | ppu-bgscroll |
| `amun` | 54.6 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d3` | 0.0 |  | bus |

### `dede` (drlatch_ee) — diff=58.5 ge, max=58.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ehor` | 58.5 | not_x1 | ppu-bgscroll |
| `cavo` | 54.0 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d4` | 0.0 |  | bus |

### `fezu` (drlatch_ee) — diff=58.5 ge, max=58.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ehor` | 58.5 | not_x1 | ppu-bgscroll |
| `cavo` | 54.0 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d2` | 0.0 |  | bus |

### `foha` (drlatch_ee) — diff=58.5 ge, max=58.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ehor` | 58.5 | not_x1 | ppu-bgscroll |
| `cavo` | 54.0 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d6` | 0.0 |  | bus |

### `foty` (drlatch_ee) — diff=58.5 ge, max=58.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ehor` | 58.5 | not_x1 | ppu-bgscroll |
| `cavo` | 54.0 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d5` | 0.0 |  | bus |

### `fujo` (drlatch_ee) — diff=58.5 ge, max=58.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ehor` | 58.5 | not_x1 | ppu-bgscroll |
| `cavo` | 54.0 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d3` | 0.0 |  | bus |

### `funy` (drlatch_ee) — diff=58.5 ge, max=58.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ehor` | 58.5 | not_x1 | ppu-bgscroll |
| `cavo` | 54.0 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d7` | 0.0 |  | bus |

### `fymo` (drlatch_ee) — diff=58.5 ge, max=58.5 ge | source: `bus:a10` (per-frame)
Category: ppu-bgscroll | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ehor` | 58.5 | not_x1 | ppu-bgscroll |
| `cavo` | 54.0 | not_x1 | ppu-bgscroll |
| `cunu` | 16.5 | not_x2 | ppu-control |
| `bus:d1` | 0.0 |  | bus |


## Boot ROM (1 races) — per-frame

### `tepu` (dffr) — diff=40.3 ge, max=42.2 ge | source: `bus:a10` (per-frame)
Category: bootrom | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `tuge` | 42.2 | nand4 | bootrom |
| `alur` | 8.6 | not_x2 | clocks |
| `sato` | 1.8 | or2 | bootrom |


## Data Bus (16 races) — per-frame

### `raxy` (dlatch) — diff=38.0 ge, max=38.0 ge | source: `bus:a15` (per-frame)
Category: bus-data | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavo` | 38.0 | nand3 | bus-data |
| `d2` | 0.0 | pad_bidir_pu | bus-data |

### `rony` (dlatch) — diff=38.0 ge, max=38.0 ge | source: `bus:a15` (per-frame)
Category: bus-data | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavo` | 38.0 | nand3 | bus-data |
| `d1` | 0.0 | pad_bidir_pu | bus-data |

### `rupa` (dlatch) — diff=38.0 ge, max=38.0 ge | source: `bus:a15` (per-frame)
Category: bus-data | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavo` | 38.0 | nand3 | bus-data |
| `d6` | 0.0 | pad_bidir_pu | bus-data |

### `sago` (dlatch) — diff=38.0 ge, max=38.0 ge | source: `bus:a15` (per-frame)
Category: bus-data | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavo` | 38.0 | nand3 | bus-data |
| `d5` | 0.0 | pad_bidir_pu | bus-data |

### `sazy` (dlatch) — diff=38.0 ge, max=38.0 ge | source: `bus:a15` (per-frame)
Category: bus-data | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavo` | 38.0 | nand3 | bus-data |
| `d7` | 0.0 | pad_bidir_pu | bus-data |

### `selo` (dlatch) — diff=38.0 ge, max=38.0 ge | source: `bus:a15` (per-frame)
Category: bus-data | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavo` | 38.0 | nand3 | bus-data |
| `d3` | 0.0 | pad_bidir_pu | bus-data |

### `sody` (dlatch) — diff=38.0 ge, max=38.0 ge | source: `bus:a15` (per-frame)
Category: bus-data | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavo` | 38.0 | nand3 | bus-data |
| `d4` | 0.0 | pad_bidir_pu | bus-data |

### `soma` (dlatch) — diff=38.0 ge, max=38.0 ge | source: `bus:a15` (per-frame)
Category: bus-data | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lavo` | 38.0 | nand3 | bus-data |
| `d0` | 0.0 | pad_bidir_pu | bus-data |

### `d5` (pad_bidir_pu) — diff=11.6 ge, max=58.6 ge | source: `t1` (static)
Category: bus-data | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ryvo` | 58.6 | nand2 | bus-data |
| `lula` | 56.1 | not_x1 | bus-data |
| `tamu` | 47.1 | nor2 | bus-data |

### `d7` (pad_bidir_pu) — diff=9.5 ge, max=58.2 ge | source: `t1` (static)
Category: bus-data | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ravu` | 58.2 | nand2 | bus-data |
| `lula` | 56.1 | not_x1 | bus-data |
| `ryda` | 48.8 | nor2 | bus-data |

### `d3` (pad_bidir_pu) — diff=8.5 ge, max=60.9 ge | source: `t1` (static)
Category: bus-data | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rera` | 60.9 | nand2 | bus-data |
| `lula` | 56.1 | not_x1 | bus-data |
| `seze` | 52.5 | nor2 | bus-data |

### `d0` (pad_bidir_pu) — diff=8.4 ge, max=64.5 ge | source: `t1` (static)
Category: bus-data | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `ruxa` | 64.5 | nand2 | bus-data |
| `rune` | 61.0 | nor2 | bus-data |
| `lula` | 56.1 | not_x1 | bus-data |

### `d4` (pad_bidir_pu) — diff=8.3 ge, max=59.8 ge | source: `t1` (static)
Category: bus-data | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rory` | 59.8 | nand2 | bus-data |
| `lula` | 56.1 | not_x1 | bus-data |
| `resy` | 51.4 | nor2 | bus-data |

### `d6` (pad_bidir_pu) — diff=8.1 ge, max=59.5 ge | source: `t1` (static)
Category: bus-data | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rafy` | 59.5 | nand2 | bus-data |
| `lula` | 56.1 | not_x1 | bus-data |
| `rogy` | 51.4 | nor2 | bus-data |

### `d2` (pad_bidir_pu) — diff=7.4 ge, max=61.7 ge | source: `t1` (static)
Category: bus-data | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `raby` | 61.7 | nand2 | bus-data |
| `lula` | 56.1 | not_x1 | bus-data |
| `suly` | 54.3 | nor2 | bus-data |


## OAM Interface (3 races) — per-frame

### `xedy` (dffr_cc) — diff=5.5 ge, max=14.1 ge | source: `bus:oam_~{a3}_tri` (per-frame)
Category: ppu-oam | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `yfoc` | 14.1 | not_x1 | ppu-oam |
| `wuda` | 10.4 | not_x2 | ppu-oam |
| `cyke` | 8.6 | not_x2 | ppu-oam |

### `xecu` (dffr_cc) — diff=4.1 ge, max=12.7 ge | source: `bus:oam_~{a7}_tri` (per-frame)
Category: ppu-oam | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `yzet` | 12.7 | not_x1 | ppu-oam |
| `wuda` | 10.4 | not_x2 | ppu-oam |
| `cyke` | 8.6 | not_x2 | ppu-oam |

### `maka` (dffr) — diff=10.1 ge, max=16.5 ge | source: `afer` (static)
Category: ppu-oam | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `cunu` | 16.5 | not_x2 | ppu-control |
| `zeme` | 8.9 | not_x4 | ppu-control |
| `caty` | 6.4 | not_x1 | ppu-oam |


## VRAM Interface (7 races) — per-frame

### `md4` (pad_bidir_pu) — diff=7.5 ge, max=56.3 ge | source: `bus:a10` (per-frame)
Category: ppu-vram | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rofa` | 56.3 | not_x2 | ppu-vram |
| `ryro` | 53.8 | not_x2 | ppu-vram |
| `rube` | 48.8 | not_x2 | ppu-vram |

### `md6` (pad_bidir_pu) — diff=7.5 ge, max=56.3 ge | source: `bus:a10` (per-frame)
Category: ppu-vram | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rofa` | 56.3 | not_x2 | ppu-vram |
| `reku` | 51.5 | not_x2 | ppu-vram |
| `ryty` | 48.8 | not_x2 | ppu-vram |

### `md5` (pad_bidir_pu) — diff=7.0 ge, max=56.3 ge | source: `bus:a10` (per-frame)
Category: ppu-vram | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rofa` | 56.3 | not_x2 | ppu-vram |
| `revu` | 52.6 | not_x2 | ppu-vram |
| `rumu` | 49.3 | not_x2 | ppu-vram |

### `md3` (pad_bidir_pu) — diff=6.9 ge, max=56.3 ge | source: `bus:a10` (per-frame)
Category: ppu-vram | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rofa` | 56.3 | not_x2 | ppu-vram |
| `rada` | 52.4 | not_x2 | ppu-vram |
| `rodu` | 49.5 | not_x2 | ppu-vram |

### `md7` (pad_bidir_pu) — diff=6.8 ge, max=56.3 ge | source: `bus:a10` (per-frame)
Category: ppu-vram | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rofa` | 56.3 | not_x2 | ppu-vram |
| `ryze` | 51.1 | not_x2 | ppu-vram |
| `rady` | 49.6 | not_x2 | ppu-vram |

### `md2` (pad_bidir_pu) — diff=6.5 ge, max=56.3 ge | source: `bus:a10` (per-frame)
Category: ppu-vram | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rofa` | 56.3 | not_x2 | ppu-vram |
| `razo` | 53.0 | not_x2 | ppu-vram |
| `rare` | 49.8 | not_x2 | ppu-vram |

### `md1` (pad_bidir_pu) — diff=4.9 ge, max=56.3 ge | source: `bus:a10` (per-frame)
Category: ppu-vram | Effective: per-frame

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `rofa` | 56.3 | not_x2 | ppu-vram |
| `ryky` | 53.9 | not_x2 | ppu-vram |
| `ruly` | 51.4 | not_x2 | ppu-vram |


## Test Mode (8 races) — static

### `jale` (dffr) — diff=70.1 ge, max=70.1 ge | source: `bus:a10` (per-frame)
Category: test | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `atoz` | 70.1 | nand4 | joypad |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d2` | 0.0 |  | bus |

### `jute` (dffr) — diff=70.1 ge, max=70.1 ge | source: `bus:a10` (per-frame)
Category: test | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `atoz` | 70.1 | nand4 | joypad |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d0` | 0.0 |  | bus |

### `kecy` (dffr) — diff=70.1 ge, max=70.1 ge | source: `bus:a10` (per-frame)
Category: test | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `atoz` | 70.1 | nand4 | joypad |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d1` | 0.0 |  | bus |

### `keru` (dffr) — diff=70.1 ge, max=70.1 ge | source: `bus:a10` (per-frame)
Category: test | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `atoz` | 70.1 | nand4 | joypad |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d7` | 0.0 |  | bus |

### `kuko` (dffr) — diff=70.1 ge, max=70.1 ge | source: `bus:a10` (per-frame)
Category: test | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `atoz` | 70.1 | nand4 | joypad |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d6` | 0.0 |  | bus |

### `kyme` (dffr) — diff=70.1 ge, max=70.1 ge | source: `bus:a10` (per-frame)
Category: test | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `atoz` | 70.1 | nand4 | joypad |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d3` | 0.0 |  | bus |

### `amut` (dffr) — diff=48.5 ge, max=48.5 ge | source: `bus:a10` (per-frame)
Category: test | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `aper` | 48.5 | nand5 | test |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d1` | 0.0 |  | bus |

### `buro` (dffr) — diff=48.5 ge, max=48.5 ge | source: `bus:a10` (per-frame)
Category: test | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `aper` | 48.5 | nand5 | test |
| `alur` | 8.6 | not_x2 | clocks |
| `bus:d0` | 0.0 |  | bus |


## Sprite X Priority (10 races) — static

### `cedy` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `enut` | 31.2 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `eboj` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `guva` | 34.2 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `egav` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `emol` | 32.0 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `exuq` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `foxa` | 44.6 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `fono` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `guze` | 52.4 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `gota` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `gyfy` | 34.7 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `wafy` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `gega` | 37.0 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `wapo` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `gutu` | 41.8 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `womy` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `xoja` | 40.2 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |

### `xudy` (dffr) — diff=48.7 ge, max=58.4 ge | source: `afer` (static)
Category: ppu-xprio | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `byva` | 58.4 | not_x1 | ppu-xprio |
| `gono` | 41.1 | nor2 | ppu-xprio |
| `wuty` | 9.7 | not_x2 | ppu-ycomp |


## LCD Output (18 races) — static

### `sude` (dffr) — diff=47.4 ge, max=47.4 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mude` | 47.4 | nor2 | ppu-lcd |
| `telu` | 0.0 | dffr | ppu-lcd |

### `taha` (dffr) — diff=47.4 ge, max=47.4 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mude` | 47.4 | nor2 | ppu-lcd |
| `sude` | 0.0 | dffr | ppu-lcd |

### `telu` (dffr) — diff=47.4 ge, max=47.4 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mude` | 47.4 | nor2 | ppu-lcd |
| `vyzo` | 0.0 | dffr | ppu-lcd |

### `typo` (dffr) — diff=47.4 ge, max=47.4 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mude` | 47.4 | nor2 | ppu-lcd |
| `saxo` | 0.0 | dffr | ppu-lcd |

### `tyry` (dffr) — diff=47.4 ge, max=47.4 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mude` | 47.4 | nor2 | ppu-lcd |
| `taha` | 0.0 | dffr | ppu-lcd |

### `vyzo` (dffr) — diff=47.4 ge, max=47.4 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mude` | 47.4 | nor2 | ppu-lcd |
| `typo` | 0.0 | dffr | ppu-lcd |

### `saxo` (dffr) — diff=46.0 ge, max=47.4 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `mude` | 47.4 | nor2 | ppu-lcd |
| `talu` | 1.4 | not_x4 | ppu-lcd |

### `meda` (dffr) — diff=43.7 ge, max=43.7 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfe` | 43.7 | not_x1 | ppu-lcd |
| `neru` | 8.2 | nor8 | ppu-lcd |
| `nype` | 0.0 | dffr | ppu-lcd |

### `myta` (dffr) — diff=43.7 ge, max=43.7 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfe` | 43.7 | not_x1 | ppu-lcd |
| `noko` | 2.5 | and4 | ppu-lcd |
| `nype` | 0.0 | dffr | ppu-lcd |

### `napo` (dffr) — diff=43.7 ge, max=43.7 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfe` | 43.7 | not_x1 | ppu-lcd |
| `popu` | 0.0 | dffr | ppu-lcd |

### `nype` (dffr) — diff=43.7 ge, max=43.7 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfe` | 43.7 | not_x1 | ppu-lcd |
| `talu` | 1.4 | not_x4 | ppu-lcd |
| `rutu` | 0.0 | dffr | ppu-lcd |

### `popu` (dffr) — diff=43.7 ge, max=43.7 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfe` | 43.7 | not_x1 | ppu-lcd |
| `xyvo` | 8.4 | and2 | ppu-lcd |
| `nype` | 0.0 | dffr | ppu-lcd |

### `luca` (dffr) — diff=43.5 ge, max=43.7 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfe` | 43.7 | not_x1 | ppu-lcd |
| `lofu` | 0.2 | not_x1 | ppu-lcd |

### `rutu` (dffr) — diff=41.3 ge, max=43.7 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfe` | 43.7 | not_x1 | ppu-lcd |
| `sanu` | 3.2 | and4 | ppu-lcd |
| `sono` | 2.4 | not_x1 | ppu-lcd |

### `sygu` (dffr) — diff=41.3 ge, max=43.7 ge | source: `afer` (static)
Category: ppu-lcd | Effective: static

| Input | Depth (ge) | Type | Category |
|-------|-----------|------|----------|
| `lyfe` | 43.7 | not_x1 | ppu-lcd |
| `tegy` | 7.9 | nand4 | ppu-lcd |
| `sono` | 2.4 | not_x1 | ppu-lcd |
