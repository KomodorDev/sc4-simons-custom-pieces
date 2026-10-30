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

Contains the southeast surface junction and the upper-deck ramp landings. The upper off-ramp feeds only the avenue heading southeast, and the upper on-ramp receives only traffic arriving from the southeast. These right turns stay on their adjacent carriageway. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-in-1` | road / 1 / primary | in | [-8.0, -23.109934, 1.487699]; [0.7905593165701673, 0.6123854725449568]; -0.296123295 | `path-interface-a732cf9caf8dce8cfeaa` |
| `1-W-in-2` | road / 1 / primary | in | [-8.0, -3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-W-in-3` | road / 1 / primary | in | [-8.0, 3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-N-out-4` | road / 1 / primary | out | [-3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-N-out-5` | road / 1 / primary | out | [3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-N-out-6` | road / 1 / primary | out | [23.109934, 8.0, 1.487699]; [0.6123854725449568, 0.7905593165701673]; 0.296123295 | `path-interface-085ec70dd9403a42b8c3` |
| `1-E-out-7` | road / 1 / primary | out | [24.0, -35.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-8` | road / 1 / primary | out | [24.0, -28.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-S-in-9` | road / 1 / primary | in | [28.8, -24.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-S-in-10` | road / 1 / primary | in | [35.2, -24.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `2-W-in-1` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-N-out-2` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-E-out-3` | pedestrian / 2 / primary | out | [24.0, -39.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-S-in-4` | pedestrian / 2 / primary | in | [39.3, -24.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-1` → `1-E-out-7` | primary |
| road | `1-W-in-2` → `1-E-out-7` | primary |
| road | `1-W-in-3` → `1-E-out-8` | primary |
| road | `1-S-in-9` → `1-N-out-4` | primary |
| road | `1-S-in-10` → `1-N-out-6` | primary |
| road | `1-S-in-10` → `1-N-out-5` | primary |
| pedestrian | `2-W-in-1` → `2-E-out-3` | primary |
| pedestrian | `2-S-in-4` → `2-N-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-1` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-3` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-9` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-9` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-9` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-9` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-9` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-9` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-10` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-10` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-10` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-10` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-10` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-southeast-junction --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

The adaptive-ground integration retains the complete saved car, pedestrian, and ramp routes, but its game behaviour remains unverified for this component. Test a fresh placement from the current build in all four rotations, compare the selection preview with the placed decks, and inspect automatic pavement at the Avenue ends and ramp mouths. Retained routes do not establish working transfers between the adaptive Avenue tiles and neighbouring highway tiles, ordinary Avenue overplacement or redraw, or pedestrian travel. The canonical software views remain a static geometry and ground-artwork reference. The isolated prototype’s pavement and rotation observations do not transfer to this full component; use the [assembly testing guide](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md) and [network specification](../../NETWORK_SPEC.md) for the exact scope.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/32 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/32 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 248, passed: 0, failed: 0, stale: 0, not_applicable: 0.

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
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7 | — | <a href="#case-in_game_route_query-92c6542c04cd22216865">[ ] unverified</a> | <a href="#case-in_game_route_query-e9a51ddedac7bd2e7687">[ ] unverified</a> | <a href="#case-in_game_route_query-b0c72c52cea47ea4ba69">[ ] unverified</a> | <a href="#case-in_game_route_query-edfd987a6bc82377fe2b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7 | — | <a href="#case-in_game_route_query-84491b6ab4ed516f8dab">[ ] unverified</a> | <a href="#case-in_game_route_query-b5edf5312c31e21fa1f7">[ ] unverified</a> | <a href="#case-in_game_route_query-efed06ee0c8bfe59b739">[ ] unverified</a> | <a href="#case-in_game_route_query-ce9dcf2358858d48d641">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8 | — | <a href="#case-in_game_route_query-5f701686f72e21ece8fa">[ ] unverified</a> | <a href="#case-in_game_route_query-502799817be17fb8f4ad">[ ] unverified</a> | <a href="#case-in_game_route_query-e3e38ff3ed3ea839c45e">[ ] unverified</a> | <a href="#case-in_game_route_query-6ccd3a7433ebd55e46ce">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4 | — | <a href="#case-in_game_route_query-16d1a08e46e8e6d39156">[ ] unverified</a> | <a href="#case-in_game_route_query-b9ebed210c7250c06e2c">[ ] unverified</a> | <a href="#case-in_game_route_query-4524bab1f04caf50796a">[ ] unverified</a> | <a href="#case-in_game_route_query-6a70fe7f1d3734f22bbc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6 | — | <a href="#case-in_game_route_query-1e93d879560af096ea11">[ ] unverified</a> | <a href="#case-in_game_route_query-ba7a6f5d086bb4935659">[ ] unverified</a> | <a href="#case-in_game_route_query-993d6e3b0c23501d1bdd">[ ] unverified</a> | <a href="#case-in_game_route_query-ea65e26ccf48296f8a6f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5 | — | <a href="#case-in_game_route_query-7fec7dfbeef703a9eb13">[ ] unverified</a> | <a href="#case-in_game_route_query-aaa796a3f369b557ef9d">[ ] unverified</a> | <a href="#case-in_game_route_query-469d06d2150660902b3e">[ ] unverified</a> | <a href="#case-in_game_route_query-7602525727c471b8913c">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7</summary>

<a id="case-in_game_route_query-92c6542c04cd22216865"></a>

**0° CCW: unverified** — `in_game_route_query-92c6542c04cd22216865`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-e9a51ddedac7bd2e7687"></a>

**90° CCW: unverified** — `in_game_route_query-e9a51ddedac7bd2e7687`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-b0c72c52cea47ea4ba69"></a>

**180° CCW: unverified** — `in_game_route_query-b0c72c52cea47ea4ba69`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-edfd987a6bc82377fe2b"></a>

**270° CCW: unverified** — `in_game_route_query-edfd987a6bc82377fe2b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7</summary>

<a id="case-in_game_route_query-84491b6ab4ed516f8dab"></a>

**0° CCW: unverified** — `in_game_route_query-84491b6ab4ed516f8dab`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-b5edf5312c31e21fa1f7"></a>

**90° CCW: unverified** — `in_game_route_query-b5edf5312c31e21fa1f7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-efed06ee0c8bfe59b739"></a>

**180° CCW: unverified** — `in_game_route_query-efed06ee0c8bfe59b739`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_route_query-ce9dcf2358858d48d641"></a>

**270° CCW: unverified** — `in_game_route_query-ce9dcf2358858d48d641`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8</summary>

<a id="case-in_game_route_query-5f701686f72e21ece8fa"></a>

**0° CCW: unverified** — `in_game_route_query-5f701686f72e21ece8fa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-502799817be17fb8f4ad"></a>

**90° CCW: unverified** — `in_game_route_query-502799817be17fb8f4ad`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-e3e38ff3ed3ea839c45e"></a>

**180° CCW: unverified** — `in_game_route_query-e3e38ff3ed3ea839c45e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-6ccd3a7433ebd55e46ce"></a>

**270° CCW: unverified** — `in_game_route_query-6ccd3a7433ebd55e46ce`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4</summary>

<a id="case-in_game_route_query-16d1a08e46e8e6d39156"></a>

**0° CCW: unverified** — `in_game_route_query-16d1a08e46e8e6d39156`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-b9ebed210c7250c06e2c"></a>

**90° CCW: unverified** — `in_game_route_query-b9ebed210c7250c06e2c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-4524bab1f04caf50796a"></a>

**180° CCW: unverified** — `in_game_route_query-4524bab1f04caf50796a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-6a70fe7f1d3734f22bbc"></a>

**270° CCW: unverified** — `in_game_route_query-6a70fe7f1d3734f22bbc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6</summary>

<a id="case-in_game_route_query-1e93d879560af096ea11"></a>

**0° CCW: unverified** — `in_game_route_query-1e93d879560af096ea11`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-ba7a6f5d086bb4935659"></a>

**90° CCW: unverified** — `in_game_route_query-ba7a6f5d086bb4935659`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-993d6e3b0c23501d1bdd"></a>

**180° CCW: unverified** — `in_game_route_query-993d6e3b0c23501d1bdd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-ea65e26ccf48296f8a6f"></a>

**270° CCW: unverified** — `in_game_route_query-ea65e26ccf48296f8a6f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5</summary>

<a id="case-in_game_route_query-7fec7dfbeef703a9eb13"></a>

**0° CCW: unverified** — `in_game_route_query-7fec7dfbeef703a9eb13`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-aaa796a3f369b557ef9d"></a>

**90° CCW: unverified** — `in_game_route_query-aaa796a3f369b557ef9d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-469d06d2150660902b3e"></a>

**180° CCW: unverified** — `in_game_route_query-469d06d2150660902b3e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-7602525727c471b8913c"></a>

**270° CCW: unverified** — `in_game_route_query-7602525727c471b8913c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7 | — | <a href="#case-in_game_visible_travel-92c6542c04cd22216865">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e9a51ddedac7bd2e7687">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b0c72c52cea47ea4ba69">[ ] unverified</a> | <a href="#case-in_game_visible_travel-edfd987a6bc82377fe2b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7 | — | <a href="#case-in_game_visible_travel-84491b6ab4ed516f8dab">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b5edf5312c31e21fa1f7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-efed06ee0c8bfe59b739">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ce9dcf2358858d48d641">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8 | — | <a href="#case-in_game_visible_travel-5f701686f72e21ece8fa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-502799817be17fb8f4ad">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e3e38ff3ed3ea839c45e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6ccd3a7433ebd55e46ce">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4 | — | <a href="#case-in_game_visible_travel-16d1a08e46e8e6d39156">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b9ebed210c7250c06e2c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4524bab1f04caf50796a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6a70fe7f1d3734f22bbc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6 | — | <a href="#case-in_game_visible_travel-1e93d879560af096ea11">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ba7a6f5d086bb4935659">[ ] unverified</a> | <a href="#case-in_game_visible_travel-993d6e3b0c23501d1bdd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ea65e26ccf48296f8a6f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5 | — | <a href="#case-in_game_visible_travel-7fec7dfbeef703a9eb13">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aaa796a3f369b557ef9d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-469d06d2150660902b3e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7602525727c471b8913c">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7</summary>

<a id="case-in_game_visible_travel-92c6542c04cd22216865"></a>

**0° CCW: unverified** — `in_game_visible_travel-92c6542c04cd22216865`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-e9a51ddedac7bd2e7687"></a>

**90° CCW: unverified** — `in_game_visible_travel-e9a51ddedac7bd2e7687`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-b0c72c52cea47ea4ba69"></a>

**180° CCW: unverified** — `in_game_visible_travel-b0c72c52cea47ea4ba69`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-edfd987a6bc82377fe2b"></a>

**270° CCW: unverified** — `in_game_visible_travel-edfd987a6bc82377fe2b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-E-out-7; entry: 1-W-in-1; exit: 1-E-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7</summary>

<a id="case-in_game_visible_travel-84491b6ab4ed516f8dab"></a>

**0° CCW: unverified** — `in_game_visible_travel-84491b6ab4ed516f8dab`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-b5edf5312c31e21fa1f7"></a>

**90° CCW: unverified** — `in_game_visible_travel-b5edf5312c31e21fa1f7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-efed06ee0c8bfe59b739"></a>

**180° CCW: unverified** — `in_game_visible_travel-efed06ee0c8bfe59b739`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-ce9dcf2358858d48d641"></a>

**270° CCW: unverified** — `in_game_visible_travel-ce9dcf2358858d48d641`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-7; entry: 1-W-in-2; exit: 1-E-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8</summary>

<a id="case-in_game_visible_travel-5f701686f72e21ece8fa"></a>

**0° CCW: unverified** — `in_game_visible_travel-5f701686f72e21ece8fa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-502799817be17fb8f4ad"></a>

**90° CCW: unverified** — `in_game_visible_travel-502799817be17fb8f4ad`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-e3e38ff3ed3ea839c45e"></a>

**180° CCW: unverified** — `in_game_visible_travel-e3e38ff3ed3ea839c45e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-6ccd3a7433ebd55e46ce"></a>

**270° CCW: unverified** — `in_game_visible_travel-6ccd3a7433ebd55e46ce`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-3>1-E-out-8; entry: 1-W-in-3; exit: 1-E-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4</summary>

<a id="case-in_game_visible_travel-16d1a08e46e8e6d39156"></a>

**0° CCW: unverified** — `in_game_visible_travel-16d1a08e46e8e6d39156`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-b9ebed210c7250c06e2c"></a>

**90° CCW: unverified** — `in_game_visible_travel-b9ebed210c7250c06e2c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-4524bab1f04caf50796a"></a>

**180° CCW: unverified** — `in_game_visible_travel-4524bab1f04caf50796a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-6a70fe7f1d3734f22bbc"></a>

**270° CCW: unverified** — `in_game_visible_travel-6a70fe7f1d3734f22bbc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-9>1-N-out-4; entry: 1-S-in-9; exit: 1-N-out-4.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6</summary>

<a id="case-in_game_visible_travel-1e93d879560af096ea11"></a>

**0° CCW: unverified** — `in_game_visible_travel-1e93d879560af096ea11`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-ba7a6f5d086bb4935659"></a>

**90° CCW: unverified** — `in_game_visible_travel-ba7a6f5d086bb4935659`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-993d6e3b0c23501d1bdd"></a>

**180° CCW: unverified** — `in_game_visible_travel-993d6e3b0c23501d1bdd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-ea65e26ccf48296f8a6f"></a>

**270° CCW: unverified** — `in_game_visible_travel-ea65e26ccf48296f8a6f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-6; entry: 1-S-in-10; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5</summary>

<a id="case-in_game_visible_travel-7fec7dfbeef703a9eb13"></a>

**0° CCW: unverified** — `in_game_visible_travel-7fec7dfbeef703a9eb13`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-aaa796a3f369b557ef9d"></a>

**90° CCW: unverified** — `in_game_visible_travel-aaa796a3f369b557ef9d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-469d06d2150660902b3e"></a>

**180° CCW: unverified** — `in_game_visible_travel-469d06d2150660902b3e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-7602525727c471b8913c"></a>

**270° CCW: unverified** — `in_game_visible_travel-7602525727c471b8913c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-10>1-N-out-5; entry: 1-S-in-10; exit: 1-N-out-5.

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
<summary>Forbidden transfer — road → road — 76 cases; unverified: 76</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6b11d9311e2e4530524c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cafb8b11fdd53d90431">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45a5504937301507099f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d88f787ff091e22c17d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7ae2fb8febef2838146b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7fb33ab9fe8ba81df126">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-764699f4c34db939086d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86118fe777bba026e49d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3468fd7edd0d4243f176">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4b8089ad33df57cf687">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8c4a8ee7be376534dfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92b4f2249658f4b9bb76">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-76881a6e343f18123360">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cca5eeaec56fe1198e76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7e4efea41156f520691">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de9cf133c7288af87b2a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ae7e9c28c831c7dfcfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7f28a81b3c39e41c548">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b983092ead29116c994">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cccd3e38bd84d04b0111">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f56abd1febc1e4b0b09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e36d30601e92967b18dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8ddaf832d6b832611c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee8b68fd9bafc9d33375">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6b8830eb2b0af28e59f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d826ab7a242ac0628836">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0aa1f868360e21771f46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22e699959c703a1affda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c339fd55b392edf20877">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce2418ad487a3e50a443">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-341fea643f3fa95b8e44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1477ff2bd6fa26bce0d4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f50099a159518157c79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-329f0b761def8f1beef3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9e0ab0e3472a4bfaa55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5795e8de6cf15c84065a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c1cf79ea02ba06044880">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78f7e742bb17ac90bf13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49b58a11584daeb25f9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68af5a27847f1375ee37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9de4c4b4c87672ea43e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4356ffc76ca40c658464">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c24d9d91b376ed5cc95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e031cd462a6f95dd0cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4f8e5f132b22832dacb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d2f01b5c49ac98e0dc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7685d76d2188619227db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4e3db35195f24058ef2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-9; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b3ef51245e001a9fe744">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a06f4406d229278f60a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b632add39767f90fe800">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9b673f0c8a17dd6b5b6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e831f32e1711fadbb9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6fd417bb4716c856edbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67d9ff18360346269751">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37e00494e4d3122cd4ca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-9; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7ac1d8364fd59a43d9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef87085df65d089d3ec0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c1c3cfb54f5dbcaf8a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-994f92152b5e7c174516">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0b6a2405d33dee300ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89d3bdb3a0fa177b4bdb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1db5bb6116efb4b720e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b66c80a6c74c320282c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-10; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eb8cc8d1aa5da7419be6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ebb87d5b7d2c9d04dd7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e67d51bb08cf04748c1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f08c2979e9b9d256012f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-10; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac519a03fc87b00a5fb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c5d6ff8285fd0b8903d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d13c9fa4c6bdb6ef16fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b29e2fa05ef8062662f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-10; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9c2dcb66835063eaeaaf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52f69f952d016cd4d81a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f070b5e2faa770ba02a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-837b694ea8379db3a5af">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6b11d9311e2e4530524c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6b11d9311e2e4530524c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cafb8b11fdd53d90431"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4cafb8b11fdd53d90431`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45a5504937301507099f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-45a5504937301507099f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d88f787ff091e22c17d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d88f787ff091e22c17d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


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
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3468fd7edd0d4243f176"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3468fd7edd0d4243f176`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4b8089ad33df57cf687"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4b8089ad33df57cf687`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8c4a8ee7be376534dfe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8c4a8ee7be376534dfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92b4f2249658f4b9bb76"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92b4f2249658f4b9bb76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-76881a6e343f18123360"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-76881a6e343f18123360`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cca5eeaec56fe1198e76"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cca5eeaec56fe1198e76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7e4efea41156f520691"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d7e4efea41156f520691`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de9cf133c7288af87b2a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de9cf133c7288af87b2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ae7e9c28c831c7dfcfe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ae7e9c28c831c7dfcfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7f28a81b3c39e41c548"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f7f28a81b3c39e41c548`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b983092ead29116c994"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2b983092ead29116c994`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cccd3e38bd84d04b0111"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cccd3e38bd84d04b0111`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c339fd55b392edf20877"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c339fd55b392edf20877`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce2418ad487a3e50a443"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce2418ad487a3e50a443`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-341fea643f3fa95b8e44"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-341fea643f3fa95b8e44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1477ff2bd6fa26bce0d4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1477ff2bd6fa26bce0d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f50099a159518157c79"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f50099a159518157c79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-329f0b761def8f1beef3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-329f0b761def8f1beef3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9e0ab0e3472a4bfaa55"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c9e0ab0e3472a4bfaa55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5795e8de6cf15c84065a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5795e8de6cf15c84065a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-W-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4f8e5f132b22832dacb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4f8e5f132b22832dacb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d2f01b5c49ac98e0dc0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d2f01b5c49ac98e0dc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7685d76d2188619227db"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7685d76d2188619227db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4e3db35195f24058ef2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4e3db35195f24058ef2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-3; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-9; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b3ef51245e001a9fe744"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b3ef51245e001a9fe744`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a06f4406d229278f60a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a06f4406d229278f60a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b632add39767f90fe800"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b632add39767f90fe800`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9b673f0c8a17dd6b5b6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b9b673f0c8a17dd6b5b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e831f32e1711fadbb9d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e831f32e1711fadbb9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6fd417bb4716c856edbe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6fd417bb4716c856edbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67d9ff18360346269751"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67d9ff18360346269751`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37e00494e4d3122cd4ca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-37e00494e4d3122cd4ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-9; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7ac1d8364fd59a43d9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7ac1d8364fd59a43d9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef87085df65d089d3ec0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef87085df65d089d3ec0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c1c3cfb54f5dbcaf8a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4c1c3cfb54f5dbcaf8a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-994f92152b5e7c174516"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-994f92152b5e7c174516`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0b6a2405d33dee300ef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0b6a2405d33dee300ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89d3bdb3a0fa177b4bdb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-89d3bdb3a0fa177b4bdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1db5bb6116efb4b720e3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1db5bb6116efb4b720e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b66c80a6c74c320282c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7b66c80a6c74c320282c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-10; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eb8cc8d1aa5da7419be6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eb8cc8d1aa5da7419be6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ebb87d5b7d2c9d04dd7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ebb87d5b7d2c9d04dd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e67d51bb08cf04748c1c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e67d51bb08cf04748c1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f08c2979e9b9d256012f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f08c2979e9b9d256012f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-10; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac519a03fc87b00a5fb9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac519a03fc87b00a5fb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c5d6ff8285fd0b8903d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2c5d6ff8285fd0b8903d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d13c9fa4c6bdb6ef16fa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d13c9fa4c6bdb6ef16fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b29e2fa05ef8062662f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8b29e2fa05ef8062662f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-E-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-10; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9c2dcb66835063eaeaaf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9c2dcb66835063eaeaaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52f69f952d016cd4d81a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-52f69f952d016cd4d81a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f070b5e2faa770ba02a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9f070b5e2faa770ba02a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-837b694ea8379db3a5af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-837b694ea8379db3a5af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3e46594aa7f1ddf4c337">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6aa0356a60e55a5f3c31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a49145431e4002081878">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7f9a880e2cc4d8da2b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-325f5a7e464781e01a11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e59f556e1bf5a664a338">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc2c6fcc160c4fdcddf7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1c92bdd3a635c1ba36e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2ba2bff824f3dd2176eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c5f27ce8f80b8c5d344">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bedd8fd84ebe1cc1f8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13203d3997a6700b607c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1ababafdf7e6ab2e5fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98dd04a0d22ca706eac3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0343ccf7f4b7c5d5edd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ce2ef992793897858b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4cb67f645ec0f091a488">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a565b1fcf44b861dbd81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee54a63a5f52ad78218b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ff89353fdd43d449917">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7e9b5bddcfd70784a10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7a16678feea1f082283">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c80fa5034eda32830d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8aa2ac45bb8a8b05ea6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1ecd54479047efec73df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9b7d6f5803152a699e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-122645e1d88f71e32e41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a782d89d4a4bb47b0f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79c30e5e414236dd2edb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b15914139383a7bf8426">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-948dcd4a7c484228bec1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b7c44db5d2e6319f967">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eff71bd27542440c34af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55a65e944c092add4858">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65c9617a509302411db3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3dd9e71f63a620a0e2f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0a3350e31c0cb217ca6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb507ea698c7da127013">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d19d62102eb453329417">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec61419ba9d53c03a683">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 1-S-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1ecd54479047efec73df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ecd54479047efec73df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9b7d6f5803152a699e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9b7d6f5803152a699e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-122645e1d88f71e32e41"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-122645e1d88f71e32e41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a782d89d4a4bb47b0f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8a782d89d4a4bb47b0f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79c30e5e414236dd2edb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79c30e5e414236dd2edb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b15914139383a7bf8426"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b15914139383a7bf8426`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-948dcd4a7c484228bec1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-948dcd4a7c484228bec1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b7c44db5d2e6319f967"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1b7c44db5d2e6319f967`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eff71bd27542440c34af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eff71bd27542440c34af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55a65e944c092add4858"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-55a65e944c092add4858`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65c9617a509302411db3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65c9617a509302411db3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3dd9e71f63a620a0e2f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3dd9e71f63a620a0e2f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0a3350e31c0cb217ca6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0a3350e31c0cb217ca6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb507ea698c7da127013"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cb507ea698c7da127013`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d19d62102eb453329417"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d19d62102eb453329417`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec61419ba9d53c03a683"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec61419ba9d53c03a683`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-28d82d3a8b633426f119">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-383345c0388405b7f8c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe558992dfa8aa40be74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4843d376dc6058ce5ea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95350ea8c3e93b331283">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c687947a48e82915f7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3efc3aaa50e2a4c845b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd16c0afc0df005e6bf1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bf2f53fb48bf6cb4fad8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f44e760964222302c77b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-405dcdb332e656dfbb5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d435db8b755fc6bb8f32">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ee06479e2c36e49e6cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-211bd803b6c97ff7c844">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f0d51fb33b52d888f83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab02934b95161f964cfa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-89a41348bd864f29661d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4ac500851c984b7261f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b9ddf9e38b30358038f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4b27155e9af5306f253">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-733c805b158b47992b53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad55e9488f068386e290">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16fc46ee004bcf10b712">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9088e799ada7f61b1cad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8a86f5a199144923509f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b52c5bcdda07ba93ab53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-303509a0bdfb1d8e716f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d88fc4bea534308360a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-564d618c32354a0d379b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86421fca5c8ac717e663">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3753b0da4d7b0faa171">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-722e4cd270876540efa8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f890e9e1591f059036ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9fc2a010bf55db958ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a66f39b97fa4be1c65b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c940cd6b7b7806131d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd5afafa471290fc4809">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62379c041971dde0e6ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bbdc18d8d35a8e11c0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c084db36417b779a8e09">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-28d82d3a8b633426f119"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-28d82d3a8b633426f119`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-383345c0388405b7f8c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-383345c0388405b7f8c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe558992dfa8aa40be74"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fe558992dfa8aa40be74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4843d376dc6058ce5ea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b4843d376dc6058ce5ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


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
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ee06479e2c36e49e6cb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ee06479e2c36e49e6cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-211bd803b6c97ff7c844"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-211bd803b6c97ff7c844`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f0d51fb33b52d888f83"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4f0d51fb33b52d888f83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab02934b95161f964cfa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab02934b95161f964cfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-89a41348bd864f29661d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-89a41348bd864f29661d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4ac500851c984b7261f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e4ac500851c984b7261f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b9ddf9e38b30358038f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0b9ddf9e38b30358038f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4b27155e9af5306f253"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4b27155e9af5306f253`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-733c805b158b47992b53"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-733c805b158b47992b53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad55e9488f068386e290"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ad55e9488f068386e290`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16fc46ee004bcf10b712"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-16fc46ee004bcf10b712`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9088e799ada7f61b1cad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9088e799ada7f61b1cad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f890e9e1591f059036ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f890e9e1591f059036ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9fc2a010bf55db958ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9fc2a010bf55db958ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a66f39b97fa4be1c65b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1a66f39b97fa4be1c65b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c940cd6b7b7806131d8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6c940cd6b7b7806131d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd5afafa471290fc4809"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd5afafa471290fc4809`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62379c041971dde0e6ad"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62379c041971dde0e6ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bbdc18d8d35a8e11c0e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5bbdc18d8d35a8e11c0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c084db36417b779a8e09"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c084db36417b779a8e09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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
