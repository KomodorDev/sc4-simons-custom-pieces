# DD RHW-4 — Lower Diagonal Entry Branch

Purpose: explain this reusable piece and its connections and test coverage.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

These angled and north-up views render the actual saved game models and their referenced textures. They show geometry and tile ownership; the game must still be inspected separately.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Lower Diagonal Entry Branch — Clean angled view](previews/preview.png)

![DD RHW-4 — Lower Diagonal Entry Branch — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

Merges a ramp into an outer lower-deck lane, while retaining the upper-deck through lanes.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 1 tiles inside a 1 × 1-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Roads**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. Game placement, vehicle travel, lighting, demolition, and save/reload are unverified. The ramp slopes are a deliberately steep experiment, with a 40% software limit, rather than an established NAM design standard.

<!-- BEGIN PIECE OVERVIEW -->

Reusable lower entry branch component of the compact diagonal double-decker highway and Avenue interchange. Place its owned tiles exactly as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.

Exact reusable identifier: `ddrhw-diagonal-lower-entry-branch`.

Footprint: **1 × 1 tiles**. Exact menu name: **DD RHW-4 — Lower Diagonal Entry Branch**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-508b180723f876d0dff8) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · South exit**<br>`1-S-out-1`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`1-S-out-4`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`1-E-out-7`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`1-E-out-9`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`1-S-in-2`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-78b47be1097668bd4b23) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-aad285db8c55156224b1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4d78f04309410f417af5) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-4fc2e884fcbb60abe4a2)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-4fc2e884fcbb60abe4a2) |
| **Road · North entrance**<br>`1-N-in-3`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-6a5479bb2d392966d840)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-6a5479bb2d392966d840) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a237a9496b8cf8be109f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-afd7263e6d7fdc76e6bb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-868622ad7b96d99a6c70) |
| **Road · South entrance**<br>`1-S-in-5`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3112f1ff14ad97666ee7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f1831cc87d44bd007bfe) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-263a8f0e1f69a4ad02a4)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-263a8f0e1f69a4ad02a4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fbd507de73009247786f) |
| **Road · East entrance**<br>`1-E-in-6`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6aa4db5a47dd28db1026) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-75b4aa8be611faf80193)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-75b4aa8be611faf80193) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a6b1697faeeb54ee3b46) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eec94f21f272fcbe6dfa) |
| **Road · East entrance**<br>`1-E-in-8`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b5f68983470a4bb1b9fc)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b5f68983470a4bb1b9fc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-73602351a683b7b2eafb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f788c3a0e0182588dc85) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0d8e83cbc22de1b2fb83)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2723161b26dc14652f7b) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

<!-- END CONNECTOR OVERVIEW -->
