# DD RHW-4 — Orthogonal Y Connection Core — L1/L2

Purpose: Provide the east DD branch and the middle-band connections that join the two diagonal components into one Y junction.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical [angled view](previews/preview.png) and [north-up view](previews/preview-top.png) show this component by itself at 0°. The [thumbnail](previews/preview-thumb.png) identifies the same type in the assembly guide. Each city tile measures 16 × 16 m. Software renders show saved models and ownership; game appearance and moving traffic have separate checks in [TESTING](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Clean angled view](previews/preview.png)

![DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

**DD RHW-4** is a double-decker RealHighway: each deck is a carriageway carrying two lanes in one direction, and the other deck carries the opposite direction. Level 1, or L1, is 7.5 m above ground; Level 2, or L2, is 15 m. This component carries cars and supplies no Avenue, pedestrian route, ground-highway transition, or custom cast shadows.

This is the centre component of the three-part Y junction. Orthogonal means aligned with a horizontal or vertical city-grid line. Its native east socket has two outgoing upper lanes and two incoming lower lanes. The five owned cells carry fragments of all six journeys, including the middle portions of the two branch-to-branch climbs. The adjoining diagonal pieces complete those journeys.

In the unrotated [complete Y junction](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md), A is the southwest stem, B is the northwest diagonal branch, and C is the east branch. The lower 7.5 m deck enters from the east, and the upper 15 m deck leaves toward the east. The exact reusable identifier is `ddrhw-y-orthogonal-core`, and the exact component name is **DD RHW-4 — Orthogonal Y Connection Core — L1/L2**.

### 2.1 Owned cells and native approach

This component owns **5 cells inside a 5 × 1-tile rectangle**, measuring 80 × 16 m. The rectangle describes its surrounding extent; only the cells listed below are owned. Local source addresses are `(column,row)`: column 0 is the left column, row 0 is the top row, columns increase eastward, and rows increase southward. These source rows run opposite to the assembly picture’s northward Y labels.

| Local source row | Owned columns |
| --- | --- |
| 0 | 0, 1, 2, 3, and 4 |

A **PATH** resource stores a tile’s directed traffic routes. All five owned cells contain traffic fragments. A pavement or support projecting beyond a tile edge is not permission to replace the neighbouring native socket.

Its local reference (0,0) is owned. All five cells in row 0 are owned. The east native socket is local (5,0), immediately beyond the rectangle, next to the joining owner at (4,0). A **native socket** is an ordinary NAM DD highway tile requested beside the fixed custom construction. It remains unowned and draggable. The next outward native cell is local (6,0), followed by the same straight row. Keep that eastward continuation clear. The complete original cell list is maintained in [piece.jsonc](piece.jsonc).

### 2.2 Place the component

1. Use a verified experimental build with the audited NAM 50 right-hand-traffic inputs, following the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md). Building a DAT, which is a game-resource archive, does not install it. Close the game before replacing an installed revision, restart it afterward, and use a fresh placement for these new construction rules, models, and traffic paths.
2. Open a disposable city, flatten the whole construction area, and leave all owned cells and the native approach clear. For the full junction, follow the [assembly placement plan](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md#3-placements), which places this component as **P03** at **(X1, Y3)**, with a 0° rotation.
3. Open **Transportation → Highways → SCP → Assemblies**. In a prepared assembly menu, select **SCP | ASSEMBLY | DD RHW-4 — Compact Y-Junction — Diagonal Stem**, then press **Tab** or **Shift+Tab** until the tooltip shows **DD RHW-4 — Orthogonal Y Connection Core — L1/L2**. In a normal piece-only build, look for this exact component under **Transportation → Highways → SCP → Pieces**.
4. Press **Home** or **End** until the model and complete occupied-cell shape match the north-up construction plan. Click once to place this component. The coordinate reference and the actual tile under the mouse cursor have not been confirmed in the game; match the whole ownership pattern, and keep an unowned reference at its planned address even when an ordinary native approach occupies that tile.
5. Inspect the native socket at local **(5,0)**, which is **(X6, Y3)** in the complete assembly. Cancel placement with **Esc**, select **RealHighway (RHW-2)**, and drag outward from that socket toward the **east** for at least three native tiles. Stop at the socket when dragging inward from an existing line; do not drag across the custom-owned cells.
6. Place the other two components at their exact assembly references. Only after the complete layout and its three native approaches are present can all six journeys be tested. Internal custom boundaries require every matching route fragment and model profile; an ordinary highway cannot replace a missing component there.

For a prebuilt control, open **Transportation → Highways → RealHighway (RHW) Starter Pieces**, press **Tab** until the name is **Double-Decker RHW-4 Starter Piece (Upper Deck: Level 2, Lower Deck: Level 1)**, place it, and extend the required straight approach with **RealHighway (RHW-2)**. The separately named rail-based DDRHW starter is a different network. Test drawing outward, drawing inward from a working line, and placing beside prebuilt approaches as separate cases; the native byte checks do not confirm those game operations.

### 2.3 Reuse and limits

A grade is height change divided by horizontal travel distance: 20% means a 2 m rise over 10 m horizontally. Its source maximum grade is approximately 25.7614%, below the declared 30% experimental limit. Some internal fragments are graded between 7.5 m and 15 m, even though both lanes are level where they meet the ordinary east DD socket. The steep profiles are compact game choices. Native joins retain at least 3 m of flat lane collar. Four proper rotations turn the entire component through 0°, 90°, 180°, and 270°; the eight cursor states repeat those four orientations and provide no reflected version.

Only the first measured native grid alignment is implemented. Reusing this type elsewhere requires agreement across every exposed route, height, direction, physical surface, and ownership boundary. The internal tile cuts are not interchangeable standard ramp sockets. Keep its sparse owned cells, native socket, and outward native staircase or straight run intact.

<!-- BEGIN PIECE OVERVIEW -->

Native orthogonal branch and the coordinated middle-band services. Place its owned cells at the matching assembly reference; every native deck retains its measured real car lanes.

Exact reusable identifier: `ddrhw-y-orthogonal-core`.

Footprint: **5 × 1 tiles**. Exact menu name: **DD RHW-4 — Orthogonal Y Connection Core — L1/L2**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix below describes journeys within this one component, including its cuts through longer assembly routes. It does not certify all six whole-junction journeys or compatibility with arbitrary neighbours. **Saved PATH** means the saved traffic-route check, **Route Query** means the route displayed by the game, and **Visible travel** means a vehicle actually completing the journey. Each has separate evidence in [TESTING](TESTING.md).

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-7b47c61cd93d472d23bf) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · South exit**<br>`b-a-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`a-b-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`c-b-out`<br>Variant: access-ramp | **Road · South exit**<br>`c-a-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`a-c-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`b-c-out`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`a-b-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8a598487f2cb8723053d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ad3a62fb3abdf9bd32da)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ad3a62fb3abdf9bd32da) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-399e6a82d788131de970) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b264301f08efa140cde0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0ff359998dc787fd0bf7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-711418f31c8083859399) |
| **Road · North entrance**<br>`b-a-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c00a9157f52df70eed63)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c00a9157f52df70eed63) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5cc2830b759159391b8e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a848f5ac095e237a98eb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e571dcadba671e7852c2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-448c8498f83da7f41448) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2f4759c325df88453ec7) |
| **Road · South entrance**<br>`a-c-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-23728c801a8cc82a9247) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e09d314a4c4c70b0771f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-929810e76bde033a26dd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9ac5e8636e303a7525a8) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-eff29eba74f513fffcf6)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-eff29eba74f513fffcf6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-60077694812620e0914d) |
| **Road · North entrance**<br>`b-c-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9cb3397e2ac3145193ec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-02daadb9c2f5a0631ee1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b3288e87f7248b179b02) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b1fb86aca9a9132d2a5d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ee4dab0ddd2d1be2f3de) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-d4ec97c3ec60731a7f8f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-d4ec97c3ec60731a7f8f) |
| **Road · East entrance**<br>`c-a-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9f7499e94d3bf51fe408) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8da99f05598d72bd7e63) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-27a318cb6a0874bed1e7) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-fc3d67bfd91d39d5603e)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-fc3d67bfd91d39d5603e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8b58476523ff247c8324) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4a62bae02a28c582b021) |
| **Road · East entrance**<br>`c-b-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5a510a5a2e0a9f7349b8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-15e50f715ddcfde5d058) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-dcc1d39b9b93f6ccba9d)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-dcc1d39b9b93f6ccba9d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0c24aa42330514462b9b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-58996679166633727c4a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3464132ecedeb9f50)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-66a07baa459df102ae1c) |

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

#### Boundary A: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 194.907° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-b-a-out` / `b-a-out` | `b-a` / `cut-b-a-out` / car | Outgoing | `[6.33277,-8,7.5]` | Not declared | 194.907° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-dd-highway-02` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 194.907° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-b-in` / `a-b-in` | `a-b` / `cut-a-b-in` / car | Incoming | `[6.33277,-8,15]` | Not declared | 194.907° | 0 |

#### Boundary B: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 345.093° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-b-a-in` / `b-a-in` | `b-a` / `cut-b-a-in` / car | Incoming | `[6.33277,8,7.5]` | Not declared | 345.093° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-dd-highway-02` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 345.093° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-b-out` / `a-b-out` | `a-b` / `cut-a-b-out` / car | Outgoing | `[6.33277,8,15]` | Not declared | 345.093° | 0 |

#### Boundary C: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (12.1595 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (12.1595 m); no nominal level |
| Outward heading | 296.834° |
| Slope at joining edge | 24.8977% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-c-b-out` / `c-b-out` | `c-b` / `cut-c-b-out` / car | Outgoing | `[23.7,8,12.1595]` | Not declared | 296.834° | 24.8977 |

#### Boundary D: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 251.357° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-c-a-out` / `c-a-out` | `c-a` / `cut-c-a-out` / car | Outgoing | `[37.3218,-8,7.5]` | Not declared | 251.357° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-dd-highway-02` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 251.357° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-c-in` / `a-c-in` | `a-c` / `cut-a-c-in` / car | Incoming | `[37.3218,-8,15]` | Not declared | 251.357° | 0 |

#### Boundary E: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (14.7115 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[3,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (14.7115 m); no nominal level |
| Outward heading | 297.491° |
| Slope at joining edge | -8.58944% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-b-c-in` / `b-c-in` | `b-c` / `cut-b-c-in` / car | Incoming | `[46.2479,8,14.7115]` | Not declared | 297.491° | -8.58944 |

#### Boundary F: `boundary-06`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[4,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 90° (East) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 2 incoming; 0 outgoing; See member directions |
| Channel spacing | 5 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-c-a-in` / `c-a-in` | `c-a` / `cut-c-a-in` / car | Incoming | `[72,-2.5,7.5]` | Not declared | 90° | 0 |
| `member-c-b-in` / `c-b-in` | `c-b` / `cut-c-b-in` / car | Incoming | `[72,2.5,7.5]` | Not declared | 90° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-dd-highway-02` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[4,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 90° (East) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 0 incoming; 2 outgoing; See member directions |
| Channel spacing | 5 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-c-out` / `a-c-out` | `a-c` / `cut-a-c-out` / car | Outgoing | `[72,-2.5,15]` | Not declared | 90° | 0 |
| `member-b-c-out` / `b-c-out` | `b-c` / `cut-b-c-out` / car | Outgoing | `[72,2.5,15]` | Not declared | 90° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
