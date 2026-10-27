# HSR L2 Merge 90 Degree Compact

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR L2 Merge 90 Degree Compact. Fixed click-to-place piece in a 2 by 2 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `interchange-hsr-merge-90-compact`.

Footprint: **2 × 2 tiles**. Exact menu name: **HSR L2 Merge 90 Degree Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR L2 Merge 90 Degree Compact](previews/preview.png)

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
| `Sout` | hsr / 7 / primary | out | [-2.0, -24.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -24.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Bin` | hsr / 7 / primary | in | [24.0, -16.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-ac60d237d23f01143255` |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-hsr-merge-90-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-hsr-merge-90-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-373e9173ace56751464d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-373e9173ace56751464d"></a>

**General: unverified** — `software_resources-373e9173ace56751464d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-373e9173ace56751464d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-373e9173ace56751464d"></a>

**General: unverified** — `software_connectivity-373e9173ace56751464d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-hsr-merge-90-compact:canonical-southeast | <a href="#case-preview_review-d3516b31824884564d2e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-hsr-merge-90-compact:canonical-southeast</summary>

<a id="case-preview_review-d3516b31824884564d2e"></a>

**General: unverified** — `preview_review-d3516b31824884564d2e`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-hsr-merge-90-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-df3394488f6681570613">[ ] unverified</a> | <a href="#case-in_game_render-163bda22499050ef9f87">[ ] unverified</a> | <a href="#case-in_game_render-bec74974c2cb8ef5e1cd">[ ] unverified</a> | <a href="#case-in_game_render-fb5e8b6e1483fa4737d9">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-df3394488f6681570613"></a>

**0° CCW: unverified** — `in_game_render-df3394488f6681570613`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-163bda22499050ef9f87"></a>

**90° CCW: unverified** — `in_game_render-163bda22499050ef9f87`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-bec74974c2cb8ef5e1cd"></a>

**180° CCW: unverified** — `in_game_render-bec74974c2cb8ef5e1cd`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-fb5e8b6e1483fa4737d9"></a>

**270° CCW: unverified** — `in_game_render-fb5e8b6e1483fa4737d9`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-df3394488f6681570613">[ ] unverified</a> | <a href="#case-in_game_placement-163bda22499050ef9f87">[ ] unverified</a> | <a href="#case-in_game_placement-bec74974c2cb8ef5e1cd">[ ] unverified</a> | <a href="#case-in_game_placement-fb5e8b6e1483fa4737d9">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-df3394488f6681570613"></a>

**0° CCW: unverified** — `in_game_placement-df3394488f6681570613`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-163bda22499050ef9f87"></a>

**90° CCW: unverified** — `in_game_placement-163bda22499050ef9f87`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-bec74974c2cb8ef5e1cd"></a>

**180° CCW: unverified** — `in_game_placement-bec74974c2cb8ef5e1cd`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-fb5e8b6e1483fa4737d9"></a>

**270° CCW: unverified** — `in_game_placement-fb5e8b6e1483fa4737d9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-df3394488f6681570613">[ ] unverified</a> | <a href="#case-in_game_demolition-163bda22499050ef9f87">[ ] unverified</a> | <a href="#case-in_game_demolition-bec74974c2cb8ef5e1cd">[ ] unverified</a> | <a href="#case-in_game_demolition-fb5e8b6e1483fa4737d9">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-df3394488f6681570613"></a>

**0° CCW: unverified** — `in_game_demolition-df3394488f6681570613`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-163bda22499050ef9f87"></a>

**90° CCW: unverified** — `in_game_demolition-163bda22499050ef9f87`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-bec74974c2cb8ef5e1cd"></a>

**180° CCW: unverified** — `in_game_demolition-bec74974c2cb8ef5e1cd`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-fb5e8b6e1483fa4737d9"></a>

**270° CCW: unverified** — `in_game_demolition-fb5e8b6e1483fa4737d9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-df3394488f6681570613">[ ] unverified</a> | <a href="#case-in_game_save_reload-163bda22499050ef9f87">[ ] unverified</a> | <a href="#case-in_game_save_reload-bec74974c2cb8ef5e1cd">[ ] unverified</a> | <a href="#case-in_game_save_reload-fb5e8b6e1483fa4737d9">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-df3394488f6681570613"></a>

**0° CCW: unverified** — `in_game_save_reload-df3394488f6681570613`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-163bda22499050ef9f87"></a>

**90° CCW: unverified** — `in_game_save_reload-163bda22499050ef9f87`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-bec74974c2cb8ef5e1cd"></a>

**180° CCW: unverified** — `in_game_save_reload-bec74974c2cb8ef5e1cd`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-fb5e8b6e1483fa4737d9"></a>

**270° CCW: unverified** — `in_game_save_reload-fb5e8b6e1483fa4737d9`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-b858dc0516d080f80fb6">[ ] unverified</a> | <a href="#case-in_game_journey-cf09f1565c63b1c0d938">[ ] unverified</a> | <a href="#case-in_game_journey-743ecaa17e7e9cc68563">[ ] unverified</a> | <a href="#case-in_game_journey-5ef49f096b89604d3224">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-98e5c5b215d3a34d11e2">[ ] unverified</a> | <a href="#case-in_game_journey-9f458c21cad01d53511e">[ ] unverified</a> | <a href="#case-in_game_journey-4e07bfe6710e97b2db8b">[ ] unverified</a> | <a href="#case-in_game_journey-85f47b1e1b20d1434c80">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-0255ebd8107a89fe51bc">[ ] unverified</a> | <a href="#case-in_game_journey-b93cb2123d367df431a1">[ ] unverified</a> | <a href="#case-in_game_journey-e0e95b336d8109780072">[ ] unverified</a> | <a href="#case-in_game_journey-e78f5aa65966f6a1f8c1">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-b858dc0516d080f80fb6"></a>

**0° CCW: unverified** — `in_game_journey-b858dc0516d080f80fb6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-cf09f1565c63b1c0d938"></a>

**90° CCW: unverified** — `in_game_journey-cf09f1565c63b1c0d938`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-743ecaa17e7e9cc68563"></a>

**180° CCW: unverified** — `in_game_journey-743ecaa17e7e9cc68563`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-5ef49f096b89604d3224"></a>

**270° CCW: unverified** — `in_game_journey-5ef49f096b89604d3224`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-98e5c5b215d3a34d11e2"></a>

**0° CCW: unverified** — `in_game_journey-98e5c5b215d3a34d11e2`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-9f458c21cad01d53511e"></a>

**90° CCW: unverified** — `in_game_journey-9f458c21cad01d53511e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-4e07bfe6710e97b2db8b"></a>

**180° CCW: unverified** — `in_game_journey-4e07bfe6710e97b2db8b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-85f47b1e1b20d1434c80"></a>

**270° CCW: unverified** — `in_game_journey-85f47b1e1b20d1434c80`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-0255ebd8107a89fe51bc"></a>

**0° CCW: unverified** — `in_game_journey-0255ebd8107a89fe51bc`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-b93cb2123d367df431a1"></a>

**90° CCW: unverified** — `in_game_journey-b93cb2123d367df431a1`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-e0e95b336d8109780072"></a>

**180° CCW: unverified** — `in_game_journey-e0e95b336d8109780072`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-e78f5aa65966f6a1f8c1"></a>

**270° CCW: unverified** — `in_game_journey-e78f5aa65966f6a1f8c1`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f3d389b980043f3ec8b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfe4e56b2ae262fcd818">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64b5f3400fb40a310661">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0be7a71dedcf61970f9f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d86d47c18378d818b46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29d0dd3cea030f530aa5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f06e0418de1fb93e123a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-575d0ec1277fc8cbe444">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1bf3edc709968602f940">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a688c6900e24dbcb333f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36345ae5f0080874b7e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d1710547e38940f5c94">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f3d389b980043f3ec8b8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f3d389b980043f3ec8b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfe4e56b2ae262fcd818"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cfe4e56b2ae262fcd818`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64b5f3400fb40a310661"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-64b5f3400fb40a310661`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0be7a71dedcf61970f9f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0be7a71dedcf61970f9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d86d47c18378d818b46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d86d47c18378d818b46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29d0dd3cea030f530aa5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-29d0dd3cea030f530aa5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f06e0418de1fb93e123a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f06e0418de1fb93e123a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-575d0ec1277fc8cbe444"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-575d0ec1277fc8cbe444`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1bf3edc709968602f940"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1bf3edc709968602f940`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a688c6900e24dbcb333f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a688c6900e24dbcb333f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36345ae5f0080874b7e5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-36345ae5f0080874b7e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d1710547e38940f5c94"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6d1710547e38940f5c94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
