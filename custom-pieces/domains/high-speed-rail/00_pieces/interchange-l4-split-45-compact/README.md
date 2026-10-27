# Rail L4 Split 45 Degree Compact

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

Rail L4 Split 45 Degree Compact. Fixed click-to-place piece in a 3 by 4 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The L4 mainline and branch are both one-way single tracks.

Exact reusable identifier: `interchange-l4-split-45-compact`.

Footprint: **3 × 4 tiles**. Exact menu name: **Rail L4 Split 45 Degree Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![Rail L4 Split 45 Degree Compact](previews/preview.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/8 applicable cases passed; 0 failed, 0 stale.

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
| `Sin` | hsr / 7 / primary | in | [0.0, -56.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Nout` | hsr / 7 / primary | out | [0.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Bout` | hsr / 7 / primary | out | [40.0, 0.0, 30.5]; [0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-13a0d20884fd73110dea` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Sin` → `Bout` | primary |

### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 27, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-l4-split-45-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-l4-split-45-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ed9d5098330045e0b710">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ed9d5098330045e0b710"></a>

**General: unverified** — `software_resources-ed9d5098330045e0b710`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ed9d5098330045e0b710">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ed9d5098330045e0b710"></a>

**General: unverified** — `software_connectivity-ed9d5098330045e0b710`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-l4-split-45-compact:canonical-southeast | <a href="#case-preview_review-4989de213dd46b273ac4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-l4-split-45-compact:canonical-southeast</summary>

<a id="case-preview_review-4989de213dd46b273ac4"></a>

**General: unverified** — `preview_review-4989de213dd46b273ac4`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-l4-split-45-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-583bf219ea719faf0c44">[ ] unverified</a> | <a href="#case-in_game_render-c48f4e1165f0814b1ba8">[ ] unverified</a> | <a href="#case-in_game_render-65a4952e6558138b9d4c">[ ] unverified</a> | <a href="#case-in_game_render-8c6d8a36e6c7c3a63313">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-583bf219ea719faf0c44"></a>

**0° CCW: unverified** — `in_game_render-583bf219ea719faf0c44`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c48f4e1165f0814b1ba8"></a>

**90° CCW: unverified** — `in_game_render-c48f4e1165f0814b1ba8`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-65a4952e6558138b9d4c"></a>

**180° CCW: unverified** — `in_game_render-65a4952e6558138b9d4c`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8c6d8a36e6c7c3a63313"></a>

**270° CCW: unverified** — `in_game_render-8c6d8a36e6c7c3a63313`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-583bf219ea719faf0c44">[ ] unverified</a> | <a href="#case-in_game_placement-c48f4e1165f0814b1ba8">[ ] unverified</a> | <a href="#case-in_game_placement-65a4952e6558138b9d4c">[ ] unverified</a> | <a href="#case-in_game_placement-8c6d8a36e6c7c3a63313">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-583bf219ea719faf0c44"></a>

**0° CCW: unverified** — `in_game_placement-583bf219ea719faf0c44`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c48f4e1165f0814b1ba8"></a>

**90° CCW: unverified** — `in_game_placement-c48f4e1165f0814b1ba8`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-65a4952e6558138b9d4c"></a>

**180° CCW: unverified** — `in_game_placement-65a4952e6558138b9d4c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8c6d8a36e6c7c3a63313"></a>

**270° CCW: unverified** — `in_game_placement-8c6d8a36e6c7c3a63313`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-583bf219ea719faf0c44">[ ] unverified</a> | <a href="#case-in_game_demolition-c48f4e1165f0814b1ba8">[ ] unverified</a> | <a href="#case-in_game_demolition-65a4952e6558138b9d4c">[ ] unverified</a> | <a href="#case-in_game_demolition-8c6d8a36e6c7c3a63313">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-583bf219ea719faf0c44"></a>

**0° CCW: unverified** — `in_game_demolition-583bf219ea719faf0c44`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c48f4e1165f0814b1ba8"></a>

**90° CCW: unverified** — `in_game_demolition-c48f4e1165f0814b1ba8`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-65a4952e6558138b9d4c"></a>

**180° CCW: unverified** — `in_game_demolition-65a4952e6558138b9d4c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8c6d8a36e6c7c3a63313"></a>

**270° CCW: unverified** — `in_game_demolition-8c6d8a36e6c7c3a63313`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-583bf219ea719faf0c44">[ ] unverified</a> | <a href="#case-in_game_save_reload-c48f4e1165f0814b1ba8">[ ] unverified</a> | <a href="#case-in_game_save_reload-65a4952e6558138b9d4c">[ ] unverified</a> | <a href="#case-in_game_save_reload-8c6d8a36e6c7c3a63313">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-583bf219ea719faf0c44"></a>

**0° CCW: unverified** — `in_game_save_reload-583bf219ea719faf0c44`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c48f4e1165f0814b1ba8"></a>

**90° CCW: unverified** — `in_game_save_reload-c48f4e1165f0814b1ba8`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-65a4952e6558138b9d4c"></a>

**180° CCW: unverified** — `in_game_save_reload-65a4952e6558138b9d4c`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8c6d8a36e6c7c3a63313"></a>

**270° CCW: unverified** — `in_game_save_reload-8c6d8a36e6c7c3a63313`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-21c9ff0af413766630fd">[ ] unverified</a> | <a href="#case-in_game_journey-0c141a049457dbe62cd7">[ ] unverified</a> | <a href="#case-in_game_journey-19699908891473fe8bac">[ ] unverified</a> | <a href="#case-in_game_journey-becb1935b688300e6258">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-217123a084dbda1a849d">[ ] unverified</a> | <a href="#case-in_game_journey-8a371ee21f51d05f6038">[ ] unverified</a> | <a href="#case-in_game_journey-59dc1c67cf40bb44605d">[ ] unverified</a> | <a href="#case-in_game_journey-9cdb225289b2678be0da">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-21c9ff0af413766630fd"></a>

**0° CCW: unverified** — `in_game_journey-21c9ff0af413766630fd`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-0c141a049457dbe62cd7"></a>

**90° CCW: unverified** — `in_game_journey-0c141a049457dbe62cd7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-19699908891473fe8bac"></a>

**180° CCW: unverified** — `in_game_journey-19699908891473fe8bac`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-becb1935b688300e6258"></a>

**270° CCW: unverified** — `in_game_journey-becb1935b688300e6258`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-217123a084dbda1a849d"></a>

**0° CCW: unverified** — `in_game_journey-217123a084dbda1a849d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-8a371ee21f51d05f6038"></a>

**90° CCW: unverified** — `in_game_journey-8a371ee21f51d05f6038`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-59dc1c67cf40bb44605d"></a>

**180° CCW: unverified** — `in_game_journey-59dc1c67cf40bb44605d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-9cdb225289b2678be0da"></a>

**270° CCW: unverified** — `in_game_journey-9cdb225289b2678be0da`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
