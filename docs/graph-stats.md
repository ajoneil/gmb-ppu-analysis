# GateBoy PPU Dependency Graph — Statistics

## Graph Metrics

| Metric | Value |
|--------|-------|
| Total nodes | 2804 |
| Total edges | 5006 |
| Registered nodes (DFF, latch, bus, boundary + @old proxies) | 899 |
| Combinatorial nodes (gates, wires) | 1905 |
| Weakly connected components | 110 |
| Has cycles (before DAG conversion) | Yes |
| Edges removed to break cycles | 62 |
| Total critical paths found | 1265 |
| Maximum combinatorial depth | 17 (clock distribution) |
| Maximum PPU-specific depth | 14 (VRAM bus) |

## Node Type Breakdown

| Type | Count | Description |
|------|-------|-------------|
| combinatorial | 1905 | `wire` locals and `Gate` state members |
| registered | 801 | DFF, latch, and 200 `@old` temporal boundary proxies (~601 unique) |
| bus | 63 | Tri-state buses (CPU, VRAM, OAM data) |
| boundary | 35 | SigIn/SigOut (chip boundary signals) |

## Source Files Parsed

| File | Statements |
|------|-----------|
| GateBoy.cpp | 278 |
| GateBoySpriteStore.cpp | 651 |
| GateBoyPixPipe.cpp | 518 |
| GateBoyVramBus.cpp | 503 |
| GateBoyOamBus.cpp | 353 |
| GateBoyTimer.cpp | 182 |
| GateBoyLCD.cpp | 170 |
| GateBoyExtBus.cpp | 162 |
| GateBoyInterrupts.cpp | 112 |
| GateBoyDMA.cpp | 69 |
| GateBoySerial.cpp | 69 |
| GateBoyCpuBus.cpp | 64 |
| GateBoyClocks.cpp | 60 |
| GateBoyJoypad.cpp | 59 |
| GateBoyRegisters.cpp | 44 |
| GateBoyReset.cpp | 38 |
| **Total** | **3332** |

## Unresolved References (139)

Signal references that could not be resolved to known graph nodes:

1. **Computed state methods** (e.g., `XAPO_VID_RSTn_new()`, `SYRO_FE00_FFFF_new()`) — inline methods on `GateBoyState` that compute values from multiple fields. These add 1-3 gates of depth not captured by the parser.

2. **CPU address bus** (`BUS_CPU_A00p`-`BUS_CPU_A15p`) — driven by the CPU model outside gate logic, treated as external inputs.

3. **Map/tile address computations** (`ABOD_MAP_X1_new`, etc.) — computed inline using patterns not matched by our regex.

These unresolved refs mean reported depths are **lower bounds** — actual paths may be 1-3 gates deeper.

## Cycle-Breaking

62 edges were removed to create a DAG. They represent:

- **Bus read-back loops** (38 edges): CPU data bus driven by registers that are also written from the bus (interrupt flags, TIMA, OAM/VRAM data latches)
- **Sprite pipe masking** (16 edges): Sprite pipe output feeds back into sprite mask logic
- **Control feedback** (8 edges): DMA latch, scan done, fetch done, window hit, fetch clock gating

These are real async feedback paths in hardware (through DFF async set/reset), not true combinatorial cycles.
