# DD RHW-4 — Diagonal Highway and Slip-Lane Stamp

Purpose: place both highway decks and their slip-lane openings together, then attach the ramp pieces independently.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled and north-up views render the actual saved game models and their referenced textures. The connection overview uses the shared complete-boundary cards, including nonzero endpoint slopes.

<!-- BEGIN PIECE VIEWS -->

![DD RHW-4 — Diagonal Highway and Slip-Lane Stamp — Clean angled view](previews/preview.png)

![DD RHW-4 — Diagonal Highway and Slip-Lane Stamp — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This is one highway stamp: both elevated decks, their retained native supports, and all four slip-lane openings are placed together. It owns 27 construction tiles in a sparse 10 × 10-tile rectangle. It contains no descending or ascending ramp and no Avenue ramp terminal. The four sloped openings are fixed; attach either the complete retained compact set or the R40 set shown in the modular assembly.

A **construction tile** is a 16 × 16 m city square occupied by this piece. This piece owns 27 tiles inside a 10 × 10-tile bounding rectangle. Model artwork can extend beyond an owned tile; the assembly plan keeps the construction ownership separate.

1. Prepare Windows SimCity 4 with the exact NAM 50 right-hand-traffic inputs in the [build guide](../../../../docs/BUILD_AND_INSTALL.md), including the adaptive Avenue capture for the stamp and terminals.
2. Open a disposable city and flatten the full 10 × 10-tile placement area.
3. Open **Transportation → Highways**, and select **SCP | ASSEMBLY | DD RHW-4 — Modular Diagonal Avenue Diamond**. Press **Tab** or **Shift+Tab** until **DD RHW-4 — Diagonal Highway and Slip-Lane Stamp** appears. Each click places just this component.
4. Follow the [assembly placement table](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/README.md#3-placements) for the reference tile and rotation. Press **Home** or **End** to rotate, then click once at the specified reference position.
5. After the seven parts are placed, extend ordinary diagonal Avenue approaches from the two outer Avenue ends. Placing over an existing Avenue or dragging through occupied pieces remains a separate unverified game test.

The stamp retains native Avenue paths underneath the crossing. Two Avenue-only cells use pristine native pavement so that detached compact ramp artwork does not remain underneath the new layout. Eight selection states repeat four rotations; they do not reflect the traffic directions. Custom attachments must match the whole connector card, including position, height, heading, slope, direction, and all services. A matching card alone does not prove that barriers and road surfaces fit; see [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Place the complete double-decker highway and four slip-lane openings in one click. On-ramps, off-ramps, and Avenue terminals are separate pieces attached at measured sloped boundaries.

Exact reusable identifier: `ddrhw-modular-highway-stamp`.

Footprint: **10 × 10 tiles**. Exact menu name: **DD RHW-4 — Diagonal Highway and Slip-Lane Stamp**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes movements within this piece. A connector overview, when supplied, describes its exposed boundaries; neither establishes compatibility with an untested neighbour.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-d0ef5112f7b9929ff065) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · West exit**<br>`1-W-out-1`<br>Variant: dd-rhw-l1 | **Road · West exit**<br>`1-W-out-3`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`1-E-out-6`<br>Variant: access-ramp | **Road · West exit**<br>`1-W-out-9`<br>Variant: avenue-ground | **Road · West exit**<br>`1-W-out-10`<br>Variant: avenue-ground | **Road · East exit**<br>`1-E-out-11`<br>Variant: avenue-ground | **Road · East exit**<br>`1-E-out-12`<br>Variant: avenue-ground | **Road · West exit**<br>`1-W-out-15`<br>Variant: access-ramp | **Road · North exit**<br>`1-N-out-18`<br>Variant: dd-rhw-l2 | **Road · North exit**<br>`1-N-out-20`<br>Variant: dd-rhw-l2 | **Pedestrian · West exit**<br>`2-W-out-2`<br>Variant: avenue-sidewalk | **Pedestrian · East exit**<br>`2-E-out-3`<br>Variant: avenue-sidewalk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Road · West entrance**<br>`1-W-in-2`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-66febcb432cac1b0159c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7c40e76bd8c2b4346058) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-970fc5a9b1d0a8c2372a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-970fc5a9b1d0a8c2372a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cb1d8096403374f1e242) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-198dc316adf9147dc23d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4d7d1963b00195b4ecd7) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d43e2f8e9f2b30e24418) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-03030d91a135ec960cdb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b25a6beded8762da7bd1) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-5a1d5c5a6d49fee5445c)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-5a1d5c5a6d49fee5445c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ec80ad41a12a10f10477) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d33a9ff99515e785533a) |
| **Road · West entrance**<br>`1-W-in-4`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cfd406c14ccc7ffe5e6b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c24ff28a590450ae79b6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-75db42d202240f976d3f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c023ade9ddb73040ad5a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d7afccb42ffd3737365c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f7820ea78f9a413160ab) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-038ac45d6c38b5c75bd9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-18bcc3ddb4f43bbc492d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-a3aff6dcd302447428bb)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-a3aff6dcd302447428bb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9a2a30813cbe5f01849b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-10c4a0acbc7c51574909) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-135e7c32048431400296) |
| **Road · North entrance**<br>`1-N-in-5`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ab707a58a23111cb6d24) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b3c07d4ff49097bc85fb)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b3c07d4ff49097bc85fb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-93422a00895ba981be05) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-05de384baedba0fdabd1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e8619c9b4d4208509fb0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9a340fa9aadab45ee9b5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-45f069120d53d41b817f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bb18a9801562490ade39) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-942f27966016777a316b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dbe3da1852990a5a5623) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0834b6565e74b47aefe1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-630abeaf75f7b9a53be8) |
| **Road · North entrance**<br>`1-N-in-7`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c34d9de362ebd902abcf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8bd49aa53c16ade8325d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-950f2e1665a51caa1bc4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c7624f68b679f3d4cb55) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9ae34d8c3cfbb268f938) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-77ae9cee788b8980a1bc)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-77ae9cee788b8980a1bc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-549b58b475c7fc9e023d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4be84acdb23c7b536a6f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1f795fb78b1987b3f3af) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b82dcf2427dff7644dae) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9666bc0bae1f36cb0e80) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-32446335bf7839f28bda) |
| **Road · North entrance**<br>`1-N-in-8`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-02ac829809f960238cf0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-01b579da253305b19e0c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a7ae964cb5f097b0812d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-402a6d486911424ecff0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f74c346d81fc74312bcc) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2a1c693bb5910b7b6db5) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-4374b03403ce80fb5790)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-4374b03403ce80fb5790) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-47ad65daca01e52896fe) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2cf7fe728534755cbe3c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a5044c756ea880774b1b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-58cbef086864c3548663) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bbc03c0ac8bc78dfe9eb) |
| **Road · South entrance**<br>`1-S-in-13`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3930800e560ea2ae9448) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c64401220c98e0675679) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b34baedf92cc8a1e1850) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b2dff0b763d01837833a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b2dff0b763d01837833a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9b7ef4766b05198e585d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-691d60f8926d3ba78321) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cd73f23d230c6d7b6d2e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e3670945219eb58c2744) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-934fafda1656f4b4a6d3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-64bc1d8f68a09422f3bb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8fc31b5de321a5aa04ab) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1cc555d9a8377f1c27a7) |
| **Road · South entrance**<br>`1-S-in-14`<br>Variant: avenue-ground | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-53d0a09cbcc2d67064c9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-19788729d67c181c3eee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-66f84b66dab33700563f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1f7e2a301c6c6e9a6ece) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b386e673161cc3353f56)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b386e673161cc3353f56) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-253fb897fc7cd583b4a2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a162d9c91d48270a99f8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c6dd03181040b99825ec) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1506e9dde5b3835e3cd8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fd55e64b4596f0e11b9e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8de86385cc533f91762a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-440aafef1624959b0ebf) |
| **Road · South entrance**<br>`1-S-in-16`<br>Variant: access-ramp | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-912375e61e38abf38ed2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ed68e7d3991671bd0b16) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1ad75c690890a8b7ea45) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-35dbba093bfcc28b4bb9) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a6dcd80efc365281efee) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5d1fef44b44298ed9290) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7977bb570c4fdcd68291) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-51f420cc231dc1ed093d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-43dcbae61b76f0113fe1) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-993d0ba38b14cb3cbcf1)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-993d0ba38b14cb3cbcf1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e1624d872f8476b9b164) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7d3e1937f5db675134bb) |
| **Road · North entrance**<br>`1-N-in-17`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8eebd93b1df445815963) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-d128aebf7134c1a61f8a)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-d128aebf7134c1a61f8a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-1ae752f1829d7b2c3cfd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a36f03493d9f145dde59) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-337dc10fc669a8cc9c17) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-29bbd7ea897f4c3b4e1c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-620b0d335de85887d6df) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-8f61501a127ecfa4cc66)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-8f61501a127ecfa4cc66) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d6d8f130bf846a6bbbe8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ddfb84b0c35023ddceba) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c7600c8691527eb57e08) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a8fd4549d8d7a077d995) |
| **Road · North entrance**<br>`1-N-in-19`<br>Variant: dd-rhw-l1 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-90deaa158fa729894ee8)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-90deaa158fa729894ee8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b355d1a40002ffce4c85) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-10250c9895b993ed9c7f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-859b8f8153ec950a5137) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b626c6b0ecbacee7cf25) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d31a54bab84f0c30a31a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0029b8d1b59b2a47e23f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ee513a2f7f6b3c359fd8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fa94466884e56559c5c2) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d36b5be1429fedb7aa14) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3cbf07738791637e195e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-5439a3d045ca09d8ef69) |
| **Pedestrian · North entrance**<br>`2-N-in-1`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-068afd5d04630eb0a817) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9e73a7e3bccf3ac5cdcd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8edc1cc5e26482252bbb) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6a7fa7146c5208c3ea03) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-040fd6cb410278cc1b53) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d40b779e968ea04bc5fd) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0ff19418709d2493ad67) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d3f4b7c1ce6206d5ab6e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c0e8a0e5a2e69361d80c) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0281c52aa8b78b591392) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-3f9b449d6326a1c07276) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-4d3847a380323c3058a3)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-4d3847a380323c3058a3) |
| **Pedestrian · South entrance**<br>`2-S-in-4`<br>Variant: avenue-sidewalk | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-96add150c70ca306c29e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-652c9b75e15491beff5b) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b8c0e1cf53c069ffa9c5) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-86cbb6b44d0444dd8773) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-da6f0ab98782dd08bd23) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e3e51e71e3bddf30643d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6496daebe51f6507b37e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-95791c5ce0194005c2b4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e3c7d837decdd00dd8df) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0e8600956565bd9c10bf) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-74bff4e9f001a185c0cf)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-74bff4e9f001a185c0cf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-1c233e8adbd824473999)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d1ff89f4be378cb28e6c) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 9 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.

#### Boundary A: `boundary-01`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,9]` / West |
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
| `member-1-w-out-1` / `1-W-out-1` | `lower-lane-02` / `cut-1-w-out-1` / car | Outgoing | `[-8,-147.2,7.5]` | Not declared | 225° | 0 |
| `member-1-w-out-3` / `1-W-out-3` | `lower-lane-01` / `cut-1-w-out-3` / car | Outgoing | `[-8,-140.8,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,9]` / West |
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
| `member-1-w-in-2` / `1-W-in-2` | `upper-lane-01` / `cut-1-w-in-2` / car | Incoming | `[-8,-147.2,15]` | Not declared | 225° | 0 |
| `member-1-w-in-4` / `1-W-in-4` | `upper-lane-02` / `cut-1-w-in-4` / car | Incoming | `[-8,-140.8,15]` | Not declared | 225° | 0 |

#### Boundary B: `boundary-02`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.74513 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,6]` / North |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.74513 m); no nominal level |
| Outward heading | 11.6638° |
| Slope at joining edge | -22.6757% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-n-in-5` / `1-N-in-5` | `lower-ramp-01` / `cut-1-n-in-5` / car | Incoming | `[26.2074,-88,6.74513]` | Not declared | 11.6638° | -22.6757 |

#### Boundary C: `boundary-03`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (12.2582 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[2,8]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (12.2582 m); no nominal level |
| Outward heading | 68.0206° |
| Slope at joining edge | -29.6095% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-e-out-6` / `1-E-out-6` | `upper-ramp-01` / `cut-1-e-out-6` / car | Outgoing | `[40,-120.143,12.2582]` | Not declared | 68.0206° | -29.6095 |

#### Boundary D: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[3,4]` / North |
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
| `member-1-n-in-7` / `1-N-in-7` | `avenue-lane-01` / `cut-1-n-in-7` / car | Incoming | `[44.8,-56,0]` | Not declared | 315° | 0 |
| `member-1-n-in-8` / `1-N-in-8` | `avenue-lane-02` / `cut-1-n-in-8` / car | Incoming | `[51.2,-56,0]` | Not declared | 315° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[3,4]` / North |
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
| `member-2-n-in-1` / `2-N-in-1` | `avenue-walkway-01` / `cut-2-n-in-1` / pedestrian | Incoming | `[40.7,-56,0]` | Not declared | 315° | 0 |

#### Boundary E: `boundary-05`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[4,3]` / West |
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
| `member-1-w-out-10` / `1-W-out-10` | `avenue-lane-04` / `cut-1-w-out-10` / car | Outgoing | `[56,-44.8,0]` | Not declared | 315° | 0 |
| `member-1-w-out-9` / `1-W-out-9` | `avenue-lane-03` / `cut-1-w-out-9` / car | Outgoing | `[56,-51.2,0]` | Not declared | 315° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-05-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[4,3]` / West |
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
| `member-2-w-out-2` / `2-W-out-2` | `avenue-walkway-02` / `cut-2-w-out-2` / pedestrian | Outgoing | `[56,-40.7,0]` | Not declared | 315° | 0 |

#### Boundary F: `boundary-06`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[4,5]` / East |
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
| `member-1-e-out-11` / `1-E-out-11` | `avenue-lane-01` / `cut-1-e-out-11` / car | Outgoing | `[72,-83.2,0]` | Not declared | 135° | 0 |
| `member-1-e-out-12` / `1-E-out-12` | `avenue-lane-02` / `cut-1-e-out-12` / car | Outgoing | `[72,-76.8,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-06-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[4,5]` / East |
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
| `member-2-e-out-3` / `2-E-out-3` | `avenue-walkway-01` / `cut-2-e-out-3` / pedestrian | Outgoing | `[72,-87.3,0]` | Not declared | 135° | 0 |

#### Boundary G: `boundary-07`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-07-avenue-mainline-01` / `avenue-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[5,4]` / South |
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
| `member-1-s-in-13` / `1-S-in-13` | `avenue-lane-03` / `cut-1-s-in-13` / car | Incoming | `[76.8,-72,0]` | Not declared | 135° | 0 |
| `member-1-s-in-14` / `1-S-in-14` | `avenue-lane-04` / `cut-1-s-in-14` / car | Incoming | `[83.2,-72,0]` | Not declared | 135° | 0 |

##### Service group 2 / 2: PEDESTRIAN — Custom (0 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-07-avenue-walkways-02` / `avenue-walkways` |
| Network / game class / role | pedestrian / Engine class (2); primary |
| Source cell / edge | `[5,4]` / South |
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
| `member-2-s-in-4` / `2-S-in-4` | `avenue-walkway-02` / `cut-2-s-in-4` / pedestrian | Incoming | `[87.3,-72,0]` | Not declared | 135° | 0 |

#### Boundary H: `boundary-08`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.74513 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-08-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[6,2]` / West |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.74513 m); no nominal level |
| Outward heading | 258.336° |
| Slope at joining edge | -22.6757% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-w-out-15` / `1-W-out-15` | `lower-ramp-02` / `cut-1-w-out-15` / car | Outgoing | `[88,-26.2074,6.74513]` | Not declared | 258.336° | -22.6757 |

#### Boundary I: `boundary-09`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (12.2582 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-09-upper-mainline-01` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[8,2]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (12.2582 m); no nominal level |
| Outward heading | 201.979° |
| Slope at joining edge | -29.6095% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-1-s-in-16` / `1-S-in-16` | `upper-ramp-02` / `cut-1-s-in-16` / car | Incoming | `[120.143,-40,12.2582]` | Not declared | 201.979° | -29.6095 |

#### Boundary J: `boundary-10`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-10-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[9,0]` / North |
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
| `member-1-n-in-17` / `1-N-in-17` | `lower-lane-01` / `cut-1-n-in-17` / car | Incoming | `[140.8,8,7.5]` | Not declared | 45° | 0 |
| `member-1-n-in-19` / `1-N-in-19` | `lower-lane-02` / `cut-1-n-in-19` / car | Incoming | `[147.2,8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-10-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[9,0]` / North |
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
| `member-1-n-out-18` / `1-N-out-18` | `upper-lane-02` / `cut-1-n-out-18` / car | Outgoing | `[140.8,8,15]` | Not declared | 45° | 0 |
| `member-1-n-out-20` / `1-N-out-20` | `upper-lane-01` / `cut-1-n-out-20` / car | Outgoing | `[147.2,8,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
