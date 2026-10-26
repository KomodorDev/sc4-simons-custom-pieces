---
title: "Straight-stem HSR trumpet V4: testing and decisions"
summary: "Explain the current V4 resource contract, retain the historical atomization rationale and distinguish software checks from human game observations."
audience: "Testers, assembly authors, and maintainers"
document_type: "reference"
---

# Straight-stem HSR trumpet V4: testing and decisions

[Building guide](README.md) · [Current resource contract](checks/resources.json) · [Decision history](checks/atomization.json) · [Quality contract](checks/contract.json) · [Layout contract](checks/layout.json) · [Shared observation procedure](../../../../docs/TESTING.md)

## Accepted and retained candidates

**Atomization** means separating a larger piece into smaller useful modules. The historical candidate threshold was **strictly below 5 mm of original lateral deviation**. It selected a tail for investigation; it did not prove that its deck, wall openings or supports could be replaced. The actual corrections in adjoining retained tiles had separate bounds: **24.5 mm** for paired junctions and **8.2 mm** for one-way curves. A **millimetre** is 0.001 m. The recorded eligibility measurements and correction bounds remain distinct.

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

## Current independent acceptance scope

A **PATH** describes train movement. An **S3D model** contains visible triangles. A **DAT archive** packages those game resources. A **fingerprint** is a hash of exact file bytes; it detects any change in the approved resources.

The schema-3 [current resource contract](checks/resources.json) pins all **14 current piece DATs**, their identities, recipes, sizes, resource counts and hashes. It also pins the models, PATHs and shadows of all **109 placed tiles**, their owning pieces and rotations, all six complete directed journeys, the fixed layout and the historical decision content. Verification reads the current staged build and compares these exact approved fingerprints before performing independent physical and routing checks. No deleted predecessor archive, source folder or private historical fixture is required.

The earlier redesign was limited to eight world tiles: **(X0–X1, Y13)** and **(X13–X14, Y13)** for paired tails and joining collars; **(X6, Y6–Y7)** and **(X8, Y6–Y7)** for one-way tails and joining collars. The ledger preserves its measured movement and bounds as history. This cleanup authorizes no geometry changes: the current fingerprint contract protects **all 109 tiles**, including those eight, and the four extracted placements still use the existing standard straight types at their specified rotations. Each current type generates its geometry from its own retained source.

The placement contract requires **26 placements, 14 types, 109 occupied tiles and 75 support centres**, at least **16 m** apart. Outside ports, the **20 × 23 tile** construction rectangle and fixed X/Y grid are unchanged. All six HSR journeys must pass every proper rotation, with no U-turn or unintended level transfer. Full native bed, underside and parapet sections are checked at the four exposed ordinary connections. Keeping an inherited interface byte-identical does not establish that every visual detail at that interface has been redesigned.

The verifier also checks full **5 m** train corridors, native visible rails, deck intersections, pillar contacts, separate tile ownership, all five model/shadow zooms and construction rotation lists. Existing per-module minimum radius is **24 m**, curvature-change limit **0.0015 per square metre**, and native-end curvature limit **0.0005 per metre**. The two direct-slip journeys receive additional end-to-end checks. The other four journeys are pinned to their exact approved current geometry and retain the constituent modules' independent contracts; this does not impose a new whole-journey curvature threshold on the loop.

## Inherited interface checks and limits

The four ordinary connections receive full native slab, underside and parapet checks. P03B's western interface retains its approved model bytes, including an inherited incomplete outer parapet-cap section. Its train corridor and neighbouring geometry remain checked; this cleanup does not repair that separate visual detail.

The two shortened one-way curves retain their custom-end tiles. Their standalone rail audit allows a narrowly limited **2.65 m cut depth**, tied to the exact approved port-tile model hashes at all five zooms. This accounts for a rail strip crossing the artificial standalone cut. It neither widens the allowed rail strip nor permits stray rails inside the piece. The complete-assembly audit uses actual neighbouring models and uncut routes, with no artificial end cap. Mutation tests reject changed port hashes, excessive depth or width, and interior stray rails.

The historical mesh comparison measured the **sum of changed cross-section intervals**, not one track's movement. Two parapet strips have four interval edges, giving a one-way bound of **4 × (8.2 mm route bound + 0.05 mm section precision) = 33 mm** in total, with each edge checked independently. That did not permit a 33 mm route shift: the route bound was **8.2 mm**. The current contract now pins the approved result exactly instead of requiring the deleted comparison inputs.

## Software verification

The approved saved assembly contains **109 occupied tiles, 659,271 triangles, 167 encoded route fragments and 75 pillars**, with minimum **16 m** spacing. See the [current validation](evidence/validation.json), [executed test results and logs](evidence/test-results.json), [build provenance](evidence/build-provenance.json) and [preservation audit](evidence/preservation.json) for exact input fingerprints, current checks, suite counts and any skips. The [implementation record](evidence/atomization-implementation.json) preserves the earlier measured redesign rationale. No software result marks a human observation as passed.

From the project folder containing `custom-pieces`, run:

```sh
python3 custom-pieces/scp.py build --set hsr-straight-stem-trumpet-v4 --output custom-pieces/dist/straight-stem-trumpet-v4 --progress
python3 custom-pieces/scp.py verify --output custom-pieces/dist/straight-stem-trumpet-v4
python3 custom-pieces/domains/high-speed-rail/tools/verify_hsr_trumpet_v4.py --build custom-pieces/dist/straight-stem-trumpet-v4 --scene custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/assembly.json --output custom-pieces/domains/high-speed-rail/01_assemblies/straight-stem-trumpet-v4/evidence/validation.json
python3 custom-pieces/scp.py check --scope straight-stem-trumpet-v4
```

The validation report identifies the [exact manifest snapshot at audit time](evidence/audited-build-manifest.json). Documentation-only export metadata may change later; the approved DAT bytes remain pinned independently. A missing current descriptor, missing required staged build or changed resource fails verification. Optional integration tests may explicitly skip an absent current build; they must not hide malformed present builds or substitute generated expected answers.

The six assembly views and current standalone piece pictures retain their existing bytes. Updating documentation, packaging or the verification schema does not require rerendering or moving any track, support, placement or image caption. No smaller overall rectangle is claimed; the original gain was four ordinary straight placements and four smaller reusable cores inside the unchanged footprint.

## Game testing

**Open demolition defect, reported 2026-10-23:** selecting one tile for demolition caused connected custom parts to appear as Monorail; disconnected copies remained unchanged in the original report. The user also confirmed a smaller reproduction: place three copies of `hsr-component-lower-paired-straight` end to end, delete the middle copy, and both connected survivors appear as Monorail. The disconnected control's outcome was not separately reported for this second test. The exact original deleted type, orientation, affected cells, and confirmed game environment remain unknown. The [scoped failure report](evidence/demolition-regression-20261023.json) binds the installed menu-trial context and retains both observations and their limits. Static comparison found all 165 installed piece archives and every construction definition unchanged from the pre-menu installation; it does not establish the runtime cause or a fix. Follow the [single-tile demolition regression procedure](../../../../docs/TESTING.md#investigate-single-tile-demolition-and-connected-survivors) in a disposable city. Existing whole-placement demolition and save/reload observations do not cover this failure.

V4 game observations remain **unverified** unless the user has explicitly confirmed the exact case in this subject's own record. This cleanup changes no game observation. Use the [shared observation procedure](../../../../docs/TESTING.md) to record precise human results in `checks/manual-tests.json`; software checks cannot create those confirmations.

After installing an authorized test build, use a disposable flat city. Inspect P01AW/P01A and P03B/P03BE at every zoom, then P01B/P01BS and P03DS/P03D. Check rails, deck, wall openings, pillars and shadows. Verify each piece's cursor placement and four rotations. Build the complete arrangement, supply real Monorail demand and check every journey with Route Query and moving trains. Also test forbidden U-turns and level transfers, demolition and save/reload. Record the tested file hashes, city layout, platform and screenshots with the observation.

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 58, passed: 2, failed: 0, stale: 0, not_applicable: 0.

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
<summary>Journey — hsr — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out | — | <a href="#case-in_game_journey-935025a1afa3ba78033c">[ ] unverified</a> | <a href="#case-in_game_journey-1ee82534208d8f70e09d">[ ] unverified</a> | <a href="#case-in_game_journey-0caeff944d5ce14b121a">[ ] unverified</a> | <a href="#case-in_game_journey-31bc90bd7620f94ae1a6">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out | — | <a href="#case-in_game_journey-cb6c5202c8347ebf1286">[ ] unverified</a> | <a href="#case-in_game_journey-be7aeb2c407c297d108b">[ ] unverified</a> | <a href="#case-in_game_journey-5164724d0550dce108e6">[ ] unverified</a> | <a href="#case-in_game_journey-2e9cfce6a757c2ed9e6d">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out | — | <a href="#case-in_game_journey-a1374cdd8955a931ef39">[ ] unverified</a> | <a href="#case-in_game_journey-ac62407d1170449eb506">[ ] unverified</a> | <a href="#case-in_game_journey-4b3853ea4130fced6221">[ ] unverified</a> | <a href="#case-in_game_journey-2cd25f0ed0eef6fcbea2">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out | — | <a href="#case-in_game_journey-335c3ad51bc94699c104">[ ] unverified</a> | <a href="#case-in_game_journey-95ed5510528261ee7919">[ ] unverified</a> | <a href="#case-in_game_journey-a890a2a60344a48cfc9f">[ ] unverified</a> | <a href="#case-in_game_journey-2275d5d33b70a5c4be7a">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out | — | <a href="#case-in_game_journey-9e719d3640b74327466a">[ ] unverified</a> | <a href="#case-in_game_journey-91bbdaf46b97bf59077b">[ ] unverified</a> | <a href="#case-in_game_journey-98fd30b2f6f7ecfc6cf4">[ ] unverified</a> | <a href="#case-in_game_journey-1b00be14960ac960943b">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out | — | <a href="#case-in_game_journey-897ffbf0df74d5c6e5a4">[ ] unverified</a> | <a href="#case-in_game_journey-911cda600a9e22f7b926">[ ] unverified</a> | <a href="#case-in_game_journey-c79a5264d21ee222bcb0">[ ] unverified</a> | <a href="#case-in_game_journey-7db79214c123c3231bb6">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out</summary>

<a id="case-in_game_journey-935025a1afa3ba78033c"></a>

**0° CCW: unverified** — `in_game_journey-935025a1afa3ba78033c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_journey-1ee82534208d8f70e09d"></a>

**90° CCW: unverified** — `in_game_journey-1ee82534208d8f70e09d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_journey-0caeff944d5ce14b121a"></a>

**180° CCW: unverified** — `in_game_journey-0caeff944d5ce14b121a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

<a id="case-in_game_journey-31bc90bd7620f94ae1a6"></a>

**270° CCW: unverified** — `in_game_journey-31bc90bd7620f94ae1a6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: W.in>E.out; entry: W.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out</summary>

<a id="case-in_game_journey-cb6c5202c8347ebf1286"></a>

**0° CCW: unverified** — `in_game_journey-cb6c5202c8347ebf1286`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_journey-be7aeb2c407c297d108b"></a>

**90° CCW: unverified** — `in_game_journey-be7aeb2c407c297d108b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_journey-5164724d0550dce108e6"></a>

**180° CCW: unverified** — `in_game_journey-5164724d0550dce108e6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

<a id="case-in_game_journey-2e9cfce6a757c2ed9e6d"></a>

**270° CCW: unverified** — `in_game_journey-2e9cfce6a757c2ed9e6d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: W.in>S.out; entry: W.in; exit: S.out.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out</summary>

<a id="case-in_game_journey-a1374cdd8955a931ef39"></a>

**0° CCW: unverified** — `in_game_journey-a1374cdd8955a931ef39`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_journey-ac62407d1170449eb506"></a>

**90° CCW: unverified** — `in_game_journey-ac62407d1170449eb506`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_journey-4b3853ea4130fced6221"></a>

**180° CCW: unverified** — `in_game_journey-4b3853ea4130fced6221`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

<a id="case-in_game_journey-2cd25f0ed0eef6fcbea2"></a>

**270° CCW: unverified** — `in_game_journey-2cd25f0ed0eef6fcbea2`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: S.in>E.out; entry: S.in; exit: E.out.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out</summary>

<a id="case-in_game_journey-335c3ad51bc94699c104"></a>

**0° CCW: unverified** — `in_game_journey-335c3ad51bc94699c104`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_journey-95ed5510528261ee7919"></a>

**90° CCW: unverified** — `in_game_journey-95ed5510528261ee7919`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_journey-a890a2a60344a48cfc9f"></a>

**180° CCW: unverified** — `in_game_journey-a890a2a60344a48cfc9f`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

<a id="case-in_game_journey-2275d5d33b70a5c4be7a"></a>

**270° CCW: unverified** — `in_game_journey-2275d5d33b70a5c4be7a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: S.in>W.out; entry: S.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out</summary>

<a id="case-in_game_journey-9e719d3640b74327466a"></a>

**0° CCW: unverified** — `in_game_journey-9e719d3640b74327466a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_journey-91bbdaf46b97bf59077b"></a>

**90° CCW: unverified** — `in_game_journey-91bbdaf46b97bf59077b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_journey-98fd30b2f6f7ecfc6cf4"></a>

**180° CCW: unverified** — `in_game_journey-98fd30b2f6f7ecfc6cf4`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

<a id="case-in_game_journey-1b00be14960ac960943b"></a>

**270° CCW: unverified** — `in_game_journey-1b00be14960ac960943b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: E.in>W.out; entry: E.in; exit: W.out.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out</summary>

<a id="case-in_game_journey-897ffbf0df74d5c6e5a4"></a>

**0° CCW: unverified** — `in_game_journey-897ffbf0df74d5c6e5a4`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_journey-911cda600a9e22f7b926"></a>

**90° CCW: unverified** — `in_game_journey-911cda600a9e22f7b926`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_journey-c79a5264d21ee222bcb0"></a>

**180° CCW: unverified** — `in_game_journey-c79a5264d21ee222bcb0`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: E.in>S.out; entry: E.in; exit: S.out.

No observation recorded.

<a id="case-in_game_journey-7db79214c123c3231bb6"></a>

**270° CCW: unverified** — `in_game_journey-7db79214c123c3231bb6`.

Run the declared journey in this direction using its service network.

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
