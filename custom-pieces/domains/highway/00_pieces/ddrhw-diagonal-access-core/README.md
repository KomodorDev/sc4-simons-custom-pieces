# DD RHW-4 — and Avenue Access Core

Purpose: explain this reusable piece and its connections and test coverage.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

These angled and north-up views render the actual saved game models and their referenced textures. They show geometry and tile ownership; the game must still be inspected separately. The canonical models shown here remain a static reference for the approved geometry and ground artwork; these views do not simulate the sidewalk appearance selected by the game.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — and Avenue Access Core — Clean angled view](previews/preview.png)

![DD RHW-4 — and Avenue Access Core — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

Coordinates the crossing and the ramp landing fragments that share its five construction tiles. It preserves both opposing highway decks, the four avenue car lanes, and both avenue pedestrian channels. Ramp access uses only the adjacent avenue carriageway; cross-avenue turns are excluded.

A **construction tile** is one 16 × 16 m city square owned by this component. This component owns 5 tiles inside a 3 × 3-tile bounding rectangle. Empty cells in that rectangle belong to neighbouring components or remain open.

1. Prepare the exact NAM 50 right-hand-traffic profile using the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md).
2. Open a disposable city and flatten the complete placement area. These fixed components have no terrain-following implementation.
3. Open **Transportation → Highways**. For the complete layout, select the compact diamond assembly button, then press **Tab** or **Shift+Tab** until this exact component name appears. **Home** and **End** rotate the current component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md#3-placements), including its reference tile and rotation. Click once for this component, then select the next one.

The eight selection states repeat four proper rotations. They do not mirror the traffic directions. The complete assembly’s source design allows four right turns between the highway and avenue; ramp traffic stays on the adjacent avenue carriageway. The graded ramps remain experimental, with a 30% authoring bound. Current saved-resource results and separate game observations belong in [TESTING.md](TESTING.md).

The Avenue-bearing tiles now use **adaptive ground**, meaning copies of native Avenue textures that allow the game to select a pavement appearance. A **T21 prop** is a model attached to a network tile; these props retain the decks, supports, slip lanes, and ramp mouths on those tiles. The complete saved car, pedestrian, and ramp routes are retained. This complete-component integration still needs fresh game checks; the isolated sidewalk prototype’s observed success does not establish a pass for this piece. See the [network specification](../../NETWORK_SPEC.md) and the [assembly testing guide](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Reusable access core component of the compact diagonal double-decker highway and Avenue interchange. Place its owned tiles exactly as shown in the assembly guide; traffic uses actual car and pedestrian PATHs.

Exact reusable identifier: `ddrhw-diagonal-access-core`.

Footprint: **3 × 3 tiles**. Exact menu name: **DD RHW-4 — and Avenue Access Core**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-9089693028482b301540) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`1-W-out-3`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`1-W-out-5`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`1-W-out-7`<br>Variant: avenue-ground | **Road · West exit**<br>`1-W-out-8`<br>Variant: avenue-ground | **Road · East exit**<br>`1-E-out-9`<br>Variant: avenue-ground | **Road · East exit**<br>`1-E-out-10`<br>Variant: avenue-ground | **Road · North exit**<br>`1-N-out-13`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`1-N-out-16`<br>Variant: dd-rhw-l2 | **Pedestrian · West exit**<br>`2-W-out-2`<br>Variant: avenue-sidewalk | **Pedestrian · East exit**<br>`2-E-out-3`<br>Variant: avenue-sidewalk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · North entrance**<br>`1-N-in-1`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-df720693a84b5dd0c454) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f7e041046e4a052ed1b8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-984e29f5b3494ab34eb0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-486baadf43d62b48f73d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c6f40f775cea53813d1b)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c6f40f775cea53813d1b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e959d8bea608d3a2d4fa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d606b080abb7cd8aeec9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dc1a98f1de1171a4f786) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-66207e5cd46a640fa5c1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3599d92470898cbf80ba) |
| **Road · North entrance**<br>`1-N-in-2`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7776798361bc9c0ed7fb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7c743cd58e0982076e6f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dd6d90b7c1df7a2df7b4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-41b322a2a0e43ebfde6c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3d8206074e0c2e01b0d0) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-9ce40e67119d246b2399)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-9ce40e67119d246b2399) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-404a1d6a4966f0c212e0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7ac828b6fc796a3601b3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ee85cf3a7147df07d568) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-00cb07143aaab168ebbf) |
| **Road · West entrance**<br>`1-W-in-4`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b49d96fd379a8ed5cbc9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6ce950ee680ac257ccd0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bf046ebb0fd3c77be4be) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9e7e9702c54730a5fdd1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-63ba2822f5c2e12aaf0c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7fec7e498b6001b34b32) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6b7a581aaca49a132947) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-bf1fe0fa1bcea17388c2)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-bf1fe0fa1bcea17388c2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bf3a4961fcb2b3c201d7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a2c1801a04725cb1fec) |
| **Road · West entrance**<br>`1-W-in-6`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b5c653b01f2cdd295de9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d69afe4cba44082b51fd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6381d1ed716f23ab4b76) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-14f17a59235b0c88d420) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f29c2ee5b8cd0a9a71ca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fc7f90169b6d68d09094) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b8b62df29af47d4a901b)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b8b62df29af47d4a901b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eefaeb17333f6b61dfb6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1cc550ba1f48eb2c39c9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a6907cfe195ce614e8d) |
| **Road · South entrance**<br>`1-S-in-11`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0f8ed606be25318cbe6d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e218efc4442dea9d7b97) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-79471e1b55455f675529)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-79471e1b55455f675529) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-50c4292c270c710c0ed9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3cbc020486c7ef04bc5b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-499b644bba1f1924e41a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dd4db6744fde8c2f3bf8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c314b61037b5ab961185) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c2feef91ef21675d15c9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-81f04fb3e3b9a7757efa) |
| **Road · North entrance**<br>`1-N-in-12`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-44af3e231d1e30e3834f) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c7dcd003d64809dc03bb)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c7dcd003d64809dc03bb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b5bf0e063c55cd7bc863) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8fff45cbdc4019aaf4f6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3f11247060d725a4cb46) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e2000a64480ec5027604) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1b13fcaa1788a07a4d06) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-abd776e55ea0c743bd1c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-30ccae8de5b0fe198a77) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-162060b2dd2eccc3511a) |
| **Road · South entrance**<br>`1-S-in-14`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c0683b628fcd846d2b7d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fe619ed293a4f3316118) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9e41b43cb310d85acb6c) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-6e7209e3e86b188e1bdf)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-6e7209e3e86b188e1bdf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-aed0ed0173e7f1db8a10) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-712abe34019bb63cde6a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-301885ceb611caa4f36b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d3772860742e1cb4419d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ce6405418fe95ea7aa7a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-82437140ddf1f9611ef8) |
| **Road · North entrance**<br>`1-N-in-15`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-95a89cc316af4c9c09fd)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-95a89cc316af4c9c09fd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d529b6361ba8cf93f980) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e09e9d4e111b9017aea5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f85e61aa95757c830c6e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-69b5e27b7e784f3daf7d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bbbc4c07ec25a78aa27a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5757602bf88c1528713d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-019e69358071f8dd3077) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6dbd088c59d6db5d5cfe) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6913e6e3b004775077eb) |
| **Pedestrian · North entrance**<br>`2-N-in-1`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e75f34a97169a4a54ad0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b8268b9fcb586b36e4d3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dbc2473e5868c0e793da) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ced061156bcff10f4d3a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-88e5b96c429dd3888d30) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9c50253cbbaf94db070a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7c48ff4e9b8159eef310) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-24fb61a2a4a6e7322673) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f870fdade6c1dace97dc) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ae4abfea13e971292160)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ae4abfea13e971292160) |
| **Pedestrian · South entrance**<br>`2-S-in-4`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-99a359bdf423d8fa27e9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-038fdadba6fa09c80c7a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-59dd98b6760487a31e3d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3d8d3c6ddfee827b515e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a790f3bc897e0450aa29) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8bf8fe900e27404a5bca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0b235462c955fbb18eb5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fd79ee0a084277462fd1) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-c46b00ba0146236696c7)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-c46b00ba0146236696c7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b5f3022ace3685e7c41a)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d198fe80e24c35d30deb) |

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

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / North |
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
| `member-1-n-in-1` / `1-N-in-1` | `avenue-lane-01` / `cut-1-n-in-1` / car | Incoming | `[-3.2,-8,0]` | Not declared | 315° | 0 |
| `member-1-n-in-2` / `1-N-in-2` | `avenue-lane-02` / `cut-1-n-in-2` / car | Incoming | `[3.2,-8,0]` | Not declared | 315° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[0,1]` / North |
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
| `member-2-n-in-1` / `2-N-in-1` | `avenue-walkway-01` / `cut-2-n-in-1` / pedestrian | Incoming | `[-7.3,-8,0]` | Not declared | 315° | 0 |

#### Boundary B: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
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
| `member-1-w-out-7` / `1-W-out-7` | `avenue-lane-03` / `cut-1-w-out-7` / car | Outgoing | `[8,-3.2,0]` | Not declared | 315° | 0 |
| `member-1-w-out-8` / `1-W-out-8` | `avenue-lane-04` / `cut-1-w-out-8` / car | Outgoing | `[8,3.2,0]` | Not declared | 315° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[1,0]` / West |
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
| `member-2-w-out-2` / `2-W-out-2` | `avenue-walkway-02` / `cut-2-w-out-2` / pedestrian | Outgoing | `[8,7.3,0]` | Not declared | 315° | 0 |

#### Boundary C: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,2]` / West |
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
| `member-1-w-out-3` / `1-W-out-3` | `lower-lane-02` / `cut-1-w-out-3` / car | Outgoing | `[8,-35.2,7.5]` | Not declared | 225° | 0 |
| `member-1-w-out-5` / `1-W-out-5` | `lower-lane-01` / `cut-1-w-out-5` / car | Outgoing | `[8,-28.8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,2]` / West |
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
| `member-1-w-in-4` / `1-W-in-4` | `upper-lane-01` / `cut-1-w-in-4` / car | Incoming | `[8,-35.2,15]` | Not declared | 225° | 0 |
| `member-1-w-in-6` / `1-W-in-6` | `upper-lane-02` / `cut-1-w-in-6` / car | Incoming | `[8,-28.8,15]` | Not declared | 225° | 0 |

#### Boundary D: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,2]` / East |
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
| `member-1-e-out-10` / `1-E-out-10` | `avenue-lane-02` / `cut-1-e-out-10` / car | Outgoing | `[24,-28.8,0]` | Not declared | 135° | 0 |
| `member-1-e-out-9` / `1-E-out-9` | `avenue-lane-01` / `cut-1-e-out-9` / car | Outgoing | `[24,-35.2,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[1,2]` / East |
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
| `member-2-e-out-3` / `2-E-out-3` | `avenue-walkway-01` / `cut-2-e-out-3` / pedestrian | Outgoing | `[24,-39.3,0]` | Not declared | 135° | 0 |

#### Boundary E: `boundary-06`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,1]` / South |
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
| `member-1-s-in-11` / `1-S-in-11` | `avenue-lane-03` / `cut-1-s-in-11` / car | Incoming | `[28.8,-24,0]` | Not declared | 135° | 0 |
| `member-1-s-in-14` / `1-S-in-14` | `avenue-lane-04` / `cut-1-s-in-14` / car | Incoming | `[35.2,-24,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[2,1]` / South |
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
| `member-2-s-in-4` / `2-S-in-4` | `avenue-walkway-02` / `cut-2-s-in-4` / pedestrian | Incoming | `[39.3,-24,0]` | Not declared | 135° | 0 |

#### Boundary F: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,1]` / North |
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
| `member-1-n-in-12` / `1-N-in-12` | `lower-lane-01` / `cut-1-n-in-12` / car | Incoming | `[28.8,-8,7.5]` | Not declared | 45° | 0 |
| `member-1-n-in-15` / `1-N-in-15` | `lower-lane-02` / `cut-1-n-in-15` / car | Incoming | `[35.2,-8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,1]` / North |
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
| `member-1-n-out-13` / `1-N-out-13` | `upper-lane-02` / `cut-1-n-out-13` / car | Outgoing | `[28.8,-8,15]` | Not declared | 45° | 0 |
| `member-1-n-out-16` / `1-N-out-16` | `upper-lane-01` / `cut-1-n-out-16` / car | Outgoing | `[35.2,-8,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
