# RHW Ramp — Northwest Avenue Ramp Terminal — R40

Purpose: join separate ramp ends to the adjacent Avenue carriageway while retaining its car and pedestrian services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled and north-up views render the actual saved game models and their referenced textures. The connection overview uses the shared complete-boundary cards, including nonzero endpoint slopes.

<!-- BEGIN PIECE VIEWS -->

![RHW Ramp — Northwest Avenue Ramp Terminal — R40 — Clean angled view](previews/preview.png)

![RHW Ramp — Northwest Avenue Ramp Terminal — R40 — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This ground-level terminal joins two separately placed ramp ends to the adjacent Avenue carriageway. R40 means the new circular road centreline has a 40 m radius. The Avenue, its native car lanes, and both pedestrian paths continue through the component. Ramp traffic makes right turns only; it cannot cross the opposing Avenue carriageway.

A **construction tile** is a 16 × 16 m city square occupied by this piece. This piece owns 9 tiles inside a 3 × 3-tile bounding rectangle. Model artwork can extend beyond an owned tile; the assembly plan keeps the construction ownership separate.

1. Prepare Windows SimCity 4 with the exact NAM 50 right-hand-traffic inputs in the [build guide](../../../../docs/BUILD_AND_INSTALL.md), including the adaptive Avenue capture for the stamp and terminals.
2. Open a disposable city and flatten the full 10 × 10-tile placement area.
3. Open **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Modular Diagonal Avenue Diamond**. Press **Tab** or **Shift+Tab** until **RHW Ramp — Northwest Avenue Ramp Terminal — R40** appears. Each click places just this component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/README.md#3-placements) for the reference tile and rotation. Press **Home** or **End** to rotate, then click once at the specified reference position.
5. After the seven parts are placed, extend ordinary diagonal Avenue approaches from the two outer Avenue ends. Placing over an existing Avenue or dragging through occupied pieces remains a separate unverified game test.

These are fixed-height click-to-place components. Their geometry does not follow sloping terrain. Eight selection states repeat four rotations; they do not reflect the traffic directions. Custom attachments must match the whole connector card, including position, height, heading, slope, direction, and all services. A matching card alone does not prove that barriers and road surfaces fit; see [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Independently placed northwest avenue ramp terminal — r40. Use its complete connection cards; it attaches outside the highway stamp and owns no highway tiles.

Exact reusable identifier: `ddrhw-modular-northwest-terminal-r40`.

Footprint: **3 × 3 tiles**. Exact menu name: **RHW Ramp — Northwest Avenue Ramp Terminal — R40**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-e2a49c50612fed492b91) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · North exit**<br>`1-N-out-3`<br>Variant: avenue-ground | **Road · North exit**<br>`1-N-out-4`<br>Variant: avenue-ground | **Road · South exit**<br>`1-S-out-5`<br>Variant: avenue-ground | **Road · South exit**<br>`1-S-out-6`<br>Variant: avenue-ground | **Road · South exit**<br>`1-S-out-7`<br>Variant: avenue-ground | **Pedestrian · North exit**<br>`2-N-out-2`<br>Variant: avenue-sidewalk | **Pedestrian · South exit**<br>`2-S-out-3`<br>Variant: avenue-sidewalk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`1-W-in-1`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-794f78df7ace66b31445) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2bc30df448265ac5e99d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ce8d4363c2deb92734aa)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ce8d4363c2deb92734aa) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-defbaeda3f166704bd68)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-defbaeda3f166704bd68) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d3db8448714a53559a9f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-11e8bec5f3f26593cda7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-34ab8cc1941c1679694d) |
| **Road · West entrance**<br>`1-W-in-2`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-90d004fd56a2b9c4d252) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-726eb705aea6cbd00c4d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4f268d3b8156d6c5e5be) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8c88672b3ce6be33722f) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-e8f749a1ea8aa424773f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-e8f749a1ea8aa424773f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-979c8bd0d5a8b80bbe88) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-014113cbb1977cf94807) |
| **Road · East entrance**<br>`1-E-in-8`<br>Variant: avenue-ground | **Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-17b760468406f1fc497b)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-17b760468406f1fc497b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6e8600b0532417eee9cb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a39bb5b7461edc3c2342) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-376cc0f3765aded4d254) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-218eb53cc5c937aae5a1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-21049933365281dd4f50) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9a4c5df0add87193f73e) |
| **Road · East entrance**<br>`1-E-in-9`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-11c69b118241d661bde9) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-9212b76073da68376b89)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-9212b76073da68376b89) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4a9e0d1e17d136d3fe9f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4d81ac7d3f50d4613227) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7191a3d028818282e6df) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-471f7d2a26723ae14e03) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0b892e6ed15e9c6dca3e) |
| **Road · East entrance**<br>`1-E-in-10`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9d5cada0022479ec9ff5) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1d2800bc2cd3da3b60cc)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1d2800bc2cd3da3b60cc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-95d423d97ded68229b38) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1c1fa89eaacc5a17049b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2d5f61e8d75d6067f2fb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1e18aafa92a3754b7322) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dd98a4730353f517f91e) |
| **Pedestrian · West entrance**<br>`2-W-in-1`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e53434db7e2a16f3a5a8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b2371a54ce5ca5fd6c63) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-deb9d6331c8235bb4f15) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f770c2b4409d7802860a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b2726aecdd7f48acb77e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e58bafe38f51157719bf) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-0fe1ce6a13ac3561200f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-0fe1ce6a13ac3561200f) |
| **Pedestrian · East entrance**<br>`2-E-in-4`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-be3b10a10b844b05d8d7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-00ccd21e13c2bebc50d4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a0d5ab5f8dd229f82294) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6a2935a10d4aa3365316) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-420652fb7d92a9637d37) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-69fde5827566fb64fbf9)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-69fde5827566fb64fbf9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-028a031f9d17c33e3fed)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3235e2921b48ab00e374) |

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
| `member-1-n-out-3` / `1-N-out-3` | `avenue-lane-02` / `cut-1-n-out-3` / car | Outgoing | `[-3.2,8,0]` | Not declared | 315° | 0 |
| `member-1-n-out-4` / `1-N-out-4` | `avenue-lane-01` / `cut-1-n-out-4` / car | Outgoing | `[3.2,8,0]` | Not declared | 315° | 0 |

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
| `member-2-n-out-2` / `2-N-out-2` | `avenue-walkway-01` / `cut-2-n-out-2` / pedestrian | Outgoing | `[7.3,8,0]` | Not declared | 315° | 0 |

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
| `member-1-w-in-1` / `1-W-in-1` | `avenue-lane-04` / `cut-1-w-in-1` / car | Incoming | `[-8,-3.2,0]` | Not declared | 315° | 0 |
| `member-1-w-in-2` / `1-W-in-2` | `avenue-lane-03` / `cut-1-w-in-2` / car | Incoming | `[-8,3.2,0]` | Not declared | 315° | 0 |

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
| `member-2-w-in-1` / `2-W-in-1` | `avenue-walkway-02` / `cut-2-w-in-1` / pedestrian | Incoming | `[-8,-7.3,0]` | Not declared | 315° | 0 |

#### Boundary C: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,2]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 180° (South) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-s-out-5` / `1-S-out-5` | `avenue-ramp-02` / `cut-1-s-out-5` / car | Outgoing | `[12.2315,-40,0]` | Not declared | 180° | 0 |

#### Boundary D: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 90° (East) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-e-in-10` / `1-E-in-10` | `avenue-ramp-01` / `cut-1-e-in-10` / car | Incoming | `[40,-12.2315,0]` | Not declared | 90° | 0 |

#### Boundary E: `boundary-06`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,2]` / South |
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
| `member-1-s-out-6` / `1-S-out-6` | `avenue-lane-04` / `cut-1-s-out-6` / car | Outgoing | `[28.8,-40,0]` | Not declared | 135° | 0 |
| `member-1-s-out-7` / `1-S-out-7` | `avenue-lane-03` / `cut-1-s-out-7` / car | Outgoing | `[35.2,-40,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[2,2]` / South |
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
| `member-2-s-out-3` / `2-S-out-3` | `avenue-walkway-02` / `cut-2-s-out-3` / pedestrian | Outgoing | `[24.7,-40,0]` | Not declared | 135° | 0 |

#### Boundary F: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,2]` / East |
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
| `member-1-e-in-8` / `1-E-in-8` | `avenue-lane-02` / `cut-1-e-in-8` / car | Incoming | `[40,-35.2,0]` | Not declared | 135° | 0 |
| `member-1-e-in-9` / `1-E-in-9` | `avenue-lane-01` / `cut-1-e-in-9` / car | Incoming | `[40,-28.8,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[2,2]` / East |
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
| `member-2-e-in-4` / `2-E-in-4` | `avenue-walkway-01` / `cut-2-e-in-4` / pedestrian | Incoming | `[40,-24.7,0]` | Not declared | 135° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
