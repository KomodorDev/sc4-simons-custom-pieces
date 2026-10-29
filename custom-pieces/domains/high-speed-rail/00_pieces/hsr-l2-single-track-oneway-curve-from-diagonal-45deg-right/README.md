<a id="one-way-hsr-l2-curve-in-right"></a>

# HSR Level 2 (15.5 m) — Single-Track One-Way Curve 45° Right — Diagonal to Orthogonal

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-oneway-hsr-curve-in-right` → `hsr-l2-single-track-oneway-curve-from-diagonal-45deg-right`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR Level 2 (15.5 m) — Single-Track One-Way Curve 45° Right — Diagonal to Orthogonal. Fixed click-to-place piece in a 1 by 2 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending.

Exact reusable identifier: `hsr-l2-single-track-oneway-curve-from-diagonal-45deg-right`.

Footprint: **1 × 2 tiles**. Exact menu name: **HSR Level 2 (15.5 m) — Single-Track One-Way Curve 45° Right — Diagonal to Orthogonal**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR Level 2 (15.5 m) — Single-Track One-Way Curve 45° Right — Diagonal to Orthogonal](previews/preview.png)

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

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `out` | hsr / 7 / primary | out | [0.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |
| `in` | hsr / 7 / primary | in | [8.0, -16.0, 15.5]; [-0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-e52e55553f098fa8572d` |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-single-track-oneway-curve-from-diagonal-45deg-right/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-single-track-oneway-curve-from-diagonal-45deg-right/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b575f4f9ae7f00971bd1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b575f4f9ae7f00971bd1"></a>

**General: unverified** — `software_resources-b575f4f9ae7f00971bd1`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b575f4f9ae7f00971bd1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b575f4f9ae7f00971bd1"></a>

**General: unverified** — `software_connectivity-b575f4f9ae7f00971bd1`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-oneway-hsr-curve-in-right:canonical-southeast | <a href="#case-preview_review-eaf802532869a23a61b8">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-oneway-hsr-curve-in-right:canonical-southeast</summary>

<a id="case-preview_review-eaf802532869a23a61b8"></a>

**General: unverified** — `preview_review-eaf802532869a23a61b8`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-oneway-hsr-curve-in-right:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-d1d7fa3a48f051efa54e">[ ] unverified</a> | <a href="#case-in_game_render-32e55cb0b7aff1845a9f">[ ] unverified</a> | <a href="#case-in_game_render-d5e99cc4a01a1c333c12">[ ] unverified</a> | <a href="#case-in_game_render-77bd38c917a77a7e9818">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-d1d7fa3a48f051efa54e"></a>

**0° CCW: unverified** — `in_game_render-d1d7fa3a48f051efa54e`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-32e55cb0b7aff1845a9f"></a>

**90° CCW: unverified** — `in_game_render-32e55cb0b7aff1845a9f`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-d5e99cc4a01a1c333c12"></a>

**180° CCW: unverified** — `in_game_render-d5e99cc4a01a1c333c12`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-77bd38c917a77a7e9818"></a>

**270° CCW: unverified** — `in_game_render-77bd38c917a77a7e9818`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-d1d7fa3a48f051efa54e">[ ] unverified</a> | <a href="#case-in_game_placement-32e55cb0b7aff1845a9f">[ ] unverified</a> | <a href="#case-in_game_placement-d5e99cc4a01a1c333c12">[ ] unverified</a> | <a href="#case-in_game_placement-77bd38c917a77a7e9818">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-d1d7fa3a48f051efa54e"></a>

**0° CCW: unverified** — `in_game_placement-d1d7fa3a48f051efa54e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-32e55cb0b7aff1845a9f"></a>

**90° CCW: unverified** — `in_game_placement-32e55cb0b7aff1845a9f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-d5e99cc4a01a1c333c12"></a>

**180° CCW: unverified** — `in_game_placement-d5e99cc4a01a1c333c12`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-77bd38c917a77a7e9818"></a>

**270° CCW: unverified** — `in_game_placement-77bd38c917a77a7e9818`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-d1d7fa3a48f051efa54e">[ ] unverified</a> | <a href="#case-in_game_demolition-32e55cb0b7aff1845a9f">[ ] unverified</a> | <a href="#case-in_game_demolition-d5e99cc4a01a1c333c12">[ ] unverified</a> | <a href="#case-in_game_demolition-77bd38c917a77a7e9818">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-d1d7fa3a48f051efa54e"></a>

**0° CCW: unverified** — `in_game_demolition-d1d7fa3a48f051efa54e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-32e55cb0b7aff1845a9f"></a>

**90° CCW: unverified** — `in_game_demolition-32e55cb0b7aff1845a9f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-d5e99cc4a01a1c333c12"></a>

**180° CCW: unverified** — `in_game_demolition-d5e99cc4a01a1c333c12`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-77bd38c917a77a7e9818"></a>

**270° CCW: unverified** — `in_game_demolition-77bd38c917a77a7e9818`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-d1d7fa3a48f051efa54e">[ ] unverified</a> | <a href="#case-in_game_save_reload-32e55cb0b7aff1845a9f">[ ] unverified</a> | <a href="#case-in_game_save_reload-d5e99cc4a01a1c333c12">[ ] unverified</a> | <a href="#case-in_game_save_reload-77bd38c917a77a7e9818">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-d1d7fa3a48f051efa54e"></a>

**0° CCW: unverified** — `in_game_save_reload-d1d7fa3a48f051efa54e`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-32e55cb0b7aff1845a9f"></a>

**90° CCW: unverified** — `in_game_save_reload-32e55cb0b7aff1845a9f`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-d5e99cc4a01a1c333c12"></a>

**180° CCW: unverified** — `in_game_save_reload-d5e99cc4a01a1c333c12`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-77bd38c917a77a7e9818"></a>

**270° CCW: unverified** — `in_game_save_reload-77bd38c917a77a7e9818`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out | — | <a href="#case-in_game_journey-72578b52c0cd8d11dd67">[ ] unverified</a> | <a href="#case-in_game_journey-47d5c6e8d29f718da9ce">[ ] unverified</a> | <a href="#case-in_game_journey-c423b41414e0f0681a39">[ ] unverified</a> | <a href="#case-in_game_journey-a03b41fb5e65ae2a4fa9">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out</summary>

<a id="case-in_game_journey-72578b52c0cd8d11dd67"></a>

**0° CCW: unverified** — `in_game_journey-72578b52c0cd8d11dd67`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-47d5c6e8d29f718da9ce"></a>

**90° CCW: unverified** — `in_game_journey-47d5c6e8d29f718da9ce`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-c423b41414e0f0681a39"></a>

**180° CCW: unverified** — `in_game_journey-c423b41414e0f0681a39`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-a03b41fb5e65ae2a4fa9"></a>

**270° CCW: unverified** — `in_game_journey-a03b41fb5e65ae2a4fa9`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
