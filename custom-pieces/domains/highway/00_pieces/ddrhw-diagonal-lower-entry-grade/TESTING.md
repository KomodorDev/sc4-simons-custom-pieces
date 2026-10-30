---
title: "Testing: DD RHW-4 \u2014 Compact Lower Diagonal Entry Grade"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Compact Lower Diagonal Entry Grade

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Carries part of the lower on-ramp between its northwest surface junction and highway branch. The complete authored ramp curve is about 69.99 m long, including its level joins; its active height transition is about 35.08 m. Several components share this curve. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-S-out-1` | road / 1 / primary | out | [10.207444, -8.0, 6.745132]; [-0.2021759074179693, -0.9793492239542138]; 0.226757443 | `path-interface-ac5ba964cbefb6350eb2` |
| `1-N-in-2` | road / 1 / primary | in | [14.245568, 8.0, 3.000444]; [-0.3292115662354699, -0.9442561859245556]; 0.226761428 | `path-interface-9a0f9ddca22564095128` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-N-in-2` → `1-S-out-1` | primary |

#### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-lower-entry-grade --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/4 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 28, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-lower-entry-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-lower-entry-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-9b9104079d3b8dc15361">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-9b9104079d3b8dc15361"></a>

**General: unverified** — `software_resources-9b9104079d3b8dc15361`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-9b9104079d3b8dc15361">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-9b9104079d3b8dc15361"></a>

**General: unverified** — `software_connectivity-9b9104079d3b8dc15361`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-bd2a179fae244290a9be">[ ] unverified</a> | <a href="#case-in_game_render-5efa2bb0e42356fe2eea">[ ] unverified</a> | <a href="#case-in_game_render-fea3825d4c16ffd38755">[ ] unverified</a> | <a href="#case-in_game_render-548e2e416ad72396773e">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-bd2a179fae244290a9be"></a>

**0° CCW: unverified** — `in_game_render-bd2a179fae244290a9be`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5efa2bb0e42356fe2eea"></a>

**90° CCW: unverified** — `in_game_render-5efa2bb0e42356fe2eea`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-fea3825d4c16ffd38755"></a>

**180° CCW: unverified** — `in_game_render-fea3825d4c16ffd38755`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-548e2e416ad72396773e"></a>

**270° CCW: unverified** — `in_game_render-548e2e416ad72396773e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-bd2a179fae244290a9be">[ ] unverified</a> | <a href="#case-in_game_placement-5efa2bb0e42356fe2eea">[ ] unverified</a> | <a href="#case-in_game_placement-fea3825d4c16ffd38755">[ ] unverified</a> | <a href="#case-in_game_placement-548e2e416ad72396773e">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-bd2a179fae244290a9be"></a>

**0° CCW: unverified** — `in_game_placement-bd2a179fae244290a9be`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5efa2bb0e42356fe2eea"></a>

**90° CCW: unverified** — `in_game_placement-5efa2bb0e42356fe2eea`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-fea3825d4c16ffd38755"></a>

**180° CCW: unverified** — `in_game_placement-fea3825d4c16ffd38755`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-548e2e416ad72396773e"></a>

**270° CCW: unverified** — `in_game_placement-548e2e416ad72396773e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-bd2a179fae244290a9be">[ ] unverified</a> | <a href="#case-in_game_demolition-5efa2bb0e42356fe2eea">[ ] unverified</a> | <a href="#case-in_game_demolition-fea3825d4c16ffd38755">[ ] unverified</a> | <a href="#case-in_game_demolition-548e2e416ad72396773e">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-bd2a179fae244290a9be"></a>

**0° CCW: unverified** — `in_game_demolition-bd2a179fae244290a9be`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5efa2bb0e42356fe2eea"></a>

**90° CCW: unverified** — `in_game_demolition-5efa2bb0e42356fe2eea`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-fea3825d4c16ffd38755"></a>

**180° CCW: unverified** — `in_game_demolition-fea3825d4c16ffd38755`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-548e2e416ad72396773e"></a>

**270° CCW: unverified** — `in_game_demolition-548e2e416ad72396773e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-bd2a179fae244290a9be">[ ] unverified</a> | <a href="#case-in_game_save_reload-5efa2bb0e42356fe2eea">[ ] unverified</a> | <a href="#case-in_game_save_reload-fea3825d4c16ffd38755">[ ] unverified</a> | <a href="#case-in_game_save_reload-548e2e416ad72396773e">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-bd2a179fae244290a9be"></a>

**0° CCW: unverified** — `in_game_save_reload-bd2a179fae244290a9be`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5efa2bb0e42356fe2eea"></a>

**90° CCW: unverified** — `in_game_save_reload-5efa2bb0e42356fe2eea`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-fea3825d4c16ffd38755"></a>

**180° CCW: unverified** — `in_game_save_reload-fea3825d4c16ffd38755`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-548e2e416ad72396773e"></a>

**270° CCW: unverified** — `in_game_save_reload-548e2e416ad72396773e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1 | — | <a href="#case-in_game_route_query-e28a88dee6566c00386c">[ ] unverified</a> | <a href="#case-in_game_route_query-89871a1562d0646ea356">[ ] unverified</a> | <a href="#case-in_game_route_query-4be4434e9ceef8bf563d">[ ] unverified</a> | <a href="#case-in_game_route_query-d58024000fa573522abd">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1</summary>

<a id="case-in_game_route_query-e28a88dee6566c00386c"></a>

**0° CCW: unverified** — `in_game_route_query-e28a88dee6566c00386c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-89871a1562d0646ea356"></a>

**90° CCW: unverified** — `in_game_route_query-89871a1562d0646ea356`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-4be4434e9ceef8bf563d"></a>

**180° CCW: unverified** — `in_game_route_query-4be4434e9ceef8bf563d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-d58024000fa573522abd"></a>

**270° CCW: unverified** — `in_game_route_query-d58024000fa573522abd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1 | — | <a href="#case-in_game_visible_travel-e28a88dee6566c00386c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-89871a1562d0646ea356">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4be4434e9ceef8bf563d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d58024000fa573522abd">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1</summary>

<a id="case-in_game_visible_travel-e28a88dee6566c00386c"></a>

**0° CCW: unverified** — `in_game_visible_travel-e28a88dee6566c00386c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-89871a1562d0646ea356"></a>

**90° CCW: unverified** — `in_game_visible_travel-89871a1562d0646ea356`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-4be4434e9ceef8bf563d"></a>

**180° CCW: unverified** — `in_game_visible_travel-4be4434e9ceef8bf563d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-d58024000fa573522abd"></a>

**270° CCW: unverified** — `in_game_visible_travel-d58024000fa573522abd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-S-out-1; entry: 1-N-in-2; exit: 1-S-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-entry-grade:canonical-southeast | <a href="#case-preview_review-550b6f9d7f9d09a35f55">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-entry-grade:canonical-top | <a href="#case-preview_review-a3ce1b6149a75d9da2e8">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-entry-grade:canonical-southeast</summary>

<a id="case-preview_review-550b6f9d7f9d09a35f55"></a>

**General: unverified** — `preview_review-550b6f9d7f9d09a35f55`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-lower-entry-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-entry-grade:canonical-top</summary>

<a id="case-preview_review-a3ce1b6149a75d9da2e8"></a>

**General: unverified** — `preview_review-a3ce1b6149a75d9da2e8`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-lower-entry-grade:canonical-top.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
