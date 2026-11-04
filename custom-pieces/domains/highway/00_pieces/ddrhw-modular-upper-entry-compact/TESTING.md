---
title: "Testing: RHW Ramp — Upper Full Entry Ramp — Compact"
summary: "Check this exact component's traffic ownership, complete physical geometry, and scoped game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — Upper Full Entry Ramp — Compact

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-upper-entry-compact` resources and the matching complete [assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). This upper ramp has two traffic ports and one intrinsic journey between them. Its complete visible high throat can still overhang highway-owned tiles. Traffic follows the saved tile boundaries, while the physical model meets the highway at its flat native-edge cut.

A **PATH** is a saved traffic-route resource, and an **S3D** is the visible model made from indexed triangles. Model faces can extend beyond the tiles that store this piece's PATHs. A flat physical cut at the native highway edge is different from the traffic connection at a city-tile edge. Check both, rather than assuming that one card describes the entire physical opening.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-S-in-1` | road / 1 / primary | in | [7.109934, -56.0, 1.487699]; [0.6123875749328664, 0.7905576880075501]; 0.296093548 | `path-interface-085ec70dd9403a42b8c3` |
| `1-N-out-2` | road / 1 / primary | out | [30.669671, -8.0, 15.0]; [0.39788520723146176, 0.9174352085386612]; 0.0 | `path-interface-66f57bd35c8d7eaedd8b` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-S-in-1` → `1-N-out-2` | primary |

#### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including Wine or CrossOver. Follow the [shared build guide](../../../../docs/BUILD_AND_INSTALL.md) for exact dependency hashes and the captured Avenue input. Build the `ddrhw-modular-ramp-kit` set, and prepare the `compact-modular-diagonal-diamond` Highways menu. Building and rendering do not install game files. Use flat terrain in a disposable city, and follow the [piece placement instructions](README.md#2-piece-and-placement).

The Compact Modular assembly button cycles the highway stamp, four full compact ramps, and two Avenue junctions. If you are testing replacement of one side of an R40 build, replace its two ramps and terminal together.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-upper-entry-compact/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-upper-entry-compact/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-2a51dfe47ab2dea9f129">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-2a51dfe47ab2dea9f129"></a>

**General: unverified** — `software_resources-2a51dfe47ab2dea9f129`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-2a51dfe47ab2dea9f129">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-2a51dfe47ab2dea9f129"></a>

**General: unverified** — `software_connectivity-2a51dfe47ab2dea9f129`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-11416765d63e211ca286">[ ] unverified</a> | <a href="#case-in_game_render-8337a1fa54464d45079b">[ ] unverified</a> | <a href="#case-in_game_render-3a7c86578c7d4c6941fa">[ ] unverified</a> | <a href="#case-in_game_render-9e5f711703da0cb131a0">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-11416765d63e211ca286"></a>

**0° CCW: unverified** — `in_game_render-11416765d63e211ca286`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8337a1fa54464d45079b"></a>

**90° CCW: unverified** — `in_game_render-8337a1fa54464d45079b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3a7c86578c7d4c6941fa"></a>

**180° CCW: unverified** — `in_game_render-3a7c86578c7d4c6941fa`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9e5f711703da0cb131a0"></a>

**270° CCW: unverified** — `in_game_render-9e5f711703da0cb131a0`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-11416765d63e211ca286">[ ] unverified</a> | <a href="#case-in_game_placement-8337a1fa54464d45079b">[ ] unverified</a> | <a href="#case-in_game_placement-3a7c86578c7d4c6941fa">[ ] unverified</a> | <a href="#case-in_game_placement-9e5f711703da0cb131a0">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-11416765d63e211ca286"></a>

**0° CCW: unverified** — `in_game_placement-11416765d63e211ca286`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8337a1fa54464d45079b"></a>

**90° CCW: unverified** — `in_game_placement-8337a1fa54464d45079b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3a7c86578c7d4c6941fa"></a>

**180° CCW: unverified** — `in_game_placement-3a7c86578c7d4c6941fa`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9e5f711703da0cb131a0"></a>

**270° CCW: unverified** — `in_game_placement-9e5f711703da0cb131a0`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-11416765d63e211ca286">[ ] unverified</a> | <a href="#case-in_game_demolition-8337a1fa54464d45079b">[ ] unverified</a> | <a href="#case-in_game_demolition-3a7c86578c7d4c6941fa">[ ] unverified</a> | <a href="#case-in_game_demolition-9e5f711703da0cb131a0">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-11416765d63e211ca286"></a>

**0° CCW: unverified** — `in_game_demolition-11416765d63e211ca286`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8337a1fa54464d45079b"></a>

**90° CCW: unverified** — `in_game_demolition-8337a1fa54464d45079b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3a7c86578c7d4c6941fa"></a>

**180° CCW: unverified** — `in_game_demolition-3a7c86578c7d4c6941fa`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9e5f711703da0cb131a0"></a>

**270° CCW: unverified** — `in_game_demolition-9e5f711703da0cb131a0`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-11416765d63e211ca286">[ ] unverified</a> | <a href="#case-in_game_save_reload-8337a1fa54464d45079b">[ ] unverified</a> | <a href="#case-in_game_save_reload-3a7c86578c7d4c6941fa">[ ] unverified</a> | <a href="#case-in_game_save_reload-9e5f711703da0cb131a0">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-11416765d63e211ca286"></a>

**0° CCW: unverified** — `in_game_save_reload-11416765d63e211ca286`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8337a1fa54464d45079b"></a>

**90° CCW: unverified** — `in_game_save_reload-8337a1fa54464d45079b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3a7c86578c7d4c6941fa"></a>

**180° CCW: unverified** — `in_game_save_reload-3a7c86578c7d4c6941fa`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9e5f711703da0cb131a0"></a>

**270° CCW: unverified** — `in_game_save_reload-9e5f711703da0cb131a0`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2 | — | <a href="#case-in_game_route_query-6502880c3a06e5b36041">[ ] unverified</a> | <a href="#case-in_game_route_query-6d9d10257904a3cca0f1">[ ] unverified</a> | <a href="#case-in_game_route_query-a63467a9bdf4705e0e65">[ ] unverified</a> | <a href="#case-in_game_route_query-b06aebb19ddb476498e4">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2</summary>

<a id="case-in_game_route_query-6502880c3a06e5b36041"></a>

**0° CCW: unverified** — `in_game_route_query-6502880c3a06e5b36041`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-6d9d10257904a3cca0f1"></a>

**90° CCW: unverified** — `in_game_route_query-6d9d10257904a3cca0f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-a63467a9bdf4705e0e65"></a>

**180° CCW: unverified** — `in_game_route_query-a63467a9bdf4705e0e65`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-b06aebb19ddb476498e4"></a>

**270° CCW: unverified** — `in_game_route_query-b06aebb19ddb476498e4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2 | — | <a href="#case-in_game_visible_travel-6502880c3a06e5b36041">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6d9d10257904a3cca0f1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a63467a9bdf4705e0e65">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b06aebb19ddb476498e4">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2</summary>

<a id="case-in_game_visible_travel-6502880c3a06e5b36041"></a>

**0° CCW: unverified** — `in_game_visible_travel-6502880c3a06e5b36041`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-6d9d10257904a3cca0f1"></a>

**90° CCW: unverified** — `in_game_visible_travel-6d9d10257904a3cca0f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-a63467a9bdf4705e0e65"></a>

**180° CCW: unverified** — `in_game_visible_travel-a63467a9bdf4705e0e65`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-b06aebb19ddb476498e4"></a>

**270° CCW: unverified** — `in_game_visible_travel-b06aebb19ddb476498e4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-upper-entry-compact:canonical-southeast | <a href="#case-preview_review-ab077d4913d62df7121f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-upper-entry-compact:canonical-top | <a href="#case-preview_review-7df82f0649a42e98a322">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-upper-entry-compact:connection-overview | <a href="#case-preview_review-1fca67caf66fd57d8fbf">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-entry-compact:canonical-southeast</summary>

<a id="case-preview_review-ab077d4913d62df7121f"></a>

**General: unverified** — `preview_review-ab077d4913d62df7121f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-entry-compact:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-entry-compact:canonical-top</summary>

<a id="case-preview_review-7df82f0649a42e98a322"></a>

**General: unverified** — `preview_review-7df82f0649a42e98a322`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-entry-compact:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-entry-compact:connection-overview</summary>

<a id="case-preview_review-1fca67caf66fd57d8fbf"></a>

**General: unverified** — `preview_review-1fca67caf66fd57d8fbf`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-entry-compact:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The previous experimental stamp included curved branch throats and six extra wing cells. The corrected partition keeps a straight 21-cell stamp, transfers those six construction cells to full ramp owners, and moves all curved high-throat faces into the separately placed ramps. The independent partition audit preserves assembled geometry, UVs, materials, winding, and traffic routes, subject only to the exact float32 re-encoding required by a changed model anchor. Earlier renders and game observations do not approve this corrected ownership split.
