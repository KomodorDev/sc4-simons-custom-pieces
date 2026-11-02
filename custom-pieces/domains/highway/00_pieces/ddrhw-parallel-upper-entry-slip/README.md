# DD RHW-4 — L2 Entry Slip Lanes — Parallel

Purpose: Place this functional component of the compact parallel diagonal highway diamond and match all of its measured services.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The canonical angled and north-up pictures show the saved model in its authored 0° orientation. The connector overview identifies complete traffic boundaries. Software images show the authored resources; appearance and travel in the game need their own observations in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — L2 Entry Slip Lanes — Parallel — Clean angled view](previews/preview.png)

![DD RHW-4 — L2 Entry Slip Lanes — Parallel — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

**Current shadow policy:** this component intentionally supplies no cast shadow, as do all fifteen parallel-kit components. After installing the checked revision and restarting, use a fresh placement to avoid confusing older saved attachments with the current result. Follow the assembly’s [no-shadow and cleanup checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#44-independent-module-shadow-test); the earlier carrier repair remains historical evidence.

Fresh placement also requests one native NAM DD approach tile beyond its exposed highway end. Reserve that extra 16 × 16 m native plot outside the fixed footprint shown in the pictures. The retained models and traffic paths are unchanged. This [native highway connection experiment](../../NETWORK_SPEC.md#12-native-highway-approach-experiment) needs a game test, and existing city placements must be replaced to run the new construction request.

This straight highway section contains the upper L2 on-ramp slip-lane service and its native barrier opening. A slip lane is the auxiliary lane leading between a through lane and a ramp. Both highway decks remain completely straight, with their native through routes retained. All curved roadway outside the native highway edge belongs to the separately placed lateral-departure module.

The revised traffic route and matching white markings use the existing shoulder. Read from the highway through lane toward the ramp: the upper L2 shoulder section has a 5 m smooth sideways taper, followed by 1 m straight and parallel to the highway. An on-ramp follows the reverse sequence in its direction of travel. These two lengths are measured along the straight highway axis and describe the shoulder section, not the complete ramp. The upper route keeps its previous outer traffic port: a longer shoulder treatment would need traffic ownership beyond the retained 31-cell layout. The auxiliary-lane centre is 5.5 m from the highway axis. Its checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot at the straight shoulder section. The two occupied cells lie diagonally inside a sparse 2 × 2 rectangle. Its construction reference is an empty corner, so align both occupied preview cells instead of assuming that the reference position is a third tile. Complete boundary cards include both highway levels and every access fragment; matching only the named ramp is insufficient.

This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

A construction tile is a 16 × 16 m city square occupied by one component. This type owns **2 tiles inside a 2 × 2-tile rectangle**. Its reference position in the complete assembly is **P07: X7, Y8, at 0°**. Its actual occupied cells on that shared grid are **(X8, Y8), (X7, Y7)**. The [assembly construction picture](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#1-views) distinguishes thick ownership borders from each real model outline, including overhang.

1. Use the matching parallel-kit build with Windows SimCity 4 and NAM 50 in right-hand traffic, including supported Wine or CrossOver use. See [the build and install guide](../../../../docs/BUILD_AND_INSTALL.md); compiling a build does not install it.
2. Open a disposable, flat test area, and follow the [complete assembly placement sequence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md#3-placements). The three adaptive pieces are placed P02, P01, and P03 first so each temporary helper corner starts clear.
3. Click **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond**. Press **Tab** to cycle forward or **Shift+Tab** to cycle backward until **DD RHW-4 — L2 Entry Slip Lanes — Parallel** appears. Each click places only that selected component.
4. Keep the authored 0° orientation for the reference plan. **Home** and **End** rotate the selected preview; use the actual occupied squares to match the table. Four proper rotations repeat across eight selection states, without reflecting traffic handedness.
5. Position the construction reference at **X7, Y8**, check the occupied cells listed above, and click once. Add the matching components at their own reference positions; never place a second owner on an occupied city square merely because two models overlap visually.

**Physical connection levels:** Both highway levels: 7.5/15 m; named access at 15 m. Match exact positions, height profiles, directions, and every boundary service on the generated cards. Matching a visible edge or one road lane alone does not establish a compatible neighbour. These fixed pieces do not adjust to arbitrary terrain heights, and the kit does not establish that native RHW can be dragged through its occupied cells.

<!-- BEGIN PIECE OVERVIEW -->

Place one l2 entry slip lanes for the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-upper-entry-slip`.

Footprint: **2 × 2 tiles**. Exact menu name: **DD RHW-4 — L2 Entry Slip Lanes — Parallel**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

Read from an entrance row to an exit column. A saved PATH is the traffic data stored in the game resource. Route Query is the route shown by the game, and Visible travel is an observed car or pedestrian completing it. The matrix describes this component's intrinsic fragments; the complete journey can pass through another component's city tile even when its physical model is visibly continuous. Physical joining sections and saved traffic cuts are checked separately.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-701d53baffa501be3ea7) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`channel-11-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-12-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-13-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-14-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-15-out`<br>Variant: access-ramp | **Road · West exit**<br>`channel-16-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-17-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-18-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-19-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-20-out`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a851c802d697803e8f52) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-278a1a7d7ea29b7fc590) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-54cedfc0491e8bf01523) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-be6cbbd827eb607ca9f7)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-be6cbbd827eb607ca9f7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0b0d7435c9b247d5258e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-353113ad73bc771ca613) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0a991cb9efd224d16fe9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f339070d8d10d79f9d15) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e9aebc8c77bf16e727a4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8acba46a3a4f31599208) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bdc8ae1bf952fb32e71b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e4bdc17c821873b68230) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-9d23535fe72ba9801464)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-9d23535fe72ba9801464) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c9ffeec9714e63b644b5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-94dae94e21ba9ae287c2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7b3437f96aa06c16c1bd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-35ada28323ec7eabaaf3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4bbe0e6c9d6b4673e106) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-499c96d5f2b7aa057ed7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a018e2a4cc0d2d46e0d6) |
| **Road · North entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a8c08d2be42e5261f728) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-d8ca1775df84aa31f076)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-d8ca1775df84aa31f076) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-09ed927ec4efd95f9aa4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0a6674f457cf4923ddfa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7fc3bf4b8b5b2d8a1f13) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4bd4f56aed7b3fab0fcd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3df106344513829b9d92) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-08911640c7763ac13a3d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0c60924f3a56e7b6e6d1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f9a48f55b21bca9ffd46) |
| **Road · South entrance**<br>`channel-04-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1baab1807a609ca8c322) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c3ab6fac8c86e4c02d82) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1372d73ea4cd9aeb7d9e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f75a1e99a1395a8fce88) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-4ae3f55d9291f755c75f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-4ae3f55d9291f755c75f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6055562585bf76898046) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-868018f7bdb64f5a94ee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2547aad666e7278304ac) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-669b77de64df70971b37) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-09bcae19c968ffac789f) |
| **Road · North entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ab9c989a6e29c87b252b)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ab9c989a6e29c87b252b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0e3085cc3b1cfecd18fb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6d3edd6f86972197920b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fec1d13caa8b9483e2c4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3dc2ab0a1da2a4414afa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fc2fd7d64e1d5f60cd4d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8dccd871afbef6b9325a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-394b11469ddd61e23120) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-96e9d13c96dbf9ca7aca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93ef4c25495dc876780a) |
| **Road · West entrance**<br>`channel-06-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eab2d1c1308ea80eda63) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-843168188006ea40ff32) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0e7ada239c2718768bb4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8baf50dcd58e781c2d12) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0e1b9411d189c4bf7190) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eba8384ac8ec3de29938) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-afc9dae213597ff4050a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b69c31de727cbcc10695) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c5d9e3396975d05d6ceb) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-2685f065254bb9abb247)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-2685f065254bb9abb247) |
| **Road · West entrance**<br>`channel-07-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b610c9dbeaef591ba59f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6db24bcb7ae38afbc505) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ca5d5bfe1bb4017b058e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93f18b557b2791d3efb1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ab315a9ad6ff03692069) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ec14a59f6bff2c2679d4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6d5320f1b194c082112b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-56d893e8d11011cefb71) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1e98f1a507a388fff896)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1e98f1a507a388fff896) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-11b822e2d01901925581) |
| **Road · North entrance**<br>`channel-08-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d52043b513fa627771f9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-620bb69800dd7c6284c5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-647d80f351975b465d92) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f7cf7efafa9fe6b49825) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-124bb87469e05a60bba3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bc5708b5c29b2ff65209) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1ee09d8832a4d037fee3)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1ee09d8832a4d037fee3) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-618133673926bb261bc2)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-618133673926bb261bc2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ad58650ba559bb2c76af) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-173322082c578b53d843) |
| **Road · South entrance**<br>`channel-09-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ba8b9a8938946522199f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6b3d2f50960e4567ebae) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fe0edd54bc3bbd776bbc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e4760cbfab8b9091fc98) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6a4db7bc776df5f94702) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a8c9fea8cb091ab6971d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-32e8dcd7597ce8db47de) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cb8df38c1a397a8733b9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c9353888dd9fded6aa16) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-bd924e97601e13226f4a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-bd924e97601e13226f4a) |
| **Road · North entrance**<br>`channel-10-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a873f1cdbbe7c6513066) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-aaa9acd41d2d7d9e262c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-353b442c2b29d77b2487) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8966baf4e88278af1726) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-119824842c02bda8cdd6) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-d20c322fa31793aee640)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-d20c322fa31793aee640) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9d33e9d9bb2d5d3ccbd6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1872ec9d10fcfef7685b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d61b46629c26f561b11c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-5673f882ca9f2be73133)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-12bc239eba24d5ebefd1) |

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

#### Boundary A: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (10.0624 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (10.0624 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | -28.203% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-04-in` / `channel-04-in` | `access-upper-on` / `cut-channel-04-in` / car | Incoming | `[0.970563,-24,10.0624]` | Not declared | 225° | -28.203 |

#### Boundary B: `boundary-02`

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
| `member-channel-05-in` / `channel-05-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-05-in` / car | Incoming | `[3.2,-8,7.5]` | Not declared | 45° | 0 |

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
| `member-channel-13-out` / `channel-13-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-13-out` / car | Outgoing | `[-3.2,-8,15]` | Not declared | 45° | 0 |
| `member-channel-14-out` / `channel-14-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-14-out` / car | Outgoing | `[3.2,-8,15]` | Not declared | 45° | 0 |

#### Boundary C: `boundary-01`

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
| `member-channel-11-out` / `channel-11-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-11-out` / car | Outgoing | `[-8,-19.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-12-out` / `channel-12-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-12-out` / car | Outgoing | `[-8,-12.8,7.5]` | Not declared | 225° | 0 |

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

#### Boundary D: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (12.866 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (12.866 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 28.2027% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-15-out` / `channel-15-out` | `access-upper-on` / `cut-channel-15-out` / car | Outgoing | `[8,-16.9706,12.866]` | Not declared | 45° | 28.2027 |

#### Boundary E: `boundary-07`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-07-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 199.871° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-09-in` / `channel-09-in` | `access-upper-on` / `cut-channel-09-in` / car | Incoming | `[16.1045,-8,15]` | Not declared | 199.871° | 0 |

#### Boundary F: `boundary-06`

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
| `member-channel-08-in` / `channel-08-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-08-in` / car | Incoming | `[12.8,8,7.5]` | Not declared | 45° | 0 |
| `member-channel-10-in` / `channel-10-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-10-in` / car | Incoming | `[19.2,8,7.5]` | Not declared | 45° | 0 |

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
| `member-channel-19-out` / `channel-19-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-19-out` / car | Outgoing | `[12.8,8,15]` | Not declared | 45° | 0 |
| `member-channel-20-out` / `channel-20-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-20-out` / car | Outgoing | `[19.2,8,15]` | Not declared | 45° | 0 |

#### Boundary G: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | Different; see members |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 3 / 3 / 3 |
| Traffic arrangement / running | 0 incoming; 3 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-16-out` / `channel-16-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-16-out` / car | Outgoing | `[8,-3.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-17-out` / `channel-17-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-17-out` / car | Outgoing | `[8,3.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-18-out` / `channel-18-out` | `access-lower-off` / `cut-channel-18-out` / car | Outgoing | `[8,6.19488,7.5]` | Not declared | 260.544° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-upper-mainline-02` / `upper-mainline` |
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
| `member-channel-06-in` / `channel-06-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-06-in` / car | Incoming | `[8,-3.2,15]` | Not declared | 225° | 0 |
| `member-channel-07-in` / `channel-07-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-07-in` / car | Incoming | `[8,3.2,15]` | Not declared | 225° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
