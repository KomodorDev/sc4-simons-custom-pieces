# RHW Ramp — L2 Exit Parallel Grade — Parallel — Alignment B

Reusable Alignment B component for the close parallel diagonal diamond.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled view shows this type's actual model and overhang; the north-up view shows its relation to the city grid. These software pictures do not establish game appearance, native-neighbour compatibility, or visible traffic. Use the component's own pictures when comparing it with another type.

<!-- BEGIN PIECE VIEWS -->

![RHW Ramp — L2 Exit Parallel Grade — Parallel — Alignment B — Clean angled view](previews/preview.png)

![RHW Ramp — L2 Exit Parallel Grade — Parallel — Alignment B — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This is the fixed exit height transition between its flat lateral departure and the Avenue right-turn terminal. Its physical ramp runs parallel to the highway. It carries the complete native traffic fragments required by every city tile it owns, even when the corresponding visible highway model is supplied by a neighbouring slip component.

**Permanent ID:** `ddrhw-parallel-b-upper-exit-grade`. **Recipe:** `highway_ddrhw_parallel_b_upper_exit_grade`. This component owns **3 city tiles** inside a **2 × 3 bounding footprint**. Its local occupied cells are **[1,0], [1,1], [0,2]**, measured from the reference corner with columns increasing east and rows increasing south. Empty cells inside that rectangle remain unowned. Physical grade between 15 m and 0 m; actual cell-edge ports have their own measured intermediate heights.

1. Open **Transportation → Highways → SCP | DD RHW-4 — Parallel Diagonal Avenue Diamond**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond — Alignment B**.
2. Starting at P01, press **Tab 13 times** to reach **P14 — RHW Ramp — L2 Exit Parallel Grade — Parallel — Alignment B**. Shift+Tab moves backward. Each click places this component, rather than the whole junction.
3. In the [B reference layout](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md#3-placements), use **X3, Y4**, with the authored **0°** orientation. Home and End rotate the selected type. Match its actual occupied preview cells before clicking; the reference corner can itself be empty.
4. Join only the complete matching B boundary described by its connection card and the assembly placement plan. A similar A model does not establish matching whole-cell PATH ownership. For an independent layout, check every direction, endpoint, height, angle, and grade; compatibility with an untested neighbour remains unverified.

This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here.

All B components intentionally generate no custom cast shadows. A **PATH** is the directed game traffic resource; a visible road surface and a PATH connection establish different facts. Preserve this type's complete owned-cell traffic data when reusing it. New B identifiers require fresh placement, and game results are recorded separately in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Place one l2 exit parallel grade for Alignment B of the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-b-upper-exit-grade`.

Footprint: **2 × 3 tiles**. Exact menu name: **RHW Ramp — L2 Exit Parallel Grade — Parallel — Alignment B**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes this piece's intrinsic measured journeys. Its connector overview identifies exposed boundaries, including any overhang; it does not establish compatibility with an untested neighbour. Route Query and visible travel retain separate observation cases.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-10b700ece125100ebf4f) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · North exit**<br>`channel-07-out`<br>Variant: access-ramp | **Road · West exit**<br>`channel-08-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-09-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-10-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-11-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-12-out`<br>Variant: access-ramp |
| --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: access-ramp | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-6109f5bbccb43a432b4c)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-6109f5bbccb43a432b4c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dd2ffb9ff0be8f4d9199) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b78de417e29fadd1de84) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-153eaf778dcfeeee2573) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-85a8ffd8b41fda3fb9b2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ea09be2ee1003a42786b) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-884ddec345bb2a60fed2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-88fd231939e2e3bbbca2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6714111effcab1d1e345) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-46cdd2bbc752602f142d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-02fc375a1fff09c6b6eb) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-113c1593c347b43e4c59)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-113c1593c347b43e4c59) |
| **Road · West entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ca354d4b5797f6e1f4e0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-be3b86db48f289dbe9a3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7b1437175a882ea04c2a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0c2e6923ecf8138b8766) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-0e2c29e55dfa92a72768)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-0e2c29e55dfa92a72768) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-be6d76ce88e7d175135a) |
| **Road · West entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ad70236c87933a26ea29) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f1d61ea758b1271e52ba) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-77be9599501353f3c6db) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c5ae8754c045ab810c67)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c5ae8754c045ab810c67) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-944e41954ce485f44b63) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-85341f7d95c57435ac57) |
| **Road · North entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-06161d146c98dedf0ffd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-986cab59b6b008c49098) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-07827aee91f293cf5267)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-07827aee91f293cf5267) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0dd9fda6cad85da3db62) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0a60497bee3cf3b04690) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9d9f748919a189cf43b0) |
| **Road · North entrance**<br>`channel-06-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-62d451841e35dcba2bd6) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-de4761b284e2fef340ee)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-de4761b284e2fef340ee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-72b25bd2504a8ffd0b54) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e2c5be3266b9bbc61057) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-704f77a6e1eb3b945aec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3562800f29b9659a653a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f70a3cea6cf377724351) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 2 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.

#### Boundary A: `boundary-02`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (9.67524 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-access-network-upper-off-01` / `access-network-upper-off` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (9.67524 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-07-out` / `channel-07-out` | `access-upper-off` / `cut-channel-07-out` / car | Outgoing | `[0.970563,-24,9.67524]` | Not declared | 45° | -28.2029 |

#### Boundary B: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (13.2531 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-access-network-upper-off-01` / `access-network-upper-off` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (13.2531 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-01-in` / `channel-01-in` | `access-upper-off` / `cut-channel-01-in` / car | Incoming | `[-8,-32.9706,13.2531]` | Not declared | 225° | 28.2029 |

#### Boundary C: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
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
| `member-channel-05-in` / `channel-05-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-05-in` / car | Incoming | `[12.8,8,7.5]` | Not declared | 45° | 0 |
| `member-channel-06-in` / `channel-06-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-06-in` / car | Incoming | `[19.2,8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
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
| `member-channel-10-out` / `channel-10-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-10-out` / car | Outgoing | `[12.8,8,15]` | Not declared | 45° | 0 |
| `member-channel-11-out` / `channel-11-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-11-out` / car | Outgoing | `[19.2,8,15]` | Not declared | 45° | 0 |

#### Boundary D: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
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
| `member-channel-08-out` / `channel-08-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-08-out` / car | Outgoing | `[8,-3.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-09-out` / `channel-09-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-09-out` / car | Outgoing | `[8,3.2,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
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
| `member-channel-03-in` / `channel-03-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-03-in` / car | Incoming | `[8,-3.2,15]` | Not declared | 225° | 0 |
| `member-channel-04-in` / `channel-04-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-04-in` / car | Incoming | `[8,3.2,15]` | Not declared | 225° | 0 |

#### Boundary E: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.489958 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-access-network-upper-off-01` / `access-network-upper-off` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.489958 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-12-out` / `channel-12-out` | `access-upper-off` / `cut-channel-12-out` / car | Outgoing | `[24,-0.970563,0.489958]` | Not declared | 45° | -28.2029 |

#### Boundary F: `boundary-06`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.87155 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-access-network-upper-off-01` / `access-network-upper-off` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.87155 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-02-in` / `channel-02-in` | `access-upper-off` / `cut-channel-02-in` / car | Incoming | `[8,-16.9706,6.87155]` | Not declared | 225° | 28.2029 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
