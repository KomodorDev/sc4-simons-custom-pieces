# DD RHW-4 — L1 Entry Slip Lanes — Parallel — Alignment B

Reusable Alignment B component for the close parallel diagonal diamond.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled view shows this type's actual model and overhang; the north-up view shows its relation to the city grid. These software pictures do not establish game appearance, native-neighbour compatibility, or visible traffic. Use the component's own pictures when comparing it with another type.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — L1 Entry Slip Lanes — Parallel — Alignment B — Clean angled view](previews/preview.png)

![DD RHW-4 — L1 Entry Slip Lanes — Parallel — Alignment B — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This straight highway section supplies the named entry auxiliary slip lane and its barrier opening. The curved departure and graded ramp are separate components. Both native decks remain present even though the name identifies access on only one level.

**Permanent ID:** `ddrhw-parallel-b-lower-entry-slip`. **Recipe:** `highway_ddrhw_parallel_b_lower_entry_slip`. This component owns **2 city tiles** inside a **2 × 2 bounding footprint**. Its local occupied cells are **[1,0], [0,1]**, measured from the reference corner with columns increasing east and rows increasing south. Empty cells inside that rectangle remain unowned. Both native decks at 7.5 m and 15 m; the named access is at 7.5 m.

1. Open **Transportation → Highways → SCP | DD RHW-4 — Parallel Diagonal Avenue Diamond**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond — Alignment B**.
2. Starting at P01, press **Tab 4 times** to reach **P05 — DD RHW-4 — L1 Entry Slip Lanes — Parallel — Alignment B**. Shift+Tab moves backward. Each click places this component, rather than the whole junction.
3. In the [B reference layout](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md#3-placements), use **X1, Y3**, with the authored **0°** orientation. Home and End rotate the selected type. Match its actual occupied preview cells before clicking; the reference corner can itself be empty.
4. Join only the complete matching B boundary described by its connection card and the assembly placement plan. A similar A model does not establish matching whole-cell PATH ownership. For an independent layout, check every direction, endpoint, height, angle, and grade; compatibility with an untested neighbour remains unverified.

This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here.

All B components intentionally generate no custom cast shadows. A **PATH** is the directed game traffic resource; a visible road surface and a PATH connection establish different facts. Preserve this type's complete owned-cell traffic data when reusing it. New B identifiers require fresh placement, and game results are recorded separately in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Place one l1 entry slip lanes for Alignment B of the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-b-lower-entry-slip`.

Footprint: **2 × 2 tiles**. Exact menu name: **DD RHW-4 — L1 Entry Slip Lanes — Parallel — Alignment B**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes this piece's intrinsic measured journeys. Its connector overview identifies exposed boundaries, including any overhang; it does not establish compatibility with an untested neighbour. Route Query and visible travel retain separate observation cases.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-29ff742febf764c2e5cb) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · South exit**<br>`channel-11-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-12-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`channel-13-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-14-out`<br>Variant: dd-rhw-l2 | **Road · West exit**<br>`channel-15-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-16-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-17-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`channel-18-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-19-out`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-94d4b18206429adfc5e7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f08708d5d6fa07bb66a8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a2c8d525b392150dfd96) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-7fde8b4fc6206fbd1ad4)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-7fde8b4fc6206fbd1ad4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5e5125e492fcc0f904f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-77980bdedce008d68ae1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3a6899ca24084a157d2b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cde641306ef4cf4cbcef) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7be9380bfbb354d63185) |
| **Road · South entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3f565fa0c323a9c73756) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-67684e05cd45530b26b1) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-513688fbe40046bd9aff)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-513688fbe40046bd9aff) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e3a69404a81af36c4a52) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bdeb37e9b92ebb5d5542) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e8896a6ffb7b10b3f51f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-11c70cb135234a5b8bb2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-174cba9629867cca76b3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c804c939002990aa7cd6) |
| **Road · North entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-4a8541a721bd328d01c6)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-4a8541a721bd328d01c6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3c06866f4e3f65048c58) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-51f84a1b91908fde640e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c20060def61713fbec39) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2e189badda694bd40ff4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-81311c336d12deeb804b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3eb94af836a06fd6b022) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ca6ce9c486650bf52d83) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1a11fcd557e69eaed342) |
| **Road · East entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-363f343fd2edcb858639) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-d6b6769f2c6328a8553a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-d6b6769f2c6328a8553a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-865ff3455fdaa075edec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8c2bbfcf74646fe6aa4c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0d0b11c78615b557503a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-be74bfe7e1948f84d03e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-805f050897b3f81a97ba) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5a22d6358affc10a3bcf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-82b135631f0516874208) |
| **Road · East entrance**<br>`channel-05-in`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-a74fcdc16e9ba96ccd0d)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-a74fcdc16e9ba96ccd0d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e377e6f23c7f31e6def5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d5bdd5534945adbba6a8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2e7702a56919b66352c6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3578e40aa18f0eb6d612) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1124cd39a3238d07e9cd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-897d03274e0f7cd46e2b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e8ddd3b3fdce62a5c71b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6bb8d4923d445ece7ba7) |
| **Road · South entrance**<br>`channel-06-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-53ed37e650e49f997f4b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-80866287187b39dd54cf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b578b8f42cd79916f349) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5417a9f185a2f444be4f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2e089a86806d2939a455) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e803868e484442f53319) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ca6f83c2bcff85f14faa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4a7d6670cc6cf0a133b9) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-8177877dc4db33e225a9)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-8177877dc4db33e225a9) |
| **Road · North entrance**<br>`channel-07-in`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-efc5b0b3ab0788a57f73) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fc1344d73719c61f82d7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e8e9683b6c8e7318d1a6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-80323d5d84d0434c3797) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-a485e252c4d37d4d33b5)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-a485e252c4d37d4d33b5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-893e9918599ba0aa44cb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-56d970b43df615067ab0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c59fe08bcb6bde42a608) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ff4ed4674cc821842152) |
| **Road · South entrance**<br>`channel-08-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6bae99747cf3f8252460) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2117b22c4a7deacf0c0e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-16df1e6958ce94b5e2cd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-faf7f955ffeb1eab09c6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9da3e6d75b88d2473569) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f2933f43de637649804a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-76301c55dc2023ff12bb) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-1fc9ea092c9cb1d2fb3b)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-1fc9ea092c9cb1d2fb3b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f54212176b97c9877f7d) |
| **Road · East entrance**<br>`channel-09-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-967fe322a8d2a3189d52) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6732191f03b01fb2c5ce) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-003ebc0cec57350d15ca) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7a01c8fb6133ce7588ad) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-08ccdb85b899149874fa) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1f5002d87ecea923caf5) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-e28ef7484058cfcfc32d)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-e28ef7484058cfcfc32d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-62be2aee189f5e6f3dcb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-35158724bb8559828c0d) |
| **Road · East entrance**<br>`channel-10-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8cf909bbfb3b5ac37a82) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-23eac39c379ba2f0db42) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b67e9ae37b50ece62a7c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ba7641f58c7991f4e1a1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-51ec101f9e160399541b) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-bad96b9546be2fd42be9)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-bad96b9546be2fd42be9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ffa21fbd17186e8631a7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f831b11480553900fab3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-b93711ed3421d9c4e174)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dcc343b0d4231dd3eb05) |

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

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
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
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
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
| `member-channel-02-in` / `channel-02-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-02-in` / car | Incoming | `[3.2,-24,15]` | Not declared | 225° | 0 |

#### Boundary B: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 10.8206° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-03-in` / `channel-03-in` | `access-lower-on` / `cut-channel-03-in` / car | Incoming | `[7.15582,-8,7.5]` | Not declared | 10.8206° | 0 |

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
| `member-channel-13-out` / `channel-13-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-13-out` / car | Outgoing | `[8,-19.2,15]` | Not declared | 45° | 0 |
| `member-channel-14-out` / `channel-14-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-14-out` / car | Outgoing | `[8,-12.8,15]` | Not declared | 45° | 0 |

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
| `member-channel-08-in` / `channel-08-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-08-in` / car | Incoming | `[19.2,-8,15]` | Not declared | 225° | 0 |

#### Boundary E: `boundary-05`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.39058 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.39058 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -17.9116% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-07-in` / `channel-07-in` | `access-lower-on` / `cut-channel-07-in` / car | Incoming | `[15.0294,8,6.39058]` | Not declared | 45° | -17.9116 |

#### Boundary F: `boundary-04`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 202.664° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-15-out` / `channel-15-out` | `access-lower-on` / `cut-channel-15-out` / car | Outgoing | `[8,0.265154,7.5]` | Not declared | 202.664° | 0 |

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
| `member-channel-18-out` / `channel-18-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-18-out` / car | Outgoing | `[24,-3.2,15]` | Not declared | 45° | 0 |
| `member-channel-19-out` / `channel-19-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-19-out` / car | Outgoing | `[24,3.2,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
