# DD RHW-4 — L1 Exit Slip Lanes — Parallel — Alignment B

Reusable Alignment B component for the close parallel diagonal diamond.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled view shows this type's actual model and overhang; the north-up view shows its relation to the city grid. These software pictures do not establish game appearance, native-neighbour compatibility, or visible traffic. Use the component's own pictures when comparing it with another type.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — L1 Exit Slip Lanes — Parallel — Alignment B — Clean angled view](previews/preview.png)

![DD RHW-4 — L1 Exit Slip Lanes — Parallel — Alignment B — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This straight highway section supplies the named exit auxiliary slip lane and its barrier opening. The curved departure and graded ramp are separate components. Both native decks remain present even though the name identifies access on only one level.

**Permanent ID:** `ddrhw-parallel-b-lower-exit-slip`. **Recipe:** `highway_ddrhw_parallel_b_lower_exit_slip`. This component owns **2 city tiles** inside a **2 × 2 bounding footprint**. Its local occupied cells are **[1,0], [0,1]**, measured from the reference corner with columns increasing east and rows increasing south. Empty cells inside that rectangle remain unowned. Both native decks at 7.5 m and 15 m; the named access is at 7.5 m.

1. Open **Transportation → Highways → SCP | DD RHW-4 — Parallel Diagonal Avenue Diamond**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond — Alignment B**.
2. Starting at P01, press **Tab 3 times** to reach **P04 — DD RHW-4 — L1 Exit Slip Lanes — Parallel — Alignment B**. Shift+Tab moves backward. Each click places this component, rather than the whole junction.
3. In the [B reference layout](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md#3-placements), use **X7, Y9**, with the authored **0°** orientation. Home and End rotate the selected type. Match its actual occupied preview cells before clicking; the reference corner can itself be empty.
4. Join only the complete matching B boundary described by its connection card and the assembly placement plan. A similar A model does not establish matching whole-cell PATH ownership. For an independent layout, check every direction, endpoint, height, angle, and grade; compatibility with an untested neighbour remains unverified.

This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here.

All B components intentionally generate no custom cast shadows. A **PATH** is the directed game traffic resource; a visible road surface and a PATH connection establish different facts. Preserve this type's complete owned-cell traffic data when reusing it. New B identifiers require fresh placement, and game results are recorded separately in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Place one l1 exit slip lanes for Alignment B of the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-b-lower-exit-slip`.

Footprint: **2 × 2 tiles**. Exact menu name: **DD RHW-4 — L1 Exit Slip Lanes — Parallel — Alignment B**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes this piece's intrinsic measured journeys. Its connector overview identifies exposed boundaries, including any overhang; it does not establish compatibility with an untested neighbour. Route Query and visible travel retain separate observation cases.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-c149460b9bb96b43189c) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`channel-10-out`<br>Variant: access-ramp | **Road · South exit**<br>`channel-11-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-12-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`channel-13-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-14-out`<br>Variant: dd-rhw-l2 | **Road · West exit**<br>`channel-15-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-16-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-17-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`channel-18-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-19-out`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0e49f22d0b91540ac41d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-068af5231506f8e364f5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8549730f3101b9ce6f4b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c22cc2983e6710a0943c) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-66ccbc65ba8db91dce10)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-66ccbc65ba8db91dce10) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-18996e341f673c014f7b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-82666ea2d60b7f7c8057) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a38724157adbe249c74a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a9ce9b143b62a6e92d1c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b1b7894eb168be5a4ed5) |
| **Road · North entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-0472fa25ca66e7fb4e31)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-0472fa25ca66e7fb4e31) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5244c57f2fcb31c7e50b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cf2921ed561997ea785d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6dd0537e3bd48750c1db) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dfec688f86dea81a14f7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-38f30774ed1d7160f953) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-927b9052e8be683d4ce6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-75554fc2fdafeb4e4e68) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-010ebdc8a00478c8dd08) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9a5c83b2aa5a1e745548) |
| **Road · South entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-736272655b1787a36cd5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e58bb0ba8a6ef94bd61f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4cbe5f5c168c0755d96a) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-dacbb371cb614834008b)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-dacbb371cb614834008b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-868a0457b82b4b27739c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-764a328d9dbc84ceff4e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9c8cfd53cd16788278bc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c922a6c6526e1eaccc26) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-10d53b55ad8e3b8cb89e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f46afaf6e2f6feb989dd) |
| **Road · East entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-69b3d7b34e36035beed2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f974d11b5d952ab062be) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-64932ca7bed9b988ba9c)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-64932ca7bed9b988ba9c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7ca368a896dfae69bc32) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-18c8c479a23e45996098) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9815b3fc3f5615a82f48) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0901d80b2d512f978b46) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b31abf7e8602b4be2dd9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e2ce7f28291d6b9f10a6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-41e3882fc6a54435751e) |
| **Road · East entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a8bd5c9703c7f4591474) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-18b3f543fb1f0f29fa82)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-18b3f543fb1f0f29fa82) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f9a60e8ba0d6b6f78d55) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ee3a9e8d90f996c1a401) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bea7b6d265f1f4bcefe8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b03ea8bddf396277b9bd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eaad0b755d5ebe55e7e4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7c242ea95f71ec200661) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e4077c17871354fd44f1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-22d782a9655782b81930) |
| **Road · South entrance**<br>`channel-06-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-df8de60e3c755b5c7199) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-263eead1136617c251bf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f2d0ec9cc483df514253) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e531a78885c193ea22f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-23f9ab816b63b9c6265b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8bb9a11dda378d304a07) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-026ee28ad7583f57cf79) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f308190f60231c5fff62) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b4593808f48f014c8c5e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-abbefb985bb65a708b66)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-abbefb985bb65a708b66) |
| **Road · South entrance**<br>`channel-07-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4c9c381b845dbd9205be) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e73c639e69681b3bdca8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fa8697456fbfd8005704) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b535deaaa573959a515d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-09bc1307b2df324175fe) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f9889ba227b2d146ddce) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f389b512fb50c3cbdd0b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-57af3b76e79f59992ae7) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-3de67bef7e0007fe5746)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-3de67bef7e0007fe5746) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-82824adabfde13ae6c69) |
| **Road · East entrance**<br>`channel-08-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ba47d197fed962eaf1db) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-55ba30e3b6cdf4da48b7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b50fd085be4e4fee5acc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ee98152b251116a9ac96) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e7271206cc83d890f70c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-505865c694cf366e216e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d23f889d979e10007238) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-155cdf86bba942c1d913)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-155cdf86bba942c1d913) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-63e5311c72dcea159ce8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-69154ea9d1b4b3965138) |
| **Road · East entrance**<br>`channel-09-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3a5712996d4a1acafca8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d11b62aad828bc567d1c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1112fab7ed23e05f7791) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4e7f953816177372527d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d1f13c777e8bcaf3436e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-948d73cfe0603d541698)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-948d73cfe0603d541698) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-50eec1bdd8f240a0d847)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-50eec1bdd8f240a0d847) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e1f94786d8182ad44f25) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e17270fb0675e1a87682) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-ff9ce034c4b285775371)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9cd046b1cc5ab7ea2d60) |

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

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
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
| `member-channel-11-out` / `channel-11-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-11-out` / car | Outgoing | `[-3.2,-24,7.5]` | Not declared | 225° | 0 |
| `member-channel-12-out` / `channel-12-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-12-out` / car | Outgoing | `[3.2,-24,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-02` / `upper-mainline` |
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

#### Boundary B: `boundary-02`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 67.3356° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-02-in` / `channel-02-in` | `access-lower-off` / `cut-channel-02-in` / car | Incoming | `[-0.265154,-8,7.5]` | Not declared | 67.3356° | 0 |

#### Boundary C: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.39058 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.39058 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | -17.9116% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-10-out` / `channel-10-out` | `access-lower-off` / `cut-channel-10-out` / car | Outgoing | `[-8,-15.0294,6.39058]` | Not declared | 225° | -17.9116 |

#### Boundary D: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
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
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
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
| `member-channel-13-out` / `channel-13-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-13-out` / car | Outgoing | `[8,-19.2,15]` | Not declared | 45° | 0 |
| `member-channel-14-out` / `channel-14-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-14-out` / car | Outgoing | `[8,-12.8,15]` | Not declared | 45° | 0 |

#### Boundary E: `boundary-07`

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
| `member-channel-16-out` / `channel-16-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-16-out` / car | Outgoing | `[12.8,-8,7.5]` | Not declared | 225° | 0 |
| `member-channel-17-out` / `channel-17-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-17-out` / car | Outgoing | `[19.2,-8,7.5]` | Not declared | 225° | 0 |

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
| `member-channel-07-in` / `channel-07-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-07-in` / car | Incoming | `[19.2,-8,15]` | Not declared | 225° | 0 |

#### Boundary F: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 259.179° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-15-out` / `channel-15-out` | `access-lower-off` / `cut-channel-15-out` / car | Outgoing | `[8,-7.15582,7.5]` | Not declared | 259.179° | 0 |

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
| `member-channel-08-in` / `channel-08-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-08-in` / car | Incoming | `[24,-3.2,7.5]` | Not declared | 45° | 0 |
| `member-channel-09-in` / `channel-09-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-09-in` / car | Incoming | `[24,3.2,7.5]` | Not declared | 45° | 0 |

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
| `member-channel-18-out` / `channel-18-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-18-out` / car | Outgoing | `[24,-3.2,15]` | Not declared | 45° | 0 |
| `member-channel-19-out` / `channel-19-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-19-out` / car | Outgoing | `[24,3.2,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
