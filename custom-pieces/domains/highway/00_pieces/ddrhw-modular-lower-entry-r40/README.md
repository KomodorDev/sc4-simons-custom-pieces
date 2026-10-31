# RHW Ramp — Lower Full Entry Ramp — R40

Purpose: Place the complete lower R40 entry ramp, including its curved high throat, separately from the straight highway stamp.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled and north-up pictures show the actual saved model in its authored 0° orientation. The connection overview records complete measured traffic boundaries, including their signed slopes. A software picture does not establish appearance or vehicle travel in the game.

<!-- BEGIN PIECE VIEWS -->

![RHW Ramp — Lower Full Entry Ramp — R40 — Clean angled view](previews/preview.png)

![RHW Ramp — Lower Full Entry Ramp — R40 — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This on-ramp, carrying cars from the Avenue onto the highway includes the complete visible curved ramp at the highway opening: pavement, a 1 m underside, Jersey barriers, and the joining bridge strips. Its high physical cut meets the straight lower deck at 7.5 m and 0% grade. Some model faces extend over highway-owned construction tiles; placing this ramp does not claim those tiles a second time.

The new circular sections have a 40 m horizontal centreline radius, which is what R40 means. The retained high throat is not an R40 curve. The lower end is flat, at 0 m, and includes a 1 m straight joining chord for the matching northwest R40 Avenue terminal.

This lower ramp has four traffic ports and two intrinsic route fragments. An intrinsic fragment is the part of a traffic journey stored within this one piece. Between those fragments, the route crosses a highway-owned tile in the stamp. The visible ramp is continuous, but cars need the correctly placed stamp to join the fragments; the matrix does not promise a complete isolated highway-to-Avenue journey.

A **construction tile** is a 16 × 16 m city square occupied by one piece. This type owns 4 tiles inside a 2 × 3-tile construction rectangle. Visible model overhang does not grant overlapping construction ownership. The assembly construction picture distinguishes the actual model outline from the owned tiles.

1. Prepare Windows SimCity 4 with the exact NAM 50 right-hand-traffic inputs in the [build guide](../../../../docs/BUILD_AND_INSTALL.md), including the adaptive Avenue capture for the stamp and terminals.
2. Open a disposable city, and flatten the full 10 × 10-tile assembly area.
3. Open **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Modular Diagonal Avenue Diamond**. Press **Tab** or **Shift+Tab** until **RHW Ramp — Lower Full Entry Ramp — R40** appears. Each click places this component only.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/README.md#3-placements) for this family's reference position. Use 0° for the reference layout; **Home** and **End** rotate the selected component. Align its occupied preview cells, including sparse shapes whose construction reference cell is empty.
5. Complete the matching seven-part layout, and connect native DD RHW-4 highway approaches and ordinary diagonal Avenue approaches at the outside ends. Placement over an existing Avenue and dragging through occupied pieces remain separate game tests.

These are fixed-height click-to-place components. They do not follow sloping terrain, acquire arbitrary height offsets, or establish draggable/FLEX compatibility. Four proper rotations repeat across eight selection states; none reflects traffic handedness. Match every required traffic boundary, and check the physical joining profiles separately in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Separately placed Lower Entry Ramp — R40. Includes its entire curved high throat at the highway cutout, including explicit model overhang. Construction and traffic-path ownership remain disjoint.

Exact reusable identifier: `ddrhw-modular-lower-entry-r40`.

Footprint: **2 × 3 tiles**. Exact menu name: **RHW Ramp — Lower Full Entry Ramp — R40**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. For the lower full ramps, its two fragments become one highway-to-Avenue journey only through the stamp-owned middle tile. Boundary cards describe saved traffic cuts; the physical native-edge opening is checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-b673c66aa1974634cad8) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · South exit**<br>`1-S-out-1`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`1-S-out-3`<br>Variant: access-ramp |
| --- | --- | --- |
| **Road · East entrance**<br>`1-E-in-2`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c572434e9e4037f26161)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-7ccdc561d6bfc860bf84)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-7ccdc561d6bfc860bf84) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c572434e9e4037f26161)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3dbe19e56efdf5c49a69) |
| **Road · North entrance**<br>`1-N-in-4`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c572434e9e4037f26161)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-32908f9ea35fdf78039e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c572434e9e4037f26161)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-d388617b4443bc7ae40c)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-d388617b4443bc7ae40c) |

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

##### Service group 1 / 1: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-access-ramp-01` / `access-ramp` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 186.513° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-s-out-1` / `1-S-out-1` | `access-ramp-01` / `cut-1-s-out-1` / car | Outgoing | `[6.63407,-40,7.5]` | Not declared | 186.513° | 0 |

#### Boundary B: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-access-ramp-01` / `access-ramp` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 14.2641° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-e-in-2` / `1-E-in-2` | `access-ramp-01` / `cut-1-e-in-2` / car | Incoming | `[8,-33.9606,7.5]` | Not declared | 14.2641° | 0 |

#### Boundary C: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-access-ramp-01` / `access-ramp` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 0° (North) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-n-in-4` / `1-N-in-4` | `access-ramp-01` / `cut-1-n-in-4` / car | Incoming | `[12.2315,8,0]` | Not declared | 0° | 0 |

#### Boundary D: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.74513 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-access-ramp-01` / `access-ramp` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.74513 m); no nominal level |
| Outward heading | 191.664° |
| Slope at joining edge | 22.6757% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-s-out-3` / `1-S-out-3` | `access-ramp-01` / `cut-1-s-out-3` / car | Outgoing | `[10.2074,-24,6.74513]` | Not declared | 191.664° | 22.6757 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
