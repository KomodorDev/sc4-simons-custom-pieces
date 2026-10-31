---
title: "Testing: DD RHW-4 \u2014 Avenue Northwest Ramp Junction"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Avenue Northwest Ramp Junction

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Contains the northwest surface junction and the lower-deck ramp landings. The lower off-ramp feeds only the avenue heading northwest, and the lower on-ramp receives only traffic arriving from the northwest. These right turns stay on their adjacent carriageway. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-in-1` | road / 1 / primary | in | [-8.0, -3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-W-in-2` | road / 1 / primary | in | [-8.0, 3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-N-out-3` | road / 1 / primary | out | [-3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-S-out-4` | road / 1 / primary | out | [-1.754432, -40.0, 3.000444]; [-0.32921435266780985, -0.9442552144402037]; 0.22675602 | `path-interface-9a0f9ddca22564095128` |
| `1-N-out-5` | road / 1 / primary | out | [3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-S-out-6` | road / 1 / primary | out | [12.8, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-S-out-7` | road / 1 / primary | out | [19.2, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-E-in-8` | road / 1 / primary | in | [24.0, -19.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-E-in-9` | road / 1 / primary | in | [24.0, -12.8, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-in-10` | road / 1 / primary | in | [40.0, 1.754432, 3.000444]; [-0.9442552144402037, -0.32921435266780985]; -0.22675602 | `path-interface-aeabf380377c95bbb5f1` |
| `2-W-in-1` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-N-out-2` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-S-out-3` | pedestrian / 2 / primary | out | [8.7, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-E-in-4` | pedestrian / 2 / primary | in | [24.0, -8.7, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-1` → `1-S-out-4` | primary |
| road | `1-W-in-1` → `1-S-out-6` | primary |
| road | `1-W-in-2` → `1-S-out-7` | primary |
| road | `1-E-in-8` → `1-N-out-3` | primary |
| road | `1-E-in-9` → `1-N-out-5` | primary |
| road | `1-E-in-10` → `1-N-out-5` | primary |
| pedestrian | `2-W-in-1` → `2-S-out-3` | primary |
| pedestrian | `2-E-in-4` → `2-N-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-1` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-northwest-junction --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

The adaptive-ground integration retains the complete saved car, pedestrian, and ramp routes, but its game behaviour remains unverified for this component. Test a fresh placement from the current build in all four rotations, compare the selection preview with the placed decks, and inspect automatic pavement at the Avenue ends and ramp mouths. Retained routes do not establish working transfers between the adaptive Avenue tiles and neighbouring highway tiles, ordinary Avenue overplacement or redraw, or pedestrian travel. The canonical software views remain a static geometry and ground-artwork reference. The isolated prototype’s pavement and rotation observations do not transfer to this full component; use the [assembly testing guide](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md) and [network specification](../../NETWORK_SPEC.md) for the exact scope.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
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

Current totals: unverified: 249, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-northwest-junction/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-northwest-junction/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-aaad97762879968f7cfc">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-aaad97762879968f7cfc"></a>

**General: unverified** — `software_resources-aaad97762879968f7cfc`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-aaad97762879968f7cfc">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-aaad97762879968f7cfc"></a>

**General: unverified** — `software_connectivity-aaad97762879968f7cfc`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-34cd157023b99598cfc5">[ ] unverified</a> | <a href="#case-in_game_render-3efcb11b59402b534188">[ ] unverified</a> | <a href="#case-in_game_render-88e3b530006133672003">[ ] unverified</a> | <a href="#case-in_game_render-40603153035cbde04213">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-34cd157023b99598cfc5"></a>

**0° CCW: unverified** — `in_game_render-34cd157023b99598cfc5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3efcb11b59402b534188"></a>

**90° CCW: unverified** — `in_game_render-3efcb11b59402b534188`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-88e3b530006133672003"></a>

**180° CCW: unverified** — `in_game_render-88e3b530006133672003`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-40603153035cbde04213"></a>

**270° CCW: unverified** — `in_game_render-40603153035cbde04213`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-34cd157023b99598cfc5">[ ] unverified</a> | <a href="#case-in_game_placement-3efcb11b59402b534188">[ ] unverified</a> | <a href="#case-in_game_placement-88e3b530006133672003">[ ] unverified</a> | <a href="#case-in_game_placement-40603153035cbde04213">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-34cd157023b99598cfc5"></a>

**0° CCW: unverified** — `in_game_placement-34cd157023b99598cfc5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3efcb11b59402b534188"></a>

**90° CCW: unverified** — `in_game_placement-3efcb11b59402b534188`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-88e3b530006133672003"></a>

**180° CCW: unverified** — `in_game_placement-88e3b530006133672003`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-40603153035cbde04213"></a>

**270° CCW: unverified** — `in_game_placement-40603153035cbde04213`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-34cd157023b99598cfc5">[ ] unverified</a> | <a href="#case-in_game_demolition-3efcb11b59402b534188">[ ] unverified</a> | <a href="#case-in_game_demolition-88e3b530006133672003">[ ] unverified</a> | <a href="#case-in_game_demolition-40603153035cbde04213">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-34cd157023b99598cfc5"></a>

**0° CCW: unverified** — `in_game_demolition-34cd157023b99598cfc5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3efcb11b59402b534188"></a>

**90° CCW: unverified** — `in_game_demolition-3efcb11b59402b534188`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-88e3b530006133672003"></a>

**180° CCW: unverified** — `in_game_demolition-88e3b530006133672003`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-40603153035cbde04213"></a>

**270° CCW: unverified** — `in_game_demolition-40603153035cbde04213`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-34cd157023b99598cfc5">[ ] unverified</a> | <a href="#case-in_game_save_reload-3efcb11b59402b534188">[ ] unverified</a> | <a href="#case-in_game_save_reload-88e3b530006133672003">[ ] unverified</a> | <a href="#case-in_game_save_reload-40603153035cbde04213">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-34cd157023b99598cfc5"></a>

**0° CCW: unverified** — `in_game_save_reload-34cd157023b99598cfc5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3efcb11b59402b534188"></a>

**90° CCW: unverified** — `in_game_save_reload-3efcb11b59402b534188`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-88e3b530006133672003"></a>

**180° CCW: unverified** — `in_game_save_reload-88e3b530006133672003`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-40603153035cbde04213"></a>

**270° CCW: unverified** — `in_game_save_reload-40603153035cbde04213`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4 | — | <a href="#case-in_game_route_query-2f1f10f712ae842e97eb">[ ] unverified</a> | <a href="#case-in_game_route_query-c1705909820474d3af88">[ ] unverified</a> | <a href="#case-in_game_route_query-ce78f36ee5ef0ea98ee4">[ ] unverified</a> | <a href="#case-in_game_route_query-ecbd7d6551268b3fa528">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6 | — | <a href="#case-in_game_route_query-5addcd55361d1cc778a5">[ ] unverified</a> | <a href="#case-in_game_route_query-9c9677be211a8e84eec1">[ ] unverified</a> | <a href="#case-in_game_route_query-b8baaad2643c5d485e7e">[ ] unverified</a> | <a href="#case-in_game_route_query-71a9996d8077aa950dfc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7 | — | <a href="#case-in_game_route_query-c6c42a5dc9869884c7da">[ ] unverified</a> | <a href="#case-in_game_route_query-845182e7c8ea6dcfe114">[ ] unverified</a> | <a href="#case-in_game_route_query-b4a81243ef321fef5f38">[ ] unverified</a> | <a href="#case-in_game_route_query-8bd86b02e15ab9faebe1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3 | — | <a href="#case-in_game_route_query-75f27b0db516fa487879">[ ] unverified</a> | <a href="#case-in_game_route_query-41f9553ca41821bc12b5">[ ] unverified</a> | <a href="#case-in_game_route_query-bad4cbf4fa665ca629ff">[ ] unverified</a> | <a href="#case-in_game_route_query-fa7b7a204b8184944745">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5 | — | <a href="#case-in_game_route_query-67fd1d42d3612f7b9672">[ ] unverified</a> | <a href="#case-in_game_route_query-e747028a9225289c192e">[ ] unverified</a> | <a href="#case-in_game_route_query-583166590741e950826c">[ ] unverified</a> | <a href="#case-in_game_route_query-848a366ee3b6630d9037">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5 | — | <a href="#case-in_game_route_query-498864cd90aaee35d770">[ ] unverified</a> | <a href="#case-in_game_route_query-f9ce4438391ee8009a63">[ ] unverified</a> | <a href="#case-in_game_route_query-ab1648955e35bcec4c74">[ ] unverified</a> | <a href="#case-in_game_route_query-5ff4e6b5b65f66771ff2">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4</summary>

<a id="case-in_game_route_query-2f1f10f712ae842e97eb"></a>

**0° CCW: unverified** — `in_game_route_query-2f1f10f712ae842e97eb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-c1705909820474d3af88"></a>

**90° CCW: unverified** — `in_game_route_query-c1705909820474d3af88`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-ce78f36ee5ef0ea98ee4"></a>

**180° CCW: unverified** — `in_game_route_query-ce78f36ee5ef0ea98ee4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-ecbd7d6551268b3fa528"></a>

**270° CCW: unverified** — `in_game_route_query-ecbd7d6551268b3fa528`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6</summary>

<a id="case-in_game_route_query-5addcd55361d1cc778a5"></a>

**0° CCW: unverified** — `in_game_route_query-5addcd55361d1cc778a5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_route_query-9c9677be211a8e84eec1"></a>

**90° CCW: unverified** — `in_game_route_query-9c9677be211a8e84eec1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_route_query-b8baaad2643c5d485e7e"></a>

**180° CCW: unverified** — `in_game_route_query-b8baaad2643c5d485e7e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_route_query-71a9996d8077aa950dfc"></a>

**270° CCW: unverified** — `in_game_route_query-71a9996d8077aa950dfc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7</summary>

<a id="case-in_game_route_query-c6c42a5dc9869884c7da"></a>

**0° CCW: unverified** — `in_game_route_query-c6c42a5dc9869884c7da`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-845182e7c8ea6dcfe114"></a>

**90° CCW: unverified** — `in_game_route_query-845182e7c8ea6dcfe114`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-b4a81243ef321fef5f38"></a>

**180° CCW: unverified** — `in_game_route_query-b4a81243ef321fef5f38`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-8bd86b02e15ab9faebe1"></a>

**270° CCW: unverified** — `in_game_route_query-8bd86b02e15ab9faebe1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3</summary>

<a id="case-in_game_route_query-75f27b0db516fa487879"></a>

**0° CCW: unverified** — `in_game_route_query-75f27b0db516fa487879`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-41f9553ca41821bc12b5"></a>

**90° CCW: unverified** — `in_game_route_query-41f9553ca41821bc12b5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-bad4cbf4fa665ca629ff"></a>

**180° CCW: unverified** — `in_game_route_query-bad4cbf4fa665ca629ff`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-fa7b7a204b8184944745"></a>

**270° CCW: unverified** — `in_game_route_query-fa7b7a204b8184944745`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5</summary>

<a id="case-in_game_route_query-67fd1d42d3612f7b9672"></a>

**0° CCW: unverified** — `in_game_route_query-67fd1d42d3612f7b9672`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-e747028a9225289c192e"></a>

**90° CCW: unverified** — `in_game_route_query-e747028a9225289c192e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-583166590741e950826c"></a>

**180° CCW: unverified** — `in_game_route_query-583166590741e950826c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-848a366ee3b6630d9037"></a>

**270° CCW: unverified** — `in_game_route_query-848a366ee3b6630d9037`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5</summary>

<a id="case-in_game_route_query-498864cd90aaee35d770"></a>

**0° CCW: unverified** — `in_game_route_query-498864cd90aaee35d770`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-f9ce4438391ee8009a63"></a>

**90° CCW: unverified** — `in_game_route_query-f9ce4438391ee8009a63`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-ab1648955e35bcec4c74"></a>

**180° CCW: unverified** — `in_game_route_query-ab1648955e35bcec4c74`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-5ff4e6b5b65f66771ff2"></a>

**270° CCW: unverified** — `in_game_route_query-5ff4e6b5b65f66771ff2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4 | — | <a href="#case-in_game_visible_travel-2f1f10f712ae842e97eb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c1705909820474d3af88">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ce78f36ee5ef0ea98ee4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ecbd7d6551268b3fa528">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6 | — | <a href="#case-in_game_visible_travel-5addcd55361d1cc778a5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9c9677be211a8e84eec1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b8baaad2643c5d485e7e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-71a9996d8077aa950dfc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7 | — | <a href="#case-in_game_visible_travel-c6c42a5dc9869884c7da">[ ] unverified</a> | <a href="#case-in_game_visible_travel-845182e7c8ea6dcfe114">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b4a81243ef321fef5f38">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8bd86b02e15ab9faebe1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3 | — | <a href="#case-in_game_visible_travel-75f27b0db516fa487879">[ ] unverified</a> | <a href="#case-in_game_visible_travel-41f9553ca41821bc12b5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bad4cbf4fa665ca629ff">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fa7b7a204b8184944745">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5 | — | <a href="#case-in_game_visible_travel-67fd1d42d3612f7b9672">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e747028a9225289c192e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-583166590741e950826c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-848a366ee3b6630d9037">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5 | — | <a href="#case-in_game_visible_travel-498864cd90aaee35d770">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f9ce4438391ee8009a63">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ab1648955e35bcec4c74">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5ff4e6b5b65f66771ff2">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4</summary>

<a id="case-in_game_visible_travel-2f1f10f712ae842e97eb"></a>

**0° CCW: unverified** — `in_game_visible_travel-2f1f10f712ae842e97eb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-c1705909820474d3af88"></a>

**90° CCW: unverified** — `in_game_visible_travel-c1705909820474d3af88`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-ce78f36ee5ef0ea98ee4"></a>

**180° CCW: unverified** — `in_game_visible_travel-ce78f36ee5ef0ea98ee4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-ecbd7d6551268b3fa528"></a>

**270° CCW: unverified** — `in_game_visible_travel-ecbd7d6551268b3fa528`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6</summary>

<a id="case-in_game_visible_travel-5addcd55361d1cc778a5"></a>

**0° CCW: unverified** — `in_game_visible_travel-5addcd55361d1cc778a5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-9c9677be211a8e84eec1"></a>

**90° CCW: unverified** — `in_game_visible_travel-9c9677be211a8e84eec1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-b8baaad2643c5d485e7e"></a>

**180° CCW: unverified** — `in_game_visible_travel-b8baaad2643c5d485e7e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-71a9996d8077aa950dfc"></a>

**270° CCW: unverified** — `in_game_visible_travel-71a9996d8077aa950dfc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7</summary>

<a id="case-in_game_visible_travel-c6c42a5dc9869884c7da"></a>

**0° CCW: unverified** — `in_game_visible_travel-c6c42a5dc9869884c7da`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-845182e7c8ea6dcfe114"></a>

**90° CCW: unverified** — `in_game_visible_travel-845182e7c8ea6dcfe114`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-b4a81243ef321fef5f38"></a>

**180° CCW: unverified** — `in_game_visible_travel-b4a81243ef321fef5f38`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-8bd86b02e15ab9faebe1"></a>

**270° CCW: unverified** — `in_game_visible_travel-8bd86b02e15ab9faebe1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3</summary>

<a id="case-in_game_visible_travel-75f27b0db516fa487879"></a>

**0° CCW: unverified** — `in_game_visible_travel-75f27b0db516fa487879`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-41f9553ca41821bc12b5"></a>

**90° CCW: unverified** — `in_game_visible_travel-41f9553ca41821bc12b5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-bad4cbf4fa665ca629ff"></a>

**180° CCW: unverified** — `in_game_visible_travel-bad4cbf4fa665ca629ff`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-fa7b7a204b8184944745"></a>

**270° CCW: unverified** — `in_game_visible_travel-fa7b7a204b8184944745`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5</summary>

<a id="case-in_game_visible_travel-67fd1d42d3612f7b9672"></a>

**0° CCW: unverified** — `in_game_visible_travel-67fd1d42d3612f7b9672`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-e747028a9225289c192e"></a>

**90° CCW: unverified** — `in_game_visible_travel-e747028a9225289c192e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-583166590741e950826c"></a>

**180° CCW: unverified** — `in_game_visible_travel-583166590741e950826c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-848a366ee3b6630d9037"></a>

**270° CCW: unverified** — `in_game_visible_travel-848a366ee3b6630d9037`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-5; entry: 1-E-in-9; exit: 1-N-out-5.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5</summary>

<a id="case-in_game_visible_travel-498864cd90aaee35d770"></a>

**0° CCW: unverified** — `in_game_visible_travel-498864cd90aaee35d770`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-f9ce4438391ee8009a63"></a>

**90° CCW: unverified** — `in_game_visible_travel-f9ce4438391ee8009a63`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-ab1648955e35bcec4c74"></a>

**180° CCW: unverified** — `in_game_visible_travel-ab1648955e35bcec4c74`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-5ff4e6b5b65f66771ff2"></a>

**270° CCW: unverified** — `in_game_visible_travel-5ff4e6b5b65f66771ff2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-5; entry: 1-E-in-10; exit: 1-N-out-5.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3 | — | <a href="#case-in_game_route_query-8dcce1e753fa8bddecbb">[ ] unverified</a> | <a href="#case-in_game_route_query-e1d35cd043bf5a153a44">[ ] unverified</a> | <a href="#case-in_game_route_query-d520540a64ff04387abb">[ ] unverified</a> | <a href="#case-in_game_route_query-fa9b4dad803145645b72">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2 | — | <a href="#case-in_game_route_query-782932c2204b52a33682">[ ] unverified</a> | <a href="#case-in_game_route_query-0d373c094f93802c3c87">[ ] unverified</a> | <a href="#case-in_game_route_query-2e8d94338429237d3234">[ ] unverified</a> | <a href="#case-in_game_route_query-13bd52ff7bb9d81a536c">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3</summary>

<a id="case-in_game_route_query-8dcce1e753fa8bddecbb"></a>

**0° CCW: unverified** — `in_game_route_query-8dcce1e753fa8bddecbb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-e1d35cd043bf5a153a44"></a>

**90° CCW: unverified** — `in_game_route_query-e1d35cd043bf5a153a44`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-d520540a64ff04387abb"></a>

**180° CCW: unverified** — `in_game_route_query-d520540a64ff04387abb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-fa9b4dad803145645b72"></a>

**270° CCW: unverified** — `in_game_route_query-fa9b4dad803145645b72`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2</summary>

<a id="case-in_game_route_query-782932c2204b52a33682"></a>

**0° CCW: unverified** — `in_game_route_query-782932c2204b52a33682`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-0d373c094f93802c3c87"></a>

**90° CCW: unverified** — `in_game_route_query-0d373c094f93802c3c87`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-2e8d94338429237d3234"></a>

**180° CCW: unverified** — `in_game_route_query-2e8d94338429237d3234`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-13bd52ff7bb9d81a536c"></a>

**270° CCW: unverified** — `in_game_route_query-13bd52ff7bb9d81a536c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3 | — | <a href="#case-in_game_visible_travel-8dcce1e753fa8bddecbb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e1d35cd043bf5a153a44">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d520540a64ff04387abb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fa9b4dad803145645b72">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2 | — | <a href="#case-in_game_visible_travel-782932c2204b52a33682">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0d373c094f93802c3c87">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2e8d94338429237d3234">[ ] unverified</a> | <a href="#case-in_game_visible_travel-13bd52ff7bb9d81a536c">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3</summary>

<a id="case-in_game_visible_travel-8dcce1e753fa8bddecbb"></a>

**0° CCW: unverified** — `in_game_visible_travel-8dcce1e753fa8bddecbb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-e1d35cd043bf5a153a44"></a>

**90° CCW: unverified** — `in_game_visible_travel-e1d35cd043bf5a153a44`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-d520540a64ff04387abb"></a>

**180° CCW: unverified** — `in_game_visible_travel-d520540a64ff04387abb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-fa9b4dad803145645b72"></a>

**270° CCW: unverified** — `in_game_visible_travel-fa9b4dad803145645b72`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2</summary>

<a id="case-in_game_visible_travel-782932c2204b52a33682"></a>

**0° CCW: unverified** — `in_game_visible_travel-782932c2204b52a33682`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-0d373c094f93802c3c87"></a>

**90° CCW: unverified** — `in_game_visible_travel-0d373c094f93802c3c87`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-2e8d94338429237d3234"></a>

**180° CCW: unverified** — `in_game_visible_travel-2e8d94338429237d3234`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-13bd52ff7bb9d81a536c"></a>

**270° CCW: unverified** — `in_game_visible_travel-13bd52ff7bb9d81a536c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 76 cases; unverified: 76</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-834ac3947f711cb96404">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cfaa058e93a6865d0c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34ee92ca85adbb814b93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1ed1fda3904bb4a4fee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-005afd9ca7d14c52b381">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3117c95adb2d23b598e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-561dce65ebd1226cd59b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43273a12bdf16568af2f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8a91cf724ac908d4373">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f83926617cf77234b9e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-117bb8684522f44a5f5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62217959a270ce73a218">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2573f0138b5dd192baf7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6485283faa7b534082e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25cff35bdf5de36af43d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e6cba989bcbad4be290">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a6f3a32e442c881cf4d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-050b8ea31a0805f12069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b198c035a4d0df5c4f53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bcadf7c24efe37accf28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a090f4eeb37d5ae0416">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-889a7a8e490e1dee09fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a73fda960c6cf0eb6289">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa93d735bec76ab4022d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d7756ad2dd9dd66a490">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78d045605d54c87896a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24e31cc5d43c3c2eb817">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa5f9d7b407e06a989e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a311549567f40389429">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34229b16484ad2398a2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81419a614323c811fa4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb44437c32480c17e00e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d385b2cab662231413cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6ac7de0b81d94ad02c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30ad72aaef48ac23b20b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ef6559b92bb59ee8617">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f76e2812164430e0d754">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fa22417ed0587351662">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43466fbcba8ba4e6121b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85f12b0e6f9fc5991af9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca77d88aeec38218de3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a747ea48f5b5d9cc291e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9a046b0c1f627862317">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8edeb36684350cee481d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cd926acb2ec6a62036ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c1f0db573f1595db14d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1f6125c4386a68f2deb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e0cc341c6f204142747">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a1df6c4bdd6f5d22f8dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c336245ed06e46322e06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-373cdfb052e955906376">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c83d81c6212dc71d1b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c99d9def7b44771747e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ada40377e78bd4ac98d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddd9bd6ee23f69f91a03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b320e57e7e6342a43c5f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-62584aa6134bc1321845">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7bd40f14cb318833c8d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a68c7482a94d5a809ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-925174c672267fc2338d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-051b7f764b55905a0bf5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-efe5b17d2ea3810ab5c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-188fedb34d1c43d4cbf0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7dc9a2df4e777f2a5bc3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8828294d915200825d39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66184f29606afda1f701">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ada4879d859f4090e3b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b402667ac2a709c1b6e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-309dfbb42cccc6dd117c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-781742bf04adf8de8097">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4541ed60d2c7e7d4dc3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40130d4d0377f6c61c39">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9705250c4a874d2bc13c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9952a7bac82bb71b65b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4841d83707d5b6f0fe0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-561d793af281a7f1a09c">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-834ac3947f711cb96404"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-834ac3947f711cb96404`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cfaa058e93a6865d0c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1cfaa058e93a6865d0c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34ee92ca85adbb814b93"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-34ee92ca85adbb814b93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1ed1fda3904bb4a4fee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e1ed1fda3904bb4a4fee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-005afd9ca7d14c52b381"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-005afd9ca7d14c52b381`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3117c95adb2d23b598e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3117c95adb2d23b598e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-561dce65ebd1226cd59b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-561dce65ebd1226cd59b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43273a12bdf16568af2f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43273a12bdf16568af2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8a91cf724ac908d4373"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8a91cf724ac908d4373`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f83926617cf77234b9e9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f83926617cf77234b9e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-117bb8684522f44a5f5e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-117bb8684522f44a5f5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62217959a270ce73a218"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-62217959a270ce73a218`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2573f0138b5dd192baf7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2573f0138b5dd192baf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6485283faa7b534082e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b6485283faa7b534082e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25cff35bdf5de36af43d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25cff35bdf5de36af43d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e6cba989bcbad4be290"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e6cba989bcbad4be290`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a6f3a32e442c881cf4d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6f3a32e442c881cf4d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-050b8ea31a0805f12069"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-050b8ea31a0805f12069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b198c035a4d0df5c4f53"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b198c035a4d0df5c4f53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bcadf7c24efe37accf28"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bcadf7c24efe37accf28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a090f4eeb37d5ae0416"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a090f4eeb37d5ae0416`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-889a7a8e490e1dee09fe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-889a7a8e490e1dee09fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a73fda960c6cf0eb6289"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a73fda960c6cf0eb6289`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa93d735bec76ab4022d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aa93d735bec76ab4022d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d7756ad2dd9dd66a490"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d7756ad2dd9dd66a490`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78d045605d54c87896a1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78d045605d54c87896a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24e31cc5d43c3c2eb817"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-24e31cc5d43c3c2eb817`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa5f9d7b407e06a989e2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aa5f9d7b407e06a989e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a311549567f40389429"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a311549567f40389429`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34229b16484ad2398a2a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-34229b16484ad2398a2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81419a614323c811fa4d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81419a614323c811fa4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb44437c32480c17e00e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb44437c32480c17e00e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d385b2cab662231413cb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d385b2cab662231413cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6ac7de0b81d94ad02c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a6ac7de0b81d94ad02c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30ad72aaef48ac23b20b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-30ad72aaef48ac23b20b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ef6559b92bb59ee8617"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0ef6559b92bb59ee8617`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f76e2812164430e0d754"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f76e2812164430e0d754`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fa22417ed0587351662"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8fa22417ed0587351662`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43466fbcba8ba4e6121b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-43466fbcba8ba4e6121b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85f12b0e6f9fc5991af9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-85f12b0e6f9fc5991af9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca77d88aeec38218de3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca77d88aeec38218de3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a747ea48f5b5d9cc291e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a747ea48f5b5d9cc291e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9a046b0c1f627862317"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a9a046b0c1f627862317`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8edeb36684350cee481d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8edeb36684350cee481d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cd926acb2ec6a62036ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd926acb2ec6a62036ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c1f0db573f1595db14d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c1f0db573f1595db14d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1f6125c4386a68f2deb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b1f6125c4386a68f2deb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e0cc341c6f204142747"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e0cc341c6f204142747`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a1df6c4bdd6f5d22f8dd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a1df6c4bdd6f5d22f8dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c336245ed06e46322e06"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c336245ed06e46322e06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-373cdfb052e955906376"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-373cdfb052e955906376`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c83d81c6212dc71d1b9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3c83d81c6212dc71d1b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c99d9def7b44771747e2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c99d9def7b44771747e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ada40377e78bd4ac98d3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ada40377e78bd4ac98d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddd9bd6ee23f69f91a03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ddd9bd6ee23f69f91a03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b320e57e7e6342a43c5f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b320e57e7e6342a43c5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-62584aa6134bc1321845"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-62584aa6134bc1321845`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7bd40f14cb318833c8d5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7bd40f14cb318833c8d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a68c7482a94d5a809ba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a68c7482a94d5a809ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-925174c672267fc2338d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-925174c672267fc2338d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-051b7f764b55905a0bf5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-051b7f764b55905a0bf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-efe5b17d2ea3810ab5c5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-efe5b17d2ea3810ab5c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-188fedb34d1c43d4cbf0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-188fedb34d1c43d4cbf0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7dc9a2df4e777f2a5bc3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7dc9a2df4e777f2a5bc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8828294d915200825d39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8828294d915200825d39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66184f29606afda1f701"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-66184f29606afda1f701`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ada4879d859f4090e3b2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ada4879d859f4090e3b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b402667ac2a709c1b6e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b402667ac2a709c1b6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-309dfbb42cccc6dd117c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-309dfbb42cccc6dd117c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-781742bf04adf8de8097"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-781742bf04adf8de8097`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4541ed60d2c7e7d4dc3a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4541ed60d2c7e7d4dc3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40130d4d0377f6c61c39"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40130d4d0377f6c61c39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9705250c4a874d2bc13c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9705250c4a874d2bc13c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9952a7bac82bb71b65b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9952a7bac82bb71b65b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4841d83707d5b6f0fe0e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4841d83707d5b6f0fe0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-561d793af281a7f1a09c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-561d793af281a7f1a09c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6396ba8f92dba1a6e741">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9ca72e7ac9aebafdc6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e27da894749cad88a2fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9707bd429c1e853899b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b32a95376a0fee894319">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf3540106555971cdcc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3cc676586b01ba6aefb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6329a0eb9034ea11fc9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8443deca56ef38b8cccd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89953c4b8130eb478d7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a38e82f35738c5858472">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69672a28fbda0a79c270">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9af3246dde23d7134dc2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e6398067f78fd897799">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04c8941dcbcec4cf4c3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b35da25fe60bc8009ab3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9204cf10996063c8e3d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19da9893dba7533ccbe2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62708fa74fd3cb2c577b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50e6045640f95e43d3e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d9486698ccba3a5d2f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49219cb8141db3ddeb4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85e85d931a2706777db9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ba335ba477c7afbb338">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3643b44acf918dad4f55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6aa4d1530f48b842e8c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b23f23805e7c405483bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d8cde4f559fca49289a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dc07daec12935f162b89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f4d6fbcf0c5d7ee4250">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-108e6d3ede4bc9bd1082">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ea8ff3aaf1954f0a34a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-98956a5e7134950f96f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf2ff8861d85ba332e56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7667e5f984bf9b10ad7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2558f3818641817e964">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b87346edb5d0d11042d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4341673ab6585e09c47b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8df188f97bb1a69cc99b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62922e2298e549afbc2d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6396ba8f92dba1a6e741"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6396ba8f92dba1a6e741`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9ca72e7ac9aebafdc6d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9ca72e7ac9aebafdc6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e27da894749cad88a2fc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e27da894749cad88a2fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9707bd429c1e853899b9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9707bd429c1e853899b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b32a95376a0fee894319"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b32a95376a0fee894319`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf3540106555971cdcc8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bf3540106555971cdcc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3cc676586b01ba6aefb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c3cc676586b01ba6aefb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6329a0eb9034ea11fc9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a6329a0eb9034ea11fc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8443deca56ef38b8cccd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8443deca56ef38b8cccd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89953c4b8130eb478d7e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-89953c4b8130eb478d7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a38e82f35738c5858472"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a38e82f35738c5858472`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69672a28fbda0a79c270"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69672a28fbda0a79c270`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9af3246dde23d7134dc2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9af3246dde23d7134dc2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e6398067f78fd897799"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e6398067f78fd897799`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04c8941dcbcec4cf4c3b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-04c8941dcbcec4cf4c3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b35da25fe60bc8009ab3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b35da25fe60bc8009ab3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9204cf10996063c8e3d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9204cf10996063c8e3d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19da9893dba7533ccbe2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-19da9893dba7533ccbe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62708fa74fd3cb2c577b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-62708fa74fd3cb2c577b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50e6045640f95e43d3e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-50e6045640f95e43d3e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d9486698ccba3a5d2f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d9486698ccba3a5d2f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49219cb8141db3ddeb4d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-49219cb8141db3ddeb4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85e85d931a2706777db9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85e85d931a2706777db9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ba335ba477c7afbb338"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ba335ba477c7afbb338`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3643b44acf918dad4f55"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3643b44acf918dad4f55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6aa4d1530f48b842e8c0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6aa4d1530f48b842e8c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b23f23805e7c405483bf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b23f23805e7c405483bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d8cde4f559fca49289a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d8cde4f559fca49289a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dc07daec12935f162b89"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dc07daec12935f162b89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f4d6fbcf0c5d7ee4250"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f4d6fbcf0c5d7ee4250`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-108e6d3ede4bc9bd1082"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-108e6d3ede4bc9bd1082`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ea8ff3aaf1954f0a34a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3ea8ff3aaf1954f0a34a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-98956a5e7134950f96f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-98956a5e7134950f96f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf2ff8861d85ba332e56"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bf2ff8861d85ba332e56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7667e5f984bf9b10ad7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d7667e5f984bf9b10ad7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2558f3818641817e964"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e2558f3818641817e964`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b87346edb5d0d11042d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b87346edb5d0d11042d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4341673ab6585e09c47b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4341673ab6585e09c47b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8df188f97bb1a69cc99b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8df188f97bb1a69cc99b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62922e2298e549afbc2d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-62922e2298e549afbc2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c71082290e55ca77a51d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09861aae4c3bb190110a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7a38a1df6ec1649586f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-992242b2025798d563e1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ef156e0f530ad422d88b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df20e3efcff8692f880c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cc8f71d2512af59380f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e8b25ddcc4dafd3fea2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f191a25d81dcfd1b287c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-840beaa134df3c0bf5e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d0548e0a2a04852bed8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df337400477a90480f68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-82b7af222600793486e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95b4374da6dfbd2b13ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b5f393d5a2f83a06800">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46c09cf3a77c57e4ca67">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f93c1b87c8c0fd2bb938">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa8b23e2d0d8f99064f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7273c8a35a718a947017">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9198d9179063d121ba16">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-df3b4de4e128523adb18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b95c2ec4e447325337b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c78e05364f3647061def">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bacbc5b1e9977f3eca71">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8a6414170c90be4a2295">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83f3e5cb7b8316408caf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5589de8f28e5a8c0848f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a4e840a9474d38dda3c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2dd744b0582d0731079">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffe3e4fe34c51e095bf0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9366e2fc82793d7cbf17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90b3130996353499a79f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aca552e48376b80ac99b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-179bd5190c83b9991886">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b34783aa4b772929f5ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee86bdc75df321bf7ebd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2aa915dbe0cc7e9d3bd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26c3dbf048a91db8b075">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1fb504081d0722c74b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2cb386c26ee65d10c2d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c71082290e55ca77a51d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c71082290e55ca77a51d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09861aae4c3bb190110a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-09861aae4c3bb190110a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7a38a1df6ec1649586f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a7a38a1df6ec1649586f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-992242b2025798d563e1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-992242b2025798d563e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ef156e0f530ad422d88b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ef156e0f530ad422d88b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df20e3efcff8692f880c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-df20e3efcff8692f880c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cc8f71d2512af59380f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5cc8f71d2512af59380f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e8b25ddcc4dafd3fea2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e8b25ddcc4dafd3fea2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f191a25d81dcfd1b287c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f191a25d81dcfd1b287c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-840beaa134df3c0bf5e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-840beaa134df3c0bf5e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d0548e0a2a04852bed8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8d0548e0a2a04852bed8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df337400477a90480f68"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-df337400477a90480f68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-82b7af222600793486e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-82b7af222600793486e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95b4374da6dfbd2b13ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-95b4374da6dfbd2b13ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b5f393d5a2f83a06800"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0b5f393d5a2f83a06800`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46c09cf3a77c57e4ca67"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-46c09cf3a77c57e4ca67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f93c1b87c8c0fd2bb938"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f93c1b87c8c0fd2bb938`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa8b23e2d0d8f99064f2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa8b23e2d0d8f99064f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7273c8a35a718a947017"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7273c8a35a718a947017`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9198d9179063d121ba16"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9198d9179063d121ba16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-df3b4de4e128523adb18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-df3b4de4e128523adb18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b95c2ec4e447325337b4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b95c2ec4e447325337b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c78e05364f3647061def"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c78e05364f3647061def`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bacbc5b1e9977f3eca71"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bacbc5b1e9977f3eca71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8a6414170c90be4a2295"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8a6414170c90be4a2295`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83f3e5cb7b8316408caf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-83f3e5cb7b8316408caf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5589de8f28e5a8c0848f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5589de8f28e5a8c0848f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a4e840a9474d38dda3c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5a4e840a9474d38dda3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c2dd744b0582d0731079"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c2dd744b0582d0731079`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffe3e4fe34c51e095bf0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ffe3e4fe34c51e095bf0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9366e2fc82793d7cbf17"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9366e2fc82793d7cbf17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90b3130996353499a79f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-90b3130996353499a79f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aca552e48376b80ac99b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aca552e48376b80ac99b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-179bd5190c83b9991886"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-179bd5190c83b9991886`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b34783aa4b772929f5ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b34783aa4b772929f5ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee86bdc75df321bf7ebd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee86bdc75df321bf7ebd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2aa915dbe0cc7e9d3bd3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2aa915dbe0cc7e9d3bd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26c3dbf048a91db8b075"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-26c3dbf048a91db8b075`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1fb504081d0722c74b6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b1fb504081d0722c74b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2cb386c26ee65d10c2d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d2cb386c26ee65d10c2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2dd0d025a4d6991fa20">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49a15a30b546fccbf8f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69fb5614250a64301f2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-776ad1cbf85dcf6536ab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a38685ac4a9aa431af3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-625bf076920af9002456">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ee8f6a576fd53384e25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8255293fe79ceb1cf28a">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c2dd0d025a4d6991fa20"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c2dd0d025a4d6991fa20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49a15a30b546fccbf8f6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-49a15a30b546fccbf8f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69fb5614250a64301f2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-69fb5614250a64301f2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-776ad1cbf85dcf6536ab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-776ad1cbf85dcf6536ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a38685ac4a9aa431af3f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a38685ac4a9aa431af3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-625bf076920af9002456"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-625bf076920af9002456`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ee8f6a576fd53384e25"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2ee8f6a576fd53384e25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8255293fe79ceb1cf28a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8255293fe79ceb1cf28a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-northwest-junction:canonical-southeast | <a href="#case-preview_review-dc931912ba40eb1296fc">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-northwest-junction:canonical-top | <a href="#case-preview_review-dca9a6ac16d9e1df4047">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-northwest-junction:connection-overview | <a href="#case-preview_review-114d78931935c8958537">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-northwest-junction:canonical-southeast</summary>

<a id="case-preview_review-dc931912ba40eb1296fc"></a>

**General: unverified** — `preview_review-dc931912ba40eb1296fc`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-northwest-junction:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-northwest-junction:canonical-top</summary>

<a id="case-preview_review-dca9a6ac16d9e1df4047"></a>

**General: unverified** — `preview_review-dca9a6ac16d9e1df4047`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-northwest-junction:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-northwest-junction:connection-overview</summary>

<a id="case-preview_review-114d78931935c8958537"></a>

**General: unverified** — `preview_review-114d78931935c8958537`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-northwest-junction:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
