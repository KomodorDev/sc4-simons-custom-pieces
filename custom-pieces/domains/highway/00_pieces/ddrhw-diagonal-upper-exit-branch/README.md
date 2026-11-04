# DD RHW-4 — Upper Diagonal Exit Branch

Purpose: explain this reusable piece and its connections and test coverage.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

These angled and north-up views render the actual saved game models and their referenced textures. They show geometry and tile ownership; the game must still be inspected separately.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Upper Diagonal Exit Branch — Clean angled view](previews/preview.png)

![DD RHW-4 — Upper Diagonal Exit Branch — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

Fresh placement also requests one native NAM DD approach tile beyond its exposed highway end. Reserve that extra 16 × 16 m native plot outside the fixed footprint shown in the pictures. The retained models and traffic paths are unchanged. This [native highway connection experiment](../../NETWORK_SPEC.md#12-native-highway-approach-experiment) needs a game test, and existing city placements must be replaced to run the new construction request.

Divides an outer upper-deck lane into a continuing highway lane and an off-ramp towards the southeast avenue access. The ramp stays level until it clears the lower deck. The opposite upper-deck edge remains closed, and the branch owns the outer native cell crossed by its ramp faces.

This branch uses a real flat auxiliary lane in the former highway shoulder, with a 16 m taper and a 8 m parallel section. Its saved driving path changes between the native outer through lane and that auxiliary lane. Native-material dashed separators and a painted split area identify the join; both highway through lanes remain available.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 6 tiles inside a 3 × 3-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Highways → SCP → Assemblies**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. The complete assembly’s source design allows four right turns between the highway and avenue; ramp traffic stays on the adjacent avenue carriageway. The graded ramps remain experimental, with a 30% authoring bound. Current saved-resource results and separate game observations belong in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Reusable upper exit branch component of the compact diagonal double-decker highway and Avenue interchange. Place its owned tiles exactly as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.

Exact reusable identifier: `ddrhw-diagonal-upper-exit-branch`.

Footprint: **3 × 3 tiles**. Exact menu name: **DD RHW-4 — Upper Diagonal Exit Branch**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-a392dce6281d4c6b964a) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`1-W-out-1`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`1-W-out-3`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`1-N-out-6`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`1-N-out-8`<br>Variant: dd-rhw-l2 | **Road · West exit**<br>`1-W-out-9`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`1-W-out-11`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`1-N-out-14`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`1-N-out-16`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`1-E-out-17`<br>Variant: access-ramp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`1-W-in-2`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8439a09ee2b05204ed90) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-733e4b92ce60624082bc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3e4ef75062901491bde9) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-a9cd01cd0aa83c5c0c17)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-a9cd01cd0aa83c5c0c17) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f8b7be838d167a318535) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-96473888df6ea00e3304) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1fb1df230f528f41ba67) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d07c44f5b9433922a91a) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-77d1e715223e907493b4)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-77d1e715223e907493b4) |
| **Road · West entrance**<br>`1-W-in-4`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e7188da8e7ebec77820f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-efc4d4f1fff8660946b2) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-28ef6c9004b804688317)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-28ef6c9004b804688317) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9ef6591d7a585f5684bc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-379406e53e76bb5b6c50) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e557dff43b8a9ccfb4fb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-80c4eb293a557559363b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b004aa75aee78527c3a7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-20b124d692df646c8262) |
| **Road · North entrance**<br>`1-N-in-5`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8e00a9beccd832159d19) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-5f8f169a294c52371f4e)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-5f8f169a294c52371f4e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-350a65e6533292307cf5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e54713594651d52e033c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f2e217dc628a941fad97) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93921d686531aa57428d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1cc33594c41fe00c37b9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-43e92b0e5a351a84d5a6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3e511d78604e8c78f1e7) |
| **Road · North entrance**<br>`1-N-in-7`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f7f154ec2d53c9902875)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f7f154ec2d53c9902875) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-028786d117055e19f9d2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4b713b1e2a1bc5d5df99) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2ea3167f87de717452c6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f8ca31890c2f702e8e00) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5a942953597e37f78d8c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9561dffa7404b743f6bd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2a526b73f098fb731c9b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-484ec3f24ad3c03128ea) |
| **Road · West entrance**<br>`1-W-in-10`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5073ff66098c7bd8a67c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0202390c0fc153bb6c5d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4305fbc6a9cc3e1169ee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-750e2b3c9de00b5587c3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fbc28d090c736e3cf7b2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-660862d91cc09d156f02) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7f2e56ce4cfaa2d92c51) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-a977c3c16e7c8481949f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-a977c3c16e7c8481949f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b9e5fa94f7d7d90d2a05) |
| **Road · West entrance**<br>`1-W-in-12`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d361f46014a4a0915eca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1de597cc92790e7bbc4b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d22ca23ac465e4ec04ab) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4cf544a50bce0930c36f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-12d3b19075425465e5ae) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c0fca6c2f326e8322d27) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-3e27a03aef3c6075dd88)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-3e27a03aef3c6075dd88) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-72cb7b0a90ecb0819219) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9f5c065b78f7f1ee049f) |
| **Road · North entrance**<br>`1-N-in-13`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e299c233a85a4df439b2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2e7c5cfe00bba82afb06) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93fa4ec28fffff4b8225) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f57fb3dddab0f837e379) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-002ab2a026dc9a375f27) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f25cded85c4f3b4d9dd4)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f25cded85c4f3b4d9dd4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d7d8329ccd5cca8b30b6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a61a5c06dcebcd9fe9d0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f201d10fd10e45c2ec98) |
| **Road · North entrance**<br>`1-N-in-15`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-778b69ec0176df859115) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c024b6d719d608bf5d47) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-60bb707eec4bc7e2ac21) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b49a185ce64a975d12c7) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-2d13aaf71d7fd9b224d2)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-2d13aaf71d7fd9b224d2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ffb0924abe5da542bd44) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a88545c3c8e4b794d918) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4694464b98b0cec5e5c2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-30435f050af4dddc4402)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d1ac9c19eb66a6da50b8) |

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

#### Boundary B: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / North |
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
| `member-1-n-in-5` / `1-N-in-5` | `lower-lane-01` / `cut-1-n-in-5` / car | Incoming | `[12.8,-8,7.5]` | Not declared | 45° | 0 |
| `member-1-n-in-7` / `1-N-in-7` | `lower-lane-02` / `cut-1-n-in-7` / car | Incoming | `[19.2,-8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / North |
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
| `member-1-n-out-6` / `1-N-out-6` | `upper-lane-02` / `cut-1-n-out-6` / car | Outgoing | `[12.8,-8,15]` | Not declared | 45° | 0 |
| `member-1-n-out-8` / `1-N-out-8` | `upper-lane-01` / `cut-1-n-out-8` / car | Outgoing | `[19.2,-8,15]` | Not declared | 45° | 0 |

#### Boundary C: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
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
| `member-1-n-in-13` / `1-N-in-13` | `lower-lane-03` / `cut-1-n-in-13` / car | Incoming | `[28.8,8,7.5]` | Not declared | 45° | 0 |
| `member-1-n-in-15` / `1-N-in-15` | `lower-lane-04` / `cut-1-n-in-15` / car | Incoming | `[35.2,8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-02` / `upper-mainline` |
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
| `member-1-n-out-14` / `1-N-out-14` | `upper-lane-04` / `cut-1-n-out-14` / car | Outgoing | `[28.8,8,15]` | Not declared | 45° | 0 |
| `member-1-n-out-16` / `1-N-out-16` | `upper-lane-03` / `cut-1-n-out-16` / car | Outgoing | `[35.2,8,15]` | Not declared | 45° | 0 |

#### Boundary D: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / West |
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
| `member-1-w-out-11` / `1-W-out-11` | `lower-lane-03` / `cut-1-w-out-11` / car | Outgoing | `[24,3.2,7.5]` | Not declared | 225° | 0 |
| `member-1-w-out-9` / `1-W-out-9` | `lower-lane-04` / `cut-1-w-out-9` / car | Outgoing | `[24,-3.2,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / West |
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
| `member-1-w-in-10` / `1-W-in-10` | `upper-lane-03` / `cut-1-w-in-10` / car | Incoming | `[24,-3.2,15]` | Not declared | 225° | 0 |
| `member-1-w-in-12` / `1-W-in-12` | `upper-lane-04` / `cut-1-w-in-12` / car | Incoming | `[24,3.2,15]` | Not declared | 225° | 0 |

#### Boundary E: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (12.2582 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (12.2582 m); no nominal level |
| Outward heading | 68.0206° |
| Slope at joining edge | -29.6095% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-e-out-17` / `1-E-out-17` | `upper-ramp-01` / `cut-1-e-out-17` / car | Outgoing | `[40,-8.14277,12.2582]` | Not declared | 68.0206° | -29.6095 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
