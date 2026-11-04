---
title: "Testing: RHW Ramp — Upper Full Exit Ramp — R40"
summary: "Check this exact component's traffic ownership, complete physical geometry, and scoped game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — Upper Full Exit Ramp — R40

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-upper-exit-r40` resources and the matching complete [assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). This upper ramp has two traffic ports and one intrinsic journey between them. Its complete visible high throat can still overhang highway-owned tiles. Traffic follows the saved tile boundaries, while the physical model meets the highway at its flat native-edge cut.

A **PATH** is a saved traffic-route resource, and an **S3D** is the visible model made from indexed triangles. Model faces can extend beyond the tiles that store this piece's PATHs. A flat physical cut at the native highway edge is different from the traffic connection at a city-tile edge. Check both, rather than assuming that one card describes the entire physical opening.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-in-1` | road / 1 / primary | in | [8.0, -14.669671, 15.0]; [0.9174352085386687, 0.3978852072314444]; 0.0 | `path-interface-af2fee3a7996f5d5dde1` |
| `1-E-out-2` | road / 1 / primary | out | [72.0, -3.768542, 0.0]; [1.0, 0.0]; 0.0 | `path-interface-0aa85c099c852f580fff` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-1` → `1-E-out-2` | primary |

#### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including Wine or CrossOver. Follow the [shared build guide](../../../../docs/BUILD_AND_INSTALL.md) for exact dependency hashes and the captured Avenue input. Build the `ddrhw-modular-ramp-kit` set, and prepare the `modular-diagonal-diamond` Highways menu. Building and rendering do not install game files. Use flat terrain in a disposable city, and follow the [piece placement instructions](README.md#2-piece-and-placement).

The R40 assembly button cycles seven R40 components. The separate Compact Modular button selects the shared stamp, four full compact ramps, and two compact Avenue junctions. To replace one side of the R40 plan, swap its two ramps and terminal as a group.

## 3. Software checks

Follow the [assembly software commands](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#3-software-checks), including `python3 -B tools/run_tests.py` from the repository root and verification of the selected saved build. The focused family tests check exclusive construction ownership, exact retained high samples, signed slopes, the new R40 sections, the four flat R40 ground ports, and continuous texture phase. The face-partition tests specifically keep a centre pier when its old concrete mesh also contains a curved barrier bridge.

The [independent partition proof](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/evidence/straight-partition-preservation.json) compares complete assembled indexed triangles, original material bytes, UVs, winding, and per-cell PATH bytes against the immutable accepted checkpoint. Re-anchored faces use exactly one float32 translation from their old cell to their new host. The [reviewed model contract](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/straight-partition-models.jsonc) binds each resulting saved model; it does not approve game behaviour.

For physical joins, compare the complete pavement, 1 m underside, Jersey profiles, and inset bridge strips at the native highway edge. For traffic, compare every exposed tile-edge port, including all four ports of each lower full ramp. Standalone model overhang is deliberate; continuous route support must be checked against the assembled model union.

## 4. Game checks

Place this component in the complete matching assembly. Inspect the placed result after clicking, including rotations, barriers, pavement, supports, and shadows; the construction preview is a separate observation. Use Route Query on every required movement, watch a car complete it, confirm the opposite-carriageway ramp movements remain unavailable, save the city, close it, and reload it. Test the lower ramps through both intrinsic fragments and their stamp-owned middle tile.

For the stamp and Avenue terminals, extend an ordinary Avenue, develop nearby zoning, and inspect whether pedestrian pavement appears and rotates with the road. Check both pedestrian directions separately. Record only the exact service, direction, pose, and environment actually observed, following the [shared testing procedure](../../../../docs/TESTING.md).

## 5. Results and known issues

The independent partition audit passed its source-preservation comparison. That result is separate from verification of a newly saved DAT and from every human game observation in the generated checklist. The full retained high-prefix traffic centre-lines contain sampled transition minima of approximately 1.735 m on the lower ramps and 3.500 m on the upper ramps. These inherited kinks are preserved by the exact source partition; R40 describes only the new circular sections. The 30% maximum grade is a compact game experiment, rather than a normal real-world highway design limit. Every game result for these corrected resources remains unverified until an explicit matching observation is recorded.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/4 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 29, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-upper-exit-r40/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-upper-exit-r40/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-073d0cba29ded649065d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-073d0cba29ded649065d"></a>

**General: unverified** — `software_resources-073d0cba29ded649065d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-073d0cba29ded649065d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-073d0cba29ded649065d"></a>

**General: unverified** — `software_connectivity-073d0cba29ded649065d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-a35433541f4b1199f950">[ ] unverified</a> | <a href="#case-in_game_render-0f82976c3c4c2cebce77">[ ] unverified</a> | <a href="#case-in_game_render-88b4d7bd4d6b3a69d615">[ ] unverified</a> | <a href="#case-in_game_render-0377dcaf157d4b3a7cca">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-a35433541f4b1199f950"></a>

**0° CCW: unverified** — `in_game_render-a35433541f4b1199f950`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0f82976c3c4c2cebce77"></a>

**90° CCW: unverified** — `in_game_render-0f82976c3c4c2cebce77`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-88b4d7bd4d6b3a69d615"></a>

**180° CCW: unverified** — `in_game_render-88b4d7bd4d6b3a69d615`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0377dcaf157d4b3a7cca"></a>

**270° CCW: unverified** — `in_game_render-0377dcaf157d4b3a7cca`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-a35433541f4b1199f950">[ ] unverified</a> | <a href="#case-in_game_placement-0f82976c3c4c2cebce77">[ ] unverified</a> | <a href="#case-in_game_placement-88b4d7bd4d6b3a69d615">[ ] unverified</a> | <a href="#case-in_game_placement-0377dcaf157d4b3a7cca">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-a35433541f4b1199f950"></a>

**0° CCW: unverified** — `in_game_placement-a35433541f4b1199f950`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0f82976c3c4c2cebce77"></a>

**90° CCW: unverified** — `in_game_placement-0f82976c3c4c2cebce77`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-88b4d7bd4d6b3a69d615"></a>

**180° CCW: unverified** — `in_game_placement-88b4d7bd4d6b3a69d615`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0377dcaf157d4b3a7cca"></a>

**270° CCW: unverified** — `in_game_placement-0377dcaf157d4b3a7cca`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-a35433541f4b1199f950">[ ] unverified</a> | <a href="#case-in_game_demolition-0f82976c3c4c2cebce77">[ ] unverified</a> | <a href="#case-in_game_demolition-88b4d7bd4d6b3a69d615">[ ] unverified</a> | <a href="#case-in_game_demolition-0377dcaf157d4b3a7cca">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-a35433541f4b1199f950"></a>

**0° CCW: unverified** — `in_game_demolition-a35433541f4b1199f950`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0f82976c3c4c2cebce77"></a>

**90° CCW: unverified** — `in_game_demolition-0f82976c3c4c2cebce77`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-88b4d7bd4d6b3a69d615"></a>

**180° CCW: unverified** — `in_game_demolition-88b4d7bd4d6b3a69d615`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0377dcaf157d4b3a7cca"></a>

**270° CCW: unverified** — `in_game_demolition-0377dcaf157d4b3a7cca`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-a35433541f4b1199f950">[ ] unverified</a> | <a href="#case-in_game_save_reload-0f82976c3c4c2cebce77">[ ] unverified</a> | <a href="#case-in_game_save_reload-88b4d7bd4d6b3a69d615">[ ] unverified</a> | <a href="#case-in_game_save_reload-0377dcaf157d4b3a7cca">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-a35433541f4b1199f950"></a>

**0° CCW: unverified** — `in_game_save_reload-a35433541f4b1199f950`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0f82976c3c4c2cebce77"></a>

**90° CCW: unverified** — `in_game_save_reload-0f82976c3c4c2cebce77`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-88b4d7bd4d6b3a69d615"></a>

**180° CCW: unverified** — `in_game_save_reload-88b4d7bd4d6b3a69d615`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0377dcaf157d4b3a7cca"></a>

**270° CCW: unverified** — `in_game_save_reload-0377dcaf157d4b3a7cca`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2 | — | <a href="#case-in_game_route_query-49d1378e854bc61b99fa">[ ] unverified</a> | <a href="#case-in_game_route_query-955cb14a2fda5ca60c03">[ ] unverified</a> | <a href="#case-in_game_route_query-735afa1ea36f4d99f48d">[ ] unverified</a> | <a href="#case-in_game_route_query-18005f7c57177de59edf">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2</summary>

<a id="case-in_game_route_query-49d1378e854bc61b99fa"></a>

**0° CCW: unverified** — `in_game_route_query-49d1378e854bc61b99fa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2.

No observation recorded.

<a id="case-in_game_route_query-955cb14a2fda5ca60c03"></a>

**90° CCW: unverified** — `in_game_route_query-955cb14a2fda5ca60c03`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2.

No observation recorded.

<a id="case-in_game_route_query-735afa1ea36f4d99f48d"></a>

**180° CCW: unverified** — `in_game_route_query-735afa1ea36f4d99f48d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2.

No observation recorded.

<a id="case-in_game_route_query-18005f7c57177de59edf"></a>

**270° CCW: unverified** — `in_game_route_query-18005f7c57177de59edf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2 | — | <a href="#case-in_game_visible_travel-49d1378e854bc61b99fa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-955cb14a2fda5ca60c03">[ ] unverified</a> | <a href="#case-in_game_visible_travel-735afa1ea36f4d99f48d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-18005f7c57177de59edf">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2</summary>

<a id="case-in_game_visible_travel-49d1378e854bc61b99fa"></a>

**0° CCW: unverified** — `in_game_visible_travel-49d1378e854bc61b99fa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-955cb14a2fda5ca60c03"></a>

**90° CCW: unverified** — `in_game_visible_travel-955cb14a2fda5ca60c03`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-735afa1ea36f4d99f48d"></a>

**180° CCW: unverified** — `in_game_visible_travel-735afa1ea36f4d99f48d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-18005f7c57177de59edf"></a>

**270° CCW: unverified** — `in_game_visible_travel-18005f7c57177de59edf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-2; entry: 1-W-in-1; exit: 1-E-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-upper-exit-r40:canonical-southeast | <a href="#case-preview_review-0a0a88e4078f6771905a">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-upper-exit-r40:canonical-top | <a href="#case-preview_review-3f58e902fcd77fe85753">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-upper-exit-r40:connection-overview | <a href="#case-preview_review-885f5084ce77aeff56f8">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-exit-r40:canonical-southeast</summary>

<a id="case-preview_review-0a0a88e4078f6771905a"></a>

**General: unverified** — `preview_review-0a0a88e4078f6771905a`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-exit-r40:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-exit-r40:canonical-top</summary>

<a id="case-preview_review-3f58e902fcd77fe85753"></a>

**General: unverified** — `preview_review-3f58e902fcd77fe85753`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-exit-r40:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-exit-r40:connection-overview</summary>

<a id="case-preview_review-885f5084ce77aeff56f8"></a>

**General: unverified** — `preview_review-885f5084ce77aeff56f8`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-exit-r40:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The previous experimental stamp included curved branch throats and six extra wing cells. The corrected partition keeps a straight 21-cell stamp, transfers those six construction cells to full ramp owners, and moves all curved high-throat faces into the separately placed ramps. The independent partition audit preserves assembled geometry, UVs, materials, winding, and traffic routes, subject only to the exact float32 re-encoding required by a changed model anchor. Earlier renders and game observations do not approve this corrected ownership split.
