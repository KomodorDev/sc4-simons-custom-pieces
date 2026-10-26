# One-Way HSR L2 Wide 90 Degree Curve Right

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

A centred one-way track turns right through 90 degrees at 15.5 m; 136 m displacement in each cardinal direction and flat connection collars.

Exact reusable identifier: `hsr-component-lower-oneway-curve90-right-wide`.

Footprint: **9 × 9 tiles**. Exact menu name: **One-Way HSR L2 Wide 90 Degree Curve Right**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![One-Way HSR L2 Wide 90 Degree Curve Right](preview.png)

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
| `Sin` | hsr / 7 / primary | in | [0.0, -136.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |
| `Eout` | hsr / 7 / primary | out | [136.0, 0.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-365752af76285c80cd0b` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Eout` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-lower-oneway-curve90-right-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-lower-oneway-curve90-right-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-94e4ba9c4218dcdfcd5e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-94e4ba9c4218dcdfcd5e"></a>

**General: unverified** — `software_resources-94e4ba9c4218dcdfcd5e`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-94e4ba9c4218dcdfcd5e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-94e4ba9c4218dcdfcd5e"></a>

**General: unverified** — `software_connectivity-94e4ba9c4218dcdfcd5e`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-lower-oneway-curve90-right-wide:canonical-southeast | <a href="#case-preview_review-edb48edac1438379ee5f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-lower-oneway-curve90-right-wide:canonical-southeast</summary>

<a id="case-preview_review-edb48edac1438379ee5f"></a>

**General: unverified** — `preview_review-edb48edac1438379ee5f`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-lower-oneway-curve90-right-wide:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-255246fbd91a10359623">[ ] unverified</a> | <a href="#case-in_game_render-d969d0cda8a17d83eb39">[ ] unverified</a> | <a href="#case-in_game_render-f4f1374be5fcb644368c">[ ] unverified</a> | <a href="#case-in_game_render-e210fe65b771e4d5b153">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-255246fbd91a10359623"></a>

**0° CCW: unverified** — `in_game_render-255246fbd91a10359623`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-d969d0cda8a17d83eb39"></a>

**90° CCW: unverified** — `in_game_render-d969d0cda8a17d83eb39`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-f4f1374be5fcb644368c"></a>

**180° CCW: unverified** — `in_game_render-f4f1374be5fcb644368c`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e210fe65b771e4d5b153"></a>

**270° CCW: unverified** — `in_game_render-e210fe65b771e4d5b153`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-255246fbd91a10359623">[ ] unverified</a> | <a href="#case-in_game_placement-d969d0cda8a17d83eb39">[ ] unverified</a> | <a href="#case-in_game_placement-f4f1374be5fcb644368c">[ ] unverified</a> | <a href="#case-in_game_placement-e210fe65b771e4d5b153">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-255246fbd91a10359623"></a>

**0° CCW: unverified** — `in_game_placement-255246fbd91a10359623`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-d969d0cda8a17d83eb39"></a>

**90° CCW: unverified** — `in_game_placement-d969d0cda8a17d83eb39`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-f4f1374be5fcb644368c"></a>

**180° CCW: unverified** — `in_game_placement-f4f1374be5fcb644368c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e210fe65b771e4d5b153"></a>

**270° CCW: unverified** — `in_game_placement-e210fe65b771e4d5b153`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-255246fbd91a10359623">[ ] unverified</a> | <a href="#case-in_game_demolition-d969d0cda8a17d83eb39">[ ] unverified</a> | <a href="#case-in_game_demolition-f4f1374be5fcb644368c">[ ] unverified</a> | <a href="#case-in_game_demolition-e210fe65b771e4d5b153">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-255246fbd91a10359623"></a>

**0° CCW: unverified** — `in_game_demolition-255246fbd91a10359623`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-d969d0cda8a17d83eb39"></a>

**90° CCW: unverified** — `in_game_demolition-d969d0cda8a17d83eb39`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-f4f1374be5fcb644368c"></a>

**180° CCW: unverified** — `in_game_demolition-f4f1374be5fcb644368c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e210fe65b771e4d5b153"></a>

**270° CCW: unverified** — `in_game_demolition-e210fe65b771e4d5b153`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-255246fbd91a10359623">[ ] unverified</a> | <a href="#case-in_game_save_reload-d969d0cda8a17d83eb39">[ ] unverified</a> | <a href="#case-in_game_save_reload-f4f1374be5fcb644368c">[ ] unverified</a> | <a href="#case-in_game_save_reload-e210fe65b771e4d5b153">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-255246fbd91a10359623"></a>

**0° CCW: unverified** — `in_game_save_reload-255246fbd91a10359623`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-d969d0cda8a17d83eb39"></a>

**90° CCW: unverified** — `in_game_save_reload-d969d0cda8a17d83eb39`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-f4f1374be5fcb644368c"></a>

**180° CCW: unverified** — `in_game_save_reload-f4f1374be5fcb644368c`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e210fe65b771e4d5b153"></a>

**270° CCW: unverified** — `in_game_save_reload-e210fe65b771e4d5b153`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_journey-c62b9caef1388aaea0a3">[ ] unverified</a> | <a href="#case-in_game_journey-307cbadb079dad219d9c">[ ] unverified</a> | <a href="#case-in_game_journey-dcc1874650e53c4cd2f7">[ ] unverified</a> | <a href="#case-in_game_journey-863dcfbe96edc1135010">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_journey-c62b9caef1388aaea0a3"></a>

**0° CCW: unverified** — `in_game_journey-c62b9caef1388aaea0a3`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-307cbadb079dad219d9c"></a>

**90° CCW: unverified** — `in_game_journey-307cbadb079dad219d9c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-dcc1874650e53c4cd2f7"></a>

**180° CCW: unverified** — `in_game_journey-dcc1874650e53c4cd2f7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-863dcfbe96edc1135010"></a>

**270° CCW: unverified** — `in_game_journey-863dcfbe96edc1135010`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
