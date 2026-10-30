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

Divides an outer lower-deck lane into a continuing highway lane and an off-ramp, while retaining the upper-deck through lanes.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 1 tiles inside a 1 × 1-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Roads**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. Game placement, vehicle travel, lighting, demolition, and save/reload are unverified. The ramp slopes are a deliberately steep experiment, with a 40% software limit, rather than an established NAM design standard.

<!-- BEGIN PIECE OVERVIEW -->

Reusable lower exit branch component of the compact diagonal double-decker highway and Avenue interchange. Place its owned tiles exactly as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.

Exact reusable identifier: `ddrhw-diagonal-lower-exit-branch`.

Footprint: **1 × 1 tiles**. Exact menu name: **DD RHW-4 — Lower Diagonal Exit Branch**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-79c849dc4c10c431d268) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`1-W-out-1`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`1-S-out-2`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`1-S-out-4`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`1-E-out-7`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`1-E-out-9`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`1-S-in-3`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a0dfa3225a65f150d43) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2a26e6f8329f6f702228) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7e98f33b8208396c2f8a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d7584c718450c186ca26) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-0aa99c1c1ff369beb3fb)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-0aa99c1c1ff369beb3fb) |
| **Road · South entrance**<br>`1-S-in-5`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-286fca1c01bfdc4d37e9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a7691ef5009df474da2f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9b7961f1b49ee8d56c2e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-840d38a996e14eb90296)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-840d38a996e14eb90296) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e995e3f4a52027838d6d) |
| **Road · East entrance**<br>`1-E-in-6`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a4b828cf050426f2ab1e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-98734d82783e642b1a92) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-9d376fdbc347837a7bec)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-9d376fdbc347837a7bec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-21d56aee84df3f050eaf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a2db489dcd650e14c5b9) |
| **Road · East entrance**<br>`1-E-in-8`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-5c98ad18ede2c8ea0dd0)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-5c98ad18ede2c8ea0dd0) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-377218dbcaa7f6b480f8)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-377218dbcaa7f6b480f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-81cb9ee919a18c5a5f50) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6758b65869592bcfd8ff) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-3ebcbed25c5595ba6d82)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-073f74e80ccbfc5f39eb) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

<!-- END CONNECTOR OVERVIEW -->
