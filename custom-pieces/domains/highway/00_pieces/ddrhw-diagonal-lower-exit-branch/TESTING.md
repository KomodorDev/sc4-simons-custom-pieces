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

Divides an outer lower-deck lane into a continuing highway lane and an off-ramp towards the northwest avenue access. The branch is one diagonal city-grid step farther from the avenue than in the original layout. Its barrier opening belongs to the lower deck; the upper-deck edge remains closed here. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

This branch uses a real flat auxiliary lane in the former highway shoulder, with a 12 m taper and a 4 m parallel section. Its saved driving path changes between the native outer through lane and that auxiliary lane. Native-material dashed separators and a painted split area identify the join; both highway through lanes remain available.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -10.207444, 6.745132]; [-0.9793505697049306, -0.2021693884311566]; -0.226756787 | `path-interface-20a6d5708b4a74c22702` |
| `1-S-out-2` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-S-in-3` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-S-out-4` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-S-in-5` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-E-in-6` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-E-out-7` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-E-in-8` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-E-out-9` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-S-out-10` | road / 1 / primary | out | [12.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-S-in-11` | road / 1 / primary | in | [12.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-S-out-12` | road / 1 / primary | out | [19.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-S-in-13` | road / 1 / primary | in | [19.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-E-in-14` | road / 1 / primary | in | [24.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-E-out-15` | road / 1 / primary | out | [24.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-E-in-16` | road / 1 / primary | in | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-E-out-17` | road / 1 / primary | out | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-S-in-3` → `1-E-out-9` | primary |
| road | `1-S-in-5` → `1-E-out-7` | primary |
| road | `1-E-in-6` → `1-S-out-4` | primary |
| road | `1-E-in-8` → `1-S-out-2` | primary |
| road | `1-S-in-11` → `1-E-out-17` | primary |
| road | `1-S-in-13` → `1-E-out-15` | primary |
| road | `1-E-in-14` → `1-S-out-12` | primary |
| road | `1-E-in-16` → `1-W-out-1` | primary |
| road | `1-E-in-16` → `1-S-out-10` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-S-in-3` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-3` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-5` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-lower-exit-branch --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/36 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/36 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 344, passed: 0, failed: 0, stale: 0, not_applicable: 0.

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
<summary>Route Query — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9 | — | <a href="#case-in_game_route_query-0aa99c1c1ff369beb3fb">[ ] unverified</a> | <a href="#case-in_game_route_query-bd75b624e946c9a36309">[ ] unverified</a> | <a href="#case-in_game_route_query-aa7615cfa8659d532814">[ ] unverified</a> | <a href="#case-in_game_route_query-77df51a38d271e5003f5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7 | — | <a href="#case-in_game_route_query-840d38a996e14eb90296">[ ] unverified</a> | <a href="#case-in_game_route_query-62173e0b059f7d090ea7">[ ] unverified</a> | <a href="#case-in_game_route_query-95857a4b361dbaefcf24">[ ] unverified</a> | <a href="#case-in_game_route_query-edd6291eb8263bced548">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4 | — | <a href="#case-in_game_route_query-9d376fdbc347837a7bec">[ ] unverified</a> | <a href="#case-in_game_route_query-e4f5abfb0702aceaf5f8">[ ] unverified</a> | <a href="#case-in_game_route_query-0734261f39668706b0ea">[ ] unverified</a> | <a href="#case-in_game_route_query-d36ee4b3e867dd1474eb">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2 | — | <a href="#case-in_game_route_query-377218dbcaa7f6b480f8">[ ] unverified</a> | <a href="#case-in_game_route_query-2655978c78bbe198c74c">[ ] unverified</a> | <a href="#case-in_game_route_query-e29046cf75cf7c5a32fe">[ ] unverified</a> | <a href="#case-in_game_route_query-79f11b902eb46874e580">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17 | — | <a href="#case-in_game_route_query-642e6b1a9bbba23df634">[ ] unverified</a> | <a href="#case-in_game_route_query-f93d8805a7cbdc1656d0">[ ] unverified</a> | <a href="#case-in_game_route_query-b0ee373affc7d68b6fab">[ ] unverified</a> | <a href="#case-in_game_route_query-42b502c5dfe767328c26">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15 | — | <a href="#case-in_game_route_query-34ce9b633a4d98a9fa5e">[ ] unverified</a> | <a href="#case-in_game_route_query-ed7408b5dc1b86dad8a7">[ ] unverified</a> | <a href="#case-in_game_route_query-45eb46a19f8c5a176650">[ ] unverified</a> | <a href="#case-in_game_route_query-68c8829a1fb3552391f9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12 | — | <a href="#case-in_game_route_query-c6d276507b20deeb209e">[ ] unverified</a> | <a href="#case-in_game_route_query-8ab1e565e2fb933e2a4c">[ ] unverified</a> | <a href="#case-in_game_route_query-16dc5004f7aa04b34fad">[ ] unverified</a> | <a href="#case-in_game_route_query-23154b18b80486eb2476">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-1ce4d2571808b7fdfe35">[ ] unverified</a> | <a href="#case-in_game_route_query-07142e1de95e2cdeb3ee">[ ] unverified</a> | <a href="#case-in_game_route_query-f4d99ea4e9189feef3ad">[ ] unverified</a> | <a href="#case-in_game_route_query-0bfc267e643c994705a9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10 | — | <a href="#case-in_game_route_query-09642f3ddf122d9c5dc2">[ ] unverified</a> | <a href="#case-in_game_route_query-876dd101d6c2b7ce1905">[ ] unverified</a> | <a href="#case-in_game_route_query-5eb6418ac1741bbcd022">[ ] unverified</a> | <a href="#case-in_game_route_query-9381a67027c018f603be">[ ] unverified</a> |


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


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17</summary>

<a id="case-in_game_route_query-642e6b1a9bbba23df634"></a>

**0° CCW: unverified** — `in_game_route_query-642e6b1a9bbba23df634`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-f93d8805a7cbdc1656d0"></a>

**90° CCW: unverified** — `in_game_route_query-f93d8805a7cbdc1656d0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-b0ee373affc7d68b6fab"></a>

**180° CCW: unverified** — `in_game_route_query-b0ee373affc7d68b6fab`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-42b502c5dfe767328c26"></a>

**270° CCW: unverified** — `in_game_route_query-42b502c5dfe767328c26`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15</summary>

<a id="case-in_game_route_query-34ce9b633a4d98a9fa5e"></a>

**0° CCW: unverified** — `in_game_route_query-34ce9b633a4d98a9fa5e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-ed7408b5dc1b86dad8a7"></a>

**90° CCW: unverified** — `in_game_route_query-ed7408b5dc1b86dad8a7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-45eb46a19f8c5a176650"></a>

**180° CCW: unverified** — `in_game_route_query-45eb46a19f8c5a176650`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-68c8829a1fb3552391f9"></a>

**270° CCW: unverified** — `in_game_route_query-68c8829a1fb3552391f9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12</summary>

<a id="case-in_game_route_query-c6d276507b20deeb209e"></a>

**0° CCW: unverified** — `in_game_route_query-c6d276507b20deeb209e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_route_query-8ab1e565e2fb933e2a4c"></a>

**90° CCW: unverified** — `in_game_route_query-8ab1e565e2fb933e2a4c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_route_query-16dc5004f7aa04b34fad"></a>

**180° CCW: unverified** — `in_game_route_query-16dc5004f7aa04b34fad`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_route_query-23154b18b80486eb2476"></a>

**270° CCW: unverified** — `in_game_route_query-23154b18b80486eb2476`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-1ce4d2571808b7fdfe35"></a>

**0° CCW: unverified** — `in_game_route_query-1ce4d2571808b7fdfe35`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-07142e1de95e2cdeb3ee"></a>

**90° CCW: unverified** — `in_game_route_query-07142e1de95e2cdeb3ee`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-f4d99ea4e9189feef3ad"></a>

**180° CCW: unverified** — `in_game_route_query-f4d99ea4e9189feef3ad`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-0bfc267e643c994705a9"></a>

**270° CCW: unverified** — `in_game_route_query-0bfc267e643c994705a9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10</summary>

<a id="case-in_game_route_query-09642f3ddf122d9c5dc2"></a>

**0° CCW: unverified** — `in_game_route_query-09642f3ddf122d9c5dc2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-876dd101d6c2b7ce1905"></a>

**90° CCW: unverified** — `in_game_route_query-876dd101d6c2b7ce1905`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-5eb6418ac1741bbcd022"></a>

**180° CCW: unverified** — `in_game_route_query-5eb6418ac1741bbcd022`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-9381a67027c018f603be"></a>

**270° CCW: unverified** — `in_game_route_query-9381a67027c018f603be`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-3>1-E-out-9; entry: 1-S-in-3; exit: 1-E-out-9 | — | <a href="#case-in_game_visible_travel-0aa99c1c1ff369beb3fb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bd75b624e946c9a36309">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aa7615cfa8659d532814">[ ] unverified</a> | <a href="#case-in_game_visible_travel-77df51a38d271e5003f5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-5>1-E-out-7; entry: 1-S-in-5; exit: 1-E-out-7 | — | <a href="#case-in_game_visible_travel-840d38a996e14eb90296">[ ] unverified</a> | <a href="#case-in_game_visible_travel-62173e0b059f7d090ea7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-95857a4b361dbaefcf24">[ ] unverified</a> | <a href="#case-in_game_visible_travel-edd6291eb8263bced548">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4 | — | <a href="#case-in_game_visible_travel-9d376fdbc347837a7bec">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e4f5abfb0702aceaf5f8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0734261f39668706b0ea">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d36ee4b3e867dd1474eb">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-S-out-2; entry: 1-E-in-8; exit: 1-S-out-2 | — | <a href="#case-in_game_visible_travel-377218dbcaa7f6b480f8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2655978c78bbe198c74c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e29046cf75cf7c5a32fe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-79f11b902eb46874e580">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17 | — | <a href="#case-in_game_visible_travel-642e6b1a9bbba23df634">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f93d8805a7cbdc1656d0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b0ee373affc7d68b6fab">[ ] unverified</a> | <a href="#case-in_game_visible_travel-42b502c5dfe767328c26">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15 | — | <a href="#case-in_game_visible_travel-34ce9b633a4d98a9fa5e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ed7408b5dc1b86dad8a7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-45eb46a19f8c5a176650">[ ] unverified</a> | <a href="#case-in_game_visible_travel-68c8829a1fb3552391f9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12 | — | <a href="#case-in_game_visible_travel-c6d276507b20deeb209e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8ab1e565e2fb933e2a4c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-16dc5004f7aa04b34fad">[ ] unverified</a> | <a href="#case-in_game_visible_travel-23154b18b80486eb2476">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-1ce4d2571808b7fdfe35">[ ] unverified</a> | <a href="#case-in_game_visible_travel-07142e1de95e2cdeb3ee">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f4d99ea4e9189feef3ad">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0bfc267e643c994705a9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10 | — | <a href="#case-in_game_visible_travel-09642f3ddf122d9c5dc2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-876dd101d6c2b7ce1905">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5eb6418ac1741bbcd022">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9381a67027c018f603be">[ ] unverified</a> |


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


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17</summary>

<a id="case-in_game_visible_travel-642e6b1a9bbba23df634"></a>

**0° CCW: unverified** — `in_game_visible_travel-642e6b1a9bbba23df634`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-f93d8805a7cbdc1656d0"></a>

**90° CCW: unverified** — `in_game_visible_travel-f93d8805a7cbdc1656d0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-b0ee373affc7d68b6fab"></a>

**180° CCW: unverified** — `in_game_visible_travel-b0ee373affc7d68b6fab`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-42b502c5dfe767328c26"></a>

**270° CCW: unverified** — `in_game_visible_travel-42b502c5dfe767328c26`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15</summary>

<a id="case-in_game_visible_travel-34ce9b633a4d98a9fa5e"></a>

**0° CCW: unverified** — `in_game_visible_travel-34ce9b633a4d98a9fa5e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-ed7408b5dc1b86dad8a7"></a>

**90° CCW: unverified** — `in_game_visible_travel-ed7408b5dc1b86dad8a7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-45eb46a19f8c5a176650"></a>

**180° CCW: unverified** — `in_game_visible_travel-45eb46a19f8c5a176650`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-68c8829a1fb3552391f9"></a>

**270° CCW: unverified** — `in_game_visible_travel-68c8829a1fb3552391f9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12</summary>

<a id="case-in_game_visible_travel-c6d276507b20deeb209e"></a>

**0° CCW: unverified** — `in_game_visible_travel-c6d276507b20deeb209e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-8ab1e565e2fb933e2a4c"></a>

**90° CCW: unverified** — `in_game_visible_travel-8ab1e565e2fb933e2a4c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-16dc5004f7aa04b34fad"></a>

**180° CCW: unverified** — `in_game_visible_travel-16dc5004f7aa04b34fad`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-23154b18b80486eb2476"></a>

**270° CCW: unverified** — `in_game_visible_travel-23154b18b80486eb2476`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-1ce4d2571808b7fdfe35"></a>

**0° CCW: unverified** — `in_game_visible_travel-1ce4d2571808b7fdfe35`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-07142e1de95e2cdeb3ee"></a>

**90° CCW: unverified** — `in_game_visible_travel-07142e1de95e2cdeb3ee`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-f4d99ea4e9189feef3ad"></a>

**180° CCW: unverified** — `in_game_visible_travel-f4d99ea4e9189feef3ad`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-0bfc267e643c994705a9"></a>

**270° CCW: unverified** — `in_game_visible_travel-0bfc267e643c994705a9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-W-out-1; entry: 1-E-in-16; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10</summary>

<a id="case-in_game_visible_travel-09642f3ddf122d9c5dc2"></a>

**0° CCW: unverified** — `in_game_visible_travel-09642f3ddf122d9c5dc2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-876dd101d6c2b7ce1905"></a>

**90° CCW: unverified** — `in_game_visible_travel-876dd101d6c2b7ce1905`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-5eb6418ac1741bbcd022"></a>

**180° CCW: unverified** — `in_game_visible_travel-5eb6418ac1741bbcd022`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-9381a67027c018f603be"></a>

**270° CCW: unverified** — `in_game_visible_travel-9381a67027c018f603be`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 252 cases; unverified: 252</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a0dfa3225a65f150d43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a179db379ff0088ad6f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-552acd5272175b555932">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d99b21fa9b0af616ca5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2a26e6f8329f6f702228">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b57b4e12eeb37cca637">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d228a862ea9a79fbf385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a829516bce2deb9038f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e98f33b8208396c2f8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5107315c8e0cd5b456e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-575603691048ddfd8102">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b84360b090d46aa63ce1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7584c718450c186ca26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0d9037efd1dc90eecba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84a9e1e4f33eae6809ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40f177dd5729d081845b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fbe8cd5bb6b7b2b22d50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3040d59d5403dde47e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fe042fd64aa8ab36ee9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35b0a4a4063a404f787c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4ae3447341af48ece3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-806b80a1595af2a01d36">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3bbec79fa4cc6ec29afa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a6759ac497dbebd1c67">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-543dd2d312a889bbf92b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbed832c5e3e10c70e1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d24506488ce82aa28dc3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c66bb0b1deac500b7cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0fa894b87ad34625c28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab439c174b11b724a05d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6693a33b50bfa50c0052">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d215993c6ad348ecc5d1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-286fca1c01bfdc4d37e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b3160768a7ae25a5b4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1cb61054ba6e81a7883">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1219356c09344085b03f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a7691ef5009df474da2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0245c173be437373c98d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f666233eb8526c78b69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8afa80b6d8c1a05ee2bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9b7961f1b49ee8d56c2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7732e407420c5c2470a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b6484adf896c2741c25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3447e3f9850f53f0d45">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e995e3f4a52027838d6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee7bf17393c28b8abf1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1971179a64a28cd424f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43077756688a2e5a1077">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1aba6a6647a56f261777">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-086e619334dab1ff9acc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-420e817f29e7d886ba4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b7e1fd875dd63b09cca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f275a90b52fb4e6023d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81991e9c2d2de63496e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35067b49cc5f710d777e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b417270cae2d6e25274">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bd53be7470e6cefe87dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9068d91af7798c6cc4f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-faf1a4a2d44ca00b8398">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0eb932191b7606de998f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-47d3e88d7eafc56e83d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98ec2f33567f42c13545">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d352f29b1e9152ad3986">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f897ba36da9a26ea1ff9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4b828cf050426f2ab1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e29cba084f3ce892f3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e3ae3a58b5c393aac8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-726f74ed37aa79903731">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-98734d82783e642b1a92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7417764f65eec736e556">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63c2880e5b3e7ae5c7ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa52b3375bd940198033">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-21d56aee84df3f050eaf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-209d93277e373f6f2d60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f58b67efc2551a24632c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b3c948ef6b9d6b26c63">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a2db489dcd650e14c5b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44bbb9195572d19b493e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4645049173c7490b226f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03ccf73f70763c342add">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-289a48fabd359b418b3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ef8c7039cadda363b9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-664f9166241a11ec60ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3657d52e3f2dcf758e64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-59b162891905d4960b21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-daa75f2e34653f825591">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27ccfc07f03027d36b5b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5be57df780c534ac115c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e985f44a68e5222d06d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfdf1ef96812df57cb6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25bdba741627452ec0e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d2e70b3287d32b0694e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-385fff15d807461b9860">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bcbda425d66f769dba87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9190078c104e8a2f4c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8ec5b6ce7102edf618d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b588eab832babf6d0d15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24b2bd234ccf47a75751">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fee3104e46f40fd2b75e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c84356e4dabbf4f661fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-81cb9ee919a18c5a5f50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-caad44ad02e1caf365f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5eb619f07e0a477975a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b724c9b6e0f6375ea39">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6758b65869592bcfd8ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50ffd508f243275e9e8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71bf2d7ce41c3ea45177">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29088a7d672c2e0e7290">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-073f74e80ccbfc5f39eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-588715baa16f85b34403">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-596449625261877fb5e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a37322ea6f933259d94">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-29a72cc6ace762628bbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04069019154408c2bdb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59387bca783c89e8ea28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e9e1a8176768b6f3924">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51149c78e38aafff8ca0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77c63674981fab17c031">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ebc2513d27477d74938">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dec79f9aaa4979a73c79">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-782c586cffb1a6bf0ad9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cb2fb01e6d0dfaed03c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95cd1bed757c2637d19a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83a51ba824025cc0c057">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc35a3915641b43a0804">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abd8af8ff5251ec2ff54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75f7a2dd5b64295d91cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bb401a3aa30b20b50f1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e6c7050828a18d4b955f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89062fb3c2210db90f38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3dc9d4470e8d43ff847">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92317a03a2ea61c5ca63">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-40ac6b346dd7344b95fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f7f54f3f40e527d21fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db48e2a539a01310a4b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8acef1f5180076103724">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46d0a5afa951d79df5cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ba5386b73a8e99798c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb596e7c45699dd3ffec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b89def883e3dd2809ee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a01df3a9626cfb134de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59e1cdaa0b11de2c9576">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09370a97c66892a66d1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b935aee15b29e307e006">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c13f29f2d4e84ac99383">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a19c8021ff4e6caa259e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc1ffdf7cd712b1929ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8deeb244fd3a71fad65">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-215bc2f08f48909dbc63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79ac544869751c2b7d5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35ef6c0a3802b00b3d0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13135c8acef96ad32150">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5e6c79e0a0b73618e44f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01c2d61df3f58e57d226">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f865095fff684e6152c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85cae39ebece1573a5c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f21d4cc8d3c63f1c5939">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a10b763cdd1c89d1302">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5223062b4d1c0e9c829a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd4fe510293562ba4624">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36c2a695ea353a0359e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b762944e7f9c6308d7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55bead92500ff6333503">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74e2c144f0f16c9cce1a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93403e41c8e4d3106bbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e571a92152a1b416e487">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-646fe51c68976a8943a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38344507348dfac8343c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c05399aa966a63899ffd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a84ff4c2cbda8fe0e49c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf20fefb1006ed682b48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-661a7a9058198362749a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-daa52ab76f9f157d3b67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f053c67a2f478be53d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61b6c01df8aaf825a544">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee4fbeccee1d3fe7ad63">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fdc4a6b3f62c8d041299">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-804b29e180d4704d9c9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19d4399bd9f331e6a135">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f5caebf80523ad205f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e240cd1c6721e99c6c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c91448fa968ca80d6ee7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0998cb4ca79b9545019">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36870113858da7cec6b7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de914ef281320c0305fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-069ae499d402b381b3fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03d3988c7b1a47c5d619">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bbb89fb549ba13ca6b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c512da5128383c55cbba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e793a8c9a7ab593b454">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87f80735df268e42e60b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26030c1015dedcefdd19">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c8fca840f99a758be90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3515798a0db98861cad3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-543a2ad2352208f6b46f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b95a137b7998dd89e2d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-706c3f453b25075b0e44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca474cf5b9e21023ff5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c16eae07ccb7be515490">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-beab5ac06d319395de05">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f2b304eefcaba217dde5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc2f950d211965b77acd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99f7dce67b56dbd4b027">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03a0844352f3202377b6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46a6038f25bc6eb34d08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-189370c9616ff35df53b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fed6da2b7f8ac717c9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3587347937ac6826670">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd3dbf118d549dfd178d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97370390ed21d768e0d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dd0b594eff929f812e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12fb92118dcb19885e46">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5239dbb4689e04e6fc0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d42c29d3302f07675ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53be80a6da2cbd9f4aa2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bb8b5abbedaef542e1e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dcc7ede179ece887b5d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f052fe71b002048daa8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbe29e9802eb652e52f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f14bd7b8ef73e726055f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a951e4c7cea194b5e270">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b82b619af90feb49d29a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a98a4bde7bb1bec323a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3d8eb24de19d25e1b61">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1620b6193c983618aa4c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edbc2afa41500aa4a419">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa651dd3bb12c942c3dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fabde47e415fbbfdec66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-523f5f70a1dbbed7d818">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-508dbe7b0ccfb077ed2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3be3344e903117400ace">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68eaa2b19761dc37cc99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-69f2f4a4cb455e716236">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f6f8605b293da0d3a83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e0c2926e23e4db5651a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2143ba166cd2a4b40add">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-231009ad854cf6c30136">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f29a09d61c6f32fb669">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98135e3184d8455273bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b4c46f8d9c4a6ec78cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6b833e91ec0cc91dd968">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccca95e651ac6fb85f60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4246c0e2d99884d2d232">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88b27daf7a54dc1801b2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-169619b8c8a3f88aec0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-290fdefe42856453a5ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1789d65a1d9b1b36bc4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc8a67f2d91b9e9d5f2c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3727c56028b4bf909e92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff7353bd40babc9726ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd9ae5a33a7265431733">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7464fcb0290c82bd0eb">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 1-S-in-3; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fbe8cd5bb6b7b2b22d50"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fbe8cd5bb6b7b2b22d50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3040d59d5403dde47e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e3040d59d5403dde47e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fe042fd64aa8ab36ee9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9fe042fd64aa8ab36ee9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35b0a4a4063a404f787c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-35b0a4a4063a404f787c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-3; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4ae3447341af48ece3b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4ae3447341af48ece3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-806b80a1595af2a01d36"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-806b80a1595af2a01d36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3bbec79fa4cc6ec29afa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3bbec79fa4cc6ec29afa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a6759ac497dbebd1c67"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1a6759ac497dbebd1c67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-3; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-543dd2d312a889bbf92b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-543dd2d312a889bbf92b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbed832c5e3e10c70e1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cbed832c5e3e10c70e1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d24506488ce82aa28dc3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d24506488ce82aa28dc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c66bb0b1deac500b7cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c66bb0b1deac500b7cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0fa894b87ad34625c28"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0fa894b87ad34625c28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab439c174b11b724a05d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ab439c174b11b724a05d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6693a33b50bfa50c0052"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6693a33b50bfa50c0052`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d215993c6ad348ecc5d1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d215993c6ad348ecc5d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1aba6a6647a56f261777"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1aba6a6647a56f261777`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-086e619334dab1ff9acc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-086e619334dab1ff9acc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-420e817f29e7d886ba4d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-420e817f29e7d886ba4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b7e1fd875dd63b09cca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b7e1fd875dd63b09cca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f275a90b52fb4e6023d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f275a90b52fb4e6023d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81991e9c2d2de63496e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81991e9c2d2de63496e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35067b49cc5f710d777e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35067b49cc5f710d777e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b417270cae2d6e25274"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7b417270cae2d6e25274`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bd53be7470e6cefe87dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bd53be7470e6cefe87dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9068d91af7798c6cc4f3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9068d91af7798c6cc4f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-faf1a4a2d44ca00b8398"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-faf1a4a2d44ca00b8398`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0eb932191b7606de998f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0eb932191b7606de998f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-47d3e88d7eafc56e83d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-47d3e88d7eafc56e83d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98ec2f33567f42c13545"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-98ec2f33567f42c13545`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d352f29b1e9152ad3986"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d352f29b1e9152ad3986`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f897ba36da9a26ea1ff9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f897ba36da9a26ea1ff9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-289a48fabd359b418b3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-289a48fabd359b418b3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ef8c7039cadda363b9e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4ef8c7039cadda363b9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-664f9166241a11ec60ad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-664f9166241a11ec60ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3657d52e3f2dcf758e64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3657d52e3f2dcf758e64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-59b162891905d4960b21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-59b162891905d4960b21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-daa75f2e34653f825591"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-daa75f2e34653f825591`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27ccfc07f03027d36b5b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27ccfc07f03027d36b5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5be57df780c534ac115c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5be57df780c534ac115c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e985f44a68e5222d06d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e985f44a68e5222d06d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfdf1ef96812df57cb6f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bfdf1ef96812df57cb6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25bdba741627452ec0e9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25bdba741627452ec0e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d2e70b3287d32b0694e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0d2e70b3287d32b0694e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-385fff15d807461b9860"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-385fff15d807461b9860`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bcbda425d66f769dba87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bcbda425d66f769dba87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9190078c104e8a2f4c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9190078c104e8a2f4c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8ec5b6ce7102edf618d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b8ec5b6ce7102edf618d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b588eab832babf6d0d15"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b588eab832babf6d0d15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24b2bd234ccf47a75751"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24b2bd234ccf47a75751`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fee3104e46f40fd2b75e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fee3104e46f40fd2b75e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c84356e4dabbf4f661fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c84356e4dabbf4f661fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-29a72cc6ace762628bbf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-29a72cc6ace762628bbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04069019154408c2bdb4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04069019154408c2bdb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59387bca783c89e8ea28"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-59387bca783c89e8ea28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e9e1a8176768b6f3924"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6e9e1a8176768b6f3924`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51149c78e38aafff8ca0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51149c78e38aafff8ca0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77c63674981fab17c031"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-77c63674981fab17c031`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ebc2513d27477d74938"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ebc2513d27477d74938`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dec79f9aaa4979a73c79"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dec79f9aaa4979a73c79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-782c586cffb1a6bf0ad9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-782c586cffb1a6bf0ad9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cb2fb01e6d0dfaed03c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9cb2fb01e6d0dfaed03c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95cd1bed757c2637d19a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-95cd1bed757c2637d19a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83a51ba824025cc0c057"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83a51ba824025cc0c057`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc35a3915641b43a0804"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc35a3915641b43a0804`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abd8af8ff5251ec2ff54"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-abd8af8ff5251ec2ff54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75f7a2dd5b64295d91cc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-75f7a2dd5b64295d91cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bb401a3aa30b20b50f1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6bb401a3aa30b20b50f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e6c7050828a18d4b955f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e6c7050828a18d4b955f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89062fb3c2210db90f38"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-89062fb3c2210db90f38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3dc9d4470e8d43ff847"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b3dc9d4470e8d43ff847`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92317a03a2ea61c5ca63"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92317a03a2ea61c5ca63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-40ac6b346dd7344b95fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-40ac6b346dd7344b95fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f7f54f3f40e527d21fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1f7f54f3f40e527d21fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db48e2a539a01310a4b6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-db48e2a539a01310a4b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8acef1f5180076103724"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8acef1f5180076103724`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46d0a5afa951d79df5cb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46d0a5afa951d79df5cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ba5386b73a8e99798c5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ba5386b73a8e99798c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb596e7c45699dd3ffec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fb596e7c45699dd3ffec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b89def883e3dd2809ee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b89def883e3dd2809ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a01df3a9626cfb134de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a01df3a9626cfb134de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59e1cdaa0b11de2c9576"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-59e1cdaa0b11de2c9576`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09370a97c66892a66d1f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-09370a97c66892a66d1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b935aee15b29e307e006"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b935aee15b29e307e006`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c13f29f2d4e84ac99383"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c13f29f2d4e84ac99383`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a19c8021ff4e6caa259e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a19c8021ff4e6caa259e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc1ffdf7cd712b1929ee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dc1ffdf7cd712b1929ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8deeb244fd3a71fad65"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d8deeb244fd3a71fad65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-215bc2f08f48909dbc63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-215bc2f08f48909dbc63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79ac544869751c2b7d5f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-79ac544869751c2b7d5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35ef6c0a3802b00b3d0f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35ef6c0a3802b00b3d0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13135c8acef96ad32150"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-13135c8acef96ad32150`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5e6c79e0a0b73618e44f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5e6c79e0a0b73618e44f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01c2d61df3f58e57d226"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-01c2d61df3f58e57d226`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f865095fff684e6152c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0f865095fff684e6152c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85cae39ebece1573a5c0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-85cae39ebece1573a5c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f21d4cc8d3c63f1c5939"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f21d4cc8d3c63f1c5939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a10b763cdd1c89d1302"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3a10b763cdd1c89d1302`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5223062b4d1c0e9c829a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5223062b4d1c0e9c829a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd4fe510293562ba4624"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd4fe510293562ba4624`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36c2a695ea353a0359e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36c2a695ea353a0359e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b762944e7f9c6308d7a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4b762944e7f9c6308d7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55bead92500ff6333503"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-55bead92500ff6333503`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74e2c144f0f16c9cce1a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-74e2c144f0f16c9cce1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93403e41c8e4d3106bbc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93403e41c8e4d3106bbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e571a92152a1b416e487"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e571a92152a1b416e487`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-646fe51c68976a8943a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-646fe51c68976a8943a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38344507348dfac8343c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-38344507348dfac8343c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c05399aa966a63899ffd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c05399aa966a63899ffd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a84ff4c2cbda8fe0e49c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a84ff4c2cbda8fe0e49c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf20fefb1006ed682b48"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cf20fefb1006ed682b48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-661a7a9058198362749a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-661a7a9058198362749a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-daa52ab76f9f157d3b67"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-daa52ab76f9f157d3b67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f053c67a2f478be53d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8f053c67a2f478be53d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61b6c01df8aaf825a544"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-61b6c01df8aaf825a544`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee4fbeccee1d3fe7ad63"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee4fbeccee1d3fe7ad63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fdc4a6b3f62c8d041299"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fdc4a6b3f62c8d041299`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-804b29e180d4704d9c9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-804b29e180d4704d9c9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19d4399bd9f331e6a135"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-19d4399bd9f331e6a135`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f5caebf80523ad205f8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1f5caebf80523ad205f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e240cd1c6721e99c6c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e240cd1c6721e99c6c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c91448fa968ca80d6ee7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c91448fa968ca80d6ee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0998cb4ca79b9545019"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0998cb4ca79b9545019`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36870113858da7cec6b7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36870113858da7cec6b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de914ef281320c0305fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de914ef281320c0305fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-069ae499d402b381b3fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-069ae499d402b381b3fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03d3988c7b1a47c5d619"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03d3988c7b1a47c5d619`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bbb89fb549ba13ca6b9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5bbb89fb549ba13ca6b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c512da5128383c55cbba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c512da5128383c55cbba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e793a8c9a7ab593b454"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3e793a8c9a7ab593b454`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87f80735df268e42e60b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-87f80735df268e42e60b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26030c1015dedcefdd19"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-26030c1015dedcefdd19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c8fca840f99a758be90"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c8fca840f99a758be90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3515798a0db98861cad3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3515798a0db98861cad3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-543a2ad2352208f6b46f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-543a2ad2352208f6b46f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b95a137b7998dd89e2d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8b95a137b7998dd89e2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-706c3f453b25075b0e44"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-706c3f453b25075b0e44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca474cf5b9e21023ff5d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ca474cf5b9e21023ff5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c16eae07ccb7be515490"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c16eae07ccb7be515490`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-beab5ac06d319395de05"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-beab5ac06d319395de05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f2b304eefcaba217dde5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2b304eefcaba217dde5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc2f950d211965b77acd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fc2f950d211965b77acd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99f7dce67b56dbd4b027"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99f7dce67b56dbd4b027`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03a0844352f3202377b6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03a0844352f3202377b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46a6038f25bc6eb34d08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46a6038f25bc6eb34d08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-189370c9616ff35df53b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-189370c9616ff35df53b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fed6da2b7f8ac717c9c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8fed6da2b7f8ac717c9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3587347937ac6826670"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b3587347937ac6826670`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd3dbf118d549dfd178d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd3dbf118d549dfd178d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97370390ed21d768e0d0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-97370390ed21d768e0d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dd0b594eff929f812e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0dd0b594eff929f812e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12fb92118dcb19885e46"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-12fb92118dcb19885e46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5239dbb4689e04e6fc0b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5239dbb4689e04e6fc0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d42c29d3302f07675ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d42c29d3302f07675ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53be80a6da2cbd9f4aa2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-53be80a6da2cbd9f4aa2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bb8b5abbedaef542e1e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0bb8b5abbedaef542e1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dcc7ede179ece887b5d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dcc7ede179ece887b5d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f052fe71b002048daa8e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f052fe71b002048daa8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbe29e9802eb652e52f6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fbe29e9802eb652e52f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f14bd7b8ef73e726055f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f14bd7b8ef73e726055f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a951e4c7cea194b5e270"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a951e4c7cea194b5e270`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b82b619af90feb49d29a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b82b619af90feb49d29a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a98a4bde7bb1bec323a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a98a4bde7bb1bec323a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3d8eb24de19d25e1b61"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a3d8eb24de19d25e1b61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1620b6193c983618aa4c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1620b6193c983618aa4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edbc2afa41500aa4a419"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-edbc2afa41500aa4a419`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa651dd3bb12c942c3dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fa651dd3bb12c942c3dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fabde47e415fbbfdec66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fabde47e415fbbfdec66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-2; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-523f5f70a1dbbed7d818"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-523f5f70a1dbbed7d818`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-508dbe7b0ccfb077ed2d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-508dbe7b0ccfb077ed2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3be3344e903117400ace"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3be3344e903117400ace`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68eaa2b19761dc37cc99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68eaa2b19761dc37cc99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-69f2f4a4cb455e716236"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-69f2f4a4cb455e716236`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f6f8605b293da0d3a83"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0f6f8605b293da0d3a83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e0c2926e23e4db5651a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e0c2926e23e4db5651a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2143ba166cd2a4b40add"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2143ba166cd2a4b40add`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-231009ad854cf6c30136"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-231009ad854cf6c30136`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f29a09d61c6f32fb669"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f29a09d61c6f32fb669`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98135e3184d8455273bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98135e3184d8455273bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b4c46f8d9c4a6ec78cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2b4c46f8d9c4a6ec78cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6b833e91ec0cc91dd968"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6b833e91ec0cc91dd968`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccca95e651ac6fb85f60"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ccca95e651ac6fb85f60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4246c0e2d99884d2d232"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4246c0e2d99884d2d232`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88b27daf7a54dc1801b2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-88b27daf7a54dc1801b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-169619b8c8a3f88aec0c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-169619b8c8a3f88aec0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-290fdefe42856453a5ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-290fdefe42856453a5ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1789d65a1d9b1b36bc4b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1789d65a1d9b1b36bc4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc8a67f2d91b9e9d5f2c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc8a67f2d91b9e9d5f2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3727c56028b4bf909e92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3727c56028b4bf909e92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff7353bd40babc9726ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ff7353bd40babc9726ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd9ae5a33a7265431733"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd9ae5a33a7265431733`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7464fcb0290c82bd0eb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b7464fcb0290c82bd0eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
