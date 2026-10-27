---
title: "Straight-stem HSR trumpet V4: testing and decisions"
summary: "Define the trumpet connection checks, test setup, evidence, known defects, and retained design decisions."
audience: "Testers, assembly authors, and maintainers"
document_type: "reference"
---

# Straight-stem HSR trumpet V4: testing and decisions

[Assembly overview](README.md) · [Connection checks](#connection-checks) · [Test layout](#prepare-the-test-layout) · [Current resource contract](checks/resources.json) · [Decision history](checks/atomization.json) · [Quality contract](checks/contract.json) · [Layout contract](checks/layout.json) · [Shared observation procedure](../../../../docs/TESTING.md)

## Connection checks

The [README](README.md) is the assembly overview: pictures, required piece types, exact placements, and a summary matrix of external connections. This document holds the test procedure, exact cases, observations, failures, and engineering decisions. This trumpet is the working example for the revised presentation; a shared assembly README convention has not yet been finalized.

A **port** is an entrance to or exit from the assembly. Each matrix row is an entrance, and each column is an exit. The axis labels identify the network service as well as the approach, so an HSR port remains distinct from any future passenger, ground-rail, or other network port at the same approach. West, East, and South name the approaches in the README's north-up plan; the cases below retain each tested rotation explicitly.

Each permitted connection has four separate checks:

1. **Saved PATH:** software can follow the train routes encoded in the saved game resources from this entrance to this exit. A PATH is a resource that describes permitted vehicle movement. A software pass establishes this routing result; it does not establish what the game displays or simulates.
2. **Game appearance:** a person has inspected the complete placed assembly in the game. This is a whole-assembly check for each rotation, shared by the permitted cells, rather than a separate visual inspection of every journey. Look for missing rails, broken decks, incorrect walls, pillars, and shadows. Generated preview pictures do not count as an in-game appearance pass.
3. **Route Query:** the game's Route Query tool shows traffic following the specific entrance-to-exit connection. Record its direction, rotation, environment, and evidence separately from visible train travel.
4. **Visible train travel:** a person has watched a train travel through the specific entrance-to-exit connection in the game. A Route Query line alone does not satisfy this check. Record the direction, rotation, environment, and evidence for the observed train.

A matrix check is complete only when its required rotation cases have current passes; partial, failed, stale, and unverified coverage remains explicit. A **stale** observation belongs to inputs that have since changed and therefore cannot establish the current result. A forbidden connection is an intentionally prohibited journey, not a failed permitted journey. Its separate negative tests must confirm that the game prevents that travel. The matrix summarizes evidence; it does not discover compatible neighbouring pieces.

The former combined journey criterion allowed Route Query or traffic observation. For this pilot, its 24 unobserved journey cases are replaced by 24 Route Query cases and 24 visible-travel cases: six directions in four rotations for each check. No game result is converted into a pass by this split. The two existing software observations and all other scopes remain preserved. Any observed legacy case retained by the tooling stays historical and cannot satisfy either new criterion automatically.

Use the exact case links in the matrix and the [test checklist](#test-checklist) to record results. A pass covers only its recorded game environment and inputs. See [game testing](#game-testing) for the open demolition defect and the checks that the connection matrix does not cover.

## Accepted and retained candidates

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

## Tail extraction and current replacements

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

## Current independent acceptance scope

A **PATH** describes train movement. An **S3D model** contains visible triangles. A **DAT archive** packages those game resources. A **fingerprint** is a hash of exact file bytes; it detects any change in the approved resources.

The schema-3 [current resource contract](checks/resources.json) pins all **14 current piece DATs**, their identities, recipes, sizes, resource counts, and hashes. It also pins the models, PATHs, and shadows of all **109 placed tiles**, their owning pieces and rotations, all six complete directed journeys, the fixed layout, and the historical decision content. Verification reads the current staged build and compares these exact approved fingerprints before performing independent physical and routing checks. No deleted predecessor archive, source folder, or private historical fixture is required.

The earlier redesign was limited to eight world tiles: **(X0–X1, Y13)** and **(X13–X14, Y13)** for paired tails and joining collars; **(X6, Y6–Y7)** and **(X8, Y6–Y7)** for one-way tails and joining collars. The ledger preserves its measured movement and bounds as history. This cleanup authorizes no geometry changes: the current fingerprint contract protects **all 109 tiles**, including those eight, and the four extracted placements still use the existing standard straight types at their specified rotations. Each current type generates its geometry from its own retained source.

The placement contract requires **26 placements, 14 types, 109 occupied tiles, and 75 support centres**, at least **16 m** apart. Outside ports, the **20 × 23 tile** construction rectangle and fixed X/Y grid are unchanged. All six HSR journeys must pass every proper rotation, with no U-turn or unintended level transfer. Full native bed, underside, and parapet sections are checked at the four exposed ordinary connections. Keeping an inherited interface byte-identical does not establish that every visual detail at that interface has been redesigned.

The verifier also checks full **5 m** train corridors, native visible rails, deck intersections, pillar contacts, separate tile ownership, all five model/shadow zooms, and construction rotation lists. Existing per-module minimum radius is **24 m**, curvature-change limit **0.0015 per square metre**, and native-end curvature limit **0.0005 per metre**. The two direct-slip journeys receive additional end-to-end checks. The other four journeys are pinned to their exact approved current geometry and retain the constituent modules' independent contracts; this does not impose a new whole-journey curvature threshold on the loop.

## Inherited interface checks and limits

The four ordinary connections receive full native slab, underside and parapet checks. P03B's western interface retains its approved model bytes, including an inherited incomplete outer parapet-cap section. Its train corridor and neighbouring geometry remain checked; this cleanup does not repair that separate visual detail.

The two shortened one-way curves retain their custom-end tiles. Their standalone rail audit allows a narrowly limited **2.65 m cut depth**, tied to the exact approved port-tile model hashes at all five zooms. This accounts for a rail strip crossing the artificial standalone cut. It neither widens the allowed rail strip nor permits stray rails inside the piece. The complete-assembly audit uses actual neighbouring models and uncut routes, with no artificial end cap. Mutation tests reject changed port hashes, excessive depth or width, and interior stray rails.

The historical mesh comparison measured the **sum of changed cross-section intervals**, not one track's movement. Two parapet strips have four interval edges, giving a one-way bound of **4 × (8.2 mm route bound + 0.05 mm section precision) = 33 mm** in total, with each edge checked independently. That did not permit a 33 mm route shift: the route bound was **8.2 mm**. The current contract now pins the approved result exactly instead of requiring the deleted comparison inputs.

## Software verification

The approved saved assembly contains **109 occupied tiles, 659,271 triangles, 167 encoded route fragments, and 75 pillars**, with minimum **16 m** spacing. See the [current validation](evidence/validation.json), [executed test results and logs](evidence/test-results.json), [build provenance](evidence/build-provenance.json), and [preservation audit](evidence/preservation.json) for exact input fingerprints, current checks, suite counts, and any skips. The [implementation record](evidence/atomization-implementation.json) preserves the earlier measured redesign rationale. No software result marks a human observation as passed.

From the project folder containing `custom-pieces`, run:

```sh
python3 custom-pieces/scp.py build --set hsr-straight-stem-trumpet-v4 --output custom-pieces/dist/straight-stem-trumpet-v4 --progress
python3 custom-pieces/scp.py verify --output custom-pieces/dist/straight-stem-trumpet-v4
python3 custom-pieces/domains/high-speed-rail/tools/verify_hsr_trumpet_v4.py --build custom-pieces/dist/straight-stem-trumpet-v4 --scene custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/assembly.json --output custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/evidence/validation.json
python3 custom-pieces/scp.py check --scope straight-stem-trumpet-v4
```

The validation report identifies the [exact manifest snapshot at audit time](evidence/audited-build-manifest.json). Documentation-only export metadata may change later; the approved DAT bytes remain pinned independently. A missing current descriptor, missing required staged build or changed resource fails verification. Optional integration tests may explicitly skip an absent current build; they must not hide malformed present builds or substitute generated expected answers.

The six assembly views and current standalone piece pictures retain their existing bytes. Updating documentation, packaging, or the verification schema does not require rerendering or moving any track, support, placement, or image caption. No smaller overall rectangle is claimed; the original gain was four ordinary straight placements and four smaller reusable cores inside the unchanged footprint.

## Prepare the test layout

Use the README's [views](README.md#complete-assembly-views), [piece list](README.md#fourteen-reusable-menu-types), and [placement table](README.md#twenty-six-placements) as the fixed reference. The following sequence prepares a repeatable test layout; it is not evidence that placement or travel has passed in the game.

### Module interfaces

A **port** is a track entrance or exit. Its position, direction, height, deck width, and visible rails must agree with its neighbour. A **native end** accepts the stated ordinary track profile. A **custom curved end** requires its matching curved continuation; height alone is insufficient.

- P01AW meets the new P01A's ordinary west end. P01A meets P01S to the east and P01B at its custom branch. P01B's new ordinary south end meets P01BS, then P02A's western one-way port.
- P02A's eastern one-way port meets P03DS, then P03D. P03D's custom curved end meets P03B. P03B's new ordinary east end meets P03BE, then P03CW and P03C. P03CE completes the east approach.
- P02A's paired end meets P02B, which rises from 15.5 m to 30.5 m and meets P04S. P04A carries upper north/south HSR over lower east/west HSR without a level transfer.
- P04N and P05–P08 extend the upper stem. P09 and P10 join at 23 m. P10 descends to P03A, whose custom curved ends meet P03B and P03C.

Each linked piece README lists its declared ports; these declarations do not establish complete compatibility with a neighbouring piece. The shortened curves' custom ends retain their existing positions; their new southern ends use the centred 8 m one-way profile.

### Placement sequence

Use clear, flat terrain for the first game test and keep the full **20 × 23 tile** rectangle clear. A **cursor preview** is the complete shape attached to your pointer before you click. Press **Home** or **End** to rotate it; on keyboards without dedicated Home and End keys, check the keyboard mapping; some Mac keyboards use **Fn + ←** and **Fn + →**. Align all occupied tiles with the plan; reference positions are not certified click anchors.

1. Open **Transportation → Rail**. Select **HSR Modular One-Tile Two-Level Crossing**. Place P04A at **(X7, Y13)**, 0°, with upper track north/south.
2. Select **HSR L4 Two-Track Straight** and place P04N/P04S at **(X7, Y14)** and **(X7, Y12)**, both 0°. Select **HSR L2 Two-Track Straight**, rotate 270°, and place P04W/P04E at **(X6, Y13)** and **(X8, Y13)**.
3. Place P02B **HSR Modular Two-Track L2 to L4 Climb** at **(X7, Y11)** and P02A **HSR Modular Symmetric Split and Return** at **(X6, Y5)**, both 0°. Match the climb's high end to P04S and its low end to P02A.
4. Place upper straights P05–P08 at **(X7, Y15)** through **(X7, Y18)**, all 0°. Place P09 **HSR Tight Two-Track Corner 30.5 to 23 Metres** at **(X7, Y22)**, 0°, and P10 **HSR Tight Two-Track Corner 23 to 15.5 Metres** at **(X14, Y22)**, 270°.
5. Place P03A **HSR L2 Compact Paired Fan Join** at **(X11, Y18)**, P03B **HSR L2 Short Opposed Merge Core** at **(X9, Y13)**, and P03C **HSR L2 Compact Fan Diverge** at **(X16, Y13)**, all 0°. Their custom branch ends must meet the pictured fan routes.
6. Select the lower paired straight, rotate 270°, and place **P03BE (X14, Y13)**, **P03CW (X15, Y13)**, and **P03CE (X19, Y13)**. P03BE is the newly extracted tile at the short merge's east end.
7. Place P01A **HSR L2 Short Mainline Diverge Core** at **(X1, Y13)**, 0°. Use the same paired straight at 270° for **P01AW (X0, Y13)** and **P01S (X5, Y13)**.
8. Place P01B **HSR L2 Shortened One-Way Departure Curve** at **(X2, Y12)** and P03D **HSR L2 Shortened One-Way Return Curve** at **(X8, Y12)**, both 0°.
9. Select **One-Way HSR L2 Eight-Metre Straight**. Place **P01BS (X6, Y6)** at **180°**, pointing south, and **P03DS (X8, Y6)** at **0°**, pointing north. These complete the two connections between the shortened curves and P02A; they are the same button in different rotations.
10. Extend compatible ordinary paired HSR beyond the west edge of X0, east edge of X19, and south edge of Y0. All three outside connections have their train path at **15.5 m**. Supply travel demand and test every journey below using separate Route Query and visible-train observations.

The selected pieces support proper **0°, 90°, 180° and 270°** rotations in their construction rules. Keyboard response, cursor anchors, terrain behaviour, and actual train operation still require human tests. Plop & Paint does not stamp this complete blueprint.

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

**Open demolition defect, reported 2026-10-23:** selecting one tile for demolition caused connected custom parts to appear as Monorail; disconnected copies remained unchanged in the original report. The user also confirmed a smaller reproduction: place three copies of `hsr-component-lower-paired-straight` end to end, delete the middle copy, and both connected survivors appear as Monorail. The disconnected control's outcome was not separately reported for this second test. The exact original deleted type, orientation, affected cells, and confirmed game environment remain unknown. The [scoped failure report](evidence/demolition-regression-20261023.json) binds the installed menu-trial context and retains both observations and their limits. Static comparison found all 165 installed piece archives and every construction definition unchanged from the pre-menu installation; it does not establish the runtime cause or a fix. Follow the [single-tile demolition regression procedure](../../../../docs/TESTING.md#investigate-single-tile-demolition-and-connected-survivors) in a disposable city. Existing whole-placement demolition, and save/reload observations do not cover this failure.

V4 game observations remain **unverified** unless the user has explicitly confirmed the exact case in this subject's own record. This cleanup changes no game observation. Use the [shared observation procedure](../../../../docs/TESTING.md) to record precise human results in `checks/manual-tests.json`; software checks cannot create those confirmations.

After installing an authorized test build, use a disposable flat city. Inspect P01AW/P01A and P03B/P03BE at every zoom, then P01B/P01BS and P03DS/P03D. Check rails, deck, wall openings, pillars, and shadows. Verify each piece's cursor placement and four rotations. Build the complete arrangement, supply real Monorail demand and check every journey with Route Query and moving trains. Also test forbidden U-turns and level transfers, demolition, and save/reload. Record the tested file hashes, city layout, platform, and screenshots with the observation.

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 82, passed: 2, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-fb989639955077c49383">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-fb989639955077c49383"></a>

**General: passed** — `software_resources-fb989639955077c49383`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:35.427083+00:00; evidence: [evidence/validation.json]; environment: 

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-fb989639955077c49383">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-fb989639955077c49383"></a>

**General: passed** — `software_connectivity-fb989639955077c49383`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:35.480326+00:00; evidence: [evidence/validation.json]; environment: 

</details>

</details>

<details>
<summary>Preview review — Images — 6 cases; unverified: 6</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:straight-stem-trumpet-v4:clean-southeast | <a href="#case-preview_review-48a60c2c64f3348b7b78">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:straight-stem-trumpet-v4:clean-top | <a href="#case-preview_review-aed7734e9ecffe26325e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:straight-stem-trumpet-v4:named-northwest | <a href="#case-preview_review-2561022812598330a304">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:straight-stem-trumpet-v4:named-southeast | <a href="#case-preview_review-6027b3b75397d93e4137">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:straight-stem-trumpet-v4:named-top | <a href="#case-preview_review-9a0709480b9933303c05">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:straight-stem-trumpet-v4:tile-ownership | <a href="#case-preview_review-82510a61f70ec0285a29">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:straight-stem-trumpet-v4:clean-southeast</summary>

<a id="case-preview_review-48a60c2c64f3348b7b78"></a>

**General: unverified** — `preview_review-48a60c2c64f3348b7b78`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:straight-stem-trumpet-v4:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet-v4:clean-top</summary>

<a id="case-preview_review-aed7734e9ecffe26325e"></a>

**General: unverified** — `preview_review-aed7734e9ecffe26325e`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:straight-stem-trumpet-v4:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet-v4:named-northwest</summary>

<a id="case-preview_review-2561022812598330a304"></a>

**General: unverified** — `preview_review-2561022812598330a304`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:straight-stem-trumpet-v4:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet-v4:named-southeast</summary>

<a id="case-preview_review-6027b3b75397d93e4137"></a>

**General: unverified** — `preview_review-6027b3b75397d93e4137`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:straight-stem-trumpet-v4:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet-v4:named-top</summary>

<a id="case-preview_review-9a0709480b9933303c05"></a>

**General: unverified** — `preview_review-9a0709480b9933303c05`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:straight-stem-trumpet-v4:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:straight-stem-trumpet-v4:tile-ownership</summary>

<a id="case-preview_review-82510a61f70ec0285a29"></a>

**General: unverified** — `preview_review-82510a61f70ec0285a29`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:straight-stem-trumpet-v4:tile-ownership.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-1e76dcd30aba7445f7fc">[ ] unverified</a> | <a href="#case-in_game_render-518c4dbebce97ad76311">[ ] unverified</a> | <a href="#case-in_game_render-649f56bd91694b9554eb">[ ] unverified</a> | <a href="#case-in_game_render-89d6c51534495032543c">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-1e76dcd30aba7445f7fc"></a>

**0° CCW: unverified** — `in_game_render-1e76dcd30aba7445f7fc`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-518c4dbebce97ad76311"></a>

**90° CCW: unverified** — `in_game_render-518c4dbebce97ad76311`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-649f56bd91694b9554eb"></a>

**180° CCW: unverified** — `in_game_render-649f56bd91694b9554eb`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-89d6c51534495032543c"></a>

**270° CCW: unverified** — `in_game_render-89d6c51534495032543c`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-1e76dcd30aba7445f7fc">[ ] unverified</a> | <a href="#case-in_game_placement-518c4dbebce97ad76311">[ ] unverified</a> | <a href="#case-in_game_placement-649f56bd91694b9554eb">[ ] unverified</a> | <a href="#case-in_game_placement-89d6c51534495032543c">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-1e76dcd30aba7445f7fc"></a>

**0° CCW: unverified** — `in_game_placement-1e76dcd30aba7445f7fc`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-518c4dbebce97ad76311"></a>

**90° CCW: unverified** — `in_game_placement-518c4dbebce97ad76311`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-649f56bd91694b9554eb"></a>

**180° CCW: unverified** — `in_game_placement-649f56bd91694b9554eb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-89d6c51534495032543c"></a>

**270° CCW: unverified** — `in_game_placement-89d6c51534495032543c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-1e76dcd30aba7445f7fc">[ ] unverified</a> | <a href="#case-in_game_demolition-518c4dbebce97ad76311">[ ] unverified</a> | <a href="#case-in_game_demolition-649f56bd91694b9554eb">[ ] unverified</a> | <a href="#case-in_game_demolition-89d6c51534495032543c">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-1e76dcd30aba7445f7fc"></a>

**0° CCW: unverified** — `in_game_demolition-1e76dcd30aba7445f7fc`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-518c4dbebce97ad76311"></a>

**90° CCW: unverified** — `in_game_demolition-518c4dbebce97ad76311`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-649f56bd91694b9554eb"></a>

**180° CCW: unverified** — `in_game_demolition-649f56bd91694b9554eb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-89d6c51534495032543c"></a>

**270° CCW: unverified** — `in_game_demolition-89d6c51534495032543c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-1e76dcd30aba7445f7fc">[ ] unverified</a> | <a href="#case-in_game_save_reload-518c4dbebce97ad76311">[ ] unverified</a> | <a href="#case-in_game_save_reload-649f56bd91694b9554eb">[ ] unverified</a> | <a href="#case-in_game_save_reload-89d6c51534495032543c">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-1e76dcd30aba7445f7fc"></a>

**0° CCW: unverified** — `in_game_save_reload-1e76dcd30aba7445f7fc`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-518c4dbebce97ad76311"></a>

**90° CCW: unverified** — `in_game_save_reload-518c4dbebce97ad76311`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-649f56bd91694b9554eb"></a>

**180° CCW: unverified** — `in_game_save_reload-649f56bd91694b9554eb`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-89d6c51534495032543c"></a>

**270° CCW: unverified** — `in_game_save_reload-89d6c51534495032543c`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out | — | <a href="#case-in_game_route_query-935025a1afa3ba78033c">[ ] unverified</a> | <a href="#case-in_game_route_query-1ee82534208d8f70e09d">[ ] unverified</a> | <a href="#case-in_game_route_query-0caeff944d5ce14b121a">[ ] unverified</a> | <a href="#case-in_game_route_query-31bc90bd7620f94ae1a6">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out | — | <a href="#case-in_game_route_query-cb6c5202c8347ebf1286">[ ] unverified</a> | <a href="#case-in_game_route_query-be7aeb2c407c297d108b">[ ] unverified</a> | <a href="#case-in_game_route_query-5164724d0550dce108e6">[ ] unverified</a> | <a href="#case-in_game_route_query-2e9cfce6a757c2ed9e6d">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out | — | <a href="#case-in_game_route_query-a1374cdd8955a931ef39">[ ] unverified</a> | <a href="#case-in_game_route_query-ac62407d1170449eb506">[ ] unverified</a> | <a href="#case-in_game_route_query-4b3853ea4130fced6221">[ ] unverified</a> | <a href="#case-in_game_route_query-2cd25f0ed0eef6fcbea2">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out | — | <a href="#case-in_game_route_query-335c3ad51bc94699c104">[ ] unverified</a> | <a href="#case-in_game_route_query-95ed5510528261ee7919">[ ] unverified</a> | <a href="#case-in_game_route_query-a890a2a60344a48cfc9f">[ ] unverified</a> | <a href="#case-in_game_route_query-2275d5d33b70a5c4be7a">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out | — | <a href="#case-in_game_route_query-9e719d3640b74327466a">[ ] unverified</a> | <a href="#case-in_game_route_query-91bbdaf46b97bf59077b">[ ] unverified</a> | <a href="#case-in_game_route_query-98fd30b2f6f7ecfc6cf4">[ ] unverified</a> | <a href="#case-in_game_route_query-1b00be14960ac960943b">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out | — | <a href="#case-in_game_route_query-897ffbf0df74d5c6e5a4">[ ] unverified</a> | <a href="#case-in_game_route_query-911cda600a9e22f7b926">[ ] unverified</a> | <a href="#case-in_game_route_query-c79a5264d21ee222bcb0">[ ] unverified</a> | <a href="#case-in_game_route_query-7db79214c123c3231bb6">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out</summary>

<a id="case-in_game_route_query-935025a1afa3ba78033c"></a>

**0° CCW: unverified** — `in_game_route_query-935025a1afa3ba78033c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_route_query-1ee82534208d8f70e09d"></a>

**90° CCW: unverified** — `in_game_route_query-1ee82534208d8f70e09d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_route_query-0caeff944d5ce14b121a"></a>

**180° CCW: unverified** — `in_game_route_query-0caeff944d5ce14b121a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_route_query-31bc90bd7620f94ae1a6"></a>

**270° CCW: unverified** — `in_game_route_query-31bc90bd7620f94ae1a6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out</summary>

<a id="case-in_game_route_query-cb6c5202c8347ebf1286"></a>

**0° CCW: unverified** — `in_game_route_query-cb6c5202c8347ebf1286`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_route_query-be7aeb2c407c297d108b"></a>

**90° CCW: unverified** — `in_game_route_query-be7aeb2c407c297d108b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_route_query-5164724d0550dce108e6"></a>

**180° CCW: unverified** — `in_game_route_query-5164724d0550dce108e6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_route_query-2e9cfce6a757c2ed9e6d"></a>

**270° CCW: unverified** — `in_game_route_query-2e9cfce6a757c2ed9e6d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out</summary>

<a id="case-in_game_route_query-a1374cdd8955a931ef39"></a>

**0° CCW: unverified** — `in_game_route_query-a1374cdd8955a931ef39`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_route_query-ac62407d1170449eb506"></a>

**90° CCW: unverified** — `in_game_route_query-ac62407d1170449eb506`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_route_query-4b3853ea4130fced6221"></a>

**180° CCW: unverified** — `in_game_route_query-4b3853ea4130fced6221`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_route_query-2cd25f0ed0eef6fcbea2"></a>

**270° CCW: unverified** — `in_game_route_query-2cd25f0ed0eef6fcbea2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out</summary>

<a id="case-in_game_route_query-335c3ad51bc94699c104"></a>

**0° CCW: unverified** — `in_game_route_query-335c3ad51bc94699c104`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_route_query-95ed5510528261ee7919"></a>

**90° CCW: unverified** — `in_game_route_query-95ed5510528261ee7919`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_route_query-a890a2a60344a48cfc9f"></a>

**180° CCW: unverified** — `in_game_route_query-a890a2a60344a48cfc9f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_route_query-2275d5d33b70a5c4be7a"></a>

**270° CCW: unverified** — `in_game_route_query-2275d5d33b70a5c4be7a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out</summary>

<a id="case-in_game_route_query-9e719d3640b74327466a"></a>

**0° CCW: unverified** — `in_game_route_query-9e719d3640b74327466a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_route_query-91bbdaf46b97bf59077b"></a>

**90° CCW: unverified** — `in_game_route_query-91bbdaf46b97bf59077b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_route_query-98fd30b2f6f7ecfc6cf4"></a>

**180° CCW: unverified** — `in_game_route_query-98fd30b2f6f7ecfc6cf4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_route_query-1b00be14960ac960943b"></a>

**270° CCW: unverified** — `in_game_route_query-1b00be14960ac960943b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out</summary>

<a id="case-in_game_route_query-897ffbf0df74d5c6e5a4"></a>

**0° CCW: unverified** — `in_game_route_query-897ffbf0df74d5c6e5a4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_route_query-911cda600a9e22f7b926"></a>

**90° CCW: unverified** — `in_game_route_query-911cda600a9e22f7b926`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_route_query-c79a5264d21ee222bcb0"></a>

**180° CCW: unverified** — `in_game_route_query-c79a5264d21ee222bcb0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_route_query-7db79214c123c3231bb6"></a>

**270° CCW: unverified** — `in_game_route_query-7db79214c123c3231bb6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out | — | <a href="#case-in_game_visible_travel-935025a1afa3ba78033c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1ee82534208d8f70e09d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0caeff944d5ce14b121a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-31bc90bd7620f94ae1a6">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out | — | <a href="#case-in_game_visible_travel-cb6c5202c8347ebf1286">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be7aeb2c407c297d108b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5164724d0550dce108e6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2e9cfce6a757c2ed9e6d">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out | — | <a href="#case-in_game_visible_travel-a1374cdd8955a931ef39">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ac62407d1170449eb506">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4b3853ea4130fced6221">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2cd25f0ed0eef6fcbea2">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out | — | <a href="#case-in_game_visible_travel-335c3ad51bc94699c104">[ ] unverified</a> | <a href="#case-in_game_visible_travel-95ed5510528261ee7919">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a890a2a60344a48cfc9f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2275d5d33b70a5c4be7a">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out | — | <a href="#case-in_game_visible_travel-9e719d3640b74327466a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-91bbdaf46b97bf59077b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-98fd30b2f6f7ecfc6cf4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1b00be14960ac960943b">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out | — | <a href="#case-in_game_visible_travel-897ffbf0df74d5c6e5a4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-911cda600a9e22f7b926">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c79a5264d21ee222bcb0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7db79214c123c3231bb6">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out</summary>

<a id="case-in_game_visible_travel-935025a1afa3ba78033c"></a>

**0° CCW: unverified** — `in_game_visible_travel-935025a1afa3ba78033c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_visible_travel-1ee82534208d8f70e09d"></a>

**90° CCW: unverified** — `in_game_visible_travel-1ee82534208d8f70e09d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_visible_travel-0caeff944d5ce14b121a"></a>

**180° CCW: unverified** — `in_game_visible_travel-0caeff944d5ce14b121a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_visible_travel-31bc90bd7620f94ae1a6"></a>

**270° CCW: unverified** — `in_game_visible_travel-31bc90bd7620f94ae1a6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out</summary>

<a id="case-in_game_visible_travel-cb6c5202c8347ebf1286"></a>

**0° CCW: unverified** — `in_game_visible_travel-cb6c5202c8347ebf1286`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_visible_travel-be7aeb2c407c297d108b"></a>

**90° CCW: unverified** — `in_game_visible_travel-be7aeb2c407c297d108b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_visible_travel-5164724d0550dce108e6"></a>

**180° CCW: unverified** — `in_game_visible_travel-5164724d0550dce108e6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_visible_travel-2e9cfce6a757c2ed9e6d"></a>

**270° CCW: unverified** — `in_game_visible_travel-2e9cfce6a757c2ed9e6d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out</summary>

<a id="case-in_game_visible_travel-a1374cdd8955a931ef39"></a>

**0° CCW: unverified** — `in_game_visible_travel-a1374cdd8955a931ef39`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_visible_travel-ac62407d1170449eb506"></a>

**90° CCW: unverified** — `in_game_visible_travel-ac62407d1170449eb506`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_visible_travel-4b3853ea4130fced6221"></a>

**180° CCW: unverified** — `in_game_visible_travel-4b3853ea4130fced6221`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_visible_travel-2cd25f0ed0eef6fcbea2"></a>

**270° CCW: unverified** — `in_game_visible_travel-2cd25f0ed0eef6fcbea2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out</summary>

<a id="case-in_game_visible_travel-335c3ad51bc94699c104"></a>

**0° CCW: unverified** — `in_game_visible_travel-335c3ad51bc94699c104`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_visible_travel-95ed5510528261ee7919"></a>

**90° CCW: unverified** — `in_game_visible_travel-95ed5510528261ee7919`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_visible_travel-a890a2a60344a48cfc9f"></a>

**180° CCW: unverified** — `in_game_visible_travel-a890a2a60344a48cfc9f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_visible_travel-2275d5d33b70a5c4be7a"></a>

**270° CCW: unverified** — `in_game_visible_travel-2275d5d33b70a5c4be7a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out</summary>

<a id="case-in_game_visible_travel-9e719d3640b74327466a"></a>

**0° CCW: unverified** — `in_game_visible_travel-9e719d3640b74327466a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_visible_travel-91bbdaf46b97bf59077b"></a>

**90° CCW: unverified** — `in_game_visible_travel-91bbdaf46b97bf59077b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_visible_travel-98fd30b2f6f7ecfc6cf4"></a>

**180° CCW: unverified** — `in_game_visible_travel-98fd30b2f6f7ecfc6cf4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_visible_travel-1b00be14960ac960943b"></a>

**270° CCW: unverified** — `in_game_visible_travel-1b00be14960ac960943b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out</summary>

<a id="case-in_game_visible_travel-897ffbf0df74d5c6e5a4"></a>

**0° CCW: unverified** — `in_game_visible_travel-897ffbf0df74d5c6e5a4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_visible_travel-911cda600a9e22f7b926"></a>

**90° CCW: unverified** — `in_game_visible_travel-911cda600a9e22f7b926`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_visible_travel-c79a5264d21ee222bcb0"></a>

**180° CCW: unverified** — `in_game_visible_travel-c79a5264d21ee222bcb0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_visible_travel-7db79214c123c3231bb6"></a>

**270° CCW: unverified** — `in_game_visible_travel-7db79214c123c3231bb6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph | — | <a href="#case-in_game_forbidden_transfer-5e7720c782995408fbd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34fff7e1a9eb422d6c3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4aa09b1528b4104521da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9424da48468a67a34bad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph | — | <a href="#case-in_game_forbidden_transfer-0e614229b03bfe5c1e73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1812b2006304b7c72221">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6789463f81e846e26420">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3af56e2b16b90cab12e7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph | — | <a href="#case-in_game_forbidden_transfer-6f8a97ec7efb05be09c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48dc00a5d1e0c6231374">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d349a9a65ad8f06fa73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d54eefd540d1a8c6693">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph</summary>

<a id="case-in_game_forbidden_transfer-5e7720c782995408fbd3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5e7720c782995408fbd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34fff7e1a9eb422d6c3d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-34fff7e1a9eb422d6c3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4aa09b1528b4104521da"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4aa09b1528b4104521da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9424da48468a67a34bad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9424da48468a67a34bad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: W.in; to port: W.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph</summary>

<a id="case-in_game_forbidden_transfer-0e614229b03bfe5c1e73"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e614229b03bfe5c1e73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1812b2006304b7c72221"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1812b2006304b7c72221`.

Confirm this undeclared transfer is unavailable.

Scope: from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6789463f81e846e26420"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6789463f81e846e26420`.

Confirm this undeclared transfer is unavailable.

Scope: from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3af56e2b16b90cab12e7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3af56e2b16b90cab12e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: S.in; to port: S.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph</summary>

<a id="case-in_game_forbidden_transfer-6f8a97ec7efb05be09c5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6f8a97ec7efb05be09c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48dc00a5d1e0c6231374"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48dc00a5d1e0c6231374`.

Confirm this undeclared transfer is unavailable.

Scope: from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d349a9a65ad8f06fa73"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d349a9a65ad8f06fa73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d54eefd540d1a8c6693"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d54eefd540d1a8c6693`.

Confirm this undeclared transfer is unavailable.

Scope: from port: E.in; to port: E.out; from service: hsr; to service: hsr; basis: not reachable in actual saved assembly graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

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
