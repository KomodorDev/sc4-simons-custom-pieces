# One-Way HSR L2 Curve Out Left

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

One-Way HSR L2 Curve Out Left. Fixed click-to-place piece in a 1 by 2 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending.

Exact reusable identifier: `interchange-oneway-hsr-curve-out-left`.

Footprint: **1 × 2 tiles**. Exact menu name: **One-Way HSR L2 Curve Out Left**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![One-Way HSR L2 Curve Out Left](previews/preview.png)

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
| `out` | hsr / 7 / primary | out | [-8.0, 0.0, 15.5]; [-0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-e52e55553f098fa8572d` |
| `in` | hsr / 7 / primary | in | [0.0, -24.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `in` → `out` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-oneway-hsr-curve-out-left/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-oneway-hsr-curve-out-left/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0e48d4118679178e0b1a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0e48d4118679178e0b1a"></a>

**General: unverified** — `software_resources-0e48d4118679178e0b1a`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0e48d4118679178e0b1a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0e48d4118679178e0b1a"></a>

**General: unverified** — `software_connectivity-0e48d4118679178e0b1a`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-oneway-hsr-curve-out-left:canonical-southeast | <a href="#case-preview_review-a34907f41ad3ee147874">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-oneway-hsr-curve-out-left:canonical-southeast</summary>

<a id="case-preview_review-a34907f41ad3ee147874"></a>

**General: unverified** — `preview_review-a34907f41ad3ee147874`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-oneway-hsr-curve-out-left:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-a0f0e79f6964523b7096">[ ] unverified</a> | <a href="#case-in_game_render-28753ae180d9899ce3ff">[ ] unverified</a> | <a href="#case-in_game_render-d753a860f782e58ca63c">[ ] unverified</a> | <a href="#case-in_game_render-5c6965316dfcc96a814a">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-a0f0e79f6964523b7096"></a>

**0° CCW: unverified** — `in_game_render-a0f0e79f6964523b7096`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-28753ae180d9899ce3ff"></a>

**90° CCW: unverified** — `in_game_render-28753ae180d9899ce3ff`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-d753a860f782e58ca63c"></a>

**180° CCW: unverified** — `in_game_render-d753a860f782e58ca63c`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5c6965316dfcc96a814a"></a>

**270° CCW: unverified** — `in_game_render-5c6965316dfcc96a814a`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-a0f0e79f6964523b7096">[ ] unverified</a> | <a href="#case-in_game_placement-28753ae180d9899ce3ff">[ ] unverified</a> | <a href="#case-in_game_placement-d753a860f782e58ca63c">[ ] unverified</a> | <a href="#case-in_game_placement-5c6965316dfcc96a814a">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-a0f0e79f6964523b7096"></a>

**0° CCW: unverified** — `in_game_placement-a0f0e79f6964523b7096`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-28753ae180d9899ce3ff"></a>

**90° CCW: unverified** — `in_game_placement-28753ae180d9899ce3ff`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-d753a860f782e58ca63c"></a>

**180° CCW: unverified** — `in_game_placement-d753a860f782e58ca63c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5c6965316dfcc96a814a"></a>

**270° CCW: unverified** — `in_game_placement-5c6965316dfcc96a814a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-a0f0e79f6964523b7096">[ ] unverified</a> | <a href="#case-in_game_demolition-28753ae180d9899ce3ff">[ ] unverified</a> | <a href="#case-in_game_demolition-d753a860f782e58ca63c">[ ] unverified</a> | <a href="#case-in_game_demolition-5c6965316dfcc96a814a">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-a0f0e79f6964523b7096"></a>

**0° CCW: unverified** — `in_game_demolition-a0f0e79f6964523b7096`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-28753ae180d9899ce3ff"></a>

**90° CCW: unverified** — `in_game_demolition-28753ae180d9899ce3ff`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-d753a860f782e58ca63c"></a>

**180° CCW: unverified** — `in_game_demolition-d753a860f782e58ca63c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5c6965316dfcc96a814a"></a>

**270° CCW: unverified** — `in_game_demolition-5c6965316dfcc96a814a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-a0f0e79f6964523b7096">[ ] unverified</a> | <a href="#case-in_game_save_reload-28753ae180d9899ce3ff">[ ] unverified</a> | <a href="#case-in_game_save_reload-d753a860f782e58ca63c">[ ] unverified</a> | <a href="#case-in_game_save_reload-5c6965316dfcc96a814a">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-a0f0e79f6964523b7096"></a>

**0° CCW: unverified** — `in_game_save_reload-a0f0e79f6964523b7096`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-28753ae180d9899ce3ff"></a>

**90° CCW: unverified** — `in_game_save_reload-28753ae180d9899ce3ff`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-d753a860f782e58ca63c"></a>

**180° CCW: unverified** — `in_game_save_reload-d753a860f782e58ca63c`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5c6965316dfcc96a814a"></a>

**270° CCW: unverified** — `in_game_save_reload-5c6965316dfcc96a814a`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out | — | <a href="#case-in_game_journey-9a2089558e1914bf7f58">[ ] unverified</a> | <a href="#case-in_game_journey-cbce75f4b20f4c3ca3eb">[ ] unverified</a> | <a href="#case-in_game_journey-b1ffa10fbd26d00c8d33">[ ] unverified</a> | <a href="#case-in_game_journey-eac664dda22fbca9b6be">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out</summary>

<a id="case-in_game_journey-9a2089558e1914bf7f58"></a>

**0° CCW: unverified** — `in_game_journey-9a2089558e1914bf7f58`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-cbce75f4b20f4c3ca3eb"></a>

**90° CCW: unverified** — `in_game_journey-cbce75f4b20f4c3ca3eb`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-b1ffa10fbd26d00c8d33"></a>

**180° CCW: unverified** — `in_game_journey-b1ffa10fbd26d00c8d33`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-eac664dda22fbca9b6be"></a>

**270° CCW: unverified** — `in_game_journey-eac664dda22fbca9b6be`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
