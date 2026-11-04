---
title: "DD RHW-4 — Compact Y-Junction — Diagonal Stem — Reversed Traffic"
summary: "Build the reversed-traffic counterpart with driver-left yellow markings using three separate components."
audience: "players"
document_type: "guide"
---

# DD RHW-4 — Compact Y-Junction — Diagonal Stem — Reversed Traffic

<!-- ASSEMBLY README LAYOUT: 1 -->

[1. Views](#1-views) · [2. Pieces](#2-pieces) · [3. Placements](#3-placements) · [4. Connection matrix](#4-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

This assembly connects three double-decker RealHighway arms: **A** extends southwest, **B** extends northwest, and **C** extends east. Each native DD RHW-4 end has two lanes in one direction at 15 m and two lanes in the opposite direction at 7.5 m. Each incoming lane serves one of the other arms, giving six one-lane journeys and no U-turns. Every journey runs in the opposite direction to the original Y at the same physical arm positions, so yellow moves to the opposite physical edge while staying on the driver's left. On the upper deck, A is outgoing, and B and C are incoming; the lower directions are opposite.

The junction uses **three reusable component types, three placements, and 21 occupied city tiles within a 6 × 7-tile rectangle**, or 96 × 112 m. A city tile is 16 × 16 m. The rectangle includes unowned holes; it is not a solid 42-tile component. Keep the native approaches and their continuation space clear as described below.

The four A↔B and A↔C journeys remain level. Both B↔C journeys descend on separate ramps from the 15 m upper deck to the 7.5 m lower deck. A **grade** is height gained divided by horizontal distance: a 20% grade rises 2 m over 10 m horizontally. The source peak grades are approximately 25.761% for B→C and 26.572% for C→B, below this library's experimental 30% ceiling. These are compact game ramps, and their driving behavior remains subject to the [game checks](TESTING.md#4-game-checks).

The graded links normally have a 6 m-wide deck, including their barriers. Short transitions narrow the inner shoulder to a 5.25 m deck, leaving 3.59375 m of unobstructed asphalt so the neighbouring decks clear one another. Each route still carries one lane.

## 1. Views

The six pictures below show the actual compiled pavement, decks, barriers, and supports at the registered component positions. They are software renders, rather than game screenshots. Every picture uses one fixed city grid: X increases eastward, Y increases northward, and (X0, Y0) is the southwest tile centre of the construction rectangle. A north-up view places A at the lower left, B at the upper left, and C at the right.

![Clean north-up view of the compact DD RHW Y-junction](previews/overview-top.png)

![Clean southeast view showing the two decks and the separate graded links](previews/preview.png)

![Named north-up view identifying all three component placements](previews/named-top.png)

![Named southeast view identifying the three reusable components](previews/named-southeast.png)

![Named northwest view showing the opposite sides of the decks](previews/named-northwest.png)

The construction view places ownership colours over the actual top-view model at 30% opacity. Each colour identifies one component's occupied tiles. Opaque outlines distinguish the tile boundaries from the actual model projections, and reference diamonds show the placement references. A reference can be an unowned tile inside a component's surrounding rectangle; match the complete occupied shape, rather than assuming the reference must contain road.

![Construction view with 30% ownership colours, actual model outlines, and placement references](previews/tile-ownership.png)

## 2. Pieces

A **type** is a reusable component design. A **placement** is one copy placed in the city. This assembly uses each of its three types once. Each click places only the selected component. Click an angled thumbnail or **Top view** to inspect that component separately in its unrotated orientation.

| Standalone angled picture | Exact component name and permanent piece ID | Placement | Quantity | Occupied tiles |
| --- | --- | --- | ---: | ---: |
| [![Diagonal Two-Branch Stem](../../00_pieces/ddrhw-y-reversed-diagonal-stem-split/previews/preview-thumb.png)](../../00_pieces/ddrhw-y-reversed-diagonal-stem-split/previews/preview.png)<br>[Top view](../../00_pieces/ddrhw-y-reversed-diagonal-stem-split/previews/preview-top.png) | **[DD RHW-4 — Diagonal Two-Branch Stem — L1/L2 — Reversed Traffic](../../00_pieces/ddrhw-y-reversed-diagonal-stem-split/README.md)**<br>`ddrhw-y-reversed-diagonal-stem-split` | P01 | 1 | 8 |
| [![Diagonal Branch and Paired Graded Links](../../00_pieces/ddrhw-y-reversed-diagonal-branch/previews/preview-thumb.png)](../../00_pieces/ddrhw-y-reversed-diagonal-branch/previews/preview.png)<br>[Top view](../../00_pieces/ddrhw-y-reversed-diagonal-branch/previews/preview-top.png) | **[DD RHW-4 — Diagonal Branch and Paired Graded Links — L1/L2 — Reversed Traffic](../../00_pieces/ddrhw-y-reversed-diagonal-branch/README.md)**<br>`ddrhw-y-reversed-diagonal-branch` | P02 | 1 | 8 |
| [![Orthogonal Y Connection Core](../../00_pieces/ddrhw-y-reversed-orthogonal-core/previews/preview-thumb.png)](../../00_pieces/ddrhw-y-reversed-orthogonal-core/previews/preview.png)<br>[Top view](../../00_pieces/ddrhw-y-reversed-orthogonal-core/previews/preview-top.png) | **[DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Reversed Traffic](../../00_pieces/ddrhw-y-reversed-orthogonal-core/README.md)**<br>`ddrhw-y-reversed-orthogonal-core` | P03 | 1 | 5 |

P01 contains the southwest native connection and the south band of the flat split and merge. P02 contains the northwest native connection and the north band of both graded links. P03 contains the east native connection and the coordinated centre band. Each component owns every surface and saved route fragment within its occupied tiles, including fragments belonging to several journeys. This prevents one placement from replacing another's lanes on the same city tile.

Standalone pictures include cut road ends, partial beams, and piers whose remaining geometry belongs to an adjacent component. The three registered placements complete those shared structures.

These are functional multi-tile modules, rather than independent full-length ramps. Reuse requires matching every exposed lane boundary, height, direction, and physical cross-section. The generated connector overviews in the individual manuals describe their intrinsic boundaries; they do not establish compatibility with arbitrary existing pieces. Native extensions are supported only at the three reviewed exterior sockets.

## 3. Placements

The table and construction view describe the unrotated layout. A **reference tile** is the component's local column 0, row 0 position. Rows in the source run southward, while the displayed Y coordinate runs northward. The reference for P02 is unowned by the custom component; its first custom-owned tile lies immediately east of it. That reference can contain the ordinary native B approach after extension or in a prebuilt control. P01 and P03 have occupied reference tiles. These are measured geometric references; the actual mouse-cursor anchor still requires a game observation. Match the entire occupied shape before clicking.

1. Prepare a flat, clear area at least 6 tiles wide and 7 tiles tall, plus room southwest, northwest, and east for ordinary native DD RHW approaches. Use the southwest tile centre as (X0, Y0).
2. Build and deliberately install a verified experimental selection through the [build and installation guide](../../../../docs/BUILD_AND_INSTALL.md). Building the source does not install it. Close SimCity 4 before replacing a plugin, restart it afterward, and use fresh placements for this new controller, model, and PATH revision.
3. Open **Transportation → Highways → SCP → Assemblies**, and select **SCP | ASSEMBLY | DD RHW-4 — Compact Y-Junction — Diagonal Stem — Reversed Traffic**. This is one menu button containing three components.
4. Press **Tab** to move forward through the components or **Shift+Tab** to move backward. Read the component's full name in its tooltip. Press **Home** or **End** to rotate it until its orientation matches the north-up construction view. Use 0° for all three rows below.
5. Select the **Diagonal Two-Branch Stem**, put its reference at (X0, Y2), check its eight occupied cells against P01, and click once.
6. Select the **Diagonal Branch and Paired Graded Links**, put its unowned reference at (X0, Y6), check its eight occupied cells against P02, and click once. Do not shift it east merely because the reference cell is unowned.
7. Select the **Orthogonal Y Connection Core**, put its reference at (X1, Y3), check its five occupied cells against P03, and click once.
8. Inspect the three native approach sockets listed below. Each new component requests an optional ordinary NAM DD RHW tile outside its owned cells. Confirm that the expected native tile appears and that no temporary Road or construction-marker tile remains. Missing automatic placement is an unverified game outcome, not a reason to place another custom component over the socket.
9. Cancel component placement with **Esc**. Open **Transportation → Highways**, select **RealHighway (RHW-2)**, and drag outward from each native socket in its listed direction for at least three native tiles. Keep the diagonal two-cell staircase clear, and do not drag through the 21 custom-owned tiles. For a separate prebuilt-approach control, select **Transportation → Highways → RealHighway (RHW) Starter Pieces**, press **Tab** until the tooltip reads **Double-Decker RHW-4 Starter Piece (Upper Deck: Level 2, Lower Deck: Level 1)**, place it in the matching orientation, and extend its approach with **RealHighway (RHW-2)**. The similarly named rail-based DDRHW starter is a different network. Record outward dragging, inward connection, and placement beside prebuilt native approaches separately.

| Placement | Reference tile | Rotation | Bounding rectangle | Owned tiles |
| --- | --- | ---: | --- | ---: |
| P01 — Diagonal Two-Branch Stem | (X0, Y2) | 0° | 5 × 3 tiles | 8 |
| P02 — Diagonal Branch and Paired Graded Links | (X0, Y6), unowned reference | 0° | 5 × 3 tiles | 8 |
| P03 — Orthogonal Y Connection Core | (X1, Y3) | 0° | 5 × 1 tiles | 5 |

| Arm | Optional native socket | Continue outward | Incoming / outgoing deck |
| --- | --- | --- | --- |
| A — southwest stem | (X0, Y1) | Southwest, keeping the diagonal two-cell native pattern clear | Lower incoming / upper outgoing |
| B — northwest branch | (X0, Y5) | Northwest, keeping the diagonal two-cell native pattern clear | Upper incoming / lower outgoing |
| C — east branch | (X6, Y3) | East along Y3 | Upper incoming / lower outgoing |

The diagonal approaches need their staggered neighbouring native cells as they continue away from the junction; the one optional socket is not the whole approach. The native masks are protected from custom ownership. Both diagonal sockets are unowned holes inside the overall construction rectangle. C at (X6, Y3) is one tile east of that rectangle, immediately beyond P03's last owned tile. Leave room beyond the rectangle for connecting roads. Use the [native connection test](TESTING.md#4-game-checks) to establish actual construction behavior.

Only the first measured diagonal alignment is supplied. The four proper rotations are software-checked; reflected geometry and another native grid phase are not delivered variants. All six journeys and the prohibition on U-turns are defined below.

Every journey carries one lane. Use this traffic table to identify the required entering and leaving decks when connecting the native approaches. The four level journeys keep their deck height. Both branch-to-branch journeys descend on separate routes; they do not cross at the same height. A negative grade means height decreases in the direction of travel.

| Journey | Entering arm and deck | Leaving arm and deck | Height profile |
| --- | --- | --- | --- |
| A→B | Southwest, L1 | Northwest, L1 | Level at 7.5 m |
| B→A | Northwest, L2 | Southwest, L2 | Level at 15 m |
| A→C | Southwest, L1 | East, L1 | Level at 7.5 m |
| C→A | East, L2 | Southwest, L2 | Level at 15 m |
| B→C | Northwest, L2 | East, L1 | Descends 15→7.5 m; peak absolute grade approximately 25.761% |
| C→B | East, L2 | Northwest, L1 | Descends 15→7.5 m; peak absolute grade approximately 26.572% |

The generated matrix checks the saved assembled route graph. Route Query, moving traffic, native dragging, and appearance remain separate [game checks](TESTING.md#4-game-checks). The original assembly remains a separate selectable three-component cycle.

<!-- BEGIN ASSEMBLY CONNECTION MATRIX -->

## 4. Connection matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [✅](TESTING.md#case-in_game_render-1eddce0b9ae85ad884c7) — the complete assembly’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [TESTING](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · external-2**<br>`external-2`<br>Variant: dd-rhw-l2 | **Road · external-4**<br>`external-4`<br>Variant: dd-rhw-l2 | **Road · external-5**<br>`external-5`<br>Variant: dd-rhw-l1 | **Road · external-7**<br>`external-7`<br>Variant: dd-rhw-l1 | **Road · external-9**<br>`external-9`<br>Variant: dd-rhw-l1 | **Road · external-11**<br>`external-11`<br>Variant: dd-rhw-l1 |
| --- | --- | --- | --- | --- | --- | --- |
| **Road · external-1**<br>`external-1`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2f83c4e48ededb78f622) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-db97304c4ca44135b89e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e78a608055f9740a9eb3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ef9418f7cf3504e8495d) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>**Route Query:** [✅](TESTING.md#case-in_game_route_query-d8a66df811018497e13a)<br>**Visible travel:** [✅](TESTING.md#case-in_game_visible_travel-d8a66df811018497e13a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8a9e38685a53189cec04) |
| **Road · external-3**<br>`external-3`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ab9563f3678c208c59c0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7c78354135f7f82c6ff2) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>**Route Query:** [✅](TESTING.md#case-in_game_route_query-1a2cdc3a3552f2e342c8)<br>**Visible travel:** [✅](TESTING.md#case-in_game_visible_travel-1a2cdc3a3552f2e342c8) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f05ee6a992d161f6221a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-775461730fb0320b7551) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-21f0af52fa38ac599df5) |
| **Road · external-6**<br>`external-6`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-354f50d5fea62fff400a) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>**Route Query:** [✅](TESTING.md#case-in_game_route_query-2a2a2c6c876befa9fdc4)<br>**Visible travel:** [✅](TESTING.md#case-in_game_visible_travel-2a2a2c6c876befa9fdc4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-04db0894dd5d861747e0) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-19ced577cedd85227b3a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-badd8cd070c2dd575a25) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-feb29abc0175d7339a97) |
| **Road · external-8**<br>`external-8`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-f56e7ad8bc073217ae55) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ae056abfbc2304ecf62e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-feaa3d0cb98512f3ecf3) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-38bda43d0ca7c349dc2f) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8e9d08b139bb4ecd061c) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>**Route Query:** [✅](TESTING.md#case-in_game_route_query-5ace0d9ea2329ac06ba1)<br>**Visible travel:** [✅](TESTING.md#case-in_game_visible_travel-5ace0d9ea2329ac06ba1) |
| **Road · external-10**<br>`external-10`<br>Variant: dd-rhw-l2 | **Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>**Route Query:** [✅](TESTING.md#case-in_game_route_query-ed6697a6188f6d8fe31e)<br>**Visible travel:** [✅](TESTING.md#case-in_game_visible_travel-ed6697a6188f6d8fe31e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-769623c9f01ca95cceea) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-82c75dbf8c3f7dc8e190) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-fdcc5be28a1bb3cfd543) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-705f63bbf795196a35bf) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cdc4505b6d31cd4005e0) |
| **Road · external-12**<br>`external-12`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-ae4212e277ae316758e4) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-876d1ac7e53bc6e82963) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8cb8dbeb79827efa2f4e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>**Route Query:** [✅](TESTING.md#case-in_game_route_query-6975b9e0a8028159ad14)<br>**Visible travel:** [✅](TESTING.md#case-in_game_visible_travel-6975b9e0a8028159ad14) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0c54f40751b6b87bf998) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-a0045479dcaf4b437fc5)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9ac60b007bece4aac7eb) |

Source: [connections.json](connections.json).

<!-- END ASSEMBLY CONNECTION MATRIX -->
