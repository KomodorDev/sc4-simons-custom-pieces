# DD RHW-4 — Lower Diagonal Exit Branch

Purpose: explain this reusable piece and its connections and test coverage.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

These angled and north-up views render the actual saved game models and their referenced textures. They show geometry and tile ownership; the game must still be inspected separately.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Lower Diagonal Exit Branch — Clean angled view](previews/preview.png)

![DD RHW-4 — Lower Diagonal Exit Branch — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

Divides an outer lower-deck lane into a continuing highway lane and an off-ramp towards the northwest avenue access. The branch is one diagonal city-grid step farther from the avenue than in the original layout. Its barrier opening belongs to the lower deck; the upper-deck edge remains closed here.

This branch uses a real flat auxiliary lane in the former highway shoulder, with a 12 m taper and a 4 m parallel section. Its saved driving path changes between the native outer through lane and that auxiliary lane. Native-material dashed separators and a painted split area identify the join; both highway through lanes remain available.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 3 tiles inside a 2 × 2-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Highways → SCP → Assemblies**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. The complete assembly’s source design allows four right turns between the highway and avenue; ramp traffic stays on the adjacent avenue carriageway. The graded ramps remain experimental, with a 30% authoring bound. Current saved-resource results and separate game observations belong in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Reusable lower exit branch component of the compact diagonal double-decker highway and Avenue interchange. Place its owned tiles exactly as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.

Exact reusable identifier: `ddrhw-diagonal-lower-exit-branch`.

Footprint: **2 × 2 tiles**. Exact menu name: **DD RHW-4 — Lower Diagonal Exit Branch**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-79c849dc4c10c431d268) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`1-W-out-1`<br>Variant: access-ramp | **Road · South exit**<br>`1-S-out-2`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`1-S-out-4`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`1-E-out-7`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`1-E-out-9`<br>Variant: dd-rhw-l2 | **Road · South exit**<br>`1-S-out-10`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`1-S-out-12`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`1-E-out-15`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`1-E-out-17`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`1-S-in-3`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a0dfa3225a65f150d43) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2a26e6f8329f6f702228) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7e98f33b8208396c2f8a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d7584c718450c186ca26) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-0aa99c1c1ff369beb3fb)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-0aa99c1c1ff369beb3fb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fbe8cd5bb6b7b2b22d50) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a4ae3447341af48ece3b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-543dd2d312a889bbf92b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b0fa894b87ad34625c28) |
| **Road · South entrance**<br>`1-S-in-5`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-286fca1c01bfdc4d37e9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a7691ef5009df474da2f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9b7961f1b49ee8d56c2e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-840d38a996e14eb90296)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-840d38a996e14eb90296) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e995e3f4a52027838d6d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1aba6a6647a56f261777) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f275a90b52fb4e6023d4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bd53be7470e6cefe87dc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-47d3e88d7eafc56e83d5) |
| **Road · East entrance**<br>`1-E-in-6`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a4b828cf050426f2ab1e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-98734d82783e642b1a92) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-9d376fdbc347837a7bec)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-9d376fdbc347837a7bec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-21d56aee84df3f050eaf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a2db489dcd650e14c5b9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-289a48fabd359b418b3d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-59b162891905d4960b21) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e985f44a68e5222d06d3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-385fff15d807461b9860) |
| **Road · East entrance**<br>`1-E-in-8`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b588eab832babf6d0d15) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-377218dbcaa7f6b480f8)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-377218dbcaa7f6b480f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-81cb9ee919a18c5a5f50) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6758b65869592bcfd8ff) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-073f74e80ccbfc5f39eb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-29a72cc6ace762628bbf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-51149c78e38aafff8ca0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-782c586cffb1a6bf0ad9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cc35a3915641b43a0804) |
| **Road · South entrance**<br>`1-S-in-11`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e6c7050828a18d4b955f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-40ac6b346dd7344b95fc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-46d0a5afa951d79df5cb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5a01df3a9626cfb134de) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c13f29f2d4e84ac99383) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-215bc2f08f48909dbc63) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5e6c79e0a0b73618e44f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f21d4cc8d3c63f1c5939) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-642e6b1a9bbba23df634)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-642e6b1a9bbba23df634) |
| **Road · South entrance**<br>`1-S-in-13`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-36c2a695ea353a0359e6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93403e41c8e4d3106bbc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c05399aa966a63899ffd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-daa52ab76f9f157d3b67) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fdc4a6b3f62c8d041299) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2e240cd1c6721e99c6c9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-de914ef281320c0305fe) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-34ce9b633a4d98a9fa5e)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-34ce9b633a4d98a9fa5e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c512da5128383c55cbba) |
| **Road · East entrance**<br>`1-E-in-14`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1c8fca840f99a758be90) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-706c3f453b25075b0e44) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f2b304eefcaba217dde5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-46a6038f25bc6eb34d08) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dd3dbf118d549dfd178d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5239dbb4689e04e6fc0b) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c6d276507b20deeb209e)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c6d276507b20deeb209e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dcc7ede179ece887b5d9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a951e4c7cea194b5e270) |
| **Road · East entrance**<br>`1-E-in-16`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1ce4d2571808b7fdfe35)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1ce4d2571808b7fdfe35) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1620b6193c983618aa4c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-523f5f70a1dbbed7d818) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-69f2f4a4cb455e716236) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-231009ad854cf6c30136) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-09642f3ddf122d9c5dc2)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-09642f3ddf122d9c5dc2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6b833e91ec0cc91dd968) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-169619b8c8a3f88aec0c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3727c56028b4bf909e92) |

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

#### Boundary A: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
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
| `member-1-s-out-2` / `1-S-out-2` | `lower-lane-02` / `cut-1-s-out-2` / car | Outgoing | `[-3.2,-24,7.5]` | Not declared | 225° | 0 |
| `member-1-s-out-4` / `1-S-out-4` | `lower-lane-01` / `cut-1-s-out-4` / car | Outgoing | `[3.2,-24,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
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
| `member-1-s-in-3` / `1-S-in-3` | `upper-lane-01` / `cut-1-s-in-3` / car | Incoming | `[-3.2,-24,15]` | Not declared | 225° | 0 |
| `member-1-s-in-5` / `1-S-in-5` | `upper-lane-02` / `cut-1-s-in-5` / car | Incoming | `[3.2,-24,15]` | Not declared | 225° | 0 |

#### Boundary B: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.74513 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.74513 m); no nominal level |
| Outward heading | 258.336° |
| Slope at joining edge | -22.6757% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-w-out-1` / `1-W-out-1` | `lower-ramp-01` / `cut-1-w-out-1` / car | Outgoing | `[-8,-10.2074,6.74513]` | Not declared | 258.336° | -22.6757 |

#### Boundary C: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
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
| `member-1-e-in-6` / `1-E-in-6` | `lower-lane-01` / `cut-1-e-in-6` / car | Incoming | `[8,-19.2,7.5]` | Not declared | 45° | 0 |
| `member-1-e-in-8` / `1-E-in-8` | `lower-lane-02` / `cut-1-e-in-8` / car | Incoming | `[8,-12.8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
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
| `member-1-e-out-7` / `1-E-out-7` | `upper-lane-02` / `cut-1-e-out-7` / car | Outgoing | `[8,-19.2,15]` | Not declared | 45° | 0 |
| `member-1-e-out-9` / `1-E-out-9` | `upper-lane-01` / `cut-1-e-out-9` / car | Outgoing | `[8,-12.8,15]` | Not declared | 45° | 0 |

#### Boundary D: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-lower-mainline-01` / `lower-mainline` |
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
| `member-1-s-out-10` / `1-S-out-10` | `lower-lane-04` / `cut-1-s-out-10` / car | Outgoing | `[12.8,-8,7.5]` | Not declared | 225° | 0 |
| `member-1-s-out-12` / `1-S-out-12` | `lower-lane-03` / `cut-1-s-out-12` / car | Outgoing | `[19.2,-8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-upper-mainline-02` / `upper-mainline` |
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
| `member-1-s-in-11` / `1-S-in-11` | `upper-lane-03` / `cut-1-s-in-11` / car | Incoming | `[12.8,-8,15]` | Not declared | 225° | 0 |
| `member-1-s-in-13` / `1-S-in-13` | `upper-lane-04` / `cut-1-s-in-13` / car | Incoming | `[19.2,-8,15]` | Not declared | 225° | 0 |

#### Boundary E: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
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
| `member-1-e-in-14` / `1-E-in-14` | `lower-lane-03` / `cut-1-e-in-14` / car | Incoming | `[24,-3.2,7.5]` | Not declared | 45° | 0 |
| `member-1-e-in-16` / `1-E-in-16` | `lower-lane-04` / `cut-1-e-in-16` / car | Incoming | `[24,3.2,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-02` / `upper-mainline` |
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
| `member-1-e-out-15` / `1-E-out-15` | `upper-lane-04` / `cut-1-e-out-15` / car | Outgoing | `[24,-3.2,15]` | Not declared | 45° | 0 |
| `member-1-e-out-17` / `1-E-out-17` | `upper-lane-03` / `cut-1-e-out-17` / car | Outgoing | `[24,3.2,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
