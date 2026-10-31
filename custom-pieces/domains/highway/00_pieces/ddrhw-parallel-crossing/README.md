# DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel — Clean angled view](previews/preview.png)

![DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This is the central crossing of both straight highway decks over the diagonal ground Avenue. L0 means the ground pavement at 0 m, L1 is the lower deck at 7.5 m, and L2 is the upper deck at 15 m. The three occupied tiles preserve the native Avenue car and pedestrian routes and the four highway through lanes. The outside-deck upper-ramp turns also cross these city tiles, so their required traffic fragments stay with this owner.

Its sparse 2 × 2 footprint has three occupied corners and an empty local [1,1] corner. That empty corner supplies a temporary placement handle, which the supported NAM DLL removes. It is not a fourth permanent road tile. The highway model stays straight; curved high departures belong to the separate ramp modules.

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **3 tiles inside a 2 × 2-tile rectangle**. Its reference position in the complete assembly is **P01: X4, Y5, at 0°**. Its actual occupied cells on that shared grid are **(X4, Y5), (X5, Y5), (X4, Y4)**. The [assembly construction picture](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X4, Y5**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** 0 m Avenue; 7.5 m L1; 15 m L2. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

<!-- BEGIN PIECE OVERVIEW -->

Place one dd rhw / avenue crossing for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-crossing`.

Footprint: **2 × 2 tiles**. Exact menu name: **DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-c36b058e6f1085b5f41e) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`channel-11-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-12-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-13-out`<br>Variant: avenue-ground | **Road · North exit**<br>`channel-14-out`<br>Variant: avenue-ground | **Road · East exit**<br>`channel-15-out`<br>Variant: avenue-ground | **Road · East exit**<br>`channel-16-out`<br>Variant: avenue-ground | **Road · East exit**<br>`channel-17-out`<br>Variant: avenue-ground | **Road · North exit**<br>`channel-18-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-19-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-20-out`<br>Variant: access-ramp | **Pedestrian · North exit**<br>`channel-23-out`<br>Variant: avenue-sidewalk | **Pedestrian · East exit**<br>`channel-24-out`<br>Variant: avenue-sidewalk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1bd90a8ae90419a2ba3d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a6860327a6f71b1039d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3260bfc585119d14c085) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-05fa46f64ae8cd77e33c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0bea3e8dc9edea2d5a07) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-01408cdbd23ffbc9e15e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8771d1a0de9cb18d5b4d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-aabc5d2f9ec020f679d4) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-9c0ce3ac5085a861c837)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-9c0ce3ac5085a861c837) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5959c56e8e94addd2615) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ac568c11582a42f5ef65) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9a3e17e58446872ffa7f) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e3201bde843483f4a7ff) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0f6e569d86e179c9df4d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7bccd8283407e0267c37) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4e5073a86246050f04c4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3a64328c16f9028043ad) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8546b0f024513b8231e7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2c0c270d3008fb74448d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-276dc328887ec5a73af7)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-276dc328887ec5a73af7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-11dc7ca5df5e434b90b8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-164da9651996996779fa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-350ea170251738be922b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5a3a35c15e80c32d55e1) |
| **Road · West entrance**<br>`channel-03-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f9a5c679fa5ccccc29ab) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cc0fef22f08cf4cb2529) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c61f1080fb1dac156372) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-40ef635d10a73ba724d3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a6cb57de8e84bbee0a4e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-2836d996db6128e14724)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-2836d996db6128e14724) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-35143634d8ced064ebb6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e8e80706fc7890c45b18) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b4ed8f3b9ce41182aad2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cae9e6dbb0bb509ff1a5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d52ebc21277fab52fc25) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-390969abbc5da468c29b) |
| **Road · West entrance**<br>`channel-04-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0fc0fb1b87069b4f0531) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0a1fbaa353dc64eaf41b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b10e6a2df866076429bf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2c5a6564a85444f518fa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9aae3519cf707f301ef9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-50f4ce62bace365d3c10) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-5135f97300d37145f205)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-5135f97300d37145f205) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ebc15120885d58800b84) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-824c9324b7a399d78a38) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-11d98b140ec45190438a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4d6e19705bfaca243918) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c0e4468c04a1a0cf5801) |
| **Road · South entrance**<br>`channel-05-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-09bd24c0e1a9306d7800) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-85b8a711037da8ce006d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4e4252b4dfc6338ad6ba) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-73b91bbf456e046e0693) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-540a8b5c25e95596b096)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-540a8b5c25e95596b096) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d7917c2a42043eb5205b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b9c5191301ece65e01ab) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-080123257346c1b23f53) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f917640dba8c9f4d9aec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b8ea2da307ff7b42cc5b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-84bba4c2f07b6256b8ce) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9ee76821369dc09c085e) |
| **Road · South entrance**<br>`channel-06-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-250d11d142c844a89dee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-336baed47ed59616e057) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-db6586bcbdd417580318)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-db6586bcbdd417580318) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-af087a283cc185cc27d8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-87e8605e174706f65100) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-14e7e1066f3ff9f4c767) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f1820dcc0190bf33c411) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f52931bf337b9e4623f9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-aa4f9c53bedd43e0e8b8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d65ea8bada569310a98c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0037745e9939bfc28ad8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-527003334f6838406ff9) |
| **Road · North entrance**<br>`channel-07-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-328c7b05fbf844fb831e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-004a6f8a50eb9d0d84d1)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-004a6f8a50eb9d0d84d1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b0d86bde721de459d39b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0111ca869446c1f8cfcf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3548f2dacf02693984bc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ad56cacafc9825886868) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-71286a4da40b07c7f1e9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-223c5b0c5bbbceaebbe5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b0c1ff6e3bc8cdf302c4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d878954c05c19ca1101d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5e41eba0f1ce3d7d7112) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8b817a4ee7294ab1775e) |
| **Road · South entrance**<br>`channel-08-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ada9f0dfe1ddcf050827) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fa42f67e7bd63c536096) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b7d851ccc943001a8447) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-829f9ac3e99aecdac0bc)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-829f9ac3e99aecdac0bc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-55e199ce74dcfed30084) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-370b7746d56a249dc34a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6d2bbfaf81e500c582ef) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2d1f607e406461d402a5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e758bd281c980e4958bf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e87e4bd11e0eaecbc6f3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b7f0f93c573f7e82f591) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c26bc7bb95fff0845528) |
| **Road · North entrance**<br>`channel-09-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-4dc9f7b947d4b0a5af85)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-4dc9f7b947d4b0a5af85) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-37a5cc03c9ebdbcf1a05) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d9e09dc5450224473844) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4577915363ccd00957ba) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fc7545d40ab394d96eea) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-002e497e194063aed971) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-23b7f6803752e61fc6f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d7cddc9d634faa2055f9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-524d4c6b6196b21596eb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0a9facf0c0c1df29f4da) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c2b5ec79561418f11857) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-655a30c3f96c7732cc40) |
| **Road · South entrance**<br>`channel-10-in`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2e2f0c65d98b71787690) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-310e2b671f933d78cc4f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-41a400db768853a55b2c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e8fd7e11ba1a6fa65cec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7601424e6f5b4dab86f3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5a3354214cf9dc7081c4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-051380956433ac67d676) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4d7398f830bbb48975eb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-41c3a7610121866570c5) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-4a11fd7029524ca99703)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-4a11fd7029524ca99703) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-28bb63b272b514b4212d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-45947b5bcaf52c8419f7) |
| **Pedestrian · West entrance**<br>`channel-21-in`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c51c66bad1e29465fa3b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7c196711f8f2547f9e56) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-460c5a1c7736a562b9f2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0f0b4fc51701dde52690) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2b7e28d745281284d534) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d2509eee63be96e477b0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-adcaf40bceeb125ce3f5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5eb6bd2b1af1c0dd9447) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-338e9b36dfdc6c9c29ca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ed32e6175114821afc49) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2293b024cdf7ede7262e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-51ed2712e3b38ee25e6c)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-51ed2712e3b38ee25e6c) |
| **Pedestrian · South entrance**<br>`channel-22-in`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6c3ada90a709c8d480e0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d33e50d3e18539ff5659) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-617aa39ddba7ec95c2c0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7eb5172dd1183321ee0a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2526912e455e82ac5823) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ba57b6361c551a5f476d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9c9e668887490c4a3f39) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-271f41fe284bd3b5265a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-88a381ff5b7bc49c5be9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a835b8ce197650077358) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-6ad6c4f14377e790fed5)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-6ad6c4f14377e790fed5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ac49012ca7f09ecbd5ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-12fbfbe83222e97b6bb5) |

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
| `member-channel-13-out` / `channel-13-out` | `avenue-mainline-axis-plus-3-39411-positive` / `cut-channel-13-out` / car | Outgoing | `[-3.2,8,0]` | Not declared | 315° | 0 |
| `member-channel-14-out` / `channel-14-out` | `avenue-mainline-axis-plus-7-91960-positive` / `cut-channel-14-out` / car | Outgoing | `[3.2,8,0]` | Not declared | 315° | 0 |

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
| `member-channel-23-out` / `channel-23-out` | `avenue-walkways-axis-plus-10-81873-positive` / `cut-channel-23-out` / pedestrian | Outgoing | `[7.3,8,0]` | Not declared | 315° | 0 |

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
| `member-channel-03-in` / `channel-03-in` | `avenue-mainline-axis-minus-7-91960-negative` / `cut-channel-03-in` / car | Incoming | `[-8,-3.2,0]` | Not declared | 315° | 0 |
| `member-channel-04-in` / `channel-04-in` | `avenue-mainline-axis-minus-3-39411-negative` / `cut-channel-04-in` / car | Incoming | `[-8,3.2,0]` | Not declared | 315° | 0 |

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
| `member-channel-21-in` / `channel-21-in` | `avenue-walkways-axis-minus-10-81873-negative` / `cut-channel-21-in` / pedestrian | Incoming | `[-8,-7.3,0]` | Not declared | 315° | 0 |

#### Boundary C: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.131713 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-access-network-upper-off-01` / `access-network-upper-off` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.131713 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 18.3235% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-05-in` / `channel-05-in` | `access-upper-off` / `cut-channel-05-in` / car | Incoming | `[0.970563,-24,0.131713]` | Not declared | 225° | 18.3235 |

#### Boundary D: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / West |
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
| `member-channel-11-out` / `channel-11-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-11-out` / car | Outgoing | `[-8,-19.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-12-out` / `channel-12-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-12-out` / car | Outgoing | `[-8,-12.8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / West |
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
| `member-channel-01-in` / `channel-01-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-01-in` / car | Incoming | `[-8,-19.2,15]` | Not declared | 225° | 0 |
| `member-channel-02-in` / `channel-02-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-02-in` / car | Incoming | `[-8,-12.8,15]` | Not declared | 225° | 0 |

#### Boundary E: `boundary-04`

All 3 service groups are required together at this edge.

##### Service group 1 / 3: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-access-network-upper-off-01` / `access-network-upper-off` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 100.421° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-15-out` / `channel-15-out` | `access-upper-off` / `cut-channel-15-out` / car | Outgoing | `[8,-20.6752,0]` | Not declared | 100.421° | 0 |

##### Service group 2 / 3: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-mainline-02` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
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
| `member-channel-16-out` / `channel-16-out` | `avenue-mainline-axis-minus-7-91960-negative` / `cut-channel-16-out` / car | Outgoing | `[8,-19.2,0]` | Not declared | 135° | 0 |
| `member-channel-17-out` / `channel-17-out` | `avenue-mainline-axis-minus-3-39411-negative` / `cut-channel-17-out` / car | Outgoing | `[8,-12.8,0]` | Not declared | 135° | 0 |

##### Service group 3 / 3: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-walkways-03` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[0,1]` / East |
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
| `member-channel-24-out` / `channel-24-out` | `avenue-walkways-axis-minus-10-81873-negative` / `cut-channel-24-out` / pedestrian | Outgoing | `[8,-23.3,0]` | Not declared | 135° | 0 |

#### Boundary F: `boundary-08`

All 3 service groups are required together at this edge.

##### Service group 1 / 3: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-08-access-network-upper-on-01` / `access-network-upper-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0 m); no nominal level |
| Outward heading | 169.579° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-10-in` / `channel-10-in` | `access-upper-on` / `cut-channel-10-in` / car | Incoming | `[20.6752,-8,0]` | Not declared | 169.579° | 0 |

##### Service group 2 / 3: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-08-avenue-mainline-02` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
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
| `member-channel-06-in` / `channel-06-in` | `avenue-mainline-axis-plus-3-39411-positive` / `cut-channel-06-in` / car | Incoming | `[12.8,-8,0]` | Not declared | 135° | 0 |
| `member-channel-08-in` / `channel-08-in` | `avenue-mainline-axis-plus-7-91960-positive` / `cut-channel-08-in` / car | Incoming | `[19.2,-8,0]` | Not declared | 135° | 0 |

##### Service group 3 / 3: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-08-avenue-walkways-03` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[1,0]` / South |
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
| `member-channel-22-in` / `channel-22-in` | `avenue-walkways-axis-plus-10-81873-positive` / `cut-channel-22-in` / pedestrian | Incoming | `[23.3,-8,0]` | Not declared | 135° | 0 |

#### Boundary G: `boundary-06`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
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
| `member-channel-07-in` / `channel-07-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-07-in` / car | Incoming | `[12.8,8,7.5]` | Not declared | 45° | 0 |
| `member-channel-09-in` / `channel-09-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-09-in` / car | Incoming | `[19.2,8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
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
| `member-channel-18-out` / `channel-18-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-18-out` / car | Outgoing | `[12.8,8,15]` | Not declared | 45° | 0 |
| `member-channel-19-out` / `channel-19-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-19-out` / car | Outgoing | `[19.2,8,15]` | Not declared | 45° | 0 |

#### Boundary H: `boundary-07`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.131713 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-07-access-network-upper-on-01` / `access-network-upper-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.131713 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 18.3235% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-20-out` / `channel-20-out` | `access-upper-on` / `cut-channel-20-out` / car | Outgoing | `[24,-0.970563,0.131713]` | Not declared | 45° | 18.3235 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
