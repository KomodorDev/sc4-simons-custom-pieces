# One-Way GHSR Diagonal East Half

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

One-Way GHSR Diagonal East Half. Fixed click-to-place piece in a 1 by 1 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending.

Exact reusable identifier: `interchange-oneway-ground-diagonal-east-half`.

Footprint: **1 × 1 tiles**. Exact menu name: **One-Way GHSR Diagonal East Half**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![One-Way GHSR Diagonal East Half](preview.png)

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
| `in` | ghsr / 7 / primary | in | [0.0, -8.0, 1.0]; [0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-6c94c39b4abd67a7479e` |
| `out` | ghsr / 7 / primary | out | [8.0, 0.0, 1.0]; [0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-f99fce9a9cdaf09202fb` |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-oneway-ground-diagonal-east-half/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-oneway-ground-diagonal-east-half/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-8f4706d24d84fd579311">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-8f4706d24d84fd579311"></a>

**General: unverified** — `software_resources-8f4706d24d84fd579311`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-8f4706d24d84fd579311">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-8f4706d24d84fd579311"></a>

**General: unverified** — `software_connectivity-8f4706d24d84fd579311`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-oneway-ground-diagonal-east-half:canonical-southeast | <a href="#case-preview_review-9a5c5bed524670b72d1e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-oneway-ground-diagonal-east-half:canonical-southeast</summary>

<a id="case-preview_review-9a5c5bed524670b72d1e"></a>

**General: unverified** — `preview_review-9a5c5bed524670b72d1e`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-oneway-ground-diagonal-east-half:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-083e06b1fcac1ab60d6e">[ ] unverified</a> | <a href="#case-in_game_render-a5d792ed89a1891116fa">[ ] unverified</a> | <a href="#case-in_game_render-8a7dee8f156bf04ebc0b">[ ] unverified</a> | <a href="#case-in_game_render-170ed08e916d565b57d9">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-083e06b1fcac1ab60d6e"></a>

**0° CCW: unverified** — `in_game_render-083e06b1fcac1ab60d6e`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a5d792ed89a1891116fa"></a>

**90° CCW: unverified** — `in_game_render-a5d792ed89a1891116fa`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8a7dee8f156bf04ebc0b"></a>

**180° CCW: unverified** — `in_game_render-8a7dee8f156bf04ebc0b`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-170ed08e916d565b57d9"></a>

**270° CCW: unverified** — `in_game_render-170ed08e916d565b57d9`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-083e06b1fcac1ab60d6e">[ ] unverified</a> | <a href="#case-in_game_placement-a5d792ed89a1891116fa">[ ] unverified</a> | <a href="#case-in_game_placement-8a7dee8f156bf04ebc0b">[ ] unverified</a> | <a href="#case-in_game_placement-170ed08e916d565b57d9">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-083e06b1fcac1ab60d6e"></a>

**0° CCW: unverified** — `in_game_placement-083e06b1fcac1ab60d6e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a5d792ed89a1891116fa"></a>

**90° CCW: unverified** — `in_game_placement-a5d792ed89a1891116fa`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8a7dee8f156bf04ebc0b"></a>

**180° CCW: unverified** — `in_game_placement-8a7dee8f156bf04ebc0b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-170ed08e916d565b57d9"></a>

**270° CCW: unverified** — `in_game_placement-170ed08e916d565b57d9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-083e06b1fcac1ab60d6e">[ ] unverified</a> | <a href="#case-in_game_demolition-a5d792ed89a1891116fa">[ ] unverified</a> | <a href="#case-in_game_demolition-8a7dee8f156bf04ebc0b">[ ] unverified</a> | <a href="#case-in_game_demolition-170ed08e916d565b57d9">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-083e06b1fcac1ab60d6e"></a>

**0° CCW: unverified** — `in_game_demolition-083e06b1fcac1ab60d6e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a5d792ed89a1891116fa"></a>

**90° CCW: unverified** — `in_game_demolition-a5d792ed89a1891116fa`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8a7dee8f156bf04ebc0b"></a>

**180° CCW: unverified** — `in_game_demolition-8a7dee8f156bf04ebc0b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-170ed08e916d565b57d9"></a>

**270° CCW: unverified** — `in_game_demolition-170ed08e916d565b57d9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-083e06b1fcac1ab60d6e">[ ] unverified</a> | <a href="#case-in_game_save_reload-a5d792ed89a1891116fa">[ ] unverified</a> | <a href="#case-in_game_save_reload-8a7dee8f156bf04ebc0b">[ ] unverified</a> | <a href="#case-in_game_save_reload-170ed08e916d565b57d9">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-083e06b1fcac1ab60d6e"></a>

**0° CCW: unverified** — `in_game_save_reload-083e06b1fcac1ab60d6e`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a5d792ed89a1891116fa"></a>

**90° CCW: unverified** — `in_game_save_reload-a5d792ed89a1891116fa`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8a7dee8f156bf04ebc0b"></a>

**180° CCW: unverified** — `in_game_save_reload-8a7dee8f156bf04ebc0b`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-170ed08e916d565b57d9"></a>

**270° CCW: unverified** — `in_game_save_reload-170ed08e916d565b57d9`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out | — | <a href="#case-in_game_journey-d3d2dbab91388236fd84">[ ] unverified</a> | <a href="#case-in_game_journey-cb1baa6d95ece37a5e28">[ ] unverified</a> | <a href="#case-in_game_journey-8eefc78d7c8f97d31d6d">[ ] unverified</a> | <a href="#case-in_game_journey-7875851304a9f281dc18">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out</summary>

<a id="case-in_game_journey-d3d2dbab91388236fd84"></a>

**0° CCW: unverified** — `in_game_journey-d3d2dbab91388236fd84`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-cb1baa6d95ece37a5e28"></a>

**90° CCW: unverified** — `in_game_journey-cb1baa6d95ece37a5e28`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-8eefc78d7c8f97d31d6d"></a>

**180° CCW: unverified** — `in_game_journey-8eefc78d7c8f97d31d6d`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-7875851304a9f281dc18"></a>

**270° CCW: unverified** — `in_game_journey-7875851304a9f281dc18`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
