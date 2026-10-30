---
title: "Testing: DD RHW-4 \u2014 Lower Diagonal Exit Branch"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Lower Diagonal Exit Branch

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Divides an outer lower-deck lane into a continuing highway lane and an off-ramp, while retaining the upper-deck through lanes. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -2.099767, 7.5]; [-0.9990856163918183, -0.042754311115729825]; 0.0 | `path-interface-f40f342499965fc0b115` |
| `1-S-out-2` | road / 1 / primary | out | [-3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-S-in-3` | road / 1 / primary | in | [-3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-S-out-4` | road / 1 / primary | out | [3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-S-in-5` | road / 1 / primary | in | [3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-E-in-6` | road / 1 / primary | in | [8.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-E-out-7` | road / 1 / primary | out | [8.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-E-in-8` | road / 1 / primary | in | [8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-E-out-9` | road / 1 / primary | out | [8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-S-in-3` → `1-E-out-9` | primary |
| road | `1-S-in-5` → `1-E-out-7` | primary |
| road | `1-E-in-6` → `1-S-out-4` | primary |
| road | `1-E-in-8` → `1-W-out-1` | primary |
| road | `1-E-in-8` → `1-S-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-S-in-3` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-lower-exit-branch --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The current assembly’s executed checks and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/20 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/20 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 120, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-lower-exit-branch/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-lower-exit-branch/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-3ebcbed25c5595ba6d82">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-3ebcbed25c5595ba6d82"></a>

**General: unverified** — `software_resources-3ebcbed25c5595ba6d82`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-3ebcbed25c5595ba6d82">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-3ebcbed25c5595ba6d82"></a>

**General: unverified** — `software_connectivity-3ebcbed25c5595ba6d82`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-79c849dc4c10c431d268">[ ] unverified</a> | <a href="#case-in_game_render-dfccb89bd56422c97c31">[ ] unverified</a> | <a href="#case-in_game_render-ebb6d8f77d8506f62e05">[ ] unverified</a> | <a href="#case-in_game_render-0b20ffd6bb1f6ab70036">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-79c849dc4c10c431d268"></a>

**0° CCW: unverified** — `in_game_render-79c849dc4c10c431d268`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-dfccb89bd56422c97c31"></a>

**90° CCW: unverified** — `in_game_render-dfccb89bd56422c97c31`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ebb6d8f77d8506f62e05"></a>

**180° CCW: unverified** — `in_game_render-ebb6d8f77d8506f62e05`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0b20ffd6bb1f6ab70036"></a>

**270° CCW: unverified** — `in_game_render-0b20ffd6bb1f6ab70036`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-79c849dc4c10c431d268">[ ] unverified</a> | <a href="#case-in_game_placement-dfccb89bd56422c97c31">[ ] unverified</a> | <a href="#case-in_game_placement-ebb6d8f77d8506f62e05">[ ] unverified</a> | <a href="#case-in_game_placement-0b20ffd6bb1f6ab70036">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-79c849dc4c10c431d268"></a>

**0° CCW: unverified** — `in_game_placement-79c849dc4c10c431d268`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-dfccb89bd56422c97c31"></a>

**90° CCW: unverified** — `in_game_placement-dfccb89bd56422c97c31`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ebb6d8f77d8506f62e05"></a>

**180° CCW: unverified** — `in_game_placement-ebb6d8f77d8506f62e05`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0b20ffd6bb1f6ab70036"></a>

**270° CCW: unverified** — `in_game_placement-0b20ffd6bb1f6ab70036`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-79c849dc4c10c431d268">[ ] unverified</a> | <a href="#case-in_game_demolition-dfccb89bd56422c97c31">[ ] unverified</a> | <a href="#case-in_game_demolition-ebb6d8f77d8506f62e05">[ ] unverified</a> | <a href="#case-in_game_demolition-0b20ffd6bb1f6ab70036">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-79c849dc4c10c431d268"></a>

**0° CCW: unverified** — `in_game_demolition-79c849dc4c10c431d268`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-dfccb89bd56422c97c31"></a>

**90° CCW: unverified** — `in_game_demolition-dfccb89bd56422c97c31`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ebb6d8f77d8506f62e05"></a>

**180° CCW: unverified** — `in_game_demolition-ebb6d8f77d8506f62e05`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0b20ffd6bb1f6ab70036"></a>

**270° CCW: unverified** — `in_game_demolition-0b20ffd6bb1f6ab70036`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-79c849dc4c10c431d268">[ ] unverified</a> | <a href="#case-in_game_save_reload-dfccb89bd56422c97c31">[ ] unverified</a> | <a href="#case-in_game_save_reload-ebb6d8f77d8506f62e05">[ ] unverified</a> | <a href="#case-in_game_save_reload-0b20ffd6bb1f6ab70036">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-79c849dc4c10c431d268"></a>

**0° CCW: unverified** — `in_game_save_reload-79c849dc4c10c431d268`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-dfccb89bd56422c97c31"></a>

**90° CCW: unverified** — `in_game_save_reload-dfccb89bd56422c97c31`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ebb6d8f77d8506f62e05"></a>

**180° CCW: unverified** — `in_game_save_reload-ebb6d8f77d8506f62e05`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0b20ffd6bb1f6ab70036"></a>

**270° CCW: unverified** — `in_game_save_reload-0b20ffd6bb1f6ab70036`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9 | — | <a href="#case-in_game_route_query-0aa99c1c1ff369beb3fb">[ ] unverified</a> | <a href="#case-in_game_route_query-bd75b624e946c9a36309">[ ] unverified</a> | <a href="#case-in_game_route_query-aa7615cfa8659d532814">[ ] unverified</a> | <a href="#case-in_game_route_query-77df51a38d271e5003f5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7 | — | <a href="#case-in_game_route_query-840d38a996e14eb90296">[ ] unverified</a> | <a href="#case-in_game_route_query-62173e0b059f7d090ea7">[ ] unverified</a> | <a href="#case-in_game_route_query-95857a4b361dbaefcf24">[ ] unverified</a> | <a href="#case-in_game_route_query-edd6291eb8263bced548">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4 | — | <a href="#case-in_game_route_query-9d376fdbc347837a7bec">[ ] unverified</a> | <a href="#case-in_game_route_query-e4f5abfb0702aceaf5f8">[ ] unverified</a> | <a href="#case-in_game_route_query-0734261f39668706b0ea">[ ] unverified</a> | <a href="#case-in_game_route_query-d36ee4b3e867dd1474eb">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-5c98ad18ede2c8ea0dd0">[ ] unverified</a> | <a href="#case-in_game_route_query-c5103c8c4052e1f9b442">[ ] unverified</a> | <a href="#case-in_game_route_query-e67a2703bdfb993451cf">[ ] unverified</a> | <a href="#case-in_game_route_query-567cc00ff9653bd6c0c3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2 | — | <a href="#case-in_game_route_query-377218dbcaa7f6b480f8">[ ] unverified</a> | <a href="#case-in_game_route_query-2655978c78bbe198c74c">[ ] unverified</a> | <a href="#case-in_game_route_query-e29046cf75cf7c5a32fe">[ ] unverified</a> | <a href="#case-in_game_route_query-79f11b902eb46874e580">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9</summary>

<a id="case-in_game_route_query-0aa99c1c1ff369beb3fb"></a>

**0° CCW: unverified** — `in_game_route_query-0aa99c1c1ff369beb3fb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-bd75b624e946c9a36309"></a>

**90° CCW: unverified** — `in_game_route_query-bd75b624e946c9a36309`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-aa7615cfa8659d532814"></a>

**180° CCW: unverified** — `in_game_route_query-aa7615cfa8659d532814`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-77df51a38d271e5003f5"></a>

**270° CCW: unverified** — `in_game_route_query-77df51a38d271e5003f5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7</summary>

<a id="case-in_game_route_query-840d38a996e14eb90296"></a>

**0° CCW: unverified** — `in_game_route_query-840d38a996e14eb90296`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-62173e0b059f7d090ea7"></a>

**90° CCW: unverified** — `in_game_route_query-62173e0b059f7d090ea7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-95857a4b361dbaefcf24"></a>

**180° CCW: unverified** — `in_game_route_query-95857a4b361dbaefcf24`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-edd6291eb8263bced548"></a>

**270° CCW: unverified** — `in_game_route_query-edd6291eb8263bced548`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4</summary>

<a id="case-in_game_route_query-9d376fdbc347837a7bec"></a>

**0° CCW: unverified** — `in_game_route_query-9d376fdbc347837a7bec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-e4f5abfb0702aceaf5f8"></a>

**90° CCW: unverified** — `in_game_route_query-e4f5abfb0702aceaf5f8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-0734261f39668706b0ea"></a>

**180° CCW: unverified** — `in_game_route_query-0734261f39668706b0ea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-d36ee4b3e867dd1474eb"></a>

**270° CCW: unverified** — `in_game_route_query-d36ee4b3e867dd1474eb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-5c98ad18ede2c8ea0dd0"></a>

**0° CCW: unverified** — `in_game_route_query-5c98ad18ede2c8ea0dd0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-c5103c8c4052e1f9b442"></a>

**90° CCW: unverified** — `in_game_route_query-c5103c8c4052e1f9b442`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-e67a2703bdfb993451cf"></a>

**180° CCW: unverified** — `in_game_route_query-e67a2703bdfb993451cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-567cc00ff9653bd6c0c3"></a>

**270° CCW: unverified** — `in_game_route_query-567cc00ff9653bd6c0c3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2</summary>

<a id="case-in_game_route_query-377218dbcaa7f6b480f8"></a>

**0° CCW: unverified** — `in_game_route_query-377218dbcaa7f6b480f8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2.

No observation recorded.

<a id="case-in_game_route_query-2655978c78bbe198c74c"></a>

**90° CCW: unverified** — `in_game_route_query-2655978c78bbe198c74c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2.

No observation recorded.

<a id="case-in_game_route_query-e29046cf75cf7c5a32fe"></a>

**180° CCW: unverified** — `in_game_route_query-e29046cf75cf7c5a32fe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2.

No observation recorded.

<a id="case-in_game_route_query-79f11b902eb46874e580"></a>

**270° CCW: unverified** — `in_game_route_query-79f11b902eb46874e580`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9 | — | <a href="#case-in_game_visible_travel-0aa99c1c1ff369beb3fb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bd75b624e946c9a36309">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aa7615cfa8659d532814">[ ] unverified</a> | <a href="#case-in_game_visible_travel-77df51a38d271e5003f5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7 | — | <a href="#case-in_game_visible_travel-840d38a996e14eb90296">[ ] unverified</a> | <a href="#case-in_game_visible_travel-62173e0b059f7d090ea7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-95857a4b361dbaefcf24">[ ] unverified</a> | <a href="#case-in_game_visible_travel-edd6291eb8263bced548">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4 | — | <a href="#case-in_game_visible_travel-9d376fdbc347837a7bec">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e4f5abfb0702aceaf5f8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0734261f39668706b0ea">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d36ee4b3e867dd1474eb">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-5c98ad18ede2c8ea0dd0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c5103c8c4052e1f9b442">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e67a2703bdfb993451cf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-567cc00ff9653bd6c0c3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2 | — | <a href="#case-in_game_visible_travel-377218dbcaa7f6b480f8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2655978c78bbe198c74c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e29046cf75cf7c5a32fe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-79f11b902eb46874e580">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9</summary>

<a id="case-in_game_visible_travel-0aa99c1c1ff369beb3fb"></a>

**0° CCW: unverified** — `in_game_visible_travel-0aa99c1c1ff369beb3fb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-bd75b624e946c9a36309"></a>

**90° CCW: unverified** — `in_game_visible_travel-bd75b624e946c9a36309`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-aa7615cfa8659d532814"></a>

**180° CCW: unverified** — `in_game_visible_travel-aa7615cfa8659d532814`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-77df51a38d271e5003f5"></a>

**270° CCW: unverified** — `in_game_visible_travel-77df51a38d271e5003f5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7</summary>

<a id="case-in_game_visible_travel-840d38a996e14eb90296"></a>

**0° CCW: unverified** — `in_game_visible_travel-840d38a996e14eb90296`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-62173e0b059f7d090ea7"></a>

**90° CCW: unverified** — `in_game_visible_travel-62173e0b059f7d090ea7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-95857a4b361dbaefcf24"></a>

**180° CCW: unverified** — `in_game_visible_travel-95857a4b361dbaefcf24`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-edd6291eb8263bced548"></a>

**270° CCW: unverified** — `in_game_visible_travel-edd6291eb8263bced548`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4</summary>

<a id="case-in_game_visible_travel-9d376fdbc347837a7bec"></a>

**0° CCW: unverified** — `in_game_visible_travel-9d376fdbc347837a7bec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-e4f5abfb0702aceaf5f8"></a>

**90° CCW: unverified** — `in_game_visible_travel-e4f5abfb0702aceaf5f8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-0734261f39668706b0ea"></a>

**180° CCW: unverified** — `in_game_visible_travel-0734261f39668706b0ea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-d36ee4b3e867dd1474eb"></a>

**270° CCW: unverified** — `in_game_visible_travel-d36ee4b3e867dd1474eb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-5c98ad18ede2c8ea0dd0"></a>

**0° CCW: unverified** — `in_game_visible_travel-5c98ad18ede2c8ea0dd0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-c5103c8c4052e1f9b442"></a>

**90° CCW: unverified** — `in_game_visible_travel-c5103c8c4052e1f9b442`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-e67a2703bdfb993451cf"></a>

**180° CCW: unverified** — `in_game_visible_travel-e67a2703bdfb993451cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-567cc00ff9653bd6c0c3"></a>

**270° CCW: unverified** — `in_game_visible_travel-567cc00ff9653bd6c0c3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-W-out-1; entry: 1-E-in-8; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2</summary>

<a id="case-in_game_visible_travel-377218dbcaa7f6b480f8"></a>

**0° CCW: unverified** — `in_game_visible_travel-377218dbcaa7f6b480f8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-2655978c78bbe198c74c"></a>

**90° CCW: unverified** — `in_game_visible_travel-2655978c78bbe198c74c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-e29046cf75cf7c5a32fe"></a>

**180° CCW: unverified** — `in_game_visible_travel-e29046cf75cf7c5a32fe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-79f11b902eb46874e580"></a>

**270° CCW: unverified** — `in_game_visible_travel-79f11b902eb46874e580`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 60 cases; unverified: 60</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a0dfa3225a65f150d43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a179db379ff0088ad6f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-552acd5272175b555932">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d99b21fa9b0af616ca5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2a26e6f8329f6f702228">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b57b4e12eeb37cca637">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d228a862ea9a79fbf385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a829516bce2deb9038f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e98f33b8208396c2f8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5107315c8e0cd5b456e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-575603691048ddfd8102">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b84360b090d46aa63ce1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7584c718450c186ca26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0d9037efd1dc90eecba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84a9e1e4f33eae6809ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40f177dd5729d081845b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-286fca1c01bfdc4d37e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b3160768a7ae25a5b4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1cb61054ba6e81a7883">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1219356c09344085b03f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a7691ef5009df474da2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0245c173be437373c98d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f666233eb8526c78b69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8afa80b6d8c1a05ee2bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9b7961f1b49ee8d56c2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7732e407420c5c2470a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b6484adf896c2741c25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3447e3f9850f53f0d45">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e995e3f4a52027838d6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee7bf17393c28b8abf1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1971179a64a28cd424f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43077756688a2e5a1077">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4b828cf050426f2ab1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e29cba084f3ce892f3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e3ae3a58b5c393aac8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-726f74ed37aa79903731">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-98734d82783e642b1a92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7417764f65eec736e556">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63c2880e5b3e7ae5c7ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa52b3375bd940198033">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-21d56aee84df3f050eaf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-209d93277e373f6f2d60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f58b67efc2551a24632c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b3c948ef6b9d6b26c63">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a2db489dcd650e14c5b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44bbb9195572d19b493e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4645049173c7490b226f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03ccf73f70763c342add">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-81cb9ee919a18c5a5f50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-caad44ad02e1caf365f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5eb619f07e0a477975a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b724c9b6e0f6375ea39">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6758b65869592bcfd8ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50ffd508f243275e9e8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71bf2d7ce41c3ea45177">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29088a7d672c2e0e7290">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-073f74e80ccbfc5f39eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-588715baa16f85b34403">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-596449625261877fb5e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a37322ea6f933259d94">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-S-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a0dfa3225a65f150d43"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a0dfa3225a65f150d43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a179db379ff0088ad6f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a179db379ff0088ad6f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-552acd5272175b555932"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-552acd5272175b555932`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d99b21fa9b0af616ca5b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d99b21fa9b0af616ca5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-3; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2a26e6f8329f6f702228"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2a26e6f8329f6f702228`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b57b4e12eeb37cca637"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1b57b4e12eeb37cca637`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d228a862ea9a79fbf385"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d228a862ea9a79fbf385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a829516bce2deb9038f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2a829516bce2deb9038f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7e98f33b8208396c2f8a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7e98f33b8208396c2f8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5107315c8e0cd5b456e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5107315c8e0cd5b456e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-575603691048ddfd8102"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-575603691048ddfd8102`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b84360b090d46aa63ce1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b84360b090d46aa63ce1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7584c718450c186ca26"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7584c718450c186ca26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0d9037efd1dc90eecba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0d9037efd1dc90eecba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84a9e1e4f33eae6809ee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-84a9e1e4f33eae6809ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40f177dd5729d081845b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40f177dd5729d081845b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-286fca1c01bfdc4d37e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-286fca1c01bfdc4d37e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b3160768a7ae25a5b4e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b3160768a7ae25a5b4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1cb61054ba6e81a7883"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d1cb61054ba6e81a7883`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1219356c09344085b03f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1219356c09344085b03f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a7691ef5009df474da2f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a7691ef5009df474da2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0245c173be437373c98d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0245c173be437373c98d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f666233eb8526c78b69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3f666233eb8526c78b69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8afa80b6d8c1a05ee2bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8afa80b6d8c1a05ee2bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9b7961f1b49ee8d56c2e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9b7961f1b49ee8d56c2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7732e407420c5c2470a7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7732e407420c5c2470a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b6484adf896c2741c25"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3b6484adf896c2741c25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3447e3f9850f53f0d45"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a3447e3f9850f53f0d45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e995e3f4a52027838d6d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e995e3f4a52027838d6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee7bf17393c28b8abf1e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ee7bf17393c28b8abf1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1971179a64a28cd424f8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1971179a64a28cd424f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43077756688a2e5a1077"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43077756688a2e5a1077`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4b828cf050426f2ab1e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4b828cf050426f2ab1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e29cba084f3ce892f3b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e29cba084f3ce892f3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e3ae3a58b5c393aac8f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5e3ae3a58b5c393aac8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-726f74ed37aa79903731"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-726f74ed37aa79903731`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-98734d82783e642b1a92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-98734d82783e642b1a92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7417764f65eec736e556"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7417764f65eec736e556`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63c2880e5b3e7ae5c7ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63c2880e5b3e7ae5c7ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa52b3375bd940198033"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aa52b3375bd940198033`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-21d56aee84df3f050eaf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-21d56aee84df3f050eaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-209d93277e373f6f2d60"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-209d93277e373f6f2d60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f58b67efc2551a24632c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f58b67efc2551a24632c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b3c948ef6b9d6b26c63"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b3c948ef6b9d6b26c63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a2db489dcd650e14c5b9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a2db489dcd650e14c5b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44bbb9195572d19b493e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-44bbb9195572d19b493e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4645049173c7490b226f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4645049173c7490b226f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03ccf73f70763c342add"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03ccf73f70763c342add`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-81cb9ee919a18c5a5f50"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81cb9ee919a18c5a5f50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-caad44ad02e1caf365f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-caad44ad02e1caf365f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5eb619f07e0a477975a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f5eb619f07e0a477975a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b724c9b6e0f6375ea39"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b724c9b6e0f6375ea39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6758b65869592bcfd8ff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6758b65869592bcfd8ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50ffd508f243275e9e8a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-50ffd508f243275e9e8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71bf2d7ce41c3ea45177"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-71bf2d7ce41c3ea45177`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29088a7d672c2e0e7290"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-29088a7d672c2e0e7290`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-073f74e80ccbfc5f39eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-073f74e80ccbfc5f39eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-588715baa16f85b34403"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-588715baa16f85b34403`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-596449625261877fb5e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-596449625261877fb5e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a37322ea6f933259d94"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5a37322ea6f933259d94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-exit-branch:canonical-southeast | <a href="#case-preview_review-9c59cd078de8ea91f587">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-exit-branch:canonical-top | <a href="#case-preview_review-cdee898cbe2d0b150e7f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-exit-branch:canonical-southeast</summary>

<a id="case-preview_review-9c59cd078de8ea91f587"></a>

**General: unverified** — `preview_review-9c59cd078de8ea91f587`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-lower-exit-branch:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-exit-branch:canonical-top</summary>

<a id="case-preview_review-cdee898cbe2d0b150e7f"></a>

**General: unverified** — `preview_review-cdee898cbe2d0b150e7f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-lower-exit-branch:canonical-top.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
