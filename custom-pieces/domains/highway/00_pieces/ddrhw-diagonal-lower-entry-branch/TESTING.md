---
title: "Testing: DD RHW-4 \u2014 Lower Diagonal Entry Branch"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Lower Diagonal Entry Branch

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Merges a ramp into an outer lower-deck lane, while retaining the upper-deck through lanes. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-S-out-1` | road / 1 / primary | out | [-3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-S-in-2` | road / 1 / primary | in | [-3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-3` | road / 1 / primary | in | [2.099767, 8.0, 7.5]; [-0.042754311115729825, -0.9990856163918183]; 0.0 | `path-interface-5c91dc69e8e07ebc1c39` |
| `1-S-out-4` | road / 1 / primary | out | [3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-S-in-5` | road / 1 / primary | in | [3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-E-in-6` | road / 1 / primary | in | [8.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-E-out-7` | road / 1 / primary | out | [8.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-E-in-8` | road / 1 / primary | in | [8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-E-out-9` | road / 1 / primary | out | [8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-S-in-2` → `1-E-out-9` | primary |
| road | `1-N-in-3` → `1-S-out-1` | primary |
| road | `1-S-in-5` → `1-E-out-7` | primary |
| road | `1-E-in-6` → `1-S-out-4` | primary |
| road | `1-E-in-8` → `1-S-out-1` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-S-in-2` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-lower-entry-branch --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-lower-entry-branch/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-lower-entry-branch/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0d8e83cbc22de1b2fb83">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0d8e83cbc22de1b2fb83"></a>

**General: unverified** — `software_resources-0d8e83cbc22de1b2fb83`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0d8e83cbc22de1b2fb83">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0d8e83cbc22de1b2fb83"></a>

**General: unverified** — `software_connectivity-0d8e83cbc22de1b2fb83`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-508b180723f876d0dff8">[ ] unverified</a> | <a href="#case-in_game_render-749bb105670e75a42be7">[ ] unverified</a> | <a href="#case-in_game_render-e59db242e59c15b61a3b">[ ] unverified</a> | <a href="#case-in_game_render-fd39a9f250add7771b1b">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-508b180723f876d0dff8"></a>

**0° CCW: unverified** — `in_game_render-508b180723f876d0dff8`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-749bb105670e75a42be7"></a>

**90° CCW: unverified** — `in_game_render-749bb105670e75a42be7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e59db242e59c15b61a3b"></a>

**180° CCW: unverified** — `in_game_render-e59db242e59c15b61a3b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-fd39a9f250add7771b1b"></a>

**270° CCW: unverified** — `in_game_render-fd39a9f250add7771b1b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-508b180723f876d0dff8">[ ] unverified</a> | <a href="#case-in_game_placement-749bb105670e75a42be7">[ ] unverified</a> | <a href="#case-in_game_placement-e59db242e59c15b61a3b">[ ] unverified</a> | <a href="#case-in_game_placement-fd39a9f250add7771b1b">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-508b180723f876d0dff8"></a>

**0° CCW: unverified** — `in_game_placement-508b180723f876d0dff8`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-749bb105670e75a42be7"></a>

**90° CCW: unverified** — `in_game_placement-749bb105670e75a42be7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e59db242e59c15b61a3b"></a>

**180° CCW: unverified** — `in_game_placement-e59db242e59c15b61a3b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-fd39a9f250add7771b1b"></a>

**270° CCW: unverified** — `in_game_placement-fd39a9f250add7771b1b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-508b180723f876d0dff8">[ ] unverified</a> | <a href="#case-in_game_demolition-749bb105670e75a42be7">[ ] unverified</a> | <a href="#case-in_game_demolition-e59db242e59c15b61a3b">[ ] unverified</a> | <a href="#case-in_game_demolition-fd39a9f250add7771b1b">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-508b180723f876d0dff8"></a>

**0° CCW: unverified** — `in_game_demolition-508b180723f876d0dff8`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-749bb105670e75a42be7"></a>

**90° CCW: unverified** — `in_game_demolition-749bb105670e75a42be7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e59db242e59c15b61a3b"></a>

**180° CCW: unverified** — `in_game_demolition-e59db242e59c15b61a3b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-fd39a9f250add7771b1b"></a>

**270° CCW: unverified** — `in_game_demolition-fd39a9f250add7771b1b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-508b180723f876d0dff8">[ ] unverified</a> | <a href="#case-in_game_save_reload-749bb105670e75a42be7">[ ] unverified</a> | <a href="#case-in_game_save_reload-e59db242e59c15b61a3b">[ ] unverified</a> | <a href="#case-in_game_save_reload-fd39a9f250add7771b1b">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-508b180723f876d0dff8"></a>

**0° CCW: unverified** — `in_game_save_reload-508b180723f876d0dff8`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-749bb105670e75a42be7"></a>

**90° CCW: unverified** — `in_game_save_reload-749bb105670e75a42be7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e59db242e59c15b61a3b"></a>

**180° CCW: unverified** — `in_game_save_reload-e59db242e59c15b61a3b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-fd39a9f250add7771b1b"></a>

**270° CCW: unverified** — `in_game_save_reload-fd39a9f250add7771b1b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9 | — | <a href="#case-in_game_route_query-4fc2e884fcbb60abe4a2">[ ] unverified</a> | <a href="#case-in_game_route_query-0ee77b68ac662ef5ced5">[ ] unverified</a> | <a href="#case-in_game_route_query-8a4a464c634bdc031b5f">[ ] unverified</a> | <a href="#case-in_game_route_query-4b6a305eba1f81539ed8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1 | — | <a href="#case-in_game_route_query-6a5479bb2d392966d840">[ ] unverified</a> | <a href="#case-in_game_route_query-7c083aee796e26262d84">[ ] unverified</a> | <a href="#case-in_game_route_query-e627e289986aef3cdd58">[ ] unverified</a> | <a href="#case-in_game_route_query-016679e5218ceb4b6446">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7 | — | <a href="#case-in_game_route_query-263a8f0e1f69a4ad02a4">[ ] unverified</a> | <a href="#case-in_game_route_query-59e095475704dd10d936">[ ] unverified</a> | <a href="#case-in_game_route_query-adf2c1dcce3ca47a0485">[ ] unverified</a> | <a href="#case-in_game_route_query-000186a5f435301a2261">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4 | — | <a href="#case-in_game_route_query-75b4aa8be611faf80193">[ ] unverified</a> | <a href="#case-in_game_route_query-0af8e09af8a677536921">[ ] unverified</a> | <a href="#case-in_game_route_query-aee34f26ac7d900cbd4b">[ ] unverified</a> | <a href="#case-in_game_route_query-204a54829247f31fe9ce">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1 | — | <a href="#case-in_game_route_query-b5f68983470a4bb1b9fc">[ ] unverified</a> | <a href="#case-in_game_route_query-650619ef0549ecfef054">[ ] unverified</a> | <a href="#case-in_game_route_query-e58e99c929e8fb05af44">[ ] unverified</a> | <a href="#case-in_game_route_query-f3defc125c7d35aaa1d7">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9</summary>

<a id="case-in_game_route_query-4fc2e884fcbb60abe4a2"></a>

**0° CCW: unverified** — `in_game_route_query-4fc2e884fcbb60abe4a2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-0ee77b68ac662ef5ced5"></a>

**90° CCW: unverified** — `in_game_route_query-0ee77b68ac662ef5ced5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-8a4a464c634bdc031b5f"></a>

**180° CCW: unverified** — `in_game_route_query-8a4a464c634bdc031b5f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-4b6a305eba1f81539ed8"></a>

**270° CCW: unverified** — `in_game_route_query-4b6a305eba1f81539ed8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1</summary>

<a id="case-in_game_route_query-6a5479bb2d392966d840"></a>

**0° CCW: unverified** — `in_game_route_query-6a5479bb2d392966d840`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-7c083aee796e26262d84"></a>

**90° CCW: unverified** — `in_game_route_query-7c083aee796e26262d84`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-e627e289986aef3cdd58"></a>

**180° CCW: unverified** — `in_game_route_query-e627e289986aef3cdd58`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-016679e5218ceb4b6446"></a>

**270° CCW: unverified** — `in_game_route_query-016679e5218ceb4b6446`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7</summary>

<a id="case-in_game_route_query-263a8f0e1f69a4ad02a4"></a>

**0° CCW: unverified** — `in_game_route_query-263a8f0e1f69a4ad02a4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-59e095475704dd10d936"></a>

**90° CCW: unverified** — `in_game_route_query-59e095475704dd10d936`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-adf2c1dcce3ca47a0485"></a>

**180° CCW: unverified** — `in_game_route_query-adf2c1dcce3ca47a0485`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-000186a5f435301a2261"></a>

**270° CCW: unverified** — `in_game_route_query-000186a5f435301a2261`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4</summary>

<a id="case-in_game_route_query-75b4aa8be611faf80193"></a>

**0° CCW: unverified** — `in_game_route_query-75b4aa8be611faf80193`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-0af8e09af8a677536921"></a>

**90° CCW: unverified** — `in_game_route_query-0af8e09af8a677536921`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-aee34f26ac7d900cbd4b"></a>

**180° CCW: unverified** — `in_game_route_query-aee34f26ac7d900cbd4b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-204a54829247f31fe9ce"></a>

**270° CCW: unverified** — `in_game_route_query-204a54829247f31fe9ce`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1</summary>

<a id="case-in_game_route_query-b5f68983470a4bb1b9fc"></a>

**0° CCW: unverified** — `in_game_route_query-b5f68983470a4bb1b9fc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-650619ef0549ecfef054"></a>

**90° CCW: unverified** — `in_game_route_query-650619ef0549ecfef054`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-e58e99c929e8fb05af44"></a>

**180° CCW: unverified** — `in_game_route_query-e58e99c929e8fb05af44`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-f3defc125c7d35aaa1d7"></a>

**270° CCW: unverified** — `in_game_route_query-f3defc125c7d35aaa1d7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9 | — | <a href="#case-in_game_visible_travel-4fc2e884fcbb60abe4a2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0ee77b68ac662ef5ced5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8a4a464c634bdc031b5f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4b6a305eba1f81539ed8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1 | — | <a href="#case-in_game_visible_travel-6a5479bb2d392966d840">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7c083aee796e26262d84">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e627e289986aef3cdd58">[ ] unverified</a> | <a href="#case-in_game_visible_travel-016679e5218ceb4b6446">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7 | — | <a href="#case-in_game_visible_travel-263a8f0e1f69a4ad02a4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-59e095475704dd10d936">[ ] unverified</a> | <a href="#case-in_game_visible_travel-adf2c1dcce3ca47a0485">[ ] unverified</a> | <a href="#case-in_game_visible_travel-000186a5f435301a2261">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4 | — | <a href="#case-in_game_visible_travel-75b4aa8be611faf80193">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0af8e09af8a677536921">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aee34f26ac7d900cbd4b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-204a54829247f31fe9ce">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1 | — | <a href="#case-in_game_visible_travel-b5f68983470a4bb1b9fc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-650619ef0549ecfef054">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e58e99c929e8fb05af44">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f3defc125c7d35aaa1d7">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9</summary>

<a id="case-in_game_visible_travel-4fc2e884fcbb60abe4a2"></a>

**0° CCW: unverified** — `in_game_visible_travel-4fc2e884fcbb60abe4a2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-0ee77b68ac662ef5ced5"></a>

**90° CCW: unverified** — `in_game_visible_travel-0ee77b68ac662ef5ced5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-8a4a464c634bdc031b5f"></a>

**180° CCW: unverified** — `in_game_visible_travel-8a4a464c634bdc031b5f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-4b6a305eba1f81539ed8"></a>

**270° CCW: unverified** — `in_game_visible_travel-4b6a305eba1f81539ed8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-9; entry: 1-S-in-2; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1</summary>

<a id="case-in_game_visible_travel-6a5479bb2d392966d840"></a>

**0° CCW: unverified** — `in_game_visible_travel-6a5479bb2d392966d840`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-7c083aee796e26262d84"></a>

**90° CCW: unverified** — `in_game_visible_travel-7c083aee796e26262d84`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-e627e289986aef3cdd58"></a>

**180° CCW: unverified** — `in_game_visible_travel-e627e289986aef3cdd58`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-016679e5218ceb4b6446"></a>

**270° CCW: unverified** — `in_game_visible_travel-016679e5218ceb4b6446`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-S-out-1; entry: 1-N-in-3; exit: 1-S-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7</summary>

<a id="case-in_game_visible_travel-263a8f0e1f69a4ad02a4"></a>

**0° CCW: unverified** — `in_game_visible_travel-263a8f0e1f69a4ad02a4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-59e095475704dd10d936"></a>

**90° CCW: unverified** — `in_game_visible_travel-59e095475704dd10d936`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-adf2c1dcce3ca47a0485"></a>

**180° CCW: unverified** — `in_game_visible_travel-adf2c1dcce3ca47a0485`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-000186a5f435301a2261"></a>

**270° CCW: unverified** — `in_game_visible_travel-000186a5f435301a2261`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4</summary>

<a id="case-in_game_visible_travel-75b4aa8be611faf80193"></a>

**0° CCW: unverified** — `in_game_visible_travel-75b4aa8be611faf80193`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-0af8e09af8a677536921"></a>

**90° CCW: unverified** — `in_game_visible_travel-0af8e09af8a677536921`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-aee34f26ac7d900cbd4b"></a>

**180° CCW: unverified** — `in_game_visible_travel-aee34f26ac7d900cbd4b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-204a54829247f31fe9ce"></a>

**270° CCW: unverified** — `in_game_visible_travel-204a54829247f31fe9ce`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1</summary>

<a id="case-in_game_visible_travel-b5f68983470a4bb1b9fc"></a>

**0° CCW: unverified** — `in_game_visible_travel-b5f68983470a4bb1b9fc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-650619ef0549ecfef054"></a>

**90° CCW: unverified** — `in_game_visible_travel-650619ef0549ecfef054`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-e58e99c929e8fb05af44"></a>

**180° CCW: unverified** — `in_game_visible_travel-e58e99c929e8fb05af44`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-f3defc125c7d35aaa1d7"></a>

**270° CCW: unverified** — `in_game_visible_travel-f3defc125c7d35aaa1d7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-1; entry: 1-E-in-8; exit: 1-S-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 60 cases; unverified: 60</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-78b47be1097668bd4b23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6b5bdd54eabd2131976">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6bda23266406d2654e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-704d10b4aa9a3ef34df7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aad285db8c55156224b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8928323c3ebd9abf83db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b50de60261ab4ef2fd4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-500684eda8e9fd222f8b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d78f04309410f417af5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a250cc7d8c49d98a8880">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07f557e4b5596da4bb9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8824f930218166d96c3a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a237a9496b8cf8be109f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0730f3a6bf08532b0b28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc2bf370eb73803bd1b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91bdde45d2459bdfd9cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-afd7263e6d7fdc76e6bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-438f20fa80c3e2dfee28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-618472c4f8ebe56880b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfe94db72998d9966d3f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-868622ad7b96d99a6c70">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b72cab74890bfca90c0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-536c6e7d87dbb235501c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31284849bbed48680469">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3112f1ff14ad97666ee7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6115e8b479a45e137c89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3400cde8febd73f1fe3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c34b8c13e76e10bd5ce1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f1831cc87d44bd007bfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f271beb1ed6937c15314">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfe830270c28816eed44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41dc6581f9412674f49a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fbd507de73009247786f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7616c05f72011d131173">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbf285b5916a30012051">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79146cf6a43682b8cc12">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6aa4db5a47dd28db1026">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c156d7c4d05b6e1a623">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8c48673df9bb98aa590">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1269ec80a2e0cf55cdd5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a6b1697faeeb54ee3b46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62d18cc5f767d612c3db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a44c14159f7da706de5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b17e2ce434b04185727a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eec94f21f272fcbe6dfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-337954a399b888d41e70">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-965c3e13047249be44f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d0afe351a819fd49080">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73602351a683b7b2eafb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b65cfab235e63cf2108">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5847be5a298c6a8fa755">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8edb998922bb00b32fad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f788c3a0e0182588dc85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10bc741294d668616423">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-001b4bab62a023bdee38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b079a2f4766ff78cb0de">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2723161b26dc14652f7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e4a9ae7f8f33439e8d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfc8ee4ee01d4f6a598d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e22e186e6187b6d71b8">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-78b47be1097668bd4b23"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-78b47be1097668bd4b23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6b5bdd54eabd2131976"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d6b5bdd54eabd2131976`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6bda23266406d2654e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e6bda23266406d2654e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-704d10b4aa9a3ef34df7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-704d10b4aa9a3ef34df7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aad285db8c55156224b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aad285db8c55156224b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8928323c3ebd9abf83db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8928323c3ebd9abf83db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b50de60261ab4ef2fd4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9b50de60261ab4ef2fd4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-500684eda8e9fd222f8b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-500684eda8e9fd222f8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d78f04309410f417af5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d78f04309410f417af5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a250cc7d8c49d98a8880"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a250cc7d8c49d98a8880`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07f557e4b5596da4bb9e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-07f557e4b5596da4bb9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8824f930218166d96c3a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8824f930218166d96c3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a237a9496b8cf8be109f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a237a9496b8cf8be109f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0730f3a6bf08532b0b28"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0730f3a6bf08532b0b28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc2bf370eb73803bd1b0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc2bf370eb73803bd1b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91bdde45d2459bdfd9cb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-91bdde45d2459bdfd9cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-afd7263e6d7fdc76e6bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-afd7263e6d7fdc76e6bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-438f20fa80c3e2dfee28"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-438f20fa80c3e2dfee28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-618472c4f8ebe56880b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-618472c4f8ebe56880b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfe94db72998d9966d3f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cfe94db72998d9966d3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-868622ad7b96d99a6c70"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-868622ad7b96d99a6c70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b72cab74890bfca90c0d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b72cab74890bfca90c0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-536c6e7d87dbb235501c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-536c6e7d87dbb235501c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31284849bbed48680469"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-31284849bbed48680469`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3112f1ff14ad97666ee7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3112f1ff14ad97666ee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6115e8b479a45e137c89"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6115e8b479a45e137c89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3400cde8febd73f1fe3e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3400cde8febd73f1fe3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c34b8c13e76e10bd5ce1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c34b8c13e76e10bd5ce1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f1831cc87d44bd007bfe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f1831cc87d44bd007bfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f271beb1ed6937c15314"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f271beb1ed6937c15314`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfe830270c28816eed44"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cfe830270c28816eed44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41dc6581f9412674f49a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-41dc6581f9412674f49a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fbd507de73009247786f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fbd507de73009247786f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7616c05f72011d131173"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7616c05f72011d131173`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbf285b5916a30012051"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bbf285b5916a30012051`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79146cf6a43682b8cc12"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79146cf6a43682b8cc12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6aa4db5a47dd28db1026"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6aa4db5a47dd28db1026`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c156d7c4d05b6e1a623"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c156d7c4d05b6e1a623`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8c48673df9bb98aa590"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e8c48673df9bb98aa590`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1269ec80a2e0cf55cdd5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1269ec80a2e0cf55cdd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a6b1697faeeb54ee3b46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6b1697faeeb54ee3b46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62d18cc5f767d612c3db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62d18cc5f767d612c3db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a44c14159f7da706de5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a44c14159f7da706de5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b17e2ce434b04185727a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b17e2ce434b04185727a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eec94f21f272fcbe6dfa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eec94f21f272fcbe6dfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-337954a399b888d41e70"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-337954a399b888d41e70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-965c3e13047249be44f7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-965c3e13047249be44f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d0afe351a819fd49080"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d0afe351a819fd49080`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73602351a683b7b2eafb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73602351a683b7b2eafb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b65cfab235e63cf2108"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b65cfab235e63cf2108`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5847be5a298c6a8fa755"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5847be5a298c6a8fa755`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8edb998922bb00b32fad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8edb998922bb00b32fad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f788c3a0e0182588dc85"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f788c3a0e0182588dc85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10bc741294d668616423"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-10bc741294d668616423`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-001b4bab62a023bdee38"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-001b4bab62a023bdee38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b079a2f4766ff78cb0de"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b079a2f4766ff78cb0de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2723161b26dc14652f7b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2723161b26dc14652f7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e4a9ae7f8f33439e8d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e4a9ae7f8f33439e8d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfc8ee4ee01d4f6a598d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cfc8ee4ee01d4f6a598d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e22e186e6187b6d71b8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e22e186e6187b6d71b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-entry-branch:canonical-southeast | <a href="#case-preview_review-d8842e018ca2bf56719e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-entry-branch:canonical-top | <a href="#case-preview_review-f6ceae529af51d5892a9">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-entry-branch:canonical-southeast</summary>

<a id="case-preview_review-d8842e018ca2bf56719e"></a>

**General: unverified** — `preview_review-d8842e018ca2bf56719e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-lower-entry-branch:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-entry-branch:canonical-top</summary>

<a id="case-preview_review-f6ceae529af51d5892a9"></a>

**General: unverified** — `preview_review-f6ceae529af51d5892a9`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-lower-entry-branch:canonical-top.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
