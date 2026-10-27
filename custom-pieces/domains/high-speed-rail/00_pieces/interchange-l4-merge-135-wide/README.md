# Rail L4 Merge 135 Degree Wide

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

Rail L4 Merge 135 Degree Wide. Fixed click-to-place piece in a 12 by 13 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The L4 mainline and branch are both one-way single tracks.

Exact reusable identifier: `interchange-l4-merge-135-wide`.

Footprint: **12 × 13 tiles**. Exact menu name: **Rail L4 Merge 135 Degree Wide**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.json).

![Rail L4 Merge 135 Degree Wide](previews/preview.png)

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
| `Sin` | hsr / 7 / primary | in | [0.0, -184.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Nout` | hsr / 7 / primary | out | [0.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Bin` | hsr / 7 / primary | in | [184.0, -144.0, 30.5]; [-0.7071067811865475, -0.7071067811865475]; 0.0 | `path-interface-13a0d20884fd73110dea` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Bin` → `Nout` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-l4-merge-135-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-l4-merge-135-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-3e3f474d2cdd663c84b4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-3e3f474d2cdd663c84b4"></a>

**General: unverified** — `software_resources-3e3f474d2cdd663c84b4`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-3e3f474d2cdd663c84b4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-3e3f474d2cdd663c84b4"></a>

**General: unverified** — `software_connectivity-3e3f474d2cdd663c84b4`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-l4-merge-135-wide:canonical-southeast | <a href="#case-preview_review-f7f7cd94001b3730ebf9">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-l4-merge-135-wide:canonical-southeast</summary>

<a id="case-preview_review-f7f7cd94001b3730ebf9"></a>

**General: unverified** — `preview_review-f7f7cd94001b3730ebf9`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-l4-merge-135-wide:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-b73fcbe11da70204992a">[ ] unverified</a> | <a href="#case-in_game_render-2bc2e46f595e53256e87">[ ] unverified</a> | <a href="#case-in_game_render-87b91dc7e56f50998d69">[ ] unverified</a> | <a href="#case-in_game_render-028a5c0ba2019a7792f3">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-b73fcbe11da70204992a"></a>

**0° CCW: unverified** — `in_game_render-b73fcbe11da70204992a`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2bc2e46f595e53256e87"></a>

**90° CCW: unverified** — `in_game_render-2bc2e46f595e53256e87`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-87b91dc7e56f50998d69"></a>

**180° CCW: unverified** — `in_game_render-87b91dc7e56f50998d69`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-028a5c0ba2019a7792f3"></a>

**270° CCW: unverified** — `in_game_render-028a5c0ba2019a7792f3`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-b73fcbe11da70204992a">[ ] unverified</a> | <a href="#case-in_game_placement-2bc2e46f595e53256e87">[ ] unverified</a> | <a href="#case-in_game_placement-87b91dc7e56f50998d69">[ ] unverified</a> | <a href="#case-in_game_placement-028a5c0ba2019a7792f3">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-b73fcbe11da70204992a"></a>

**0° CCW: unverified** — `in_game_placement-b73fcbe11da70204992a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2bc2e46f595e53256e87"></a>

**90° CCW: unverified** — `in_game_placement-2bc2e46f595e53256e87`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-87b91dc7e56f50998d69"></a>

**180° CCW: unverified** — `in_game_placement-87b91dc7e56f50998d69`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-028a5c0ba2019a7792f3"></a>

**270° CCW: unverified** — `in_game_placement-028a5c0ba2019a7792f3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-b73fcbe11da70204992a">[ ] unverified</a> | <a href="#case-in_game_demolition-2bc2e46f595e53256e87">[ ] unverified</a> | <a href="#case-in_game_demolition-87b91dc7e56f50998d69">[ ] unverified</a> | <a href="#case-in_game_demolition-028a5c0ba2019a7792f3">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-b73fcbe11da70204992a"></a>

**0° CCW: unverified** — `in_game_demolition-b73fcbe11da70204992a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2bc2e46f595e53256e87"></a>

**90° CCW: unverified** — `in_game_demolition-2bc2e46f595e53256e87`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-87b91dc7e56f50998d69"></a>

**180° CCW: unverified** — `in_game_demolition-87b91dc7e56f50998d69`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-028a5c0ba2019a7792f3"></a>

**270° CCW: unverified** — `in_game_demolition-028a5c0ba2019a7792f3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-b73fcbe11da70204992a">[ ] unverified</a> | <a href="#case-in_game_save_reload-2bc2e46f595e53256e87">[ ] unverified</a> | <a href="#case-in_game_save_reload-87b91dc7e56f50998d69">[ ] unverified</a> | <a href="#case-in_game_save_reload-028a5c0ba2019a7792f3">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-b73fcbe11da70204992a"></a>

**0° CCW: unverified** — `in_game_save_reload-b73fcbe11da70204992a`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2bc2e46f595e53256e87"></a>

**90° CCW: unverified** — `in_game_save_reload-2bc2e46f595e53256e87`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-87b91dc7e56f50998d69"></a>

**180° CCW: unverified** — `in_game_save_reload-87b91dc7e56f50998d69`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-028a5c0ba2019a7792f3"></a>

**270° CCW: unverified** — `in_game_save_reload-028a5c0ba2019a7792f3`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-9bcb4be7de248ddc576f">[ ] unverified</a> | <a href="#case-in_game_journey-8410525754b63a78e2bd">[ ] unverified</a> | <a href="#case-in_game_journey-8b17a3153ccd5d05c3ee">[ ] unverified</a> | <a href="#case-in_game_journey-fa62198420fbd507b38d">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-ff35f0ab7c1a6d1279e3">[ ] unverified</a> | <a href="#case-in_game_journey-29690afd8369f5722320">[ ] unverified</a> | <a href="#case-in_game_journey-071b11e887444e0cc19d">[ ] unverified</a> | <a href="#case-in_game_journey-aa00dc2699a2a1666efa">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-9bcb4be7de248ddc576f"></a>

**0° CCW: unverified** — `in_game_journey-9bcb4be7de248ddc576f`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-8410525754b63a78e2bd"></a>

**90° CCW: unverified** — `in_game_journey-8410525754b63a78e2bd`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-8b17a3153ccd5d05c3ee"></a>

**180° CCW: unverified** — `in_game_journey-8b17a3153ccd5d05c3ee`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-fa62198420fbd507b38d"></a>

**270° CCW: unverified** — `in_game_journey-fa62198420fbd507b38d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-ff35f0ab7c1a6d1279e3"></a>

**0° CCW: unverified** — `in_game_journey-ff35f0ab7c1a6d1279e3`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-29690afd8369f5722320"></a>

**90° CCW: unverified** — `in_game_journey-29690afd8369f5722320`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-071b11e887444e0cc19d"></a>

**180° CCW: unverified** — `in_game_journey-071b11e887444e0cc19d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-aa00dc2699a2a1666efa"></a>

**270° CCW: unverified** — `in_game_journey-aa00dc2699a2a1666efa`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
