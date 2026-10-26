# One-Way GHSR Curve In Right

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

One-Way GHSR Curve In Right. Fixed click-to-place piece in a 1 by 2 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending.

Exact reusable identifier: `interchange-oneway-ground-curve-in-right`.

Footprint: **1 × 2 tiles**. Exact menu name: **One-Way GHSR Curve In Right**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![One-Way GHSR Curve In Right](preview.png)

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
| `out` | ghsr / 7 / primary | out | [0.0, 8.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-459a3d38a8ff1501aa51` |
| `in` | ghsr / 7 / primary | in | [8.0, -16.0, 1.0]; [-0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-6c94c39b4abd67a7479e` |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-oneway-ground-curve-in-right/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-oneway-ground-curve-in-right/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-1a13cb4c7abbd6334aa3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-1a13cb4c7abbd6334aa3"></a>

**General: unverified** — `software_resources-1a13cb4c7abbd6334aa3`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-1a13cb4c7abbd6334aa3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-1a13cb4c7abbd6334aa3"></a>

**General: unverified** — `software_connectivity-1a13cb4c7abbd6334aa3`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-oneway-ground-curve-in-right:canonical-southeast | <a href="#case-preview_review-908b50251de9c6c3988b">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-oneway-ground-curve-in-right:canonical-southeast</summary>

<a id="case-preview_review-908b50251de9c6c3988b"></a>

**General: unverified** — `preview_review-908b50251de9c6c3988b`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-oneway-ground-curve-in-right:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-eb9155c1d12e45e41251">[ ] unverified</a> | <a href="#case-in_game_render-3a45e6adbfc9660001fe">[ ] unverified</a> | <a href="#case-in_game_render-a9d8633bafd2d27592b8">[ ] unverified</a> | <a href="#case-in_game_render-7050b180d47efb3d5c30">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-eb9155c1d12e45e41251"></a>

**0° CCW: unverified** — `in_game_render-eb9155c1d12e45e41251`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3a45e6adbfc9660001fe"></a>

**90° CCW: unverified** — `in_game_render-3a45e6adbfc9660001fe`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a9d8633bafd2d27592b8"></a>

**180° CCW: unverified** — `in_game_render-a9d8633bafd2d27592b8`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7050b180d47efb3d5c30"></a>

**270° CCW: unverified** — `in_game_render-7050b180d47efb3d5c30`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-eb9155c1d12e45e41251">[ ] unverified</a> | <a href="#case-in_game_placement-3a45e6adbfc9660001fe">[ ] unverified</a> | <a href="#case-in_game_placement-a9d8633bafd2d27592b8">[ ] unverified</a> | <a href="#case-in_game_placement-7050b180d47efb3d5c30">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-eb9155c1d12e45e41251"></a>

**0° CCW: unverified** — `in_game_placement-eb9155c1d12e45e41251`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3a45e6adbfc9660001fe"></a>

**90° CCW: unverified** — `in_game_placement-3a45e6adbfc9660001fe`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a9d8633bafd2d27592b8"></a>

**180° CCW: unverified** — `in_game_placement-a9d8633bafd2d27592b8`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7050b180d47efb3d5c30"></a>

**270° CCW: unverified** — `in_game_placement-7050b180d47efb3d5c30`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-eb9155c1d12e45e41251">[ ] unverified</a> | <a href="#case-in_game_demolition-3a45e6adbfc9660001fe">[ ] unverified</a> | <a href="#case-in_game_demolition-a9d8633bafd2d27592b8">[ ] unverified</a> | <a href="#case-in_game_demolition-7050b180d47efb3d5c30">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-eb9155c1d12e45e41251"></a>

**0° CCW: unverified** — `in_game_demolition-eb9155c1d12e45e41251`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3a45e6adbfc9660001fe"></a>

**90° CCW: unverified** — `in_game_demolition-3a45e6adbfc9660001fe`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a9d8633bafd2d27592b8"></a>

**180° CCW: unverified** — `in_game_demolition-a9d8633bafd2d27592b8`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7050b180d47efb3d5c30"></a>

**270° CCW: unverified** — `in_game_demolition-7050b180d47efb3d5c30`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-eb9155c1d12e45e41251">[ ] unverified</a> | <a href="#case-in_game_save_reload-3a45e6adbfc9660001fe">[ ] unverified</a> | <a href="#case-in_game_save_reload-a9d8633bafd2d27592b8">[ ] unverified</a> | <a href="#case-in_game_save_reload-7050b180d47efb3d5c30">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-eb9155c1d12e45e41251"></a>

**0° CCW: unverified** — `in_game_save_reload-eb9155c1d12e45e41251`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3a45e6adbfc9660001fe"></a>

**90° CCW: unverified** — `in_game_save_reload-3a45e6adbfc9660001fe`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a9d8633bafd2d27592b8"></a>

**180° CCW: unverified** — `in_game_save_reload-a9d8633bafd2d27592b8`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7050b180d47efb3d5c30"></a>

**270° CCW: unverified** — `in_game_save_reload-7050b180d47efb3d5c30`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out | — | <a href="#case-in_game_journey-76e2fad93c62f381dfc6">[ ] unverified</a> | <a href="#case-in_game_journey-59f0056ac78aeddfd408">[ ] unverified</a> | <a href="#case-in_game_journey-cec11a0e99e8062cbf6f">[ ] unverified</a> | <a href="#case-in_game_journey-2885268c5e00777ad75b">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out</summary>

<a id="case-in_game_journey-76e2fad93c62f381dfc6"></a>

**0° CCW: unverified** — `in_game_journey-76e2fad93c62f381dfc6`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-59f0056ac78aeddfd408"></a>

**90° CCW: unverified** — `in_game_journey-59f0056ac78aeddfd408`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-cec11a0e99e8062cbf6f"></a>

**180° CCW: unverified** — `in_game_journey-cec11a0e99e8062cbf6f`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-2885268c5e00777ad75b"></a>

**270° CCW: unverified** — `in_game_journey-2885268c5e00777ad75b`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
