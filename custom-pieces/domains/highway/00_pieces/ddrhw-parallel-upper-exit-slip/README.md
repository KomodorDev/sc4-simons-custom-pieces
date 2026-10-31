# DD RHW-4 — L2 Exit Slip Lanes — Parallel

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — L2 Exit Slip Lanes — Parallel — Clean angled view](previews/preview.png)

![DD RHW-4 — L2 Exit Slip Lanes — Parallel — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This straight highway section contains the upper L2 off-ramp slip-lane service and its native barrier opening. A slip lane is the auxiliary lane leading between a through lane and a ramp. Both highway decks remain completely straight, with their native through routes retained. All curved roadway outside the native highway edge belongs to the separately placed lateral-departure module.

The two occupied cells lie diagonally inside a sparse 2 × 2 rectangle. Its construction reference is an empty corner, so align both occupied preview cells instead of assuming that the reference position is a third tile. Complete boundary cards include both highway levels and every access fragment; matching only the named ramp is insufficient.

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **2 tiles inside a 2 × 2-tile rectangle**. Its reference position in the complete assembly is **P06: X1, Y2, at 0°**. Its actual occupied cells on that shared grid are **(X2, Y2), (X1, Y1)**. The [assembly construction picture](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **DD RHW-4 — L2 Exit Slip Lanes — Parallel** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X1, Y2**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** Both highway levels: 7.5/15 m; named access at 15 m. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

<!-- BEGIN PIECE OVERVIEW -->

Place one l2 exit slip lanes for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-upper-exit-slip`.

Footprint: **2 × 2 tiles**. Exact menu name: **DD RHW-4 — L2 Exit Slip Lanes — Parallel**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-f375ad5bde0008a6816a) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`channel-10-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-11-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-12-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-13-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-14-out`<br>Variant: dd-rhw-l2 | **Road · West exit**<br>`channel-15-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-16-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-17-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-18-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-19-out`<br>Variant: access-ramp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c288558cba5598d8c8b2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7db861a5971a8652e19c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e9cc59e52e360adf7ed5) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-2568f245e92965e16e83)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-2568f245e92965e16e83) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-6427b509ad0ac2de32a3)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-6427b509ad0ac2de32a3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c398514e23c94a08beb5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0535b6b5ed2ad465d39d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-176dc802ee0595c54e08) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6ae758240248c9ff34e6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0c6d4c497332793204d4) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c9dad47d4d50c79b12d3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-547eaf6b97393c8c9595) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ee60d20ab0bd25c83169)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ee60d20ab0bd25c83169) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6f81a13a0252e2d4f80f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-53b5f4abf0073fa99ce4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1bc115a6b2b62d4b1a63) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ef1c219418f866c54ed1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-19cd0b6a481b23890a4a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-65d312f1f8e08340bb01) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f4632cebdee978a653f6) |
| **Road · North entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-057be867aabfe34ed494) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b2453bef8671a44f604e)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b2453bef8671a44f604e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-052f6187989bb9dc00c4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-32cf5df4c19f61b9adf9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0ec52bf7d1a177c46544) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a27c40abd4a7b52df64d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cef52ef589512f8dad97) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f8599fbc281fbe40f203) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ebf41b4c299421482963) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a26679feb51a1b315c1b) |
| **Road · North entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-beafaa930c58f60380bb)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-beafaa930c58f60380bb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5e23635be76b490a944e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cfdd69756b0bb2a63f9e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d87df7141833674e27bb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4138a34b177b8dbd6788) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-10dc78820eb96e563510) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ffaf37660060c220ae7f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fcc947157dfc40338479) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3f852cfb53e00266037f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7410591712d2b3aa0b55) |
| **Road · West entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3e6b1f2f7f08d2ef5851) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-72b05fff7abd3b533872) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bbc190c9023bbe435138) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ff569a80afe00149062b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fdfea12e238aee6d630a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-501532ccf2e0a23d10b0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f32ef0de22a211bedd77) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-177032a32d86101ce687) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-646fc96fd1ba0fb3de77)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-646fc96fd1ba0fb3de77) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dfc4a3808b4e4c71b4d0) |
| **Road · West entrance**<br>`channel-06-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-01c73c6cd46ee3a873dd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1c789b3871cebd1c1c8b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fba684a739a3a99a6024) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7d977659a4532fa69db0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9e140aca59f5d40eb045) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e1a2ec0d4be49806cd3c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c51ae7d39f2bb26044bc) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-eec35bf8cfc304211404)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-eec35bf8cfc304211404) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-467cfb45ad0b8969cc5c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e0290125bf0f63960888) |
| **Road · North entrance**<br>`channel-07-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2143b78406f9affde40d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8696ed330d7a30859224) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cb5fad379b7b05098056) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-751f863cfaf2e94c26a3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ec84ebceeb6abe434db9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0df627298cbc2f32a22f) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-554eb64f1333da233fb3)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-554eb64f1333da233fb3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0729c983638e5a231c54) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2b7deeaae357a6ecf4ba) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8aeff58d0f022c7fc45f) |
| **Road · South entrance**<br>`channel-08-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-64f4ec2f05c4cb832423) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-635fd5f6a9b356c15771) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-71e96fbb07010b7c6bdf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1db2002e69243f81767d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e3c78c88191498b85191) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-46b377fd2bc68cb7ab13) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-00e5238bbad7ec34d62d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3f1027b1db72188f1a69) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-86931637487578b810ac) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-2a38116282055d3ff378)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-2a38116282055d3ff378) |
| **Road · North entrance**<br>`channel-09-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-226be17a0a3dd7959768) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a23f4987366819b01828) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ad02ec66c08d5b77fb69) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7b043fc947bbfa6742bd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-990af91943b6815bc35b) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-e22f077f8b849acadcdd)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-e22f077f8b849acadcdd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-034562010273122dfb1a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-40be866cf8b81857170d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f650a6d91f5f90573511) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-d6a5f833ba420944301f)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dfe9d8d21ce5b761380f) |

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

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / North |
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
| `member-channel-03-in` / `channel-03-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-03-in` / car | Incoming | `[-3.2,-8,7.5]` | Not declared | 45° | 0 |
| `member-channel-04-in` / `channel-04-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-04-in` / car | Incoming | `[3.2,-8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / North |
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
| `member-channel-12-out` / `channel-12-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-12-out` / car | Outgoing | `[-3.2,-8,15]` | Not declared | 45° | 0 |
| `member-channel-13-out` / `channel-13-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-13-out` / car | Outgoing | `[3.2,-8,15]` | Not declared | 45° | 0 |

#### Boundary B: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
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
| `member-channel-10-out` / `channel-10-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-10-out` / car | Outgoing | `[-8,-19.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-11-out` / `channel-11-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-11-out` / car | Outgoing | `[-8,-12.8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-upper-mainline-02` / `upper-mainline` |
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

#### Boundary C: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 70.1287° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-14-out` / `channel-14-out` | `access-upper-off` / `cut-channel-14-out` / car | Outgoing | `[8,-16.1045,15]` | Not declared | 70.1287° | 0 |

#### Boundary D: `boundary-07`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (12.866 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-07-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (12.866 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 28.2027% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-08-in` / `channel-08-in` | `access-upper-off` / `cut-channel-08-in` / car | Incoming | `[16.9706,-8,12.866]` | Not declared | 225° | 28.2027 |

#### Boundary E: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-lower-mainline-01` / `lower-mainline` |
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
| End / component | `boundary-05-upper-mainline-02` / `upper-mainline` |
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
| `member-channel-17-out` / `channel-17-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-17-out` / car | Outgoing | `[12.8,8,15]` | Not declared | 45° | 0 |
| `member-channel-18-out` / `channel-18-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-18-out` / car | Outgoing | `[19.2,8,15]` | Not declared | 45° | 0 |

#### Boundary F: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
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
| `member-channel-15-out` / `channel-15-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-15-out` / car | Outgoing | `[8,-3.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-16-out` / `channel-16-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-16-out` / car | Outgoing | `[8,3.2,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
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
| `member-channel-05-in` / `channel-05-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-05-in` / car | Incoming | `[8,-3.2,15]` | Not declared | 225° | 0 |
| `member-channel-06-in` / `channel-06-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-06-in` / car | Incoming | `[8,3.2,15]` | Not declared | 225° | 0 |

#### Boundary G: `boundary-06`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (10.0624 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (10.0624 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -28.203% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-19-out` / `channel-19-out` | `access-upper-off` / `cut-channel-19-out` / car | Outgoing | `[24,-0.970563,10.0624]` | Not declared | 45° | -28.203 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
