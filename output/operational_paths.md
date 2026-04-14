# Operational Critical Paths by Functional Area


## Sprite Control (3 paths, max depth 39)

### Path 1: depth 39 (195-585 ns, 491% half T-cycle)
```
[REGISTERED:dffr] muwy (ppu-stat)
  [not_x1] ebos (ppu-ycomp)
    [full_add] eruc (ppu-ycomp)
      [full_add] enef (ppu-ycomp)
        [full_add] feco (ppu-ycomp)
          [full_add] gyky (ppu-ycomp)
            [full_add] gopu (ppu-ycomp)
              [full_add] fuwa (ppu-ycomp)
                [full_add] goju (ppu-ycomp)
                  [full_add] wuhu (ppu-ycomp)
                    [not_x1] gewy (ppu-ycomp)
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

### Path 3: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] fony (ppu-objctl)
  [and4] feto (ppu-objctl)
    [REGISTERED:dffr] byba (ppu-objctl)
```


## test (17 paths, max depth 32)

### Path 1: depth 32 (160-480 ns, 403% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [and2] byza (apu-ch3)
                        [or3] beta (apu-ch3)
                          [not_x1] azor (apu-ch3)
                            [not_x6] buku (apu-ch3) x6
                              [mux] atur (apu-ch3)
                                [not_x3] aler (apu-ch3) x3
                                  [not_x1] yrar (apu-ch3)
                                    [and2] ymaw (apu-ch3)
                                      [or2] ysod (apu-ch3)
                                        [and2] ylac (apu-ch3)
                                          [or2] ymul (apu-ch3)
                                            [BOUNDARY:wave_ram] wave_ram () fan-out=16
```

### Path 2: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [muxi] ujyv (bus-data)
            [not_x3] tedo (bus-data) x3 fan-out=14
              [not_x2] ajas (ppu-control) x2
                [not_x4] asot (ppu-control) x4 fan-out=14
                  [nand3] bota (ppu-oam)
                    [and3] asyt (ppu-oam)
                      [not_x1] bode (ppu-oam) fan-out=17
                        [not_x1] yval (ppu-oam)
                          [not_x1] yryv (ppu-oam)
                            [not_x2] zodo (ppu-oam) x2
                              [not_x1] wusu (ppu-oam)
                                [or3] wazo (ppu-oam)
                                  [nand2] wujy (ppu-oam)
                                    [not_x3] wahe (ppu-oam) x3
                                      [nand2] wycy (ppu-oam)
                                        [not_x2] wory (ppu-oam) x2
                                          [not_x2] wame (ppu-oam) x2
                                            [BOUNDARY:oam] oam_a ()
```

### Path 3: depth 26 (130-390 ns, 327% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [muxi] ujyv (bus-data)
            [not_x3] tedo (bus-data) x3 fan-out=14
              [not_x2] ajas (ppu-control) x2
                [not_x4] asot (ppu-control) x4 fan-out=14
                  [nand3] bota (ppu-oam)
                    [and3] asyt (ppu-oam)
                      [not_x1] bode (ppu-oam) fan-out=17
                        [not_x1] yval (ppu-oam)
                          [not_x1] yryv (ppu-oam)
                            [not_x2] zodo (ppu-oam) x2
                              [not_x1] wusu (ppu-oam)
                                [or3] wazo (ppu-oam)
                                  [nand2] wujy (ppu-oam)
                                    [not_x3] wahe (ppu-oam) x3
                                      [nand2] wycy (ppu-oam)
                                        [not_x2] wory (ppu-oam) x2
                                          [not_x2] wame (ppu-oam) x2
                                            [BOUNDARY:oam] oam_b ()
```

### Path 4: depth 25 (125-375 ns, 315% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [muxi] ujyv (bus-data)
            [not_x3] tedo (bus-data) x3 fan-out=14
              [not_x2] ajas (ppu-control) x2
                [not_x4] asot (ppu-control) x4 fan-out=14
                  [nand3] bota (ppu-oam)
                    [and3] asyt (ppu-oam)
                      [not_x1] bode (ppu-oam) fan-out=17
                        [not_x1] yval (ppu-oam)
                          [not_x1] yryv (ppu-oam)
                            [not_x2] zodo (ppu-oam) x2
                              [not_x1] wusu (ppu-oam)
                                [or3] wazo (ppu-oam)
                                  [nand2] wujy (ppu-oam)
                                    [not_x3] wahe (ppu-oam) x3
                                      [nand2] wycy (ppu-oam)
                                        [not_x2] wory (ppu-oam) x2
                                          [BOUNDARY:oam] oam_a ()
```

### Path 5: depth 25 (125-375 ns, 315% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [muxi] ujyv (bus-data)
            [not_x3] tedo (bus-data) x3 fan-out=14
              [not_x2] ajas (ppu-control) x2
                [not_x4] asot (ppu-control) x4 fan-out=14
                  [nand3] bota (ppu-oam)
                    [and3] asyt (ppu-oam)
                      [not_x1] bode (ppu-oam) fan-out=17
                        [not_x1] yval (ppu-oam)
                          [not_x1] yryv (ppu-oam)
                            [not_x2] zodo (ppu-oam) x2
                              [not_x1] wusu (ppu-oam)
                                [or3] wazo (ppu-oam)
                                  [nand2] wujy (ppu-oam)
                                    [not_x3] wahe (ppu-oam) x3
                                      [nand2] wycy (ppu-oam)
                                        [not_x2] wory (ppu-oam) x2
                                          [BOUNDARY:oam] oam_b ()
```

### Path 6: depth 24 (120-360 ns, 302% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [and2] byza (apu-ch3)
                        [or3] beta (apu-ch3)
                          [not_x1] azor (apu-ch3)
                            [not_x6] buku (apu-ch3) x6
                              [mux] atur (apu-ch3)
                                [not_x3] aler (apu-ch3) x3
                                  [not_x1] yrar (apu-ch3)
                                    [BOUNDARY:wave_ram] wave_ram () fan-out=16
```

### Path 7: depth 23 (115-345 ns, 289% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [muxi] ujyv (bus-data)
            [not_x3] tedo (bus-data) x3 fan-out=14
              [not_x2] ajas (ppu-control) x2
                [not_x4] asot (ppu-control) x4 fan-out=14
                  [nand3] bota (ppu-oam)
                    [and3] asyt (ppu-oam)
                      [not_x1] bode (ppu-oam) fan-out=17
                        [not_x1] yval (ppu-oam)
                          [not_x1] yryv (ppu-oam)
                            [not_x2] zodo (ppu-oam) x2
                              [not_x1] wusu (ppu-oam)
                                [or3] wazo (ppu-oam)
                                  [nand2] wujy (ppu-oam)
                                    [not_x3] wahe (ppu-oam) x3
                                      [BOUNDARY:oam] oam_a ()
```

### Path 8: depth 23 (115-345 ns, 289% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [muxi] ujyv (bus-data)
            [not_x3] tedo (bus-data) x3 fan-out=14
              [not_x2] ajas (ppu-control) x2
                [not_x4] asot (ppu-control) x4 fan-out=14
                  [nand3] bota (ppu-oam)
                    [and3] asyt (ppu-oam)
                      [not_x1] bode (ppu-oam) fan-out=17
                        [not_x1] yval (ppu-oam)
                          [not_x1] yryv (ppu-oam)
                            [not_x2] zodo (ppu-oam) x2
                              [not_x1] wusu (ppu-oam)
                                [or3] wazo (ppu-oam)
                                  [nand2] wujy (ppu-oam)
                                    [not_x3] wahe (ppu-oam) x3
                                      [BOUNDARY:oam] oam_b ()
```

### Path 9: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [and2] byza (apu-ch3)
                        [not_x3] amyt (apu-ch3) x3
                          [not_x1] ydez (apu-ch3)
                            [BOUNDARY:wave_ram] wave_ram () fan-out=16
```

### Path 10: depth 17 (85-255 ns, 214% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [nand2] atef (hram)
                    [not_x2] apuh (hram) x2
                      [or2] wype (hram)
                        [nand2] wopo (hram)
                          [not_x2] wuly (hram) x2
                            [BOUNDARY:high_ram] high_ram ()
```


## bus (649 paths, max depth 32)

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
[REGISTERED:dffr] muwy (ppu-stat)
  [half_add] fafo (ppu-bgscroll)
    [full_add] emux (ppu-bgscroll)
      [full_add] ecab (ppu-bgscroll)
        [full_add] etam (ppu-bgscroll)
          [full_add] doto (ppu-bgscroll)
            [full_add] daba (ppu-bgscroll)
              [not_if0] cypo (ppu-bgscroll)
                [BUS:] bus:~ma7 (bus)
```

### Path 6: depth 24 (120-360 ns, 302% half T-cycle)
```
[REGISTERED:dffr] xeho (ppu-stat)
  [half_add] atad (ppu-bgscroll)
    [full_add] behu (ppu-bgscroll)
      [full_add] apyh (ppu-bgscroll)
        [full_add] babe (ppu-bgscroll)
          [full_add] abod (ppu-bgscroll)
            [full_add] bewy (ppu-bgscroll)
              [not_if0] alel (ppu-bgscroll)
                [BUS:] bus:~ma2 (bus)
```

### Path 7: depth 20 (100-300 ns, 252% half T-cycle)
```
[REGISTERED:dffr] muwy (ppu-stat)
  [half_add] fafo (ppu-bgscroll)
    [full_add] emux (ppu-bgscroll)
      [full_add] ecab (ppu-bgscroll)
        [full_add] etam (ppu-bgscroll)
          [full_add] doto (ppu-bgscroll)
            [not_if0] case (ppu-bgscroll)
              [BUS:] bus:~ma6 (bus)
```

### Path 8: depth 20 (100-300 ns, 252% half T-cycle)
```
[REGISTERED:dffr] xeho (ppu-stat)
  [half_add] atad (ppu-bgscroll)
    [full_add] behu (ppu-bgscroll)
      [full_add] apyh (ppu-bgscroll)
        [full_add] babe (ppu-bgscroll)
          [full_add] abod (ppu-bgscroll)
            [not_if0] afeb (ppu-bgscroll)
              [BUS:] bus:~ma1 (bus)
```

### Path 9: depth 19 (95-285 ns, 239% half T-cycle)
```
[REGISTERED:dffr] muwy (ppu-stat)
  [not_x1] ebos (ppu-ycomp)
    [full_add] eruc (ppu-ycomp)
      [full_add] enef (ppu-ycomp)
        [full_add] feco (ppu-ycomp)
          [full_add] gyky (ppu-ycomp)
            [not_x1] gysa (ppu-ycomp)
              [not_if0] wenu (ppu-ycomp)
                [BUS:] bus:sprite_y_store3 (bus) fan-out=11
```

### Path 10: depth 16 (80-240 ns, 201% half T-cycle)
```
[REGISTERED:dffr] muwy (ppu-stat)
  [half_add] fafo (ppu-bgscroll)
    [full_add] emux (ppu-bgscroll)
      [full_add] ecab (ppu-bgscroll)
        [full_add] etam (ppu-bgscroll)
          [not_if0] duho (ppu-bgscroll)
            [BUS:] bus:~ma5 (bus)
```


## VRAM Interface (37 paths, max depth 29)

### Path 1: depth 29 (145-435 ns, 365% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
                [and2] tuca (ppu-vram)
                  [mux] tole (ppu-vram)
                    [and2] sere (ppu-vram)
                      [and2] sazo (ppu-vram)
                        [not_x1] ryje (ppu-vram)
                          [not_x1] revo (ppu-vram)
                            [and2] rocy (ppu-vram)
                              [not_x3] rahu (ppu-vram) x3 fan-out=17
                                [not_x1] rove (ppu-vram)
                                  [and2] suke (ppu-vram)
                                    [not_x2] ryze (ppu-vram) x2
                                      [PAD:pad_bidir_pu] md7 (ppu-vram)
```

### Path 2: depth 29 (145-435 ns, 365% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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

### Path 3: depth 29 (145-435 ns, 365% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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

### Path 4: depth 29 (145-435 ns, 365% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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

### Path 5: depth 29 (145-435 ns, 365% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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

### Path 6: depth 29 (145-435 ns, 365% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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

### Path 7: depth 29 (145-435 ns, 365% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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

### Path 8: depth 29 (145-435 ns, 365% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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

### Path 9: depth 28 (140-420 ns, 352% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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

### Path 10: depth 28 (140-420 ns, 352% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [nor2] tefa (ppu-vram)
              [and2] sose (ppu-vram)
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


## Sprite X Priority (10 paths, max depth 27)

### Path 1: depth 27 (135-405 ns, 340% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
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
                              [or2] gyga (ppu-xprio)
                                [nor2] guze (ppu-xprio)
                                  [REGISTERED:dffr] fono (ppu-xprio)
```

### Path 2: depth 25 (125-375 ns, 315% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
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

### Path 3: depth 23 (115-345 ns, 289% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
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

### Path 4: depth 21 (105-315 ns, 264% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
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

### Path 5: depth 19 (95-285 ns, 239% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
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

### Path 6: depth 17 (85-255 ns, 214% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
          [nand3] ydug (ppu-xprio)
            [not_x1] wefu (ppu-xprio)
              [or2] geze (ppu-xprio)
                [or2] fuma (ppu-xprio)
                  [or2] gede (ppu-xprio)
                    [or2] wuto (ppu-xprio)
                      [nor2] gono (ppu-xprio)
                        [REGISTERED:dffr] xudy (ppu-xprio)
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
          [nand3] ydug (ppu-xprio)
            [not_x1] wefu (ppu-xprio)
              [or2] geze (ppu-xprio)
                [or2] fuma (ppu-xprio)
                  [or2] gede (ppu-xprio)
                    [nor2] gyfy (ppu-xprio)
                      [REGISTERED:dffr] gota (ppu-xprio)
```

### Path 8: depth 13 (65-195 ns, 164% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
          [nand3] ydug (ppu-xprio)
            [not_x1] wefu (ppu-xprio)
              [or2] geze (ppu-xprio)
                [or2] fuma (ppu-xprio)
                  [nor2] emol (ppu-xprio)
                    [REGISTERED:dffr] egav (ppu-xprio)
```

### Path 9: depth 11 (55-165 ns, 138% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
          [nand3] ydug (ppu-xprio)
            [not_x1] wefu (ppu-xprio)
              [or2] geze (ppu-xprio)
                [nor2] enut (ppu-xprio)
                  [REGISTERED:dffr] cedy (ppu-xprio)
```

### Path 10: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
          [nand3] ydug (ppu-xprio)
            [nor2] guva (ppu-xprio)
              [REGISTERED:dffr] eboj (ppu-xprio)
```


## Data Bus (16 paths, max depth 19)

### Path 1: depth 19 (95-285 ns, 239% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 2: depth 19 (95-285 ns, 239% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 3: depth 19 (95-285 ns, 239% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 4: depth 19 (95-285 ns, 239% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 5: depth 19 (95-285 ns, 239% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 6: depth 19 (95-285 ns, 239% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 7: depth 19 (95-285 ns, 239% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 8: depth 19 (95-285 ns, 239% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 9: depth 18 (90-270 ns, 227% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [not_x1] levo (bus-data)
              [ao21] lagu (bus-data)
                [not_x1] lywe (bus-data)
                  [or2] moty (bus-data)
                    [mux] roru (bus-adr) fan-out=10
                      [nor2] rogy (bus-data)
                        [PAD:pad_bidir_pu] d6 (bus-data)
```

### Path 10: depth 18 (90-270 ns, 227% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [and2] texo (bus-adr)
            [not_x1] levo (bus-data)
              [ao21] lagu (bus-data)
                [not_x1] lywe (bus-data)
                  [or2] moty (bus-data)
                    [mux] roru (bus-adr) fan-out=10
                      [nor2] ryda (bus-data)
                        [PAD:pad_bidir_pu] d7 (bus-data)
```


## DMA (2 paths, max depth 16)

### Path 1: depth 16 (80-240 ns, 201% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x2] dyky (ppu-control) x2
                    [not_x4] cupa (ppu-control) x4 fan-out=13
                      [and2] lavy (ppu-dma)
                        [nor2] lupa (ppu-dma)
                          [REGISTERED:dffr] luvy (ppu-dma)
```

### Path 2: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] mugu (ppu-dma)
  [nand6] navo (ppu-dma)
    [not_x1] nolo (ppu-dma)
      [REGISTERED:dffr] myte (ppu-dma)
```


## Timer (9 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [nand4] tope (timer)
                    [or2] muzu (timer)
                      [nand3] mexu (timer)
                        [REGISTERED:tffnl] nuga (timer)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [nand4] tope (timer)
                    [or2] muzu (timer)
                      [nand3] mexu (timer)
                        [REGISTERED:tffnl] peda (timer)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [nand4] tope (timer)
                    [or2] muzu (timer)
                      [nand3] mexu (timer)
                        [REGISTERED:tffnl] rage (timer)
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 8: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
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

### Path 9: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] nydu (timer)
  [nor2] mery (timer)
    [REGISTERED:dffr] moba (timer)
```


## apu-ch2 (22 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] agyn (apu-ch2)
                        [not_x1] aget (apu-ch2)
                          [REGISTERED:tffnl] akyd (apu-ch2)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] agyn (apu-ch2)
                        [not_x1] aget (apu-ch2)
                          [REGISTERED:tffnl] buva (apu-ch2)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] agyn (apu-ch2)
                        [not_x1] bymo (apu-ch2)
                          [REGISTERED:tffnl] came (apu-ch2)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] agyn (apu-ch2)
                        [not_x1] bymo (apu-ch2)
                          [REGISTERED:tffnl] conu (apu-ch2)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] agyn (apu-ch2)
                        [not_x1] bymo (apu-ch2)
                          [REGISTERED:tffnl] cera (apu-ch2)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] agyn (apu-ch2)
                        [not_x1] bymo (apu-ch2)
                          [REGISTERED:tffnl] eryc (apu-ch2)
```

### Path 7: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko (apu-ch2)
  [not_x1] etuk (apu-ch2)
    [not_x1] davu (apu-ch2)
      [nor2] duju (apu-ch2)
        [not_x1] cogu (apu-ch2)
          [REGISTERED:tffnl] cyvo (apu-ch2)
```

### Path 8: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko (apu-ch2)
  [not_x1] etuk (apu-ch2)
    [not_x1] davu (apu-ch2)
      [nor2] duju (apu-ch2)
        [not_x1] cogu (apu-ch2)
          [REGISTERED:tffnl] done (apu-ch2)
```

### Path 9: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko (apu-ch2)
  [not_x1] etuk (apu-ch2)
    [not_x1] davu (apu-ch2)
      [nor2] duju (apu-ch2)
        [not_x1] cogu (apu-ch2)
          [REGISTERED:tffnl] dynu (apu-ch2)
```

### Path 10: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko (apu-ch2)
  [not_x1] etuk (apu-ch2)
    [not_x1] davu (apu-ch2)
      [nor2] duju (apu-ch2)
        [not_x1] cogu (apu-ch2)
          [REGISTERED:tffnl] ezof (apu-ch2)
```


## apu-ch1 (39 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] boro (apu-ch1)
                        [not_x1] bugy (apu-ch1)
                          [REGISTERED:tffnl] bovy (apu-ch1)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] boro (apu-ch1)
                        [not_x1] bugy (apu-ch1)
                          [REGISTERED:tffnl] bacy (apu-ch1)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] boro (apu-ch1)
                        [not_x1] bepe (apu-ch1)
                          [REGISTERED:tffnl] cura (apu-ch1)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] boro (apu-ch1)
                        [not_x1] bugy (apu-ch1)
                          [REGISTERED:tffnl] cuno (apu-ch1)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] boro (apu-ch1)
                        [not_x1] bugy (apu-ch1)
                          [REGISTERED:tffnl] cavy (apu-ch1)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] boro (apu-ch1)
                        [not_x1] bepe (apu-ch1)
                          [REGISTERED:tffnl] eram (apu-ch1)
```

### Path 7: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] comy (apu-ch1)
  [not_x1] cyte (apu-ch1)
    [not_x1] cope (apu-ch1)
      [nor2] epyk (apu-ch1)
        [not_x1] dako (apu-ch1)
          [REGISTERED:tffnl] copu (apu-ch1)
```

### Path 8: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:drlatch_ee] avaf (apu-ch1)
  [not_x3] aryl (apu-ch1) x3 fan-out=14
    [xor] culu (apu-ch1)
      [REGISTERED:dffr_cc_q] deva (apu-ch1)
```

### Path 9: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:drlatch_ee] avaf (apu-ch1)
  [not_x3] aryl (apu-ch1) x3 fan-out=14
    [xor] cale (apu-ch1)
      [REGISTERED:dffr_cc_q] defa (apu-ch1)
```

### Path 10: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] comy (apu-ch1)
  [not_x1] cyte (apu-ch1)
    [not_x1] cope (apu-ch1)
      [nor2] epyk (apu-ch1)
        [not_x1] dega (apu-ch1)
          [REGISTERED:tffnl] ekov (apu-ch1)
```


## apu-ch4 (15 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] caze (apu-ch4)
                        [not_x1] dotu (apu-ch4)
                          [REGISTERED:tffnl] cedo (apu-ch4)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] caze (apu-ch4)
                        [not_x1] dotu (apu-ch4)
                          [REGISTERED:tffnl] dena (apu-ch4)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] caze (apu-ch4)
                        [not_x1] dotu (apu-ch4)
                          [REGISTERED:tffnl] dano (apu-ch4)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] caze (apu-ch4)
                        [not_x1] epek (apu-ch4)
                          [REGISTERED:tffnl] edop (apu-ch4)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] caze (apu-ch4)
                        [not_x1] dotu (apu-ch4)
                          [REGISTERED:tffnl] favy (apu-ch4)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] caze (apu-ch4)
                        [not_x1] epek (apu-ch4)
                          [REGISTERED:tffnl] fylo (apu-ch4)
```

### Path 7: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:tffnl] feko (apu-ch4)
  [nand5] cuty (apu-ch4)
    [not_x1] dubo (apu-ch4)
      [or2] evur (apu-ch4)
        [REGISTERED:dffr] fyno (apu-ch4)
```

### Path 8: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] hyro (apu-ch4)
  [xnor] hura (apu-ch4)
    [REGISTERED:dffr] joto (apu-ch4)
```

### Path 9: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] gone (apu-ch4) fan-out=14
  [nor2] enec (apu-ch4)
    [not_x1] dapy (apu-ch4)
      [REGISTERED:tffnl] cuna (apu-ch4)
```

### Path 10: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] gone (apu-ch4) fan-out=14
  [nor2] enec (apu-ch4)
    [not_x1] dapy (apu-ch4)
      [REGISTERED:tffnl] cofe (apu-ch4)
```


## apu-ch3 (24 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] dery (apu-ch3)
                        [not_x1] emut (apu-ch3)
                          [REGISTERED:tffnl] foro (apu-ch3)
```

### Path 2: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] dery (apu-ch3)
                        [not_x1] emut (apu-ch3)
                          [REGISTERED:tffnl] fave (apu-ch3)
```

### Path 3: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] dery (apu-ch3)
                        [not_x1] emut (apu-ch3)
                          [REGISTERED:tffnl] fyru (apu-ch3)
```

### Path 4: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] dery (apu-ch3)
                        [not_x1] gajy (apu-ch3)
                          [REGISTERED:tffnl] fory (apu-ch3)
```

### Path 5: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] dery (apu-ch3)
                        [not_x1] emut (apu-ch3)
                          [REGISTERED:tffnl] gemo (apu-ch3)
```

### Path 6: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] dery (apu-ch3)
                        [not_x1] gajy (apu-ch3)
                          [REGISTERED:tffnl] gevo (apu-ch3)
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] dery (apu-ch3)
                        [not_x1] gajy (apu-ch3)
                          [REGISTERED:tffnl] gatu (apu-ch3)
```

### Path 8: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [nand2] arev (clocks)
            [not_x3] apov (clocks) x3
              [muxi] ubal (bus-data)
                [not_x3] tapu (bus-data) x3 fan-out=13
                  [not_x1] bafu (apu-control)
                    [not_x6] bogy (apu-control) x6 fan-out=37
                      [nand2] dery (apu-ch3)
                        [not_x1] gajy (apu-ch3)
                          [REGISTERED:tffnl] gapo (apu-ch3)
```

### Path 9: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] davo (apu-ch3)
  [not_x2] coka (apu-ch3) x2 fan-out=13
    [mux] bole (apu-ch3)
      [not_x1] ydod (apu-ch3)
        [and2] ygef (apu-ch3)
          [BOUNDARY:wave_ram] wave_ram () fan-out=16
```

### Path 10: depth 6 (30-90 ns, 76% half T-cycle)
```
[REGISTERED:dffr] davo (apu-ch3)
  [not_x2] coka (apu-ch3) x2 fan-out=13
    [mux] agyl (apu-ch3)
      [and2] yjej (apu-ch3)
        [BOUNDARY:wave_ram] wave_ram () fan-out=16
```


## Address Bus (16 paths, max depth 15)

### Path 1: depth 15 (75-225 ns, 189% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [or3] taba (clocks)
        [sm83] cpu () fan-out=42
          [oa21] agut (clocks)
            [nor2] awod (clocks)
              [not_x3] abuz (clocks) x3
                [nand2] sepy (bus-adr)
                  [mux] tazy (bus-adr)
                    [nor2] rulo (bus-adr)
                      [PAD:pad_bidir] a15 (bus-adr)
```

### Path 2: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] amet (bus-adr)
              [nand2] kupo (bus-adr)
                [PAD:pad_bidir] a0 (bus-adr)
```

### Path 3: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] pege (bus-adr)
              [nand2] puhe (bus-adr)
                [PAD:pad_bidir] a14 (bus-adr)
```

### Path 4: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] muce (bus-adr)
              [nor2] leva (bus-adr)
                [PAD:pad_bidir] a13 (bus-adr)
```

### Path 5: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] mojy (bus-adr)
              [nor2] loso (bus-adr)
                [PAD:pad_bidir] a12 (bus-adr)
```

### Path 6: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] male (bus-adr)
              [nor2] lyny (bus-adr)
                [PAD:pad_bidir] a11 (bus-adr)
```

### Path 7: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] pamy (bus-adr)
              [nor2] rore (bus-adr)
                [PAD:pad_bidir] a10 (bus-adr)
```

### Path 8: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] masu (bus-adr)
              [nand2] mune (bus-adr)
                [PAD:pad_bidir] a9 (bus-adr)
```

### Path 9: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] mano (bus-adr)
              [nor2] mego (bus-adr)
                [PAD:pad_bidir] a8 (bus-adr)
```

### Path 10: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru (ppu-dma)
  [not_x1] lebu (ppu-dma)
    [nor3] muda (ppu-dma)
      [not_x1] logo (ppu-dma)
        [nand2] mory (ppu-dma)
          [not_x1] luma (ppu-dma) fan-out=20
            [mux] asur (bus-adr)
              [nor2] colo (bus-adr)
                [PAD:pad_bidir] a7 (bus-adr)
```


## Sprite Y Compare (3 paths, max depth 14)

### Path 1: depth 14 (70-210 ns, 176% half T-cycle)
```
[REGISTERED:dffr] nopa (ppu-cycles)
  [and2] nuny (ppu-cycles)
    [nor2] puku (ppu-cycles)
      [nor3] rydy (ppu-cycles)
        [not_x1] sylo (ppu-cycles)
          [nand2] tuxy (ppu-cycles)
            [not_x2] suzu (ppu-cycles) x2
              [or3] tevo (ppu-cycles)
                [nor3] nyxu (ppu-cycles)
                  [nand3] moce (ppu-cycles)
                    [not_x1] lyry (ppu-cycles)
                      [and4] teky (ppu-ycomp)
                        [REGISTERED:dffr] sobu (ppu-ycomp)
```

### Path 2: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:dffr] toxe (ppu-ycomp)
  [not_x1] tytu (ppu-ycomp)
    [nand2] tacu (ppu-ycomp)
      [and2] vape (ppu-oam)
        [not_x1] xujy (ppu-oam)
          [nand3] bycu (ppu-oam)
            [not_x2] cota (ppu-oam) x2
              [not_x2] wovu (ppu-oam) x2
                [BOUNDARY:oam] oam_a ()
```

### Path 3: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:dffr] toxe (ppu-ycomp)
  [not_x1] tytu (ppu-ycomp)
    [nand2] tacu (ppu-ycomp)
      [and2] vape (ppu-oam)
        [not_x1] xujy (ppu-oam)
          [nand3] bycu (ppu-oam)
            [not_x2] cota (ppu-oam) x2
              [not_x2] wovu (ppu-oam) x2
                [BOUNDARY:oam] oam_b ()
```


## LCD Output (11 paths, max depth 14)

### Path 1: depth 14 (70-210 ns, 176% half T-cycle)
```
[REGISTERED:dffsr] pybo (ppu-bgfifo)
  [and2] rajy (ppu-mux)
    [and2] ryfu (ppu-mux)
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
[REGISTERED:dffsr] pybo (ppu-bgfifo)
  [and2] rajy (ppu-mux)
    [and2] ryfu (ppu-mux)
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

### Path 4: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] rutu (ppu-lcd)
  [not_x3] pure (ppu-lcd) x3
    [not_x1] kasa (ppu-lcd)
      [ao22] kahe (ppu-lcd)
        [not_x3] kymo (ppu-lcd) x3
          [PAD:pad_out] cpl (ppu-lcd)
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
[REGISTERED:dffr] lydo (ppu-stat)
  [and4] noko (ppu-lcd)
    [REGISTERED:dffr] myta (ppu-lcd)
```

### Path 8: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] lovu (ppu-stat)
  [and2] xyvo (ppu-lcd)
    [REGISTERED:dffr] popu (ppu-lcd)
```

### Path 9: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] saxo (ppu-lcd)
  [and4] sanu (ppu-lcd)
    [REGISTERED:dffr] rutu (ppu-lcd)
```

### Path 10: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] lexa (ppu-stat)
  [nor8] neru (ppu-lcd)
    [REGISTERED:dffr] meda (ppu-lcd)
```


## STAT/LY (8 paths, max depth 13)

### Path 1: depth 13 (65-195 ns, 164% half T-cycle)
```
[REGISTERED:dffr] ceno (ppu-objctl)
  [not_x2] ceha (ppu-objctl) x2
    [not_x1] byjo (ppu-objctl)
      [and2] azem (ppu-objctl)
        [and2] aror (ppu-xprio) fan-out=10
          [nand3] dyka (ppu-xprio)
            [nand5] fove (ppu-xprio)
              [or2] fepo (ppu-xprio)
                [not_x1] xena (ppu-stat)
                  [and2] wodu (ppu-stat)
                    [REGISTERED:dffr] voga (ppu-stat)
```

### Path 2: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [and2] tyba (ppu-stat)
    [and2] sury (ppu-stat)
      [xor] roku (ppu-stat)
        [REGISTERED:dffr] sybe (ppu-stat)
```

### Path 3: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] savy (ppu-stat)
  [and2] xuke (ppu-stat)
    [and2] xyle (ppu-stat)
      [xor] xora (ppu-stat)
        [REGISTERED:dffr] xydo (ppu-stat)
```

### Path 4: depth 6 (30-90 ns, 76% half T-cycle)
```
[REGISTERED:dffr] lexa (ppu-stat)
  [xor] reda (ppu-stat)
    [nor4] subo (ppu-stat)
      [nand2] rape (ppu-stat)
        [not_x1] paly (ppu-stat)
          [REGISTERED:dffr] ropo (ppu-stat)
```

### Path 5: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [and2] tyba (ppu-stat)
    [xor] tyge (ppu-stat)
      [REGISTERED:dffr] tako (ppu-stat)
```

### Path 6: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] savy (ppu-stat)
  [and2] xuke (ppu-stat)
    [xor] xegy (ppu-stat)
      [REGISTERED:dffr] xodu (ppu-stat)
```

### Path 7: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] savy (ppu-stat)
  [xor] rybo (ppu-stat)
    [REGISTERED:dffr] savy (ppu-stat)
```

### Path 8: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] tuhu (ppu-stat)
  [xor] sake (ppu-stat)
    [REGISTERED:dffr] tuky (ppu-stat)
```


## Sprite Pixel Shifter (16 paths, max depth 9)

### Path 1: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pono (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] mytu (ppu-objfifo)
```

### Path 2: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pono (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] mofo (ppu-objfifo)
```

### Path 3: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pobe (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] pudu (ppu-objfifo)
```

### Path 4: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pute (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] pefo (ppu-objfifo)
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
          [mux] puly (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] rydu (ppu-objfifo)
```

### Path 7: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pawe (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] rama (ppu-objfifo)
```

### Path 8: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pobe (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] ramu (ppu-objfifo)
```

### Path 9: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pute (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] rewo (ppu-objfifo)
```

### Path 10: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly (ppu-ycomp)
  [nor2] saky (ppu-ycomp)
    [or2] tyso (ppu-ycomp)
      [not_x2] texy (ppu-ycomp) x2
        [and2] xono (ppu-objfifo)
          [mux] pelo (ppu-objfifo)
            [REGISTERED:dlatch_ee_q] roka (ppu-objfifo)
```


## BG/Win Cycles (3 paths, max depth 8)

### Path 1: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:drlatch_ee] mypu (ppu-window)
  [xnor] nezo (ppu-window)
    [nand5] puky (ppu-window)
      [not_x1] nufa (ppu-window)
        [nand5] nogy (ppu-window)
          [not_x1] nuko (ppu-window)
            [nor2] pany (ppu-cycles)
              [REGISTERED:dffr] ryfa (ppu-cycles)
```

### Path 2: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:drlatch_ee] mypu (ppu-window)
  [xnor] nezo (ppu-window)
    [nand5] puky (ppu-window)
      [not_x1] nufa (ppu-window)
        [nand5] nogy (ppu-window)
          [not_x1] nuko (ppu-window)
            [REGISTERED:dffr] pyco (ppu-cycles)
```

### Path 3: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] roga (ppu-cycles)
  [xnor] syby (ppu-cycles)
    [nand4] rone (ppu-cycles)
      [not_x1] pohu (ppu-cycles)
        [REGISTERED:dffr] puxa (ppu-cycles)
```


## Window Logic (1 paths, max depth 7)

### Path 1: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] lafo (ppu-stat)
  [xnor] nupa (ppu-window)
    [nand5] palo (ppu-window)
      [not_x1] nele (ppu-window)
        [nand5] pafu (ppu-window)
          [not_x1] roge (ppu-window)
            [REGISTERED:dffr] sary (ppu-window)
```


## apu-control (1 paths, max depth 5)

### Path 1: depth 5 (25-75 ns, 63% half T-cycle)
```
[PAD:pad_in] t1 (test)
  [not_x1] ubet (test)
    [and2] unor (test) fan-out=34
      [and2] efop (apu-control)
        [REGISTERED:drlatch_ee] fero (apu-control)
```


## Joypad (12 paths, max depth 3)

### Path 1: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [not_x1] kura (test)
    [or2] cela (joypad)
      [PAD:pad_out_diff] p15 (joypad)
```

### Path 2: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [not_x1] kura (test)
    [or2] karu (joypad)
      [PAD:pad_out_diff] p14 (joypad)
```

### Path 3: depth 2 (10-30 ns, 25% half T-cycle)
```
[PAD:pad_bidir_pu] p10 (joypad)
  [or4] kery (joypad)
    [REGISTERED:dlatch] awob (joypad)
```

### Path 4: depth 2 (10-30 ns, 25% half T-cycle)
```
[PAD:pad_bidir_pu] p10 (joypad)
  [or4] kery (joypad)
    [REGISTERED:dffr] batu (joypad)
```

### Path 5: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [not_x1] kura (test)
    [nor2] kybu (test)
      [PAD:pad_bidir_pu] p10 (joypad)
```

### Path 6: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [not_x1] kura (test)
    [nor2] kabu (test)
      [PAD:pad_bidir_pu] p11 (joypad)
```

### Path 7: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [not_x1] kura (test)
    [nor2] kasy (test)
      [PAD:pad_bidir_pu] p12 (joypad)
```

### Path 8: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [not_x1] kura (test)
    [nor2] kale (test)
      [PAD:pad_bidir_pu] p13 (joypad)
```

### Path 9: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [nand2] kole (test)
    [PAD:pad_bidir_pu] p10 (joypad)
```

### Path 10: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [nand2] kyto (test)
    [PAD:pad_bidir_pu] p11 (joypad)
```


## bootrom (1 paths, max depth 2)

### Path 1: depth 2 (10-30 ns, 25% half T-cycle)
```
[BUS:] bus:d0 (bus) fan-out=46
  [or2] sato (bootrom)
    [REGISTERED:dffr] tepu (bootrom)
```


## Serial (4 paths, max depth 2)

### Path 1: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] elys (serial)
  [muxi] kena (serial)
    [PAD:pad_out] sout (serial)
```

### Path 2: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [not_x1] jeva (test)
    [nor2] kywe (test)
      [PAD:pad_bidir_pu] sin (serial)
```

### Path 3: depth 1 (5-15 ns, 13% half T-cycle)
```
[PAD:pad_bidir_pu] sin (serial)
  [not_x1] cage (serial)
    [REGISTERED:dffsr] cuba (serial)
```

### Path 4: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] buro (test)
  [nand2] kore (test)
    [PAD:pad_bidir_pu] sin (serial)
```


## Sprite X Match (80 paths, max depth 1)

### Path 1: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] depo (ppu-xcomp) fan-out=17
  [not_x1] bady (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] cusy (ppu-xcomp)
```

### Path 2: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] baxo (ppu-xcomp)
  [not_x1] arop (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] ceso (ppu-xcomp)
```

### Path 3: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] gomo (ppu-xcomp) fan-out=17
  [not_x1] cose (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] cywe (ppu-xcomp)
```

### Path 4: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] depo (ppu-xcomp) fan-out=17
  [not_x1] bady (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] cuvy (ppu-xcomp)
```

### Path 5: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] gomo (ppu-xcomp) fan-out=17
  [not_x1] cose (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] dake (ppu-xcomp)
```

### Path 6: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] yzos (ppu-xcomp)
  [not_x1] xatu (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] dyfu (ppu-xcomp)
```

### Path 7: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] zezy (ppu-xcomp)
  [not_x1] yvok (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] dazo (ppu-xcomp)
```

### Path 8: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] yzos (ppu-xcomp)
  [not_x1] xatu (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] dury (ppu-xcomp)
```

### Path 9: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] zyve (ppu-xcomp)
  [not_x1] ypur (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] desu (ppu-xcomp)
```

### Path 10: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] zyty (ppu-xcomp)
  [not_x1] zocy (ppu-xcomp) fan-out=10
    [REGISTERED:drlatch_ee] duko (ppu-xcomp)
```


## OAM Interface (6 paths, max depth 1)

### Path 1: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a2}_tri (bus)
  [not_x1] yfot (ppu-oam)
    [REGISTERED:dffr_cc] xadu (ppu-oam)
```

### Path 2: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a3}_tri (bus)
  [not_x1] yfoc (ppu-oam)
    [REGISTERED:dffr_cc] xedy (ppu-oam)
```

### Path 3: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a5}_tri (bus)
  [not_x1] ymev (ppu-oam)
    [REGISTERED:dffr_cc] xobe (ppu-oam)
```

### Path 4: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a7}_tri (bus)
  [not_x1] yzet (ppu-oam)
    [REGISTERED:dffr_cc] xecu (ppu-oam)
```

### Path 5: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a6}_tri (bus)
  [not_x1] xemu (ppu-oam)
    [REGISTERED:dffr_cc] yduf (ppu-oam)
```

### Path 6: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a4}_tri (bus)
  [not_x1] yvom (ppu-oam)
    [REGISTERED:dffr_cc] zuze (ppu-oam)
```
