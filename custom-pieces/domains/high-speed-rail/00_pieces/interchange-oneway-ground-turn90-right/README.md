# One-Way GHSR 90 Degree Right Compact Curve

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

One-Way GHSR 90 Degree Right Compact Curve. Fixed click-to-place piece in a 3 by 3 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending.

Exact reusable identifier: `interchange-oneway-ground-turn90-right`.

Footprint: **3 × 3 tiles**. Exact menu name: **One-Way GHSR 90 Degree Right Compact Curve**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![One-Way GHSR 90 Degree Right Compact Curve](previews/preview.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/4 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Purpose: describe intrinsic directional interfaces and permitted service journeys.

Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `in` | ghsr / 7 / primary | in | [0.0, -40.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-459a3d38a8ff1501aa51` |
| `out` | ghsr / 7 / primary | out | [40.0, 0.0, 1.0]; [1.0, 0.0]; 0.0 | `path-interface-ab4e40517da7fa0dbd34` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr | `in` → `out` | primary |

### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 23, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-oneway-ground-turn90-right/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-oneway-ground-turn90-right/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-06c64d7d18622bd48739">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-06c64d7d18622bd48739"></a>

**General: unverified** — `software_resources-06c64d7d18622bd48739`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-06c64d7d18622bd48739">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-06c64d7d18622bd48739"></a>

**General: unverified** — `software_connectivity-06c64d7d18622bd48739`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-oneway-ground-turn90-right:canonical-southeast | <a href="#case-preview_review-944e12376893c6b0556a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-oneway-ground-turn90-right:canonical-southeast</summary>

<a id="case-preview_review-944e12376893c6b0556a"></a>

**General: unverified** — `preview_review-944e12376893c6b0556a`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-oneway-ground-turn90-right:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-c7a1d24ce2cf175b0da2">[ ] unverified</a> | <a href="#case-in_game_render-3b3ce78341730d943785">[ ] unverified</a> | <a href="#case-in_game_render-355f10ccb81c6717a1e9">[ ] unverified</a> | <a href="#case-in_game_render-4282d4e15b10091f37af">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-c7a1d24ce2cf175b0da2"></a>

**0° CCW: unverified** — `in_game_render-c7a1d24ce2cf175b0da2`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3b3ce78341730d943785"></a>

**90° CCW: unverified** — `in_game_render-3b3ce78341730d943785`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-355f10ccb81c6717a1e9"></a>

**180° CCW: unverified** — `in_game_render-355f10ccb81c6717a1e9`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-4282d4e15b10091f37af"></a>

**270° CCW: unverified** — `in_game_render-4282d4e15b10091f37af`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-c7a1d24ce2cf175b0da2">[ ] unverified</a> | <a href="#case-in_game_placement-3b3ce78341730d943785">[ ] unverified</a> | <a href="#case-in_game_placement-355f10ccb81c6717a1e9">[ ] unverified</a> | <a href="#case-in_game_placement-4282d4e15b10091f37af">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-c7a1d24ce2cf175b0da2"></a>

**0° CCW: unverified** — `in_game_placement-c7a1d24ce2cf175b0da2`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3b3ce78341730d943785"></a>

**90° CCW: unverified** — `in_game_placement-3b3ce78341730d943785`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-355f10ccb81c6717a1e9"></a>

**180° CCW: unverified** — `in_game_placement-355f10ccb81c6717a1e9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-4282d4e15b10091f37af"></a>

**270° CCW: unverified** — `in_game_placement-4282d4e15b10091f37af`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-c7a1d24ce2cf175b0da2">[ ] unverified</a> | <a href="#case-in_game_demolition-3b3ce78341730d943785">[ ] unverified</a> | <a href="#case-in_game_demolition-355f10ccb81c6717a1e9">[ ] unverified</a> | <a href="#case-in_game_demolition-4282d4e15b10091f37af">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-c7a1d24ce2cf175b0da2"></a>

**0° CCW: unverified** — `in_game_demolition-c7a1d24ce2cf175b0da2`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3b3ce78341730d943785"></a>

**90° CCW: unverified** — `in_game_demolition-3b3ce78341730d943785`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-355f10ccb81c6717a1e9"></a>

**180° CCW: unverified** — `in_game_demolition-355f10ccb81c6717a1e9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-4282d4e15b10091f37af"></a>

**270° CCW: unverified** — `in_game_demolition-4282d4e15b10091f37af`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-c7a1d24ce2cf175b0da2">[ ] unverified</a> | <a href="#case-in_game_save_reload-3b3ce78341730d943785">[ ] unverified</a> | <a href="#case-in_game_save_reload-355f10ccb81c6717a1e9">[ ] unverified</a> | <a href="#case-in_game_save_reload-4282d4e15b10091f37af">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-c7a1d24ce2cf175b0da2"></a>

**0° CCW: unverified** — `in_game_save_reload-c7a1d24ce2cf175b0da2`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3b3ce78341730d943785"></a>

**90° CCW: unverified** — `in_game_save_reload-3b3ce78341730d943785`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-355f10ccb81c6717a1e9"></a>

**180° CCW: unverified** — `in_game_save_reload-355f10ccb81c6717a1e9`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-4282d4e15b10091f37af"></a>

**270° CCW: unverified** — `in_game_save_reload-4282d4e15b10091f37af`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out | — | <a href="#case-in_game_journey-9ad1a5b42cc7cda378dc">[ ] unverified</a> | <a href="#case-in_game_journey-8a0b72139bfd100789e8">[ ] unverified</a> | <a href="#case-in_game_journey-c8cc53eaaf55861239fb">[ ] unverified</a> | <a href="#case-in_game_journey-be0c72c72428b491309a">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out</summary>

<a id="case-in_game_journey-9ad1a5b42cc7cda378dc"></a>

**0° CCW: unverified** — `in_game_journey-9ad1a5b42cc7cda378dc`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-8a0b72139bfd100789e8"></a>

**90° CCW: unverified** — `in_game_journey-8a0b72139bfd100789e8`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-c8cc53eaaf55861239fb"></a>

**180° CCW: unverified** — `in_game_journey-c8cc53eaaf55861239fb`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-be0c72c72428b491309a"></a>

**270° CCW: unverified** — `in_game_journey-be0c72c72428b491309a`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
