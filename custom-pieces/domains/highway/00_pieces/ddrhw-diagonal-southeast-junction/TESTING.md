---
title: "Testing: DD RHW-4 \u2014 Avenue Southeast Ramp Junction"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Avenue Southeast Ramp Junction

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Contains the southeast surface junction and the upper-deck ramp landings. Both avenue directions can enter the upper deck or receive traffic leaving that deck. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-in-1` | road / 1 / primary | in | [-8.0, -22.601434, 1.817631]; [0.8334622813545903, 0.5525763526963506]; -0.386266857 | `path-interface-95072b0547417ef03720` |
| `1-W-in-2` | road / 1 / primary | in | [-8.0, -3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-W-in-3` | road / 1 / primary | in | [-8.0, -2.805841, 0.0]; [0.8277168386819117, -0.5611460014670177]; 0.0 | `path-interface-76afa9fcb157c192156c` |
| `1-W-in-4` | road / 1 / primary | in | [-8.0, 3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-N-out-5` | road / 1 / primary | out | [-3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-N-out-6` | road / 1 / primary | out | [2.805841, 8.0, 0.0]; [-0.5611460014670177, 0.8277168386819117]; 0.0 | `path-interface-24061b69de696e6c8ae8` |
| `1-N-out-7` | road / 1 / primary | out | [3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-N-out-8` | road / 1 / primary | out | [22.601434, 8.0, 1.817631]; [0.5525763526963506, 0.8334622813545903]; 0.386266857 | `path-interface-5015313eb0038d7c0221` |
| `1-E-out-9` | road / 1 / primary | out | [24.0, -35.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-10` | road / 1 / primary | out | [24.0, -28.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-S-in-11` | road / 1 / primary | in | [28.8, -24.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-S-in-12` | road / 1 / primary | in | [35.2, -24.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `2-W-in-1` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-N-out-2` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-E-out-3` | pedestrian / 2 / primary | out | [24.0, -39.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-S-in-4` | pedestrian / 2 / primary | in | [39.3, -24.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-1` → `1-E-out-9` | primary |
| road | `1-W-in-1` → `1-N-out-6` | primary |
| road | `1-W-in-2` → `1-E-out-9` | primary |
| road | `1-W-in-3` → `1-N-out-8` | primary |
| road | `1-W-in-4` → `1-E-out-10` | primary |
| road | `1-S-in-11` → `1-N-out-5` | primary |
| road | `1-S-in-12` → `1-N-out-8` | primary |
| road | `1-S-in-12` → `1-N-out-7` | primary |
| pedestrian | `2-W-in-1` → `2-E-out-3` | primary |
| pedestrian | `2-S-in-4` → `2-N-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-1` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-N-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-N-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-11` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-12` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-12` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-12` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-12` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-12` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-12` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-southeast-junction --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The current assembly’s executed checks and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/40 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/40 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 316, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-southeast-junction/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-southeast-junction/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0b53cd7996f02454c3a7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0b53cd7996f02454c3a7"></a>

**General: unverified** — `software_resources-0b53cd7996f02454c3a7`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0b53cd7996f02454c3a7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0b53cd7996f02454c3a7"></a>

**General: unverified** — `software_connectivity-0b53cd7996f02454c3a7`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-1971e5729b46d8d832a3">[ ] unverified</a> | <a href="#case-in_game_render-ed49a60c503ab5571274">[ ] unverified</a> | <a href="#case-in_game_render-2b77d4cb5978d4debdfd">[ ] unverified</a> | <a href="#case-in_game_render-8d0907359ba53ba7eed2">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-1971e5729b46d8d832a3"></a>

**0° CCW: unverified** — `in_game_render-1971e5729b46d8d832a3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ed49a60c503ab5571274"></a>

**90° CCW: unverified** — `in_game_render-ed49a60c503ab5571274`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2b77d4cb5978d4debdfd"></a>

**180° CCW: unverified** — `in_game_render-2b77d4cb5978d4debdfd`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8d0907359ba53ba7eed2"></a>

**270° CCW: unverified** — `in_game_render-8d0907359ba53ba7eed2`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-1971e5729b46d8d832a3">[ ] unverified</a> | <a href="#case-in_game_placement-ed49a60c503ab5571274">[ ] unverified</a> | <a href="#case-in_game_placement-2b77d4cb5978d4debdfd">[ ] unverified</a> | <a href="#case-in_game_placement-8d0907359ba53ba7eed2">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-1971e5729b46d8d832a3"></a>

**0° CCW: unverified** — `in_game_placement-1971e5729b46d8d832a3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ed49a60c503ab5571274"></a>

**90° CCW: unverified** — `in_game_placement-ed49a60c503ab5571274`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2b77d4cb5978d4debdfd"></a>

**180° CCW: unverified** — `in_game_placement-2b77d4cb5978d4debdfd`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8d0907359ba53ba7eed2"></a>

**270° CCW: unverified** — `in_game_placement-8d0907359ba53ba7eed2`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-1971e5729b46d8d832a3">[ ] unverified</a> | <a href="#case-in_game_demolition-ed49a60c503ab5571274">[ ] unverified</a> | <a href="#case-in_game_demolition-2b77d4cb5978d4debdfd">[ ] unverified</a> | <a href="#case-in_game_demolition-8d0907359ba53ba7eed2">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-1971e5729b46d8d832a3"></a>

**0° CCW: unverified** — `in_game_demolition-1971e5729b46d8d832a3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ed49a60c503ab5571274"></a>

**90° CCW: unverified** — `in_game_demolition-ed49a60c503ab5571274`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2b77d4cb5978d4debdfd"></a>

**180° CCW: unverified** — `in_game_demolition-2b77d4cb5978d4debdfd`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8d0907359ba53ba7eed2"></a>

**270° CCW: unverified** — `in_game_demolition-8d0907359ba53ba7eed2`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-1971e5729b46d8d832a3">[ ] unverified</a> | <a href="#case-in_game_save_reload-ed49a60c503ab5571274">[ ] unverified</a> | <a href="#case-in_game_save_reload-2b77d4cb5978d4debdfd">[ ] unverified</a> | <a href="#case-in_game_save_reload-8d0907359ba53ba7eed2">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-1971e5729b46d8d832a3"></a>

**0° CCW: unverified** — `in_game_save_reload-1971e5729b46d8d832a3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ed49a60c503ab5571274"></a>

**90° CCW: unverified** — `in_game_save_reload-ed49a60c503ab5571274`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2b77d4cb5978d4debdfd"></a>

**180° CCW: unverified** — `in_game_save_reload-2b77d4cb5978d4debdfd`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8d0907359ba53ba7eed2"></a>

**270° CCW: unverified** — `in_game_save_reload-8d0907359ba53ba7eed2`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9 | — | <a href="#case-in_game_route_query-0f26f974903a2663c027">[ ] unverified</a> | <a href="#case-in_game_route_query-bd499b3c6d74d3d5f374">[ ] unverified</a> | <a href="#case-in_game_route_query-94f692ae62e7133ec29e">[ ] unverified</a> | <a href="#case-in_game_route_query-0a4d721d001a2fbbee0f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6 | — | <a href="#case-in_game_route_query-6ab022615b8662b962b7">[ ] unverified</a> | <a href="#case-in_game_route_query-d3fa491eea5a3ce13707">[ ] unverified</a> | <a href="#case-in_game_route_query-4bc26fe75ae59ffd059e">[ ] unverified</a> | <a href="#case-in_game_route_query-b57da487635eef630462">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9 | — | <a href="#case-in_game_route_query-b0f0c945f03ada56d39d">[ ] unverified</a> | <a href="#case-in_game_route_query-3cf83503175c6daca3b6">[ ] unverified</a> | <a href="#case-in_game_route_query-1b4e554475e89a50dbec">[ ] unverified</a> | <a href="#case-in_game_route_query-fe13f45ba5f82998bf1b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8 | — | <a href="#case-in_game_route_query-bef81d5bc9b7a41abec7">[ ] unverified</a> | <a href="#case-in_game_route_query-41dea6009f84923e6d4f">[ ] unverified</a> | <a href="#case-in_game_route_query-e837143fffb4962649a6">[ ] unverified</a> | <a href="#case-in_game_route_query-b0acbb599d6e99256ea8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10 | — | <a href="#case-in_game_route_query-dd3f9ab6b17a8501c878">[ ] unverified</a> | <a href="#case-in_game_route_query-188e1610e4f70d7715bf">[ ] unverified</a> | <a href="#case-in_game_route_query-4234a460944a6cfe5735">[ ] unverified</a> | <a href="#case-in_game_route_query-7ff60bbdf29691c6db09">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5 | — | <a href="#case-in_game_route_query-e9c3697624c6b1b05214">[ ] unverified</a> | <a href="#case-in_game_route_query-edc3a973fea91f77e8e5">[ ] unverified</a> | <a href="#case-in_game_route_query-242c82698e95cf784750">[ ] unverified</a> | <a href="#case-in_game_route_query-2dd0d0e1a4d032e096cc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8 | — | <a href="#case-in_game_route_query-a6042f0b64cc7fd6daa1">[ ] unverified</a> | <a href="#case-in_game_route_query-fbdffec8ae50dd526525">[ ] unverified</a> | <a href="#case-in_game_route_query-3b33f5896f7bb9ca731d">[ ] unverified</a> | <a href="#case-in_game_route_query-792cca12298d2a8a6f28">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7 | — | <a href="#case-in_game_route_query-12f861f5288cbf2681e5">[ ] unverified</a> | <a href="#case-in_game_route_query-9ddfb751d2f2698cecd9">[ ] unverified</a> | <a href="#case-in_game_route_query-82046242f3f8853a26dd">[ ] unverified</a> | <a href="#case-in_game_route_query-7b99b5b9948e82c1d959">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9</summary>

<a id="case-in_game_route_query-0f26f974903a2663c027"></a>

**0° CCW: unverified** — `in_game_route_query-0f26f974903a2663c027`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-bd499b3c6d74d3d5f374"></a>

**90° CCW: unverified** — `in_game_route_query-bd499b3c6d74d3d5f374`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-94f692ae62e7133ec29e"></a>

**180° CCW: unverified** — `in_game_route_query-94f692ae62e7133ec29e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-0a4d721d001a2fbbee0f"></a>

**270° CCW: unverified** — `in_game_route_query-0a4d721d001a2fbbee0f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6</summary>

<a id="case-in_game_route_query-6ab022615b8662b962b7"></a>

**0° CCW: unverified** — `in_game_route_query-6ab022615b8662b962b7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-d3fa491eea5a3ce13707"></a>

**90° CCW: unverified** — `in_game_route_query-d3fa491eea5a3ce13707`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-4bc26fe75ae59ffd059e"></a>

**180° CCW: unverified** — `in_game_route_query-4bc26fe75ae59ffd059e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-b57da487635eef630462"></a>

**270° CCW: unverified** — `in_game_route_query-b57da487635eef630462`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9</summary>

<a id="case-in_game_route_query-b0f0c945f03ada56d39d"></a>

**0° CCW: unverified** — `in_game_route_query-b0f0c945f03ada56d39d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-3cf83503175c6daca3b6"></a>

**90° CCW: unverified** — `in_game_route_query-3cf83503175c6daca3b6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-1b4e554475e89a50dbec"></a>

**180° CCW: unverified** — `in_game_route_query-1b4e554475e89a50dbec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-fe13f45ba5f82998bf1b"></a>

**270° CCW: unverified** — `in_game_route_query-fe13f45ba5f82998bf1b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8</summary>

<a id="case-in_game_route_query-bef81d5bc9b7a41abec7"></a>

**0° CCW: unverified** — `in_game_route_query-bef81d5bc9b7a41abec7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-41dea6009f84923e6d4f"></a>

**90° CCW: unverified** — `in_game_route_query-41dea6009f84923e6d4f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-e837143fffb4962649a6"></a>

**180° CCW: unverified** — `in_game_route_query-e837143fffb4962649a6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-b0acbb599d6e99256ea8"></a>

**270° CCW: unverified** — `in_game_route_query-b0acbb599d6e99256ea8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10</summary>

<a id="case-in_game_route_query-dd3f9ab6b17a8501c878"></a>

**0° CCW: unverified** — `in_game_route_query-dd3f9ab6b17a8501c878`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_route_query-188e1610e4f70d7715bf"></a>

**90° CCW: unverified** — `in_game_route_query-188e1610e4f70d7715bf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_route_query-4234a460944a6cfe5735"></a>

**180° CCW: unverified** — `in_game_route_query-4234a460944a6cfe5735`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_route_query-7ff60bbdf29691c6db09"></a>

**270° CCW: unverified** — `in_game_route_query-7ff60bbdf29691c6db09`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5</summary>

<a id="case-in_game_route_query-e9c3697624c6b1b05214"></a>

**0° CCW: unverified** — `in_game_route_query-e9c3697624c6b1b05214`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-edc3a973fea91f77e8e5"></a>

**90° CCW: unverified** — `in_game_route_query-edc3a973fea91f77e8e5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-242c82698e95cf784750"></a>

**180° CCW: unverified** — `in_game_route_query-242c82698e95cf784750`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-2dd0d0e1a4d032e096cc"></a>

**270° CCW: unverified** — `in_game_route_query-2dd0d0e1a4d032e096cc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8</summary>

<a id="case-in_game_route_query-a6042f0b64cc7fd6daa1"></a>

**0° CCW: unverified** — `in_game_route_query-a6042f0b64cc7fd6daa1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-fbdffec8ae50dd526525"></a>

**90° CCW: unverified** — `in_game_route_query-fbdffec8ae50dd526525`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-3b33f5896f7bb9ca731d"></a>

**180° CCW: unverified** — `in_game_route_query-3b33f5896f7bb9ca731d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-792cca12298d2a8a6f28"></a>

**270° CCW: unverified** — `in_game_route_query-792cca12298d2a8a6f28`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7</summary>

<a id="case-in_game_route_query-12f861f5288cbf2681e5"></a>

**0° CCW: unverified** — `in_game_route_query-12f861f5288cbf2681e5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7.

No observation recorded.

<a id="case-in_game_route_query-9ddfb751d2f2698cecd9"></a>

**90° CCW: unverified** — `in_game_route_query-9ddfb751d2f2698cecd9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7.

No observation recorded.

<a id="case-in_game_route_query-82046242f3f8853a26dd"></a>

**180° CCW: unverified** — `in_game_route_query-82046242f3f8853a26dd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7.

No observation recorded.

<a id="case-in_game_route_query-7b99b5b9948e82c1d959"></a>

**270° CCW: unverified** — `in_game_route_query-7b99b5b9948e82c1d959`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9 | — | <a href="#case-in_game_visible_travel-0f26f974903a2663c027">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bd499b3c6d74d3d5f374">[ ] unverified</a> | <a href="#case-in_game_visible_travel-94f692ae62e7133ec29e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0a4d721d001a2fbbee0f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6 | — | <a href="#case-in_game_visible_travel-6ab022615b8662b962b7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d3fa491eea5a3ce13707">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4bc26fe75ae59ffd059e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b57da487635eef630462">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9 | — | <a href="#case-in_game_visible_travel-b0f0c945f03ada56d39d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3cf83503175c6daca3b6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1b4e554475e89a50dbec">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fe13f45ba5f82998bf1b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8 | — | <a href="#case-in_game_visible_travel-bef81d5bc9b7a41abec7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-41dea6009f84923e6d4f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e837143fffb4962649a6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b0acbb599d6e99256ea8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10 | — | <a href="#case-in_game_visible_travel-dd3f9ab6b17a8501c878">[ ] unverified</a> | <a href="#case-in_game_visible_travel-188e1610e4f70d7715bf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4234a460944a6cfe5735">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7ff60bbdf29691c6db09">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5 | — | <a href="#case-in_game_visible_travel-e9c3697624c6b1b05214">[ ] unverified</a> | <a href="#case-in_game_visible_travel-edc3a973fea91f77e8e5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-242c82698e95cf784750">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2dd0d0e1a4d032e096cc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8 | — | <a href="#case-in_game_visible_travel-a6042f0b64cc7fd6daa1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fbdffec8ae50dd526525">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3b33f5896f7bb9ca731d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-792cca12298d2a8a6f28">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7 | — | <a href="#case-in_game_visible_travel-12f861f5288cbf2681e5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9ddfb751d2f2698cecd9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-82046242f3f8853a26dd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7b99b5b9948e82c1d959">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9</summary>

<a id="case-in_game_visible_travel-0f26f974903a2663c027"></a>

**0° CCW: unverified** — `in_game_visible_travel-0f26f974903a2663c027`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-bd499b3c6d74d3d5f374"></a>

**90° CCW: unverified** — `in_game_visible_travel-bd499b3c6d74d3d5f374`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-94f692ae62e7133ec29e"></a>

**180° CCW: unverified** — `in_game_visible_travel-94f692ae62e7133ec29e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-0a4d721d001a2fbbee0f"></a>

**270° CCW: unverified** — `in_game_visible_travel-0a4d721d001a2fbbee0f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-9; entry: 1-W-in-1; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6</summary>

<a id="case-in_game_visible_travel-6ab022615b8662b962b7"></a>

**0° CCW: unverified** — `in_game_visible_travel-6ab022615b8662b962b7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-d3fa491eea5a3ce13707"></a>

**90° CCW: unverified** — `in_game_visible_travel-d3fa491eea5a3ce13707`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-4bc26fe75ae59ffd059e"></a>

**180° CCW: unverified** — `in_game_visible_travel-4bc26fe75ae59ffd059e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-b57da487635eef630462"></a>

**270° CCW: unverified** — `in_game_visible_travel-b57da487635eef630462`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-N-out-6; entry: 1-W-in-1; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9</summary>

<a id="case-in_game_visible_travel-b0f0c945f03ada56d39d"></a>

**0° CCW: unverified** — `in_game_visible_travel-b0f0c945f03ada56d39d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-3cf83503175c6daca3b6"></a>

**90° CCW: unverified** — `in_game_visible_travel-3cf83503175c6daca3b6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-1b4e554475e89a50dbec"></a>

**180° CCW: unverified** — `in_game_visible_travel-1b4e554475e89a50dbec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-fe13f45ba5f82998bf1b"></a>

**270° CCW: unverified** — `in_game_visible_travel-fe13f45ba5f82998bf1b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-9; entry: 1-W-in-2; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8</summary>

<a id="case-in_game_visible_travel-bef81d5bc9b7a41abec7"></a>

**0° CCW: unverified** — `in_game_visible_travel-bef81d5bc9b7a41abec7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-41dea6009f84923e6d4f"></a>

**90° CCW: unverified** — `in_game_visible_travel-41dea6009f84923e6d4f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-e837143fffb4962649a6"></a>

**180° CCW: unverified** — `in_game_visible_travel-e837143fffb4962649a6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-b0acbb599d6e99256ea8"></a>

**270° CCW: unverified** — `in_game_visible_travel-b0acbb599d6e99256ea8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-N-out-8; entry: 1-W-in-3; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10</summary>

<a id="case-in_game_visible_travel-dd3f9ab6b17a8501c878"></a>

**0° CCW: unverified** — `in_game_visible_travel-dd3f9ab6b17a8501c878`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-188e1610e4f70d7715bf"></a>

**90° CCW: unverified** — `in_game_visible_travel-188e1610e4f70d7715bf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-4234a460944a6cfe5735"></a>

**180° CCW: unverified** — `in_game_visible_travel-4234a460944a6cfe5735`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-7ff60bbdf29691c6db09"></a>

**270° CCW: unverified** — `in_game_visible_travel-7ff60bbdf29691c6db09`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-E-out-10; entry: 1-W-in-4; exit: 1-E-out-10.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5</summary>

<a id="case-in_game_visible_travel-e9c3697624c6b1b05214"></a>

**0° CCW: unverified** — `in_game_visible_travel-e9c3697624c6b1b05214`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-edc3a973fea91f77e8e5"></a>

**90° CCW: unverified** — `in_game_visible_travel-edc3a973fea91f77e8e5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-242c82698e95cf784750"></a>

**180° CCW: unverified** — `in_game_visible_travel-242c82698e95cf784750`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-2dd0d0e1a4d032e096cc"></a>

**270° CCW: unverified** — `in_game_visible_travel-2dd0d0e1a4d032e096cc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-N-out-5; entry: 1-S-in-11; exit: 1-N-out-5.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8</summary>

<a id="case-in_game_visible_travel-a6042f0b64cc7fd6daa1"></a>

**0° CCW: unverified** — `in_game_visible_travel-a6042f0b64cc7fd6daa1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-fbdffec8ae50dd526525"></a>

**90° CCW: unverified** — `in_game_visible_travel-fbdffec8ae50dd526525`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-3b33f5896f7bb9ca731d"></a>

**180° CCW: unverified** — `in_game_visible_travel-3b33f5896f7bb9ca731d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-792cca12298d2a8a6f28"></a>

**270° CCW: unverified** — `in_game_visible_travel-792cca12298d2a8a6f28`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-8; entry: 1-S-in-12; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7</summary>

<a id="case-in_game_visible_travel-12f861f5288cbf2681e5"></a>

**0° CCW: unverified** — `in_game_visible_travel-12f861f5288cbf2681e5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-9ddfb751d2f2698cecd9"></a>

**90° CCW: unverified** — `in_game_visible_travel-9ddfb751d2f2698cecd9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-82046242f3f8853a26dd"></a>

**180° CCW: unverified** — `in_game_visible_travel-82046242f3f8853a26dd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-7b99b5b9948e82c1d959"></a>

**270° CCW: unverified** — `in_game_visible_travel-7b99b5b9948e82c1d959`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-12>1-N-out-7; entry: 1-S-in-12; exit: 1-N-out-7.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3 | — | <a href="#case-in_game_route_query-7887b1660f1849add211">[ ] unverified</a> | <a href="#case-in_game_route_query-37f78c5995d7d7954312">[ ] unverified</a> | <a href="#case-in_game_route_query-4e13a8fd3b225a7fb348">[ ] unverified</a> | <a href="#case-in_game_route_query-09bc00bb96136d909aff">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2 | — | <a href="#case-in_game_route_query-1b58748ac647b738ddb7">[ ] unverified</a> | <a href="#case-in_game_route_query-08688d2270d4975aa109">[ ] unverified</a> | <a href="#case-in_game_route_query-e60dcb272b8e5fcbfd7e">[ ] unverified</a> | <a href="#case-in_game_route_query-2756ced2e45411fbc9f3">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3</summary>

<a id="case-in_game_route_query-7887b1660f1849add211"></a>

**0° CCW: unverified** — `in_game_route_query-7887b1660f1849add211`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-37f78c5995d7d7954312"></a>

**90° CCW: unverified** — `in_game_route_query-37f78c5995d7d7954312`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-4e13a8fd3b225a7fb348"></a>

**180° CCW: unverified** — `in_game_route_query-4e13a8fd3b225a7fb348`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-09bc00bb96136d909aff"></a>

**270° CCW: unverified** — `in_game_route_query-09bc00bb96136d909aff`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2</summary>

<a id="case-in_game_route_query-1b58748ac647b738ddb7"></a>

**0° CCW: unverified** — `in_game_route_query-1b58748ac647b738ddb7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-08688d2270d4975aa109"></a>

**90° CCW: unverified** — `in_game_route_query-08688d2270d4975aa109`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-e60dcb272b8e5fcbfd7e"></a>

**180° CCW: unverified** — `in_game_route_query-e60dcb272b8e5fcbfd7e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-2756ced2e45411fbc9f3"></a>

**270° CCW: unverified** — `in_game_route_query-2756ced2e45411fbc9f3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3 | — | <a href="#case-in_game_visible_travel-7887b1660f1849add211">[ ] unverified</a> | <a href="#case-in_game_visible_travel-37f78c5995d7d7954312">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4e13a8fd3b225a7fb348">[ ] unverified</a> | <a href="#case-in_game_visible_travel-09bc00bb96136d909aff">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2 | — | <a href="#case-in_game_visible_travel-1b58748ac647b738ddb7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-08688d2270d4975aa109">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e60dcb272b8e5fcbfd7e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2756ced2e45411fbc9f3">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3</summary>

<a id="case-in_game_visible_travel-7887b1660f1849add211"></a>

**0° CCW: unverified** — `in_game_visible_travel-7887b1660f1849add211`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-37f78c5995d7d7954312"></a>

**90° CCW: unverified** — `in_game_visible_travel-37f78c5995d7d7954312`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-4e13a8fd3b225a7fb348"></a>

**180° CCW: unverified** — `in_game_visible_travel-4e13a8fd3b225a7fb348`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-09bc00bb96136d909aff"></a>

**270° CCW: unverified** — `in_game_visible_travel-09bc00bb96136d909aff`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-E-out-3; entry: 2-W-in-1; exit: 2-E-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2</summary>

<a id="case-in_game_visible_travel-1b58748ac647b738ddb7"></a>

**0° CCW: unverified** — `in_game_visible_travel-1b58748ac647b738ddb7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-08688d2270d4975aa109"></a>

**90° CCW: unverified** — `in_game_visible_travel-08688d2270d4975aa109`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-e60dcb272b8e5fcbfd7e"></a>

**180° CCW: unverified** — `in_game_visible_travel-e60dcb272b8e5fcbfd7e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-2756ced2e45411fbc9f3"></a>

**270° CCW: unverified** — `in_game_visible_travel-2756ced2e45411fbc9f3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-N-out-2; entry: 2-S-in-4; exit: 2-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 112 cases; unverified: 112</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7ae2fb8febef2838146b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7fb33ab9fe8ba81df126">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-764699f4c34db939086d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86118fe777bba026e49d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9620e61c65a823817c62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93ea25f1846e5492cb95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a0fde682a23638df039">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79a0be7e31f8f0f96459">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e77337e3b6cc9046ac5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46880c460db8f3bdb291">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe58104826c00a815ea4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39ff2a23d88b9ffe55ca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5d0aba7069b81484a38e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1914b0411e206e1c8913">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7109bf14f7e61f3b309a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b8b4c70bdda7a3f742a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f56abd1febc1e4b0b09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e36d30601e92967b18dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8ddaf832d6b832611c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee8b68fd9bafc9d33375">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6b8830eb2b0af28e59f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d826ab7a242ac0628836">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0aa1f868360e21771f46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22e699959c703a1affda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d9772d345cd01666f506">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d283bc07b45f4e4ee0ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2a216fcc55902557306">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bde76f95a2ba2394ee16">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a40e16235165b08b1463">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bd60aa02fee2e780686">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e08a13e4bf93fb714f0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd0ac5379c5e95c71e30">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2d59e2b6ea9cf9d6481">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-416d33c1e82fdb3718fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a17a38a29f7b3c3c8a24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f2866f662adc75cd906">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c1cf79ea02ba06044880">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78f7e742bb17ac90bf13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49b58a11584daeb25f9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68af5a27847f1375ee37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9de4c4b4c87672ea43e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4356ffc76ca40c658464">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c24d9d91b376ed5cc95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e031cd462a6f95dd0cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a1ec57a437ab7ef6643">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0c1df98502efe6b0fd9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ee8433d475d0062347d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e834c2a64684649d313">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-67c240f02ea07a4cbee3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b0d069e5f089be3a747">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3862106294eabbe8802d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cec8d75510cada29c25">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8172e55a5f90f995dcd5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc2e4d17dcdbf0bfe0ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0f02da706f7c85083fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80294b630c84e1a64a56">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-827a8785572c24205b18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1907fde5979ae3500077">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b166f625dda32e2d920">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-818237df41f1b7c263b5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-337af1bf2fbd8e99d092">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55dcfecb5c0193aa75c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ac378194b6bdc9bc0f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11adcb7a6429141fcbde">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-44bf51f844e221495389">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84982f49704b9c01be82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-348149792b12f087d3cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f22ae68875c176eb1158">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b178317cd682e6942300">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b64102b55684970253cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ecf60bf97ff42095928">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa8ff6fd3bbfe19bb466">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-11be1114f85029a242d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11657d528bcb86d022ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b872ab79373195e09e8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-656ebc93a8774368d332">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a3661c7739a1b0e7a1ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03d36a7dafd8f06aad8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b0ee12c50a6f4765a7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cffc89788579653e93ed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9736d439a78bdded155">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0da336e9c11be6880eed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cefa9f6ef07d65dda66d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ff9b5cf1c95fbe3be6f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a210aa97783330e6ba2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d948482a817f076d7cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6831e11b63f165e18b38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68f7cae8ff6260f04d3f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2886d09d43b2212a7b1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a723d329c71ca69ecbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-493a6454cdde69015563">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f43a6fd421948894b52">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d101ae717c3cdfdddffe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-904dcf6ac009c629c07d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8353465c4bddf92b7d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-695767eea9753d55d694">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-68efcda87b5384a7d82d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5edd48071be95fc4387">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42b3d05ec7c777a3dd71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc93b9a7fe730d9ec640">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d02b44a492bff43fe451">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42a5d1960969c85eb7f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed887f53053eca10940d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74f686ef7fc32d522345">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-83669fd31c518371eb7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f14d25b33f4c8883fb21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-747dc0363c2a6d92ea1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbf6874fbdc82340b1ab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f82b9e55a0f70569218e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61a522367fed7f094ceb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76c340cca39ac5ab7558">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef4c154be90511a3014e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7ae2fb8febef2838146b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7ae2fb8febef2838146b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7fb33ab9fe8ba81df126"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7fb33ab9fe8ba81df126`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-764699f4c34db939086d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-764699f4c34db939086d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86118fe777bba026e49d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-86118fe777bba026e49d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9620e61c65a823817c62"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9620e61c65a823817c62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93ea25f1846e5492cb95"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-93ea25f1846e5492cb95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a0fde682a23638df039"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1a0fde682a23638df039`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79a0be7e31f8f0f96459"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79a0be7e31f8f0f96459`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e77337e3b6cc9046ac5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e77337e3b6cc9046ac5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46880c460db8f3bdb291"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-46880c460db8f3bdb291`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe58104826c00a815ea4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fe58104826c00a815ea4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39ff2a23d88b9ffe55ca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39ff2a23d88b9ffe55ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5d0aba7069b81484a38e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5d0aba7069b81484a38e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1914b0411e206e1c8913"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1914b0411e206e1c8913`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7109bf14f7e61f3b309a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7109bf14f7e61f3b309a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b8b4c70bdda7a3f742a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1b8b4c70bdda7a3f742a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7f56abd1febc1e4b0b09"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f56abd1febc1e4b0b09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e36d30601e92967b18dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e36d30601e92967b18dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8ddaf832d6b832611c3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a8ddaf832d6b832611c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee8b68fd9bafc9d33375"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee8b68fd9bafc9d33375`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6b8830eb2b0af28e59f2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6b8830eb2b0af28e59f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d826ab7a242ac0628836"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d826ab7a242ac0628836`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0aa1f868360e21771f46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0aa1f868360e21771f46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22e699959c703a1affda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22e699959c703a1affda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d9772d345cd01666f506"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d9772d345cd01666f506`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d283bc07b45f4e4ee0ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d283bc07b45f4e4ee0ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2a216fcc55902557306"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2a216fcc55902557306`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bde76f95a2ba2394ee16"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bde76f95a2ba2394ee16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a40e16235165b08b1463"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a40e16235165b08b1463`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bd60aa02fee2e780686"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8bd60aa02fee2e780686`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e08a13e4bf93fb714f0c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e08a13e4bf93fb714f0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd0ac5379c5e95c71e30"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd0ac5379c5e95c71e30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2d59e2b6ea9cf9d6481"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2d59e2b6ea9cf9d6481`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-416d33c1e82fdb3718fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-416d33c1e82fdb3718fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a17a38a29f7b3c3c8a24"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a17a38a29f7b3c3c8a24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f2866f662adc75cd906"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3f2866f662adc75cd906`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c1cf79ea02ba06044880"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c1cf79ea02ba06044880`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78f7e742bb17ac90bf13"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78f7e742bb17ac90bf13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49b58a11584daeb25f9a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-49b58a11584daeb25f9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68af5a27847f1375ee37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68af5a27847f1375ee37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9de4c4b4c87672ea43e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9de4c4b4c87672ea43e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4356ffc76ca40c658464"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4356ffc76ca40c658464`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c24d9d91b376ed5cc95"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0c24d9d91b376ed5cc95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e031cd462a6f95dd0cb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e031cd462a6f95dd0cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a1ec57a437ab7ef6643"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a1ec57a437ab7ef6643`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0c1df98502efe6b0fd9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0c1df98502efe6b0fd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ee8433d475d0062347d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7ee8433d475d0062347d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e834c2a64684649d313"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e834c2a64684649d313`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-67c240f02ea07a4cbee3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-67c240f02ea07a4cbee3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b0d069e5f089be3a747"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b0d069e5f089be3a747`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3862106294eabbe8802d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3862106294eabbe8802d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cec8d75510cada29c25"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5cec8d75510cada29c25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8172e55a5f90f995dcd5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8172e55a5f90f995dcd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc2e4d17dcdbf0bfe0ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dc2e4d17dcdbf0bfe0ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0f02da706f7c85083fd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0f02da706f7c85083fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80294b630c84e1a64a56"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-80294b630c84e1a64a56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-827a8785572c24205b18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-827a8785572c24205b18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1907fde5979ae3500077"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1907fde5979ae3500077`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b166f625dda32e2d920"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8b166f625dda32e2d920`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-818237df41f1b7c263b5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-818237df41f1b7c263b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-337af1bf2fbd8e99d092"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-337af1bf2fbd8e99d092`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55dcfecb5c0193aa75c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-55dcfecb5c0193aa75c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ac378194b6bdc9bc0f6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ac378194b6bdc9bc0f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11adcb7a6429141fcbde"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-11adcb7a6429141fcbde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-44bf51f844e221495389"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-44bf51f844e221495389`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84982f49704b9c01be82"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-84982f49704b9c01be82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-348149792b12f087d3cd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-348149792b12f087d3cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f22ae68875c176eb1158"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f22ae68875c176eb1158`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b178317cd682e6942300"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b178317cd682e6942300`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b64102b55684970253cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b64102b55684970253cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ecf60bf97ff42095928"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ecf60bf97ff42095928`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa8ff6fd3bbfe19bb466"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aa8ff6fd3bbfe19bb466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-11be1114f85029a242d2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-11be1114f85029a242d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11657d528bcb86d022ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-11657d528bcb86d022ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b872ab79373195e09e8d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b872ab79373195e09e8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-656ebc93a8774368d332"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-656ebc93a8774368d332`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a3661c7739a1b0e7a1ff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a3661c7739a1b0e7a1ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03d36a7dafd8f06aad8b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-03d36a7dafd8f06aad8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b0ee12c50a6f4765a7b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2b0ee12c50a6f4765a7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cffc89788579653e93ed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cffc89788579653e93ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9736d439a78bdded155"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9736d439a78bdded155`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0da336e9c11be6880eed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0da336e9c11be6880eed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cefa9f6ef07d65dda66d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cefa9f6ef07d65dda66d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ff9b5cf1c95fbe3be6f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2ff9b5cf1c95fbe3be6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a210aa97783330e6ba2f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a210aa97783330e6ba2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d948482a817f076d7cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d948482a817f076d7cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6831e11b63f165e18b38"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6831e11b63f165e18b38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68f7cae8ff6260f04d3f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68f7cae8ff6260f04d3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2886d09d43b2212a7b1f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2886d09d43b2212a7b1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a723d329c71ca69ecbf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a723d329c71ca69ecbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-493a6454cdde69015563"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-493a6454cdde69015563`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f43a6fd421948894b52"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6f43a6fd421948894b52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d101ae717c3cdfdddffe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d101ae717c3cdfdddffe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-904dcf6ac009c629c07d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-904dcf6ac009c629c07d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8353465c4bddf92b7d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8353465c4bddf92b7d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-695767eea9753d55d694"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-695767eea9753d55d694`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-68efcda87b5384a7d82d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-68efcda87b5384a7d82d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5edd48071be95fc4387"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b5edd48071be95fc4387`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42b3d05ec7c777a3dd71"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42b3d05ec7c777a3dd71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc93b9a7fe730d9ec640"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc93b9a7fe730d9ec640`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d02b44a492bff43fe451"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d02b44a492bff43fe451`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42a5d1960969c85eb7f2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-42a5d1960969c85eb7f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed887f53053eca10940d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed887f53053eca10940d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74f686ef7fc32d522345"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-74f686ef7fc32d522345`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-83669fd31c518371eb7c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-83669fd31c518371eb7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f14d25b33f4c8883fb21"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f14d25b33f4c8883fb21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-747dc0363c2a6d92ea1c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-747dc0363c2a6d92ea1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbf6874fbdc82340b1ab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bbf6874fbdc82340b1ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f82b9e55a0f70569218e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f82b9e55a0f70569218e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61a522367fed7f094ceb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-61a522367fed7f094ceb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76c340cca39ac5ab7558"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-76c340cca39ac5ab7558`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef4c154be90511a3014e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ef4c154be90511a3014e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3e46594aa7f1ddf4c337">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6aa0356a60e55a5f3c31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a49145431e4002081878">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7f9a880e2cc4d8da2b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-325f5a7e464781e01a11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e59f556e1bf5a664a338">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc2c6fcc160c4fdcddf7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1c92bdd3a635c1ba36e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2ba2bff824f3dd2176eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c5f27ce8f80b8c5d344">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bedd8fd84ebe1cc1f8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13203d3997a6700b607c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1ababafdf7e6ab2e5fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98dd04a0d22ca706eac3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0343ccf7f4b7c5d5edd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ce2ef992793897858b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4cb67f645ec0f091a488">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a565b1fcf44b861dbd81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee54a63a5f52ad78218b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ff89353fdd43d449917">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7e9b5bddcfd70784a10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7a16678feea1f082283">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c80fa5034eda32830d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8aa2ac45bb8a8b05ea6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-facf2d9d5fd9e19d2ce6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6170852d79c93d3d6e69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5d21838b6a11b600e6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29a9bc624ae881e744f1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f8dd6be3b83e6d4e30d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c3f313da8835a19984a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc5f7f3a5e8df73e126f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d0f00228196e4fbb99b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-94d662e7c0f576414b57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adc77f43de7349d9ab6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b77da0109a502f2abdb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d633106a3afe8d57ced3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41031d23dde7a4af0d61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7baeb89cab551894fa6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a578d1c423fde8876de5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c8c10e3441e3a0805b6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41e8e72072c332c9e928">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dbbdfcaf8757d17c44a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-847093bfcb61cf80cc89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8844c098fc9eb7b39942">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0b8c3c86aad0260f08a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-052b1be17b003dc8f268">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c691c90c237505b68256">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b61ad4eafcdaade58114">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3e46594aa7f1ddf4c337"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e46594aa7f1ddf4c337`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6aa0356a60e55a5f3c31"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6aa0356a60e55a5f3c31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a49145431e4002081878"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a49145431e4002081878`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7f9a880e2cc4d8da2b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a7f9a880e2cc4d8da2b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-325f5a7e464781e01a11"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-325f5a7e464781e01a11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e59f556e1bf5a664a338"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e59f556e1bf5a664a338`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc2c6fcc160c4fdcddf7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dc2c6fcc160c4fdcddf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1c92bdd3a635c1ba36e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b1c92bdd3a635c1ba36e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2ba2bff824f3dd2176eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2ba2bff824f3dd2176eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c5f27ce8f80b8c5d344"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9c5f27ce8f80b8c5d344`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bedd8fd84ebe1cc1f8e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6bedd8fd84ebe1cc1f8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13203d3997a6700b607c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-13203d3997a6700b607c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d1ababafdf7e6ab2e5fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1ababafdf7e6ab2e5fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98dd04a0d22ca706eac3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-98dd04a0d22ca706eac3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0343ccf7f4b7c5d5edd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f0343ccf7f4b7c5d5edd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ce2ef992793897858b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7ce2ef992793897858b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4cb67f645ec0f091a488"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4cb67f645ec0f091a488`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a565b1fcf44b861dbd81"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a565b1fcf44b861dbd81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee54a63a5f52ad78218b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee54a63a5f52ad78218b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ff89353fdd43d449917"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ff89353fdd43d449917`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7e9b5bddcfd70784a10"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7e9b5bddcfd70784a10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7a16678feea1f082283"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f7a16678feea1f082283`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c80fa5034eda32830d7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c80fa5034eda32830d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8aa2ac45bb8a8b05ea6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d8aa2ac45bb8a8b05ea6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-facf2d9d5fd9e19d2ce6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-facf2d9d5fd9e19d2ce6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6170852d79c93d3d6e69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6170852d79c93d3d6e69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5d21838b6a11b600e6f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5d21838b6a11b600e6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29a9bc624ae881e744f1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-29a9bc624ae881e744f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f8dd6be3b83e6d4e30d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f8dd6be3b83e6d4e30d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c3f313da8835a19984a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2c3f313da8835a19984a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc5f7f3a5e8df73e126f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cc5f7f3a5e8df73e126f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d0f00228196e4fbb99b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d0f00228196e4fbb99b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-94d662e7c0f576414b57"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-94d662e7c0f576414b57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adc77f43de7349d9ab6b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-adc77f43de7349d9ab6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b77da0109a502f2abdb3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b77da0109a502f2abdb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d633106a3afe8d57ced3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d633106a3afe8d57ced3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41031d23dde7a4af0d61"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41031d23dde7a4af0d61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7baeb89cab551894fa6b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7baeb89cab551894fa6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a578d1c423fde8876de5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a578d1c423fde8876de5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c8c10e3441e3a0805b6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c8c10e3441e3a0805b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41e8e72072c332c9e928"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41e8e72072c332c9e928`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dbbdfcaf8757d17c44a2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dbbdfcaf8757d17c44a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-847093bfcb61cf80cc89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-847093bfcb61cf80cc89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8844c098fc9eb7b39942"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8844c098fc9eb7b39942`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0b8c3c86aad0260f08a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0b8c3c86aad0260f08a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-052b1be17b003dc8f268"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-052b1be17b003dc8f268`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c691c90c237505b68256"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c691c90c237505b68256`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b61ad4eafcdaade58114"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b61ad4eafcdaade58114`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95350ea8c3e93b331283">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c687947a48e82915f7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3efc3aaa50e2a4c845b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd16c0afc0df005e6bf1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bf2f53fb48bf6cb4fad8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f44e760964222302c77b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-405dcdb332e656dfbb5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d435db8b755fc6bb8f32">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c342c7fd33678c1b688e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c29ce334825696c9e2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eeea16b4eb4500388a78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c221349efbb5db5b0fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3419b59ea23eb049f1b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1053b4229fb7a8315bd8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e62ab6755cab1005ef83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3edad4cbff72f0cebf71">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de61840dc69ecf973133">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13ca979f3fb596177bde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e071462f37779c3c74a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ff5859b338c68435b50">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-024d22d339d3024a6449">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4c19120bc073084a7c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2133fa3c8d9ec4b7e8ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-713c53ac51681f26be4f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8a86f5a199144923509f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b52c5bcdda07ba93ab53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-303509a0bdfb1d8e716f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d88fc4bea534308360a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-564d618c32354a0d379b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86421fca5c8ac717e663">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3753b0da4d7b0faa171">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-722e4cd270876540efa8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a951826da54fa974ab4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec777b05bebaf98ba05f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0e5eddb99509439117e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76df056660bcd17a198e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-328c41e392763a8f7994">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6d4ed091984a313d4f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0eec8ec99faccf486fe2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af1d45d1ae2c7d624753">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-98b56de365c6ca76c657">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d53d7f87f883b98dcff2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91a3c6cdbc529f93d830">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d63e0c224a3eeef8ff6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a1e1e292e5b36952f765">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17d2e71bb68efe26ab50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0baf7afb2c545efa25db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edc1cf245b0e3641da74">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-95350ea8c3e93b331283"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-95350ea8c3e93b331283`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c687947a48e82915f7b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8c687947a48e82915f7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3efc3aaa50e2a4c845b6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3efc3aaa50e2a4c845b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd16c0afc0df005e6bf1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd16c0afc0df005e6bf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bf2f53fb48bf6cb4fad8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bf2f53fb48bf6cb4fad8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f44e760964222302c77b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f44e760964222302c77b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-405dcdb332e656dfbb5f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-405dcdb332e656dfbb5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d435db8b755fc6bb8f32"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d435db8b755fc6bb8f32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c342c7fd33678c1b688e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c342c7fd33678c1b688e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c29ce334825696c9e2b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6c29ce334825696c9e2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eeea16b4eb4500388a78"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eeea16b4eb4500388a78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c221349efbb5db5b0fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5c221349efbb5db5b0fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3419b59ea23eb049f1b5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3419b59ea23eb049f1b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1053b4229fb7a8315bd8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1053b4229fb7a8315bd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e62ab6755cab1005ef83"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e62ab6755cab1005ef83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3edad4cbff72f0cebf71"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3edad4cbff72f0cebf71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de61840dc69ecf973133"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de61840dc69ecf973133`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13ca979f3fb596177bde"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-13ca979f3fb596177bde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e071462f37779c3c74a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e071462f37779c3c74a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ff5859b338c68435b50"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ff5859b338c68435b50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-024d22d339d3024a6449"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-024d22d339d3024a6449`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4c19120bc073084a7c0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a4c19120bc073084a7c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2133fa3c8d9ec4b7e8ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2133fa3c8d9ec4b7e8ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-713c53ac51681f26be4f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-713c53ac51681f26be4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8a86f5a199144923509f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8a86f5a199144923509f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b52c5bcdda07ba93ab53"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b52c5bcdda07ba93ab53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-303509a0bdfb1d8e716f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-303509a0bdfb1d8e716f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d88fc4bea534308360a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d88fc4bea534308360a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-564d618c32354a0d379b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-564d618c32354a0d379b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86421fca5c8ac717e663"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-86421fca5c8ac717e663`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3753b0da4d7b0faa171"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f3753b0da4d7b0faa171`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-722e4cd270876540efa8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-722e4cd270876540efa8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a951826da54fa974ab4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a951826da54fa974ab4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec777b05bebaf98ba05f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec777b05bebaf98ba05f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0e5eddb99509439117e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f0e5eddb99509439117e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76df056660bcd17a198e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-76df056660bcd17a198e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-328c41e392763a8f7994"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-328c41e392763a8f7994`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6d4ed091984a313d4f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c6d4ed091984a313d4f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0eec8ec99faccf486fe2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0eec8ec99faccf486fe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af1d45d1ae2c7d624753"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af1d45d1ae2c7d624753`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-98b56de365c6ca76c657"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-98b56de365c6ca76c657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d53d7f87f883b98dcff2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d53d7f87f883b98dcff2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91a3c6cdbc529f93d830"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-91a3c6cdbc529f93d830`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d63e0c224a3eeef8ff6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d63e0c224a3eeef8ff6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a1e1e292e5b36952f765"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a1e1e292e5b36952f765`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17d2e71bb68efe26ab50"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-17d2e71bb68efe26ab50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0baf7afb2c545efa25db"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0baf7afb2c545efa25db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edc1cf245b0e3641da74"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-edc1cf245b0e3641da74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-915a90ba596cc794f114">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f9c08b70ed4003513e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-413c4fc6db2eaa765a85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1e114510f97b41dfdc3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d90768fe27275a02a734">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d892caba899eb134ff6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96a0a8035b7cb8ee724f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33a2724eb356a1164775">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-915a90ba596cc794f114"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-915a90ba596cc794f114`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f9c08b70ed4003513e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f9c08b70ed4003513e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-413c4fc6db2eaa765a85"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-413c4fc6db2eaa765a85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1e114510f97b41dfdc3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b1e114510f97b41dfdc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d90768fe27275a02a734"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d90768fe27275a02a734`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d892caba899eb134ff6b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d892caba899eb134ff6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96a0a8035b7cb8ee724f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-96a0a8035b7cb8ee724f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33a2724eb356a1164775"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-33a2724eb356a1164775`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-southeast-junction:canonical-southeast | <a href="#case-preview_review-920a9ef4286a6a634588">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-southeast-junction:canonical-top | <a href="#case-preview_review-a16ab91d8095502e2516">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-southeast-junction:canonical-southeast</summary>

<a id="case-preview_review-920a9ef4286a6a634588"></a>

**General: unverified** — `preview_review-920a9ef4286a6a634588`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-southeast-junction:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-southeast-junction:canonical-top</summary>

<a id="case-preview_review-a16ab91d8095502e2516"></a>

**General: unverified** — `preview_review-a16ab91d8095502e2516`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-southeast-junction:canonical-top.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
