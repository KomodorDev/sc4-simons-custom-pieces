# RHW Ramp — L1 Entry Parallel Grade — Parallel

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![RHW Ramp — L1 Entry Parallel Grade — Parallel — Clean angled view](previews/preview.png)

![RHW Ramp — L1 Entry Parallel Grade — Parallel — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This lower L1 on-ramp contains the straight parallel grade between the flat high departure at 7.5 m and the ground terminal at 0 m. A grade is height change divided by horizontal distance: 20% means 2 m of height change over 10 m horizontally. Its physical straight run is 44.872251 m, with a maximum source grade of approximately 17.911624%. The profile includes a 2 m change of grade at each end and a final 1 m flat ground collar.

This is a fixed-height transition, not a straight slope that can be repeated to obtain any chosen height. Its visible grade model overhangs neighbouring departure and terminal tiles. Its whole-cell traffic ownership also includes one native highway half, so the model and traffic boundaries differ. The native through PATHs and outside-deck ramp route remain with those owned cells. The visible native highway half and its centre pier instead belong to the adjacent straight slip-lane model through overhang, leaving this component’s physical model as a pure graded ramp.

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **2 tiles inside a 2 × 1-tile rectangle**. Its reference position in the complete assembly is **P13: X2, Y4, at 0°**. Its actual occupied cells on that shared grid are **(X2, Y4), (X3, Y4)**. The [assembly construction picture](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **RHW Ramp — L1 Entry Parallel Grade — Parallel** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X2, Y4**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** Physical grade: 7.5 ↔ 0 m; saved tile-edge cuts have their measured intermediate heights. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

<!-- BEGIN PIECE OVERVIEW -->

Place one l1 entry parallel grade for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-lower-entry-grade`.

Footprint: **2 × 1 tiles**. Exact menu name: **RHW Ramp — L1 Entry Parallel Grade — Parallel**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-73298d60b51d673cf7de) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · South exit**<br>`channel-06-out`<br>Variant: access-ramp | **Road · South exit**<br>`channel-07-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-08-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`channel-09-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-10-out`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e27361ceafaf5fa0d536) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c08b91ae37389c9552d4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4037cad9d9d7e3a72de0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-16e41796e16de87a992d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ace3e59dbb8237483938)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ace3e59dbb8237483938) |
| **Road · North entrance**<br>`channel-02-in`<br>Variant: access-ramp | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-44024dd261e654216c31)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-44024dd261e654216c31) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9346ab26c70bf62cc189) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a18bb6927b46dc908030) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a261db6b6f5e8043c8fd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-869fc9b99e4ffe373223) |
| **Road · South entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-211d0bc517a7ad4b538d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5e462fe617cf01bb33d3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-56ebbbd3304953ad160f) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-739a4336d40735397629)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-739a4336d40735397629) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-de60dae125de6d33ee4f) |
| **Road · East entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7324414a66167193e06f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6575c0663abe2fa1a5e0) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-06b96dcde2c053b52509)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-06b96dcde2c053b52509) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9d1cbdb4c334c9f36362) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f48c23b2511b98532f02) |
| **Road · East entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-aa300ce36fac53605c64) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-e746ce8e25ac9ddef8b9)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-e746ce8e25ac9ddef8b9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c4edaede883922d2e4ed) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-71aeabf04f965b21cf0d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c565b761ac92812f117)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-86f671242d3bd6f5b5b9) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 0 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.

#### Boundary A: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (4.36411 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-access-network-lower-on-01` / `access-network-lower-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (4.36411 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 17.9118% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-06-out` / `channel-06-out` | `access-lower-on` / `cut-channel-06-out` / car | Outgoing | `[-0.970563,-8,4.36411]` | Not declared | 225° | 17.9118 |

#### Boundary B: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
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
| `member-channel-07-out` / `channel-07-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-07-out` / car | Outgoing | `[12.8,-8,7.5]` | Not declared | 225° | 0 |
| `member-channel-08-out` / `channel-08-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-08-out` / car | Outgoing | `[19.2,-8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
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
| `member-channel-01-in` / `channel-01-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-01-in` / car | Incoming | `[12.8,-8,15]` | Not declared | 225° | 0 |
| `member-channel-03-in` / `channel-03-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-03-in` / car | Incoming | `[19.2,-8,15]` | Not declared | 225° | 0 |

#### Boundary C: `boundary-02`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.311171 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-access-network-lower-on-01` / `access-network-lower-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.311171 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -17.912% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-02-in` / `channel-02-in` | `access-lower-on` / `cut-channel-02-in` / car | Incoming | `[15.0294,8,0.311171]` | Not declared | 45° | -17.912 |

#### Boundary D: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
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
| `member-channel-04-in` / `channel-04-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-04-in` / car | Incoming | `[24,-3.2,7.5]` | Not declared | 45° | 0 |
| `member-channel-05-in` / `channel-05-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-05-in` / car | Incoming | `[24,3.2,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
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
| `member-channel-09-out` / `channel-09-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-09-out` / car | Outgoing | `[24,-3.2,15]` | Not declared | 45° | 0 |
| `member-channel-10-out` / `channel-10-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-10-out` / car | Outgoing | `[24,3.2,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
