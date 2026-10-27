---
title: "Straight-stem HSR trumpet: testing and design history"
summary: "Define the trumpet connection checks, test setup, evidence, known defects, and retained design decisions."
audience: "Testers, assembly authors, and maintainers"
document_type: "reference"
---

# Straight-stem HSR trumpet: testing and design history

[Assembly overview](README.md) · [Connection checks](#connection-checks) · [Test layout](#prepare-the-test-layout) · [Current resource contract](checks/resources.json) · [Design history](#design-history) · [Quality contract](checks/contract.json) · [Layout contract](checks/layout.json) · [Shared observation procedure](../../../../docs/TESTING.md)

## Connection checks

The [README](README.md) is the assembly overview: pictures, required piece types, exact placements, and a summary matrix of external connections. This document holds the test procedure, exact cases, observations, failures, and engineering decisions. This trumpet is the working example for the revised presentation; a shared assembly README convention has not yet been finalized.

A **port** is an entrance to or exit from the assembly. Each matrix row is an entrance, and each column is an exit. The axis labels identify the network service as well as the approach, so an HSR port remains distinct from any future passenger, ground-rail, or other network port at the same approach. West, East, and South name the approaches in the README's north-up plan. West → East and East → West are separate cells and separate directed journeys.

**Game appearance** has one overall status above the matrix. A person inspects the complete placed assembly in the game for missing rails, broken decks, incorrect walls, pillars, and shadows. Generated preview pictures do not establish an in-game appearance pass.

Each permitted connection has three separate checks:

1. **Saved PATH:** software can follow the train routes encoded in the saved game resources from this entrance to this exit. A PATH is a resource that describes permitted vehicle movement. A software pass establishes this routing result; it does not establish what the game displays or simulates.
2. **Route Query:** the game's Route Query tool shows traffic following the specific entrance-to-exit connection. Record the direction, environment, and evidence separately from visible train travel.
3. **Visible train travel:** a person has watched a train travel through the specific entrance-to-exit connection in the game. A Route Query line alone does not satisfy this check. Record the direction, environment, and evidence for the observed train.

The README uses **✅** for a current pass, **❌** for a current failure, and **?** when a current result has not been established. Open its status links for exact evidence, failures, stale results, or missing coverage. A **stale** observation belongs to inputs that have since changed and therefore cannot establish the current result. A forbidden connection is an intentionally prohibited journey; its separate in-game check confirms that the game prevents that travel. The matrix summarizes evidence; it does not discover compatible neighbouring pieces.

Manual game checks use the north-up test layout shown in the README. **0°** identifies that reference orientation in the record; the test plan does not require rebuilding and retesting the whole assembly at 90°, 180°, and 270°. Individual pieces still use the placement table's specified rotations. The independent software checks retain the supported construction rotations and their existing routing requirements.

There is one Route Query case and one visible-travel case for each of the six permitted directions, one whole-assembly appearance case, and one negative case for each of the three forbidden U-turns. Placement, demolition, and save/reload each have one case for the reference layout. The six existing preview-review cases stay separate from actual game appearance. Previously unobserved duplicate rotation cases are removed; any observed retired case stays historical. No game result is converted into a pass by changing this test plan, and both existing software observations remain unchanged.

Use the exact case links in the matrix and the [test checklist](#test-checklist) to record results. A pass covers only its recorded game environment, layout, and inputs. See [game testing](#game-testing) for the open demolition defect and the checks that the connection matrix does not cover.

## Current independent acceptance scope

A **PATH** describes train movement. An **S3D model** contains visible triangles. A **DAT archive** packages those game resources. A **fingerprint** is a hash of exact file bytes; it detects any change in the approved resources.

The schema-3 [current resource contract](checks/resources.json) pins all **14 current piece DATs**, their identities, recipes, sizes, resource counts, and hashes. It also pins the models, PATHs, and shadows of all **109 placed tiles**, their owning pieces and rotations, all six complete directed journeys, the fixed layout, and the historical decision content. Verification reads the current staged build and compares these exact approved fingerprints before performing independent physical and routing checks. Verification uses the current compiled resources and their declared contracts.

The placement contract requires **26 placements, 14 types, 109 occupied tiles, and 75 support centres**, at least **16 m** apart. Outside ports, the **20 × 23 tile** construction rectangle and fixed X/Y grid are unchanged. The software verifier checks all six HSR journeys in every proper rotation, with no U-turn or unintended level transfer. Full native bed, underside, and parapet sections are checked at the four exposed ordinary connections. Keeping an inherited interface byte-identical does not establish that every visual detail at that interface has been redesigned.

The verifier also checks full **5 m** train corridors, native visible rails, deck intersections, pillar contacts, separate tile ownership, all five model/shadow zooms, and construction rotation lists. Existing per-module minimum radius is **24 m**, curvature-change limit **0.0015 per square metre**, and native-end curvature limit **0.0005 per metre**. The two direct-slip journeys receive additional end-to-end checks. The other four journeys are pinned to their exact approved current geometry and retain the constituent modules' independent contracts; this does not impose a new whole-journey curvature threshold on the loop.

## Inherited interface checks and limits

The four ordinary connections receive full native slab, underside and parapet checks. P03B's western interface retains its approved model bytes, including an inherited incomplete outer parapet-cap section. Its train corridor and neighbouring geometry remain checked; this cleanup does not repair that separate visual detail.

The two shortened one-way curves retain their custom-end tiles. Their standalone rail audit allows a narrowly limited **2.65 m cut depth**, tied to the exact approved port-tile model hashes at all five zooms. This accounts for a rail strip crossing the artificial standalone cut. It neither widens the allowed rail strip nor permits stray rails inside the piece. The complete-assembly audit uses actual neighbouring models and uncut routes, with no artificial end cap. Mutation tests reject changed port hashes, excessive depth or width, and interior stray rails.

## Software verification

The approved saved assembly contains **109 occupied tiles, 659,271 triangles, 167 encoded route fragments, and 75 pillars**, with minimum **16 m** spacing. The [current validation](evidence/validation.json) identifies the exact audited resources and checks. Historical test logs, build provenance, and preservation audits remain linked in the [design history](#design-history). No software result marks a human observation as passed.

From the project folder containing `custom-pieces`, run:

```sh
python3 custom-pieces/scp.py build --set hsr-straight-stem-trumpet --output custom-pieces/dist/straight-stem-trumpet --progress
python3 custom-pieces/scp.py verify --output custom-pieces/dist/straight-stem-trumpet
python3 custom-pieces/domains/high-speed-rail/tools/verify_hsr_trumpet.py --build custom-pieces/dist/straight-stem-trumpet --scene custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/assembly.json --output custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/evidence/validation.json
python3 custom-pieces/scp.py check --scope straight-stem-trumpet
```

The validation report identifies the [exact manifest snapshot at audit time](evidence/audited-build-manifest.json). Documentation-only export metadata may change later; the approved DAT bytes remain pinned independently. A missing current descriptor, missing required staged build or changed resource fails verification. Optional integration tests may explicitly skip an absent current build; they must not hide malformed present builds or substitute generated expected answers.

The six assembly pictures start with `Assembly - Straight-stem HSR trumpet`; the second row identifies a `Clean view`, `Component guide`, or `Construction view`, followed by the camera direction. Their current [render report](evidence/render.json) identifies the exact images, renderer settings, and saved-model inputs. Only the first two header rows changed; every pixel from row 108 downward remains unchanged. The standalone component pictures and their [picture report](evidence/piece-previews.json) keep their existing bytes. When those pictures are next refreshed, their first row will start with `Piece - ` and their source-backed display name; their second row will identify a `Clean view` or `Connection overview`. Frozen reports in the design history describe their original inputs and images. Updated assembly picture hashes affect image-review dependencies, without creating new software or game passes.

## Prepare the test layout

Use the README's [views](README.md#1-views), [piece list](README.md#2-pieces), and [placement table](README.md#3-placements) as the fixed reference. The following sequence prepares a repeatable test layout; it is not evidence that placement or travel has passed in the game.

### Layout reference

Each city tile measures **16 × 16 m**. On the north-up plan, **X0–X19** increase east/right and **Y0–Y22** increase north/up. The central crossing stays at **(X7, Y13)**. The southwest tile centre is implicitly **(X0, Y0)**; no global origin marker appears. Standalone piece previews use their own local zero-based grid and authored 0° orientation.

A **reference position** is a piece's software reference tile, which can be empty in a sparse piece. The table therefore describes exact model positions rather than certified mouse-click anchors. Align the entire cursor preview with the ownership plan. A rotation is **counterclockwise from the standalone 0° picture**: 270° counterclockwise equals 90° clockwise. Proper rotations turn the route and its direction together; they do not reverse a one-way track.

### Module interfaces

A **port** is a track entrance or exit. Its position, direction, height, deck width, and visible rails must agree with its neighbour. A **native end** accepts the stated ordinary track profile. A **custom curved end** requires its matching curved continuation; height alone is insufficient.

- P01AW meets P01A's ordinary west end. P01A meets P01S to the east and P01B at its custom branch. P01B's ordinary south end meets P01BS, then P02A's western one-way port.
- P02A's eastern one-way port meets P03DS, then P03D. P03D's custom curved end meets P03B. P03B's ordinary east end meets P03BE, then P03CW and P03C. P03CE completes the east approach.
- P02A's paired end meets P02B, which rises from 15.5 m to 30.5 m and meets P04S. P04A carries upper north/south HSR over lower east/west HSR without a level transfer.
- P04N and P05–P08 extend the upper stem. P09 and P10 join at 23 m. P10 descends to P03A, whose custom curved ends meet P03B and P03C.

Each linked piece README lists its declared ports; these declarations do not establish complete compatibility with a neighbouring piece. The curves use their declared custom interfaces and the centred 8 m one-way profile at their southern ends.

### Placement sequence

Use clear, flat terrain for the first game test and keep the full **20 × 23 tile** rectangle clear. A **cursor preview** is the complete shape attached to your pointer before you click. Press **Home** or **End** to rotate it; on keyboards without dedicated Home and End keys, check the keyboard mapping; some Mac keyboards use **Fn + ←** and **Fn + →**. Align all occupied tiles with the plan; reference positions are not certified click anchors.

1. Open **Transportation → Rail**. Select **HSR Modular One-Tile Two-Level Crossing**. Place P04A at **(X7, Y13)**, 0°, with upper track north/south.
2. Select **HSR L4 Two-Track Straight** and place P04N/P04S at **(X7, Y14)** and **(X7, Y12)**, both 0°. Select **HSR L2 Two-Track Straight**, rotate 270°, and place P04W/P04E at **(X6, Y13)** and **(X8, Y13)**.
3. Place P02B **HSR Modular Two-Track L2 to L4 Climb** at **(X7, Y11)** and P02A **HSR Modular Symmetric Split and Return** at **(X6, Y5)**, both 0°. Match the climb's high end to P04S and its low end to P02A.
4. Place upper straights P05–P08 at **(X7, Y15)** through **(X7, Y18)**, all 0°. Place P09 **HSR Tight Two-Track Corner 30.5 to 23 Metres** at **(X7, Y22)**, 0°, and P10 **HSR Tight Two-Track Corner 23 to 15.5 Metres** at **(X14, Y22)**, 270°.
5. Place P03A **HSR L2 Compact Paired Fan Join** at **(X11, Y18)**, P03B **HSR L2 Short Opposed Merge Core** at **(X9, Y13)**, and P03C **HSR L2 Compact Fan Diverge** at **(X16, Y13)**, all 0°. Their custom branch ends must meet the pictured fan routes.
6. Select the lower paired straight, rotate 270°, and place **P03BE (X14, Y13)**, **P03CW (X15, Y13)**, and **P03CE (X19, Y13)**.
7. Place P01A **HSR L2 Short Mainline Diverge Core** at **(X1, Y13)**, 0°. Use the same paired straight at 270° for **P01AW (X0, Y13)** and **P01S (X5, Y13)**.
8. Place P01B **HSR L2 Shortened One-Way Departure Curve** at **(X2, Y12)** and P03D **HSR L2 Shortened One-Way Return Curve** at **(X8, Y12)**, both 0°.
9. Select **One-Way HSR L2 Eight-Metre Straight**. Place **P01BS (X6, Y6)** at **180°**, pointing south, and **P03DS (X8, Y6)** at **0°**, pointing north. These complete the two connections between the curves and P02A; select the same cycle component at the two specified rotations.
10. Extend compatible ordinary paired HSR beyond the west edge of X0, east edge of X19, and south edge of Y0. All three outside connections have their train path at **15.5 m**. Supply travel demand and test every journey below using separate Route Query and visible-train observations.

The selected pieces support proper **0°, 90°, 180°, and 270°** rotations in their construction rules. For this game test, use each placement at the rotation specified in the README. Keyboard response, cursor anchors, terrain behaviour, and actual train operation still require human observations. Plop & Paint does not stamp this complete blueprint.

### Directed routes under test

**Service:** HSR, using the game's Monorail traffic class. Each direction is a separate journey. P04A appears twice in South → West because that journey passes first above and later along the mainline; no transfer occurs inside the crossing.

| Journey | Placement sequence |
| --- | --- |
| West → East | P01AW → P01A → P01S → P04W → P04A → P04E → P03B → P03BE → P03CW → P03C → P03CE |
| East → West | P03CE → P03C → P03CW → P03BE → P03B → P04E → P04A → P04W → P01S → P01A → P01AW |
| West → South | P01AW → P01A → P01B → P01BS → P02A |
| South → East | P02A → P03DS → P03D → P03B → P03BE → P03CW → P03C → P03CE |
| South → West | P02A → P02B → P04S → P04A → P04N → P05 → P06 → P07 → P08 → P09 → P10 → P03A → P03B → P04E → P04A → P04W → P01S → P01A → P01AW |
| East → South | P03CE → P03C → P03A → P10 → P09 → P08 → P07 → P06 → P05 → P04N → P04A → P04S → P02B → P02A |

U-turns and transfers between the two crossing levels are forbidden. The separate Route Query and visible-travel cases are generated from this version's own record in [TESTING.md](TESTING.md).

## Game testing

**Open demolition defect, reported 2026-10-23:** selecting one tile for demolition caused connected custom parts to appear as Monorail; disconnected copies remained unchanged in the original report. The user also confirmed a smaller reproduction: place three copies of `hsr-component-lower-paired-straight` end to end, delete the middle copy, and both connected survivors appear as Monorail. The disconnected control's outcome was not separately reported for this second test. The exact original deleted type, orientation, affected cells, and confirmed game environment remain unknown. The [scoped failure report](evidence/demolition-regression-20261023.json) binds the installed menu-trial context and retains both observations and their limits. Static comparison found all 165 installed piece archives and every construction definition unchanged from the pre-menu installation; it does not establish the runtime cause or a fix. Follow the [single-tile demolition regression procedure](../../../../docs/TESTING.md#investigate-single-tile-demolition-and-connected-survivors) in a disposable city. Existing whole-placement demolition and save/reload observations do not cover this failure.

The assembly menu uses one **SCP | ASSEMBLY | HSR Trumpet** button. Check that Tab visits its fourteen components, Shift+Tab reverses that order, and one click places only the selected component. The [assembly-menu guide](../../../../docs/BUILD_AND_INSTALL.md#prepare-the-assembly-menu) explains the candidate-specific menu checks. The [executed assembly-menu audit](evidence/assembly-menu.json) confirms one button, a fourteen-component cycle, unchanged piece archives, and no submenu. The candidate is staged at `custom-pieces/dist/straight-stem-trumpet` and has not been installed. Static verification does not establish the button's appearance or keyboard behaviour in the game.

Assembly game observations remain **unverified** unless the user has explicitly confirmed the exact case in this subject's own record. Documentation and menu changes do not establish a game observation. Use the [shared observation procedure](../../../../docs/TESTING.md) to record precise human results in `checks/manual-tests.json`; software checks cannot create those confirmations.

After installing an authorized test build, use a disposable flat city. Inspect P01AW/P01A and P03B/P03BE at every zoom, then P01B/P01BS and P03DS/P03D. Check rails, deck, wall openings, pillars, and shadows. Verify each piece's cursor placement at its specified orientation. Build the complete reference arrangement, supply real Monorail demand, and check every journey with separate Route Query and visible-train observations. Also test forbidden U-turns and level transfers, demolition, and save/reload. Record the tested file hashes, city layout, platform, and screenshots with the observation.

## Design history

Historical executions retain their original names, paths, input fingerprints, and results. The [test logs](evidence/test-results.json), [build provenance](evidence/build-provenance.json), and [preservation audit](evidence/preservation.json) describe those original executions. Current entry points, scene identifiers, and software checks use `straight-stem-trumpet`.

This section retains the historical design decisions and their original measurements. These records explain how the current geometry was chosen; they do not represent additional selectable assembly versions or current game-test passes. See the [decision ledger](checks/atomization.json) and [implementation record](evidence/atomization-implementation.json) for the original evidence.

### Accepted and retained candidates

**Atomization** means separating a larger piece into smaller useful modules. The historical candidate threshold was **strictly below 5 mm of original lateral deviation**. It selected a tail for investigation; it did not prove that its deck, wall openings, or supports could be replaced. The actual corrections in adjoining retained tiles had separate bounds: **24.5 mm** for paired junctions and **8.2 mm** for one-way curves. A **millimetre** is 0.001 m. The recorded eligibility measurements and correction bounds remain distinct.

Local X/Y positions in the following table refer to the original reviewed modules, not the shortened current previews. The schema-2 [atomization history](checks/atomization.json) retains those measurements, all **51 reviewed source cells**, the 17 decisions and their reasons. Original identifiers and hashes describe historical inputs; current verification neither opens deleted predecessor definitions nor remeasures deleted DATs. Instead, it checks that the recorded history stays unchanged and that every current replacement still matches its approved geometry fingerprint.

| Candidate in original piece | Original deviation | Decision | Reason |
| --- | ---: | --- | --- |
| P01A: (X0, Y0) | 4.018 mm | Extract into standard straight | The original branch tail is strictly below 5 mm from the compatible ordinary straight. A bounded correction in its adjoining retained tile gives an independently placeable native end; the existing straight then owns the extracted tile and its support. Both mirrored tails are changed together to preserve direct-slip symmetry. |
| P03B: (X5, Y0) | 4.018 mm | Extract into standard straight | The original branch tail is strictly below 5 mm from the compatible ordinary straight. A bounded correction in its adjoining retained tile gives an independently placeable native end; the existing straight then owns the extracted tile and its support. Both mirrored tails are changed together to preserve direct-slip symmetry. |
| P01B: (X4, Y0) | 2.058 mm | Extract into standard straight | The original branch tail is strictly below 5 mm from the compatible ordinary straight. A bounded correction in its adjoining retained tile gives an independently placeable native end; the existing straight then owns the extracted tile and its support. Both mirrored tails are changed together to preserve direct-slip symmetry. |
| P03D: (X0, Y0) | 2.058 mm | Extract into standard straight | The original branch tail is strictly below 5 mm from the compatible ordinary straight. A bounded correction in its adjoining retained tile gives an independently placeable native end; the existing straight then owns the extracted tile and its support. Both mirrored tails are changed together to preserve direct-slip symmetry. |
| P01A: Whole-piece substitution | Not applicable | Retain | A rotated P03C is a different branch: its socket misses by 5.835829856 m and its tangent by 2.202886 degrees. Replacing P01A that way would move several existing modules and break the agreed direct-slip symmetry. |
| P01A: (X4, Y0) | 0.000 mm | Retain | Straight PATHs are insufficient: this tile owns a 500 mm branch-platform wing and an open parapet. An ordinary straight restores a wall only 1.169553309 m from the neighbouring branch PATH, inside its 2.6 m half-width clearance. |
| P02A: (X1, Y0) | 119.840 mm | Retain | Both directional branch tails move 119.840 mm, above the 5 mm eligibility threshold. This is also a split/merge platform rather than an ordinary straight profile. |
| P02A: (X0, Y5), (X2, Y5) | 119.840 mm | Retain | The side tails each move 119.840 mm. They fail the 5 mm threshold and participate in the shared split/merge platform. |
| P02A: (X1, Y3) | 0.000 mm | Retain | Its paired PATHs are straight but the shared slab is 16 m wide and has branch wall openings. An ordinary 15 m straight changes the physical connection. |
| P03B: (X0, Y0) | 6.437 mm | Retain | Its branch moves 6.437054 mm. This is above the strict 5 mm threshold, so it is not silently rounded into eligibility. |
| P03B: (X4, Y0) | 286.369 mm | Retain | The branch moves 286.369 mm and the northern branch deck reaches 8 m beyond the centre instead of the native 7.5 m half-width. An ordinary straight removes useful branch geometry. |
| P01B: (X4, Y1) | 148.533 mm | Retain | The next tile bends 148.533079 mm. Its route is not an almost-straight tail under the 5 mm policy. |
| P03D: (X0, Y1) | 148.533 mm | Retain | The next tile bends 148.533079 mm. Its route is not an almost-straight tail under the 5 mm policy. |
| P01B: (X4, Y2) | 1025.727 mm | Retain | This tile contains 1.02572658 m of lateral curve movement, so replacing it with a straight would materially change the layout. |
| P03D: (X0, Y2) | 1025.727 mm | Retain | This tile contains 1.02572658 m of lateral curve movement, so replacing it with a straight would materially change the layout. |
| P01B: (X4, Y3) | 3543.300 mm | Retain | This is a substantial bend of approximately 3.5433 m, not a straight tail. |
| P03D: (X0, Y3) | 3543.300 mm | Retain | This is a substantial bend of approximately 3.5433 m, not a straight tail. |

The saved [candidate-coverage report](evidence/candidate-coverage.json) preserves the rationale for the 34 generic retained cells: eight were structural models without train routes, while the other 26 each had a route fragment more than 5 mm from every tested cardinal or 45° straight, even with the best lateral offset. The smallest such recorded deviation was **72.955 mm**. It also records physical wall-clearance witnesses for the two all-straight candidates; an ordinary replacement at P02A would put a wall approximately **1.5 m** from the adjoining branch, inside its **2.6 m** clearance half-width. These are historical measurement results, not instructions to restore the removed source files or fixtures. A candidate can be reconsidered only through a separately authorized redesign and new evidence.

### Tail extraction decisions

**Atomization** means separating a larger piece into smaller useful modules. V4 extracts four almost-straight tail tiles into two existing standard types. Their remaining junctions and curves become four new reusable types with their own menu buttons. No new special straight variant is needed. The comparison table preserves each **original reviewed piece’s local coordinates** as historical measurement context; those predecessor definitions are not current dependencies. The shortened V4 preview starts its own local grid: for example, new P01B local (X4, Y0) is the retained tile at assembly (X6, Y7), while original P01B local (X4, Y0) becomes the separate P01BS tile at assembly (X6, Y6).

| Original placement and local tile | Assembly tile | New ordinary placement | Existing standard and rotation | Remaining reusable core |
| --- | --- | --- | --- | --- |
| P01A (X0, Y0) | (X0, Y13) | P01AW | HSR L2 Two-Track Straight, 270° | P01A: Short Mainline Diverge Core, 4 tiles |
| P03B (X5, Y0) | (X14, Y13) | P03BE | HSR L2 Two-Track Straight, 270° | P03B: Short Opposed Merge Core, 5 tiles |
| P01B (X4, Y0) | (X6, Y6) | P01BS | One-Way HSR L2 Eight-Metre Straight, 180° | P01B: Shortened One-Way Departure Curve, 12 tiles |
| P03D (X0, Y0) | (X8, Y6) | P03DS | One-Way HSR L2 Eight-Metre Straight, 0° | P03D: Shortened One-Way Return Curve, 12 tiles |

The original P01A/P03B tails deviate **4.018 mm** from ordinary paired track; P01B/P03D deviate **2.058 mm** from centred one-way track. Those measurements qualify under the requested **strictly less than 5 mm** candidate policy. The joining curve in the next retained tile needs a separately measured correction: approximately **24.33 mm** for each paired junction and **8.14 mm** for each one-way curve. These were small local redesigns; the sub-5 mm eligibility threshold was not a bound on every adjoining route correction. The independent bounds are **24.5 mm** and **8.2 mm**, while the existing curve, clearance, and support limits stay in force.

The one-way straight must be **One-Way HSR L2 Eight-Metre Straight** (`hsr-component-lower-oneway-straight`), whose centred deck is 8 m wide. The similarly named `interchange-oneway-hsr-straight` has a different 7.5 m profile and is not the replacement used here. P01BS runs south at 180°; P03DS runs north at 0°.

Not every straight-looking tile qualifies. P02A's end tails bend **119.840 mm**. P03B's western tail bends **6.437 mm**. P01A's opposite end has straight train routes but a necessary platform wing and wall opening beside the branch; inserting a normal straight would put a wall inside the branch's train clearance. A rotated P03C also misses P01A's branch connection by approximately **5.836 m**. The [decision table in TESTING](TESTING.md#accepted-and-retained-candidates) explains the remaining candidates. The [historical decision record](checks/atomization.json) accounts for all **51 reviewed source tiles** in the five original modules and records why each stayed or was extracted. Current verification checks the retained design against its [approved resource fingerprints](checks/resources.json), without opening deleted predecessor files.

### Preserved measurement context

The earlier redesign was limited to eight world tiles: **(X0–X1, Y13)** and **(X13–X14, Y13)** for paired tails and joining collars; **(X6, Y6–Y7)** and **(X8, Y6–Y7)** for one-way tails and joining collars. The ledger preserves its measured movement and bounds as history. This cleanup authorizes no geometry changes: the current fingerprint contract protects **all 109 tiles**, including those eight, and the four extracted placements still use the existing standard straight types at their specified rotations. Each current type generates its geometry from its own retained source.

The historical mesh comparison measured the **sum of changed cross-section intervals**, not one track's movement. Two parapet strips have four interval edges, giving a one-way bound of **4 × (8.2 mm route bound + 0.05 mm section precision) = 33 mm** in total, with each edge checked independently. That did not permit a 33 mm route shift: the route bound was **8.2 mm**. The current contract now pins the approved result exactly instead of requiring the deleted comparison inputs.

### Identity and presentation cleanup

On 2026-10-27, the maintained assembly identity, collection, verifier, and test names changed to `straight-stem-trumpet`. The [migration report](evidence/identity-migration.json) records the mapping and unchanged measured payloads. Original identity-bound contracts and the [original observations](evidence/design-history/checks-manual-tests-before-identity-rename.json) are archived byte for byte; their passes were not relabelled as new cases. Current software cases require their own executed verification, and game checks remain unverified.

The six assembly renders received neutral titles, with the atomization-history text removed. The saved S3D model bytes, track layout, supports, and every image pixel below the header band remain unchanged. The [current render report](evidence/render.json) and archived render-source context record the caption and identity updates separately from geometry.

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Human game checks are required only at 0° CCW. Supported construction orientations and software rotation checks retain their separate scope; these human cases do not establish observations at the other orientations.

Current totals: unverified: 25, passed: 2, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-fe740c153144a3695751">[x] passed</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-fe740c153144a3695751"></a>

**General: passed** — `software_resources-fe740c153144a3695751`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: actual saved-resource and full-assembly audit; confirmed at: 2026-10-27T14:12:46.158490+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json]; environment:

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-fe740c153144a3695751">[x] passed</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-fe740c153144a3695751"></a>

**General: passed** — `software_connectivity-fe740c153144a3695751`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet.py: actual saved-resource and full-assembly audit; confirmed at: 2026-10-27T14:12:46.158490+00:00; evidence: [evidence/validation.json, evidence/audited-build-manifest.json]; environment:

</details>

</details>

<details>
<summary>Preview review — Images — 6 cases; unverified: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:straight-stem-trumpet:clean-southeast | <a href="#case-preview_review-4255f74d1a0022065ce4">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:clean-top | <a href="#case-preview_review-8f00df0ccb26670bca5a">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:named-northwest | <a href="#case-preview_review-09c7f0560ea1efecf6f1">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:named-southeast | <a href="#case-preview_review-b0defe1adfa80a596bb8">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:named-top | <a href="#case-preview_review-ecf9be65aaa4dd4c3c7b">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:straight-stem-trumpet:tile-ownership | <a href="#case-preview_review-a613bd9fbd07c6e7cb5f">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:clean-southeast</summary>

<a id="case-preview_review-4255f74d1a0022065ce4"></a>

**General: unverified** — `preview_review-4255f74d1a0022065ce4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:clean-top</summary>

<a id="case-preview_review-8f00df0ccb26670bca5a"></a>

**General: unverified** — `preview_review-8f00df0ccb26670bca5a`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:named-northwest</summary>

<a id="case-preview_review-09c7f0560ea1efecf6f1"></a>

**General: unverified** — `preview_review-09c7f0560ea1efecf6f1`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:named-southeast</summary>

<a id="case-preview_review-b0defe1adfa80a596bb8"></a>

**General: unverified** — `preview_review-b0defe1adfa80a596bb8`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:named-top</summary>

<a id="case-preview_review-ecf9be65aaa4dd4c3c7b"></a>

**General: unverified** — `preview_review-ecf9be65aaa4dd4c3c7b`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet:tile-ownership</summary>

<a id="case-preview_review-a613bd9fbd07c6e7cb5f"></a>

**General: unverified** — `preview_review-a613bd9fbd07c6e7cb5f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:straight-stem-trumpet:tile-ownership.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-4b8e61d1c512b7c578e8">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-4b8e61d1c512b7c578e8"></a>

**0° CCW: unverified** — `in_game_render-4b8e61d1c512b7c578e8`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-4b8e61d1c512b7c578e8">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-4b8e61d1c512b7c578e8"></a>

**0° CCW: unverified** — `in_game_placement-4b8e61d1c512b7c578e8`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-4b8e61d1c512b7c578e8">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-4b8e61d1c512b7c578e8"></a>

**0° CCW: unverified** — `in_game_demolition-4b8e61d1c512b7c578e8`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-4b8e61d1c512b7c578e8">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-4b8e61d1c512b7c578e8"></a>

**0° CCW: unverified** — `in_game_save_reload-4b8e61d1c512b7c578e8`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 6 cases; unverified: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out | — | <a href="#case-in_game_route_query-8b08022118fd9f445d85">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out | — | <a href="#case-in_game_route_query-76bf51a0e3b87a77ead7">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out | — | <a href="#case-in_game_route_query-336582ad6132a64a36f8">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out | — | <a href="#case-in_game_route_query-2572758d9ad9c64a40fd">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out | — | <a href="#case-in_game_route_query-87f3cb5204e2970d80c1">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out | — | <a href="#case-in_game_route_query-aea09525a3e21f949d2b">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out</summary>

<a id="case-in_game_route_query-8b08022118fd9f445d85"></a>

**0° CCW: unverified** — `in_game_route_query-8b08022118fd9f445d85`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out</summary>

<a id="case-in_game_route_query-76bf51a0e3b87a77ead7"></a>

**0° CCW: unverified** — `in_game_route_query-76bf51a0e3b87a77ead7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out</summary>

<a id="case-in_game_route_query-336582ad6132a64a36f8"></a>

**0° CCW: unverified** — `in_game_route_query-336582ad6132a64a36f8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out</summary>

<a id="case-in_game_route_query-2572758d9ad9c64a40fd"></a>

**0° CCW: unverified** — `in_game_route_query-2572758d9ad9c64a40fd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out</summary>

<a id="case-in_game_route_query-87f3cb5204e2970d80c1"></a>

**0° CCW: unverified** — `in_game_route_query-87f3cb5204e2970d80c1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out</summary>

<a id="case-in_game_route_query-aea09525a3e21f949d2b"></a>

**0° CCW: unverified** — `in_game_route_query-aea09525a3e21f949d2b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 6 cases; unverified: 6</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out | — | <a href="#case-in_game_visible_travel-8b08022118fd9f445d85">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out | — | <a href="#case-in_game_visible_travel-76bf51a0e3b87a77ead7">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out | — | <a href="#case-in_game_visible_travel-336582ad6132a64a36f8">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out | — | <a href="#case-in_game_visible_travel-2572758d9ad9c64a40fd">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out | — | <a href="#case-in_game_visible_travel-87f3cb5204e2970d80c1">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out | — | <a href="#case-in_game_visible_travel-aea09525a3e21f949d2b">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out</summary>

<a id="case-in_game_visible_travel-8b08022118fd9f445d85"></a>

**0° CCW: unverified** — `in_game_visible_travel-8b08022118fd9f445d85`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out</summary>

<a id="case-in_game_visible_travel-76bf51a0e3b87a77ead7"></a>

**0° CCW: unverified** — `in_game_visible_travel-76bf51a0e3b87a77ead7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out</summary>

<a id="case-in_game_visible_travel-336582ad6132a64a36f8"></a>

**0° CCW: unverified** — `in_game_visible_travel-336582ad6132a64a36f8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out</summary>

<a id="case-in_game_visible_travel-2572758d9ad9c64a40fd"></a>

**0° CCW: unverified** — `in_game_visible_travel-2572758d9ad9c64a40fd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out</summary>

<a id="case-in_game_visible_travel-87f3cb5204e2970d80c1"></a>

**0° CCW: unverified** — `in_game_visible_travel-87f3cb5204e2970d80c1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out</summary>

<a id="case-in_game_visible_travel-aea09525a3e21f949d2b"></a>

**0° CCW: unverified** — `in_game_visible_travel-aea09525a3e21f949d2b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-92b725456842f93c47ca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-dfbdc4123044e5fb53fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9f7a461fa713c7413977">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-92b725456842f93c47ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-92b725456842f93c47ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-dfbdc4123044e5fb53fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dfbdc4123044e5fb53fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9f7a461fa713c7413977"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f7a461fa713c7413977`.

Confirm this undeclared transfer is unavailable.

Scope: from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

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
| hsr | `E.in` → `S.out` | primary |
| hsr | `E.in` → `W.out` | primary |
| hsr | `S.in` → `E.out` | primary |
| hsr | `S.in` → `W.out` | primary |
| hsr | `W.in` → `E.out` | primary |
| hsr | `W.in` → `S.out` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `W.in` | hsr / `W.out` | not reachable in the saved placed encoded-route graph |
| hsr / `S.in` | hsr / `S.out` | not reachable in the saved placed encoded-route graph |
| hsr / `E.in` | hsr / `E.out` | not reachable in the saved placed encoded-route graph |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->
