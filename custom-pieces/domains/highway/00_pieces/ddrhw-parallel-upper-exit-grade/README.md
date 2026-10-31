# RHW Ramp — L2 Exit Parallel Grade — Parallel

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![RHW Ramp — L2 Exit Parallel Grade — Parallel — Clean angled view](previews/preview.png)

![RHW Ramp — L2 Exit Parallel Grade — Parallel — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This upper L2 off-ramp contains the straight parallel grade between the flat high departure at 15 m and the ground terminal at 0 m. A grade is height change divided by horizontal distance: 20% means 2 m of height change over 10 m horizontally. Its physical straight run is 56.185959 m, with a maximum source grade of approximately 28.202932%. The profile includes a 2 m change of grade at each end and a final 1 m flat ground collar.

This is a fixed-height transition, not a straight slope that can be repeated to obtain any chosen height. Its visible grade model overhangs neighbouring departure and terminal tiles. Its whole-cell traffic ownership also includes one native highway half, so the model and traffic boundaries differ. The native through PATHs and outside-deck ramp route remain with those owned cells. The visible native highway half and its centre pier instead belong to the adjacent straight slip-lane model through overhang, leaving this component’s physical model as a pure graded ramp.

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **3 tiles inside a 2 × 2-tile rectangle**. Its reference position in the complete assembly is **P14: X3, Y3, at 0°**. Its actual occupied cells on that shared grid are **(X3, Y3), (X4, Y3), (X3, Y2)**. The [assembly construction picture](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **RHW Ramp — L2 Exit Parallel Grade — Parallel** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X3, Y3**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** Physical grade: 15 ↔ 0 m; saved tile-edge cuts have their measured intermediate heights. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

<!-- BEGIN PIECE OVERVIEW -->

Place one l2 exit parallel grade for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-upper-exit-grade`.

Footprint: **2 × 2 tiles**. Exact menu name: **RHW Ramp — L2 Exit Parallel Grade — Parallel**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-0336998525a8d477398d) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`channel-06-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-07-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-08-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-09-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-10-out`<br>Variant: access-ramp |
| --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-06bc1e8fe6d0d9e68964) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ac5c2903ada82abe05c5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f70411370829ae1835b3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-42f0ddc8b74b0b57a86b) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-232fe54cc3f3474601f2)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-232fe54cc3f3474601f2) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cbbf9f25aa4757b208d1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8432590a80ec35fef389) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4268d33b687d934bef4b) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1c1ae1e3f9a94ec021e0)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1c1ae1e3f9a94ec021e0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f086f701d2e58cd29312) |
| **Road · West entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ce395ba727bb842462f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a92fe59a9dd60f0af439) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-23d999f4bad43fe92088)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-23d999f4bad43fe92088) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-32d9aececb48f09c4777) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f576fc9e422b73f067b1) |
| **Road · North entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-19542bc27f0195183f7f) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-535903121452f6f091db)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-535903121452f6f091db) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-21897fe29d869c3434b5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1dca6e87a52aa88003dc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-21514df48349928528db) |
| **Road · North entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-fe525a2dfe6d1a3d8135)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-fe525a2dfe6d1a3d8135) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b1fe012b07a68b84e7f6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4e31d741395452c6faa6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-41d46cf661c67e793183) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-79012443a3bbc8d4eb57)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-098e6163cb2b2ce0bdb1) |

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

#### Boundary A: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / North |
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
| `member-channel-04-in` / `channel-04-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-04-in` / car | Incoming | `[-3.2,8,7.5]` | Not declared | 45° | 0 |
| `member-channel-05-in` / `channel-05-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-05-in` / car | Incoming | `[3.2,8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / North |
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
| `member-channel-08-out` / `channel-08-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-08-out` / car | Outgoing | `[-3.2,8,15]` | Not declared | 45° | 0 |
| `member-channel-09-out` / `channel-09-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-09-out` / car | Outgoing | `[3.2,8,15]` | Not declared | 45° | 0 |

#### Boundary B: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / West |
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
| `member-channel-06-out` / `channel-06-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-06-out` / car | Outgoing | `[-8,-3.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-07-out` / `channel-07-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-07-out` / car | Outgoing | `[-8,3.2,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / West |
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
| `member-channel-02-in` / `channel-02-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-02-in` / car | Incoming | `[-8,-3.2,15]` | Not declared | 225° | 0 |
| `member-channel-03-in` / `channel-03-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-03-in` / car | Incoming | `[-8,3.2,15]` | Not declared | 225° | 0 |

#### Boundary C: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (10.0624 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-access-network-upper-off-01` / `access-network-upper-off` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (10.0624 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 28.202% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-01-in` / `channel-01-in` | `access-upper-off` / `cut-channel-01-in` / car | Incoming | `[-8,-16.9706,10.0624]` | Not declared | 225° | 28.202 |

#### Boundary D: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.131713 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-access-network-upper-off-01` / `access-network-upper-off` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.131713 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -18.3238% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-10-out` / `channel-10-out` | `access-upper-off` / `cut-channel-10-out` / car | Outgoing | `[16.9706,8,0.131713]` | Not declared | 45° | -18.3238 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
