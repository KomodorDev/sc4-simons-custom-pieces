# GHSR Diagonal S-Curve Right

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

A two-way diagonal S-curve shifts a diagonal line sideways while preserving its entry and exit heading. Native HSR or GHSR track ends; select the matching height and handedness.

Exact reusable identifier: `rail-ghsr-diagonal-s-right`.

Footprint: **3 × 3 tiles**. Exact menu name: **GHSR Diagonal S-Curve Right**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![GHSR Diagonal S-Curve Right](preview.png)

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
| `Sout` | ghsr / 7 / primary | out | [-2.9, -40.0, 1.0]; [-0.7071067811865469, -0.7071067811865482]; 0.0 | `path-interface-2fb13cb0f06be67da5ca` |
| `Sin` | ghsr / 7 / primary | in | [2.9, -40.0, 1.0]; [0.7924468634807409, 0.6099409549780503]; 0.0 | `path-interface-58b56c96ed533e6fe24c` |
| `Eout` | ghsr / 7 / primary | out | [40.0, -18.8, 1.0]; [0.7673849336782874, 0.6411866838632648]; 0.0 | `path-interface-51af382a22884cd23974` |
| `Ein` | ghsr / 7 / primary | in | [40.0, -13.1, 1.0]; [-0.707106781186548, -0.7071067811865471]; 0.0 | `path-interface-493b20c718656c56d5d7` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr | `Sin` → `Eout` | primary |
| ghsr | `Ein` → `Sout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| ghsr / `Sin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Ein` | ghsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 35, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/rail-ghsr-diagonal-s-right/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/rail-ghsr-diagonal-s-right/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-4fda3e45ebffdd53cd03">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-4fda3e45ebffdd53cd03"></a>

**General: unverified** — `software_resources-4fda3e45ebffdd53cd03`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-4fda3e45ebffdd53cd03">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-4fda3e45ebffdd53cd03"></a>

**General: unverified** — `software_connectivity-4fda3e45ebffdd53cd03`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:rail-ghsr-diagonal-s-right:canonical-southeast | <a href="#case-preview_review-0c1509a5cd76d1b1d65b">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:rail-ghsr-diagonal-s-right:canonical-southeast</summary>

<a id="case-preview_review-0c1509a5cd76d1b1d65b"></a>

**General: unverified** — `preview_review-0c1509a5cd76d1b1d65b`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:rail-ghsr-diagonal-s-right:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-d104c70dd4dc416f629e">[ ] unverified</a> | <a href="#case-in_game_render-a2f21cd86ef9bb01d7c5">[ ] unverified</a> | <a href="#case-in_game_render-1fd2569721b0c7a35454">[ ] unverified</a> | <a href="#case-in_game_render-e92662d16efdd2bd0c26">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-d104c70dd4dc416f629e"></a>

**0° CCW: unverified** — `in_game_render-d104c70dd4dc416f629e`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a2f21cd86ef9bb01d7c5"></a>

**90° CCW: unverified** — `in_game_render-a2f21cd86ef9bb01d7c5`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1fd2569721b0c7a35454"></a>

**180° CCW: unverified** — `in_game_render-1fd2569721b0c7a35454`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e92662d16efdd2bd0c26"></a>

**270° CCW: unverified** — `in_game_render-e92662d16efdd2bd0c26`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-d104c70dd4dc416f629e">[ ] unverified</a> | <a href="#case-in_game_placement-a2f21cd86ef9bb01d7c5">[ ] unverified</a> | <a href="#case-in_game_placement-1fd2569721b0c7a35454">[ ] unverified</a> | <a href="#case-in_game_placement-e92662d16efdd2bd0c26">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-d104c70dd4dc416f629e"></a>

**0° CCW: unverified** — `in_game_placement-d104c70dd4dc416f629e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a2f21cd86ef9bb01d7c5"></a>

**90° CCW: unverified** — `in_game_placement-a2f21cd86ef9bb01d7c5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1fd2569721b0c7a35454"></a>

**180° CCW: unverified** — `in_game_placement-1fd2569721b0c7a35454`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e92662d16efdd2bd0c26"></a>

**270° CCW: unverified** — `in_game_placement-e92662d16efdd2bd0c26`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-d104c70dd4dc416f629e">[ ] unverified</a> | <a href="#case-in_game_demolition-a2f21cd86ef9bb01d7c5">[ ] unverified</a> | <a href="#case-in_game_demolition-1fd2569721b0c7a35454">[ ] unverified</a> | <a href="#case-in_game_demolition-e92662d16efdd2bd0c26">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-d104c70dd4dc416f629e"></a>

**0° CCW: unverified** — `in_game_demolition-d104c70dd4dc416f629e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a2f21cd86ef9bb01d7c5"></a>

**90° CCW: unverified** — `in_game_demolition-a2f21cd86ef9bb01d7c5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1fd2569721b0c7a35454"></a>

**180° CCW: unverified** — `in_game_demolition-1fd2569721b0c7a35454`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e92662d16efdd2bd0c26"></a>

**270° CCW: unverified** — `in_game_demolition-e92662d16efdd2bd0c26`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-d104c70dd4dc416f629e">[ ] unverified</a> | <a href="#case-in_game_save_reload-a2f21cd86ef9bb01d7c5">[ ] unverified</a> | <a href="#case-in_game_save_reload-1fd2569721b0c7a35454">[ ] unverified</a> | <a href="#case-in_game_save_reload-e92662d16efdd2bd0c26">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-d104c70dd4dc416f629e"></a>

**0° CCW: unverified** — `in_game_save_reload-d104c70dd4dc416f629e`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a2f21cd86ef9bb01d7c5"></a>

**90° CCW: unverified** — `in_game_save_reload-a2f21cd86ef9bb01d7c5`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1fd2569721b0c7a35454"></a>

**180° CCW: unverified** — `in_game_save_reload-1fd2569721b0c7a35454`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e92662d16efdd2bd0c26"></a>

**270° CCW: unverified** — `in_game_save_reload-e92662d16efdd2bd0c26`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_journey-35de89335fa8c5c2a41a">[ ] unverified</a> | <a href="#case-in_game_journey-30d8de0ec3516ef8052f">[ ] unverified</a> | <a href="#case-in_game_journey-8210fc7247560df3c3a1">[ ] unverified</a> | <a href="#case-in_game_journey-cac158c3b2d122361e20">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout | — | <a href="#case-in_game_journey-3791a032ac62e0c93500">[ ] unverified</a> | <a href="#case-in_game_journey-3be66cedbf084f2c569d">[ ] unverified</a> | <a href="#case-in_game_journey-75e10b2a06b88c8106fb">[ ] unverified</a> | <a href="#case-in_game_journey-d9d199e1421eed72f802">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_journey-35de89335fa8c5c2a41a"></a>

**0° CCW: unverified** — `in_game_journey-35de89335fa8c5c2a41a`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-30d8de0ec3516ef8052f"></a>

**90° CCW: unverified** — `in_game_journey-30d8de0ec3516ef8052f`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-8210fc7247560df3c3a1"></a>

**180° CCW: unverified** — `in_game_journey-8210fc7247560df3c3a1`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-cac158c3b2d122361e20"></a>

**270° CCW: unverified** — `in_game_journey-cac158c3b2d122361e20`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout</summary>

<a id="case-in_game_journey-3791a032ac62e0c93500"></a>

**0° CCW: unverified** — `in_game_journey-3791a032ac62e0c93500`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-3be66cedbf084f2c569d"></a>

**90° CCW: unverified** — `in_game_journey-3be66cedbf084f2c569d`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-75e10b2a06b88c8106fb"></a>

**180° CCW: unverified** — `in_game_journey-75e10b2a06b88c8106fb`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-d9d199e1421eed72f802"></a>

**270° CCW: unverified** — `in_game_journey-d9d199e1421eed72f802`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dbc42e66032b94908918">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ed9a758bc616b6fe727">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5240befef4fe47c9731d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eefde9a3a552cee7bde5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5bded7cf67de5a6adbd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99ce2267932d287db5aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24fedd9ad989c3c1d430">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39e80f3cb166606d8730">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dbc42e66032b94908918"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dbc42e66032b94908918`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ed9a758bc616b6fe727"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ed9a758bc616b6fe727`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5240befef4fe47c9731d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5240befef4fe47c9731d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eefde9a3a552cee7bde5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eefde9a3a552cee7bde5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5bded7cf67de5a6adbd1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5bded7cf67de5a6adbd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99ce2267932d287db5aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-99ce2267932d287db5aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24fedd9ad989c3c1d430"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-24fedd9ad989c3c1d430`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39e80f3cb166606d8730"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39e80f3cb166606d8730`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

This diagonal S-curve has a 3 × 3 construction rectangle, four occupied cells, and an empty construction reference cell. The Left and Right geometries are separate authored types, rather than reflections inferred from a name. Empty cells do not establish construction clearance.

Use the [independent source contract](../../implementation/scp_hsr/rail_feature_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
