# RHW Ramp — L2 Entry Parallel Grade — Parallel — Alignment B

Reusable Alignment B component for the close parallel diagonal diamond.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled view shows this type's actual model and overhang; the north-up view shows its relation to the city grid. These software pictures do not establish game appearance, native-neighbour compatibility, or visible traffic. Use the component's own pictures when comparing it with another type.

<!-- BEGIN PIECE VIEWS -->

![RHW Ramp — L2 Entry Parallel Grade — Parallel — Alignment B — Clean angled view](previews/preview.png)

![RHW Ramp — L2 Entry Parallel Grade — Parallel — Alignment B — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This is the fixed entry height transition between its flat lateral departure and the Avenue right-turn terminal. Its physical ramp runs parallel to the highway. It carries the complete native traffic fragments required by every city tile it owns, even when the corresponding visible highway model is supplied by a neighbouring slip component.

**Permanent ID:** `ddrhw-parallel-b-upper-entry-grade`. **Recipe:** `highway_ddrhw_parallel_b_upper_entry_grade`. This component owns **3 city tiles** inside a **3 × 2 bounding footprint**. Its local occupied cells are **[2,0], [0,1], [1,1]**, measured from the reference corner with columns increasing east and rows increasing south. Empty cells inside that rectangle remain unowned. Physical grade between 15 m and 0 m; actual cell-edge ports have their own measured intermediate heights.

1. Open **Transportation → Highways → SCP → Assemblies**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond — Alignment B**.
2. Starting at P01, press **Tab 14 times** to reach **P15 — RHW Ramp — L2 Entry Parallel Grade — Parallel — Alignment B**. Shift+Tab moves backward. Each click places this component, rather than the whole junction.
3. In the [B reference layout](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md#3-placements), use **X6, Y7**, with the authored **0°** orientation. Home and End rotate the selected type. Match its actual occupied preview cells before clicking; the reference corner can itself be empty.
4. Join only the complete matching B boundary described by its connection card and the assembly placement plan. A similar A model does not establish matching whole-cell PATH ownership. For an independent layout, check every direction, endpoint, height, angle, and grade; compatibility with an untested neighbour remains unverified.

This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here.

All B components intentionally generate no custom cast shadows. A **PATH** is the directed game traffic resource; a visible road surface and a PATH connection establish different facts. Preserve this type's complete owned-cell traffic data when reusing it. New B identifiers require fresh placement, and game results are recorded separately in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Place one l2 entry parallel grade for Alignment B of the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-b-upper-entry-grade`.

Footprint: **3 × 2 tiles**. Exact menu name: **RHW Ramp — L2 Entry Parallel Grade — Parallel — Alignment B**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes this piece's intrinsic measured journeys. Its connector overview identifies exposed boundaries, including any overhang; it does not establish compatibility with an untested neighbour. Route Query and visible travel retain separate observation cases.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-a4ae690c50aff3ee8c32) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`channel-07-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-08-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-09-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-10-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-11-out`<br>Variant: access-ramp | **Road · North exit**<br>`channel-12-out`<br>Variant: access-ramp |
| --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-78f256bf952b8fca10e0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6601fc7fbb202bdf60b8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f4be11ac3caaad789ae8) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c6ed5787adc0d320bfe7)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c6ed5787adc0d320bfe7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-17ea5ab92f31d666db45) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-255a76c0bb2e3b132af4) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e20bae55a25f61127ff0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a1fbcb8d99d6f019c85) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f880f87bfb94c76cfbc6)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f880f87bfb94c76cfbc6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c170569b71e8b0c9b2e2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f4308de265fe58bcb429) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fe9778c69fc4ae8b5fca) |
| **Road · North entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-889fa9dd52378dde5cd3) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-51a3f802ca067c76d0cd)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-51a3f802ca067c76d0cd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1c145116de015174e036) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-50302fea8fa125eaf0dc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ef5296a4f740c7c46754) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7e6b7f2142b8b678a606) |
| **Road · South entrance**<br>`channel-04-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f6ac3ce249d4c7ee0816) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-042a69751ceca1aed582) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f4e44125b1149a50e9b2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f637e35e3bdd7269b4c1) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-3a73632d07d3d345d116)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-3a73632d07d3d345d116) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c943912b676e46f77984) |
| **Road · North entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-2337a652e855fe2f2448)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-2337a652e855fe2f2448) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c232a10531df4ab2f843) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0c964109d1f9c6368559) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3828f671a8e8fa25ca92) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a849f332698d35368f6f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d8ce18ac2d1ca0d07abf) |
| **Road · West entrance**<br>`channel-06-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cc132acd026941825c7f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-37c4519c10456ab2642e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a08f27909278b2342700) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2f638eed47fc1518ca96) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-deb9b02e1b507a17535d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1934396b4f14a6c9f18e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-75e547b0bcf8bcf29de9)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-75e547b0bcf8bcf29de9) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 1 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.

#### Boundary A: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.489958 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-access-network-upper-on-01` / `access-network-upper-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.489958 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | -28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-04-in` / `channel-04-in` | `access-upper-on` / `cut-channel-04-in` / car | Incoming | `[0.970563,-24,0.489958]` | Not declared | 225° | -28.2029 |

#### Boundary B: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 2 incoming; 0 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-03-in` / `channel-03-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-03-in` / car | Incoming | `[-3.2,-8,7.5]` | Not declared | 45° | 0 |
| `member-channel-05-in` / `channel-05-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-05-in` / car | Incoming | `[3.2,-8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 0 incoming; 2 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-09-out` / `channel-09-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-09-out` / car | Outgoing | `[-3.2,-8,15]` | Not declared | 45° | 0 |
| `member-channel-10-out` / `channel-10-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-10-out` / car | Outgoing | `[3.2,-8,15]` | Not declared | 45° | 0 |

#### Boundary C: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 0 incoming; 2 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-07-out` / `channel-07-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-07-out` / car | Outgoing | `[-8,-19.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-08-out` / `channel-08-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-08-out` / car | Outgoing | `[-8,-12.8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 2 incoming; 0 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-01-in` / `channel-01-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-01-in` / car | Incoming | `[-8,-19.2,15]` | Not declared | 225° | 0 |
| `member-channel-02-in` / `channel-02-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-02-in` / car | Incoming | `[-8,-12.8,15]` | Not declared | 225° | 0 |

#### Boundary D: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.87155 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-access-network-upper-on-01` / `access-network-upper-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.87155 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-11-out` / `channel-11-out` | `access-upper-on` / `cut-channel-11-out` / car | Outgoing | `[16.9706,-8,6.87155]` | Not declared | 45° | 28.2029 |

#### Boundary E: `boundary-06`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (13.2531 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-access-network-upper-on-01` / `access-network-upper-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (13.2531 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-12-out` / `channel-12-out` | `access-upper-on` / `cut-channel-12-out` / car | Outgoing | `[32.9706,8,13.2531]` | Not declared | 45° | 28.2029 |

#### Boundary F: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (9.67524 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-access-network-upper-on-01` / `access-network-upper-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (9.67524 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | -28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-06-in` / `channel-06-in` | `access-upper-on` / `cut-channel-06-in` / car | Incoming | `[24,-0.970563,9.67524]` | Not declared | 225° | -28.2029 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
