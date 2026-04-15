# Operational Critical Paths by Functional Area


## Bus (689 paths, max depth 103.08)

### Path 1: depth 103.08 (515.4-1546.2 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control x2
                  [not_if0] buzu  — APU Control
                    [BUS:] bus:d0  — CPU data bus D0 fan-out=46
```

### Path 2: depth 103.08 (515.4-1546.2 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control x2
                  [not_if0] capu  — APU Control
                    [BUS:] bus:d1  — CPU data bus D1 fan-out=44
```

### Path 3: depth 103.08 (515.4-1546.2 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control x2
                  [not_if0] caga  — APU Control
                    [BUS:] bus:d2  — CPU data bus D2 fan-out=43
```

### Path 4: depth 103.08 (515.4-1546.2 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control x2
                  [not_if0] boca  — APU Control
                    [BUS:] bus:d3  — CPU data bus D3 fan-out=39
```

### Path 5: depth 103.08 (515.4-1546.2 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control x2
                  [not_if0] cavu  — APU Control
                    [BUS:] bus:d4  — CPU data bus D4 fan-out=40
```

### Path 6: depth 103.08 (515.4-1546.2 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control x2
                  [not_if0] cudu  — APU Control
                    [BUS:] bus:d5  — CPU data bus D5 fan-out=39
```

### Path 7: depth 103.08 (515.4-1546.2 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control x2
                  [not_if0] cada  — APU Control
                    [BUS:] bus:d6  — CPU data bus D6 fan-out=41
```

### Path 8: depth 103.08 (515.4-1546.2 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cora  — APU Decode
            [not_x1] gepa  — APU Control
              [nor2] hefa  — APU Control
                [not_x2] gumu  — APU Control x2
                  [not_if0] cere  — APU Control
                    [BUS:] bus:d7  — CPU data bus D7 fan-out=41
```

### Path 9: depth 103.03 (515.15-1545.45 ns, 1297% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cuge  — APU Decode
            [nand2] bare  — CH4
              [not_if0] cury  — CH4
                [BUS:] bus:d6  — CPU data bus D6 fan-out=41
```

### Path 10: depth 101.75 (508.75-1526.25 ns, 1280% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] cuge  — APU Decode
            [nand2] bagu  — CH4
              [not_if0] atel  — CH4
                [BUS:] bus:d0  — CPU data bus D0 fan-out=46
```


## LCD Output (10 paths, max depth 71.24000000000001)

### Path 1: depth 71.24000000000001 (356.20000000000005-1068.6000000000001 ns, 896% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [nand5] fefy  — Sprite X Priority
              [or2] fepo  — Sprite X Priority
                [not_x1] xena  — STAT/LY
                  [and2] wodu  — STAT/LY
                    [nor3] vybo  — BG/Win Cycles
                      [and3] tyfa  — BG/Win Cycles
                        [not_x4] segu  — BG/Win Cycles x4
                          [or2] sacu  — Pixel Shift Clock (CLKPIPE) fan-out=53
                            [and2] toba  — BG/Win Cycles
                              [or2] semu  — BG/Win Cycles
                                [not_x3] rypo  — BG/Win Cycles x3
                                  [PAD:pad_out] cp  — LCD
```

### Path 2: depth 54.34 (271.70000000000005-815.1 ns, 684% half T-cycle)
```
[REGISTERED:dffsr] wufy  — Sprite FIFO
  [and2] xula  — Pixel Mux
    [nor2] nuly  — Pixel Mux
      [nor3] poka  — Pixel Mux
        [nand2] lafu  — Pixel Mux
          [not_x1] lava  — Pixel Mux
            [and3] volo  — Pixel Mux
              [ao2222] waly  — Pixel Mux
                [or3] pero  — Pixel Mux
                  [not_x2] remy  — Pixel Mux x2
                    [PAD:pad_out] ld0  — LCD
```

### Path 3: depth 53.65 (268.25-804.75 ns, 675% half T-cycle)
```
[REGISTERED:dffsr] wufy  — Sprite FIFO
  [and2] xula  — Pixel Mux
    [nor2] nuly  — Pixel Mux
      [nor3] poka  — Pixel Mux
        [nand2] lafu  — Pixel Mux
          [not_x1] lava  — Pixel Mux
            [and3] volo  — Pixel Mux
              [ao2222] wufu  — Pixel Mux
                [or3] paty  — Pixel Mux
                  [not_x2] ravo  — Pixel Mux x2
                    [PAD:pad_out] ld1  — LCD
```

### Path 4: depth 10.49 (52.45-157.35 ns, 132% half T-cycle)
```
[REGISTERED:dffr] rutu  — LCD
  [or2] ryno  — LCD
    [not_x2] pogu  — LCD x2
      [PAD:pad_out] cpg  — LCD
```

### Path 5: depth 8.37 (41.849999999999994-125.54999999999998 ns, 105% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [and2] xyvo  — LCD
    [REGISTERED:dffr] popu  — LCD
```

### Path 6: depth 8.18 (40.9-122.69999999999999 ns, 103% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [nor8] neru  — LCD
    [REGISTERED:dffr] meda  — LCD
```

### Path 7: depth 7.93 (39.65-118.94999999999999 ns, 100% half T-cycle)
```
[REGISTERED:dffr] telu  — LCD
  [not_x1] vate  — LCD
    [nand7] tozu  — LCD
      [nand4] tegy  — LCD
        [REGISTERED:dffr] sygu  — LCD
```

### Path 8: depth 5.18 (25.9-77.69999999999999 ns, 65% half T-cycle)
```
[REGISTERED:dffr] meda  — LCD
  [not_x3] mure  — LCD x3
    [PAD:pad_out] s  — LCD
```

### Path 9: depth 3.25 (16.25-48.75 ns, 41% half T-cycle)
```
[REGISTERED:dffr] saxo  — LCD
  [and4] sanu  — LCD
    [REGISTERED:dffr] rutu  — LCD
```

### Path 10: depth 2.48 (12.4-37.2 ns, 31% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [and4] noko  — LCD
    [REGISTERED:dffr] myta  — LCD
```


## Timer (17 paths, max depth 70.96000000000001)

### Path 1: depth 70.96000000000001 (354.80000000000007-1064.4 ns, 893% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [or2] muzu  — Timer
            [nand3] mexu  — Timer
              [REGISTERED:tffnl] nuga  — Timer
```

### Path 2: depth 70.96000000000001 (354.80000000000007-1064.4 ns, 893% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [or2] muzu  — Timer
            [nand3] mexu  — Timer
              [REGISTERED:tffnl] peda  — Timer
```

### Path 3: depth 70.96000000000001 (354.80000000000007-1064.4 ns, 893% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [or2] muzu  — Timer
            [nand3] mexu  — Timer
              [REGISTERED:tffnl] peru  — Timer
```

### Path 4: depth 70.96000000000001 (354.80000000000007-1064.4 ns, 893% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [or2] muzu  — Timer
            [nand3] mexu  — Timer
              [REGISTERED:tffnl] povy  — Timer
```

### Path 5: depth 70.96000000000001 (354.80000000000007-1064.4 ns, 893% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [or2] muzu  — Timer
            [nand3] mexu  — Timer
              [REGISTERED:tffnl] rage  — Timer
```

### Path 6: depth 70.96000000000001 (354.80000000000007-1064.4 ns, 893% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [or2] muzu  — Timer
            [nand3] mexu  — Timer
              [REGISTERED:tffnl] rate  — Timer
```

### Path 7: depth 70.96000000000001 (354.80000000000007-1064.4 ns, 893% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [or2] muzu  — Timer
            [nand3] mexu  — Timer
              [REGISTERED:tffnl] rega  — Timer
```

### Path 8: depth 70.96000000000001 (354.80000000000007-1064.4 ns, 893% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [or2] muzu  — Timer
            [nand3] mexu  — Timer
              [REGISTERED:tffnl] ruby  — Timer
```

### Path 9: depth 66.8 (334.0-1002.0 ns, 841% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [muxi] rato  — Timer
            [nor2] pagu  — Timer
              [REGISTERED:tffnl] nuga  — Timer
```

### Path 10: depth 66.05000000000001 (330.25000000000006-990.7500000000002 ns, 831% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [and3] ryfo  — Timer
        [nand4] tope  — Timer
          [muxi] petu  — Timer
            [nor2] nero  — Timer
              [REGISTERED:tffnl] povy  — Timer
```


## APU CH4 (Noise) (17 paths, max depth 66.15)

### Path 1: depth 66.15 (330.75-992.2500000000001 ns, 832% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] danu  — APU Decode
            [nand2] caze  — CH4
              [not_x1] dotu  — CH4
                [REGISTERED:tffnl] cedo  — CH4
```

### Path 2: depth 66.15 (330.75-992.2500000000001 ns, 832% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] danu  — APU Decode
            [nand2] caze  — CH4
              [not_x1] dotu  — CH4
                [REGISTERED:tffnl] dano  — CH4
```

### Path 3: depth 66.15 (330.75-992.2500000000001 ns, 832% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] danu  — APU Decode
            [nand2] caze  — CH4
              [not_x1] dotu  — CH4
                [REGISTERED:tffnl] dena  — CH4
```

### Path 4: depth 66.15 (330.75-992.2500000000001 ns, 832% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] danu  — APU Decode
            [nand2] caze  — CH4
              [not_x1] dotu  — CH4
                [REGISTERED:tffnl] favy  — CH4
```

### Path 5: depth 63.53000000000001 (317.65000000000003-952.9500000000002 ns, 799% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] danu  — APU Decode
            [nand2] caze  — CH4
              [not_x1] epek  — CH4
                [REGISTERED:tffnl] edop  — CH4
```

### Path 6: depth 63.53000000000001 (317.65000000000003-952.9500000000002 ns, 799% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [or2] bezy  — APU Decode
          [nor2] danu  — APU Decode
            [nand2] caze  — CH4
              [not_x1] epek  — CH4
                [REGISTERED:tffnl] fylo  — CH4
```

### Path 7: depth 8.49 (42.45-127.35000000000001 ns, 107% half T-cycle)
```
[REGISTERED:dffr] fosy  — CH4
  [nor2] enec  — CH4
    [not_x1] dapy  — CH4
      [REGISTERED:tffnl] cofe  — CH4
```

### Path 8: depth 8.49 (42.45-127.35000000000001 ns, 107% half T-cycle)
```
[REGISTERED:dffr] fosy  — CH4
  [nor2] enec  — CH4
    [not_x1] dapy  — CH4
      [REGISTERED:tffnl] cuna  — CH4
```

### Path 9: depth 8.49 (42.45-127.35000000000001 ns, 107% half T-cycle)
```
[REGISTERED:dffr] fosy  — CH4
  [nor2] enec  — CH4
    [not_x1] dapy  — CH4
      [REGISTERED:tffnl] dogo  — CH4
```

### Path 10: depth 6.51 (32.55-97.64999999999999 ns, 82% half T-cycle)
```
[REGISTERED:tffnl] cofe  — CH4
  [and3] ejex  — CH4
    [REGISTERED:dffr] fosy  — CH4
```


## Data Bus (24 paths, max depth 64.49)

### Path 1: depth 64.49 (322.45-967.3499999999999 ns, 812% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [not_x1] lula fan-out=16
                [nand2] ruxa
                  [PAD:pad_bidir_pu] d0
```

### Path 2: depth 63.51 (317.55-952.65 ns, 799% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [not_x1] lula fan-out=16
                [nand2] ruja
                  [PAD:pad_bidir_pu] d1
```

### Path 3: depth 61.699999999999996 (308.5-925.4999999999999 ns, 776% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [not_x1] lula fan-out=16
                [nand2] raby
                  [PAD:pad_bidir_pu] d2
```

### Path 4: depth 61.00999999999999 (305.04999999999995-915.1499999999999 ns, 768% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [nor2] rune
                [PAD:pad_bidir_pu] d0
```

### Path 5: depth 60.94 (304.7-914.0999999999999 ns, 767% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [not_x1] lula fan-out=16
                [nand2] rera
                  [PAD:pad_bidir_pu] d3
```

### Path 6: depth 59.74999999999999 (298.74999999999994-896.2499999999999 ns, 752% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [not_x1] lula fan-out=16
                [nand2] rory
                  [PAD:pad_bidir_pu] d4
```

### Path 7: depth 59.459999999999994 (297.29999999999995-891.8999999999999 ns, 748% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [not_x1] lula fan-out=16
                [nand2] rafy
                  [PAD:pad_bidir_pu] d6
```

### Path 8: depth 58.72999999999999 (293.65-880.9499999999998 ns, 739% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [nor2] rypu
                [PAD:pad_bidir_pu] d1
```

### Path 9: depth 58.65 (293.25-879.75 ns, 738% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [not_x1] lula fan-out=16
                [nand2] ryvo
                  [PAD:pad_bidir_pu] d5
```

### Path 10: depth 58.209999999999994 (291.04999999999995-873.1499999999999 ns, 733% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x1] redu
            [mux] roru fan-out=10
              [not_x1] lula fan-out=16
                [nand2] ravu
                  [PAD:pad_bidir_pu] d7
```


## APU CH2 (Square) (23 paths, max depth 60.7)

### Path 1: depth 60.7 (303.5-910.5 ns, 764% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] covy  — APU Decode
              [nand2] agyn  — CH2
                [not_x1] bymo  — CH2
                  [REGISTERED:tffnl] came  — CH2
```

### Path 2: depth 60.7 (303.5-910.5 ns, 764% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] covy  — APU Decode
              [nand2] agyn  — CH2
                [not_x1] bymo  — CH2
                  [REGISTERED:tffnl] cera  — CH2
```

### Path 3: depth 60.7 (303.5-910.5 ns, 764% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] covy  — APU Decode
              [nand2] agyn  — CH2
                [not_x1] bymo  — CH2
                  [REGISTERED:tffnl] conu  — CH2
```

### Path 4: depth 60.7 (303.5-910.5 ns, 764% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] covy  — APU Decode
              [nand2] agyn  — CH2
                [not_x1] bymo  — CH2
                  [REGISTERED:tffnl] eryc  — CH2
```

### Path 5: depth 57.540000000000006 (287.70000000000005-863.1000000000001 ns, 724% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] covy  — APU Decode
              [nand2] agyn  — CH2
                [not_x1] aget  — CH2
                  [REGISTERED:tffnl] akyd  — CH2
```

### Path 6: depth 57.540000000000006 (287.70000000000005-863.1000000000001 ns, 724% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] covy  — APU Decode
              [nand2] agyn  — CH2
                [not_x1] aget  — CH2
                  [REGISTERED:tffnl] buva  — CH2
```

### Path 7: depth 21.060000000000002 (105.30000000000001-315.90000000000003 ns, 265% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] cogu  — CH2
          [REGISTERED:tffnl] cyvo  — CH2
```

### Path 8: depth 21.060000000000002 (105.30000000000001-315.90000000000003 ns, 265% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] cogu  — CH2
          [REGISTERED:tffnl] done  — CH2
```

### Path 9: depth 21.060000000000002 (105.30000000000001-315.90000000000003 ns, 265% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] cogu  — CH2
          [REGISTERED:tffnl] dynu  — CH2
```

### Path 10: depth 21.060000000000002 (105.30000000000001-315.90000000000003 ns, 265% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] cogu  — CH2
          [REGISTERED:tffnl] ezof  — CH2
```


## APU CH1 (Square+Sweep) (42 paths, max depth 59.620000000000005)

### Path 1: depth 59.620000000000005 (298.1-894.3000000000001 ns, 750% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] caxe  — APU Decode
              [nand2] boro  — CH1
                [not_x1] bepe  — CH1
                  [REGISTERED:tffnl] cura  — CH1
```

### Path 2: depth 59.620000000000005 (298.1-894.3000000000001 ns, 750% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] caxe  — APU Decode
              [nand2] boro  — CH1
                [not_x1] bepe  — CH1
                  [REGISTERED:tffnl] eram  — CH1
```

### Path 3: depth 58.86000000000001 (294.3-882.9000000000001 ns, 741% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] caxe  — APU Decode
              [nand2] boro  — CH1
                [not_x1] bugy  — CH1
                  [REGISTERED:tffnl] bacy  — CH1
```

### Path 4: depth 58.86000000000001 (294.3-882.9000000000001 ns, 741% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] caxe  — APU Decode
              [nand2] boro  — CH1
                [not_x1] bugy  — CH1
                  [REGISTERED:tffnl] bovy  — CH1
```

### Path 5: depth 58.86000000000001 (294.3-882.9000000000001 ns, 741% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] caxe  — APU Decode
              [nand2] boro  — CH1
                [not_x1] bugy  — CH1
                  [REGISTERED:tffnl] cavy  — CH1
```

### Path 6: depth 58.86000000000001 (294.3-882.9000000000001 ns, 741% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] caxe  — APU Decode
              [nand2] boro  — CH1
                [not_x1] bugy  — CH1
                  [REGISTERED:tffnl] cuno  — CH1
```

### Path 7: depth 19.16 (95.8-287.4 ns, 241% half T-cycle)
```
[REGISTERED:dffr] comy  — CH1
  [not_x1] cyte  — CH1
    [not_x1] cope  — CH1
      [nor2] epyk  — CH1
        [not_x1] dega  — CH1
          [REGISTERED:tffnl] ekov  — CH1
```

### Path 8: depth 19.16 (95.8-287.4 ns, 241% half T-cycle)
```
[REGISTERED:dffr] comy  — CH1
  [not_x1] cyte  — CH1
    [not_x1] cope  — CH1
      [nor2] epyk  — CH1
        [not_x1] dega  — CH1
          [REGISTERED:tffnl] feva  — CH1
```

### Path 9: depth 19.16 (95.8-287.4 ns, 241% half T-cycle)
```
[REGISTERED:dffr] comy  — CH1
  [not_x1] cyte  — CH1
    [not_x1] cope  — CH1
      [nor2] epyk  — CH1
        [not_x1] dega  — CH1
          [REGISTERED:tffnl] hyke  — CH1
```

### Path 10: depth 19.16 (95.8-287.4 ns, 241% half T-cycle)
```
[REGISTERED:dffr] comy  — CH1
  [not_x1] cyte  — CH1
    [not_x1] cope  — CH1
      [nor2] epyk  — CH1
        [not_x1] dega  — CH1
          [REGISTERED:tffnl] jema  — CH1
```


## DMA (2 paths, max depth 57.6)

### Path 1: depth 57.6 (288.0-864.0 ns, 725% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [nand3] wutu  — PPU Decode
        [not_x2] wero  — PPU Decode x2 fan-out=12
          [nand5] wate  — PPU Decode
            [not_x2] xeda  — PPU Decode x2
              [and2] lavy  — DMA
                [nor2] lupa  — DMA
                  [REGISTERED:dffr] luvy  — DMA
```

### Path 2: depth 3.3699999999999997 (16.849999999999998-50.55 ns, 42% half T-cycle)
```
[REGISTERED:dffr] mugu  — DMA
  [nand6] navo  — DMA
    [not_x1] nolo  — DMA
      [REGISTERED:dffr] myte  — DMA
```


## VRAM Interface (37 paths, max depth 56.34)

### Path 1: depth 56.34 (281.70000000000005-845.1 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [or2] rela  — VRAM
                        [not_x1] rena  — VRAM
                          [not_x2] rofa  — VRAM x2
                            [PAD:pad_bidir_pu] md0  — VRAM
```

### Path 2: depth 56.34 (281.70000000000005-845.1 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [or2] rela  — VRAM
                        [not_x1] rena  — VRAM
                          [not_x2] rofa  — VRAM x2
                            [PAD:pad_bidir_pu] md1  — VRAM
```

### Path 3: depth 56.34 (281.70000000000005-845.1 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [or2] rela  — VRAM
                        [not_x1] rena  — VRAM
                          [not_x2] rofa  — VRAM x2
                            [PAD:pad_bidir_pu] md2  — VRAM
```

### Path 4: depth 56.34 (281.70000000000005-845.1 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [or2] rela  — VRAM
                        [not_x1] rena  — VRAM
                          [not_x2] rofa  — VRAM x2
                            [PAD:pad_bidir_pu] md3  — VRAM
```

### Path 5: depth 56.34 (281.70000000000005-845.1 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [or2] rela  — VRAM
                        [not_x1] rena  — VRAM
                          [not_x2] rofa  — VRAM x2
                            [PAD:pad_bidir_pu] md4  — VRAM
```

### Path 6: depth 56.34 (281.70000000000005-845.1 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [or2] rela  — VRAM
                        [not_x1] rena  — VRAM
                          [not_x2] rofa  — VRAM x2
                            [PAD:pad_bidir_pu] md5  — VRAM
```

### Path 7: depth 56.34 (281.70000000000005-845.1 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [or2] rela  — VRAM
                        [not_x1] rena  — VRAM
                          [not_x2] rofa  — VRAM x2
                            [PAD:pad_bidir_pu] md6  — VRAM
```

### Path 8: depth 56.34 (281.70000000000005-845.1 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [or2] rela  — VRAM
                        [not_x1] rena  — VRAM
                          [not_x2] rofa  — VRAM x2
                            [PAD:pad_bidir_pu] md7  — VRAM
```

### Path 9: depth 56.31 (281.55-844.6500000000001 ns, 709% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [and2] rocy  — VRAM
                        [not_x3] rahu  — VRAM x3 fan-out=17
                          [not_x1] rove  — VRAM
                            [and2] sefa  — VRAM
                              [not_x2] rege  — VRAM x2
                                [PAD:pad_bidir_pu] md0  — VRAM
```

### Path 10: depth 53.91 (269.54999999999995-808.65 ns, 678% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [not_x1] syro
      [nor2] tefa  — VRAM
        [and2] sose  — VRAM
          [and2] tuca  — VRAM
            [mux] tole  — VRAM
              [and2] sere  — VRAM
                [and2] sazo  — VRAM
                  [not_x1] ryje  — VRAM
                    [not_x1] revo  — VRAM
                      [and2] rocy  — VRAM
                        [not_x3] rahu  — VRAM x3 fan-out=17
                          [not_x1] rove  — VRAM
                            [and2] sogo  — VRAM
                              [not_x2] ryky  — VRAM x2
                                [PAD:pad_bidir_pu] md1  — VRAM
```


## Address Bus (32 paths, max depth 55.78)

### Path 1: depth 55.78 (278.9-836.7 ns, 702% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] amet
              [nor2] koty
                [PAD:pad_bidir] a0
```

### Path 2: depth 54.769999999999996 (273.84999999999997-821.55 ns, 689% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nor8] tulo
    [and2] tutu
      [nor2] soby
        [nand2] sepy
          [mux] tazy
            [nor2] rulo
              [PAD:pad_bidir] a15
```

### Path 3: depth 54.33 (271.65-814.9499999999999 ns, 684% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] apok
              [nor2] bajo
                [PAD:pad_bidir] a2
```

### Path 4: depth 50.15 (250.75-752.25 ns, 631% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] atol
              [nor2] cotu
                [PAD:pad_bidir] a1
```

### Path 5: depth 49.47 (247.35-742.05 ns, 623% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] asur
              [nor2] colo
                [PAD:pad_bidir] a7
```

### Path 6: depth 49.400000000000006 (247.00000000000003-741.0000000000001 ns, 622% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] atem
              [nor2] bevo
                [PAD:pad_bidir] a4
```

### Path 7: depth 47.81 (239.05-717.1500000000001 ns, 602% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] amer
              [nor2] bola
                [PAD:pad_bidir] a3
```

### Path 8: depth 45.61 (228.05-684.15 ns, 574% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] amet
              [nand2] kupo
                [PAD:pad_bidir] a0
```

### Path 9: depth 45.019999999999996 (225.09999999999997-675.3 ns, 567% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] pamy
              [nor2] rore
                [PAD:pad_bidir] a10
```

### Path 10: depth 44.28 (221.4-664.2 ns, 557% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] mano
              [nor2] mego
                [PAD:pad_bidir] a8
```


## APU CH3 (Wave) (28 paths, max depth 55.28)

### Path 1: depth 55.28 (276.4-829.2 ns, 696% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] dusa  — APU Decode
              [nand2] dery  — CH3
                [not_x1] gajy  — CH3
                  [REGISTERED:tffnl] fory  — CH3
```

### Path 2: depth 55.28 (276.4-829.2 ns, 696% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] dusa  — APU Decode
              [nand2] dery  — CH3
                [not_x1] gajy  — CH3
                  [REGISTERED:tffnl] gapo  — CH3
```

### Path 3: depth 55.28 (276.4-829.2 ns, 696% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] dusa  — APU Decode
              [nand2] dery  — CH3
                [not_x1] gajy  — CH3
                  [REGISTERED:tffnl] gatu  — CH3
```

### Path 4: depth 55.28 (276.4-829.2 ns, 696% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] dusa  — APU Decode
              [nand2] dery  — CH3
                [not_x1] gajy  — CH3
                  [REGISTERED:tffnl] gevo  — CH3
```

### Path 5: depth 55.18 (275.9-827.7 ns, 694% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] dusa  — APU Decode
              [nand2] dery  — CH3
                [not_x1] emut  — CH3
                  [REGISTERED:tffnl] fave  — CH3
```

### Path 6: depth 55.18 (275.9-827.7 ns, 694% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] dusa  — APU Decode
              [nand2] dery  — CH3
                [not_x1] emut  — CH3
                  [REGISTERED:tffnl] foro  — CH3
```

### Path 7: depth 55.18 (275.9-827.7 ns, 694% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] dusa  — APU Decode
              [nand2] dery  — CH3
                [not_x1] emut  — CH3
                  [REGISTERED:tffnl] fyru  — CH3
```

### Path 8: depth 55.18 (275.9-827.7 ns, 694% half T-cycle)
```
[BUS:] bus:a10  — CPU addr bus A10
  [nand7] tuna
    [nor2] syke fan-out=11
      [not_x1] bako  — APU Decode
        [nor2] buno  — APU Decode
          [not_x2] banu  — APU Decode x2 fan-out=14
            [nor2] dusa  — APU Decode
              [nand2] dery  — CH3
                [not_x1] emut  — CH3
                  [REGISTERED:tffnl] gemo  — CH3
```

### Path 9: depth 20.79 (103.94999999999999-311.84999999999997 ns, 262% half T-cycle)
```
[REGISTERED:dffr] davo  — CH3
  [not_x2] coka  — CH3 x2 fan-out=13
    [mux] bole  — CH3
      [not_x1] ydod  — CH3
        [and2] ygef  — CH3
          [BOUNDARY:wave_ram] wave_ram fan-out=16
```

### Path 10: depth 20.549999999999997 (102.74999999999999-308.24999999999994 ns, 259% half T-cycle)
```
[REGISTERED:dffr] davo  — CH3
  [not_x2] coka  — CH3 x2 fan-out=13
    [mux] bole  — CH3
      [and2] yjej  — CH3
        [BOUNDARY:wave_ram] wave_ram fan-out=16
```


## Sprite Control (3 paths, max depth 54.35000000000001)

### Path 1: depth 54.35000000000001 (271.75000000000006-815.2500000000001 ns, 684% half T-cycle)
```
[REGISTERED:dffr] muwy  — LY bit 0
  [not_x1] ebos  — Sprite Y Compare
    [full_add] eruc  — Sprite Y Compare
      [full_add] enef  — Sprite Y Compare
        [full_add] feco  — Sprite Y Compare
          [full_add] gyky  — Sprite Y Compare
            [full_add] gopu  — Sprite Y Compare
              [full_add] fuwa  — Sprite Y Compare
                [full_add] goju  — Sprite Y Compare
                  [full_add] wuhu  — Sprite Y Compare
                    [not_x1] gewy  — Sprite Y Compare
                      [nand6] wota  — Sprite Y Compare
                        [not_x1] gese  — Sprite Y Compare
                          [and3] care  — Sprite Control
                            [not_x2] dyty  — Sprite Control x2 fan-out=11
                              [REGISTERED:dffr] dezy  — Sprite Control
```

### Path 2: depth 13.209999999999999 (66.05-198.14999999999998 ns, 166% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [and2] xyvo  — LCD
    [not_x1] ales  — Sprite Control
      [and2] abov  — Sprite Control
        [REGISTERED:dffr] catu  — Sprite Control
```

### Path 3: depth 6.03 (30.150000000000002-90.45 ns, 76% half T-cycle)
```
[REGISTERED:dffr] fony  — Sprite Control
  [and4] feto  — Sprite Control
    [REGISTERED:dffr] byba  — Sprite Control
```


## Sprite X Priority (10 paths, max depth 52.44)

### Path 1: depth 52.44 (262.2-786.5999999999999 ns, 660% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [REGISTERED:dffr] fono  — Sprite X Priority
```

### Path 2: depth 44.559999999999995 (222.79999999999998-668.4 ns, 561% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [nor2] foxa  — Sprite X Priority
                                [REGISTERED:dffr] exuq  — Sprite X Priority
```

### Path 3: depth 41.78 (208.9-626.7 ns, 526% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [nor2] gutu  — Sprite X Priority
                              [REGISTERED:dffr] wapo  — Sprite X Priority
```

### Path 4: depth 41.14 (205.7-617.1 ns, 518% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [nor2] gono  — Sprite X Priority
                        [REGISTERED:dffr] xudy  — Sprite X Priority
```

### Path 5: depth 40.23 (201.14999999999998-603.4499999999999 ns, 506% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [nor2] xoja  — Sprite X Priority
                            [REGISTERED:dffr] womy  — Sprite X Priority
```

### Path 6: depth 36.99 (184.95000000000002-554.85 ns, 465% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [nor2] gega  — Sprite X Priority
                          [REGISTERED:dffr] wafy  — Sprite X Priority
```

### Path 7: depth 34.73 (173.64999999999998-520.9499999999999 ns, 437% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [nor2] gyfy  — Sprite X Priority
                      [REGISTERED:dffr] gota  — Sprite X Priority
```

### Path 8: depth 34.17 (170.85000000000002-512.5500000000001 ns, 430% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [nor2] guva  — Sprite X Priority
              [REGISTERED:dffr] eboj  — Sprite X Priority
```

### Path 9: depth 31.98 (159.9-479.7 ns, 402% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [nor2] emol  — Sprite X Priority
                    [REGISTERED:dffr] egav  — Sprite X Priority
```

### Path 10: depth 31.189999999999998 (155.95-467.84999999999997 ns, 392% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [nor2] enut  — Sprite X Priority
                  [REGISTERED:dffr] cedy  — Sprite X Priority
```


## Test Mode (5 paths, max depth 45.85999999999999)

### Path 1: depth 45.85999999999999 (229.29999999999995-687.8999999999999 ns, 577% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [and3] yula
            [nand2] zado
              [not_x1] zery
                [not_x1] zoku
                  [BOUNDARY:boot_rom] boot_rom
```

### Path 2: depth 40.81999999999999 (204.09999999999997-612.3 ns, 514% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [and3] yula
            [nand2] zado
              [not_x1] zery
                [BOUNDARY:boot_rom] boot_rom
```

### Path 3: depth 30.009999999999998 (150.04999999999998-450.15 ns, 378% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [or3] taba  — Clocks
        [BOUNDARY:sm83] cpu fan-out=42
```

### Path 4: depth 15.61 (78.05-234.14999999999998 ns, 196% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [BOUNDARY:sm83] cpu fan-out=42
```

### Path 5: depth 15.41 (77.05-231.15 ns, 194% half T-cycle)
```
[PAD:pad_in] t2
  [not_x1] uvar
    [and2] umut
      [BOUNDARY:sm83] cpu fan-out=42
```


## STAT/LY (8 paths, max depth 45.53)

### Path 1: depth 45.53 (227.65-682.95 ns, 573% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [nand5] fefy  — Sprite X Priority
              [or2] fepo  — Sprite X Priority
                [not_x1] xena  — STAT/LY
                  [and2] wodu  — STAT/LY
                    [REGISTERED:dffr] voga  — STAT/LY
```

### Path 2: depth 8.62 (43.099999999999994-129.29999999999998 ns, 108% half T-cycle)
```
[REGISTERED:dffr] lexa  — LY bit 2
  [xor] reda  — STAT/LY
    [nor4] subo  — STAT/LY
      [nand2] rape  — STAT/LY
        [not_x1] paly  — STAT/LY
          [REGISTERED:dffr] ropo  — STAT/LY
```

### Path 3: depth 5.51 (27.549999999999997-82.64999999999999 ns, 69% half T-cycle)
```
[REGISTERED:dffr] savy  — Pixel X bit 1
  [and2] xuke  — STAT/LY
    [and2] xyle  — STAT/LY
      [xor] xora  — STAT/LY
        [REGISTERED:dffr] xydo  — Pixel X bit 3
```

### Path 4: depth 4.98 (24.900000000000002-74.7 ns, 63% half T-cycle)
```
[REGISTERED:dffr] tuhu  — STAT/LY
  [and2] tyba  — STAT/LY
    [and2] sury  — STAT/LY
      [xor] roku  — STAT/LY
        [REGISTERED:dffr] sybe  — STAT/LY
```

### Path 5: depth 3.69 (18.45-55.35 ns, 46% half T-cycle)
```
[REGISTERED:dffr] tuhu  — STAT/LY
  [and2] tyba  — STAT/LY
    [xor] tyge  — STAT/LY
      [REGISTERED:dffr] tako  — STAT/LY
```

### Path 6: depth 3.07 (15.35-46.05 ns, 39% half T-cycle)
```
[REGISTERED:dffr] savy  — Pixel X bit 1
  [and2] xuke  — STAT/LY
    [xor] xegy  — STAT/LY
      [REGISTERED:dffr] xodu  — Pixel X bit 2
```

### Path 7: depth 1.71 (8.55-25.65 ns, 22% half T-cycle)
```
[REGISTERED:dffr] savy  — Pixel X bit 1
  [xor] rybo  — STAT/LY
    [REGISTERED:dffr] savy  — Pixel X bit 1
```

### Path 8: depth 1.63 (8.149999999999999-24.45 ns, 21% half T-cycle)
```
[REGISTERED:dffr] tuhu  — STAT/LY
  [xor] sake  — STAT/LY
    [REGISTERED:dffr] tuky  — STAT/LY
```


## Sprite Pixel Shifter (16 paths, max depth 36.36)

### Path 1: depth 36.36 (181.8-545.4 ns, 458% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pono  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] mofo  — Sprite FIFO
```

### Path 2: depth 36.36 (181.8-545.4 ns, 458% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pono  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] mytu  — Sprite FIFO
```

### Path 3: depth 35.730000000000004 (178.65000000000003-535.95 ns, 450% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pute  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] pefo  — Sprite FIFO
```

### Path 4: depth 35.730000000000004 (178.65000000000003-535.95 ns, 450% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pute  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] rewo  — Sprite FIFO
```

### Path 5: depth 35.58 (177.89999999999998-533.6999999999999 ns, 448% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pelo  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] peba  — Sprite FIFO
```

### Path 6: depth 35.58 (177.89999999999998-533.6999999999999 ns, 448% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pelo  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] roka  — Sprite FIFO
```

### Path 7: depth 35.47 (177.35-532.05 ns, 446% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] puly  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] rydu  — Sprite FIFO
```

### Path 8: depth 35.47 (177.35-532.05 ns, 446% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] puly  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] sega  — Sprite FIFO
```

### Path 9: depth 35.21 (176.05-528.15 ns, 443% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pawe  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] rama  — Sprite FIFO
```

### Path 10: depth 35.21 (176.05-528.15 ns, 443% half T-cycle)
```
[REGISTERED:nor_latch] xymu  — Rendering Active (Mode 3) fan-out=23
  [not_x1] tepa  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pawe  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] semo  — Sprite FIFO
```


## Joypad (12 paths, max depth 35.33)

### Path 1: depth 35.33 (176.64999999999998-529.9499999999999 ns, 445% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [nor2] kale
      [PAD:pad_bidir_pu] p13
```

### Path 2: depth 25.7 (128.5-385.5 ns, 323% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [nor2] kabu
      [PAD:pad_bidir_pu] p11
```

### Path 3: depth 25.439999999999998 (127.19999999999999-381.59999999999997 ns, 320% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [nor2] kasy
      [PAD:pad_bidir_pu] p12
```

### Path 4: depth 25.43 (127.15-381.45 ns, 320% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [or2] karu
      [PAD:pad_out_diff] p14
```

### Path 5: depth 24.16 (120.8-362.4 ns, 304% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [nor2] kybu
      [PAD:pad_bidir_pu] p10
```

### Path 6: depth 21.83 (109.14999999999999-327.45 ns, 275% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [or2] cela
      [PAD:pad_out_diff] p15
```

### Path 7: depth 10.86 (54.3-162.89999999999998 ns, 137% half T-cycle)
```
[PAD:pad_bidir_pu] p10
  [or4] kery
    [REGISTERED:dlatch] awob
```

### Path 8: depth 10.86 (54.3-162.89999999999998 ns, 137% half T-cycle)
```
[PAD:pad_bidir_pu] p10
  [or4] kery
    [REGISTERED:dffr] batu
```

### Path 9: depth 9.86 (49.3-147.89999999999998 ns, 124% half T-cycle)
```
[REGISTERED:dffr] buro
  [nand2] kory
    [PAD:pad_bidir_pu] p13
```

### Path 10: depth 4.96 (24.8-74.4 ns, 62% half T-cycle)
```
[REGISTERED:dffr] buro
  [nand2] kyhu
    [PAD:pad_bidir_pu] p12
```


## Serial (6 paths, max depth 32.25)

### Path 1: depth 32.25 (161.25-483.75 ns, 406% half T-cycle)
```
[REGISTERED:dffr] coty
  [muxi] cave
    [or2] dawa
      [nor2] kujo
        [PAD:pad_bidir_pu_latch] sck
```

### Path 2: depth 24.25 (121.25-363.75 ns, 305% half T-cycle)
```
[REGISTERED:dffr] coty
  [muxi] cave
    [or2] dawa
      [nand2] kexu
        [PAD:pad_bidir_pu_latch] sck
```

### Path 3: depth 10.75 (53.75-161.25 ns, 135% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] jeva
    [nor2] kywe
      [PAD:pad_bidir_pu] sin
```

### Path 4: depth 6.68 (33.4-100.19999999999999 ns, 84% half T-cycle)
```
[REGISTERED:dffr] buro
  [muxi] kena
    [PAD:pad_out] sout
```

### Path 5: depth 4.78 (23.900000000000002-71.7 ns, 60% half T-cycle)
```
[REGISTERED:dffr] buro
  [nand2] kore
    [PAD:pad_bidir_pu] sin
```

### Path 6: depth 0.75 (3.75-11.25 ns, 9% half T-cycle)
```
[PAD:pad_bidir_pu] sin
  [not_x1] cage
    [REGISTERED:dffsr] cuba
```


## APU Control (1 paths, max depth 16.669999999999998)

### Path 1: depth 16.669999999999998 (83.35-250.04999999999998 ns, 210% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [and2] efop  — APU Control
        [REGISTERED:drlatch_ee] fero  — APU Control
```


## Sprite X Match (80 paths, max depth 14.09)

### Path 1: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] baxo  — Sprite X Match
  [not_x1] arop  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] ceso  — Sprite X Match
```

### Path 2: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] depo  — Sprite X Match fan-out=17
  [not_x1] bady  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] cusy  — Sprite X Match
```

### Path 3: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] depo  — Sprite X Match fan-out=17
  [not_x1] bady  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] cuvy  — Sprite X Match
```

### Path 4: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] gomo  — Sprite X Match fan-out=17
  [not_x1] cose  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] cywe  — Sprite X Match
```

### Path 5: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] gomo  — Sprite X Match fan-out=17
  [not_x1] cose  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] dake  — Sprite X Match
```

### Path 6: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] ylor  — Sprite X Match
  [not_x1] zago  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] dany  — Sprite X Match
```

### Path 7: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] zezy  — Sprite X Match
  [not_x1] yvok  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] dazo  — Sprite X Match
```

### Path 8: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] depo  — Sprite X Match fan-out=17
  [not_x1] bady  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] depy  — Sprite X Match
```

### Path 9: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] zyve  — Sprite X Match
  [not_x1] ypur  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] desu  — Sprite X Match
```

### Path 10: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[REGISTERED:dlatch_ee] gomo  — Sprite X Match fan-out=17
  [not_x1] cose  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] duhy  — Sprite X Match
```


## Other (1 paths, max depth 14.09)

### Path 1: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[BOUNDARY:sm83] cpu fan-out=42
  [not_x1] lexy
    [PAD:pad_out] m1
```


## OAM Interface (7 paths, max depth 14.09)

### Path 1: depth 14.09 (70.45-211.35 ns, 177% half T-cycle)
```
[BUS:] bus:oam_~{a3}_tri
  [not_x1] yfoc  — OAM
    [REGISTERED:dffr_cc] xedy  — OAM
```

### Path 2: depth 12.68 (63.4-190.2 ns, 160% half T-cycle)
```
[BUS:] bus:oam_~{a7}_tri
  [not_x1] yzet  — OAM
    [REGISTERED:dffr_cc] xecu  — OAM
```

### Path 3: depth 12.47 (62.35-187.05 ns, 157% half T-cycle)
```
[BUS:] bus:oam_~{a5}_tri
  [not_x1] ymev  — OAM
    [REGISTERED:dffr_cc] xobe  — OAM
```

### Path 4: depth 12.36 (61.8-185.39999999999998 ns, 156% half T-cycle)
```
[BUS:] bus:oam_~{a6}_tri
  [not_x1] xemu  — OAM
    [REGISTERED:dffr_cc] yduf  — OAM
```

### Path 5: depth 11.84 (59.2-177.6 ns, 149% half T-cycle)
```
[BUS:] bus:oam_~{a4}_tri
  [not_x1] yvom  — OAM
    [REGISTERED:dffr_cc] zuze  — OAM
```

### Path 6: depth 7.26 (36.3-108.89999999999999 ns, 91% half T-cycle)
```
[BUS:] bus:oam_~{a2}_tri
  [not_x1] yfot  — OAM
    [REGISTERED:dffr_cc] xadu  — OAM
```

### Path 7: depth 6.41 (32.05-96.15 ns, 81% half T-cycle)
```
[BUS:] bus:clk_t4  — Clock bus (clk_t4)
  [not_x1] decy  — OAM
    [not_x1] caty  — OAM
      [REGISTERED:dffr] maka  — OAM
```


## BG/Win Cycles (3 paths, max depth 9.370000000000001)

### Path 1: depth 9.370000000000001 (46.85000000000001-140.55 ns, 118% half T-cycle)
```
[REGISTERED:drlatch_ee] mypu  — Window
  [xnor] nezo  — Window
    [nand5] puky  — Window
      [not_x1] nufa  — Window
        [nand5] nogy  — Window
          [not_x1] nuko  — Window
            [nor2] pany  — BG/Win Cycles
              [REGISTERED:dffr] ryfa  — Window Y Match
```

### Path 2: depth 5.6000000000000005 (28.000000000000004-84.00000000000001 ns, 70% half T-cycle)
```
[REGISTERED:drlatch_ee] mypu  — Window
  [xnor] nezo  — Window
    [nand5] puky  — Window
      [not_x1] nufa  — Window
        [nand5] nogy  — Window
          [not_x1] nuko  — Window
            [REGISTERED:dffr] pyco  — BG/Win Cycles
```

### Path 3: depth 3.5000000000000004 (17.500000000000004-52.50000000000001 ns, 44% half T-cycle)
```
[REGISTERED:drlatch_ee] cyxu  — BG Scroll
  [xnor] sozu  — BG/Win Cycles
    [nand4] rone  — BG/Win Cycles
      [not_x1] pohu  — BG/Win Cycles
        [REGISTERED:dffr] puxa  — BG/Win Cycles
```


## Clock Distribution (1 paths, max depth 7.84)

### Path 1: depth 7.84 (39.2-117.6 ns, 99% half T-cycle)
```
[BOUNDARY:sm83] cpu fan-out=42
  [not_x1] abol  — Clocks
    [nor3] bate  — Clocks
      [not_x1] basu  — Clocks
        [not_x6] buke  — Clocks x6
          [BOUNDARY:sm83] cpu fan-out=42
```


## Window Logic (1 paths, max depth 6.699999999999999)

### Path 1: depth 6.699999999999999 (33.5-100.49999999999999 ns, 84% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [xnor] nupa  — Window
    [nand5] palo  — Window
      [not_x1] nele  — Window
        [nand5] pafu  — Window
          [not_x1] roge  — Window
            [REGISTERED:dffr] sary  — Window
```


## Boot ROM (1 paths, max depth 1.83)

### Path 1: depth 1.83 (9.15-27.450000000000003 ns, 23% half T-cycle)
```
[BUS:] bus:d0  — CPU data bus D0 fan-out=46
  [or2] sato
    [REGISTERED:dffr] tepu
```
