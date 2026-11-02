# DD RHW-4 — L2 Exit Slip Lanes — Parallel — Alignment B

Reusable Alignment B component for the close parallel diagonal diamond.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled view shows this type's actual model and overhang; the north-up view shows its relation to the city grid. These software pictures do not establish game appearance, native-neighbour compatibility, or visible traffic. Use the component's own pictures when comparing it with another type.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — L2 Exit Slip Lanes — Parallel — Alignment B — Clean angled view](previews/preview.png)

![DD RHW-4 — L2 Exit Slip Lanes — Parallel — Alignment B — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This straight highway section supplies the named exit auxiliary slip lane and its barrier opening. The curved departure and graded ramp are separate components. Both native decks remain present even though the name identifies access on only one level.

**Permanent ID:** `ddrhw-parallel-b-upper-exit-slip`. **Recipe:** `highway_ddrhw_parallel_b_upper_exit_slip`. This component owns **3 city tiles** inside a **3 × 3 bounding footprint**. Its local occupied cells are **[2,0], [1,1], [0,2]**, measured from the reference corner with columns increasing east and rows increasing south. Empty cells inside that rectangle remain unowned. Both native decks at 7.5 m and 15 m; the named access is at 15 m.

1. Open **Transportation → Highways → SCP | DD RHW-4 — Parallel Diagonal Avenue Diamond**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond — Alignment B**.
2. Starting at P01, press **Tab 5 times** to reach **P06 — DD RHW-4 — L2 Exit Slip Lanes — Parallel — Alignment B**. Shift+Tab moves backward. Each click places this component, rather than the whole junction.
3. In the [B reference layout](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md#3-placements), use **X1, Y3**, with the authored **0°** orientation. Home and End rotate the selected type. Match its actual occupied preview cells before clicking; the reference corner can itself be empty.
4. Join only the complete matching B boundary described by its connection card and the assembly placement plan. A similar A model does not establish matching whole-cell PATH ownership. For an independent layout, check every direction, endpoint, height, angle, and grade; compatibility with an untested neighbour remains unverified.

This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here.

All B components intentionally generate no custom cast shadows. A **PATH** is the directed game traffic resource; a visible road surface and a PATH connection establish different facts. Preserve this type's complete owned-cell traffic data when reusing it. New B identifiers require fresh placement, and game results are recorded separately in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Place one l2 exit slip lanes for Alignment B of the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-b-upper-exit-slip`.

Footprint: **3 × 3 tiles**. Exact menu name: **DD RHW-4 — L2 Exit Slip Lanes — Parallel — Alignment B**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes this piece's intrinsic measured journeys. Its connector overview identifies exposed boundaries, including any overhang; it does not establish compatibility with an untested neighbour. Route Query and visible travel retain separate observation cases.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-11fb118aebb6a1c0f65c) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`channel-15-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-16-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-17-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-18-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-19-out`<br>Variant: dd-rhw-l2 | **Road · West exit**<br>`channel-20-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-21-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-22-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-23-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-24-out`<br>Variant: access-ramp | **Road · West exit**<br>`channel-25-out`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`channel-26-out`<br>Variant: dd-rhw-l1 | **Road · North exit**<br>`channel-27-out`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`channel-28-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-29-out`<br>Variant: access-ramp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-84edd9ed7244cf47f598) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eb87d40e8c3d118dbfd0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-464e00e4cc834c9bbb14) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-36e938f0ff6ccac560fc)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-36e938f0ff6ccac560fc) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-f15fdf6d3262ff08b54f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-f15fdf6d3262ff08b54f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d0551a87182d87248388) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5ec3d0a1f40daa82fc6f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9efe37202c7390a34258) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e65de01d1e02fffca08a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7967fe49dd64bf4df98f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e8d284f53e9e2d3db7d3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-26cd95505a69c0916f44) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9974c46a51ec4692e83d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8fef8ee4ea404ff818bc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fa484b2520c48464f15d) |
| **Road · West entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d99e2f991dca589850f4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6e51db4470f855305836) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-96ab85494cf96da974ee)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-96ab85494cf96da974ee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-97ca54e79ed0af693ef3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b8fedfc998f034efed51) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9fdaf80a247efa167812) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7500700c71e0583bfdb7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3783542425c2cace0512) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9bfc9f74ca8fe4b84e42) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-261b104837df790e30de) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6ab7e1e61ca291305e85) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-896d036f9471ea3d7a24) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-13c14d73f6365d0c3939) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ca4946de3c6a10419034) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1e49899541005c2c510d) |
| **Road · North entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ecd10515a6f810978f6a) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-89b78e45ea9a7115eb2f)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-89b78e45ea9a7115eb2f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-01ca4d1f4f88d42aa0fa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a13f83fd614a06e3a654) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7b58f799a15d89f04ebe) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3a9a499d8dd05181790c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3576324bc3f3361199ee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-044064da0b8d30689a3b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f355f60a27c178bfb666) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fb4c52c2461c35aec390) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-62935e6170aae5447e98) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ac1d358c37eb320165f1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c1ec262db489472ceb0c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cef28d7570a1ac3f6b94) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-001f2cb42db370307b31) |
| **Road · North entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b72a58e1abc94eda9ee4)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b72a58e1abc94eda9ee4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3094b0beee7d90f78797) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-43be845b1d7c57eddaaf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-79728c1a335cf747cedb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b6f75d04649266519838) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d2a32561be0141f1758b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2bf43b752dd6e900a0cc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c973a6e070d95995b8f4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c33b609c8789a1dbf91b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b401adaa139ae12cc32d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f03c13cbbc064f2381c0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b918747ef9c36892ec49) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3b9951ce6afe7ad9b227) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-00703f7774cc51f83312) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b93678edd40776586c6e) |
| **Road · West entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6668afbdb310287f63be) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6bb1b08ca88dd562165b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2056097033752f102ab4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-68af14102f4a1292c0cf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3379366c73aa0c5d3564) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6d292b65c5bcc78caef0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9a71790a97990b4c64ca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3718a9de40c47a223413) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ed5c5fd66fcc01e0e7e4)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ed5c5fd66fcc01e0e7e4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5303952cd8932973d864) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-db8a9c690bf165f16ad6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ad554e81493b577556ab) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3b05fcb7ba123a3d2a3d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9bd007428fb20aecb0b1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-abe928d1e46293577570) |
| **Road · West entrance**<br>`channel-06-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7bf16c9eb132e125f17d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4466ab19d64a135e7a81) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0782b5b4001048d9c417) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-17100b503233299bc16f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-89c41688d0e0ade3d634) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-95d6a24d597571df7359) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1941374d0e39583d565f) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-a58a585befe92df602ee)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-a58a585befe92df602ee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-34dc3654bd32c4628d54) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5b701b7b8e4fed6646e2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f7172d9a14338049fe10) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9bd9843c74fc045e0eeb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f09d3e4272ffd88fa280) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c36e8608d2bd66a1aaba) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5cf45076aaeedaddbbbf) |
| **Road · North entrance**<br>`channel-07-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b651562f17dbeaab38eb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4f93d6e621f76aafe7d7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1abd9af1a70b2bb4583b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4ac85f20b62dc096d28e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e2bca7cdb4847cf21b55) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4cf63bc6cc8cdf5ec8c2) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-ac8f575ee14f80adee57)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-ac8f575ee14f80adee57) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0ec0d974e1c4b6e292db) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cac0d615b67fa9100c91) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-57732e6caa9943f47728) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9d69c1222fcddd241d35) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4428c91aa0c6b1d75b20) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6bce69e5e7e557ed0c69) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f0cec7675466993227ec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eacf6e89f3defab0aff2) |
| **Road · South entrance**<br>`channel-08-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-172ea99462de02ca87ea) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b2a6c9caa2c8c7e069af) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-880a4b2508119014cb2e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-60526dbb1bf709423717) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ecdcbd83563c32a0694d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-20c9bbed78eb72650203) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2246e7ad665409468c59) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5b8509f498e7c7b770dc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a63ef07c7871d210c19) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-caf1355a6b565e39a043)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-caf1355a6b565e39a043) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3ea52daf7941b59d6aa5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-95841317b89e395e719f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b1c3557aea1fa69a66dc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b7e7cd99b79de81f8c14) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d274f4865e222ec09c3c) |
| **Road · North entrance**<br>`channel-09-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4a306069bf048319a0de) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-adb51a3ffc7b54cf9be1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-97b5f3a3be182463aae7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e72cb7b1cc4bcba7bf6d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-685ce1b7a52a11170791) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-6c7a1eb2bc9611bad1b1)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-6c7a1eb2bc9611bad1b1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-89e0066bac2026114a14) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-60b4a9fe372384ccf3fc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-526b30919053b308fb27) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7e095df1c5ddb8e2e8d4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1cc42f90147acc0a2e93) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-97fea147433dcc59fbe2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f7d6f13f5112948ead29) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3af249450d0e38c09f2b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f6d7969345e3c207322c) |
| **Road · West entrance**<br>`channel-10-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-323ea9231215d804cce8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fddfa6fdd123f119e5d1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-667d9ba12df045fd211a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4bf4f670950359a41909) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-185d58e1fd71920472d1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a100f5f4389838fed7e1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-99c039f00ffee27b82c0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8ebb066d4441c064d977) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1c0dac6ec5a22cb93673) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ec0ae224e0e564c475c4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-858cde169445bf625a12) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3b50da22d028d1ce080d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-15fc0a306a8476a776c2) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b6a44d9079a41dfd88d0)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b6a44d9079a41dfd88d0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4ac67af7c6fcc0b3e566) |
| **Road · West entrance**<br>`channel-11-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-16b9689224eb13f22abc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5659e84cf80c61fde7c2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d09effb98e5b5dc135c1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ca2d6b8ad33bdde7eca4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e44bf47e79bae795b303) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f0362a74a1e5354bf0d2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-81fd53e09141884b01dc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8acd7b6fb3463ee6c3ea) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ce326bc2201aa860080e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ced4311eefb15236c297) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-384ab53ac5d474d1aad9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d8630c5687bfc0287a86) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1d31778119ce9e056078)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1d31778119ce9e056078) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b1d692f5aadc46b2ee0e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d507a0f03789d6ff4503) |
| **Road · North entrance**<br>`channel-12-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3d658770ee2567b4b61e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-392687966bb41b607734) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b897e64533580a578e27) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-beaa22159b1ddf20283c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-891a4d95814dd3db8593) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e68c662241a0ad79cf0a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2006b073d2f6494fab61) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-42d3293402110f06421f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-27d27ec5288eec9fb186) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-04ed2f137c7d00de90ca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-856e8655b6c91bfbcdf3) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-0ad3392b598fc7f66f1e)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-0ad3392b598fc7f66f1e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-61c90af13a3835473e22) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8cebb5b1c05fb5c28f67) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-eaf8080921a491f92f27) |
| **Road · South entrance**<br>`channel-13-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f51d0f6815bd2d1314d2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a8eea7d1e5e91e757074) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c7bd4b0b3f3d6e74a181) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-be769c3d58d54f251e67) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0289e918136962f6e2d4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-602625e5184897e22d27) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-99a00a73da5e16f3be4e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6f55670442d7f6e8e414) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-661e8faa6427c6a9f6a0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8ee8326e9d6ed07d20b0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1008e664a648aa2bea37) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6378bce2caae67dab396) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c166ac67ee1bfef54852) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a68993964ffbe16cdec6) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-d420fdc2db15e4e7215a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-d420fdc2db15e4e7215a) |
| **Road · North entrance**<br>`channel-14-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1d71267c862adee41294) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-784cebda3cd1d6f632ec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cbc049e3f045bd9a61a8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5bc7ef41f5d5fe8e30bc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5a243309eeaea9cc6177) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c172846c7a166f7e12ed) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a572f9ae2c5df795da9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d0168dba6a2687e4dd81) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2f4461d70df58a0c666c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b56cf1d86b453dc35397) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-7482898f2de323941acd)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-7482898f2de323941acd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dd30e0cdb85c0489557d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0351cd50b9f76a530e77) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d6f240438d458eea0709) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-0fda03ea04e8723e4ee2)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-90bd756b9e4e100ea02a) |

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

#### Boundary A: `boundary-02`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / North |
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
| `member-channel-03-in` / `channel-03-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-03-in` / car | Incoming | `[-3.2,-24,7.5]` | Not declared | 45° | 0 |
| `member-channel-04-in` / `channel-04-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-04-in` / car | Incoming | `[3.2,-24,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / North |
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
| `member-channel-17-out` / `channel-17-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-17-out` / car | Outgoing | `[-3.2,-24,15]` | Not declared | 45° | 0 |
| `member-channel-18-out` / `channel-18-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-18-out` / car | Outgoing | `[3.2,-24,15]` | Not declared | 45° | 0 |

#### Boundary B: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / West |
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
| `member-channel-15-out` / `channel-15-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-15-out` / car | Outgoing | `[-8,-35.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-16-out` / `channel-16-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-16-out` / car | Outgoing | `[-8,-28.8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / West |
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
| `member-channel-01-in` / `channel-01-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-01-in` / car | Incoming | `[-8,-35.2,15]` | Not declared | 225° | 0 |
| `member-channel-02-in` / `channel-02-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-02-in` / car | Incoming | `[-8,-28.8,15]` | Not declared | 225° | 0 |

#### Boundary C: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,2]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 82.6987° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-19-out` / `channel-19-out` | `access-upper-off` / `cut-channel-19-out` / car | Outgoing | `[8,-24.6717,15]` | Not declared | 82.6987° | 0 |

#### Boundary D: `boundary-07`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-07-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 247.336° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-08-in` / `channel-08-in` | `access-upper-off` / `cut-channel-08-in` / car | Incoming | `[16.2652,-24,15]` | Not declared | 247.336° | 0 |

#### Boundary E: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / North |
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
| `member-channel-07-in` / `channel-07-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-07-in` / car | Incoming | `[12.8,-8,7.5]` | Not declared | 45° | 0 |
| `member-channel-09-in` / `channel-09-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-09-in` / car | Incoming | `[19.2,-8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / North |
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
| `member-channel-22-out` / `channel-22-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-22-out` / car | Outgoing | `[12.8,-8,15]` | Not declared | 45° | 0 |
| `member-channel-23-out` / `channel-23-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-23-out` / car | Outgoing | `[19.2,-8,15]` | Not declared | 45° | 0 |

#### Boundary F: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / West |
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
| `member-channel-20-out` / `channel-20-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-20-out` / car | Outgoing | `[8,-19.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-21-out` / `channel-21-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-21-out` / car | Outgoing | `[8,-12.8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / West |
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
| `member-channel-05-in` / `channel-05-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-05-in` / car | Incoming | `[8,-19.2,15]` | Not declared | 225° | 0 |
| `member-channel-06-in` / `channel-06-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-06-in` / car | Incoming | `[8,-12.8,15]` | Not declared | 225° | 0 |

#### Boundary G: `boundary-06`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (13.2531 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (13.2531 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-24-out` / `channel-24-out` | `access-upper-off` / `cut-channel-24-out` / car | Outgoing | `[24,-16.9706,13.2531]` | Not declared | 45° | -28.2029 |

#### Boundary H: `boundary-11`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (9.67524 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-11-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (9.67524 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-13-in` / `channel-13-in` | `access-upper-off` / `cut-channel-13-in` / car | Incoming | `[32.9706,-8,9.67524]` | Not declared | 225° | 28.2029 |

#### Boundary I: `boundary-09`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-09-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / North |
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
| `member-channel-12-in` / `channel-12-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-12-in` / car | Incoming | `[28.8,8,7.5]` | Not declared | 45° | 0 |
| `member-channel-14-in` / `channel-14-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-14-in` / car | Incoming | `[35.2,8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-09-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / North |
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
| `member-channel-27-out` / `channel-27-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-27-out` / car | Outgoing | `[28.8,8,15]` | Not declared | 45° | 0 |
| `member-channel-28-out` / `channel-28-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-28-out` / car | Outgoing | `[35.2,8,15]` | Not declared | 45° | 0 |

#### Boundary J: `boundary-08`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-08-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / West |
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
| `member-channel-25-out` / `channel-25-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-25-out` / car | Outgoing | `[24,-3.2,7.5]` | Not declared | 225° | 0 |
| `member-channel-26-out` / `channel-26-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-26-out` / car | Outgoing | `[24,3.2,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-08-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / West |
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
| `member-channel-10-in` / `channel-10-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-10-in` / car | Incoming | `[24,-3.2,15]` | Not declared | 225° | 0 |
| `member-channel-11-in` / `channel-11-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-11-in` / car | Incoming | `[24,3.2,15]` | Not declared | 225° | 0 |

#### Boundary K: `boundary-10`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.87155 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-10-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.87155 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -28.2029% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-29-out` / `channel-29-out` | `access-upper-off` / `cut-channel-29-out` / car | Outgoing | `[40,-0.970563,6.87155]` | Not declared | 45° | -28.2029 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
