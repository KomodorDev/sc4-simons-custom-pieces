# DD RHW-4 — Diagonal Two-Branch Stem — L1/L2

Purpose: Split the southwest stem’s two upper-deck lanes between the northwest and east branches, and bring their two lower-deck return lanes together.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical [angled view](previews/preview.png) and [north-up view](previews/preview-top.png) show this component by itself at 0°. The [thumbnail](previews/preview-thumb.png) identifies the same type in the assembly guide. Each city tile measures 16 × 16 m. Software renders show saved models and ownership; game appearance and moving traffic have separate checks in [TESTING](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Diagonal Two-Branch Stem — L1/L2 — Clean angled view](previews/preview.png)

![DD RHW-4 — Diagonal Two-Branch Stem — L1/L2 — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

**DD RHW-4** is a double-decker RealHighway: each deck is a carriageway carrying two lanes in one direction, and the other deck carries the opposite direction. Level 1, or L1, is 7.5 m above ground; Level 2, or L2, is 15 m. This component carries cars and supplies no Avenue, pedestrian route, ground-highway transition, or custom cast shadows.

This is the south component of the three-part Y junction. It contains the ordinary southwest DD connection and fragments of the four level journeys A→B, B→A, A→C, and C→A. Each outgoing choice uses one incoming lane; the opposing deck receives one returning lane from each branch. The two branch-to-branch climbs belong to the other components.

In the unrotated [complete Y junction](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md), A is the southwest stem, B is the northwest diagonal branch, and C is the east branch. The upper 15 m deck enters from the southwest, and the lower 7.5 m deck leaves toward the southwest. The exact reusable identifier is `ddrhw-y-diagonal-stem-split`, and the exact component name is **DD RHW-4 — Diagonal Two-Branch Stem — L1/L2**.

### 2.1 Owned cells and native approach

This component owns **8 cells inside a 5 × 3-tile rectangle**, measuring 80 × 48 m. The rectangle describes its surrounding extent; only the cells listed below are owned. Local source addresses are `(column,row)`: column 0 is the left column, row 0 is the top row, columns increase eastward, and rows increase southward. These source rows run opposite to the assembly picture’s northward Y labels.

| Local source row | Owned columns |
| --- | --- |
| 0 | 0, 1, 2, 3, and 4 |
| 1 | 1 and 2 |
| 2 | 1 |

A **PATH** resource stores a tile’s directed traffic routes. The model-only cells are (0,0), (4,0), (2,1), and (1,2). A model-only cell owns visible pavement, a barrier, or a support, but has an intentionally empty traffic PATH. Keep it clear of other construction just like a routed owned tile.

Its local reference (0,0) is an owned model-only shoulder tile. The southwest native socket is the unowned hole at local (0,1), next to the joining owner at (1,1). A **native socket** is an ordinary NAM DD highway tile requested beside the fixed custom construction. It remains unowned and draggable. The next outward native cell is local (0,2), immediately south of the socket. Further native cells follow the southwest staircase; keep both rows of that diagonal pattern available. The complete original cell list is maintained in [piece.jsonc](piece.jsonc).

### 2.2 Place the component

1. Use a verified experimental build with the audited NAM 50 right-hand-traffic inputs, following the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md). Building a DAT, which is a game-resource archive, does not install it. Close the game before replacing an installed revision, restart it afterward, and use a fresh placement for these new construction rules, models, and traffic paths.
2. Open a disposable city, flatten the whole construction area, and leave all owned cells and the native approach clear. For the full junction, follow the [assembly placement plan](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md#3-placements), which places this component as **P01** at **(X0, Y2)**, with a 0° rotation.
3. Open **Transportation → Highways → SCP → Assemblies**. In a prepared assembly menu, select **SCP | ASSEMBLY | DD RHW-4 — Compact Y-Junction — Diagonal Stem**, then press **Tab** or **Shift+Tab** until the tooltip shows **DD RHW-4 — Diagonal Two-Branch Stem — L1/L2**. In a normal piece-only build, look for this exact component under **Transportation → Highways → SCP → Pieces**.
4. Press **Home** or **End** until the model and complete occupied-cell shape match the north-up construction plan. Click once to place this component. The coordinate reference and the actual tile under the mouse cursor have not been confirmed in the game; match the whole ownership pattern, and keep an unowned reference at its planned address even when an ordinary native approach occupies that tile.
5. Inspect the native socket at local **(0,1)**, which is **(X0, Y1)** in the complete assembly. Cancel placement with **Esc**, select **RealHighway (RHW-2)**, and drag outward from that socket toward the **southwest** for at least three native tiles. Stop at the socket when dragging inward from an existing line; do not drag across the custom-owned cells.
6. Place the other two components at their exact assembly references. Only after the complete layout and its three native approaches are present can all six journeys be tested. Internal custom boundaries require every matching route fragment and model profile; an ordinary highway cannot replace a missing component there.

For a prebuilt control, open **Transportation → Highways → RealHighway (RHW) Starter Pieces**, press **Tab** until the name is **Double-Decker RHW-4 Starter Piece (Upper Deck: Level 2, Lower Deck: Level 1)**, place it, and extend the required straight approach with **RealHighway (RHW-2)**. The separately named rail-based DDRHW starter is a different network. Test drawing outward, drawing inward from a working line, and placing beside prebuilt approaches as separate cases; the native byte checks do not confirm those game operations.

### 2.3 Reuse and limits

A grade is height change divided by horizontal travel distance: 20% means a 2 m rise over 10 m horizontally. Every traffic fragment in this component is level at either 7.5 m or 15 m; its source maximum grade is 0%. The steep profiles are compact game choices. Native joins retain at least 3 m of flat lane collar. Four proper rotations turn the entire component through 0°, 90°, 180°, and 270°; the eight cursor states repeat those four orientations and provide no reflected version.

Only the first measured native grid alignment is implemented. Reusing this type elsewhere requires agreement across every exposed route, height, direction, physical surface, and ownership boundary. The internal tile cuts are not interchangeable standard ramp sockets. Keep its sparse owned cells, native socket, and outward native staircase or straight run intact.

<!-- BEGIN PIECE OVERVIEW -->

Native diagonal two-lane split and reverse merge, with the south paired flat approaches. Place its owned cells at the matching assembly reference; every native deck retains its measured real car lanes.

Exact reusable identifier: `ddrhw-y-diagonal-stem-split`.

Footprint: **5 × 3 tiles**. Exact menu name: **DD RHW-4 — Diagonal Two-Branch Stem — L1/L2**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix below describes journeys within this one component, including its cuts through longer assembly routes. It does not certify all six whole-junction journeys or compatibility with arbitrary neighbours. **Saved PATH** means the saved traffic-route check, **Route Query** means the route displayed by the game, and **Visible travel** means a vehicle actually completing the journey. Each has separate evidence in [TESTING](TESTING.md).

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-8dd3f87e7afcfba00d9f) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`c-a-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`b-a-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`a-b-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`a-c-out`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`a-c-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-77f1c900fe258b7d5ff6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c1aa9898b74e78fb2ee7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f14f906a332b7beae134) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ae295232fcc6398d685f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ae295232fcc6398d685f) |
| **Road · West entrance**<br>`a-b-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fee520848d6106a41efb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-286c0dd116f6c195ab83) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-26ff03bc2f7d4df07262)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-26ff03bc2f7d4df07262) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-245829ffeaf2fdc2ed4e) |
| **Road · North entrance**<br>`b-a-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5f0dcfd2577fd69658f8) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-14dc9ca383d5e46eefe9)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-14dc9ca383d5e46eefe9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-75bc57c11797c9a1a2bf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c871d332efb39158e9d1) |
| **Road · North entrance**<br>`c-a-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-98c763da81280e67def4)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-98c763da81280e67def4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ce3e0bada17c8bf3c396) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c2473d075ac8d7e555aa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-f58fa0449b197b459b98)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-363ae083d8a0a11e1ea9) |

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

#### Boundary A: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 14.9073° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-b-a-in` / `b-a-in` | `b-a` / `cut-b-a-in` / car | Incoming | `[22.3328,8,7.5]` | Not declared | 14.9073° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-dd-highway-02` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 14.9073° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-b-out` / `a-b-out` | `a-b` / `cut-a-b-out` / car | Outgoing | `[22.3328,8,15]` | Not declared | 14.9073° | 0 |

#### Boundary B: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / West |
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
| `member-b-a-out` / `b-a-out` | `b-a` / `cut-b-a-out` / car | Outgoing | `[8,-12.8,7.5]` | Not declared | 225° | 0 |
| `member-c-a-out` / `c-a-out` | `c-a` / `cut-c-a-out` / car | Outgoing | `[8,-19.2,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-dd-highway-02` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / West |
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
| `member-a-b-in` / `a-b-in` | `a-b` / `cut-a-b-in` / car | Incoming | `[8,-12.8,15]` | Not declared | 225° | 0 |
| `member-a-c-in` / `a-c-in` | `a-c` / `cut-a-c-in` / car | Incoming | `[8,-19.2,15]` | Not declared | 225° | 0 |

#### Boundary C: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-dd-highway-01` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[3,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 71.3571° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-c-a-in` / `c-a-in` | `c-a` / `cut-c-a-in` / car | Incoming | `[53.3218,8,7.5]` | Not declared | 71.3571° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-dd-highway-02` / `dd-highway` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[3,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 71.3571° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-c-out` / `a-c-out` | `a-c` / `cut-a-c-out` / car | Outgoing | `[53.3218,8,15]` | Not declared | 71.3571° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
