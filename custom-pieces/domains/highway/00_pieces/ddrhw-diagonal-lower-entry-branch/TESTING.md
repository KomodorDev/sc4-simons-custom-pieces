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

Merges the on-ramp from the northwest avenue access into an outer lower-deck lane. The branch is one diagonal city-grid step farther from the avenue than in the original layout. Its barrier opening belongs to the lower deck; the upper-deck edge remains closed here. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

This branch uses a real flat auxiliary lane in the former highway shoulder, with a 12 m taper and a 4 m parallel section. Its saved driving path changes between the native outer through lane and that auxiliary lane. Native-material dashed separators and a painted split area identify the join; both highway through lanes remain available.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-S-out-1` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-S-in-2` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-S-out-3` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-S-in-4` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-E-in-5` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-E-out-6` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-E-in-7` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-E-out-8` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-N-in-9` | road / 1 / primary | in | [10.207444, 8.0, 6.745132]; [-0.2021693884311566, -0.9793505697049306]; 0.226756787 | `path-interface-85fe4503e80b365632f0` |
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
| road | `1-S-in-2` → `1-E-out-8` | primary |
| road | `1-S-in-4` → `1-E-out-6` | primary |
| road | `1-E-in-5` → `1-S-out-3` | primary |
| road | `1-E-in-7` → `1-S-out-1` | primary |
| road | `1-N-in-9` → `1-S-out-1` | primary |
| road | `1-S-in-11` → `1-E-out-17` | primary |
| road | `1-S-in-13` → `1-E-out-15` | primary |
| road | `1-E-in-14` → `1-S-out-12` | primary |
| road | `1-E-in-16` → `1-S-out-10` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-S-in-2` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-9` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-9` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-9` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-9` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-9` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-9` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-9` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-lower-entry-branch --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
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

Current totals: unverified: 345, passed: 0, failed: 0, stale: 0, not_applicable: 0.

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
<summary>Route Query — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8 | — | <a href="#case-in_game_route_query-9837de4264cc6c4ebc2d">[ ] unverified</a> | <a href="#case-in_game_route_query-faceadb12aa1a1f6d31b">[ ] unverified</a> | <a href="#case-in_game_route_query-f4acb1c5141674d705ed">[ ] unverified</a> | <a href="#case-in_game_route_query-d93635ddfe164c8b616e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6 | — | <a href="#case-in_game_route_query-a9983992c2b911374095">[ ] unverified</a> | <a href="#case-in_game_route_query-87ea7a05abe0a47c3fd5">[ ] unverified</a> | <a href="#case-in_game_route_query-c57806b764c6f13d269c">[ ] unverified</a> | <a href="#case-in_game_route_query-65f1f1e1ad86978ac406">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3 | — | <a href="#case-in_game_route_query-53101c17050fddd96498">[ ] unverified</a> | <a href="#case-in_game_route_query-bdb93e2b1329abd888eb">[ ] unverified</a> | <a href="#case-in_game_route_query-b0344dbcd474293b14a7">[ ] unverified</a> | <a href="#case-in_game_route_query-6e0c355873f9011d7785">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1 | — | <a href="#case-in_game_route_query-06fd65b283c942938831">[ ] unverified</a> | <a href="#case-in_game_route_query-d63064abdead1da6b443">[ ] unverified</a> | <a href="#case-in_game_route_query-f52fd8b0eedcdb586e20">[ ] unverified</a> | <a href="#case-in_game_route_query-6a643c52d2f96c95ab6b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1 | — | <a href="#case-in_game_route_query-e336e581e33f584610a2">[ ] unverified</a> | <a href="#case-in_game_route_query-6e78978e7a9cd8ed9e9f">[ ] unverified</a> | <a href="#case-in_game_route_query-0bd070cbea62ae0f1b87">[ ] unverified</a> | <a href="#case-in_game_route_query-a89e807dfce4497f4b27">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17 | — | <a href="#case-in_game_route_query-2634b8cba320232d7ca7">[ ] unverified</a> | <a href="#case-in_game_route_query-23e6b803ff25d3eb9f02">[ ] unverified</a> | <a href="#case-in_game_route_query-08437f80044dce9a9b25">[ ] unverified</a> | <a href="#case-in_game_route_query-852c8b1d58a6a542c97c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15 | — | <a href="#case-in_game_route_query-25e43e8863c43d9fb0b1">[ ] unverified</a> | <a href="#case-in_game_route_query-55e79cb40b224084a1ce">[ ] unverified</a> | <a href="#case-in_game_route_query-5fec3bf76a7925d92b57">[ ] unverified</a> | <a href="#case-in_game_route_query-95d5118cee31380b82a7">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12 | — | <a href="#case-in_game_route_query-685f5f2fac951e41a272">[ ] unverified</a> | <a href="#case-in_game_route_query-f9eec6a075cbd329c065">[ ] unverified</a> | <a href="#case-in_game_route_query-90fa7810e3b1dc5fe40a">[ ] unverified</a> | <a href="#case-in_game_route_query-c6a9d103144ffd9be87d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10 | — | <a href="#case-in_game_route_query-847872bd0efebb6f711a">[ ] unverified</a> | <a href="#case-in_game_route_query-ff711ad186d6716186d1">[ ] unverified</a> | <a href="#case-in_game_route_query-4044fd4465c60e2e368e">[ ] unverified</a> | <a href="#case-in_game_route_query-a6b91ba33e958dcd42bb">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8</summary>

<a id="case-in_game_route_query-9837de4264cc6c4ebc2d"></a>

**0° CCW: unverified** — `in_game_route_query-9837de4264cc6c4ebc2d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-faceadb12aa1a1f6d31b"></a>

**90° CCW: unverified** — `in_game_route_query-faceadb12aa1a1f6d31b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-f4acb1c5141674d705ed"></a>

**180° CCW: unverified** — `in_game_route_query-f4acb1c5141674d705ed`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-d93635ddfe164c8b616e"></a>

**270° CCW: unverified** — `in_game_route_query-d93635ddfe164c8b616e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6</summary>

<a id="case-in_game_route_query-a9983992c2b911374095"></a>

**0° CCW: unverified** — `in_game_route_query-a9983992c2b911374095`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-87ea7a05abe0a47c3fd5"></a>

**90° CCW: unverified** — `in_game_route_query-87ea7a05abe0a47c3fd5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-c57806b764c6f13d269c"></a>

**180° CCW: unverified** — `in_game_route_query-c57806b764c6f13d269c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-65f1f1e1ad86978ac406"></a>

**270° CCW: unverified** — `in_game_route_query-65f1f1e1ad86978ac406`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3</summary>

<a id="case-in_game_route_query-53101c17050fddd96498"></a>

**0° CCW: unverified** — `in_game_route_query-53101c17050fddd96498`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-bdb93e2b1329abd888eb"></a>

**90° CCW: unverified** — `in_game_route_query-bdb93e2b1329abd888eb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-b0344dbcd474293b14a7"></a>

**180° CCW: unverified** — `in_game_route_query-b0344dbcd474293b14a7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-6e0c355873f9011d7785"></a>

**270° CCW: unverified** — `in_game_route_query-6e0c355873f9011d7785`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1</summary>

<a id="case-in_game_route_query-06fd65b283c942938831"></a>

**0° CCW: unverified** — `in_game_route_query-06fd65b283c942938831`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-d63064abdead1da6b443"></a>

**90° CCW: unverified** — `in_game_route_query-d63064abdead1da6b443`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-f52fd8b0eedcdb586e20"></a>

**180° CCW: unverified** — `in_game_route_query-f52fd8b0eedcdb586e20`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-6a643c52d2f96c95ab6b"></a>

**270° CCW: unverified** — `in_game_route_query-6a643c52d2f96c95ab6b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1</summary>

<a id="case-in_game_route_query-e336e581e33f584610a2"></a>

**0° CCW: unverified** — `in_game_route_query-e336e581e33f584610a2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-6e78978e7a9cd8ed9e9f"></a>

**90° CCW: unverified** — `in_game_route_query-6e78978e7a9cd8ed9e9f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-0bd070cbea62ae0f1b87"></a>

**180° CCW: unverified** — `in_game_route_query-0bd070cbea62ae0f1b87`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-a89e807dfce4497f4b27"></a>

**270° CCW: unverified** — `in_game_route_query-a89e807dfce4497f4b27`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17</summary>

<a id="case-in_game_route_query-2634b8cba320232d7ca7"></a>

**0° CCW: unverified** — `in_game_route_query-2634b8cba320232d7ca7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-23e6b803ff25d3eb9f02"></a>

**90° CCW: unverified** — `in_game_route_query-23e6b803ff25d3eb9f02`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-08437f80044dce9a9b25"></a>

**180° CCW: unverified** — `in_game_route_query-08437f80044dce9a9b25`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-852c8b1d58a6a542c97c"></a>

**270° CCW: unverified** — `in_game_route_query-852c8b1d58a6a542c97c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15</summary>

<a id="case-in_game_route_query-25e43e8863c43d9fb0b1"></a>

**0° CCW: unverified** — `in_game_route_query-25e43e8863c43d9fb0b1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-55e79cb40b224084a1ce"></a>

**90° CCW: unverified** — `in_game_route_query-55e79cb40b224084a1ce`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-5fec3bf76a7925d92b57"></a>

**180° CCW: unverified** — `in_game_route_query-5fec3bf76a7925d92b57`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-95d5118cee31380b82a7"></a>

**270° CCW: unverified** — `in_game_route_query-95d5118cee31380b82a7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12</summary>

<a id="case-in_game_route_query-685f5f2fac951e41a272"></a>

**0° CCW: unverified** — `in_game_route_query-685f5f2fac951e41a272`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_route_query-f9eec6a075cbd329c065"></a>

**90° CCW: unverified** — `in_game_route_query-f9eec6a075cbd329c065`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_route_query-90fa7810e3b1dc5fe40a"></a>

**180° CCW: unverified** — `in_game_route_query-90fa7810e3b1dc5fe40a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_route_query-c6a9d103144ffd9be87d"></a>

**270° CCW: unverified** — `in_game_route_query-c6a9d103144ffd9be87d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10</summary>

<a id="case-in_game_route_query-847872bd0efebb6f711a"></a>

**0° CCW: unverified** — `in_game_route_query-847872bd0efebb6f711a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-ff711ad186d6716186d1"></a>

**90° CCW: unverified** — `in_game_route_query-ff711ad186d6716186d1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-4044fd4465c60e2e368e"></a>

**180° CCW: unverified** — `in_game_route_query-4044fd4465c60e2e368e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-a6b91ba33e958dcd42bb"></a>

**270° CCW: unverified** — `in_game_route_query-a6b91ba33e958dcd42bb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8 | — | <a href="#case-in_game_visible_travel-9837de4264cc6c4ebc2d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-faceadb12aa1a1f6d31b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f4acb1c5141674d705ed">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d93635ddfe164c8b616e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6 | — | <a href="#case-in_game_visible_travel-a9983992c2b911374095">[ ] unverified</a> | <a href="#case-in_game_visible_travel-87ea7a05abe0a47c3fd5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c57806b764c6f13d269c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-65f1f1e1ad86978ac406">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3 | — | <a href="#case-in_game_visible_travel-53101c17050fddd96498">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bdb93e2b1329abd888eb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b0344dbcd474293b14a7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6e0c355873f9011d7785">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1 | — | <a href="#case-in_game_visible_travel-06fd65b283c942938831">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d63064abdead1da6b443">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f52fd8b0eedcdb586e20">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6a643c52d2f96c95ab6b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1 | — | <a href="#case-in_game_visible_travel-e336e581e33f584610a2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6e78978e7a9cd8ed9e9f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0bd070cbea62ae0f1b87">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a89e807dfce4497f4b27">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17 | — | <a href="#case-in_game_visible_travel-2634b8cba320232d7ca7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-23e6b803ff25d3eb9f02">[ ] unverified</a> | <a href="#case-in_game_visible_travel-08437f80044dce9a9b25">[ ] unverified</a> | <a href="#case-in_game_visible_travel-852c8b1d58a6a542c97c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15 | — | <a href="#case-in_game_visible_travel-25e43e8863c43d9fb0b1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-55e79cb40b224084a1ce">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5fec3bf76a7925d92b57">[ ] unverified</a> | <a href="#case-in_game_visible_travel-95d5118cee31380b82a7">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12 | — | <a href="#case-in_game_visible_travel-685f5f2fac951e41a272">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f9eec6a075cbd329c065">[ ] unverified</a> | <a href="#case-in_game_visible_travel-90fa7810e3b1dc5fe40a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c6a9d103144ffd9be87d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10 | — | <a href="#case-in_game_visible_travel-847872bd0efebb6f711a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff711ad186d6716186d1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4044fd4465c60e2e368e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a6b91ba33e958dcd42bb">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8</summary>

<a id="case-in_game_visible_travel-9837de4264cc6c4ebc2d"></a>

**0° CCW: unverified** — `in_game_visible_travel-9837de4264cc6c4ebc2d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-faceadb12aa1a1f6d31b"></a>

**90° CCW: unverified** — `in_game_visible_travel-faceadb12aa1a1f6d31b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-f4acb1c5141674d705ed"></a>

**180° CCW: unverified** — `in_game_visible_travel-f4acb1c5141674d705ed`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-d93635ddfe164c8b616e"></a>

**270° CCW: unverified** — `in_game_visible_travel-d93635ddfe164c8b616e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6</summary>

<a id="case-in_game_visible_travel-a9983992c2b911374095"></a>

**0° CCW: unverified** — `in_game_visible_travel-a9983992c2b911374095`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-87ea7a05abe0a47c3fd5"></a>

**90° CCW: unverified** — `in_game_visible_travel-87ea7a05abe0a47c3fd5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-c57806b764c6f13d269c"></a>

**180° CCW: unverified** — `in_game_visible_travel-c57806b764c6f13d269c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-65f1f1e1ad86978ac406"></a>

**270° CCW: unverified** — `in_game_visible_travel-65f1f1e1ad86978ac406`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3</summary>

<a id="case-in_game_visible_travel-53101c17050fddd96498"></a>

**0° CCW: unverified** — `in_game_visible_travel-53101c17050fddd96498`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-bdb93e2b1329abd888eb"></a>

**90° CCW: unverified** — `in_game_visible_travel-bdb93e2b1329abd888eb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-b0344dbcd474293b14a7"></a>

**180° CCW: unverified** — `in_game_visible_travel-b0344dbcd474293b14a7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-6e0c355873f9011d7785"></a>

**270° CCW: unverified** — `in_game_visible_travel-6e0c355873f9011d7785`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1</summary>

<a id="case-in_game_visible_travel-06fd65b283c942938831"></a>

**0° CCW: unverified** — `in_game_visible_travel-06fd65b283c942938831`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-d63064abdead1da6b443"></a>

**90° CCW: unverified** — `in_game_visible_travel-d63064abdead1da6b443`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-f52fd8b0eedcdb586e20"></a>

**180° CCW: unverified** — `in_game_visible_travel-f52fd8b0eedcdb586e20`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-6a643c52d2f96c95ab6b"></a>

**270° CCW: unverified** — `in_game_visible_travel-6a643c52d2f96c95ab6b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1</summary>

<a id="case-in_game_visible_travel-e336e581e33f584610a2"></a>

**0° CCW: unverified** — `in_game_visible_travel-e336e581e33f584610a2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-6e78978e7a9cd8ed9e9f"></a>

**90° CCW: unverified** — `in_game_visible_travel-6e78978e7a9cd8ed9e9f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-0bd070cbea62ae0f1b87"></a>

**180° CCW: unverified** — `in_game_visible_travel-0bd070cbea62ae0f1b87`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-a89e807dfce4497f4b27"></a>

**270° CCW: unverified** — `in_game_visible_travel-a89e807dfce4497f4b27`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-S-out-1; entry: 1-N-in-9; exit: 1-S-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17</summary>

<a id="case-in_game_visible_travel-2634b8cba320232d7ca7"></a>

**0° CCW: unverified** — `in_game_visible_travel-2634b8cba320232d7ca7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-23e6b803ff25d3eb9f02"></a>

**90° CCW: unverified** — `in_game_visible_travel-23e6b803ff25d3eb9f02`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-08437f80044dce9a9b25"></a>

**180° CCW: unverified** — `in_game_visible_travel-08437f80044dce9a9b25`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-852c8b1d58a6a542c97c"></a>

**270° CCW: unverified** — `in_game_visible_travel-852c8b1d58a6a542c97c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-E-out-17; entry: 1-S-in-11; exit: 1-E-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15</summary>

<a id="case-in_game_visible_travel-25e43e8863c43d9fb0b1"></a>

**0° CCW: unverified** — `in_game_visible_travel-25e43e8863c43d9fb0b1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-55e79cb40b224084a1ce"></a>

**90° CCW: unverified** — `in_game_visible_travel-55e79cb40b224084a1ce`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-5fec3bf76a7925d92b57"></a>

**180° CCW: unverified** — `in_game_visible_travel-5fec3bf76a7925d92b57`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-95d5118cee31380b82a7"></a>

**270° CCW: unverified** — `in_game_visible_travel-95d5118cee31380b82a7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-E-out-15; entry: 1-S-in-13; exit: 1-E-out-15.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12</summary>

<a id="case-in_game_visible_travel-685f5f2fac951e41a272"></a>

**0° CCW: unverified** — `in_game_visible_travel-685f5f2fac951e41a272`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-f9eec6a075cbd329c065"></a>

**90° CCW: unverified** — `in_game_visible_travel-f9eec6a075cbd329c065`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-90fa7810e3b1dc5fe40a"></a>

**180° CCW: unverified** — `in_game_visible_travel-90fa7810e3b1dc5fe40a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-c6a9d103144ffd9be87d"></a>

**270° CCW: unverified** — `in_game_visible_travel-c6a9d103144ffd9be87d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-12; entry: 1-E-in-14; exit: 1-S-out-12.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10</summary>

<a id="case-in_game_visible_travel-847872bd0efebb6f711a"></a>

**0° CCW: unverified** — `in_game_visible_travel-847872bd0efebb6f711a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-ff711ad186d6716186d1"></a>

**90° CCW: unverified** — `in_game_visible_travel-ff711ad186d6716186d1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-4044fd4465c60e2e368e"></a>

**180° CCW: unverified** — `in_game_visible_travel-4044fd4465c60e2e368e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-a6b91ba33e958dcd42bb"></a>

**270° CCW: unverified** — `in_game_visible_travel-a6b91ba33e958dcd42bb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-10; entry: 1-E-in-16; exit: 1-S-out-10.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 252 cases; unverified: 252</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-78b47be1097668bd4b23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6b5bdd54eabd2131976">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6bda23266406d2654e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-704d10b4aa9a3ef34df7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0991b2cde89997aa0e1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0104ba30c07a307f692c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57a86bc95ab2a1f2d652">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af717eed03df4cf39313">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1fda65edaef5119a523f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2c9e33f89fba36db51a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-199cdb0b2709be905926">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ad73d838e47dfc3940a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-728206ef316ed77ba9d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8414d8fce4067221964c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abf530856dee50ed14ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7211812ad956c59bf6dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5ad36301db997f677eec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1cfa7689b6d77b99bca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a06d9e7268cb80ce07bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acb4e53c87eb919d7a0f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3b962dc6801969d8d49f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b3dd9fb5797d1276ea2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00f0631caadde63c2123">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d1c6976f58207f096e1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-17e7066f227a643eec65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5b47c9dd859b11d6cf5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34cc59dd086bef276ca7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9a17e8dbb5a5fb12c66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8284cc08688765e6962b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6472e81fe6cf2a994af7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9446d839fbf67054d6af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-485a849ab55570fd57c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9389c2ca224634e68336">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-780a2b2df26d869ddc42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2441e6d4e251fe964ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4730670a5baf661e147">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-876b61e05b1d6de88bb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-055608e31ded0a44cfe1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-739da32f87604f543789">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61d1d5f598754a4d18f3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a1dbef89e18fa1e77e48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c89c388adcb9d1bfc04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdd2d335cbb95cf20631">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a49097e8d34b5e88f1f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce2c0a7b040562229b4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0442ec23d9c509bc6083">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69f9551c75ac05e7b517">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-034acc7050a86b4f3309">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-007c36acba6e3aa43308">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a240c3e8f79d96b1e11b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed03dc329f17225a59b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc7daf1d9814a6824101">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6cfbb8d339f461430e1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82fe2c16e12c6f0e28c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d313628526b349ecc2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae15c9ba124291a78aa9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8cebf5a96e77000f43bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e09c1d51e59a29da4df3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbe53299f1c7cde96592">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-366b2cc7fd222e533cca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b920b7721ab1bd6ed25a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d2513ffa0ce17f379db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ecfaf86f9c769a14069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3fc4fca8151b16af54f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6850363f81763e17cd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0af75b307d32e4dd2e6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cd8df06fd7e46ac80fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1187fdbf442e96b4d16c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9727f2e118265d39cdee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a0c22b9ea17e8cedda3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e69a060e7a3182d7045">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44a1d33daee47ef5b328">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-09ad6eff9a35bd8b4117">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a752b97600290e57e79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f56ed4756fe938bed5e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5c36b204972fcc8f5fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-21646a49bdbeefbecee0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bbe1ea8bcdc5d489583">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5adfa3d790f4d5b58065">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b0ee37ccba7e805d69b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e3b6f379faa22189fd4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc57644dc6627e269bfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bd1377bb9ad86723350">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6c6b4c260b1b75d5fbd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-92fccb2136cc80e8b5c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a076f8d5e57d30182b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-854e238ebd7b02b1d8fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a1a75e25b874b423aa4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8a61d65f89adfe195430">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15c5d1e05497b34dc7be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56e45e3f188b31727bb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bc25176525fccbc1682">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de8517bfad9296d47961">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6f2ebd6d1127d26d661">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d746f0084f5351ec5466">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c54c5e18ffe5d1853a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-720d1f9e337b7bc7a2eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5459ccabb0efc59160d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6950d9f42005f2d1d6f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0de2a85bc300b39dd17">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-703616dba3f2fb4896cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7348a6019c2691c94c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7694aa6eef29213c78dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-874e271352b0b7cd0e95">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc1cc162ef5fd415d9c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb703cd7612490d487b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1349e2eb2e89bfd1084">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33c09294ac74dd69f191">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1bb7c8c1a8ee7d1c4a9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dcb5620c7076fa561ffb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f29da484086b7b8620e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-796c622cd338ab09db0d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-693028d16d443cf3ba49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9af48bad2830a0e6e311">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cadd0288a7689e37b9a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f26359df9a390a18b0ef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-285a87a70e4fd6085a1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c26f3a4b0b44622ac13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1da8f6fa5d428f6c4f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57e5ae04b58164738139">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-129060e6be11fd42f6cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fe9ddd0dd7c72134b38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4fb0ea77d94d8049eec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9147051818997a2d8dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-311444c1b0282a141606">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4dfc4db82c6594b8c0f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65e6a94ded18bce11c45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac53893a448c4118ae48">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3a400e15bc0243c0b96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f74cb592289e858c5a0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58eda561a75185e8a5ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d31e3ac51ddc2790e7c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d37d4d517a3288b509c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58940835d24900316fb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c445af75df3f9053180">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4319c5edb82d83e3da6b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-59cd7946d4479047046a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54a2f23932e681de46d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a384096a0cb684d44f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f39dfe32880a1ad50092">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4cb5b950989069d066b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-327a337419457eccab3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef48da8188d471ef9ff5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8394e26e78a4cfb3ca0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d1b8b07ba32506f7697">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c38799680c473b00d08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0498e7235929869a66a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d0d2b6a2ca6a4cef34c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2fa2336548310bd2befd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98c5cc5b0ee2152fbfb5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-577bb5c40508498114d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5437edf576f5fe1c0cdb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3de6aa8b71eb7ddc6a54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ab7ec1021b41ad81f69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab703868cada1e5bf968">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f215d3f4bf3ff27fd82">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5fe52ff9c6917c7634a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d469f424d8e4b331bd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-562792220469c2c3b9f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10dcba56e75e100ccd49">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc70838e21df0259198c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d9e1abfa710124560fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94e284694b4c8d8df3ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6fbdfa73c164443309a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9876e6d2d61c6428cee3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68d0326fcecbfa08aa7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bea04eaa4846cdab2bee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1c229d093a7f221b35e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-530db35c1ae00ce5295a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f383cdb2084d8ef751c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bac5a1e455e57335ee5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14e533e3afa8fa5782b8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8c4321babc32f0817fd9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5d62d43490b4d64923f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-720897293c85f6f7c492">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02a39b6051e06b33ab0e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-28238c3e60ba5ded5b32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2fc1d893bbf406690d9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec7e2a681003f9b58c8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc415a1fedc6a2f455a6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d9a5478d8d031fe58cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3744b5afb30cd0d4f77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2d77f6c56add24ae224">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7aa495030cad2c74205">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41fc00abbeb6d117c440">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e0b3fe09a0c4748d588">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f537ed52f7d121a4360">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3256ee5a3e18e8449c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c5ae5455ae8c390b563d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da7c18bd5b1629d0dd12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb3b851b772b7fb2ddae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f99a4f560cb899850610">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e5b9aa2b8c0d551d31f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48013e4aa33f2cacd2e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71b57d9c6ae7f7c56911">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68ed6948979573463db0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c76ceacdb906cb8d25e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebbe5fcbb9fac7ce9bbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8eb5b03246d1c2bb99cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b76fb6cb9b98eb4e2d94">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b86725fa12911664e33e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6fcd768aa79ea54f713c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d928b60d51329590ff42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43a238d8e0a35b008d03">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bda3f25b0248beab9168">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce88c91ef3f444799872">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee0ba4dbfd8ebe433fd9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96a51ecdca0a23109fa0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2db7c9a2527c4054f0ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a55850a59c736f276df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39d7b8ca17727760033d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-975d49c95a9c2bc37fb4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-07daa0d7d728a01d1465">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71b7db07d9763367f37b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ab015e3c916e6d927a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28ac6eb38911b3060bd5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-647775e6f08abc5b14d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72d1e1cc36ac991fbe08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67ac76c97d064f93b0e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65e47cc2e3ef273d7791">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dfed56dd66da277153b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85fd1b7af57176d7daae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87c492b8e63aa306eb91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f972df1c885b2cc41c87">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc762b4e211c9ba926fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f743c5f6d023c589244">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05953cd9b407a1f4fb32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cb1894e3c211a8e4b90">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6acff869eebd80581da3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-846af50c8bf28327a437">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cd2bf1ff094eff78695">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39c188b0783fa8591cb4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-df59d93627c53b8a3756">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d236425936b4f3a5f67a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8268f27575a676a5236e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0355e53a980217a20422">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-16f4f4b9c1eaa6765291">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d368739da3844eb3ccc6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac679082bf111206422c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3716cc19c958827789dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-089b32161deb5bf47fea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-992ee298fa5094518695">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9fb3adddfe98a18b677">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-862424b7e3fa7185c0cc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8fa37b87716ff89a0625">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87609985d2d34ba0ced7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1452ebbaf9def76657f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cdc41cbc072be796bf1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7161402fcca863658f22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4cf0691eb5e0ebdc78b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0deeb4cda189ff212d2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d285663da54af086701">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0991b2cde89997aa0e1f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0991b2cde89997aa0e1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0104ba30c07a307f692c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0104ba30c07a307f692c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57a86bc95ab2a1f2d652"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-57a86bc95ab2a1f2d652`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af717eed03df4cf39313"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af717eed03df4cf39313`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1fda65edaef5119a523f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1fda65edaef5119a523f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2c9e33f89fba36db51a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a2c9e33f89fba36db51a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-199cdb0b2709be905926"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-199cdb0b2709be905926`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ad73d838e47dfc3940a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8ad73d838e47dfc3940a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-728206ef316ed77ba9d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-728206ef316ed77ba9d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8414d8fce4067221964c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8414d8fce4067221964c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abf530856dee50ed14ca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-abf530856dee50ed14ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7211812ad956c59bf6dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7211812ad956c59bf6dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5ad36301db997f677eec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5ad36301db997f677eec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1cfa7689b6d77b99bca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e1cfa7689b6d77b99bca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a06d9e7268cb80ce07bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a06d9e7268cb80ce07bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acb4e53c87eb919d7a0f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acb4e53c87eb919d7a0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3b962dc6801969d8d49f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3b962dc6801969d8d49f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b3dd9fb5797d1276ea2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b3dd9fb5797d1276ea2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00f0631caadde63c2123"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-00f0631caadde63c2123`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d1c6976f58207f096e1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d1c6976f58207f096e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-17e7066f227a643eec65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-17e7066f227a643eec65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5b47c9dd859b11d6cf5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f5b47c9dd859b11d6cf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34cc59dd086bef276ca7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-34cc59dd086bef276ca7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9a17e8dbb5a5fb12c66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c9a17e8dbb5a5fb12c66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8284cc08688765e6962b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8284cc08688765e6962b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6472e81fe6cf2a994af7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6472e81fe6cf2a994af7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9446d839fbf67054d6af"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9446d839fbf67054d6af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-485a849ab55570fd57c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-485a849ab55570fd57c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9389c2ca224634e68336"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9389c2ca224634e68336`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-780a2b2df26d869ddc42"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-780a2b2df26d869ddc42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2441e6d4e251fe964ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a2441e6d4e251fe964ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4730670a5baf661e147"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c4730670a5baf661e147`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-876b61e05b1d6de88bb4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-876b61e05b1d6de88bb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-055608e31ded0a44cfe1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-055608e31ded0a44cfe1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-739da32f87604f543789"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-739da32f87604f543789`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61d1d5f598754a4d18f3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-61d1d5f598754a4d18f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a1dbef89e18fa1e77e48"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a1dbef89e18fa1e77e48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c89c388adcb9d1bfc04"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9c89c388adcb9d1bfc04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdd2d335cbb95cf20631"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cdd2d335cbb95cf20631`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a49097e8d34b5e88f1f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a49097e8d34b5e88f1f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce2c0a7b040562229b4b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce2c0a7b040562229b4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0442ec23d9c509bc6083"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0442ec23d9c509bc6083`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69f9551c75ac05e7b517"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-69f9551c75ac05e7b517`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-034acc7050a86b4f3309"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-034acc7050a86b4f3309`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-007c36acba6e3aa43308"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-007c36acba6e3aa43308`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a240c3e8f79d96b1e11b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a240c3e8f79d96b1e11b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed03dc329f17225a59b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed03dc329f17225a59b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc7daf1d9814a6824101"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc7daf1d9814a6824101`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6cfbb8d339f461430e1a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6cfbb8d339f461430e1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82fe2c16e12c6f0e28c1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-82fe2c16e12c6f0e28c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d313628526b349ecc2c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0d313628526b349ecc2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae15c9ba124291a78aa9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ae15c9ba124291a78aa9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8cebf5a96e77000f43bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8cebf5a96e77000f43bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e09c1d51e59a29da4df3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e09c1d51e59a29da4df3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbe53299f1c7cde96592"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fbe53299f1c7cde96592`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-366b2cc7fd222e533cca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-366b2cc7fd222e533cca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b920b7721ab1bd6ed25a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b920b7721ab1bd6ed25a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d2513ffa0ce17f379db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d2513ffa0ce17f379db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ecfaf86f9c769a14069"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ecfaf86f9c769a14069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3fc4fca8151b16af54f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f3fc4fca8151b16af54f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6850363f81763e17cd0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6850363f81763e17cd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0af75b307d32e4dd2e6a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0af75b307d32e4dd2e6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cd8df06fd7e46ac80fa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2cd8df06fd7e46ac80fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1187fdbf442e96b4d16c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1187fdbf442e96b4d16c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9727f2e118265d39cdee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9727f2e118265d39cdee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a0c22b9ea17e8cedda3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3a0c22b9ea17e8cedda3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e69a060e7a3182d7045"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e69a060e7a3182d7045`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44a1d33daee47ef5b328"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-44a1d33daee47ef5b328`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-09ad6eff9a35bd8b4117"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09ad6eff9a35bd8b4117`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a752b97600290e57e79"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a752b97600290e57e79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f56ed4756fe938bed5e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f56ed4756fe938bed5e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5c36b204972fcc8f5fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5c36b204972fcc8f5fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-21646a49bdbeefbecee0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-21646a49bdbeefbecee0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bbe1ea8bcdc5d489583"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6bbe1ea8bcdc5d489583`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5adfa3d790f4d5b58065"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5adfa3d790f4d5b58065`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b0ee37ccba7e805d69b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6b0ee37ccba7e805d69b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e3b6f379faa22189fd4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e3b6f379faa22189fd4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc57644dc6627e269bfe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fc57644dc6627e269bfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bd1377bb9ad86723350"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1bd1377bb9ad86723350`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6c6b4c260b1b75d5fbd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d6c6b4c260b1b75d5fbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-92fccb2136cc80e8b5c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-92fccb2136cc80e8b5c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a076f8d5e57d30182b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a076f8d5e57d30182b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-854e238ebd7b02b1d8fd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-854e238ebd7b02b1d8fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a1a75e25b874b423aa4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3a1a75e25b874b423aa4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8a61d65f89adfe195430"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8a61d65f89adfe195430`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15c5d1e05497b34dc7be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-15c5d1e05497b34dc7be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56e45e3f188b31727bb7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-56e45e3f188b31727bb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bc25176525fccbc1682"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2bc25176525fccbc1682`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de8517bfad9296d47961"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de8517bfad9296d47961`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6f2ebd6d1127d26d661"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a6f2ebd6d1127d26d661`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d746f0084f5351ec5466"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d746f0084f5351ec5466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c54c5e18ffe5d1853a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0c54c5e18ffe5d1853a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-720d1f9e337b7bc7a2eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-720d1f9e337b7bc7a2eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5459ccabb0efc59160d3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5459ccabb0efc59160d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6950d9f42005f2d1d6f9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6950d9f42005f2d1d6f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0de2a85bc300b39dd17"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0de2a85bc300b39dd17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-703616dba3f2fb4896cc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-703616dba3f2fb4896cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7348a6019c2691c94c6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b7348a6019c2691c94c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7694aa6eef29213c78dd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7694aa6eef29213c78dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-874e271352b0b7cd0e95"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-874e271352b0b7cd0e95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc1cc162ef5fd415d9c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc1cc162ef5fd415d9c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb703cd7612490d487b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bb703cd7612490d487b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1349e2eb2e89bfd1084"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b1349e2eb2e89bfd1084`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33c09294ac74dd69f191"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-33c09294ac74dd69f191`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1bb7c8c1a8ee7d1c4a9a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1bb7c8c1a8ee7d1c4a9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dcb5620c7076fa561ffb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dcb5620c7076fa561ffb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f29da484086b7b8620e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f29da484086b7b8620e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-796c622cd338ab09db0d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-796c622cd338ab09db0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-693028d16d443cf3ba49"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-693028d16d443cf3ba49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9af48bad2830a0e6e311"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9af48bad2830a0e6e311`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cadd0288a7689e37b9a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cadd0288a7689e37b9a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f26359df9a390a18b0ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f26359df9a390a18b0ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-285a87a70e4fd6085a1a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-285a87a70e4fd6085a1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c26f3a4b0b44622ac13"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4c26f3a4b0b44622ac13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1da8f6fa5d428f6c4f6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f1da8f6fa5d428f6c4f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57e5ae04b58164738139"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-57e5ae04b58164738139`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-129060e6be11fd42f6cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-129060e6be11fd42f6cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fe9ddd0dd7c72134b38"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8fe9ddd0dd7c72134b38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4fb0ea77d94d8049eec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4fb0ea77d94d8049eec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9147051818997a2d8dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a9147051818997a2d8dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-311444c1b0282a141606"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-311444c1b0282a141606`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4dfc4db82c6594b8c0f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4dfc4db82c6594b8c0f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65e6a94ded18bce11c45"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65e6a94ded18bce11c45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac53893a448c4118ae48"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac53893a448c4118ae48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3a400e15bc0243c0b96"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3a400e15bc0243c0b96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f74cb592289e858c5a0e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f74cb592289e858c5a0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58eda561a75185e8a5ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-58eda561a75185e8a5ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d31e3ac51ddc2790e7c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d31e3ac51ddc2790e7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d37d4d517a3288b509c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d37d4d517a3288b509c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58940835d24900316fb7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-58940835d24900316fb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c445af75df3f9053180"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6c445af75df3f9053180`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4319c5edb82d83e3da6b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4319c5edb82d83e3da6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-59cd7946d4479047046a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-59cd7946d4479047046a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54a2f23932e681de46d8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-54a2f23932e681de46d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a384096a0cb684d44f8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6a384096a0cb684d44f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f39dfe32880a1ad50092"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f39dfe32880a1ad50092`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4cb5b950989069d066b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4cb5b950989069d066b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-327a337419457eccab3e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-327a337419457eccab3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef48da8188d471ef9ff5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ef48da8188d471ef9ff5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8394e26e78a4cfb3ca0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8394e26e78a4cfb3ca0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d1b8b07ba32506f7697"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d1b8b07ba32506f7697`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c38799680c473b00d08"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4c38799680c473b00d08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0498e7235929869a66a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0498e7235929869a66a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d0d2b6a2ca6a4cef34c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4d0d2b6a2ca6a4cef34c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2fa2336548310bd2befd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2fa2336548310bd2befd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98c5cc5b0ee2152fbfb5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-98c5cc5b0ee2152fbfb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-577bb5c40508498114d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-577bb5c40508498114d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5437edf576f5fe1c0cdb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5437edf576f5fe1c0cdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3de6aa8b71eb7ddc6a54"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3de6aa8b71eb7ddc6a54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ab7ec1021b41ad81f69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6ab7ec1021b41ad81f69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab703868cada1e5bf968"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ab703868cada1e5bf968`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f215d3f4bf3ff27fd82"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f215d3f4bf3ff27fd82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5fe52ff9c6917c7634a5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5fe52ff9c6917c7634a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d469f424d8e4b331bd6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1d469f424d8e4b331bd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-562792220469c2c3b9f3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-562792220469c2c3b9f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10dcba56e75e100ccd49"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10dcba56e75e100ccd49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc70838e21df0259198c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc70838e21df0259198c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d9e1abfa710124560fc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d9e1abfa710124560fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94e284694b4c8d8df3ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94e284694b4c8d8df3ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6fbdfa73c164443309a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e6fbdfa73c164443309a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9876e6d2d61c6428cee3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9876e6d2d61c6428cee3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68d0326fcecbfa08aa7f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-68d0326fcecbfa08aa7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bea04eaa4846cdab2bee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bea04eaa4846cdab2bee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1c229d093a7f221b35e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c1c229d093a7f221b35e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-530db35c1ae00ce5295a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-530db35c1ae00ce5295a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f383cdb2084d8ef751c1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f383cdb2084d8ef751c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bac5a1e455e57335ee5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1bac5a1e455e57335ee5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14e533e3afa8fa5782b8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-14e533e3afa8fa5782b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8c4321babc32f0817fd9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8c4321babc32f0817fd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5d62d43490b4d64923f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d5d62d43490b4d64923f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-720897293c85f6f7c492"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-720897293c85f6f7c492`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02a39b6051e06b33ab0e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-02a39b6051e06b33ab0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-28238c3e60ba5ded5b32"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-28238c3e60ba5ded5b32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2fc1d893bbf406690d9c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2fc1d893bbf406690d9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec7e2a681003f9b58c8a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ec7e2a681003f9b58c8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc415a1fedc6a2f455a6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bc415a1fedc6a2f455a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d9a5478d8d031fe58cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d9a5478d8d031fe58cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3744b5afb30cd0d4f77"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c3744b5afb30cd0d4f77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2d77f6c56add24ae224"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2d77f6c56add24ae224`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7aa495030cad2c74205"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a7aa495030cad2c74205`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41fc00abbeb6d117c440"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41fc00abbeb6d117c440`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e0b3fe09a0c4748d588"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e0b3fe09a0c4748d588`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f537ed52f7d121a4360"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f537ed52f7d121a4360`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3256ee5a3e18e8449c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b3256ee5a3e18e8449c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c5ae5455ae8c390b563d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5ae5455ae8c390b563d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da7c18bd5b1629d0dd12"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-da7c18bd5b1629d0dd12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb3b851b772b7fb2ddae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eb3b851b772b7fb2ddae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f99a4f560cb899850610"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f99a4f560cb899850610`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e5b9aa2b8c0d551d31f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e5b9aa2b8c0d551d31f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48013e4aa33f2cacd2e4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48013e4aa33f2cacd2e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71b57d9c6ae7f7c56911"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-71b57d9c6ae7f7c56911`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68ed6948979573463db0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68ed6948979573463db0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c76ceacdb906cb8d25e2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c76ceacdb906cb8d25e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebbe5fcbb9fac7ce9bbd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ebbe5fcbb9fac7ce9bbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8eb5b03246d1c2bb99cc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8eb5b03246d1c2bb99cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b76fb6cb9b98eb4e2d94"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b76fb6cb9b98eb4e2d94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b86725fa12911664e33e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b86725fa12911664e33e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6fcd768aa79ea54f713c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6fcd768aa79ea54f713c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d928b60d51329590ff42"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d928b60d51329590ff42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43a238d8e0a35b008d03"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43a238d8e0a35b008d03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bda3f25b0248beab9168"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bda3f25b0248beab9168`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce88c91ef3f444799872"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce88c91ef3f444799872`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee0ba4dbfd8ebe433fd9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee0ba4dbfd8ebe433fd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96a51ecdca0a23109fa0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-96a51ecdca0a23109fa0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2db7c9a2527c4054f0ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2db7c9a2527c4054f0ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a55850a59c736f276df"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8a55850a59c736f276df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39d7b8ca17727760033d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-39d7b8ca17727760033d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-975d49c95a9c2bc37fb4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-975d49c95a9c2bc37fb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-07daa0d7d728a01d1465"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-07daa0d7d728a01d1465`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71b7db07d9763367f37b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-71b7db07d9763367f37b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ab015e3c916e6d927a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ab015e3c916e6d927a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28ac6eb38911b3060bd5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-28ac6eb38911b3060bd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-647775e6f08abc5b14d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-647775e6f08abc5b14d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72d1e1cc36ac991fbe08"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-72d1e1cc36ac991fbe08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67ac76c97d064f93b0e4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67ac76c97d064f93b0e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65e47cc2e3ef273d7791"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-65e47cc2e3ef273d7791`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dfed56dd66da277153b7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dfed56dd66da277153b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85fd1b7af57176d7daae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-85fd1b7af57176d7daae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87c492b8e63aa306eb91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-87c492b8e63aa306eb91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f972df1c885b2cc41c87"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f972df1c885b2cc41c87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc762b4e211c9ba926fa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc762b4e211c9ba926fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f743c5f6d023c589244"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f743c5f6d023c589244`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05953cd9b407a1f4fb32"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-05953cd9b407a1f4fb32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cb1894e3c211a8e4b90"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4cb1894e3c211a8e4b90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6acff869eebd80581da3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6acff869eebd80581da3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-846af50c8bf28327a437"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-846af50c8bf28327a437`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cd2bf1ff094eff78695"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2cd2bf1ff094eff78695`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39c188b0783fa8591cb4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39c188b0783fa8591cb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-df59d93627c53b8a3756"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-df59d93627c53b8a3756`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d236425936b4f3a5f67a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d236425936b4f3a5f67a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8268f27575a676a5236e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8268f27575a676a5236e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0355e53a980217a20422"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0355e53a980217a20422`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-16f4f4b9c1eaa6765291"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-16f4f4b9c1eaa6765291`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d368739da3844eb3ccc6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d368739da3844eb3ccc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac679082bf111206422c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ac679082bf111206422c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3716cc19c958827789dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3716cc19c958827789dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-089b32161deb5bf47fea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-089b32161deb5bf47fea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-992ee298fa5094518695"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-992ee298fa5094518695`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9fb3adddfe98a18b677"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c9fb3adddfe98a18b677`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-862424b7e3fa7185c0cc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-862424b7e3fa7185c0cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8fa37b87716ff89a0625"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8fa37b87716ff89a0625`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87609985d2d34ba0ced7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-87609985d2d34ba0ced7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1452ebbaf9def76657f1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1452ebbaf9def76657f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cdc41cbc072be796bf1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4cdc41cbc072be796bf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7161402fcca863658f22"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7161402fcca863658f22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4cf0691eb5e0ebdc78b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4cf0691eb5e0ebdc78b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0deeb4cda189ff212d2b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0deeb4cda189ff212d2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d285663da54af086701"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7d285663da54af086701`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-entry-branch:canonical-southeast | <a href="#case-preview_review-d8842e018ca2bf56719e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-entry-branch:canonical-top | <a href="#case-preview_review-f6ceae529af51d5892a9">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-entry-branch:connection-overview | <a href="#case-preview_review-474a0e13efb1d5911a47">[ ] unverified</a> | — | — | — | — |


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


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-entry-branch:connection-overview</summary>

<a id="case-preview_review-474a0e13efb1d5911a47"></a>

**General: unverified** — `preview_review-474a0e13efb1d5911a47`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-lower-entry-branch:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
