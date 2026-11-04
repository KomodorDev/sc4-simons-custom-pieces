# RHW Ramp — Upper Full Entry Ramp — R40

Purpose: Place the complete upper R40 entry ramp, including its curved high throat, separately from the straight highway stamp.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled and north-up pictures show the actual saved model in its authored 0° orientation. The connection overview records complete measured traffic boundaries, including their signed slopes. A software picture does not establish appearance or vehicle travel in the game.

<!-- BEGIN PIECE VIEWS -->

![RHW Ramp — Upper Full Entry Ramp — R40 — Clean angled view](previews/preview.png)

![RHW Ramp — Upper Full Entry Ramp — R40 — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This on-ramp, carrying cars from the Avenue onto the highway includes the complete visible curved ramp at the highway opening: pavement, a 1 m underside, Jersey barriers, and the joining bridge strips. Its high physical cut meets the straight upper deck at 15 m and 0% grade. Some model faces extend over highway-owned construction tiles; placing this ramp does not claim those tiles a second time.

The new circular sections have a 40 m horizontal centreline radius, which is what R40 means. The retained high throat is not an R40 curve. The lower end is flat, at 0 m, and includes a 1 m straight joining chord for the matching southeast R40 Avenue terminal.

This upper ramp has two traffic ports and one intrinsic journey between them. Its complete visible high throat can still overhang highway-owned tiles. Traffic follows the saved tile boundaries, while the physical model meets the highway at its flat native-edge cut.

A **construction tile** is a 16 × 16 m city square occupied by one piece. This type owns 6 tiles inside a 3 × 5-tile construction rectangle. Visible model overhang does not grant overlapping construction ownership. The assembly construction picture distinguishes the actual model outline from the owned tiles.

1. Prepare Windows SimCity 4 with the exact NAM 50 right-hand-traffic inputs in the [build guide](../../../../docs/BUILD_AND_INSTALL.md), including the adaptive Avenue capture for the stamp and terminals.
2. Open a disposable city, and flatten the full 10 × 10-tile assembly area.
3. Open **Transportation → Highways → SCP → Assemblies**, and select **SCP | ASSEMBLY | DD RHW-4 — Modular Diagonal Avenue Diamond**. Press **Tab** or **Shift+Tab** until **RHW Ramp — Upper Full Entry Ramp — R40** appears. Each click places this component only.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/README.md#3-placements) for this family's reference position. Use 0° for the reference layout; **Home** and **End** rotate the selected component. Align its occupied preview cells, including sparse shapes whose construction reference cell is empty.
5. Complete the matching seven-part layout, and connect native DD RHW-4 highway approaches and ordinary diagonal Avenue approaches at the outside ends. Placement over an existing Avenue and dragging through occupied pieces remain separate game tests.

These are fixed-height click-to-place components. They do not follow sloping terrain, acquire arbitrary height offsets, or establish draggable/FLEX compatibility. Four proper rotations repeat across eight selection states; none reflects traffic handedness. Match every required traffic boundary, and check the physical joining profiles separately in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Separately placed Upper Entry Ramp — R40. Includes its entire curved high throat at the highway cutout, including explicit model overhang. Construction and traffic-path ownership remain disjoint.

Exact reusable identifier: `ddrhw-modular-upper-entry-r40`.

Footprint: **3 × 5 tiles**. Exact menu name: **RHW Ramp — Upper Full Entry Ramp — R40**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. For the lower full ramps, its two fragments become one highway-to-Avenue journey only through the stamp-owned middle tile. Boundary cards describe saved traffic cuts; the physical native-edge opening is checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-9ab11444c9d7b0c8ab06) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · North exit**<br>`1-N-out-2`<br>Variant: dd-rhw-l2 |
| --- | --- |
| **Road · South entrance**<br>`1-S-in-1`<br>Variant: avenue-ground | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d3975890182d15048d6c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-e3b351baf41a6d4a3f95)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-e3b351baf41a6d4a3f95) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 4 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.

#### Boundary A: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-access-ramp-01` / `access-ramp` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,4]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 180° (South) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-s-in-1` / `1-S-in-1` | `access-ramp-01` / `cut-1-s-in-1` / car | Incoming | `[3.76854,-72,0]` | Not declared | 180° | 0 |

#### Boundary B: `boundary-02`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-access-ramp-01` / `access-ramp` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 23.446° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-n-out-2` / `1-N-out-2` | `access-ramp-01` / `cut-1-n-out-2` / car | Outgoing | `[14.6697,-8,15]` | Not declared | 23.446° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
