---
title: "Straight-stem HSR trumpet V4"
summary: "Rebuild the V4 trumpet from reusable menu pieces, with four small tails extracted into existing ordinary straight HSR, and explain every accepted or rejected atomization decision."
audience: "Players and assembly authors"
document_type: "guide"
---

# Straight-stem HSR trumpet V4

[Views](#complete-assembly-views) · [Atomization decisions](#tail-extraction-decisions) · [Pieces](#fourteen-reusable-menu-types) · [Placements](#twenty-six-placements) · [Build steps](#rebuild-this-arrangement) · [Testing](TESTING.md)

V4 is a **modular blueprint**: an arrangement built from several separately selectable pieces. A **piece type** is one menu button; a **placement** is one copy of that type in the city. This current blueprint uses **26 placements of 14 types**, within a **20 × 23 tile** rectangle, with **109 occupied tiles** and **75 support positions**. Its approved layout and pictures remain fixed. Earlier trumpet blueprints and their exclusive pieces have been removed; V4 has no whole-interchange one-click button.

The optional [trumpet menu experiment](../../../../docs/BUILD_AND_INSTALL.md#try-the-trumpet-menu-experiment) gives these same fourteen types a shared Tab/Shift+Tab cycle and a test submenu with individual buttons. It changes browsing only: each click still places one component, and the complete blueprint still requires the placements below. Both entry points share the same type family; Home/End rotate the current component. Actual menu visibility, selection, and cycling remain unverified until tested in SimCity 4.

**HSR** means elevated High Speed Rail. **L2** here has its train path at 15.5 m and **L4** at 30.5 m; the northern loop also uses a 23 m intermediate connection. Software verification, installation and observed train operation are separate states. V4’s actual saved resources pass software checks. An installation receipt confirms the installed files; correct rendering and train operation still require the separate human checks in TESTING.

## Tail extraction decisions

**Atomization** means separating a larger piece into smaller useful modules. V4 extracts four almost-straight tail tiles into two existing standard types. Their remaining junctions and curves become four new reusable types with their own menu buttons. No new special straight variant is needed. The comparison table preserves each **original reviewed piece’s local coordinates** as historical measurement context; those predecessor definitions are not current dependencies. The shortened V4 preview starts its own local grid: for example, new P01B local (X4, Y0) is the retained tile at assembly (X6, Y7), while original P01B local (X4, Y0) becomes the separate P01BS tile at assembly (X6, Y6).

| Original placement and local tile | Assembly tile | New ordinary placement | Existing standard and rotation | Remaining reusable core |
| --- | --- | --- | --- | --- |
| P01A (X0, Y0) | (X0, Y13) | P01AW | HSR L2 Two-Track Straight, 270° | P01A: Short Mainline Diverge Core, 4 tiles |
| P03B (X5, Y0) | (X14, Y13) | P03BE | HSR L2 Two-Track Straight, 270° | P03B: Short Opposed Merge Core, 5 tiles |
| P01B (X4, Y0) | (X6, Y6) | P01BS | One-Way HSR L2 Eight-Metre Straight, 180° | P01B: Shortened One-Way Departure Curve, 12 tiles |
| P03D (X0, Y0) | (X8, Y6) | P03DS | One-Way HSR L2 Eight-Metre Straight, 0° | P03D: Shortened One-Way Return Curve, 12 tiles |

The original P01A/P03B tails deviate **4.018 mm** from ordinary paired track; P01B/P03D deviate **2.058 mm** from centred one-way track. Those measurements qualify under the requested **strictly less than 5 mm** candidate policy. The joining curve in the next retained tile needs a separately measured correction: approximately **24.33 mm** for each paired junction and **8.14 mm** for each one-way curve. These were small local redesigns; the sub-5 mm eligibility threshold was not a bound on every adjoining route correction. The independent bounds are **24.5 mm** and **8.2 mm**, while the existing curve, clearance and support limits stay in force.

The one-way straight must be **One-Way HSR L2 Eight-Metre Straight** (`hsr-component-lower-oneway-straight`), whose centred deck is 8 m wide. The similarly named `interchange-oneway-hsr-straight` has a different 7.5 m profile and is not the replacement used here. P01BS runs south at 180°; P03DS runs north at 0°.

Not every straight-looking tile qualifies. P02A's end tails bend **119.840 mm**. P03B's western tail bends **6.437 mm**. P01A's opposite end has straight train routes but a necessary platform wing and wall opening beside the branch; inserting a normal straight would put a wall inside the branch's train clearance. A rotated P03C also misses P01A's branch connection by approximately **5.836 m**. The [decision table in TESTING](TESTING.md#accepted-and-retained-candidates) explains the remaining candidates. The [historical decision record](checks/atomization.json) accounts for all **51 reviewed source tiles** in the five original modules and records why each stayed or was extracted. Current verification checks the retained design against its [approved resource fingerprints](checks/resources.json), without opening deleted predecessor files.

## Complete assembly views

Every image uses the same city grid. The first two omit part names. The next three show exact menu names and placement labels. The final plan shows tile ownership: adjacent placements have clearly different colours and thick boundaries, even when they reuse the same button. The [render report](evidence/render.json) identifies the actual saved models and image hashes.

![V4 clean top view on the fixed X/Y city grid](previews/overview-top.png)

![V4 clean southeast view on the same X/Y grid](previews/preview.png)

![V4 named top view with every exact menu name](previews/named-top.png)

![V4 named southeast view](previews/named-southeast.png)

![V4 named northwest view](previews/named-northwest.png)

![V4 tile ownership and placement positions with distinct adjacent colours and thick boundaries](previews/tile-ownership.png)

## Coordinates and rotations

Each city tile measures **16 × 16 m**. On the north-up plan, **X0–X19** increase east/right and **Y0–Y22** increase north/up. The central crossing stays at **(X7, Y13)**. The southwest tile centre is implicitly **(X0, Y0)**; no global origin marker appears. Standalone piece previews use their own local zero-based grid and authored 0° orientation.

A **reference position** is a piece's software reference tile, which can be empty in a sparse piece. The table therefore describes exact model positions rather than certified mouse-click anchors. Align the entire cursor preview with the ownership plan. A rotation is **counterclockwise from the standalone 0° picture**: 270° counterclockwise equals 90° clockwise. Proper rotations turn the route and its direction together; they do not reverse a one-way track.

## Fourteen reusable menu types

Open **Transportation → Rail** and hover over a teal **PART HSR** icon. Its title begins **SCP | [PART]**. The table lists the exact descriptive name after that prefix. Click a thumbnail for the full angled view. Every new type also has a top view of the same saved model. Repeated placements share one button and one canonical picture.

| Standalone angled picture | Exact descriptive menu name and permanent piece ID | Placements | Quantity |
| --- | --- | --- | ---: |
| [![HSR L2 Short Mainline Diverge Core: canonical angled view](../../00_pieces/hsr-component-l2-short-mainline-diverge-core/preview-thumb.png)](../../00_pieces/hsr-component-l2-short-mainline-diverge-core/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-short-mainline-diverge-core/preview-top.png) | **[HSR L2 Short Mainline Diverge Core](../../00_pieces/hsr-component-l2-short-mainline-diverge-core/README.md)**<br>`hsr-component-l2-short-mainline-diverge-core` | P01A | 1 |
| [![HSR L2 Two-Track Straight: canonical angled view](../../00_pieces/hsr-component-lower-paired-straight/preview-thumb.png)](../../00_pieces/hsr-component-lower-paired-straight/preview.png) | **[HSR L2 Two-Track Straight](../../00_pieces/hsr-component-lower-paired-straight/README.md)**<br>`hsr-component-lower-paired-straight` | P01S, P03CW, P03CE, P04W, P04E, P01AW, P03BE | 7 |
| [![HSR L2 Shortened One-Way Departure Curve: canonical angled view](../../00_pieces/hsr-component-l2-shortened-departure-curve/preview-thumb.png)](../../00_pieces/hsr-component-l2-shortened-departure-curve/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-shortened-departure-curve/preview-top.png) | **[HSR L2 Shortened One-Way Departure Curve](../../00_pieces/hsr-component-l2-shortened-departure-curve/README.md)**<br>`hsr-component-l2-shortened-departure-curve` | P01B | 1 |
| [![HSR Modular Symmetric Split and Return: canonical angled view](../../00_pieces/hsr-component-modular-south-junction/preview-thumb.png)](../../00_pieces/hsr-component-modular-south-junction/preview.png) | **[HSR Modular Symmetric Split and Return](../../00_pieces/hsr-component-modular-south-junction/README.md)**<br>`hsr-component-modular-south-junction` | P02A | 1 |
| [![HSR Modular Two-Track L2 to L4 Climb: canonical angled view](../../00_pieces/hsr-component-modular-paired-climb/preview-thumb.png)](../../00_pieces/hsr-component-modular-paired-climb/preview.png) | **[HSR Modular Two-Track L2 to L4 Climb](../../00_pieces/hsr-component-modular-paired-climb/README.md)**<br>`hsr-component-modular-paired-climb` | P02B | 1 |
| [![HSR L2 Compact Paired Fan Join: canonical angled view](../../00_pieces/hsr-component-l2-paired-fan-compact-join/preview-thumb.png)](../../00_pieces/hsr-component-l2-paired-fan-compact-join/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-paired-fan-compact-join/preview-top.png) | **[HSR L2 Compact Paired Fan Join](../../00_pieces/hsr-component-l2-paired-fan-compact-join/README.md)**<br>`hsr-component-l2-paired-fan-compact-join` | P03A | 1 |
| [![HSR L2 Short Opposed Merge Core: canonical angled view](../../00_pieces/hsr-component-l2-short-opposed-merge-core/preview-thumb.png)](../../00_pieces/hsr-component-l2-short-opposed-merge-core/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-short-opposed-merge-core/preview-top.png) | **[HSR L2 Short Opposed Merge Core](../../00_pieces/hsr-component-l2-short-opposed-merge-core/README.md)**<br>`hsr-component-l2-short-opposed-merge-core` | P03B | 1 |
| [![HSR L2 Compact Fan Diverge: canonical angled view](../../00_pieces/hsr-component-l2-compact-fan-diverge/preview-thumb.png)](../../00_pieces/hsr-component-l2-compact-fan-diverge/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-compact-fan-diverge/preview-top.png) | **[HSR L2 Compact Fan Diverge](../../00_pieces/hsr-component-l2-compact-fan-diverge/README.md)**<br>`hsr-component-l2-compact-fan-diverge` | P03C | 1 |
| [![HSR L2 Shortened One-Way Return Curve: canonical angled view](../../00_pieces/hsr-component-l2-shortened-return-curve/preview-thumb.png)](../../00_pieces/hsr-component-l2-shortened-return-curve/preview.png)<br>[Top view](../../00_pieces/hsr-component-l2-shortened-return-curve/preview-top.png) | **[HSR L2 Shortened One-Way Return Curve](../../00_pieces/hsr-component-l2-shortened-return-curve/README.md)**<br>`hsr-component-l2-shortened-return-curve` | P03D | 1 |
| [![HSR Modular One-Tile Two-Level Crossing: canonical angled view](../../00_pieces/hsr-component-modular-crossing-core/preview-thumb.png)](../../00_pieces/hsr-component-modular-crossing-core/preview.png) | **[HSR Modular One-Tile Two-Level Crossing](../../00_pieces/hsr-component-modular-crossing-core/README.md)**<br>`hsr-component-modular-crossing-core` | P04A | 1 |
| [![HSR L4 Two-Track Straight: canonical angled view](../../00_pieces/hsr-component-upper-paired-straight/preview-thumb.png)](../../00_pieces/hsr-component-upper-paired-straight/preview.png) | **[HSR L4 Two-Track Straight](../../00_pieces/hsr-component-upper-paired-straight/README.md)**<br>`hsr-component-upper-paired-straight` | P04N, P04S, P05, P06, P07, P08 | 6 |
| [![HSR Tight Two-Track Corner 30.5 to 23 Metres: canonical angled view](../../00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/preview-thumb.png)](../../00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/preview.png) | **[HSR Tight Two-Track Corner 30.5 to 23 Metres](../../00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/README.md)**<br>`hsr-component-tight-paired-curve90-l4-to-mid` | P09 | 1 |
| [![HSR Tight Two-Track Corner 23 to 15.5 Metres: canonical angled view](../../00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/preview-thumb.png)](../../00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/preview.png) | **[HSR Tight Two-Track Corner 23 to 15.5 Metres](../../00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/README.md)**<br>`hsr-component-tight-paired-curve90-mid-to-l2` | P10 | 1 |
| [![One-Way HSR L2 Eight-Metre Straight: canonical angled view](../../00_pieces/hsr-component-lower-oneway-straight/preview-thumb.png)](../../00_pieces/hsr-component-lower-oneway-straight/preview.png) | **[One-Way HSR L2 Eight-Metre Straight](../../00_pieces/hsr-component-lower-oneway-straight/README.md)**<br>`hsr-component-lower-oneway-straight` | P01BS, P03DS | 2 |

The [standalone-picture report](evidence/piece-previews.json) records canonical orientation, local grid, model hashes and visible captions. P01AW/P01S/P03BE/P03CW/P03CE/P04W/P04E share one lower paired-straight button. P01BS/P03DS share one centred one-way-straight button. P04N/P04S/P05–P08 share one upper paired-straight button.

## Twenty-six placements

Use the position and rotation together; the standalone image always shows 0°. Occupied tile count describes the actual sparse footprint, not its bounding rectangle.

| Placement | Exact descriptive menu name | Reference position | Rotation | Occupied tiles |
| --- | --- | --- | --- | ---: |
| P01A | HSR L2 Short Mainline Diverge Core | (X1, Y13) | 0° | 4 |
| P01S | HSR L2 Two-Track Straight | (X5, Y13) | 270° | 1 |
| P01B | HSR L2 Shortened One-Way Departure Curve | (X2, Y12) | 0° | 12 |
| P02A | HSR Modular Symmetric Split and Return | (X6, Y5) | 0° | 14 |
| P02B | HSR Modular Two-Track L2 to L4 Climb | (X7, Y11) | 0° | 8 |
| P03A | HSR L2 Compact Paired Fan Join | (X11, Y18) | 0° | 15 |
| P03B | HSR L2 Short Opposed Merge Core | (X9, Y13) | 0° | 5 |
| P03CW | HSR L2 Two-Track Straight | (X15, Y13) | 270° | 1 |
| P03C | HSR L2 Compact Fan Diverge | (X16, Y13) | 0° | 3 |
| P03CE | HSR L2 Two-Track Straight | (X19, Y13) | 270° | 1 |
| P03D | HSR L2 Shortened One-Way Return Curve | (X8, Y12) | 0° | 12 |
| P04A | HSR Modular One-Tile Two-Level Crossing | (X7, Y13) | 0° | 1 |
| P04N | HSR L4 Two-Track Straight | (X7, Y14) | 0° | 1 |
| P04S | HSR L4 Two-Track Straight | (X7, Y12) | 0° | 1 |
| P04W | HSR L2 Two-Track Straight | (X6, Y13) | 270° | 1 |
| P04E | HSR L2 Two-Track Straight | (X8, Y13) | 270° | 1 |
| P05 | HSR L4 Two-Track Straight | (X7, Y15) | 0° | 1 |
| P06 | HSR L4 Two-Track Straight | (X7, Y16) | 0° | 1 |
| P07 | HSR L4 Two-Track Straight | (X7, Y17) | 0° | 1 |
| P08 | HSR L4 Two-Track Straight | (X7, Y18) | 0° | 1 |
| P09 | HSR Tight Two-Track Corner 30.5 to 23 Metres | (X7, Y22) | 0° | 10 |
| P10 | HSR Tight Two-Track Corner 23 to 15.5 Metres | (X14, Y22) | 270° | 10 |
| P01AW | HSR L2 Two-Track Straight | (X0, Y13) | 270° | 1 |
| P03BE | HSR L2 Two-Track Straight | (X14, Y13) | 270° | 1 |
| P01BS | One-Way HSR L2 Eight-Metre Straight | (X6, Y6) | 180° | 1 |
| P03DS | One-Way HSR L2 Eight-Metre Straight | (X8, Y6) | 0° | 1 |

The [machine-readable plan](assembly.json) is authoritative for identities and model translations. P01A's reference is **(X1, Y13)** because P01AW owns the western approach tile at **(X0, Y13)**. The table gives the current reference positions of the other three shortened cores. Every occupied tile has exactly one owner.

## Matching the modules

A **port** is a track entrance or exit. Its position, direction, height, deck width and visible rails must agree with its neighbour. A **native end** accepts the stated ordinary track profile. A **custom curved end** requires its matching curved continuation; height alone is insufficient.

- P01AW meets the new P01A's ordinary west end. P01A meets P01S to the east and P01B at its custom branch. P01B's new ordinary south end meets P01BS, then P02A's western one-way port.
- P02A's eastern one-way port meets P03DS, then P03D. P03D's custom curved end meets P03B. P03B's new ordinary east end meets P03BE, then P03CW and P03C. P03CE completes the east approach.
- P02A's paired end meets P02B, which rises from 15.5 m to 30.5 m and meets P04S. P04A carries upper north/south HSR over lower east/west HSR without a level transfer.
- P04N and P05–P08 extend the upper stem. P09 and P10 join at 23 m. P10 descends to P03A, whose custom curved ends meet P03B and P03C.

Each linked piece README lists its ports and concrete candidate neighbours. The shortened curves' custom ends retain their existing positions; their new southern ends use the centred 8 m one-way profile.

## Rebuild this arrangement

Use clear, flat terrain for the first game test and keep the full **20 × 23 tile** rectangle clear. A **cursor preview** is the complete shape attached to your pointer before you click. Press **Home** or **End** to rotate it; on the keyboard used here, **Fn + ←** and **Fn + →** supply those keys. Align all occupied tiles with the plan; reference positions are not certified click anchors.

1. Open **Transportation → Rail**. Select **HSR Modular One-Tile Two-Level Crossing**. Place P04A at **(X7, Y13)**, 0°, with upper track north/south.
2. Select **HSR L4 Two-Track Straight** and place P04N/P04S at **(X7, Y14)** and **(X7, Y12)**, both 0°. Select **HSR L2 Two-Track Straight**, rotate 270°, and place P04W/P04E at **(X6, Y13)** and **(X8, Y13)**.
3. Place P02B **HSR Modular Two-Track L2 to L4 Climb** at **(X7, Y11)** and P02A **HSR Modular Symmetric Split and Return** at **(X6, Y5)**, both 0°. Match the climb's high end to P04S and its low end to P02A.
4. Place upper straights P05–P08 at **(X7, Y15)** through **(X7, Y18)**, all 0°. Place P09 **HSR Tight Two-Track Corner 30.5 to 23 Metres** at **(X7, Y22)**, 0°, and P10 **HSR Tight Two-Track Corner 23 to 15.5 Metres** at **(X14, Y22)**, 270°.
5. Place P03A **HSR L2 Compact Paired Fan Join** at **(X11, Y18)**, P03B **HSR L2 Short Opposed Merge Core** at **(X9, Y13)** and P03C **HSR L2 Compact Fan Diverge** at **(X16, Y13)**, all 0°. Their custom branch ends must meet the pictured fan routes.
6. Select the lower paired straight, rotate 270°, and place **P03BE (X14, Y13)**, **P03CW (X15, Y13)** and **P03CE (X19, Y13)**. P03BE is the newly extracted tile at the short merge's east end.
7. Place P01A **HSR L2 Short Mainline Diverge Core** at **(X1, Y13)**, 0°. Use the same paired straight at 270° for **P01AW (X0, Y13)** and **P01S (X5, Y13)**.
8. Place P01B **HSR L2 Shortened One-Way Departure Curve** at **(X2, Y12)** and P03D **HSR L2 Shortened One-Way Return Curve** at **(X8, Y12)**, both 0°.
9. Select **One-Way HSR L2 Eight-Metre Straight**. Place **P01BS (X6, Y6)** at **180°**, pointing south, and **P03DS (X8, Y6)** at **0°**, pointing north. These complete the two connections between the shortened curves and P02A; they are the same button in different rotations.
10. Extend compatible ordinary paired HSR beyond the west edge of X0, east edge of X19 and south edge of Y0. All three outside connections have their train path at **15.5 m**. Supply travel demand and test every journey below using the game's route query and moving trains.

The selected pieces support proper **0°, 90°, 180° and 270°** rotations in their construction rules. Keyboard response, cursor anchors, terrain behaviour and actual train operation still require human tests. Plop & Paint does not stamp this complete blueprint.

## Six complete journeys

**Service:** HSR, using the game's Monorail traffic class. Each direction is a separate journey. P04A appears twice in South → West because that journey passes first above and later along the mainline; no transfer occurs inside the crossing.

| Journey | Placement sequence |
| --- | --- |
| West → East | P01AW → P01A → P01S → P04W → P04A → P04E → P03B → P03BE → P03CW → P03C → P03CE |
| East → West | P03CE → P03C → P03CW → P03BE → P03B → P04E → P04A → P04W → P01S → P01A → P01AW |
| West → South | P01AW → P01A → P01B → P01BS → P02A |
| South → East | P02A → P03DS → P03D → P03B → P03BE → P03CW → P03C → P03CE |
| South → West | P02A → P02B → P04S → P04A → P04N → P05 → P06 → P07 → P08 → P09 → P10 → P03A → P03B → P04E → P04A → P04W → P01S → P01A → P01AW |
| East → South | P03CE → P03C → P03A → P10 → P09 → P08 → P07 → P06 → P05 → P04N → P04A → P04S → P02B → P02A |

U-turns and transfers between the two crossing levels are forbidden. Current per-journey game checkboxes are generated from this version's own observations in [TESTING.md](TESTING.md).

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](TESTING.md#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/6 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/24 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `W.in` | hsr / 7 / primary | in | [-120.0, -2.0, 15.5]; [1.0, -0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `W.out` | hsr / 7 / primary | out | [-120.0, 2.0, 15.5]; [-1.0, -0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `S.out` | hsr / 7 / primary | out | [-2.0, -216.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `S.in` | hsr / 7 / primary | in | [2.0, -216.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `E.out` | hsr / 7 / primary | out | [200.0, -2.0, 15.5]; [1.0, -0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `E.in` | hsr / 7 / primary | in | [200.0, 2.0, 15.5]; [-1.0, -0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `W.in` → `E.out` | primary |
| hsr | `W.in` → `S.out` | primary |
| hsr | `S.in` → `E.out` | primary |
| hsr | `S.in` → `W.out` | primary |
| hsr | `E.in` → `W.out` | primary |
| hsr | `E.in` → `S.out` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `W.in` | hsr / `W.out` | No directed route exists between these ports in the saved assembly transport paths. In-game confirmation remains unverified. |
| hsr / `S.in` | hsr / `S.out` | No directed route exists between these ports in the saved assembly transport paths. In-game confirmation remains unverified. |
| hsr / `E.in` | hsr / `E.out` | No directed route exists between these ports in the saved assembly transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->
