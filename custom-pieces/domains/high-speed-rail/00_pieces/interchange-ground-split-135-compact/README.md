# GHSR Split 135 Degree Compact

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

GHSR Split 135 Degree Compact. Fixed click-to-place piece in a 6 by 6 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `interchange-ground-split-135-compact`.

Footprint: **6 × 6 tiles**. Exact menu name: **GHSR Split 135 Degree Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![GHSR Split 135 Degree Compact](previews/preview.png)

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
| `Sout` | ghsr / 7 / primary | out | [-2.0, -88.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Nin` | ghsr / 7 / primary | in | [-2.0, 8.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Sin` | ghsr / 7 / primary | in | [2.0, -88.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Nout` | ghsr / 7 / primary | out | [2.0, 8.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Bout` | ghsr / 7 / primary | out | [88.0, -16.0, 1.0]; [0.7071067811865475, -0.7071067811865475]; 0.0 | `path-interface-6c94c39b4abd67a7479e` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr | `Nin` → `Sout` | primary |
| ghsr | `Sin` → `Bout` | primary |
| ghsr | `Sin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| ghsr / `Nin` | ghsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Nin` | ghsr / `Bout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Sin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-split-135-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-split-135-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-48c654f62ef070907e7d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-48c654f62ef070907e7d"></a>

**General: unverified** — `software_resources-48c654f62ef070907e7d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-48c654f62ef070907e7d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-48c654f62ef070907e7d"></a>

**General: unverified** — `software_connectivity-48c654f62ef070907e7d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-ground-split-135-compact:canonical-southeast | <a href="#case-preview_review-b4114fc6cb431f5c56d7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-ground-split-135-compact:canonical-southeast</summary>

<a id="case-preview_review-b4114fc6cb431f5c56d7"></a>

**General: unverified** — `preview_review-b4114fc6cb431f5c56d7`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-ground-split-135-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-634bd4a26cd3f8a1d960">[ ] unverified</a> | <a href="#case-in_game_render-a916235dcc56d5c9a3ac">[ ] unverified</a> | <a href="#case-in_game_render-593ac3eae01dd4767308">[ ] unverified</a> | <a href="#case-in_game_render-bf717a2b0e9ed9ab6d30">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-634bd4a26cd3f8a1d960"></a>

**0° CCW: unverified** — `in_game_render-634bd4a26cd3f8a1d960`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a916235dcc56d5c9a3ac"></a>

**90° CCW: unverified** — `in_game_render-a916235dcc56d5c9a3ac`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-593ac3eae01dd4767308"></a>

**180° CCW: unverified** — `in_game_render-593ac3eae01dd4767308`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-bf717a2b0e9ed9ab6d30"></a>

**270° CCW: unverified** — `in_game_render-bf717a2b0e9ed9ab6d30`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-634bd4a26cd3f8a1d960">[ ] unverified</a> | <a href="#case-in_game_placement-a916235dcc56d5c9a3ac">[ ] unverified</a> | <a href="#case-in_game_placement-593ac3eae01dd4767308">[ ] unverified</a> | <a href="#case-in_game_placement-bf717a2b0e9ed9ab6d30">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-634bd4a26cd3f8a1d960"></a>

**0° CCW: unverified** — `in_game_placement-634bd4a26cd3f8a1d960`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a916235dcc56d5c9a3ac"></a>

**90° CCW: unverified** — `in_game_placement-a916235dcc56d5c9a3ac`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-593ac3eae01dd4767308"></a>

**180° CCW: unverified** — `in_game_placement-593ac3eae01dd4767308`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-bf717a2b0e9ed9ab6d30"></a>

**270° CCW: unverified** — `in_game_placement-bf717a2b0e9ed9ab6d30`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-634bd4a26cd3f8a1d960">[ ] unverified</a> | <a href="#case-in_game_demolition-a916235dcc56d5c9a3ac">[ ] unverified</a> | <a href="#case-in_game_demolition-593ac3eae01dd4767308">[ ] unverified</a> | <a href="#case-in_game_demolition-bf717a2b0e9ed9ab6d30">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-634bd4a26cd3f8a1d960"></a>

**0° CCW: unverified** — `in_game_demolition-634bd4a26cd3f8a1d960`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a916235dcc56d5c9a3ac"></a>

**90° CCW: unverified** — `in_game_demolition-a916235dcc56d5c9a3ac`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-593ac3eae01dd4767308"></a>

**180° CCW: unverified** — `in_game_demolition-593ac3eae01dd4767308`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-bf717a2b0e9ed9ab6d30"></a>

**270° CCW: unverified** — `in_game_demolition-bf717a2b0e9ed9ab6d30`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-634bd4a26cd3f8a1d960">[ ] unverified</a> | <a href="#case-in_game_save_reload-a916235dcc56d5c9a3ac">[ ] unverified</a> | <a href="#case-in_game_save_reload-593ac3eae01dd4767308">[ ] unverified</a> | <a href="#case-in_game_save_reload-bf717a2b0e9ed9ab6d30">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-634bd4a26cd3f8a1d960"></a>

**0° CCW: unverified** — `in_game_save_reload-634bd4a26cd3f8a1d960`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a916235dcc56d5c9a3ac"></a>

**90° CCW: unverified** — `in_game_save_reload-a916235dcc56d5c9a3ac`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-593ac3eae01dd4767308"></a>

**180° CCW: unverified** — `in_game_save_reload-593ac3eae01dd4767308`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-bf717a2b0e9ed9ab6d30"></a>

**270° CCW: unverified** — `in_game_save_reload-bf717a2b0e9ed9ab6d30`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-d55fd0c0653554d00bfa">[ ] unverified</a> | <a href="#case-in_game_journey-4ed74ea73d96db5e9fde">[ ] unverified</a> | <a href="#case-in_game_journey-839f0fd7a82c936bfa83">[ ] unverified</a> | <a href="#case-in_game_journey-ddbb932a6ebe2ee177a5">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-c85d91b365beb91d6d51">[ ] unverified</a> | <a href="#case-in_game_journey-3b61ca8da6e835aeec7a">[ ] unverified</a> | <a href="#case-in_game_journey-17ab3e04e8244fe1d186">[ ] unverified</a> | <a href="#case-in_game_journey-76686dc19115e88c521d">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-81ebd5de5627b04fa4dc">[ ] unverified</a> | <a href="#case-in_game_journey-fae1210e7fe86de1d4c1">[ ] unverified</a> | <a href="#case-in_game_journey-b58dea47a314b997391a">[ ] unverified</a> | <a href="#case-in_game_journey-753f4afa16dde34bebb3">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-d55fd0c0653554d00bfa"></a>

**0° CCW: unverified** — `in_game_journey-d55fd0c0653554d00bfa`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-4ed74ea73d96db5e9fde"></a>

**90° CCW: unverified** — `in_game_journey-4ed74ea73d96db5e9fde`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-839f0fd7a82c936bfa83"></a>

**180° CCW: unverified** — `in_game_journey-839f0fd7a82c936bfa83`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-ddbb932a6ebe2ee177a5"></a>

**270° CCW: unverified** — `in_game_journey-ddbb932a6ebe2ee177a5`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-c85d91b365beb91d6d51"></a>

**0° CCW: unverified** — `in_game_journey-c85d91b365beb91d6d51`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-3b61ca8da6e835aeec7a"></a>

**90° CCW: unverified** — `in_game_journey-3b61ca8da6e835aeec7a`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-17ab3e04e8244fe1d186"></a>

**180° CCW: unverified** — `in_game_journey-17ab3e04e8244fe1d186`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-76686dc19115e88c521d"></a>

**270° CCW: unverified** — `in_game_journey-76686dc19115e88c521d`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-81ebd5de5627b04fa4dc"></a>

**0° CCW: unverified** — `in_game_journey-81ebd5de5627b04fa4dc`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-fae1210e7fe86de1d4c1"></a>

**90° CCW: unverified** — `in_game_journey-fae1210e7fe86de1d4c1`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-b58dea47a314b997391a"></a>

**180° CCW: unverified** — `in_game_journey-b58dea47a314b997391a`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-753f4afa16dde34bebb3"></a>

**270° CCW: unverified** — `in_game_journey-753f4afa16dde34bebb3`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ea236c68c33f873016ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6da98ecff078ad5c6165">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80385d30246b796b1c63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb0be88f1d9fc8fed9e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b372a2a93d79e84a3426">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fa25c6deeaa27dbfd2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2e64191f166d6d121f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a086f715ea4df1a7333a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01e42862f674a43ecf46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35847bcb9f4e2d7c479e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03627cb59c81aeb98347">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccffc4e1c36f7655346c">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ea236c68c33f873016ad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ea236c68c33f873016ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6da98ecff078ad5c6165"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6da98ecff078ad5c6165`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80385d30246b796b1c63"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-80385d30246b796b1c63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb0be88f1d9fc8fed9e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fb0be88f1d9fc8fed9e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b372a2a93d79e84a3426"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b372a2a93d79e84a3426`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fa25c6deeaa27dbfd2f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5fa25c6deeaa27dbfd2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2e64191f166d6d121f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2e64191f166d6d121f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a086f715ea4df1a7333a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a086f715ea4df1a7333a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-01e42862f674a43ecf46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01e42862f674a43ecf46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35847bcb9f4e2d7c479e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35847bcb9f4e2d7c479e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03627cb59c81aeb98347"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03627cb59c81aeb98347`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccffc4e1c36f7655346c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ccffc4e1c36f7655346c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
