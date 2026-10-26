# GHSR Merge 135 Degree Wide

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

GHSR Merge 135 Degree Wide. Fixed click-to-place piece in a 12 by 13 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `interchange-ground-merge-135-wide`.

Footprint: **12 × 13 tiles**. Exact menu name: **GHSR Merge 135 Degree Wide**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![GHSR Merge 135 Degree Wide](preview.png)

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
| `Sout` | ghsr / 7 / primary | out | [-2.0, -184.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Nin` | ghsr / 7 / primary | in | [-2.0, 8.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Sin` | ghsr / 7 / primary | in | [2.0, -184.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Nout` | ghsr / 7 / primary | out | [2.0, 8.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Bin` | ghsr / 7 / primary | in | [184.0, -144.0, 1.0]; [-0.7071067811865475, -0.7071067811865475]; 0.0 | `path-interface-f99fce9a9cdaf09202fb` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr | `Nin` → `Sout` | primary |
| ghsr | `Sin` → `Nout` | primary |
| ghsr | `Bin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| ghsr / `Nin` | ghsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Sin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Bin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-merge-135-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-merge-135-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-df0c6042fc524ecd218c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-df0c6042fc524ecd218c"></a>

**General: unverified** — `software_resources-df0c6042fc524ecd218c`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-df0c6042fc524ecd218c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-df0c6042fc524ecd218c"></a>

**General: unverified** — `software_connectivity-df0c6042fc524ecd218c`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-ground-merge-135-wide:canonical-southeast | <a href="#case-preview_review-7910b0bab5df22bbfa66">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-ground-merge-135-wide:canonical-southeast</summary>

<a id="case-preview_review-7910b0bab5df22bbfa66"></a>

**General: unverified** — `preview_review-7910b0bab5df22bbfa66`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-ground-merge-135-wide:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-c4814fd0cfddd33a2e31">[ ] unverified</a> | <a href="#case-in_game_render-27f67b808fc11e56d05b">[ ] unverified</a> | <a href="#case-in_game_render-96bd8ee58ef04cd789df">[ ] unverified</a> | <a href="#case-in_game_render-270502b7270efad97a11">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-c4814fd0cfddd33a2e31"></a>

**0° CCW: unverified** — `in_game_render-c4814fd0cfddd33a2e31`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-27f67b808fc11e56d05b"></a>

**90° CCW: unverified** — `in_game_render-27f67b808fc11e56d05b`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-96bd8ee58ef04cd789df"></a>

**180° CCW: unverified** — `in_game_render-96bd8ee58ef04cd789df`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-270502b7270efad97a11"></a>

**270° CCW: unverified** — `in_game_render-270502b7270efad97a11`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-c4814fd0cfddd33a2e31">[ ] unverified</a> | <a href="#case-in_game_placement-27f67b808fc11e56d05b">[ ] unverified</a> | <a href="#case-in_game_placement-96bd8ee58ef04cd789df">[ ] unverified</a> | <a href="#case-in_game_placement-270502b7270efad97a11">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-c4814fd0cfddd33a2e31"></a>

**0° CCW: unverified** — `in_game_placement-c4814fd0cfddd33a2e31`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-27f67b808fc11e56d05b"></a>

**90° CCW: unverified** — `in_game_placement-27f67b808fc11e56d05b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-96bd8ee58ef04cd789df"></a>

**180° CCW: unverified** — `in_game_placement-96bd8ee58ef04cd789df`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-270502b7270efad97a11"></a>

**270° CCW: unverified** — `in_game_placement-270502b7270efad97a11`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-c4814fd0cfddd33a2e31">[ ] unverified</a> | <a href="#case-in_game_demolition-27f67b808fc11e56d05b">[ ] unverified</a> | <a href="#case-in_game_demolition-96bd8ee58ef04cd789df">[ ] unverified</a> | <a href="#case-in_game_demolition-270502b7270efad97a11">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-c4814fd0cfddd33a2e31"></a>

**0° CCW: unverified** — `in_game_demolition-c4814fd0cfddd33a2e31`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-27f67b808fc11e56d05b"></a>

**90° CCW: unverified** — `in_game_demolition-27f67b808fc11e56d05b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-96bd8ee58ef04cd789df"></a>

**180° CCW: unverified** — `in_game_demolition-96bd8ee58ef04cd789df`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-270502b7270efad97a11"></a>

**270° CCW: unverified** — `in_game_demolition-270502b7270efad97a11`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-c4814fd0cfddd33a2e31">[ ] unverified</a> | <a href="#case-in_game_save_reload-27f67b808fc11e56d05b">[ ] unverified</a> | <a href="#case-in_game_save_reload-96bd8ee58ef04cd789df">[ ] unverified</a> | <a href="#case-in_game_save_reload-270502b7270efad97a11">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-c4814fd0cfddd33a2e31"></a>

**0° CCW: unverified** — `in_game_save_reload-c4814fd0cfddd33a2e31`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-27f67b808fc11e56d05b"></a>

**90° CCW: unverified** — `in_game_save_reload-27f67b808fc11e56d05b`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-96bd8ee58ef04cd789df"></a>

**180° CCW: unverified** — `in_game_save_reload-96bd8ee58ef04cd789df`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-270502b7270efad97a11"></a>

**270° CCW: unverified** — `in_game_save_reload-270502b7270efad97a11`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-732b24052be1da487200">[ ] unverified</a> | <a href="#case-in_game_journey-9a4e9ca39832cbf2de7c">[ ] unverified</a> | <a href="#case-in_game_journey-fe42d8992d3876139975">[ ] unverified</a> | <a href="#case-in_game_journey-935fb5a28d8d5b88d4fd">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-7b31c2808019013e40e0">[ ] unverified</a> | <a href="#case-in_game_journey-229434b8b2336e234173">[ ] unverified</a> | <a href="#case-in_game_journey-1ede8cf5c4736f9ed6dc">[ ] unverified</a> | <a href="#case-in_game_journey-bf17053d2c482ebdb23a">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-580ce49c0d10c51e4474">[ ] unverified</a> | <a href="#case-in_game_journey-1761a8f5c479895d14c7">[ ] unverified</a> | <a href="#case-in_game_journey-2938db3c8fea1e811c5f">[ ] unverified</a> | <a href="#case-in_game_journey-b0fbd15435a8213e0906">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-732b24052be1da487200"></a>

**0° CCW: unverified** — `in_game_journey-732b24052be1da487200`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-9a4e9ca39832cbf2de7c"></a>

**90° CCW: unverified** — `in_game_journey-9a4e9ca39832cbf2de7c`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-fe42d8992d3876139975"></a>

**180° CCW: unverified** — `in_game_journey-fe42d8992d3876139975`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-935fb5a28d8d5b88d4fd"></a>

**270° CCW: unverified** — `in_game_journey-935fb5a28d8d5b88d4fd`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-7b31c2808019013e40e0"></a>

**0° CCW: unverified** — `in_game_journey-7b31c2808019013e40e0`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-229434b8b2336e234173"></a>

**90° CCW: unverified** — `in_game_journey-229434b8b2336e234173`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-1ede8cf5c4736f9ed6dc"></a>

**180° CCW: unverified** — `in_game_journey-1ede8cf5c4736f9ed6dc`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-bf17053d2c482ebdb23a"></a>

**270° CCW: unverified** — `in_game_journey-bf17053d2c482ebdb23a`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-580ce49c0d10c51e4474"></a>

**0° CCW: unverified** — `in_game_journey-580ce49c0d10c51e4474`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-1761a8f5c479895d14c7"></a>

**90° CCW: unverified** — `in_game_journey-1761a8f5c479895d14c7`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-2938db3c8fea1e811c5f"></a>

**180° CCW: unverified** — `in_game_journey-2938db3c8fea1e811c5f`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-b0fbd15435a8213e0906"></a>

**270° CCW: unverified** — `in_game_journey-b0fbd15435a8213e0906`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cbd96532db2d2b129948">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c6723b2cb79861d29ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc6dae895f2c7a7c2e2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5d4a0b8fe40dfc4a734">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12a1955cfa07e42306eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19d8556c49ca8fc9cb72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfa6e7383d277ed3119a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f12f47f854b7b07a3fc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-552ff36e7c92a83dd075">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dffc8515cda72f919095">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33f94373ec9b44523da5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6a3c81e2db08c923939">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cbd96532db2d2b129948"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cbd96532db2d2b129948`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c6723b2cb79861d29ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c6723b2cb79861d29ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc6dae895f2c7a7c2e2b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cc6dae895f2c7a7c2e2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5d4a0b8fe40dfc4a734"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b5d4a0b8fe40dfc4a734`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12a1955cfa07e42306eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12a1955cfa07e42306eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19d8556c49ca8fc9cb72"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-19d8556c49ca8fc9cb72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfa6e7383d277ed3119a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bfa6e7383d277ed3119a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f12f47f854b7b07a3fc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6f12f47f854b7b07a3fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-552ff36e7c92a83dd075"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-552ff36e7c92a83dd075`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dffc8515cda72f919095"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dffc8515cda72f919095`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33f94373ec9b44523da5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-33f94373ec9b44523da5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6a3c81e2db08c923939"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d6a3c81e2db08c923939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
