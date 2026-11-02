# DD RHW-4 — L1 Entry Slip Lanes — Parallel

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — L1 Entry Slip Lanes — Parallel — Clean angled view](previews/preview.png)

![DD RHW-4 — L1 Entry Slip Lanes — Parallel — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

**Current shadow policy:** this component intentionally supplies no cast shadow, as do all fifteen parallel-kit components. After installing the checked revision and restarting, use a fresh placement to avoid confusing older saved attachments with the current result. Follow the assembly’s [no-shadow and cleanup checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#44-independent-module-shadow-test); the earlier carrier repair remains historical evidence.

This straight highway section contains the lower L1 on-ramp slip-lane service and its native barrier opening. A slip lane is the auxiliary lane leading between a through lane and a ramp. Both highway decks remain completely straight, with their native through routes retained. All curved roadway outside the native highway edge belongs to the separately placed lateral-departure module.

The revised traffic route and matching white markings use the existing shoulder. Read from the highway through lane toward the ramp: the lower L1 shoulder section has a 8 m smooth sideways taper, followed by 4 m straight and parallel to the highway. An on-ramp follows the reverse sequence in its direction of travel. These two lengths are measured along the straight highway axis and describe the shoulder section, not the complete ramp. The lower route starts 6.788225 m farther upstream, within an already owned native highway tile. The auxiliary-lane centre is 5.5 m from the highway axis. Its checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot at the straight shoulder section. The two occupied cells lie diagonally inside a sparse 2 × 2 rectangle. Its construction reference is an empty corner, so align both occupied preview cells instead of assuming that the reference position is a third tile. Complete boundary cards include both highway levels and every access fragment; matching only the named ramp is insufficient.

This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **2 tiles inside a 2 × 2-tile rectangle**. Its reference position in the complete assembly is **P05: X1, Y3, at 0°**. Its actual occupied cells on that shared grid are **(X2, Y3), (X1, Y2)**. The [assembly construction picture](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **DD RHW-4 — L1 Entry Slip Lanes — Parallel** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X1, Y3**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** Both highway levels: 7.5/15 m; named access at 7.5 m. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

<!-- BEGIN PIECE OVERVIEW -->

Place one l1 entry slip lanes for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-lower-entry-slip`.

Footprint: **2 × 2 tiles**. Exact menu name: **DD RHW-4 — L1 Entry Slip Lanes — Parallel**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-a3bd188382bef08c9463) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · South exit**<br>`channel-11-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-12-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-13-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`channel-14-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-15-out`<br>Variant: dd-rhw-l2 | **Road · West exit**<br>`channel-16-out`<br>Variant: access-ramp | **Road · South exit**<br>`channel-17-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-18-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`channel-19-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-20-out`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6cb386346968a166f71b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-22075f8465f1bcc67cbf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-42edd6ba43c150054c91) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2698b6877d0ca7995906) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-8eed456f9223db52e2e2)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-8eed456f9223db52e2e2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3e7801edd7b7b1ce5390) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b9e6a73a832f377ad49b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e820d08deb04948dd0f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-351636182e75231cca77) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-529c4f08caba2c4bf491) |
| **Road · North entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-946a2c6ee75daa793b94)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-946a2c6ee75daa793b94) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7725c070123b5519bde1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-68b6e361d3f3efa08f4c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fda3f34b6e18a862327d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f5cf841544f154b57461) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1150166a8335b4f3efd6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-30ccbd80ec31ad785856) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-629aa9d1b402342235e5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-99ce1c77e2e37831efcf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-12da417d17b25c0f221b) |
| **Road · South entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7632cd75772344b48067) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e371cfc6f43f446578a8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c6d538d458cb6db65414) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1ffa6a39a134848e2efd)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1ffa6a39a134848e2efd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6c423208a227fa09149a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-45aee83a3cc9ab9748b1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-24db5e66db90d4adfe96) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-623f6ba1e7786eab8fb7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d8921e77b80d29e29156) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8084e24519edba4d52eb) |
| **Road · East entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-143efd0d616179423784) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eb1014e94e505dbd5a08) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-db6b81876c71c3828352)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-db6b81876c71c3828352) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b83371f1a2922f19cc49) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-29c02fd4e5f262daa9d7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3f301b3d510e3d864572) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-98270c95cad2e8f622b3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93394d963e94f0761c94) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fd0cd8c465f93669f1e9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-703b903834d1dfa7264a) |
| **Road · East entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-70c7204eb7e2ecec4079) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-badc3d137f5ca49a7734)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-badc3d137f5ca49a7734) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1f653b9ec7cc0c8bcf3a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a696ec2ea309ae9560d6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7ff0567132f30b467672) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-817f725a6f0a81b658a5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dd65aa7aa6844042a992) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-267cb126a989849e449d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-67b6d55c4bbfb5b14b2a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8e1ebc9abb1a7caa5b60) |
| **Road · South entrance**<br>`channel-06-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-63f2c3d57279b8a2bc9e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b215dddc7bc005785ede) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b71e6e40ad52db565ab3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-af00967868df5e11d364) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f06f08b8149eb262f0a8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cf63ae55ec816cd08d91) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0d917ade6d4a0b5cb5b2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7399ac924f81f0f5b5ef) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9397a3f29b4bfbe673b8) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-62c328a6fd12aadc00dd)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-62c328a6fd12aadc00dd) |
| **Road · North entrance**<br>`channel-07-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d1a03572cdc022f6115b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3b7e284b4ce254fed1a5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e005d98a305bea3ab73d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dfcb7a1a5c9356e59ed2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1f173055466e34833691) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f5c3edc2be3f01bdebb0)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f5c3edc2be3f01bdebb0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4256c799a3e366a90f95) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d4b0a076d26daa3f5a24) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1b5cbbe43761c919a0d8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3f1d2298715cc27e6c06) |
| **Road · South entrance**<br>`channel-08-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-60eaa900f574dd4b30b6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b9936625df4702f56cb5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-92b069cf41e56bf2a984) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-571280ee0534c1b6a02c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1e7297575f27077ef2c0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-680114312f01c51872e2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c1577b896e6b05c225f4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b5b871960d693bd11b46) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ff19c89a50ab115e4d9d)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ff19c89a50ab115e4d9d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d7a025d78f6ebc3d6d61) |
| **Road · East entrance**<br>`channel-09-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dca957790473fdb95fe5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-984a2082508825b0fb30) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9e209779ca26ce627c57) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-68207278853d3d6c364f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-62ec4b2fe40457b93b84) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ddb5eb875a3c5fb30d65) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1948cce67aae21930e32) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ec1cb74d13e2bf7cd696)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ec1cb74d13e2bf7cd696) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-30536969ab708cf686cc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c6d38f736f06838a583c) |
| **Road · East entrance**<br>`channel-10-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cd7d75480398b755b6d5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4727c6031f9da7102726) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9206b0912b19028f857d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f2e4f16d1f7517a437da) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f52f775c1cf0c843a158) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-16dc7e151188a5af3229) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-18041bc9dda734dc52e8)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-18041bc9dda734dc52e8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2ffe645931cfc760efd9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7933ce37df03ca52f9b2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-311b633728bfe92c407c)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8b4f8c3d573325fe663a) |

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

#### Boundary A: `boundary-03`

All 3 service groups are required together at this edge.

##### Service group 1 / 3: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-access-network-lower-on-01` / `access-network-lower-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 189.456° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-11-out` / `channel-11-out` | `access-lower-on` / `cut-channel-11-out` / car | Outgoing | `[-6.19488,-24,7.5]` | Not declared | 189.456° | 0 |

##### Service group 2 / 3: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-02` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
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
| `member-channel-12-out` / `channel-12-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-12-out` / car | Outgoing | `[-3.2,-24,7.5]` | Not declared | 225° | 0 |
| `member-channel-13-out` / `channel-13-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-13-out` / car | Outgoing | `[3.2,-24,7.5]` | Not declared | 225° | 0 |

##### Service group 3 / 3: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-03` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
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
| `member-channel-01-in` / `channel-01-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-01-in` / car | Incoming | `[-3.2,-24,15]` | Not declared | 225° | 0 |
| `member-channel-03-in` / `channel-03-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-03-in` / car | Incoming | `[3.2,-24,15]` | Not declared | 225° | 0 |

#### Boundary B: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-access-network-lower-on-01` / `access-network-lower-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 19.8713° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-02-in` / `channel-02-in` | `access-lower-on` / `cut-channel-02-in` / car | Incoming | `[-0.104467,-8,7.5]` | Not declared | 19.8713° | 0 |

#### Boundary C: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
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
| `member-channel-04-in` / `channel-04-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-04-in` / car | Incoming | `[8,-19.2,7.5]` | Not declared | 45° | 0 |
| `member-channel-05-in` / `channel-05-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-05-in` / car | Incoming | `[8,-12.8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
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
| `member-channel-14-out` / `channel-14-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-14-out` / car | Outgoing | `[8,-19.2,15]` | Not declared | 45° | 0 |
| `member-channel-15-out` / `channel-15-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-15-out` / car | Outgoing | `[8,-12.8,15]` | Not declared | 45° | 0 |

#### Boundary D: `boundary-07`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-07-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
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
| `member-channel-17-out` / `channel-17-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-17-out` / car | Outgoing | `[12.8,-8,7.5]` | Not declared | 225° | 0 |
| `member-channel-18-out` / `channel-18-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-18-out` / car | Outgoing | `[19.2,-8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-07-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
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
| `member-channel-06-in` / `channel-06-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-06-in` / car | Incoming | `[12.8,-8,15]` | Not declared | 225° | 0 |
| `member-channel-08-in` / `channel-08-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-08-in` / car | Incoming | `[19.2,-8,15]` | Not declared | 225° | 0 |

#### Boundary E: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (4.36411 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-access-network-lower-on-01` / `access-network-lower-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (4.36411 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -17.9119% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-07-in` / `channel-07-in` | `access-lower-on` / `cut-channel-07-in` / car | Incoming | `[15.0294,8,4.36411]` | Not declared | 45° | -17.9119 |

#### Boundary F: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.14473 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-access-network-lower-on-01` / `access-network-lower-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.14473 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 17.9075% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-16-out` / `channel-16-out` | `access-lower-on` / `cut-channel-16-out` / car | Outgoing | `[8,0.970563,6.14473]` | Not declared | 225° | 17.9075 |

#### Boundary G: `boundary-06`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
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
| `member-channel-09-in` / `channel-09-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-09-in` / car | Incoming | `[24,-3.2,7.5]` | Not declared | 45° | 0 |
| `member-channel-10-in` / `channel-10-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-10-in` / car | Incoming | `[24,3.2,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
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
| `member-channel-19-out` / `channel-19-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-19-out` / car | Outgoing | `[24,-3.2,15]` | Not declared | 45° | 0 |
| `member-channel-20-out` / `channel-20-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-20-out` / car | Outgoing | `[24,3.2,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
