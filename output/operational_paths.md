# Operational Critical Paths by Functional Area


## bus (263 paths, max depth 32)

### Path 1: depth 32 (160-480 ns, 403% half T-cycle)
```
[REGISTERED:dffr] muwy (ppu-stat)
  [half_add] fafo (ppu-bgscroll)
    [full_add] emux (ppu-bgscroll)
      [full_add] ecab (ppu-bgscroll)
        [full_add] etam (ppu-bgscroll)
          [full_add] doto (ppu-bgscroll)
            [full_add] daba (ppu-bgscroll)
              [full_add] efyk (ppu-bgscroll)
                [full_add] ejok (ppu-bgscroll)
                  [not_if0] dafe (ppu-bgscroll)
                    [BUS:] bus:~ma9 (bus)
```

### Path 2: depth 32 (160-480 ns, 403% half T-cycle)
```
[REGISTERED:dffr] xeho (ppu-stat)
  [half_add] atad (ppu-bgscroll)
    [full_add] behu (ppu-bgscroll)
      [full_add] apyh (ppu-bgscroll)
        [full_add] babe (ppu-bgscroll)
          [full_add] abod (ppu-bgscroll)
            [full_add] bewy (ppu-bgscroll)
              [full_add] byca (ppu-bgscroll)
                [full_add] acul (ppu-bgscroll)
                  [not_if0] ajan (ppu-bgscroll)
                    [BUS:] bus:~ma4 (bus)
```

### Path 3: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dffr] muwy (ppu-stat)
  [half_add] fafo (ppu-bgscroll)
    [full_add] emux (ppu-bgscroll)
      [full_add] ecab (ppu-bgscroll)
        [full_add] etam (ppu-bgscroll)
          [full_add] doto (ppu-bgscroll)
            [full_add] daba (ppu-bgscroll)
              [full_add] efyk (ppu-bgscroll)
                [not_if0] ceta (ppu-bgscroll)
                  [BUS:] bus:~ma8 (bus)
```

### Path 4: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dffr] xeho (ppu-stat)
  [half_add] atad (ppu-bgscroll)
    [full_add] behu (ppu-bgscroll)
      [full_add] apyh (ppu-bgscroll)
        [full_add] babe (ppu-bgscroll)
          [full_add] abod (ppu-bgscroll)
            [full_add] bewy (ppu-bgscroll)
              [full_add] byca (ppu-bgscroll)
                [not_if0] coly (ppu-bgscroll)
                  [BUS:] bus:~ma3 (bus)
```

### Path 5: depth 24 (120-360 ns, 302% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [buf_if0] tofa (ppu-vram)
                                [BUS:] bus:md6 (bus)
```

### Path 6: depth 24 (120-360 ns, 302% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [buf_if0] sote (ppu-vram)
                                [BUS:] bus:md3 (bus)
```

### Path 7: depth 24 (120-360 ns, 302% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [buf_if0] rujo (ppu-vram)
                                [BUS:] bus:md5 (bus)
```

### Path 8: depth 24 (120-360 ns, 302% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [buf_if0] teme (ppu-vram)
                                [BUS:] bus:md0 (bus)
```

### Path 9: depth 24 (120-360 ns, 302% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [buf_if0] suza (ppu-vram)
                                [BUS:] bus:md7 (bus)
```

### Path 10: depth 24 (120-360 ns, 302% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [buf_if0] tewu (ppu-vram)
                                [BUS:] bus:md1 (bus)
```


## Sprite Store (200 paths, max depth 28)

### Path 1: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] enob (ppu-objctl)
                          [not_x1] doby (ppu-objctl)
                            [REGISTERED:dlatch_ee] bozu (ppu-objreg)
```

### Path 2: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] enob (ppu-objctl)
                          [not_x1] doby (ppu-objctl)
                            [REGISTERED:dlatch_ee] fyhy (ppu-objreg)
```

### Path 3: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] enob (ppu-objctl)
                          [not_x1] doby (ppu-objctl)
                            [REGISTERED:dlatch_ee] cufo (ppu-objreg)
```

### Path 4: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] enob (ppu-objctl)
                          [not_x1] doby (ppu-objctl)
                            [REGISTERED:dlatch_ee] gyho (ppu-objreg)
```

### Path 5: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] geny (ppu-objctl)
                          [not_x1] xuxa (ppu-objctl)
                            [REGISTERED:dlatch_ee] ywak (ppu-objreg)
```

### Path 6: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] geny (ppu-objctl)
                          [not_x1] xuxa (ppu-objctl)
                            [REGISTERED:dlatch_ee] ygus (ppu-objreg)
```

### Path 7: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] caho (ppu-objctl)
                      [not_x1] buka (ppu-objctl)
                        [not_x1] bymy (ppu-objctl)
                          [not_x1] byno (ppu-objctl)
                            [REGISTERED:dlatch_ee] azap (ppu-objreg)
```

### Path 8: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] caho (ppu-objctl)
                      [not_x1] buka (ppu-objctl)
                        [not_x1] bymy (ppu-objctl)
                          [not_x1] byno (ppu-objctl)
                            [REGISTERED:dlatch_ee] afyx (ppu-objreg)
```

### Path 9: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] caho (ppu-objctl)
                      [not_x1] buka (ppu-objctl)
                        [not_x1] bymy (ppu-objctl)
                          [not_x1] byno (ppu-objctl)
                            [REGISTERED:dlatch_ee] afym (ppu-objreg)
```

### Path 10: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] caho (ppu-objctl)
                      [not_x1] buka (ppu-objctl)
                        [not_x1] bymy (ppu-objctl)
                          [not_x1] byno (ppu-objctl)
                            [REGISTERED:dlatch_ee] afut (ppu-objreg)
```


## Sprite X Match (268 paths, max depth 28)

### Path 1: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] fuxu (ppu-objctl)
                          [not_x1] gery (ppu-objctl)
                            [REGISTERED:drlatch_ee] welo (ppu-xcomp)
```

### Path 2: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] fuxu (ppu-objctl)
                          [not_x1] gery (ppu-objctl)
                            [REGISTERED:drlatch_ee] xuny (ppu-xcomp)
```

### Path 3: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cato (ppu-objctl)
                      [not_x1] decu (ppu-objctl)
                        [not_x1] weme (ppu-objctl)
                          [not_x1] wyxa (ppu-objctl)
                            [REGISTERED:drlatch_ee] yrop (ppu-xcomp)
```

### Path 4: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] fuxu (ppu-objctl)
                          [not_x1] gery (ppu-objctl)
                            [REGISTERED:drlatch_ee] xako (ppu-xcomp)
```

### Path 5: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cato (ppu-objctl)
                      [not_x1] decu (ppu-objctl)
                        [not_x1] weme (ppu-objctl)
                          [not_x1] wyxa (ppu-objctl)
                            [REGISTERED:drlatch_ee] yzof (ppu-xcomp)
```

### Path 6: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cato (ppu-objctl)
                      [not_x1] decu (ppu-objctl)
                        [not_x1] weme (ppu-objctl)
                          [not_x1] wyxa (ppu-objctl)
                            [REGISTERED:drlatch_ee] ynep (ppu-xcomp)
```

### Path 7: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] fuxu (ppu-objctl)
                          [not_x1] gery (ppu-objctl)
                            [REGISTERED:drlatch_ee] wote (ppu-xcomp)
```

### Path 8: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cato (ppu-objctl)
                      [not_x1] decu (ppu-objctl)
                        [not_x1] weme (ppu-objctl)
                          [not_x1] wyxa (ppu-objctl)
                            [REGISTERED:drlatch_ee] xuzo (ppu-xcomp)
```

### Path 9: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cemy (ppu-objctl)
                      [not_x1] dyhu (ppu-objctl)
                        [not_x1] fuxu (ppu-objctl)
                          [not_x1] gery (ppu-objctl)
                            [REGISTERED:drlatch_ee] zola (ppu-xcomp)
```

### Path 10: depth 28 (140-420 ns, 352% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [or2] cato (ppu-objctl)
                      [not_x1] decu (ppu-objctl)
                        [not_x1] weme (ppu-objctl)
                          [not_x1] wyxa (ppu-objctl)
                            [REGISTERED:drlatch_ee] xexa (ppu-xcomp)
```


## VRAM Interface (34 paths, max depth 26)

### Path 1: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [not_x1] rove (ppu-vram)
                                [and2] sogo (ppu-vram)
                                  [not_x2] ryky (ppu-vram) x2
                                    [PAD:pad_bidir_pu] md1 (ppu-vram)
```

### Path 2: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [not_x1] rove (ppu-vram)
                                [and2] sefu (ppu-vram)
                                  [not_x2] razo (ppu-vram) x2
                                    [PAD:pad_bidir_pu] md2 (ppu-vram)
```

### Path 3: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [not_x1] rove (ppu-vram)
                                [and2] sumo (ppu-vram)
                                  [not_x2] ryro (ppu-vram) x2
                                    [PAD:pad_bidir_pu] md4 (ppu-vram)
```

### Path 4: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [not_x1] rove (ppu-vram)
                                [and2] samo (ppu-vram)
                                  [not_x2] reku (ppu-vram) x2
                                    [PAD:pad_bidir_pu] md6 (ppu-vram)
```

### Path 5: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [not_x1] rove (ppu-vram)
                                [and2] suna (ppu-vram)
                                  [not_x2] rada (ppu-vram) x2
                                    [PAD:pad_bidir_pu] md3 (ppu-vram)
```

### Path 6: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [not_x1] rove (ppu-vram)
                                [and2] sazu (ppu-vram)
                                  [not_x2] revu (ppu-vram) x2
                                    [PAD:pad_bidir_pu] md5 (ppu-vram)
```

### Path 7: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [not_x1] rove (ppu-vram)
                                [and2] sefa (ppu-vram)
                                  [not_x2] rege (ppu-vram) x2
                                    [PAD:pad_bidir_pu] md0 (ppu-vram)
```

### Path 8: depth 25 (125-375 ns, 315% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [or2] sawu (ppu-vram)
                                [not_x2] rady (ppu-vram) x2
                                  [PAD:pad_bidir_pu] md7 (ppu-vram)
```

### Path 9: depth 25 (125-375 ns, 315% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [or2] sedo (ppu-vram)
                                [not_x2] ryty (ppu-vram) x2
                                  [PAD:pad_bidir_pu] md6 (ppu-vram)
```

### Path 10: depth 25 (125-375 ns, 315% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [and2] tuca (ppu-vram)
                [mux] tole (ppu-vram)
                  [and2] sere (ppu-vram)
                    [and2] sazo (ppu-vram)
                      [not_x1] ryje (ppu-vram)
                        [not_x1] revo (ppu-vram)
                          [and2] rocy (ppu-vram)
                            [not_x3] rahu (ppu-vram) x3 fan-out=17
                              [or2] sybu (ppu-vram)
                                [not_x2] rodu (ppu-vram) x2
                                  [PAD:pad_bidir_pu] md3 (ppu-vram)
```


## Sprite X Priority (19 paths, max depth 24)

### Path 1: depth 24 (120-360 ns, 302% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [not_x1] wefu (ppu-xprio)
            [or2] geze (ppu-xprio)
              [or2] fuma (ppu-xprio)
                [or2] gede (ppu-xprio)
                  [or2] wuto (ppu-xprio)
                    [or2] xyla (ppu-xprio)
                      [or2] weja (ppu-xprio)
                        [or2] wyla (ppu-xprio)
                          [or2] favo (ppu-xprio)
                            [nor2] foxa (ppu-xprio)
                              [REGISTERED:dffr] exuq (ppu-xprio)
```

### Path 2: depth 22 (110-330 ns, 277% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [not_x1] wefu (ppu-xprio)
            [or2] geze (ppu-xprio)
              [or2] fuma (ppu-xprio)
                [or2] gede (ppu-xprio)
                  [or2] wuto (ppu-xprio)
                    [or2] xyla (ppu-xprio)
                      [or2] weja (ppu-xprio)
                        [or2] wyla (ppu-xprio)
                          [nor2] gutu (ppu-xprio)
                            [REGISTERED:dffr] wapo (ppu-xprio)
```

### Path 3: depth 20 (100-300 ns, 252% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [not_x1] wefu (ppu-xprio)
            [or2] geze (ppu-xprio)
              [or2] fuma (ppu-xprio)
                [or2] gede (ppu-xprio)
                  [or2] wuto (ppu-xprio)
                    [or2] xyla (ppu-xprio)
                      [or2] weja (ppu-xprio)
                        [nor2] xoja (ppu-xprio)
                          [REGISTERED:dffr] womy (ppu-xprio)
```

### Path 4: depth 18 (90-270 ns, 227% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [not_x1] wefu (ppu-xprio)
            [or2] geze (ppu-xprio)
              [or2] fuma (ppu-xprio)
                [or2] gede (ppu-xprio)
                  [or2] wuto (ppu-xprio)
                    [or2] xyla (ppu-xprio)
                      [nor2] gega (ppu-xprio)
                        [REGISTERED:dffr] wafy (ppu-xprio)
```

### Path 5: depth 16 (80-240 ns, 201% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [not_x1] wefu (ppu-xprio)
            [or2] geze (ppu-xprio)
              [or2] fuma (ppu-xprio)
                [or2] gede (ppu-xprio)
                  [or2] wuto (ppu-xprio)
                    [nor2] gono (ppu-xprio)
                      [REGISTERED:dffr] xudy (ppu-xprio)
```

### Path 6: depth 14 (70-210 ns, 176% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [not_x1] wefu (ppu-xprio)
            [or2] geze (ppu-xprio)
              [or2] fuma (ppu-xprio)
                [or2] gede (ppu-xprio)
                  [nor2] gyfy (ppu-xprio)
                    [REGISTERED:dffr] gota (ppu-xprio)
```

### Path 7: depth 12 (60-180 ns, 151% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [not_x1] wefu (ppu-xprio)
            [or2] geze (ppu-xprio)
              [or2] fuma (ppu-xprio)
                [nor2] emol (ppu-xprio)
                  [REGISTERED:dffr] egav (ppu-xprio)
```

### Path 8: depth 10 (50-150 ns, 126% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [not_x1] wefu (ppu-xprio)
            [or2] geze (ppu-xprio)
              [nor2] enut (ppu-xprio)
                [REGISTERED:dffr] cedy (ppu-xprio)
```

### Path 9: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [nor2] guva (ppu-xprio)
            [REGISTERED:dffr] eboj (ppu-xprio)
```

### Path 10: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] toxe (ppu-ycomp)
  [nand3] tyno (ppu-ycomp)
    [or2] vusa (ppu-ycomp)
      [not_x2] wuty (ppu-ycomp) x2 fan-out=12
        [REGISTERED:dffr] fono (ppu-xprio)
```


## Sprite Control (9 paths, max depth 23)

### Path 1: depth 23 (115-345 ns, 289% half T-cycle)
```
[REGISTERED:dlatch_ee] xuso (ppu-ycomp)
  [full_add] eruc (ppu-ycomp)
    [full_add] enef (ppu-ycomp)
      [full_add] feco (ppu-ycomp)
        [full_add] gyky (ppu-ycomp)
          [or2] govu (ppu-ycomp)
            [nand6] wota (ppu-ycomp)
              [not_x1] gese (ppu-ycomp)
                [and3] care (ppu-objctl)
                  [not_x2] dyty (ppu-objctl) x2 fan-out=11
                    [REGISTERED:dffr] dezy (ppu-objctl)
```

### Path 2: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] lovu (ppu-stat)
  [and2] xyvo (ppu-lcd)
    [not_x1] ales (ppu-objctl)
      [and2] abov (ppu-objctl)
        [REGISTERED:dffr] catu (ppu-objctl)
```

### Path 3: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] dybe (ppu-objctl)
  [and2] baky (ppu-objctl)
    [or2] cake (ppu-objctl)
      [REGISTERED:dffr] bese (ppu-objctl)
```

### Path 4: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] fony (ppu-objctl)
  [and4] feto (ppu-objctl)
    [or2] gava (ppu-objctl)
      [REGISTERED:dffr] yfel (ppu-objctl)
```

### Path 5: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x1] awoh (ppu-objctl)
      [REGISTERED:dffr] anel (ppu-objctl)
```

### Path 6: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] fony (ppu-objctl)
  [and4] feto (ppu-objctl)
    [REGISTERED:dffr] byba (ppu-objctl)
```

### Path 7: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [REGISTERED:dffr] catu (ppu-objctl)
```

### Path 8: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [REGISTERED:dffr] byba (ppu-objctl)
```

### Path 9: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [REGISTERED:dffr] ceno (ppu-objctl)
```


## Data Bus (24 paths, max depth 17)

### Path 1: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [not_x1] lula (bus-data) fan-out=16
                      [nand2] raby (bus-data)
                        [PAD:pad_bidir_pu] d2 (bus-data)
```

### Path 2: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [not_x1] lula (bus-data) fan-out=16
                      [nand2] rory (bus-data)
                        [PAD:pad_bidir_pu] d4 (bus-data)
```

### Path 3: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [not_x1] lula (bus-data) fan-out=16
                      [nand2] ruja (bus-data)
                        [PAD:pad_bidir_pu] d1 (bus-data)
```

### Path 4: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [not_x1] lula (bus-data) fan-out=16
                      [nand2] ruxa (bus-data)
                        [PAD:pad_bidir_pu] d0 (bus-data)
```

### Path 5: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [not_x1] lula (bus-data) fan-out=16
                      [nand2] rafy (bus-data)
                        [PAD:pad_bidir_pu] d6 (bus-data)
```

### Path 6: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [not_x1] lula (bus-data) fan-out=16
                      [nand2] ryvo (bus-data)
                        [PAD:pad_bidir_pu] d5 (bus-data)
```

### Path 7: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [not_x1] lula (bus-data) fan-out=16
                      [nand2] ravu (bus-data)
                        [PAD:pad_bidir_pu] d7 (bus-data)
```

### Path 8: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [not_x1] lula (bus-data) fan-out=16
                      [nand2] rera (bus-data)
                        [PAD:pad_bidir_pu] d3 (bus-data)
```

### Path 9: depth 16 (80-240 ns, 201% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [nor2] suly (bus-data)
                      [PAD:pad_bidir_pu] d2 (bus-data)
```

### Path 10: depth 16 (80-240 ns, 201% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [not_x1] levo (bus-data)
            [ao21] lagu (bus-data)
              [not_x1] lywe (bus-data)
                [or2] moty (bus-data)
                  [mux] roru (bus-adr) fan-out=10
                    [nor2] resy (bus-data)
                      [PAD:pad_bidir_pu] d4 (bus-data)
```


## DMA (18 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [not_x1] pysu (ppu-dma)
                          [REGISTERED:dlatch_ee] nygy (ppu-dma)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [not_x1] pysu (ppu-dma)
                          [REGISTERED:dlatch_ee] nydo (ppu-dma)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [not_x1] pysu (ppu-dma)
                          [REGISTERED:dlatch_ee] nafa (ppu-dma)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [not_x1] pysu (ppu-dma)
                          [REGISTERED:dlatch_ee] pyne (ppu-dma)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [not_x1] pysu (ppu-dma)
                          [REGISTERED:dlatch_ee] para (ppu-dma)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [not_x1] pysu (ppu-dma)
                          [REGISTERED:dlatch_ee] maru (ppu-dma)
```

### Path 7: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [REGISTERED:dlatch_ee] nygy (ppu-dma)
```

### Path 8: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [REGISTERED:dlatch_ee] nydo (ppu-dma)
```

### Path 9: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [REGISTERED:dlatch_ee] nafa (ppu-dma)
```

### Path 10: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] lavy (ppu-dma)
                      [not_x1] loru (ppu-dma)
                        [REGISTERED:dlatch_ee] pyne (ppu-dma)
```


## STAT/LY (33 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] sepa (ppu-stat)
                      [not_x1] ryve (ppu-stat)
                        [not_x1] pupu (ppu-stat)
                          [REGISTERED:drlatch_ee] refe (ppu-stat)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] sepa (ppu-stat)
                      [not_x1] ryve (ppu-stat)
                        [not_x1] pupu (ppu-stat)
                          [REGISTERED:drlatch_ee] roxe (ppu-stat)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] sepa (ppu-stat)
                      [not_x1] ryve (ppu-stat)
                        [not_x1] pupu (ppu-stat)
                          [REGISTERED:drlatch_ee] rugu (ppu-stat)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] sepa (ppu-stat)
                      [not_x1] ryve (ppu-stat)
                        [not_x1] pupu (ppu-stat)
                          [REGISTERED:drlatch_ee] rufo (ppu-stat)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] xufa (ppu-stat)
                      [not_x1] wane (ppu-stat)
                        [not_x1] voze (ppu-stat)
                          [REGISTERED:drlatch_ee] sedy (ppu-stat)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] xufa (ppu-stat)
                      [not_x1] wane (ppu-stat)
                        [not_x1] voze (ppu-stat)
                          [REGISTERED:drlatch_ee] sota (ppu-stat)
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] xufa (ppu-stat)
                      [not_x1] wane (ppu-stat)
                        [not_x1] voze (ppu-stat)
                          [REGISTERED:drlatch_ee] vuce (ppu-stat)
```

### Path 8: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] xufa (ppu-stat)
                      [not_x1] wane (ppu-stat)
                        [not_x1] voze (ppu-stat)
                          [REGISTERED:drlatch_ee] vevo (ppu-stat)
```

### Path 9: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] xufa (ppu-stat)
                      [not_x1] wane (ppu-stat)
                        [not_x1] voze (ppu-stat)
                          [REGISTERED:drlatch_ee] raha (ppu-stat)
```

### Path 10: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] xufa (ppu-stat)
                      [not_x1] wane (ppu-stat)
                        [not_x1] voze (ppu-stat)
                          [REGISTERED:drlatch_ee] syry (ppu-stat)
```


## PPU Control (16 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [not_x1] xure (ppu-control)
                          [REGISTERED:drlatch_ee] xylo (ppu-control)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [not_x1] xure (ppu-control)
                          [REGISTERED:drlatch_ee] xafo (ppu-control)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [not_x1] xure (ppu-control)
                          [REGISTERED:drlatch_ee] wymo (ppu-control)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [not_x1] xure (ppu-control)
                          [REGISTERED:drlatch_ee] xona (ppu-control)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [not_x1] xure (ppu-control)
                          [REGISTERED:drlatch_ee] xymo (ppu-control)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [not_x1] xure (ppu-control)
                          [REGISTERED:drlatch_ee] woky (ppu-control)
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [not_x1] xure (ppu-control)
                          [REGISTERED:drlatch_ee] vyxe (ppu-control)
```

### Path 8: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [not_x1] xure (ppu-control)
                          [REGISTERED:drlatch_ee] wexu (ppu-control)
```

### Path 9: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [REGISTERED:drlatch_ee] xylo (ppu-control)
```

### Path 10: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] waru (ppu-control)
                      [not_x1] xubo (ppu-control)
                        [REGISTERED:drlatch_ee] xafo (ppu-control)
```


## BG Scrolling (32 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] arur (ppu-bgscroll)
                      [not_x1] amun (ppu-bgscroll)
                        [not_x1] bofo (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] bake (ppu-bgscroll)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] arur (ppu-bgscroll)
                      [not_x1] amun (ppu-bgscroll)
                        [not_x1] bofo (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] duzu (ppu-bgscroll)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] arur (ppu-bgscroll)
                      [not_x1] amun (ppu-bgscroll)
                        [not_x1] bofo (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] cyxu (ppu-bgscroll)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] arur (ppu-bgscroll)
                      [not_x1] amun (ppu-bgscroll)
                        [not_x1] bofo (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] bemy (ppu-bgscroll)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] arur (ppu-bgscroll)
                      [not_x1] amun (ppu-bgscroll)
                        [not_x1] bofo (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] cuzy (ppu-bgscroll)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] arur (ppu-bgscroll)
                      [not_x1] amun (ppu-bgscroll)
                        [not_x1] bofo (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] cabu (ppu-bgscroll)
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] arur (ppu-bgscroll)
                      [not_x1] amun (ppu-bgscroll)
                        [not_x1] bofo (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] daty (ppu-bgscroll)
```

### Path 8: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] arur (ppu-bgscroll)
                      [not_x1] amun (ppu-bgscroll)
                        [not_x1] bofo (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] gubo (ppu-bgscroll)
```

### Path 9: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] bedy (ppu-bgscroll)
                      [not_x1] cavo (ppu-bgscroll)
                        [not_x1] ehor (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] gave (ppu-bgscroll)
```

### Path 10: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] bedy (ppu-bgscroll)
                      [not_x1] cavo (ppu-bgscroll)
                        [not_x1] ehor (ppu-bgscroll)
                          [REGISTERED:drlatch_ee] fymo (ppu-bgscroll)
```


## Palettes (48 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] vely (ppu-pal)
                      [not_x1] tepo (ppu-pal)
                        [not_x1] lyfa (ppu-pal)
                          [REGISTERED:dlatch_ee] moru (ppu-pal)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] vely (ppu-pal)
                      [not_x1] tepo (ppu-pal)
                        [not_x1] lyfa (ppu-pal)
                          [REGISTERED:dlatch_ee] muke (ppu-pal)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] vely (ppu-pal)
                      [not_x1] tepo (ppu-pal)
                        [not_x1] lyfa (ppu-pal)
                          [REGISTERED:dlatch_ee] nusy (ppu-pal)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] vely (ppu-pal)
                      [not_x1] tepo (ppu-pal)
                        [not_x1] lyfa (ppu-pal)
                          [REGISTERED:dlatch_ee] pylu (ppu-pal)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] vely (ppu-pal)
                      [not_x1] tepo (ppu-pal)
                        [not_x1] lyfa (ppu-pal)
                          [REGISTERED:dlatch_ee] mogy (ppu-pal)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] vely (ppu-pal)
                      [not_x1] tepo (ppu-pal)
                        [not_x1] lyfa (ppu-pal)
                          [REGISTERED:dlatch_ee] pavo (ppu-pal)
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] vely (ppu-pal)
                      [not_x1] tepo (ppu-pal)
                        [not_x1] lyfa (ppu-pal)
                          [REGISTERED:dlatch_ee] maxy (ppu-pal)
```

### Path 8: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] vely (ppu-pal)
                      [not_x1] tepo (ppu-pal)
                        [not_x1] lyfa (ppu-pal)
                          [REGISTERED:dlatch_ee] mena (ppu-pal)
```

### Path 9: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] myxe (ppu-pal)
                      [not_x1] leho (ppu-pal)
                        [not_x1] luxu (ppu-pal)
                          [REGISTERED:dlatch_ee] luxo (ppu-pal)
```

### Path 10: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] myxe (ppu-pal)
                      [not_x1] leho (ppu-pal)
                        [not_x1] luxu (ppu-pal)
                          [REGISTERED:dlatch_ee] lawo (ppu-pal)
```


## Window Logic (33 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] wuza (ppu-window)
                      [not_x1] voxu (ppu-window)
                        [not_x1] mare (ppu-window)
                          [REGISTERED:drlatch_ee] meby (ppu-window)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] wuza (ppu-window)
                      [not_x1] voxu (ppu-window)
                        [not_x1] mare (ppu-window)
                          [REGISTERED:drlatch_ee] mypu (ppu-window)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] wuza (ppu-window)
                      [not_x1] voxu (ppu-window)
                        [not_x1] mare (ppu-window)
                          [REGISTERED:drlatch_ee] nofe (ppu-window)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] wuza (ppu-window)
                      [not_x1] voxu (ppu-window)
                        [not_x1] mare (ppu-window)
                          [REGISTERED:drlatch_ee] noke (ppu-window)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] wuza (ppu-window)
                      [not_x1] voxu (ppu-window)
                        [not_x1] mare (ppu-window)
                          [REGISTERED:drlatch_ee] myce (ppu-window)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] wuza (ppu-window)
                      [not_x1] voxu (ppu-window)
                        [not_x1] mare (ppu-window)
                          [REGISTERED:drlatch_ee] mypa (ppu-window)
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] wuza (ppu-window)
                      [not_x1] voxu (ppu-window)
                        [not_x1] mare (ppu-window)
                          [REGISTERED:drlatch_ee] muvo (ppu-window)
```

### Path 8: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] weko (ppu-window)
                      [not_x1] vefu (ppu-window)
                        [not_x1] nuta (ppu-window)
                          [REGISTERED:drlatch_ee] mela (ppu-window)
```

### Path 9: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] weko (ppu-window)
                      [not_x1] vefu (ppu-window)
                        [not_x1] nuta (ppu-window)
                          [REGISTERED:drlatch_ee] nuka (ppu-window)
```

### Path 10: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x2] dyky (ppu-control) x2
                  [not_x4] cupa (ppu-control) x4 fan-out=13
                    [and2] weko (ppu-window)
                      [not_x1] vefu (ppu-window)
                        [not_x1] nuta (ppu-window)
                          [REGISTERED:drlatch_ee] nene (ppu-window)
```


## test (16 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand2] atef (hram)
                  [not_x2] apuh (hram) x2
                    [nor3] azug (hram)
                      [not_x2] abev (hram) x2
                        [nand2] wopo (hram)
                          [not_x2] wuly (hram) x2
                            [BOUNDARY:high_ram] high_ram ()
```

### Path 2: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand2] atef (hram)
                  [not_x2] apuh (hram) x2
                    [nor3] azug (hram)
                      [not_x2] abev (hram) x2
                        [BOUNDARY:high_ram] high_ram ()
```

### Path 3: depth 12 (60-180 ns, 151% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [and3] yula (bootrom)
              [nand2] zado (bootrom)
                [not_x1] zery (bootrom)
                  [not_x1] zoku (bootrom)
                    [BOUNDARY:boot_rom] boot_rom ()
```

### Path 4: depth 11 (55-165 ns, 138% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [and3] yula (bootrom)
              [nand2] zado (bootrom)
                [not_x1] zery (bootrom)
                  [BOUNDARY:boot_rom] boot_rom ()
```

### Path 5: depth 11 (55-165 ns, 138% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand2] atef (hram)
                  [not_x2] apuh (hram) x2
                    [BOUNDARY:high_ram] high_ram ()
```

### Path 6: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand5] aper (test)
                  [REGISTERED:dffr] amut (test)
```

### Path 7: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand5] aper (test)
                  [REGISTERED:dffr] buro (test)
```

### Path 8: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] atoz (joypad)
                  [REGISTERED:dffr] kecy (test)
```

### Path 9: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] atoz (joypad)
                  [REGISTERED:dffr] kuko (test)
```

### Path 10: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] atoz (joypad)
                  [REGISTERED:dffr] keru (test)
```


## apu-ch2 (70 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] anuj (apu-control)
                      [nand2] evyf (apu-ch2)
                        [not_x1] duso (apu-ch2)
                          [REGISTERED:drlatch_ee] emer (apu-ch2)
```

### Path 2: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] anuj (apu-control)
                      [nand2] evyf (apu-ch2)
                        [REGISTERED:drlatch_ee] emer (apu-ch2)
```

### Path 3: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] dosa (apu-ch2)
                      [not_x2] esur (apu-ch2) x2
                        [REGISTERED:drlatch_ee] fora (apu-ch2)
```

### Path 4: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] exuc (apu-ch2)
                      [not_x1] fyxo (apu-ch2)
                        [REGISTERED:drlatch_ee] gupu (apu-ch2)
```

### Path 5: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] exuc (apu-ch2)
                      [not_x1] fyxo (apu-ch2)
                        [REGISTERED:drlatch_ee] gumy (apu-ch2)
```

### Path 6: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] dosa (apu-ch2)
                      [not_x2] esur (apu-ch2) x2
                        [REGISTERED:drlatch_ee] fova (apu-ch2)
```

### Path 7: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] dosa (apu-ch2)
                      [not_x2] esur (apu-ch2) x2
                        [REGISTERED:drlatch_ee] fome (apu-ch2)
```

### Path 8: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] dosa (apu-ch2)
                      [not_x2] esur (apu-ch2) x2
                        [REGISTERED:drlatch_ee] fedy (apu-ch2)
```

### Path 9: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] exuc (apu-ch2)
                      [not_x1] fyxo (apu-ch2)
                        [REGISTERED:drlatch_ee] goda (apu-ch2)
```

### Path 10: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] jenu (apu-ch2)
                      [not_x1] kysa (apu-ch2)
                        [REGISTERED:drlatch_ee] jany (apu-ch2)
```


## apu-ch1 (126 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] anuj (apu-control)
                      [nand2] bage (apu-ch1)
                        [not_x1] bamu (apu-ch1)
                          [REGISTERED:drlatch_ee] boko (apu-ch1)
```

### Path 2: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] cenu (apu-ch1)
                      [not_x2] ahyc (apu-ch1) x2
                        [REGISTERED:drlatch_ee] avaf (apu-ch1)
```

### Path 3: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] cenu (apu-ch1)
                      [not_x2] ahyc (apu-ch1) x2
                        [REGISTERED:drlatch_ee] anaz (apu-ch1)
```

### Path 4: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] cenu (apu-ch1)
                      [not_x2] ahyc (apu-ch1) x2
                        [REGISTERED:drlatch_ee] arax (apu-ch1)
```

### Path 5: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] cenu (apu-ch1)
                      [not_x2] ahyc (apu-ch1) x2
                        [REGISTERED:drlatch_ee] bana (apu-ch1)
```

### Path 6: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] cenu (apu-ch1)
                      [not_x2] ahyc (apu-ch1) x2
                        [REGISTERED:drlatch_ee] adek (apu-ch1)
```

### Path 7: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] cenu (apu-ch1)
                      [not_x2] ahyc (apu-ch1) x2
                        [REGISTERED:drlatch_ee] botu (apu-ch1)
```

### Path 8: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] cenu (apu-ch1)
                      [not_x2] ahyc (apu-ch1) x2
                        [REGISTERED:drlatch_ee] bany (apu-ch1)
```

### Path 9: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] gaxu (apu-ch1)
                      [not_x2] kagy (apu-ch1) x2
                        [REGISTERED:drlatch_ee] jopu (apu-ch1)
```

### Path 10: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] hafu (apu-ch1)
                      [not_x1] kygy (apu-ch1)
                        [REGISTERED:drlatch_ee] juzy (apu-ch1)
```


## apu-ch3 (72 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] anuj (apu-control)
                      [nand2] fovo (apu-ch3)
                        [not_x1] gygu (apu-ch3)
                          [REGISTERED:drlatch_ee] hoto (apu-ch3)
```

### Path 2: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] gejo (apu-ch3)
                      [not_x1] gucy (apu-ch3)
                        [REGISTERED:drlatch_ee] guxe (apu-ch3)
```

### Path 3: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] haga (apu-ch3)
                      [not_x1] guzu (apu-ch3)
                        [REGISTERED:drlatch_ee] huky (apu-ch3)
```

### Path 4: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] haga (apu-ch3)
                      [not_x1] guzu (apu-ch3)
                        [REGISTERED:drlatch_ee] hody (apu-ch3)
```

### Path 5: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] enuf (apu-ch2)
                      [not_x2] elas (apu-ch2) x2
                        [REGISTERED:drlatch_ee] gage (apu-ch3)
```

### Path 6: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] huda (apu-ch3)
                      [not_x1] hufa (apu-ch3)
                        [REGISTERED:drlatch_ee] jety (apu-ch3)
```

### Path 7: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] huda (apu-ch3)
                      [not_x1] hufa (apu-ch3)
                        [REGISTERED:drlatch_ee] jacy (apu-ch3)
```

### Path 8: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] huda (apu-ch3)
                      [not_x1] hufa (apu-ch3)
                        [REGISTERED:drlatch_ee] jemo (apu-ch3)
```

### Path 9: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] kota (apu-ch3)
                      [not_x1] kyho (apu-ch3)
                        [REGISTERED:drlatch_ee] kogu (apu-ch3)
```

### Path 10: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] jafa (apu-ch3)
                      [not_x2] kuly (apu-ch3) x2
                        [REGISTERED:drlatch_ee] jypo (apu-ch3)
```


## apu-ch4 (80 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] anuj (apu-control)
                      [nand2] dulu (apu-ch4)
                        [not_x1] cazo (apu-ch4)
                          [REGISTERED:drlatch_ee] cuny (apu-ch4)
```

### Path 2: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] getu (apu-ch4)
                      [not_x2] efug (apu-ch4) x2
                        [REGISTERED:drlatch_ee] feta (apu-ch4)
```

### Path 3: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] getu (apu-ch4)
                      [not_x2] efug (apu-ch4) x2
                        [REGISTERED:drlatch_ee] fyto (apu-ch4)
```

### Path 4: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] getu (apu-ch4)
                      [not_x2] efug (apu-ch4) x2
                        [REGISTERED:drlatch_ee] gafo (apu-ch4)
```

### Path 5: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] getu (apu-ch4)
                      [not_x2] efug (apu-ch4) x2
                        [REGISTERED:drlatch_ee] gogo (apu-ch4)
```

### Path 6: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] humo (apu-ch4)
                      [not_x2] hova (apu-ch4) x2
                        [REGISTERED:drlatch_ee] jare (apu-ch4)
```

### Path 7: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] humo (apu-ch4)
                      [not_x2] hova (apu-ch4) x2
                        [REGISTERED:drlatch_ee] jaky (apu-ch4)
```

### Path 8: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] humo (apu-ch4)
                      [not_x2] hova (apu-ch4) x2
                        [REGISTERED:drlatch_ee] jero (apu-ch4)
```

### Path 9: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] goko (apu-ch4)
                      [not_x2] fupa (apu-ch4) x2
                        [REGISTERED:drlatch_ee] geky (apu-ch4)
```

### Path 10: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [and2] daco (apu-ch4)
                      [not_x1] dyke (apu-ch4)
                        [REGISTERED:drlatch_ee] emok (apu-ch4)
```


## apu-control (42 paths, max depth 14)

### Path 1: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bupo (apu-control)
                      [not_x2] byfa (apu-control) x2
                        [not_x2] acyj (apu-control) x2
                          [REGISTERED:drlatch_ee] bofa (apu-control)
```

### Path 2: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bosu (apu-control)
                      [not_x2] baxy (apu-control) x2
                        [not_x2] bubu (apu-control) x2
                          [REGISTERED:drlatch_ee] bedu (apu-control)
```

### Path 3: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bupo (apu-control)
                      [not_x2] bono (apu-control) x2
                        [not_x2] acup (apu-control) x2
                          [REGISTERED:drlatch_ee] bafo (apu-control)
```

### Path 4: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bupo (apu-control)
                      [not_x2] byfa (apu-control) x2
                        [not_x2] acyj (apu-control) x2
                          [REGISTERED:drlatch_ee] befo (apu-control)
```

### Path 5: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bosu (apu-control)
                      [not_x2] baxy (apu-control) x2
                        [not_x2] bubu (apu-control) x2
                          [REGISTERED:drlatch_ee] bumo (apu-control)
```

### Path 6: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bosu (apu-control)
                      [not_x2] baxy (apu-control) x2
                        [not_x2] bubu (apu-control) x2
                          [REGISTERED:drlatch_ee] cozu (apu-control)
```

### Path 7: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bupo (apu-control)
                      [not_x2] bono (apu-control) x2
                        [not_x2] acup (apu-control) x2
                          [REGISTERED:drlatch_ee] atuf (apu-control)
```

### Path 8: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bosu (apu-control)
                      [not_x2] bowe (apu-control) x2
                        [not_x2] ataf (apu-control) x2
                          [REGISTERED:drlatch_ee] byga (apu-control)
```

### Path 9: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bosu (apu-control)
                      [not_x2] baxy (apu-control) x2
                        [not_x2] bubu (apu-control) x2
                          [REGISTERED:drlatch_ee] byre (apu-control)
```

### Path 10: depth 14 (70-210 ns, 176% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [not_x1] bafu (apu-control)
                  [not_x6] bogy (apu-control) x6 fan-out=37
                    [nand2] bupo (apu-control)
                      [not_x2] bono (apu-control) x2
                        [not_x2] acup (apu-control) x2
                          [REGISTERED:drlatch_ee] anev (apu-control)
```


## LCD Output (16 paths, max depth 14)

### Path 1: depth 14 (70-210 ns, 176% half T-cycle)
```
[REGISTERED:dffsr] sohu (ppu-bgfifo)
  [and2] tade (ppu-mux)
    [and2] ruta (ppu-mux)
      [nor3] poka (ppu-mux)
        [nand2] leka (ppu-mux)
          [not_x1] luku (ppu-mux)
            [and3] laru (ppu-mux)
              [ao2222] moka (ppu-mux)
                [or3] paty (ppu-mux)
                  [not_x2] ravo (ppu-mux) x2
                    [PAD:pad_out] ld1 (ppu-lcd)
```

### Path 2: depth 14 (70-210 ns, 176% half T-cycle)
```
[REGISTERED:dffsr] sohu (ppu-bgfifo)
  [and2] tade (ppu-mux)
    [and2] ruta (ppu-mux)
      [nor3] poka (ppu-mux)
        [nand2] leka (ppu-mux)
          [not_x1] luku (ppu-mux)
            [and3] laru (ppu-mux)
              [ao2222] mufa (ppu-mux)
                [or3] pero (ppu-mux)
                  [not_x2] remy (ppu-mux) x2
                    [PAD:pad_out] ld0 (ppu-lcd)
```

### Path 3: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:dffr] luca (ppu-lcd)
  [xor] magu (ppu-lcd)
    [not_x3] meco (ppu-lcd) x3
      [not_x1] kebo (ppu-lcd)
        [ao22] kupa (ppu-lcd)
          [not_x3] kofo (ppu-lcd) x3
            [PAD:pad_out] fr (ppu-lcd)
```

### Path 4: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:nor_latch] roxy (ppu-cycles)
  [or2] sacu (ppu-cycles) fan-out=53
    [and2] toba (ppu-cycles)
      [or2] semu (ppu-cycles)
        [not_x3] rypo (ppu-cycles) x3
          [PAD:pad_out] cp (ppu-lcd)
```

### Path 5: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] taha (ppu-lcd)
  [not_x1] tafy (ppu-lcd)
    [nand7] tebo (ppu-lcd)
      [nand4] tegy (ppu-lcd)
        [REGISTERED:dffr] sygu (ppu-lcd)
```

### Path 6: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] rutu (ppu-lcd)
  [or2] ryno (ppu-lcd)
    [not_x2] pogu (ppu-lcd) x2
      [PAD:pad_out] cpg (ppu-lcd)
```

### Path 7: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] vena (ppu-lcd)
  [not_x4] talu (ppu-lcd) x4
    [not_x1] sono (ppu-lcd)
      [REGISTERED:dffr] rutu (ppu-lcd)
```

### Path 8: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] saxo (ppu-lcd)
  [and4] sanu (ppu-lcd)
    [REGISTERED:dffr] rutu (ppu-lcd)
```

### Path 9: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] vena (ppu-lcd)
  [not_x4] talu (ppu-lcd) x4
    [not_x1] sono (ppu-lcd)
      [REGISTERED:dffr] sygu (ppu-lcd)
```

### Path 10: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] lydo (ppu-stat)
  [and4] noko (ppu-lcd)
    [REGISTERED:dffr] myta (ppu-lcd)
```


## Address Bus (34 paths, max depth 13)

### Path 1: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [oa21] agut (clocks)
          [nor2] awod (clocks)
            [not_x3] abuz (clocks) x3
              [nand2] sepy (bus-adr)
                [mux] tazy (bus-adr)
                  [nor2] rulo (bus-adr)
                    [PAD:pad_bidir] a15 (bus-adr)
```

### Path 2: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] lobu (bus-adr)
```

### Path 3: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] lonu (bus-adr)
```

### Path 4: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] nyre (bus-adr)
```

### Path 5: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] alor (bus-adr)
```

### Path 6: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] pate (bus-adr)
```

### Path 7: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] lumy (bus-adr)
```

### Path 8: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] lysa (bus-adr)
```

### Path 9: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] luno (bus-adr)
```

### Path 10: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [and2] texo (bus-adr)
          [ao21] loxo (bus-adr)
            [not_x1] lasy (bus-adr)
              [not_x1] mate (bus-adr) fan-out=15
                [REGISTERED:dlatch] apur (bus-adr)
```


## Clock Distribution (17 paths, max depth 13)

### Path 1: depth 13 (65-195 ns, 164% half T-cycle)
```
[BUS:] bus:~clk_t4 (bus)
  [nand4] beja (clocks)
    [not_x1] bane (clocks)
      [not_x1] belo (clocks)
        [not_x1] baze (clocks)
          [nand3] buto (clocks)
            [not_x1] bele (clocks)
              [or2] byju (clocks)
                [not_x1] baly (clocks)
                  [not_x6] boga (clocks) x6 fan-out=12
                    [mux] ulur (clocks)
                      [REGISTERED:dffr] ugot (clocks)
```

### Path 2: depth 12 (60-180 ns, 151% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [and4] tape (clocks)
                  [nor3] ufol (clocks) fan-out=16
                    [REGISTERED:dffr] ukup (clocks)
```

### Path 3: depth 12 (60-180 ns, 151% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [and4] tape (clocks)
                  [nor3] ufol (clocks) fan-out=16
                    [REGISTERED:dffr] ufor (clocks)
```

### Path 4: depth 12 (60-180 ns, 151% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [and4] tape (clocks)
                  [nor3] ufol (clocks) fan-out=16
                    [REGISTERED:dffr] uner (clocks)
```

### Path 5: depth 12 (60-180 ns, 151% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [and4] tape (clocks)
                  [nor3] ufol (clocks) fan-out=16
                    [REGISTERED:dffr] tero (clocks)
```

### Path 6: depth 12 (60-180 ns, 151% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [and4] tape (clocks)
                  [nor3] ufol (clocks) fan-out=16
                    [REGISTERED:dffr] unyk (clocks)
```

### Path 7: depth 12 (60-180 ns, 151% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [and4] tape (clocks)
                  [nor3] ufol (clocks) fan-out=16
                    [REGISTERED:dffr] tama (clocks)
```

### Path 8: depth 11 (55-165 ns, 138% half T-cycle)
```
[BUS:] bus:~clk_t4 (bus)
  [nand4] beja (clocks)
    [not_x1] bane (clocks)
      [not_x1] belo (clocks)
        [not_x1] baze (clocks)
          [nand3] buto (clocks)
            [not_x1] bele (clocks)
              [or2] byju (clocks)
                [not_x1] baly (clocks)
                  [not_x6] boga (clocks) x6 fan-out=12
                    [not_x6] boma (clocks) x6
                      [REGISTERED:dffr_cc] afer (clocks)
```

### Path 9: depth 10 (50-150 ns, 126% half T-cycle)
```
[BUS:] bus:~clk_t4 (bus)
  [nand4] beja (clocks)
    [not_x1] bane (clocks)
      [not_x1] belo (clocks)
        [not_x1] baze (clocks)
          [nand3] buto (clocks)
            [not_x1] bele (clocks)
              [or2] byju (clocks)
                [not_x1] baly (clocks)
                  [not_x6] boga (clocks) x6 fan-out=12
                    [REGISTERED:dffr_cc] afer (clocks)
```

### Path 10: depth 10 (50-150 ns, 126% half T-cycle)
```
[BUS:] bus:~clk_t4 (bus)
  [nand4] beja (clocks)
    [not_x1] bane (clocks)
      [not_x1] belo (clocks)
        [not_x1] baze (clocks)
          [nand3] buto (clocks)
            [not_x1] bele (clocks)
              [or2] byju (clocks)
                [not_x1] baly (clocks)
                  [not_x6] boga (clocks) x6 fan-out=12
                    [REGISTERED:dffr] ukup (clocks)
```


## Timer (22 paths, max depth 13)

### Path 1: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tope (timer)
                  [muxi] syru (timer)
                    [nor2] rugy (timer)
                      [REGISTERED:tffnl] rage (timer)
```

### Path 2: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tope (timer)
                  [muxi] refu (timer)
                    [nor2] pyma (timer)
                      [REGISTERED:tffnl] peda (timer)
```

### Path 3: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tope (timer)
                  [muxi] rato (timer)
                    [nor2] pagu (timer)
                      [REGISTERED:tffnl] nuga (timer)
```

### Path 4: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tope (timer)
                  [or2] muzu (timer)
                    [nand3] mexu (timer)
                      [REGISTERED:tffnl] rega (timer)
```

### Path 5: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tope (timer)
                  [or2] muzu (timer)
                    [nand3] mexu (timer)
                      [REGISTERED:tffnl] povy (timer)
```

### Path 6: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tope (timer)
                  [or2] muzu (timer)
                    [nand3] mexu (timer)
                      [REGISTERED:tffnl] peru (timer)
```

### Path 7: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tope (timer)
                  [or2] muzu (timer)
                    [nand3] mexu (timer)
                      [REGISTERED:tffnl] rate (timer)
```

### Path 8: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tope (timer)
                  [or2] muzu (timer)
                    [nand3] mexu (timer)
                      [REGISTERED:tffnl] ruby (timer)
```

### Path 9: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tyju (timer)
                  [REGISTERED:dffr] muru (timer)
```

### Path 10: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tyju (timer)
                  [REGISTERED:dffr] tyva (timer)
```


## Sprite Y Compare (28 paths, max depth 13)

### Path 1: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [not_x2] ajas (ppu-control) x2
              [not_x4] asot (ppu-control) x4 fan-out=14
                [nand3] bota (ppu-oam)
                  [and3] asyt (ppu-oam)
                    [not_x1] bode (ppu-oam) fan-out=17
                      [REGISTERED:dlatch] zaxe (ppu-ycomp)
```

### Path 2: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [not_x2] ajas (ppu-control) x2
              [not_x4] asot (ppu-control) x4 fan-out=14
                [nand3] bota (ppu-oam)
                  [and3] asyt (ppu-oam)
                    [not_x1] bode (ppu-oam) fan-out=17
                      [REGISTERED:dlatch] xafu (ppu-ycomp)
```

### Path 3: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [not_x2] ajas (ppu-control) x2
              [not_x4] asot (ppu-control) x4 fan-out=14
                [nand3] bota (ppu-oam)
                  [and3] asyt (ppu-oam)
                    [not_x1] bode (ppu-oam) fan-out=17
                      [REGISTERED:dlatch] wone (ppu-ycomp)
```

### Path 4: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [not_x2] ajas (ppu-control) x2
              [not_x4] asot (ppu-control) x4 fan-out=14
                [nand3] bota (ppu-oam)
                  [and3] asyt (ppu-oam)
                    [not_x1] bode (ppu-oam) fan-out=17
                      [REGISTERED:dlatch] yses (ppu-ycomp)
```

### Path 5: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [not_x2] ajas (ppu-control) x2
              [not_x4] asot (ppu-control) x4 fan-out=14
                [nand3] bota (ppu-oam)
                  [and3] asyt (ppu-oam)
                    [not_x1] bode (ppu-oam) fan-out=17
                      [REGISTERED:dlatch] zeca (ppu-ycomp)
```

### Path 6: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [not_x2] ajas (ppu-control) x2
              [not_x4] asot (ppu-control) x4 fan-out=14
                [nand3] bota (ppu-oam)
                  [and3] asyt (ppu-oam)
                    [not_x1] bode (ppu-oam) fan-out=17
                      [REGISTERED:dlatch] yceb (ppu-ycomp)
```

### Path 7: depth 13 (65-195 ns, 164% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [not_x2] ajas (ppu-control) x2
              [not_x4] asot (ppu-control) x4 fan-out=14
                [nand3] bota (ppu-oam)
                  [and3] asyt (ppu-oam)
                    [not_x1] bode (ppu-oam) fan-out=17
                      [REGISTERED:dlatch] zuca (ppu-ycomp)
```

### Path 8: depth 11 (55-165 ns, 138% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [not_x2] apux (ppu-stat) x2 fan-out=10
    [xor] woju (ppu-xcomp)
      [nor4] xeba (ppu-xcomp)
        [nand3] ydug (ppu-xprio)
          [nand5] fefy (ppu-xprio)
            [or2] fepo (ppu-xprio)
              [and4] teky (ppu-ycomp)
                [REGISTERED:dffr] sobu (ppu-ycomp)
```

### Path 9: depth 11 (55-165 ns, 138% half T-cycle)
```
[BUS:] bus:a15 (bus)
  [nand7] tuna (sys-decode)
    [nor2] syke (sys-decode) fan-out=11
      [not_x1] soha (sys-decode)
        [nand2] rope (sys-decode)
          [not_x2] saro (sys-decode) x2
            [oai21] cufe (ppu-oam)
              [nand3] bycu (ppu-oam)
                [not_x2] cota (ppu-oam) x2
                  [not_x1] ywok (ppu-ycomp)
                    [not_x1] ysum (ppu-ycomp)
                      [REGISTERED:dlatch_ee] ybog (ppu-ycomp)
```

### Path 10: depth 11 (55-165 ns, 138% half T-cycle)
```
[BUS:] bus:a15 (bus)
  [nand7] tuna (sys-decode)
    [nor2] syke (sys-decode) fan-out=11
      [not_x1] soha (sys-decode)
        [nand2] rope (sys-decode)
          [not_x2] saro (sys-decode) x2
            [oai21] cufe (ppu-oam)
              [nand3] bycu (ppu-oam)
                [not_x2] cota (ppu-oam) x2
                  [not_x1] ywok (ppu-ycomp)
                    [not_x1] ysum (ppu-ycomp)
                      [REGISTERED:dlatch_ee] wyso (ppu-ycomp)
```


## Joypad (23 paths, max depth 10)

### Path 1: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] atoz (joypad)
                  [REGISTERED:dffr] kely (joypad)
```

### Path 2: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] atoz (joypad)
                  [REGISTERED:dffr] cofy (joypad)
```

### Path 3: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [and4] acat (joypad)
              [not_x1] byzo (joypad) fan-out=10
                [REGISTERED:dlatch] kapa (joypad)
```

### Path 4: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [and4] acat (joypad)
              [not_x1] byzo (joypad) fan-out=10
                [REGISTERED:dlatch] kolo (joypad)
```

### Path 5: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [and4] acat (joypad)
              [not_x1] byzo (joypad) fan-out=10
                [REGISTERED:dlatch] kevu (joypad)
```

### Path 6: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [and4] acat (joypad)
              [not_x1] byzo (joypad) fan-out=10
                [REGISTERED:dlatch] keja (joypad)
```

### Path 7: depth 10 (50-150 ns, 126% half T-cycle)
```
[BUS:] bus:~clk_t4 (bus)
  [nand4] beja (clocks)
    [not_x1] bane (clocks)
      [not_x1] belo (clocks)
        [not_x1] baze (clocks)
          [nand3] buto (clocks)
            [not_x1] bele (clocks)
              [or2] byju (clocks)
                [not_x1] baly (clocks)
                  [not_x6] boga (clocks) x6 fan-out=12
                    [REGISTERED:dlatch] awob (joypad)
```

### Path 8: depth 10 (50-150 ns, 126% half T-cycle)
```
[BUS:] bus:~clk_t4 (bus)
  [nand4] beja (clocks)
    [not_x1] bane (clocks)
      [not_x1] belo (clocks)
        [not_x1] baze (clocks)
          [nand3] buto (clocks)
            [not_x1] bele (clocks)
              [or2] byju (clocks)
                [not_x1] baly (clocks)
                  [not_x6] boga (clocks) x6 fan-out=12
                    [REGISTERED:dffr] batu (joypad)
```

### Path 9: depth 10 (50-150 ns, 126% half T-cycle)
```
[BUS:] bus:~clk_t4 (bus)
  [nand4] beja (clocks)
    [not_x1] bane (clocks)
      [not_x1] belo (clocks)
        [not_x1] baze (clocks)
          [nand3] buto (clocks)
            [not_x1] bele (clocks)
              [or2] byju (clocks)
                [not_x1] baly (clocks)
                  [not_x6] boga (clocks) x6 fan-out=12
                    [REGISTERED:dffr] acef (joypad)
```

### Path 10: depth 10 (50-150 ns, 126% half T-cycle)
```
[BUS:] bus:~clk_t4 (bus)
  [nand4] beja (clocks)
    [not_x1] bane (clocks)
      [not_x1] belo (clocks)
        [not_x1] baze (clocks)
          [nand3] buto (clocks)
            [not_x1] bele (clocks)
              [or2] byju (clocks)
                [not_x1] baly (clocks)
                  [not_x6] boga (clocks) x6 fan-out=12
                    [REGISTERED:dffr] agem (joypad)
```


## bootrom (1 paths, max depth 10)

### Path 1: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] tuge (bootrom)
                  [REGISTERED:dffr] tepu (bootrom)
```


## Serial (10 paths, max depth 10)

### Path 1: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] uwam (serial)
                  [REGISTERED:dffr] culy (serial)
```

### Path 2: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] uwam (serial)
                  [REGISTERED:dffr] etaf (serial)
```

### Path 3: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [nand2] arev (clocks)
          [not_x3] apov (clocks) x3
            [muxi] ubal (bus-data)
              [not_x3] tapu (bus-data) x3 fan-out=13
                [nand4] uwam (serial)
                  [REGISTERED:dffr] coty (serial)
```

### Path 4: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] etaf (serial)
  [or2] dawa (serial)
    [nor2] kujo (serial)
      [PAD:pad_bidir_pu_latch] sck (serial)
```

### Path 5: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] etaf (serial)
  [or2] dawa (serial)
    [not_x1] edyl (serial)
      [REGISTERED:dffr] elys (serial)
```

### Path 6: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [not_x1] jeva (test)
    [nor2] kywe (test)
      [PAD:pad_bidir_pu] sin (serial)
```

### Path 7: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] etaf (serial)
  [or2] dawa (serial)
    [REGISTERED:dffr] cafa (serial)
```

### Path 8: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] elys (serial)
  [muxi] kena (serial)
    [PAD:pad_out] sout (serial)
```

### Path 9: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [nand2] kore (test)
    [PAD:pad_bidir_pu] sin (serial)
```

### Path 10: depth 1 (5-15 ns, 13% half T-cycle)
```
[PAD:pad_bidir_pu] sin (serial)
  [not_x1] cage (serial)
    [REGISTERED:dffsr] cuba (serial)
```


## Sprite Pixel Shifter (48 paths, max depth 9)

### Path 1: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] puly (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] rydu (ppu-objfifo)
```

### Path 2: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] puly (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] sega (ppu-objfifo)
```

### Path 3: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pugu (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] suny (ppu-objfifo)
```

### Path 4: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pugu (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] suto (ppu-objfifo)
```

### Path 5: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pelo (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] peba (ppu-objfifo)
```

### Path 6: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pelo (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] roka (ppu-objfifo)
```

### Path 7: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pacy (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] sele (ppu-objfifo)
```

### Path 8: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pacy (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] saja (ppu-objfifo)
```

### Path 9: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pawe (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] semo (ppu-objfifo)
```

### Path 10: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pawe (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] rama (ppu-objfifo)
```


## Interrupts (5 paths, max depth 8)

### Path 1: depth 8 (40-120 ns, 101% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [nand4] rolo (int)
              [REGISTERED:dlatch] nejy (int)
```

### Path 2: depth 8 (40-120 ns, 101% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [nand4] rolo (int)
              [REGISTERED:dlatch] nuty (int)
```

### Path 3: depth 8 (40-120 ns, 101% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [nand4] rolo (int)
              [REGISTERED:dlatch] pavy (int)
```

### Path 4: depth 8 (40-120 ns, 101% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [nand4] rolo (int)
              [REGISTERED:dlatch] maty (int)
```

### Path 5: depth 8 (40-120 ns, 101% half T-cycle)
```
[PAD:pad_in] t2 (test)
  [not_x1] uvar (test)
    [and2] umut (test)
      [sm83] cpu () fan-out=42
        [muxi] ujyv (bus-data)
          [not_x3] tedo (bus-data) x3 fan-out=14
            [nand4] rolo (int)
              [REGISTERED:dlatch] mopo (int)
```


## BG/Win Cycles (7 paths, max depth 8)

### Path 1: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:drlatch_ee] nuku (ppu-window)
  [xnor] pase (ppu-window)
    [nand5] puky (ppu-window)
      [not_x1] nufa (ppu-window)
        [nand5] nogy (ppu-window)
          [not_x1] nuko (ppu-window)
            [nor2] pany (ppu-cycles)
              [REGISTERED:dffr] ryfa (ppu-cycles)
```

### Path 2: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:drlatch_ee] nuku (ppu-window)
  [xnor] pase (ppu-window)
    [nand5] puky (ppu-window)
      [not_x1] nufa (ppu-window)
        [nand5] nogy (ppu-window)
          [not_x1] nuko (ppu-window)
            [REGISTERED:dffr] pyco (ppu-cycles)
```

### Path 3: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] nyka (ppu-cycles)
  [nand4] suvu (ppu-cycles)
    [not_x1] tave (ppu-cycles)
      [or3] tevo (ppu-cycles)
        [nor2] paso (ppu-cycles)
          [REGISTERED:dffr] roga (ppu-cycles)
```

### Path 4: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] nyka (ppu-cycles)
  [nand4] suvu (ppu-cycles)
    [not_x1] tave (ppu-cycles)
      [or3] tevo (ppu-cycles)
        [nor2] paso (ppu-cycles)
          [REGISTERED:dffr] rubu (ppu-cycles)
```

### Path 5: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] nyka (ppu-cycles)
  [nand4] suvu (ppu-cycles)
    [not_x1] tave (ppu-cycles)
      [or3] tevo (ppu-cycles)
        [nor2] paso (ppu-cycles)
          [REGISTERED:dffr] ryku (ppu-cycles)
```

### Path 6: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] ryku (ppu-cycles)
  [xnor] suha (ppu-cycles)
    [nand4] rone (ppu-cycles)
      [not_x1] pohu (ppu-cycles)
        [REGISTERED:dffr] puxa (ppu-cycles)
```

### Path 7: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] rubu (ppu-cycles)
  [nand3] roze (ppu-cycles)
    [nand2] pecu (ppu-cycles)
      [REGISTERED:dffr] ryku (ppu-cycles)
```


## BG Pixel Shifter (32 paths, max depth 7)

### Path 1: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [not_x2] labu (ppu-bgfifo) x2
              [REGISTERED:dffr_cc_q] pozo (ppu-bgfifo)
```

### Path 2: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [not_x2] labu (ppu-bgfifo) x2
              [REGISTERED:dffr_cc_q] pyzo (ppu-bgfifo)
```

### Path 3: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [not_x2] labu (ppu-bgfifo) x2
              [REGISTERED:dffr_cc_q] pyju (ppu-bgfifo)
```

### Path 4: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [not_x2] labu (ppu-bgfifo) x2
              [REGISTERED:dffr_cc_q] poju (ppu-bgfifo)
```

### Path 5: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [not_x2] labu (ppu-bgfifo) x2
              [REGISTERED:dffr_cc_q] pulo (ppu-bgfifo)
```

### Path 6: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [not_x2] labu (ppu-bgfifo) x2
              [REGISTERED:dffr_cc_q] powy (ppu-bgfifo)
```

### Path 7: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [not_x2] labu (ppu-bgfifo) x2
              [REGISTERED:dffr_cc_q] rawu (ppu-bgfifo)
```

### Path 8: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [not_x2] labu (ppu-bgfifo) x2
              [REGISTERED:dffr_cc_q] poxa (ppu-bgfifo)
```

### Path 9: depth 6 (30-90 ns, 76% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [REGISTERED:dffr_cc_q] pozo (ppu-bgfifo)
```

### Path 10: depth 6 (30-90 ns, 76% half T-cycle)
```
[REGISTERED:dffr] laxu (ppu-cycles)
  [not_x1] laxe (ppu-cycles)
    [nor3] myso (ppu-cycles)
      [and2] mofu (ppu-cycles)
        [not_x1] leso (ppu-bgfifo)
          [not_x2] luve (ppu-bgfifo) x2
            [REGISTERED:dffr_cc_q] pyzo (ppu-bgfifo)
```


## OAM Interface (19 paths, max depth 3)

### Path 1: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [not_x2] wuda (ppu-oam) x2
        [REGISTERED:dffr_cc] xecu (ppu-oam)
```

### Path 2: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [not_x2] wuda (ppu-oam) x2
        [REGISTERED:dffr_cc] xadu (ppu-oam)
```

### Path 3: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [not_x2] wuda (ppu-oam) x2
        [REGISTERED:dffr_cc] zuze (ppu-oam)
```

### Path 4: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [not_x2] wuda (ppu-oam) x2
        [REGISTERED:dffr_cc] xedy (ppu-oam)
```

### Path 5: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [not_x2] wuda (ppu-oam) x2
        [REGISTERED:dffr_cc] yduf (ppu-oam)
```

### Path 6: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [not_x2] wuda (ppu-oam) x2
        [REGISTERED:dffr_cc] xobe (ppu-oam)
```

### Path 7: depth 2 (10-30 ns, 25% half T-cycle)
```
[BUS:] bus:clk_t4 (bus)
  [not_x1] decy (ppu-oam)
    [not_x1] caty (ppu-oam)
      [REGISTERED:dffr] maka (ppu-oam)
```

### Path 8: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [REGISTERED:dffr_cc] xecu (ppu-oam)
```

### Path 9: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [REGISTERED:dffr_cc] xadu (ppu-oam)
```

### Path 10: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] wuvu (ppu-lcd)
  [not_x2] xupy (ppu-oam) x2
    [not_x2] cyke (ppu-oam) x2
      [REGISTERED:dffr_cc] zuze (ppu-oam)
```
