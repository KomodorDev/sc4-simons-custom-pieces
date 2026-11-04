# DD RHW-4 — Avenue Northwest Ramp Junction

Purpose: explain this reusable piece and its connections and test coverage.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

These angled and north-up views render the actual saved game models and their referenced textures. They show geometry and tile ownership; the game must still be inspected separately. The canonical models shown here remain a static reference for the approved geometry and ground artwork; these views do not simulate the sidewalk appearance selected by the game.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Avenue Northwest Ramp Junction — Clean angled view](previews/preview.png)

![DD RHW-4 — Avenue Northwest Ramp Junction — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

Contains the northwest surface junction and the lower-deck ramp landings. The lower off-ramp feeds only the avenue heading northwest, and the lower on-ramp receives only traffic arriving from the northwest. These right turns stay on their adjacent carriageway.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 6 tiles inside a 3 × 3-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Highways → SCP → Assemblies**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. The complete assembly’s source design allows four right turns between the highway and avenue; ramp traffic stays on the adjacent avenue carriageway. The graded ramps remain experimental, with a 30% authoring bound. Current saved-resource results and separate game observations belong in [TESTING.md](TESTING.md).

The Avenue-bearing tiles now use **adaptive ground**, meaning copies of native Avenue textures that allow the game to select a pavement appearance. A **T21 prop** is a model attached to a network tile; these props retain the decks, supports, slip lanes, and ramp mouths on those tiles. The complete saved car, pedestrian, and ramp routes are retained. This complete-component integration still needs fresh game checks; the isolated sidewalk prototype’s observed success does not establish a pass for this piece. See the [network specification](../../NETWORK_SPEC.md) and the [assembly testing guide](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Reusable northwest junction component of the compact diagonal double-decker highway and Avenue interchange. Place its owned tiles exactly as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.

Exact reusable identifier: `ddrhw-diagonal-northwest-junction`.

Footprint: **3 × 3 tiles**. Exact menu name: **DD RHW-4 — Avenue Northwest Ramp Junction**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-34cd157023b99598cfc5) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · North exit**<br>`1-N-out-3`<br>Variant: avenue-ground | **Road · South exit**<br>`1-S-out-4`<br>Variant: access-ramp | **Road · North exit**<br>`1-N-out-5`<br>Variant: avenue-ground | **Road · South exit**<br>`1-S-out-6`<br>Variant: avenue-ground | **Road · South exit**<br>`1-S-out-7`<br>Variant: avenue-ground | **Pedestrian · North exit**<br>`2-N-out-2`<br>Variant: avenue-sidewalk | **Pedestrian · South exit**<br>`2-S-out-3`<br>Variant: avenue-sidewalk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`1-W-in-1`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-834ac3947f711cb96404) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-2f1f10f712ae842e97eb)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-2f1f10f712ae842e97eb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-005afd9ca7d14c52b381) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-5addcd55361d1cc778a5)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-5addcd55361d1cc778a5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e8a91cf724ac908d4373) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6396ba8f92dba1a6e741) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b32a95376a0fee894319) |
| **Road · West entrance**<br>`1-W-in-2`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2573f0138b5dd192baf7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a6f3a32e442c881cf4d6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0a090f4eeb37d5ae0416) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7d7756ad2dd9dd66a490) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c6c42a5dc9869884c7da)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c6c42a5dc9869884c7da) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8443deca56ef38b8cccd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9af3246dde23d7134dc2) |
| **Road · East entrance**<br>`1-E-in-8`<br>Variant: avenue-ground | **Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-75f27b0db516fa487879)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-75f27b0db516fa487879) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5a311549567f40389429) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d385b2cab662231413cb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f76e2812164430e0d754) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ca77d88aeec38218de3c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9204cf10996063c8e3d8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7d9486698ccba3a5d2f9) |
| **Road · East entrance**<br>`1-E-in-9`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cd926acb2ec6a62036ec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a1df6c4bdd6f5d22f8dd) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-67fd1d42d3612f7b9672)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-67fd1d42d3612f7b9672) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c99d9def7b44771747e2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-62584aa6134bc1321845) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3643b44acf918dad4f55) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dc07daec12935f162b89) |
| **Road · East entrance**<br>`1-E-in-10`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-051b7f764b55905a0bf5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8828294d915200825d39) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-498864cd90aaee35d770)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-498864cd90aaee35d770) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-309dfbb42cccc6dd117c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9705250c4a874d2bc13c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-98956a5e7134950f96f9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b87346edb5d0d11042d1) |
| **Pedestrian · West entrance**<br>`2-W-in-1`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c71082290e55ca77a51d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ef156e0f530ad422d88b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f191a25d81dcfd1b287c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-82b7af222600793486e7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f93c1b87c8c0fd2bb938) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c2dd0d025a4d6991fa20) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-8dcce1e753fa8bddecbb)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-8dcce1e753fa8bddecbb) |
| **Pedestrian · East entrance**<br>`2-E-in-4`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-df3b4de4e128523adb18) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8a6414170c90be4a2295) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c2dd744b0582d0731079) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-aca552e48376b80ac99b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2aa915dbe0cc7e9d3bd3) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-782932c2204b52a33682)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-782932c2204b52a33682) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-aaad97762879968f7cfc)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a38685ac4a9aa431af3f) |

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
| `member-1-n-out-3` / `1-N-out-3` | `avenue-lane-03` / `cut-1-n-out-3` / car | Outgoing | `[-3.2,8,0]` | Not declared | 315° | 0 |
| `member-1-n-out-5` / `1-N-out-5` | `avenue-lane-04` / `cut-1-n-out-5` / car | Outgoing | `[3.2,8,0]` | Not declared | 315° | 0 |

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
| `member-2-n-out-2` / `2-N-out-2` | `avenue-walkway-02` / `cut-2-n-out-2` / pedestrian | Outgoing | `[7.3,8,0]` | Not declared | 315° | 0 |

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
| `member-1-w-in-1` / `1-W-in-1` | `avenue-lane-01` / `cut-1-w-in-1` / car | Incoming | `[-8,-3.2,0]` | Not declared | 315° | 0 |
| `member-1-w-in-2` / `1-W-in-2` | `avenue-lane-02` / `cut-1-w-in-2` / car | Incoming | `[-8,3.2,0]` | Not declared | 315° | 0 |

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
| `member-2-w-in-1` / `2-W-in-1` | `avenue-walkway-01` / `cut-2-w-in-1` / pedestrian | Incoming | `[-8,-7.3,0]` | Not declared | 315° | 0 |

#### Boundary C: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (3.00044 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (3.00044 m); no nominal level |
| Outward heading | 199.221° |
| Slope at joining edge | 22.6756% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-s-out-4` / `1-S-out-4` | `avenue-ramp-01` / `cut-1-s-out-4` / car | Outgoing | `[-1.75443,-40,3.00044]` | Not declared | 199.221° | 22.6756 |

#### Boundary D: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / South |
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
| `member-1-s-out-6` / `1-S-out-6` | `avenue-lane-01` / `cut-1-s-out-6` / car | Outgoing | `[12.8,-24,0]` | Not declared | 135° | 0 |
| `member-1-s-out-7` / `1-S-out-7` | `avenue-lane-02` / `cut-1-s-out-7` / car | Outgoing | `[19.2,-24,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[1,1]` / South |
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
| `member-2-s-out-3` / `2-S-out-3` | `avenue-walkway-01` / `cut-2-s-out-3` / pedestrian | Outgoing | `[8.7,-24,0]` | Not declared | 135° | 0 |

#### Boundary E: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / East |
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
| `member-1-e-in-8` / `1-E-in-8` | `avenue-lane-03` / `cut-1-e-in-8` / car | Incoming | `[24,-19.2,0]` | Not declared | 135° | 0 |
| `member-1-e-in-9` / `1-E-in-9` | `avenue-lane-04` / `cut-1-e-in-9` / car | Incoming | `[24,-12.8,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[1,1]` / East |
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
| `member-2-e-in-4` / `2-E-in-4` | `avenue-walkway-02` / `cut-2-e-in-4` / pedestrian | Incoming | `[24,-8.7,0]` | Not declared | 135° | 0 |

#### Boundary F: `boundary-06`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (3.00044 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (3.00044 m); no nominal level |
| Outward heading | 70.7789° |
| Slope at joining edge | 22.6756% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-e-in-10` / `1-E-in-10` | `avenue-ramp-02` / `cut-1-e-in-10` / car | Incoming | `[40,1.75443,3.00044]` | Not declared | 70.7789° | 22.6756 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
