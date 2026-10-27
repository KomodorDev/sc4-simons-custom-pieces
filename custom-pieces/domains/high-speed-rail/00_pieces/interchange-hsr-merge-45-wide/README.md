# HSR L2 Merge 45 Degree Wide

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR L2 Merge 45 Degree Wide. Fixed click-to-place piece in a 6 by 9 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `interchange-hsr-merge-45-wide`.

Footprint: **6 × 9 tiles**. Exact menu name: **HSR L2 Merge 45 Degree Wide**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.json).

![HSR L2 Merge 45 Degree Wide](previews/preview.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/12 applicable cases passed; 0 failed, 0 stale.

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
| `Sout` | hsr / 7 / primary | out | [-2.0, -104.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -104.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Bin` | hsr / 7 / primary | in | [88.0, -128.0, 15.5]; [-0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-e52e55553f098fa8572d` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Bin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Bin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 43, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-hsr-merge-45-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-hsr-merge-45-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b432ff4cb81f25301e49">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b432ff4cb81f25301e49"></a>

**General: unverified** — `software_resources-b432ff4cb81f25301e49`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b432ff4cb81f25301e49">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b432ff4cb81f25301e49"></a>

**General: unverified** — `software_connectivity-b432ff4cb81f25301e49`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-hsr-merge-45-wide:canonical-southeast | <a href="#case-preview_review-4fd908916715e0f730e6">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-hsr-merge-45-wide:canonical-southeast</summary>

<a id="case-preview_review-4fd908916715e0f730e6"></a>

**General: unverified** — `preview_review-4fd908916715e0f730e6`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-hsr-merge-45-wide:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-e1201e3ef581b4decdda">[ ] unverified</a> | <a href="#case-in_game_render-466a305767253d553ae9">[ ] unverified</a> | <a href="#case-in_game_render-c7d61d1cee6c1452612e">[ ] unverified</a> | <a href="#case-in_game_render-0be8de49f31346040f14">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-e1201e3ef581b4decdda"></a>

**0° CCW: unverified** — `in_game_render-e1201e3ef581b4decdda`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-466a305767253d553ae9"></a>

**90° CCW: unverified** — `in_game_render-466a305767253d553ae9`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c7d61d1cee6c1452612e"></a>

**180° CCW: unverified** — `in_game_render-c7d61d1cee6c1452612e`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0be8de49f31346040f14"></a>

**270° CCW: unverified** — `in_game_render-0be8de49f31346040f14`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-e1201e3ef581b4decdda">[ ] unverified</a> | <a href="#case-in_game_placement-466a305767253d553ae9">[ ] unverified</a> | <a href="#case-in_game_placement-c7d61d1cee6c1452612e">[ ] unverified</a> | <a href="#case-in_game_placement-0be8de49f31346040f14">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-e1201e3ef581b4decdda"></a>

**0° CCW: unverified** — `in_game_placement-e1201e3ef581b4decdda`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-466a305767253d553ae9"></a>

**90° CCW: unverified** — `in_game_placement-466a305767253d553ae9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c7d61d1cee6c1452612e"></a>

**180° CCW: unverified** — `in_game_placement-c7d61d1cee6c1452612e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0be8de49f31346040f14"></a>

**270° CCW: unverified** — `in_game_placement-0be8de49f31346040f14`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-e1201e3ef581b4decdda">[ ] unverified</a> | <a href="#case-in_game_demolition-466a305767253d553ae9">[ ] unverified</a> | <a href="#case-in_game_demolition-c7d61d1cee6c1452612e">[ ] unverified</a> | <a href="#case-in_game_demolition-0be8de49f31346040f14">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-e1201e3ef581b4decdda"></a>

**0° CCW: unverified** — `in_game_demolition-e1201e3ef581b4decdda`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-466a305767253d553ae9"></a>

**90° CCW: unverified** — `in_game_demolition-466a305767253d553ae9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c7d61d1cee6c1452612e"></a>

**180° CCW: unverified** — `in_game_demolition-c7d61d1cee6c1452612e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0be8de49f31346040f14"></a>

**270° CCW: unverified** — `in_game_demolition-0be8de49f31346040f14`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-e1201e3ef581b4decdda">[ ] unverified</a> | <a href="#case-in_game_save_reload-466a305767253d553ae9">[ ] unverified</a> | <a href="#case-in_game_save_reload-c7d61d1cee6c1452612e">[ ] unverified</a> | <a href="#case-in_game_save_reload-0be8de49f31346040f14">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-e1201e3ef581b4decdda"></a>

**0° CCW: unverified** — `in_game_save_reload-e1201e3ef581b4decdda`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-466a305767253d553ae9"></a>

**90° CCW: unverified** — `in_game_save_reload-466a305767253d553ae9`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c7d61d1cee6c1452612e"></a>

**180° CCW: unverified** — `in_game_save_reload-c7d61d1cee6c1452612e`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0be8de49f31346040f14"></a>

**270° CCW: unverified** — `in_game_save_reload-0be8de49f31346040f14`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-0b95052e37b163c84f82">[ ] unverified</a> | <a href="#case-in_game_journey-3b2aaabfdd1bc533a3b7">[ ] unverified</a> | <a href="#case-in_game_journey-372bd354343bbeab394e">[ ] unverified</a> | <a href="#case-in_game_journey-77506b48f2be7c786588">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-4c19f5a22329d26d7dcb">[ ] unverified</a> | <a href="#case-in_game_journey-74f4219d819bbd04de9e">[ ] unverified</a> | <a href="#case-in_game_journey-8511aa9275446e407311">[ ] unverified</a> | <a href="#case-in_game_journey-71038c4081b85cc86585">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-8090c71d592db298246d">[ ] unverified</a> | <a href="#case-in_game_journey-8a92ef6fdcd5bb3ea7fd">[ ] unverified</a> | <a href="#case-in_game_journey-c4c5e92d3af37650b7d6">[ ] unverified</a> | <a href="#case-in_game_journey-5311302ba3e265fcb7db">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-0b95052e37b163c84f82"></a>

**0° CCW: unverified** — `in_game_journey-0b95052e37b163c84f82`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-3b2aaabfdd1bc533a3b7"></a>

**90° CCW: unverified** — `in_game_journey-3b2aaabfdd1bc533a3b7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-372bd354343bbeab394e"></a>

**180° CCW: unverified** — `in_game_journey-372bd354343bbeab394e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-77506b48f2be7c786588"></a>

**270° CCW: unverified** — `in_game_journey-77506b48f2be7c786588`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-4c19f5a22329d26d7dcb"></a>

**0° CCW: unverified** — `in_game_journey-4c19f5a22329d26d7dcb`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-74f4219d819bbd04de9e"></a>

**90° CCW: unverified** — `in_game_journey-74f4219d819bbd04de9e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-8511aa9275446e407311"></a>

**180° CCW: unverified** — `in_game_journey-8511aa9275446e407311`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-71038c4081b85cc86585"></a>

**270° CCW: unverified** — `in_game_journey-71038c4081b85cc86585`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-8090c71d592db298246d"></a>

**0° CCW: unverified** — `in_game_journey-8090c71d592db298246d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-8a92ef6fdcd5bb3ea7fd"></a>

**90° CCW: unverified** — `in_game_journey-8a92ef6fdcd5bb3ea7fd`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-c4c5e92d3af37650b7d6"></a>

**180° CCW: unverified** — `in_game_journey-c4c5e92d3af37650b7d6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-5311302ba3e265fcb7db"></a>

**270° CCW: unverified** — `in_game_journey-5311302ba3e265fcb7db`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e293949104f0fde0cfd5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd3a870cb0c3f85a4861">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab8925242509e25b7f23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39e9afa498f292f86f61">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9256d19b087f30812d2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2782a9a2dd94d27d5a0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55c8f1f12199aad7c993">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d0e4642898c2fd758d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b459607ce1eaffe41041">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d370d63239d5ee170f80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07c007f4be84484b6161">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ae20f33db1526dbc30d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e293949104f0fde0cfd5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e293949104f0fde0cfd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd3a870cb0c3f85a4861"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cd3a870cb0c3f85a4861`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab8925242509e25b7f23"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ab8925242509e25b7f23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39e9afa498f292f86f61"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39e9afa498f292f86f61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9256d19b087f30812d2e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9256d19b087f30812d2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2782a9a2dd94d27d5a0f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2782a9a2dd94d27d5a0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55c8f1f12199aad7c993"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-55c8f1f12199aad7c993`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d0e4642898c2fd758d8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d0e4642898c2fd758d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b459607ce1eaffe41041"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b459607ce1eaffe41041`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d370d63239d5ee170f80"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d370d63239d5ee170f80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07c007f4be84484b6161"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-07c007f4be84484b6161`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ae20f33db1526dbc30d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2ae20f33db1526dbc30d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
