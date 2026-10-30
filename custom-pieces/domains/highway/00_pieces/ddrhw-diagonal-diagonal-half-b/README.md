# DD RHW-4 — Diagonal Continuation B

Purpose: explain this reusable piece and its connections and test coverage.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

These angled and north-up views render the actual saved game models and their referenced textures. They show geometry and tile ownership; the game must still be inspected separately.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Diagonal Continuation B — Clean angled view](previews/preview.png)

![DD RHW-4 — Diagonal Continuation B — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

Preserves the complementary native diagonal DD RHW-4 continuation half and adds one 0.8 m-square concrete centre column from ground to the upper deck. Its lane positions differ from continuation A, so the halves are not interchangeable.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 1 tile inside a 1 × 1-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Highways**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. The complete assembly’s source design allows four right turns between the highway and avenue; ramp traffic stays on the adjacent avenue carriageway. The graded ramps remain experimental, with a 30% authoring bound. Current saved-resource results and separate game observations belong in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Reusable native diagonal DD RHW-4 continuation half with an authored concrete centre pier meeting both deck pavement planes. Use the complementary half and the assembly placement guide; traffic follows measured native car lanes.

Exact reusable identifier: `ddrhw-diagonal-diagonal-half-b`.

Footprint: **1 × 1 tiles**. Exact menu name: **DD RHW-4 — Diagonal Continuation B**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-8317ebfa194a2352be94) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`1-W-out-1`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`1-W-out-3`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`1-N-out-6`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`1-N-out-8`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`1-W-in-2`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fc2427a060eb1d08a69e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0848c25791260558a010) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f746c779e0e5794308cf) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-96fa10f3a9c7168c8410)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-96fa10f3a9c7168c8410) |
| **Road · West entrance**<br>`1-W-in-4`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-59e93eedd0c865427a1f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e71bc4ad24a0863e0578) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b24508a14e3f1d713d01)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b24508a14e3f1d713d01) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ddb2f0310088f6648dc4) |
| **Road · North entrance**<br>`1-N-in-5`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-716a36ba8a7d8c889bd0) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-59058363138f7d4fbb3a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-59058363138f7d4fbb3a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cc5cd266dca5283b78ca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7f42147d0f2cb4b17c46) |
| **Road · North entrance**<br>`1-N-in-7`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-83ee6157b50702e2f441)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-83ee6157b50702e2f441) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2041ae287320a10f5212) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3729503dd81886537f61) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-6ce48a0b0061a76032d1)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7059a23841d6c2bf4616) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

<!-- END CONNECTOR OVERVIEW -->
