# DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Reversed Traffic

Purpose: Supply the orthogonal y connection core component of the reversed-traffic compact DD RHW Y junction, with yellow on the driver's left.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The [angled view](previews/preview.png), [north-up view](previews/preview-top.png), and [thumbnail](previews/preview-thumb.png) show this component alone at 0°. A city tile measures 16 × 16 m. The pictures are software renders of saved models; game appearance and moving traffic have separate observations in [TESTING](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Reversed Traffic — Clean angled view](previews/preview.png)

![DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Reversed Traffic — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

**DD RHW-4** is a double-decker RealHighway with two lanes per travel deck. Level 1, or L1, is 7.5 m above ground; Level 2, or L2, is 15 m. The two decks carry opposite directions. A **PATH** resource stores directed traffic routes, and a **DAT** file is an archive containing game resources. This component carries cars and supplies no ground-highway transition or pedestrian route. Custom cast shadows are disabled.

The east upper deck carries traffic into the junction at 15 m. Its lower deck carries traffic out at 7.5 m. This owner contains the east connection and the coordinated middle band of the six journeys. In the [complete assembly](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/README.md), A is southwest, B is northwest, and C is east. Every directed journey is the reverse of the corresponding original Y journey. The physical arm positions remain the same. Yellow is on the driver's left on every deck; this is a separate type, so the original remains selectable.

### 2.1 Owned cells and native approach

This type owns **5 city tiles inside a 5 × 1-tile rectangle**. Only the cells listed below are occupied. Local source addresses are (column,row): columns increase eastward, and rows increase southward. The complete permanent definition is [piece.jsonc](piece.jsonc).

| Local source row | Owned columns |
| --- | --- |
| 0 | 0, 1, 2, 3, and 4 |

Every owned cell contains a traffic PATH. The model and traffic fragments in each cell have one construction owner.

Its local reference (0,0) is occupied. The east native socket is immediately outside the five-cell row. A **native socket** is an ordinary NAM DD highway tile beside the custom component. This component's socket is unowned at local **(5,0)**, or **(X6, Y3)** in the complete assembly. Reserve the outward **east** approach as a straight row along Y3. A component owns all road, barrier, support, and route fragments inside each of its occupied cells, even when several journeys cross that cell.

### 2.2 Place the component

1. Use a deliberately installed, verified experimental build with the audited NAM 50 right-hand-traffic inputs. Follow the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md). Close SimCity 4 before changing plugin files, restart it afterward, and place this new revision afresh.
2. Prepare a flat area using the [complete placement plan](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/README.md#3-placements). This component is **P03**, with its reference at **(X1, Y3)** and a **0°** rotation. The complete assembly occupies 21 tiles within a 6 × 7-tile rectangle; leave additional native continuation space outside it.
3. Open **Transportation → Highways → SCP → Assemblies**, and select **SCP | ASSEMBLY | DD RHW-4 — Compact Y-Junction — Diagonal Stem — Reversed Traffic**. Press **Tab** or **Shift+Tab** until the tooltip shows **DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Reversed Traffic**. Each click places only one component.
4. Press **Home** or **End** until the model and all occupied cells match the north-up construction view. Keep the reference at the stated address, including when it is unowned. The actual cursor anchor still requires a game observation, so compare the complete occupied shape before clicking once.
5. Inspect the ordinary native tile at **(X6, Y3)**. Cancel placement with **Esc**, choose **RealHighway (RHW-2)**, and drag outward toward the **east** for at least three native tiles. Do not drag across the custom-owned cells. Record automatic socket appearance, outward dragging, and attachment to a prebuilt native approach as separate game checks.
6. Place the other two components at their exact references. Test all six journeys only after all components and three native approaches are complete.

For a prebuilt native control, select **Transportation → Highways → RealHighway (RHW) Starter Pieces**, and press **Tab** until the tooltip reads **Double-Decker RHW-4 Starter Piece (Upper Deck: Level 2, Lower Deck: Level 1)**. Place it, and extend it with **RealHighway (RHW-2)**. Match the reversed component's straight east–west alignment and deck directions: the upper deck enters from the east, and the lower deck leaves toward the east. The separately named rail-based DDRHW starter uses a different network.

### 2.3 Reuse and limits

The exact reusable identifier is `ddrhw-y-reversed-orthogonal-core`. Four proper rotations turn the whole type through 0°, 90°, 180°, and 270°. Its eight cursor states repeat those four orientations; they do not reflect the layout. Reuse requires matching every exposed lane, direction, height, cross-section, and ownership boundary. An internal component cut is not an arbitrary native highway socket.

A **grade** is vertical height change divided by horizontal distance. For example, a 20% descent loses 2 m in 10 m horizontally. The complete reversed assembly has four level journeys and two separate descents from 15 m to 7.5 m. Their peak absolute grades are approximately 25.761% for B→C and 26.572% for C→B, below the experimental 30% ceiling. These compact game choices still require visible-vehicle checks.

<!-- BEGIN PIECE OVERVIEW -->

Native orthogonal branch and the coordinated middle-band services; all directed journeys and their driver-left markings are reversed. Place its owned cells at the matching assembly reference; every native deck retains its measured real car lanes.

Exact reusable identifier: `ddrhw-y-reversed-orthogonal-core`.

Footprint: **5 × 1 tiles**. Exact menu name: **DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Reversed Traffic**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes this component's saved route fragments. Whole-junction journeys require all three placements. **Saved PATH** checks the stored routes, **Route Query** checks the route shown by the game, and **Visible travel** checks an actual vehicle. These have separate evidence in [TESTING](TESTING.md).

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-af8a4bc9c7efcb882175) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · South exit**<br>`b-a-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`a-b-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`c-a-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`c-b-out`<br>Variant: access-ramp | **Road · East exit**<br>`a-c-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`b-c-out`<br>Variant: dd-rhw-l1 |
| --- | --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`a-b-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9ed4f7db290a92c79c0d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-fe7c01d49b0a96b35427)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-fe7c01d49b0a96b35427) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5f86d7591cba70996ab9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b3d7bef5f9c3c46f4493) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-369f2af1254a78f5c508) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5cb4f8e8aee96086e3cf) |
| **Road · North entrance**<br>`b-a-in`<br>Variant: dd-rhw-l2 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-5b96428d575eba8323cf)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-5b96428d575eba8323cf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5de982b8f0b9d6f5e38f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-55cc930e52335e08626c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cc46e053ca83f7d22e39) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a37a4c60befe02fc1173) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6e26e24f03c2b3fa95be) |
| **Road · North entrance**<br>`b-c-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-652509d59657d33910da) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a06e8cc542d6eed20309) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ccface7371e74e8d677f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ceaec1a2a592a6837470) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2ebcad5dce135b4667c3) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-295add80c99d169bf040)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-295add80c99d169bf040) |
| **Road · South entrance**<br>`a-c-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a378e7ad8a89c2c8332c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b3c70abb4a1dc3ada96c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-842314025ba5d77c97c3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e0a35844d3871430ec16) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-213f3d041b6219b97307)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-213f3d041b6219b97307) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ef468d3be70dadf5a303) |
| **Road · East entrance**<br>`c-a-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0ff679700e06e6ccd3a0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9dadf5649f2b29173b49) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1dd6bd6a13b810ad058f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1dd6bd6a13b810ad058f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e19646300424981c2cbe) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-05de2e86bd72c422ac31) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2b09dff078e41000d50d) |
| **Road · East entrance**<br>`c-b-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2d52096fa98119e54780) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8cddc0af8afe11c00823) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-905aa8d40901cfbd4640) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-334e8545d173f700a70a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-334e8545d173f700a70a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-48c03611c62e106192f0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-4165cba542545e361c35)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-519d5bc9c14c5b345f92) |

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
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-b-in` / `a-b-in` | `a-b` / `cut-a-b-in` / car | Incoming | `[6.33277,-8,7.5]` | Not declared | 194.907° | 0 |

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
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-b-a-out` / `b-a-out` | `b-a` / `cut-b-a-out` / car | Outgoing | `[6.33277,-8,15]` | Not declared | 194.907° | 0 |

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
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-b-out` / `a-b-out` | `a-b` / `cut-a-b-out` / car | Outgoing | `[6.33277,8,7.5]` | Not declared | 345.093° | 0 |

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
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-b-a-in` / `b-a-in` | `b-a` / `cut-b-a-in` / car | Incoming | `[6.33277,8,15]` | Not declared | 345.093° | 0 |

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
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-b-c-in` / `b-c-in` | `b-c` / `cut-b-c-in` / car | Incoming | `[23.7,8,12.1595]` | Not declared | 296.834° | 24.8977 |

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
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-c-in` / `a-c-in` | `a-c` / `cut-a-c-in` / car | Incoming | `[37.3218,-8,7.5]` | Not declared | 251.357° | 0 |

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
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-c-a-out` / `c-a-out` | `c-a` / `cut-c-a-out` / car | Outgoing | `[37.3218,-8,15]` | Not declared | 251.357° | 0 |

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
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-c-b-out` / `c-b-out` | `c-b` / `cut-c-b-out` / car | Outgoing | `[46.2479,8,14.7115]` | Not declared | 297.491° | -8.58944 |

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
| Traffic arrangement / running | 0 incoming; 2 outgoing; See member directions |
| Channel spacing | 5 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-a-c-out` / `a-c-out` | `a-c` / `cut-a-c-out` / car | Outgoing | `[72,-2.5,7.5]` | Not declared | 90° | 0 |
| `member-b-c-out` / `b-c-out` | `b-c` / `cut-b-c-out` / car | Outgoing | `[72,2.5,7.5]` | Not declared | 90° | 0 |

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
| Traffic arrangement / running | 2 incoming; 0 outgoing; See member directions |
| Channel spacing | 5 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-c-a-in` / `c-a-in` | `c-a` / `cut-c-a-in` / car | Incoming | `[72,-2.5,15]` | Not declared | 90° | 0 |
| `member-c-b-in` / `c-b-in` | `c-b` / `cut-c-b-in` / car | Incoming | `[72,2.5,15]` | Not declared | 90° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
