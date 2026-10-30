# DD RHW-4 — Compact Lower Diagonal Exit Grade

Purpose: explain this reusable piece and its connections and test coverage.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

These angled and north-up views render the actual saved game models and their referenced textures. They show geometry and tile ownership; the game must still be inspected separately.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Compact Lower Diagonal Exit Grade — Clean angled view](previews/preview.png)

![DD RHW-4 — Compact Lower Diagonal Exit Grade — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

Carries the steep descending part of the lower off-ramp. The complete descent is about 24.16 m long, split at construction-tile boundaries.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 1 tiles inside a 1 × 1-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Roads**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. Game placement, vehicle travel, lighting, demolition, and save/reload are unverified. The ramp slopes are a deliberately steep experiment, with a 40% software limit, rather than an established NAM design standard.

<!-- BEGIN PIECE OVERVIEW -->

Reusable lower exit grade component of the compact diagonal double-decker highway and Avenue interchange. Place its owned tiles exactly as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.

Exact reusable identifier: `ddrhw-diagonal-lower-exit-grade`.

Footprint: **1 × 1 tiles**. Exact menu name: **DD RHW-4 — Compact Lower Diagonal Exit Grade**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-40d510a66cbd1268b779) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`1-W-out-1`<br>Variant: access-ramp |
| --- | --- |
| **Road · East entrance**<br>`1-E-in-2`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-70c60453512517b46bdf)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-0683906e44185e677044)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-0683906e44185e677044) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

<!-- END CONNECTOR OVERVIEW -->
