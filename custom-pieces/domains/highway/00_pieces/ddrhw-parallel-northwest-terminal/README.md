# Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW — Clean angled view](previews/preview.png)

![Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

**Current shadow policy:** this component intentionally supplies no cast shadow, as do all fifteen parallel-kit components. After installing the checked revision and restarting, use a fresh placement to avoid confusing older saved attachments with the current result. Follow the assembly’s [no-shadow and cleanup checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#44-independent-module-shadow-test); the earlier carrier repair remains historical evidence.

This ground terminal joins the lower L1 on-ramp and off-ramp to the northwest Avenue arm. Each ramp approaches the Avenue at 90° and uses a finite right turn into or out of the adjacent carriageway. A carriageway is the part of a road carrying traffic in one direction. The turn has a 6 m centreline radius, labelled R6; there is no ramp movement across the opposing carriageway. The terminal asphalt keeps the 6 m-wide join to its grade, then narrows smoothly to 3.5 m over the first 3 m toward the Avenue. The remainder of the turn and its joining collar are 3.5 m wide.

Its three occupied tiles retain the native two-way Avenue and pedestrian channels. The 3.5 m asphalt leaves 0.5 m on each side of the checked 2.5 m-wide car corridor. Where a ramp runs parallel to an Avenue pedestrian centreline, the retained clearance to its asphalt edge is approximately 1.149 m; this measures a route centreline, not a promised sidewalk width. Each driveway still crosses a pedestrian route on the way into its carriageway. Adaptive pavement can appear beside that driveway, but no continuous sidewalk surface is drawn across the ramp asphalt. The visible turn models extend above some neighbouring owners, while their traffic fragments remain with the city tile they cross. All three native Avenue cells use the implemented adaptive-ground resources and rotating overlay models. The unused local [1,1] corner is the removable placement handle.

Adaptive sidewalks are implemented for all three Avenue cells of this component. The game selects a native Avenue pavement appearance from the surrounding development; connecting another Avenue alone does not force a sidewalk to appear. The rotating highway or ramp model is attached above that native ground artwork, and the pedestrian PATHs are separate retained traffic data. The complete new assembly still needs its own game observations. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **3 tiles inside a 2 × 2-tile rectangle**. Its reference position in the complete assembly is **P02: X3, Y6, at 0°**. Its actual occupied cells on that shared grid are **(X3, Y6), (X4, Y6), (X3, Y5)**. The [assembly construction picture](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X3, Y6**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** 0 m ground Avenue and right-turn pavement. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

<!-- BEGIN PIECE OVERVIEW -->

Place one northwest avenue right-turn terminal for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-northwest-terminal`.

Footprint: **2 × 2 tiles**. Exact menu name: **Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-3f154465659fba41604e) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · North exit**<br>`channel-06-out`<br>Variant: avenue-ground | **Road · South exit**<br>`channel-07-out`<br>Variant: access-ramp | **Road · North exit**<br>`channel-08-out`<br>Variant: avenue-ground | **Road · East exit**<br>`channel-09-out`<br>Variant: avenue-ground | **Road · East exit**<br>`channel-10-out`<br>Variant: avenue-ground | **Pedestrian · North exit**<br>`channel-13-out`<br>Variant: avenue-sidewalk | **Pedestrian · East exit**<br>`channel-14-out`<br>Variant: avenue-sidewalk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-88adf1d10e409b71703c) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f1a985e02baf99cf2c04)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f1a985e02baf99cf2c04) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c9b86c7368ec94764ca9) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-0912c59dd2e19e4f84f8)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-0912c59dd2e19e4f84f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c7a47db55578fcc3f69a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-32faeca94d2b625ca9b6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1484c5c0f687a9a68de9) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eac8f1216df59858bc08) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3ceb87d8baebfa265b10) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a03cf734c41a215c0af2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93bfa912fd79e86d34f2) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b22488a4e18858fc5be0)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b22488a4e18858fc5be0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3fa57168b1afda01ab8b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3d7ffa77e72935ec2ac9) |
| **Road · South entrance**<br>`channel-03-in`<br>Variant: avenue-ground | **Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c616a473fefd272719cc)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c616a473fefd272719cc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e9505f457944463710e5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9508e6366cca99b2f907) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b41db4dfec76bdc55871) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fe5187ec4a841d9f3447) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a0d903472d25b03505af) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a7130a951b3129a2539a) |
| **Road · South entrance**<br>`channel-04-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d5be1207b3b397d25c4a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93546c578dec5832ce87) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-757c82fed45f3a38f86c)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-757c82fed45f3a38f86c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5b64b500a41a08319b64) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3a8ea72cb097ddc0ab6b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e754535de867f195bd1e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9e4059c453cc5e7f96b3) |
| **Road · East entrance**<br>`channel-05-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-066437f1269f598e56f1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dab666cb41e67c3c5488) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-7748ada03d4888a35c7a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-7748ada03d4888a35c7a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-184fb48f711ce372a4d5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8204b71799bb9ce925cf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ae31cb9868fb5df6e9e6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2614e05187ab014fe037) |
| **Pedestrian · West entrance**<br>`channel-11-in`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-81cb624a037ffe649e89) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-40ccc7492c0198ef859c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-35b27a1a52db576dab7d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a537c2777e75e34478bb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-30b8419ddc16249a4611) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4b9a96331cbb3f95d232) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-a59e06a507334b9b0e44)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-a59e06a507334b9b0e44) |
| **Pedestrian · South entrance**<br>`channel-12-in`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7274c25e674a2d91f231) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a7af6a727d59ac040b3f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3cac43f7d10f6daf961a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fefefb234a9d28e2dc5b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e975447c99360e9d119a) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-6c4a479f93e3cb4f5e96)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-6c4a479f93e3cb4f5e96) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-118633f47b48c078753c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bed24ece32a5f8c8d64f) |

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

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 315° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 0 incoming; 2 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-06-out` / `channel-06-out` | `avenue-mainline-axis-plus-3-39411-positive` / `cut-channel-06-out` / car | Outgoing | `[-3.2,8,0]` | Not declared | 315° | 0 |
| `member-channel-08-out` / `channel-08-out` | `avenue-mainline-axis-plus-7-91960-positive` / `cut-channel-08-out` / car | Outgoing | `[3.2,8,0]` | Not declared | 315° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[0,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 315° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | walkway |
| Traffic modes | pedestrian |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-13-out` / `channel-13-out` | `avenue-walkways-axis-plus-10-81873-positive` / `cut-channel-13-out` / pedestrian | Outgoing | `[7.3,8,0]` | Not declared | 315° | 0 |

#### Boundary B: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 315° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 2 incoming; 0 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-01-in` / `channel-01-in` | `avenue-mainline-axis-minus-7-91960-negative` / `cut-channel-01-in` / car | Incoming | `[-8,-3.2,0]` | Not declared | 315° | 0 |
| `member-channel-02-in` / `channel-02-in` | `avenue-mainline-axis-minus-3-39411-negative` / `cut-channel-02-in` / car | Incoming | `[-8,3.2,0]` | Not declared | 315° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[0,0]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 315° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | walkway |
| Traffic modes | pedestrian |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-11-in` / `channel-11-in` | `avenue-walkways-axis-minus-10-81873-negative` / `cut-channel-11-in` / pedestrian | Incoming | `[-8,-7.3,0]` | Not declared | 315° | 0 |

#### Boundary C: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.311171 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.311171 m); no nominal level |
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
| `member-channel-07-out` / `channel-07-out` | `access-lower-on` / `cut-channel-07-out` / car | Outgoing | `[-0.970563,-24,0.311171]` | Not declared | 225° | 17.9118 |

#### Boundary D: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 135° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 0 incoming; 2 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-09-out` / `channel-09-out` | `avenue-mainline-axis-minus-7-91960-negative` / `cut-channel-09-out` / car | Outgoing | `[8,-19.2,0]` | Not declared | 135° | 0 |
| `member-channel-10-out` / `channel-10-out` | `avenue-mainline-axis-minus-3-39411-negative` / `cut-channel-10-out` / car | Outgoing | `[8,-12.8,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[0,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 135° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | walkway |
| Traffic modes | pedestrian |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-14-out` / `channel-14-out` | `avenue-walkways-axis-minus-10-81873-negative` / `cut-channel-14-out` / pedestrian | Outgoing | `[8,-23.3,0]` | Not declared | 135° | 0 |

#### Boundary E: `boundary-06`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 135° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 2 incoming; 0 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-03-in` / `channel-03-in` | `avenue-mainline-axis-plus-3-39411-positive` / `cut-channel-03-in` / car | Incoming | `[12.8,-8,0]` | Not declared | 135° | 0 |
| `member-channel-04-in` / `channel-04-in` | `avenue-mainline-axis-plus-7-91960-positive` / `cut-channel-04-in` / car | Incoming | `[19.2,-8,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[1,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 135° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | walkway |
| Traffic modes | pedestrian |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-12-in` / `channel-12-in` | `avenue-walkways-axis-plus-10-81873-positive` / `cut-channel-12-in` / pedestrian | Incoming | `[23.3,-8,0]` | Not declared | 135° | 0 |

#### Boundary F: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.311171 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.311171 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 17.9118% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-05-in` / `channel-05-in` | `access-lower-off` / `cut-channel-05-in` / car | Incoming | `[24,0.970563,0.311171]` | Not declared | 45° | 17.9118 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
