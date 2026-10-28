---
title: "Straight-stem HSR trumpet"
summary: "Show the modular HSR trumpet, its reusable pieces and placements, and the status of each directed external connection."
audience: "Players and assembly authors"
document_type: "guide"
---

# Straight-stem HSR trumpet

[1. Views](#1-views) · [2. Pieces](#2-pieces) · [3. Placements](#3-placements) · [4. Connection matrix](#4-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

This **modular blueprint** is an arrangement built from reusable component types. A **placement** is one copy of a component in the city. The trumpet uses **26 placements of 13 types**, within a **20 × 23 tile** rectangle, with **105 occupied tiles** and **74 support positions**.

Open **Transportation → Rail**, select the **SCP | ASSEMBLY | HSR Trumpet** button, and press **Tab** to cycle forward through its components or **Shift+Tab** to cycle backward. Each click places the selected component. Use the placement table to complete the arrangement. [Build and install the assembly menu](../../../../docs/BUILD_AND_INSTALL.md#prepare-the-assembly-menu) before following these menu instructions.

**HSR** means elevated High Speed Rail. **L2** has its train path at 15.5 m, and **L4** at 30.5 m; the northern loop also uses a 23 m intermediate connection. Current software and game-check results appear in the connection matrix. The reported [demolition defect](TESTING.md#known-issues) remains open.

## 1. Views

Every image is titled **Assembly - Straight-stem HSR trumpet** and uses the same city grid. Its second row identifies its purpose and camera direction. The first two are **Clean view** images without part names. The next three are **Component guide** images with exact component names and placement labels in the side legend. The final **Construction view** shows tile ownership: adjacent placements have clearly different colours and thick boundaries, even when they reuse the same button. The [render report](evidence/render.json) identifies the actual saved models and image hashes.

The current pictures show the four-tile P07 and separate P26, with all 26 placement labels and the revised tile ownership. Their actual-model evidence is separate from human picture approval and game-test results.

![clean top view on the fixed X/Y city grid](previews/overview-top.png)

![clean southeast view on the same X/Y grid](previews/preview.png)

![named top view with every exact component name](previews/named-top.png)

![named southeast view](previews/named-southeast.png)

![named northwest view](previews/named-northwest.png)

![tile ownership and placement positions with distinct adjacent colours and thick boundaries](previews/tile-ownership.png)

## 2. Pieces

Use **Tab** or **Shift+Tab** on the assembly button to select the component named in the table. Repeated placements reuse that component in the same cycle. Click a thumbnail to open its full standalone picture; each picture shows the component at 0°.

| Standalone angled picture | Component name and permanent piece ID | Placements | Quantity |
| --- | --- | --- | ---: |
| [![HSR L2 Short Mainline Diverge Core: canonical angled view](../../00_pieces/hsr-component-l2-short-mainline-diverge-core/previews/preview-thumb.png)](../../00_pieces/hsr-component-l2-short-mainline-diverge-core/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-short-mainline-diverge-core/previews/preview-top.png) | **[HSR L2 Short Mainline Diverge Core](../../00_pieces/hsr-component-l2-short-mainline-diverge-core/README.md)**<br>`hsr-component-l2-short-mainline-diverge-core` | P01, P08 | 2 |
| [![HSR L2 Two-Track Straight: canonical angled view](../../00_pieces/hsr-component-lower-paired-straight/previews/preview-thumb.png)](../../00_pieces/hsr-component-lower-paired-straight/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-lower-paired-straight/previews/preview-top.png) | **[HSR L2 Two-Track Straight](../../00_pieces/hsr-component-lower-paired-straight/README.md)**<br>`hsr-component-lower-paired-straight` | P02, P09, P14, P15, P22, P23, P26 | 7 |
| [![HSR L2 Shortened One-Way Departure Curve: canonical angled view](../../00_pieces/hsr-component-l2-shortened-departure-curve/previews/preview-thumb.png)](../../00_pieces/hsr-component-l2-shortened-departure-curve/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-shortened-departure-curve/previews/preview-top.png) | **[HSR L2 Shortened One-Way Departure Curve](../../00_pieces/hsr-component-l2-shortened-departure-curve/README.md)**<br>`hsr-component-l2-shortened-departure-curve` | P03 | 1 |
| [![HSR Modular Symmetric Split and Return: canonical angled view](../../00_pieces/hsr-component-modular-south-junction/previews/preview-thumb.png)](../../00_pieces/hsr-component-modular-south-junction/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-modular-south-junction/previews/preview-top.png) | **[HSR Modular Symmetric Split and Return](../../00_pieces/hsr-component-modular-south-junction/README.md)**<br>`hsr-component-modular-south-junction` | P04 | 1 |
| [![HSR Modular Two-Track L2 to L4 Climb: canonical angled view](../../00_pieces/hsr-component-modular-paired-climb/previews/preview-thumb.png)](../../00_pieces/hsr-component-modular-paired-climb/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-modular-paired-climb/previews/preview-top.png) | **[HSR Modular Two-Track L2 to L4 Climb](../../00_pieces/hsr-component-modular-paired-climb/README.md)**<br>`hsr-component-modular-paired-climb` | P05 | 1 |
| [![HSR L2 Compact Paired Fan Join: canonical angled view](../../00_pieces/hsr-component-l2-paired-fan-compact-join/previews/preview-thumb.png)](../../00_pieces/hsr-component-l2-paired-fan-compact-join/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-paired-fan-compact-join/previews/preview-top.png) | **[HSR L2 Compact Paired Fan Join](../../00_pieces/hsr-component-l2-paired-fan-compact-join/README.md)**<br>`hsr-component-l2-paired-fan-compact-join` | P06 | 1 |
| [![HSR L2 Short Opposed Merge Core: canonical angled view](../../00_pieces/hsr-component-l2-short-opposed-merge-core/previews/preview-thumb.png)](../../00_pieces/hsr-component-l2-short-opposed-merge-core/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-short-opposed-merge-core/previews/preview-top.png) | **[HSR L2 Short Opposed Merge Core](../../00_pieces/hsr-component-l2-short-opposed-merge-core/README.md)**<br>`hsr-component-l2-short-opposed-merge-core` | P07 | 1 |
| [![HSR L2 Shortened One-Way Return Curve: canonical angled view](../../00_pieces/hsr-component-l2-shortened-return-curve/previews/preview-thumb.png)](../../00_pieces/hsr-component-l2-shortened-return-curve/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-shortened-return-curve/previews/preview-top.png) | **[HSR L2 Shortened One-Way Return Curve](../../00_pieces/hsr-component-l2-shortened-return-curve/README.md)**<br>`hsr-component-l2-shortened-return-curve` | P10 | 1 |
| [![HSR Modular One-Tile Two-Level Crossing: canonical angled view](../../00_pieces/hsr-component-modular-crossing-core/previews/preview-thumb.png)](../../00_pieces/hsr-component-modular-crossing-core/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-modular-crossing-core/previews/preview-top.png) | **[HSR Modular One-Tile Two-Level Crossing](../../00_pieces/hsr-component-modular-crossing-core/README.md)**<br>`hsr-component-modular-crossing-core` | P11 | 1 |
| [![HSR L4 Two-Track Straight: canonical angled view](../../00_pieces/hsr-component-upper-paired-straight/previews/preview-thumb.png)](../../00_pieces/hsr-component-upper-paired-straight/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-upper-paired-straight/previews/preview-top.png) | **[HSR L4 Two-Track Straight](../../00_pieces/hsr-component-upper-paired-straight/README.md)**<br>`hsr-component-upper-paired-straight` | P12, P13, P16, P17, P18, P19 | 6 |
| [![HSR Tight Two-Track Corner 30.5 to 23 Metres: canonical angled view](../../00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/previews/preview-thumb.png)](../../00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/previews/preview-top.png) | **[HSR Tight Two-Track Corner 30.5 to 23 Metres](../../00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/README.md)**<br>`hsr-component-tight-paired-curve90-l4-to-mid` | P20 | 1 |
| [![HSR Tight Two-Track Corner 23 to 15.5 Metres: canonical angled view](../../00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/previews/preview-thumb.png)](../../00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/previews/preview-top.png) | **[HSR Tight Two-Track Corner 23 to 15.5 Metres](../../00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/README.md)**<br>`hsr-component-tight-paired-curve90-mid-to-l2` | P21 | 1 |
| [![One-Way HSR L2 Eight-Metre Straight: canonical angled view](../../00_pieces/hsr-component-lower-oneway-straight/previews/preview-thumb.png)](../../00_pieces/hsr-component-lower-oneway-straight/previews/preview.png)<br>[Top view](../../00_pieces/hsr-component-lower-oneway-straight/previews/preview-top.png) | **[One-Way HSR L2 Eight-Metre Straight](../../00_pieces/hsr-component-lower-oneway-straight/README.md)**<br>`hsr-component-lower-oneway-straight` | P24, P25 | 2 |

The [standalone-picture report](evidence/piece-previews.json) records the current component images, their saved-model sources, and all 26 placements. Each canonical picture shows 0°; use the rotation in the placement table when building. Quantities count placements, so the same component can appear several times in the arrangement.

## 3. Placements

Use each position and rotation together; standalone component pictures show 0°. The [layout reference in TESTING.md](TESTING.md#layout-reference) defines the grid and rotation convention. Follow the [numbered placement sequence](TESTING.md#placement-sequence) to select and place the components in order. Occupied tiles count only the tiles belonging to that placement.

| Placement | Exact descriptive menu name | Reference position | Rotation | Occupied tiles |
| --- | --- | --- | --- | ---: |
| P01 | HSR L2 Short Mainline Diverge Core | (X1, Y13) | 0° | 4 |
| P02 | HSR L2 Two-Track Straight | (X5, Y13) | 270° | 1 |
| P03 | HSR L2 Shortened One-Way Departure Curve | (X2, Y12) | 0° | 12 |
| P04 | HSR Modular Symmetric Split and Return | (X6, Y5) | 0° | 14 |
| P05 | HSR Modular Two-Track L2 to L4 Climb | (X7, Y11) | 0° | 8 |
| P06 | HSR L2 Compact Paired Fan Join | (X11, Y18) | 0° | 11 |
| P07 | HSR L2 Short Opposed Merge Core | (X10, Y13) | 0° | 4 |
| P08 | HSR L2 Short Mainline Diverge Core | (X18, Y13) | 180° | 4 |
| P09 | HSR L2 Two-Track Straight | (X19, Y13) | 270° | 1 |
| P10 | HSR L2 Shortened One-Way Return Curve | (X8, Y12) | 0° | 12 |
| P11 | HSR Modular One-Tile Two-Level Crossing | (X7, Y13) | 0° | 1 |
| P12 | HSR L4 Two-Track Straight | (X7, Y14) | 0° | 1 |
| P13 | HSR L4 Two-Track Straight | (X7, Y12) | 0° | 1 |
| P14 | HSR L2 Two-Track Straight | (X6, Y13) | 270° | 1 |
| P15 | HSR L2 Two-Track Straight | (X8, Y13) | 270° | 1 |
| P16 | HSR L4 Two-Track Straight | (X7, Y15) | 0° | 1 |
| P17 | HSR L4 Two-Track Straight | (X7, Y16) | 0° | 1 |
| P18 | HSR L4 Two-Track Straight | (X7, Y17) | 0° | 1 |
| P19 | HSR L4 Two-Track Straight | (X7, Y18) | 0° | 1 |
| P20 | HSR Tight Two-Track Corner 30.5 to 23 Metres | (X7, Y22) | 0° | 10 |
| P21 | HSR Tight Two-Track Corner 23 to 15.5 Metres | (X14, Y22) | 270° | 10 |
| P22 | HSR L2 Two-Track Straight | (X0, Y13) | 270° | 1 |
| P23 | HSR L2 Two-Track Straight | (X14, Y13) | 270° | 1 |
| P24 | One-Way HSR L2 Eight-Metre Straight | (X6, Y6) | 180° | 1 |
| P25 | One-Way HSR L2 Eight-Metre Straight | (X8, Y6) | 0° | 1 |
| P26 | HSR L2 Two-Track Straight | (X9, Y13) | 270° | 1 |

The [machine-readable plan](assembly.json) is authoritative for identities and model translations. P01's reference is **(X1, Y13)** because P22 owns the western approach tile at **(X0, Y13)**. P26 similarly owns the ordinary tile at **(X9, Y13)**, and P07's four-tile core starts at **(X10, Y13)**. Every occupied tile has exactly one owner. P01 and P08 reuse the same Short Mainline Diverge Core: P01 is at 0°, and P08 is at 180°. P08 replaces the earlier separate eastern diverge and its western straight; the fan and opposed merge have matching revised branch angles. The retained component types keep their permanent game identifiers.

P06 uses the approved wider Compact Paired Fan Join: its paired structure stays 15 m wide through the approach before widening into the fork. Its [fan width comparison](../../00_pieces/hsr-component-l2-paired-fan-compact-join/evidence/fan-width-audit.json) records the shoulders-and-walls change and preservation of the fan's routes, radii, joining cuts, and support positions. The subsequent [P07/P26 extraction audit](evidence/merge-west-tail-extraction.json) verifies the current four-tile core, separate straight, and narrowly bounded seam adjustment. Detailed scope and historical comparisons remain in [TESTING](TESTING.md#western-merge-approach-extraction).

<!-- BEGIN ASSEMBLY CONNECTION MATRIX -->

## 4. Connection matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-4b8e61d1c512b7c578e8) — the complete assembly’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [TESTING](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **HSR · West exit**<br>`W.out` | **HSR · South exit**<br>`S.out` | **HSR · East exit**<br>`E.out` |
| --- | --- | --- | --- |
| **HSR · West entrance**<br>`W.in` | **Forbidden**<br>**Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-92b725456842f93c47ca) | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-aea09525a3e21f949d2b)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-aea09525a3e21f949d2b) | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-87f3cb5204e2970d80c1)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-87f3cb5204e2970d80c1) |
| **HSR · South entrance**<br>`S.in` | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-2572758d9ad9c64a40fd)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-2572758d9ad9c64a40fd) | **Forbidden**<br>**Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-dfbdc4123044e5fb53fe) | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-336582ad6132a64a36f8)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-336582ad6132a64a36f8) |
| **HSR · East entrance**<br>`E.in` | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-76bf51a0e3b87a77ead7)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-76bf51a0e3b87a77ead7) | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-8b08022118fd9f445d85)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-8b08022118fd9f445d85) | **Forbidden**<br>**Saved PATH:** [✅](TESTING.md#case-software_connectivity-fe740c153144a3695751)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9f7a461fa713c7413977) |

Source: [connections.json](connections.json).

<!-- END ASSEMBLY CONNECTION MATRIX -->
