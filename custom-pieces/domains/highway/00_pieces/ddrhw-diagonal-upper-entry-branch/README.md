# DD RHW-4 — Upper Diagonal Entry Branch

Purpose: explain this reusable piece and its connections and test coverage.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

These angled and north-up views render the actual saved game models and their referenced textures. They show geometry and tile ownership; the game must still be inspected separately.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Upper Diagonal Entry Branch — Clean angled view](previews/preview.png)

![DD RHW-4 — Upper Diagonal Entry Branch — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

Fresh placement also requests one native NAM DD approach tile beyond its exposed highway end. Reserve that extra 16 × 16 m native plot outside the fixed footprint shown in the pictures. The retained models and traffic paths are unchanged. This [native highway connection experiment](../../NETWORK_SPEC.md#12-native-highway-approach-experiment) needs a game test, and existing city placements must be replaced to run the new construction request.

Merges the on-ramp from the southeast avenue access into an outer upper-deck lane. Its final section stays level above the lower deck. The opposite upper-deck edge remains closed, and the branch owns the outer native cell crossed by its ramp faces.

This branch uses a real flat auxiliary lane in the former highway shoulder, with a 16 m taper and a 8 m parallel section. Its saved driving path changes between the native outer through lane and that auxiliary lane. Native-material dashed separators and a painted split area identify the join; both highway through lanes remain available.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 6 tiles inside a 3 × 3-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Highways**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. The complete assembly’s source design allows four right turns between the highway and avenue; ramp traffic stays on the adjacent avenue carriageway. The graded ramps remain experimental, with a 30% authoring bound. Current saved-resource results and separate game observations belong in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Reusable upper entry branch component of the compact diagonal double-decker highway and Avenue interchange. Place its owned tiles exactly as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.

Exact reusable identifier: `ddrhw-diagonal-upper-entry-branch`.

Footprint: **3 × 3 tiles**. Exact menu name: **DD RHW-4 — Upper Diagonal Entry Branch**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-e3e03a745a6696759c92) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`1-W-out-1`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`1-W-out-3`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`1-N-out-6`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`1-N-out-8`<br>Variant: dd-rhw-l2 | **Road · West exit**<br>`1-W-out-9`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`1-W-out-11`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`1-N-out-15`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`1-N-out-17`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`1-W-in-2`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b0aee0d649fbcb98b476) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7d1d1b2d29096bf5913c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-695f02d1c34621886a25) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-312697fbd48dee48f659)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-312697fbd48dee48f659) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3a24c754d90ec99df446) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2d3dac869b3d07eaf373) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8ee4bd7183779ec5853c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-aff639267f9f7fcd293d) |
| **Road · West entrance**<br>`1-W-in-4`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0ebb55c4cb8b0aeca591) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b20bdacd6ae5f60e5abf) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-07b604fd15d6ff2af07a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-07b604fd15d6ff2af07a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f5b23f1709a12ff183cf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ade5156c8adba798613b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6068810aa5adb992a035) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ebba66d21f65e164e163) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-22b2b91b8c865bba3dfa) |
| **Road · North entrance**<br>`1-N-in-5`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-92b0a12950dd954e6d7f) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-532a7dc7b158b92dbe73)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-532a7dc7b158b92dbe73) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-850f572991d629717868) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f268add71f2a26500e47) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9cb1292a8911ee6276b2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b7bc8907fddc6da3c542) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a612be1ffbdef55037a5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-250e27f1320e9179581f) |
| **Road · North entrance**<br>`1-N-in-7`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-103469cee15692a2af75)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-103469cee15692a2af75) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e0e4dd002b59153e18e9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-08bd786b0633143a951f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-53cf22c1f3f269a5a814) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-79e8139231c2667c70ec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bc35220c34cecdd8cb37) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e6cf515ab5c56d47e7ad) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ab914021d3b168f09d8d) |
| **Road · West entrance**<br>`1-W-in-10`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-52b8729068dca5035cbb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-83ae180da58159709598) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bb63cc8ec4de8afdd610) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9326b84e8e403fb3d3f1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-42239666222bb50e6e2d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c15dc450eccfda9eea6e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7c22d33589e983e08153) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f269e259772525b7d6e8)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f269e259772525b7d6e8) |
| **Road · West entrance**<br>`1-W-in-12`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2170a2d0418ca4fcd585) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8051bf6f529c859c9803) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-48f20387552fdd714a8d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-51f604b47f6829732515) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8f3cd686fb759cde2ea0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1e7e36b0a693e3f842ac) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1f8a9984715cdada118e)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1f8a9984715cdada118e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-54ef600aeb3df589e4dd) |
| **Road · South entrance**<br>`1-S-in-13`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3fdd8c28667cb6f1f4f7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-08a4819f05e9788c9006) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-17221f87d2766da02a43) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-49f9df403a53f7e50efb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-15a9f4bdb69338eba383) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3ce81e34d36967da0439) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3d1eb60553fe814dbcd1) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-474719545888b39235cd)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-474719545888b39235cd) |
| **Road · North entrance**<br>`1-N-in-14`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d1ccaa0eaf183e349518) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9c7360991e4c1d694dd2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a5800828e134bb5a88d3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1610feb83e1b9ff4ceea) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b45e70b87e16c785b747) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c203030e90895068848d)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c203030e90895068848d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8c127e1a3fe590ed9abd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f532b7da51b0d052a597) |
| **Road · North entrance**<br>`1-N-in-16`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a0e402c2b01119f968c7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-473df4314a2ea62a35ef) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93ad0634085cbc5fb818) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f7397e8dbadd3eb378e2) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f5bf402242c70d8ef08d)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f5bf402242c70d8ef08d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6ebd7caab27b31e7828a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7d46f7a56185bfc1f1d4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-c63fa7fd479936a01204)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c2820a1627fce6b7d578) |

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

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / North |
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
| `member-1-n-in-5` / `1-N-in-5` | `lower-lane-01` / `cut-1-n-in-5` / car | Incoming | `[-3.2,-24,7.5]` | Not declared | 45° | 0 |
| `member-1-n-in-7` / `1-N-in-7` | `lower-lane-02` / `cut-1-n-in-7` / car | Incoming | `[3.2,-24,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / North |
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
| `member-1-n-out-6` / `1-N-out-6` | `upper-lane-02` / `cut-1-n-out-6` / car | Outgoing | `[-3.2,-24,15]` | Not declared | 45° | 0 |
| `member-1-n-out-8` / `1-N-out-8` | `upper-lane-01` / `cut-1-n-out-8` / car | Outgoing | `[3.2,-24,15]` | Not declared | 45° | 0 |

#### Boundary B: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / West |
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
| `member-1-w-out-1` / `1-W-out-1` | `lower-lane-02` / `cut-1-w-out-1` / car | Outgoing | `[-8,-35.2,7.5]` | Not declared | 225° | 0 |
| `member-1-w-out-3` / `1-W-out-3` | `lower-lane-01` / `cut-1-w-out-3` / car | Outgoing | `[-8,-28.8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / West |
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
| `member-1-w-in-2` / `1-W-in-2` | `upper-lane-01` / `cut-1-w-in-2` / car | Incoming | `[-8,-35.2,15]` | Not declared | 225° | 0 |
| `member-1-w-in-4` / `1-W-in-4` | `upper-lane-02` / `cut-1-w-in-4` / car | Incoming | `[-8,-28.8,15]` | Not declared | 225° | 0 |

#### Boundary C: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
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
| `member-1-w-out-11` / `1-W-out-11` | `lower-lane-03` / `cut-1-w-out-11` / car | Outgoing | `[8,-12.8,7.5]` | Not declared | 225° | 0 |
| `member-1-w-out-9` / `1-W-out-9` | `lower-lane-04` / `cut-1-w-out-9` / car | Outgoing | `[8,-19.2,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
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
| `member-1-w-in-10` / `1-W-in-10` | `upper-lane-03` / `cut-1-w-in-10` / car | Incoming | `[8,-19.2,15]` | Not declared | 225° | 0 |
| `member-1-w-in-12` / `1-W-in-12` | `upper-lane-04` / `cut-1-w-in-12` / car | Incoming | `[8,-12.8,15]` | Not declared | 225° | 0 |

#### Boundary D: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (12.2582 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,2]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (12.2582 m); no nominal level |
| Outward heading | 201.979° |
| Slope at joining edge | -29.6095% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-s-in-13` / `1-S-in-13` | `upper-ramp-01` / `cut-1-s-in-13` / car | Incoming | `[8.14277,-40,12.2582]` | Not declared | 201.979° | -29.6095 |

#### Boundary E: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / North |
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
| `member-1-n-in-14` / `1-N-in-14` | `lower-lane-03` / `cut-1-n-in-14` / car | Incoming | `[28.8,8,7.5]` | Not declared | 45° | 0 |
| `member-1-n-in-16` / `1-N-in-16` | `lower-lane-04` / `cut-1-n-in-16` / car | Incoming | `[35.2,8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / North |
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
| `member-1-n-out-15` / `1-N-out-15` | `upper-lane-04` / `cut-1-n-out-15` / car | Outgoing | `[28.8,8,15]` | Not declared | 45° | 0 |
| `member-1-n-out-17` / `1-N-out-17` | `upper-lane-03` / `cut-1-n-out-17` / car | Outgoing | `[35.2,8,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
