<a id="one-way-l4-split-135deg-left-compact"></a>

# HSR Level 4 (30.5 m) — Split 135° Left from Single-Track One-Way Mainline — Compact

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-l4-split-135-compact-left` → `hsr-l4-single-track-oneway-split-135deg-left-compact`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

A left-hand split or merge on the centered one-way 30.5 m track. No opposing mainline track is crossed. Use matching one-way L4 fillers and level adapters. The L4 mainline and branch are both one-way single tracks.

Exact reusable identifier: `hsr-l4-single-track-oneway-split-135deg-left-compact`.

Footprint: **6 × 6 tiles**. Exact menu name: **HSR Level 4 (30.5 m) — Split 135° Left from Single-Track One-Way Mainline — Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.jsonc).

![HSR Level 4 (30.5 m) — Split 135° Left from Single-Track One-Way Mainline — Compact](previews/preview.png)

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

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Bout` | hsr / 7 / primary | out | [-8.0, -16.0, 30.5]; [-0.7071067811865475, -0.7071067811865475]; 0.0 | `path-interface-13a0d20884fd73110dea` |
| `Sin` | hsr / 7 / primary | in | [80.0, -88.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Nout` | hsr / 7 / primary | out | [80.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Bout` | primary |
| hsr | `Sin` → `Nout` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l4-single-track-oneway-split-135deg-left-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l4-single-track-oneway-split-135deg-left-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-6e6abb3400ff25b128d0">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-6e6abb3400ff25b128d0"></a>

**General: unverified** — `software_resources-6e6abb3400ff25b128d0`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-6e6abb3400ff25b128d0">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-6e6abb3400ff25b128d0"></a>

**General: unverified** — `software_connectivity-6e6abb3400ff25b128d0`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-l4-split-135-compact-left:canonical-southeast | <a href="#case-preview_review-827833b700e516b7a70a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-l4-split-135-compact-left:canonical-southeast</summary>

<a id="case-preview_review-827833b700e516b7a70a"></a>

**General: unverified** — `preview_review-827833b700e516b7a70a`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-l4-split-135-compact-left:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-ef5b6ac94c166a545785">[ ] unverified</a> | <a href="#case-in_game_render-51c72ef36053b1d4c085">[ ] unverified</a> | <a href="#case-in_game_render-93cb5f04c6a1411c16fb">[ ] unverified</a> | <a href="#case-in_game_render-b68a8632953d5e6e39ed">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-ef5b6ac94c166a545785"></a>

**0° CCW: unverified** — `in_game_render-ef5b6ac94c166a545785`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-51c72ef36053b1d4c085"></a>

**90° CCW: unverified** — `in_game_render-51c72ef36053b1d4c085`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-93cb5f04c6a1411c16fb"></a>

**180° CCW: unverified** — `in_game_render-93cb5f04c6a1411c16fb`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-b68a8632953d5e6e39ed"></a>

**270° CCW: unverified** — `in_game_render-b68a8632953d5e6e39ed`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-ef5b6ac94c166a545785">[ ] unverified</a> | <a href="#case-in_game_placement-51c72ef36053b1d4c085">[ ] unverified</a> | <a href="#case-in_game_placement-93cb5f04c6a1411c16fb">[ ] unverified</a> | <a href="#case-in_game_placement-b68a8632953d5e6e39ed">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-ef5b6ac94c166a545785"></a>

**0° CCW: unverified** — `in_game_placement-ef5b6ac94c166a545785`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-51c72ef36053b1d4c085"></a>

**90° CCW: unverified** — `in_game_placement-51c72ef36053b1d4c085`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-93cb5f04c6a1411c16fb"></a>

**180° CCW: unverified** — `in_game_placement-93cb5f04c6a1411c16fb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-b68a8632953d5e6e39ed"></a>

**270° CCW: unverified** — `in_game_placement-b68a8632953d5e6e39ed`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-ef5b6ac94c166a545785">[ ] unverified</a> | <a href="#case-in_game_demolition-51c72ef36053b1d4c085">[ ] unverified</a> | <a href="#case-in_game_demolition-93cb5f04c6a1411c16fb">[ ] unverified</a> | <a href="#case-in_game_demolition-b68a8632953d5e6e39ed">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-ef5b6ac94c166a545785"></a>

**0° CCW: unverified** — `in_game_demolition-ef5b6ac94c166a545785`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-51c72ef36053b1d4c085"></a>

**90° CCW: unverified** — `in_game_demolition-51c72ef36053b1d4c085`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-93cb5f04c6a1411c16fb"></a>

**180° CCW: unverified** — `in_game_demolition-93cb5f04c6a1411c16fb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-b68a8632953d5e6e39ed"></a>

**270° CCW: unverified** — `in_game_demolition-b68a8632953d5e6e39ed`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-ef5b6ac94c166a545785">[ ] unverified</a> | <a href="#case-in_game_save_reload-51c72ef36053b1d4c085">[ ] unverified</a> | <a href="#case-in_game_save_reload-93cb5f04c6a1411c16fb">[ ] unverified</a> | <a href="#case-in_game_save_reload-b68a8632953d5e6e39ed">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-ef5b6ac94c166a545785"></a>

**0° CCW: unverified** — `in_game_save_reload-ef5b6ac94c166a545785`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-51c72ef36053b1d4c085"></a>

**90° CCW: unverified** — `in_game_save_reload-51c72ef36053b1d4c085`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-93cb5f04c6a1411c16fb"></a>

**180° CCW: unverified** — `in_game_save_reload-93cb5f04c6a1411c16fb`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-b68a8632953d5e6e39ed"></a>

**270° CCW: unverified** — `in_game_save_reload-b68a8632953d5e6e39ed`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-8f9b56da96b5e234f7a5">[ ] unverified</a> | <a href="#case-in_game_journey-a01c6d30604983667391">[ ] unverified</a> | <a href="#case-in_game_journey-b3fee989980aee929998">[ ] unverified</a> | <a href="#case-in_game_journey-d8a0bb58d488eef7f580">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-b3b109a5c6dfc8db1882">[ ] unverified</a> | <a href="#case-in_game_journey-c84489e4f8041952a320">[ ] unverified</a> | <a href="#case-in_game_journey-fbeeebd9d29602c7cda2">[ ] unverified</a> | <a href="#case-in_game_journey-709d6b70ac6389f8ec1d">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-8f9b56da96b5e234f7a5"></a>

**0° CCW: unverified** — `in_game_journey-8f9b56da96b5e234f7a5`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-a01c6d30604983667391"></a>

**90° CCW: unverified** — `in_game_journey-a01c6d30604983667391`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-b3fee989980aee929998"></a>

**180° CCW: unverified** — `in_game_journey-b3fee989980aee929998`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-d8a0bb58d488eef7f580"></a>

**270° CCW: unverified** — `in_game_journey-d8a0bb58d488eef7f580`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-b3b109a5c6dfc8db1882"></a>

**0° CCW: unverified** — `in_game_journey-b3b109a5c6dfc8db1882`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-c84489e4f8041952a320"></a>

**90° CCW: unverified** — `in_game_journey-c84489e4f8041952a320`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-fbeeebd9d29602c7cda2"></a>

**180° CCW: unverified** — `in_game_journey-fbeeebd9d29602c7cda2`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-709d6b70ac6389f8ec1d"></a>

**270° CCW: unverified** — `in_game_journey-709d6b70ac6389f8ec1d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
