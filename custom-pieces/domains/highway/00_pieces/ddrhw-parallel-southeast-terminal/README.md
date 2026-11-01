# Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW — Clean angled view](previews/preview.png)

![Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

**Current shadow policy:** this component intentionally supplies no cast shadow, as do all fifteen parallel-kit components. After installing the checked revision and restarting, use a fresh placement to avoid confusing older saved attachments with the current result. Follow the assembly’s [no-shadow and cleanup checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#44-independent-module-shadow-test); the earlier carrier repair remains historical evidence.

This ground terminal joins the upper L2 on-ramp and off-ramp to the southeast Avenue arm. Each ramp approaches the Avenue at 90° and uses a finite right turn into or out of the adjacent carriageway. A carriageway is the part of a road carrying traffic in one direction. The turn has a 6 m centreline radius, labelled R6; there is no ramp movement across the opposing carriageway. The terminal asphalt keeps the 6 m-wide join to its grade, then narrows smoothly to 3.5 m over the first 3 m toward the Avenue. The remainder of the turn and its joining collar are 3.5 m wide.

Its three occupied tiles retain the native two-way Avenue and pedestrian channels. The 3.5 m asphalt leaves 0.5 m on each side of the checked 2.5 m-wide car corridor. Where a ramp runs parallel to an Avenue pedestrian centreline, the retained clearance to its asphalt edge is approximately 1.149 m; this measures a route centreline, not a promised sidewalk width. Each driveway still crosses a pedestrian route on the way into its carriageway. Adaptive pavement can appear beside that driveway, but no continuous sidewalk surface is drawn across the ramp asphalt. The visible turn models extend above some neighbouring owners, while their traffic fragments remain with the city tile they cross. All three native Avenue cells use the implemented adaptive-ground resources and rotating overlay models. The unused local [1,1] corner is the removable placement handle.

Adaptive sidewalks are implemented for all three Avenue cells of this component. The game selects a native Avenue pavement appearance from the surrounding development; connecting another Avenue alone does not force a sidewalk to appear. The rotating highway or ramp model is attached above that native ground artwork, and the pedestrian PATHs are separate retained traffic data. The complete new assembly still needs its own game observations. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **3 tiles inside a 2 × 2-tile rectangle**. Its reference position in the complete assembly is **P03: X5, Y4, at 0°**. Its actual occupied cells on that shared grid are **(X5, Y4), (X6, Y4), (X5, Y3)**. The [assembly construction picture](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X5, Y4**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** 0 m ground Avenue and right-turn pavement. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

<!-- BEGIN PIECE OVERVIEW -->

Place one southeast avenue right-turn terminal for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-southeast-terminal`.

Footprint: **2 × 2 tiles**. Exact menu name: **Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-1299f176a9f2715662e1) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · North exit**<br>`channel-06-out`<br>Variant: avenue-ground | **Road · North exit**<br>`channel-07-out`<br>Variant: avenue-ground | **Road · North exit**<br>`channel-08-out`<br>Variant: avenue-ground | **Road · East exit**<br>`channel-09-out`<br>Variant: avenue-ground | **Road · East exit**<br>`channel-10-out`<br>Variant: avenue-ground | **Pedestrian · North exit**<br>`channel-13-out`<br>Variant: avenue-sidewalk | **Pedestrian · East exit**<br>`channel-14-out`<br>Variant: avenue-sidewalk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6e14f82208382a71f170) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a2bb053161908030ef8d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2544a94456d75ac78985) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f1f3a3adb8761bd4394f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f1f3a3adb8761bd4394f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1057754f626888e6322d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c3691b679bea36802e18) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f62c40f0942fc78815d5) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a80209bee990964aaa7f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0f95c175f39d120db88c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cf2e326512a068a7ec2e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-7913d9835c08c5437360)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-7913d9835c08c5437360) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6e050c94512722c883b1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0564caff8654ec8d6be7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0f64abd5f89070c4a635) |
| **Road · West entrance**<br>`channel-03-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c0366f32a8a1fff7d0fa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d135479ed97b42257912) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-01d3c61ebbb94759b073) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cc604a3c4604f49361e3) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f77a11a467ab4fee0a90)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f77a11a467ab4fee0a90) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3bf53d3cb9ef692d34f4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9c952ee5b5823a85311c) |
| **Road · South entrance**<br>`channel-04-in`<br>Variant: avenue-ground | **Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-dde6ddba312e61808ffa)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-dde6ddba312e61808ffa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-79813c45d99feb01e5ba) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-20c18bbc05fbd091a92e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a4c347d79d4242e65a16) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-44a57e242701427950ae) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-70bf29af85c714b9e49f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-383c2942b58644dcf72c) |
| **Road · South entrance**<br>`channel-05-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d7e4d01ff4786ca4f570) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-83e959532d623cd67798)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-83e959532d623cd67798) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1cab22d8daf6dfcb2735)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1cab22d8daf6dfcb2735) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93b4267c1870233619dc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a1511b0b3f8d25bb65ce) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-522d1e164d0be3cd7c5a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a736ccd73fce5dd88b92) |
| **Pedestrian · West entrance**<br>`channel-11-in`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-417881c5dab0d59589e8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3e60cf6078bbb857fc91) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e42926d586af641e7097) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2363faeb784f66d4bece) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1524f783bf26a1c6d1af) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5873ac2a9efda77b3d66) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f04154c4f70c1a3c142a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f04154c4f70c1a3c142a) |
| **Pedestrian · South entrance**<br>`channel-12-in`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a758233b6f9e533a4804) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d0b30e2c60d6cead6b4e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fd04c81ca5b6b1d6834f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2d174dd4e7fea5b3259b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3dc854da2cfe913ad888) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-4aeb553200bd52ae4341)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-4aeb553200bd52ae4341) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-e7127b767359efa32b5e)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e52589fbaca8992c87a9) |

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
| Outward heading | Different; see members |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 3 / 3 / 3 |
| Traffic arrangement / running | 0 incoming; 3 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-06-out` / `channel-06-out` | `avenue-mainline-axis-plus-3-39411-positive` / `cut-channel-06-out` / car | Outgoing | `[-3.2,8,0]` | Not declared | 315° | 0 |
| `member-channel-07-out` / `channel-07-out` | `avenue-mainline-axis-plus-7-91960-positive` / `cut-channel-07-out` / car | Outgoing | `[3.2,8,0]` | Not declared | 315° | 0 |
| `member-channel-08-out` / `channel-08-out` | `access-upper-on` / `cut-channel-08-out` / car | Outgoing | `[4.67515,8,0]` | Not declared | 349.579° | 0 |

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
| Outward heading | Different; see members |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 3 / 3 / 3 |
| Traffic arrangement / running | 3 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-01-in` / `channel-01-in` | `access-upper-off` / `cut-channel-01-in` / car | Incoming | `[-8,-4.67515,0]` | Not declared | 280.421° | 0 |
| `member-channel-02-in` / `channel-02-in` | `avenue-mainline-axis-minus-7-91960-negative` / `cut-channel-02-in` / car | Incoming | `[-8,-3.2,0]` | Not declared | 315° | 0 |
| `member-channel-03-in` / `channel-03-in` | `avenue-mainline-axis-minus-3-39411-negative` / `cut-channel-03-in` / car | Incoming | `[-8,3.2,0]` | Not declared | 315° | 0 |

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

#### Boundary C: `boundary-03`

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

#### Boundary D: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-mainline-01` / `avenue-mainline` |
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
| `member-channel-04-in` / `channel-04-in` | `avenue-mainline-axis-plus-3-39411-positive` / `cut-channel-04-in` / car | Incoming | `[12.8,-8,0]` | Not declared | 135° | 0 |
| `member-channel-05-in` / `channel-05-in` | `avenue-mainline-axis-plus-7-91960-positive` / `cut-channel-05-in` / car | Incoming | `[19.2,-8,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-walkways-02` / `avenue-walkways` |
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

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
