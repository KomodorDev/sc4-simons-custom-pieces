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

Contains the northwest surface junction and the lower-deck ramp landings. Both avenue directions can enter the lower deck or receive traffic leaving that deck. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

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
| `1-S-out-4` | road / 1 / primary | out | [2.237287, -40.0, 3.985684]; [-0.05054654119578982, -0.998721706569524]; 0.338466957 | `path-interface-e962113498b0059e6dc4` |
| `1-N-out-5` | road / 1 / primary | out | [3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-E-in-6` | road / 1 / primary | in | [8.0, -24.015569, 0.0]; [-0.7262547071069894, -0.6874257053710903]; 0.0 | `path-interface-72fb336ee867ba7d9c96` |
| `1-S-out-7` | road / 1 / primary | out | [8.016449, -24.0, 0.0]; [-0.7262546147312291, -0.6874258029646502]; 0.0 | `path-interface-4cf26ae2e87bbd79ef30` |
| `1-S-out-8` | road / 1 / primary | out | [12.8, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-S-out-9` | road / 1 / primary | out | [18.319815, -24.0, 0.0]; [0.09391289549060457, -0.9955804176763274]; 0.0 | `path-interface-13942085a6106bbb7ffc` |
| `1-S-out-10` | road / 1 / primary | out | [19.2, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-E-in-11` | road / 1 / primary | in | [24.0, -19.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-E-in-12` | road / 1 / primary | in | [24.0, -18.319815, 0.0]; [-0.9955804176763274, 0.09391289549060457]; 0.0 | `path-interface-cf8230f2cf90d80dde56` |
| `1-E-in-13` | road / 1 / primary | in | [24.0, -12.8, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-in-14` | road / 1 / primary | in | [24.0, -8.016449, 0.0]; [-0.6874258029646502, -0.7262546147312291]; 0.0 | `path-interface-eccc0f2ac290f14c28d8` |
| `1-S-out-15` | road / 1 / primary | out | [24.015569, -8.0, 0.0]; [-0.6874257053710903, -0.7262547071069894]; 0.0 | `path-interface-b4cdbf5b9c0b3b50a875` |
| `1-E-in-16` | road / 1 / primary | in | [40.0, -2.237287, 3.985684]; [-0.998721706569524, -0.05054654119578982]; -0.338466957 | `path-interface-3f53148c09905eadd6a6` |
| `2-W-in-1` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-N-out-2` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-S-out-3` | pedestrian / 2 / primary | out | [8.7, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-E-in-4` | pedestrian / 2 / primary | in | [24.0, -8.7, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-1` → `1-S-out-4` | primary |
| road | `1-W-in-1` → `1-S-out-8` | primary |
| road | `1-W-in-2` → `1-S-out-10` | primary |
| road | `1-E-in-6` → `1-S-out-4` | primary |
| road | `1-E-in-11` → `1-N-out-3` | primary |
| road | `1-E-in-12` → `1-S-out-7` | primary |
| road | `1-E-in-13` → `1-N-out-5` | primary |
| road | `1-E-in-14` → `1-S-out-9` | primary |
| road | `1-E-in-16` → `1-S-out-15` | primary |
| road | `1-E-in-16` → `1-N-out-5` | primary |
| pedestrian | `2-W-in-1` → `2-S-out-3` | primary |
| pedestrian | `2-E-in-4` → `2-N-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-1` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-6` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-11` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-12` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-13` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-14` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-16` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-northwest-junction --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The current assembly’s executed checks and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/48 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/48 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 468, passed: 0, failed: 0, stale: 0, not_applicable: 0.

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
<summary>Route Query — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4 | — | <a href="#case-in_game_route_query-2f1f10f712ae842e97eb">[ ] unverified</a> | <a href="#case-in_game_route_query-c1705909820474d3af88">[ ] unverified</a> | <a href="#case-in_game_route_query-ce78f36ee5ef0ea98ee4">[ ] unverified</a> | <a href="#case-in_game_route_query-ecbd7d6551268b3fa528">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8 | — | <a href="#case-in_game_route_query-d313433b8b63cd2d8da7">[ ] unverified</a> | <a href="#case-in_game_route_query-6f0775f1c081cd55911a">[ ] unverified</a> | <a href="#case-in_game_route_query-7b9b05e49e3308166d9a">[ ] unverified</a> | <a href="#case-in_game_route_query-e65c3de9f1e9031ca690">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10 | — | <a href="#case-in_game_route_query-a46b23160e11c879f74d">[ ] unverified</a> | <a href="#case-in_game_route_query-5bd4932502d77df1640e">[ ] unverified</a> | <a href="#case-in_game_route_query-82abf91dcf821e650bed">[ ] unverified</a> | <a href="#case-in_game_route_query-260a19b849e2abce1612">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4 | — | <a href="#case-in_game_route_query-202daceb9b53b4ca963f">[ ] unverified</a> | <a href="#case-in_game_route_query-b8925374eab51d9509e9">[ ] unverified</a> | <a href="#case-in_game_route_query-c2e16f4836d563aa02ac">[ ] unverified</a> | <a href="#case-in_game_route_query-5d18dfde9bd83b6ef3b5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3 | — | <a href="#case-in_game_route_query-075d49a2194d1d0f2ace">[ ] unverified</a> | <a href="#case-in_game_route_query-413ee4b1189c1c8e0f46">[ ] unverified</a> | <a href="#case-in_game_route_query-be56a0b4c8b8f9c8ff04">[ ] unverified</a> | <a href="#case-in_game_route_query-cab084ffb3e3b1500399">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7 | — | <a href="#case-in_game_route_query-1ae58fe4ba8c2434301b">[ ] unverified</a> | <a href="#case-in_game_route_query-888d04edad48bfea233b">[ ] unverified</a> | <a href="#case-in_game_route_query-7849325e392728fef59a">[ ] unverified</a> | <a href="#case-in_game_route_query-2bc82600b584fa199ac8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5 | — | <a href="#case-in_game_route_query-1105f0cb42fc162e4afb">[ ] unverified</a> | <a href="#case-in_game_route_query-ff5c9aaedbbe22786ce9">[ ] unverified</a> | <a href="#case-in_game_route_query-cd3812e8efe0e009d429">[ ] unverified</a> | <a href="#case-in_game_route_query-2840fd238624cd517088">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9 | — | <a href="#case-in_game_route_query-7e74852c80b4925dc9f8">[ ] unverified</a> | <a href="#case-in_game_route_query-768bf6b69c81075914b9">[ ] unverified</a> | <a href="#case-in_game_route_query-77a8d76f04a36fb68a07">[ ] unverified</a> | <a href="#case-in_game_route_query-8d02f69d512561e7ba7e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15 | — | <a href="#case-in_game_route_query-d6f7304f2d72dbfecbf1">[ ] unverified</a> | <a href="#case-in_game_route_query-594fa39716c9160a3977">[ ] unverified</a> | <a href="#case-in_game_route_query-c957116f7969005bdc8f">[ ] unverified</a> | <a href="#case-in_game_route_query-a06807a5e2e597258b8c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5 | — | <a href="#case-in_game_route_query-1fb9f2efe77d2c793e2f">[ ] unverified</a> | <a href="#case-in_game_route_query-62dba10af526c9f3fd11">[ ] unverified</a> | <a href="#case-in_game_route_query-1256052981d48309158e">[ ] unverified</a> | <a href="#case-in_game_route_query-6e39e7d73d668fbdab3c">[ ] unverified</a> |


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
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8</summary>

<a id="case-in_game_route_query-d313433b8b63cd2d8da7"></a>

**0° CCW: unverified** — `in_game_route_query-d313433b8b63cd2d8da7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_route_query-6f0775f1c081cd55911a"></a>

**90° CCW: unverified** — `in_game_route_query-6f0775f1c081cd55911a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_route_query-7b9b05e49e3308166d9a"></a>

**180° CCW: unverified** — `in_game_route_query-7b9b05e49e3308166d9a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_route_query-e65c3de9f1e9031ca690"></a>

**270° CCW: unverified** — `in_game_route_query-e65c3de9f1e9031ca690`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10</summary>

<a id="case-in_game_route_query-a46b23160e11c879f74d"></a>

**0° CCW: unverified** — `in_game_route_query-a46b23160e11c879f74d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-5bd4932502d77df1640e"></a>

**90° CCW: unverified** — `in_game_route_query-5bd4932502d77df1640e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-82abf91dcf821e650bed"></a>

**180° CCW: unverified** — `in_game_route_query-82abf91dcf821e650bed`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_route_query-260a19b849e2abce1612"></a>

**270° CCW: unverified** — `in_game_route_query-260a19b849e2abce1612`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4</summary>

<a id="case-in_game_route_query-202daceb9b53b4ca963f"></a>

**0° CCW: unverified** — `in_game_route_query-202daceb9b53b4ca963f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-b8925374eab51d9509e9"></a>

**90° CCW: unverified** — `in_game_route_query-b8925374eab51d9509e9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-c2e16f4836d563aa02ac"></a>

**180° CCW: unverified** — `in_game_route_query-c2e16f4836d563aa02ac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_route_query-5d18dfde9bd83b6ef3b5"></a>

**270° CCW: unverified** — `in_game_route_query-5d18dfde9bd83b6ef3b5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3</summary>

<a id="case-in_game_route_query-075d49a2194d1d0f2ace"></a>

**0° CCW: unverified** — `in_game_route_query-075d49a2194d1d0f2ace`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-413ee4b1189c1c8e0f46"></a>

**90° CCW: unverified** — `in_game_route_query-413ee4b1189c1c8e0f46`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-be56a0b4c8b8f9c8ff04"></a>

**180° CCW: unverified** — `in_game_route_query-be56a0b4c8b8f9c8ff04`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-cab084ffb3e3b1500399"></a>

**270° CCW: unverified** — `in_game_route_query-cab084ffb3e3b1500399`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7</summary>

<a id="case-in_game_route_query-1ae58fe4ba8c2434301b"></a>

**0° CCW: unverified** — `in_game_route_query-1ae58fe4ba8c2434301b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-888d04edad48bfea233b"></a>

**90° CCW: unverified** — `in_game_route_query-888d04edad48bfea233b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-7849325e392728fef59a"></a>

**180° CCW: unverified** — `in_game_route_query-7849325e392728fef59a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-2bc82600b584fa199ac8"></a>

**270° CCW: unverified** — `in_game_route_query-2bc82600b584fa199ac8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5</summary>

<a id="case-in_game_route_query-1105f0cb42fc162e4afb"></a>

**0° CCW: unverified** — `in_game_route_query-1105f0cb42fc162e4afb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-ff5c9aaedbbe22786ce9"></a>

**90° CCW: unverified** — `in_game_route_query-ff5c9aaedbbe22786ce9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-cd3812e8efe0e009d429"></a>

**180° CCW: unverified** — `in_game_route_query-cd3812e8efe0e009d429`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-2840fd238624cd517088"></a>

**270° CCW: unverified** — `in_game_route_query-2840fd238624cd517088`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9</summary>

<a id="case-in_game_route_query-7e74852c80b4925dc9f8"></a>

**0° CCW: unverified** — `in_game_route_query-7e74852c80b4925dc9f8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9.

No observation recorded.

<a id="case-in_game_route_query-768bf6b69c81075914b9"></a>

**90° CCW: unverified** — `in_game_route_query-768bf6b69c81075914b9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9.

No observation recorded.

<a id="case-in_game_route_query-77a8d76f04a36fb68a07"></a>

**180° CCW: unverified** — `in_game_route_query-77a8d76f04a36fb68a07`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9.

No observation recorded.

<a id="case-in_game_route_query-8d02f69d512561e7ba7e"></a>

**270° CCW: unverified** — `in_game_route_query-8d02f69d512561e7ba7e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15</summary>

<a id="case-in_game_route_query-d6f7304f2d72dbfecbf1"></a>

**0° CCW: unverified** — `in_game_route_query-d6f7304f2d72dbfecbf1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15.

No observation recorded.

<a id="case-in_game_route_query-594fa39716c9160a3977"></a>

**90° CCW: unverified** — `in_game_route_query-594fa39716c9160a3977`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15.

No observation recorded.

<a id="case-in_game_route_query-c957116f7969005bdc8f"></a>

**180° CCW: unverified** — `in_game_route_query-c957116f7969005bdc8f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15.

No observation recorded.

<a id="case-in_game_route_query-a06807a5e2e597258b8c"></a>

**270° CCW: unverified** — `in_game_route_query-a06807a5e2e597258b8c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5</summary>

<a id="case-in_game_route_query-1fb9f2efe77d2c793e2f"></a>

**0° CCW: unverified** — `in_game_route_query-1fb9f2efe77d2c793e2f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-62dba10af526c9f3fd11"></a>

**90° CCW: unverified** — `in_game_route_query-62dba10af526c9f3fd11`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-1256052981d48309158e"></a>

**180° CCW: unverified** — `in_game_route_query-1256052981d48309158e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_route_query-6e39e7d73d668fbdab3c"></a>

**270° CCW: unverified** — `in_game_route_query-6e39e7d73d668fbdab3c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-4; entry: 1-W-in-1; exit: 1-S-out-4 | — | <a href="#case-in_game_visible_travel-2f1f10f712ae842e97eb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c1705909820474d3af88">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ce78f36ee5ef0ea98ee4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ecbd7d6551268b3fa528">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8 | — | <a href="#case-in_game_visible_travel-d313433b8b63cd2d8da7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6f0775f1c081cd55911a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7b9b05e49e3308166d9a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e65c3de9f1e9031ca690">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10 | — | <a href="#case-in_game_visible_travel-a46b23160e11c879f74d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5bd4932502d77df1640e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-82abf91dcf821e650bed">[ ] unverified</a> | <a href="#case-in_game_visible_travel-260a19b849e2abce1612">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4 | — | <a href="#case-in_game_visible_travel-202daceb9b53b4ca963f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b8925374eab51d9509e9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c2e16f4836d563aa02ac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5d18dfde9bd83b6ef3b5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3 | — | <a href="#case-in_game_visible_travel-075d49a2194d1d0f2ace">[ ] unverified</a> | <a href="#case-in_game_visible_travel-413ee4b1189c1c8e0f46">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be56a0b4c8b8f9c8ff04">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cab084ffb3e3b1500399">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7 | — | <a href="#case-in_game_visible_travel-1ae58fe4ba8c2434301b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-888d04edad48bfea233b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7849325e392728fef59a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2bc82600b584fa199ac8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5 | — | <a href="#case-in_game_visible_travel-1105f0cb42fc162e4afb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff5c9aaedbbe22786ce9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cd3812e8efe0e009d429">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2840fd238624cd517088">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9 | — | <a href="#case-in_game_visible_travel-7e74852c80b4925dc9f8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-768bf6b69c81075914b9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-77a8d76f04a36fb68a07">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8d02f69d512561e7ba7e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15 | — | <a href="#case-in_game_visible_travel-d6f7304f2d72dbfecbf1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-594fa39716c9160a3977">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c957116f7969005bdc8f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a06807a5e2e597258b8c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5 | — | <a href="#case-in_game_visible_travel-1fb9f2efe77d2c793e2f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-62dba10af526c9f3fd11">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1256052981d48309158e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6e39e7d73d668fbdab3c">[ ] unverified</a> |


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
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8</summary>

<a id="case-in_game_visible_travel-d313433b8b63cd2d8da7"></a>

**0° CCW: unverified** — `in_game_visible_travel-d313433b8b63cd2d8da7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-6f0775f1c081cd55911a"></a>

**90° CCW: unverified** — `in_game_visible_travel-6f0775f1c081cd55911a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-7b9b05e49e3308166d9a"></a>

**180° CCW: unverified** — `in_game_visible_travel-7b9b05e49e3308166d9a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-e65c3de9f1e9031ca690"></a>

**270° CCW: unverified** — `in_game_visible_travel-e65c3de9f1e9031ca690`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-8; entry: 1-W-in-1; exit: 1-S-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10</summary>

<a id="case-in_game_visible_travel-a46b23160e11c879f74d"></a>

**0° CCW: unverified** — `in_game_visible_travel-a46b23160e11c879f74d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-5bd4932502d77df1640e"></a>

**90° CCW: unverified** — `in_game_visible_travel-5bd4932502d77df1640e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-82abf91dcf821e650bed"></a>

**180° CCW: unverified** — `in_game_visible_travel-82abf91dcf821e650bed`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-260a19b849e2abce1612"></a>

**270° CCW: unverified** — `in_game_visible_travel-260a19b849e2abce1612`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-10; entry: 1-W-in-2; exit: 1-S-out-10.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4</summary>

<a id="case-in_game_visible_travel-202daceb9b53b4ca963f"></a>

**0° CCW: unverified** — `in_game_visible_travel-202daceb9b53b4ca963f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-b8925374eab51d9509e9"></a>

**90° CCW: unverified** — `in_game_visible_travel-b8925374eab51d9509e9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-c2e16f4836d563aa02ac"></a>

**180° CCW: unverified** — `in_game_visible_travel-c2e16f4836d563aa02ac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-5d18dfde9bd83b6ef3b5"></a>

**270° CCW: unverified** — `in_game_visible_travel-5d18dfde9bd83b6ef3b5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-6>1-S-out-4; entry: 1-E-in-6; exit: 1-S-out-4.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3</summary>

<a id="case-in_game_visible_travel-075d49a2194d1d0f2ace"></a>

**0° CCW: unverified** — `in_game_visible_travel-075d49a2194d1d0f2ace`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-413ee4b1189c1c8e0f46"></a>

**90° CCW: unverified** — `in_game_visible_travel-413ee4b1189c1c8e0f46`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-be56a0b4c8b8f9c8ff04"></a>

**180° CCW: unverified** — `in_game_visible_travel-be56a0b4c8b8f9c8ff04`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-cab084ffb3e3b1500399"></a>

**270° CCW: unverified** — `in_game_visible_travel-cab084ffb3e3b1500399`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-11>1-N-out-3; entry: 1-E-in-11; exit: 1-N-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7</summary>

<a id="case-in_game_visible_travel-1ae58fe4ba8c2434301b"></a>

**0° CCW: unverified** — `in_game_visible_travel-1ae58fe4ba8c2434301b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-888d04edad48bfea233b"></a>

**90° CCW: unverified** — `in_game_visible_travel-888d04edad48bfea233b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-7849325e392728fef59a"></a>

**180° CCW: unverified** — `in_game_visible_travel-7849325e392728fef59a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-2bc82600b584fa199ac8"></a>

**270° CCW: unverified** — `in_game_visible_travel-2bc82600b584fa199ac8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-12>1-S-out-7; entry: 1-E-in-12; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5</summary>

<a id="case-in_game_visible_travel-1105f0cb42fc162e4afb"></a>

**0° CCW: unverified** — `in_game_visible_travel-1105f0cb42fc162e4afb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-ff5c9aaedbbe22786ce9"></a>

**90° CCW: unverified** — `in_game_visible_travel-ff5c9aaedbbe22786ce9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-cd3812e8efe0e009d429"></a>

**180° CCW: unverified** — `in_game_visible_travel-cd3812e8efe0e009d429`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-2840fd238624cd517088"></a>

**270° CCW: unverified** — `in_game_visible_travel-2840fd238624cd517088`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-13>1-N-out-5; entry: 1-E-in-13; exit: 1-N-out-5.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9</summary>

<a id="case-in_game_visible_travel-7e74852c80b4925dc9f8"></a>

**0° CCW: unverified** — `in_game_visible_travel-7e74852c80b4925dc9f8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-768bf6b69c81075914b9"></a>

**90° CCW: unverified** — `in_game_visible_travel-768bf6b69c81075914b9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-77a8d76f04a36fb68a07"></a>

**180° CCW: unverified** — `in_game_visible_travel-77a8d76f04a36fb68a07`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-8d02f69d512561e7ba7e"></a>

**270° CCW: unverified** — `in_game_visible_travel-8d02f69d512561e7ba7e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-14>1-S-out-9; entry: 1-E-in-14; exit: 1-S-out-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15</summary>

<a id="case-in_game_visible_travel-d6f7304f2d72dbfecbf1"></a>

**0° CCW: unverified** — `in_game_visible_travel-d6f7304f2d72dbfecbf1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-594fa39716c9160a3977"></a>

**90° CCW: unverified** — `in_game_visible_travel-594fa39716c9160a3977`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-c957116f7969005bdc8f"></a>

**180° CCW: unverified** — `in_game_visible_travel-c957116f7969005bdc8f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-a06807a5e2e597258b8c"></a>

**270° CCW: unverified** — `in_game_visible_travel-a06807a5e2e597258b8c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-S-out-15; entry: 1-E-in-16; exit: 1-S-out-15.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5</summary>

<a id="case-in_game_visible_travel-1fb9f2efe77d2c793e2f"></a>

**0° CCW: unverified** — `in_game_visible_travel-1fb9f2efe77d2c793e2f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-62dba10af526c9f3fd11"></a>

**90° CCW: unverified** — `in_game_visible_travel-62dba10af526c9f3fd11`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-1256052981d48309158e"></a>

**180° CCW: unverified** — `in_game_visible_travel-1256052981d48309158e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-6e39e7d73d668fbdab3c"></a>

**270° CCW: unverified** — `in_game_visible_travel-6e39e7d73d668fbdab3c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-16>1-N-out-5; entry: 1-E-in-16; exit: 1-N-out-5.

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
<summary>Forbidden transfer — road → road — 216 cases; unverified: 216</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-834ac3947f711cb96404">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cfaa058e93a6865d0c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34ee92ca85adbb814b93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1ed1fda3904bb4a4fee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-005afd9ca7d14c52b381">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3117c95adb2d23b598e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-561dce65ebd1226cd59b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43273a12bdf16568af2f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8a91cf724ac908d4373">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f83926617cf77234b9e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-117bb8684522f44a5f5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62217959a270ce73a218">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-38642be6a74674a9d28e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e02e215b74c412f2e7b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1907fc26a51e6a34c322">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d599f829349c87d6ac1c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d54812ae3724d393a8f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28447e0ea73ee37908a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c24ce12acf2884d44cb1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee530ff45bce40d48b5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca6608e2529b894b2159">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a188150e2dfbccc485fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c97188989c7027916556">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b03dc50d2e87ec4ff303">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2573f0138b5dd192baf7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6485283faa7b534082e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25cff35bdf5de36af43d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e6cba989bcbad4be290">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a6f3a32e442c881cf4d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-050b8ea31a0805f12069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b198c035a4d0df5c4f53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bcadf7c24efe37accf28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a090f4eeb37d5ae0416">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-889a7a8e490e1dee09fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a73fda960c6cf0eb6289">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa93d735bec76ab4022d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c49b9335cf869804e822">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48ba381f44d5cd3e75c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff358fb99048545f2ff1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49ff9e17c5e956216992">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7599b2fccc8ce85dd30f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa3b5d70b4a15f6aef01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-149588bd4ce6a74c6fc6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f56039055df428602d4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d3a74f3b26ea41efeb5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-292de8270aa589135d3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e07ccfca3b8c328e3d5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b619fa0fca66a1fb44d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-af5c33e675feceb14ff1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8e1648738295b29e47a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31e0eb6348d199b8b2ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f723714ac316764fd5f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c55e423a24584397681d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ee3cdb0a4d3c8db561e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47c61c97e07f0174a979">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64ce4e9222d7a62684a5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-88d09aafd0a1366e0647">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a39eb08086c74715c309">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8d8ea3bc5e0688cc9cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e023f77efa93ab779b40">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa2d8d627bd1ba36ad8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9816fd1911324d9df2b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7da69dc6684997478db8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70411e55bef709f1ce00">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee120a1f690cc44b1da5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48c86eb4d67793a26564">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d44d6062ed1153131e3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-235215a98d56e0fd20b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ae2e1b3a3ce5a1bd8c1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62423f2be4f427a78df4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13b5b69a9bda9bfa1611">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db564ec9d9b674f0848c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b21925af80c575f27e0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4bcdd3da0d3129d6f10a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-279e64c78a1e7f40c275">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-898b2aa9aee474793b24">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c494d715ca7fb855e65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19fae97138d7508a3731">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-747b596fdda670db45e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-855651eb3196c7ce9cff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3ef1ef39bec900281d8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24e0bea0bf42bc8c6770">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-533335f6e5a209cdb8ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-634590f979b8c01b78cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cec347b9d84c62a36adc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f2ce513c1beb7fe871d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c7e3eb2d66083ec4576">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6136d3da756f9e7b27b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d13b84405c2fed7d824">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84fafd47dc9d60f5cf2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd15f8fe84444f4e89ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59cfcb83ae68ac92bb0f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aace97205c892b0d7032">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cde23e47a36aff9d187">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-215a2dea1bc0de2a223a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ae4f4d8886ee85a1cf7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c5adef55adbe5963d47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a93249b62b2a63e4c2af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18473eee6843c798c2da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f82316722a3a3c7b62d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10e37d7a173058c1f50b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e2e111e9c4b0478d2b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5fc4f36f3dd04a09be2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c60cee7a6a459bc812c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1183444fdca55f0af2e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b6fee113688072ab27a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db663f6c91745a501b8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-267e7f12e4a2a8eb20df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0213905529fcd0627eb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-308fc6f9606e07d9aced">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da1d88e5cad74a4617d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4188e374688fbfa9cd77">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-06a38ea4d75cba65810a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-150c7c6f3194a6f5cf2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-debd5bdfb798e2f498e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7778683ade4f9c12542c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a2f38d1b21656daa3d33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f174644103f2633363f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3114099821eff3d0d0eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de723d9beac8851d4e19">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9bd0bdee981512a61f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c56f4bbb5b25a58c5a1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42ce1da359f25efc6940">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95095b2881b45ddaeca2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b260161af2c8fbf2643f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-857c1e0e7e7cd8b80727">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61f624d0ae4612547113">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4377a115283702431677">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-571b31a32d0d3f4e6e2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cb35e06a1ae2fc524cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f93278d47f5e122d83b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-547b0998e7acf65fd74e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e267a451f71baccf4ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b920bf270eb906f0f201">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd60eb005fdab628f54f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17474c370c237ea43f9d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3302c191a7654a67a172">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8595ab671a9f13c0686f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea2d86d32b0f5aede44b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fc15288f468707d8ca8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f6237be0259a5a446848">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44b8ddcdc32ff13f71b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67ea2d3fa41104fb770f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de0c3f7b9ac37bfc09ab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4542d91f489ae308d931">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7be9e98c07d348a1744a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6542fc29c526fcc6d997">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b30244a5f6f8be43fabb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7fe1cfa4ea7f011ca90a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c8119ddfd7102cf2eb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dc48c0965be31610b7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9df24b668b590e5c0945">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-28ed65ceeb468afd9d9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9d57f47258018d4af99">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03e31e89eba32cc84090">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ecaba44c6b7ca34f8ac9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5eee66d58ed1ed8bf942">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9691e5031208a0111bd2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d24b3870eb00092a797f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed8bc8f7e0da072453d2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-28de511befd347828d95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27c4d7e75a193c04269d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43bdcb24012911816306">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c47f243dbcea5fb220b2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35463adfe4cd42ced474">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40d779cf762394af246b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42421fead8703d21db29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59eb50fd9f53e8030957">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eaf174f4ad5c63ad6614">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00c4a5f6dfbb5b3d1160">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e05c56c18c0a7363e3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf29f7617085c1e8c8e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-72de144bbe871b077aa0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ae609c952063eb0cd7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-486ce237fb6eb5d0dce4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e04a3654726ee6b2160d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d3d40960f50578459cf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfe08834ac72f086edd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65041b863fe03bef856a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be905d869fcf7c7aef08">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc01d6134b553d9750d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23ce62d4606f868b0269">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3210f492eac7ed69646c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fca1a253973d76ccf475">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-571e13a5772be9b79197">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1950b164e680e21ab16f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-279fc60ae252ed84c378">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dabca757950cb92b07b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-18745d9fa2ef2d74767c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a0c67da5fa5693cefcd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80a3d70893b570df8462">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cafa030eaceb1af7e817">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a93b0e26579e3f37b81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d5d0b7be37cca741125">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d05e4e667b4c702f704">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d182c27bffc1e37f0ead">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-decc19003377508b729b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-023b869240fe8d131b22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef8a4bada376f41d82da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4a250feb07e8d2875e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0d4f3ffbb8fb7a06737">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cc53c31739d5a33dc66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09d02693b593cbb23950">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aed8f0f4a483e49e7169">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a13acf0e811195ccf990">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d5ea78afb5691ce8042">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea1132828e6258561c2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff5c62372d4115333f41">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0a28989c64173b5d087">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82287d6a32245ca655ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-188e358360eb5f249e78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c2db84f500e0a35f131">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ebb02fe5ef69f1476573">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12afa61c6027a9db2e69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9c92fb3571df0aef45a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a31d9e988fe5fc89fb5">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-38642be6a74674a9d28e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-38642be6a74674a9d28e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e02e215b74c412f2e7b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e02e215b74c412f2e7b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1907fc26a51e6a34c322"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1907fc26a51e6a34c322`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d599f829349c87d6ac1c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d599f829349c87d6ac1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d54812ae3724d393a8f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d54812ae3724d393a8f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28447e0ea73ee37908a7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-28447e0ea73ee37908a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c24ce12acf2884d44cb1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c24ce12acf2884d44cb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee530ff45bce40d48b5b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee530ff45bce40d48b5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca6608e2529b894b2159"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca6608e2529b894b2159`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a188150e2dfbccc485fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a188150e2dfbccc485fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c97188989c7027916556"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c97188989c7027916556`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b03dc50d2e87ec4ff303"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b03dc50d2e87ec4ff303`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c49b9335cf869804e822"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c49b9335cf869804e822`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48ba381f44d5cd3e75c2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48ba381f44d5cd3e75c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff358fb99048545f2ff1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ff358fb99048545f2ff1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49ff9e17c5e956216992"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-49ff9e17c5e956216992`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7599b2fccc8ce85dd30f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7599b2fccc8ce85dd30f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa3b5d70b4a15f6aef01"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa3b5d70b4a15f6aef01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-149588bd4ce6a74c6fc6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-149588bd4ce6a74c6fc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f56039055df428602d4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5f56039055df428602d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d3a74f3b26ea41efeb5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d3a74f3b26ea41efeb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-292de8270aa589135d3f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-292de8270aa589135d3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e07ccfca3b8c328e3d5c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e07ccfca3b8c328e3d5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b619fa0fca66a1fb44d8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b619fa0fca66a1fb44d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-af5c33e675feceb14ff1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-af5c33e675feceb14ff1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8e1648738295b29e47a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d8e1648738295b29e47a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31e0eb6348d199b8b2ca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-31e0eb6348d199b8b2ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f723714ac316764fd5f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8f723714ac316764fd5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c55e423a24584397681d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c55e423a24584397681d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ee3cdb0a4d3c8db561e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6ee3cdb0a4d3c8db561e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47c61c97e07f0174a979"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-47c61c97e07f0174a979`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64ce4e9222d7a62684a5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64ce4e9222d7a62684a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-88d09aafd0a1366e0647"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-88d09aafd0a1366e0647`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a39eb08086c74715c309"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a39eb08086c74715c309`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8d8ea3bc5e0688cc9cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f8d8ea3bc5e0688cc9cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e023f77efa93ab779b40"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e023f77efa93ab779b40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa2d8d627bd1ba36ad8f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa2d8d627bd1ba36ad8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9816fd1911324d9df2b5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9816fd1911324d9df2b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7da69dc6684997478db8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7da69dc6684997478db8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70411e55bef709f1ce00"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-70411e55bef709f1ce00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee120a1f690cc44b1da5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee120a1f690cc44b1da5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48c86eb4d67793a26564"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48c86eb4d67793a26564`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d44d6062ed1153131e3c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d44d6062ed1153131e3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-235215a98d56e0fd20b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-235215a98d56e0fd20b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ae2e1b3a3ce5a1bd8c1d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ae2e1b3a3ce5a1bd8c1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62423f2be4f427a78df4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62423f2be4f427a78df4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13b5b69a9bda9bfa1611"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-13b5b69a9bda9bfa1611`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db564ec9d9b674f0848c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db564ec9d9b674f0848c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b21925af80c575f27e0d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b21925af80c575f27e0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4bcdd3da0d3129d6f10a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4bcdd3da0d3129d6f10a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-279e64c78a1e7f40c275"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-279e64c78a1e7f40c275`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-898b2aa9aee474793b24"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-898b2aa9aee474793b24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c494d715ca7fb855e65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c494d715ca7fb855e65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19fae97138d7508a3731"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-19fae97138d7508a3731`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-747b596fdda670db45e4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-747b596fdda670db45e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-855651eb3196c7ce9cff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-855651eb3196c7ce9cff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3ef1ef39bec900281d8a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3ef1ef39bec900281d8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24e0bea0bf42bc8c6770"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24e0bea0bf42bc8c6770`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-533335f6e5a209cdb8ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-533335f6e5a209cdb8ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-634590f979b8c01b78cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-634590f979b8c01b78cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cec347b9d84c62a36adc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cec347b9d84c62a36adc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f2ce513c1beb7fe871d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2f2ce513c1beb7fe871d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c7e3eb2d66083ec4576"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c7e3eb2d66083ec4576`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6136d3da756f9e7b27b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6136d3da756f9e7b27b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d13b84405c2fed7d824"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d13b84405c2fed7d824`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84fafd47dc9d60f5cf2a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-84fafd47dc9d60f5cf2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd15f8fe84444f4e89ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd15f8fe84444f4e89ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59cfcb83ae68ac92bb0f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-59cfcb83ae68ac92bb0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aace97205c892b0d7032"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aace97205c892b0d7032`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cde23e47a36aff9d187"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1cde23e47a36aff9d187`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-215a2dea1bc0de2a223a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-215a2dea1bc0de2a223a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ae4f4d8886ee85a1cf7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ae4f4d8886ee85a1cf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c5adef55adbe5963d47"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c5adef55adbe5963d47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a93249b62b2a63e4c2af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a93249b62b2a63e4c2af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18473eee6843c798c2da"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-18473eee6843c798c2da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f82316722a3a3c7b62d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f82316722a3a3c7b62d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10e37d7a173058c1f50b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10e37d7a173058c1f50b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e2e111e9c4b0478d2b2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1e2e111e9c4b0478d2b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5fc4f36f3dd04a09be2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5fc4f36f3dd04a09be2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c60cee7a6a459bc812c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c60cee7a6a459bc812c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1183444fdca55f0af2e5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1183444fdca55f0af2e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b6fee113688072ab27a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b6fee113688072ab27a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db663f6c91745a501b8a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-db663f6c91745a501b8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-267e7f12e4a2a8eb20df"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-267e7f12e4a2a8eb20df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0213905529fcd0627eb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0213905529fcd0627eb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-308fc6f9606e07d9aced"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-308fc6f9606e07d9aced`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da1d88e5cad74a4617d9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-da1d88e5cad74a4617d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4188e374688fbfa9cd77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4188e374688fbfa9cd77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-06a38ea4d75cba65810a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-06a38ea4d75cba65810a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-150c7c6f3194a6f5cf2d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-150c7c6f3194a6f5cf2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-debd5bdfb798e2f498e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-debd5bdfb798e2f498e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7778683ade4f9c12542c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7778683ade4f9c12542c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a2f38d1b21656daa3d33"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a2f38d1b21656daa3d33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f174644103f2633363f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f174644103f2633363f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3114099821eff3d0d0eb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3114099821eff3d0d0eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de723d9beac8851d4e19"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de723d9beac8851d4e19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9bd0bdee981512a61f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9bd0bdee981512a61f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c56f4bbb5b25a58c5a1d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c56f4bbb5b25a58c5a1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42ce1da359f25efc6940"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42ce1da359f25efc6940`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95095b2881b45ddaeca2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95095b2881b45ddaeca2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b260161af2c8fbf2643f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b260161af2c8fbf2643f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-857c1e0e7e7cd8b80727"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-857c1e0e7e7cd8b80727`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61f624d0ae4612547113"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-61f624d0ae4612547113`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4377a115283702431677"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4377a115283702431677`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-571b31a32d0d3f4e6e2f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-571b31a32d0d3f4e6e2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cb35e06a1ae2fc524cc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6cb35e06a1ae2fc524cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f93278d47f5e122d83b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f93278d47f5e122d83b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-547b0998e7acf65fd74e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-547b0998e7acf65fd74e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e267a451f71baccf4ab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e267a451f71baccf4ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b920bf270eb906f0f201"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b920bf270eb906f0f201`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd60eb005fdab628f54f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd60eb005fdab628f54f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17474c370c237ea43f9d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-17474c370c237ea43f9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3302c191a7654a67a172"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3302c191a7654a67a172`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8595ab671a9f13c0686f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8595ab671a9f13c0686f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea2d86d32b0f5aede44b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ea2d86d32b0f5aede44b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fc15288f468707d8ca8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4fc15288f468707d8ca8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f6237be0259a5a446848"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f6237be0259a5a446848`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44b8ddcdc32ff13f71b4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-44b8ddcdc32ff13f71b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67ea2d3fa41104fb770f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67ea2d3fa41104fb770f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de0c3f7b9ac37bfc09ab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de0c3f7b9ac37bfc09ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4542d91f489ae308d931"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4542d91f489ae308d931`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7be9e98c07d348a1744a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7be9e98c07d348a1744a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6542fc29c526fcc6d997"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6542fc29c526fcc6d997`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b30244a5f6f8be43fabb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b30244a5f6f8be43fabb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7fe1cfa4ea7f011ca90a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7fe1cfa4ea7f011ca90a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c8119ddfd7102cf2eb3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c8119ddfd7102cf2eb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dc48c0965be31610b7f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1dc48c0965be31610b7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9df24b668b590e5c0945"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9df24b668b590e5c0945`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-28ed65ceeb468afd9d9c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-28ed65ceeb468afd9d9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9d57f47258018d4af99"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c9d57f47258018d4af99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03e31e89eba32cc84090"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03e31e89eba32cc84090`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ecaba44c6b7ca34f8ac9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ecaba44c6b7ca34f8ac9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5eee66d58ed1ed8bf942"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5eee66d58ed1ed8bf942`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9691e5031208a0111bd2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9691e5031208a0111bd2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d24b3870eb00092a797f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d24b3870eb00092a797f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed8bc8f7e0da072453d2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed8bc8f7e0da072453d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-28de511befd347828d95"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-28de511befd347828d95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27c4d7e75a193c04269d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-27c4d7e75a193c04269d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43bdcb24012911816306"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-43bdcb24012911816306`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c47f243dbcea5fb220b2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c47f243dbcea5fb220b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35463adfe4cd42ced474"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35463adfe4cd42ced474`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40d779cf762394af246b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-40d779cf762394af246b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42421fead8703d21db29"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42421fead8703d21db29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59eb50fd9f53e8030957"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-59eb50fd9f53e8030957`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eaf174f4ad5c63ad6614"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eaf174f4ad5c63ad6614`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00c4a5f6dfbb5b3d1160"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00c4a5f6dfbb5b3d1160`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e05c56c18c0a7363e3e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e05c56c18c0a7363e3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf29f7617085c1e8c8e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cf29f7617085c1e8c8e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-72de144bbe871b077aa0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-72de144bbe871b077aa0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ae609c952063eb0cd7c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6ae609c952063eb0cd7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-486ce237fb6eb5d0dce4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-486ce237fb6eb5d0dce4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e04a3654726ee6b2160d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e04a3654726ee6b2160d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-N-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d3d40960f50578459cf9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d3d40960f50578459cf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfe08834ac72f086edd0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bfe08834ac72f086edd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65041b863fe03bef856a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65041b863fe03bef856a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be905d869fcf7c7aef08"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-be905d869fcf7c7aef08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc01d6134b553d9750d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc01d6134b553d9750d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23ce62d4606f868b0269"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23ce62d4606f868b0269`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3210f492eac7ed69646c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3210f492eac7ed69646c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fca1a253973d76ccf475"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fca1a253973d76ccf475`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-571e13a5772be9b79197"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-571e13a5772be9b79197`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1950b164e680e21ab16f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1950b164e680e21ab16f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-279fc60ae252ed84c378"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-279fc60ae252ed84c378`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dabca757950cb92b07b9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dabca757950cb92b07b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-18745d9fa2ef2d74767c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-18745d9fa2ef2d74767c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a0c67da5fa5693cefcd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5a0c67da5fa5693cefcd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80a3d70893b570df8462"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-80a3d70893b570df8462`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cafa030eaceb1af7e817"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cafa030eaceb1af7e817`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 1-S-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a93b0e26579e3f37b81"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a93b0e26579e3f37b81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d5d0b7be37cca741125"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d5d0b7be37cca741125`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d05e4e667b4c702f704"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9d05e4e667b4c702f704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d182c27bffc1e37f0ead"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d182c27bffc1e37f0ead`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-decc19003377508b729b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-decc19003377508b729b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-023b869240fe8d131b22"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-023b869240fe8d131b22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef8a4bada376f41d82da"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ef8a4bada376f41d82da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4a250feb07e8d2875e0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4a250feb07e8d2875e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0d4f3ffbb8fb7a06737"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0d4f3ffbb8fb7a06737`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cc53c31739d5a33dc66"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9cc53c31739d5a33dc66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09d02693b593cbb23950"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-09d02693b593cbb23950`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aed8f0f4a483e49e7169"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aed8f0f4a483e49e7169`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a13acf0e811195ccf990"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a13acf0e811195ccf990`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d5ea78afb5691ce8042"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d5ea78afb5691ce8042`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea1132828e6258561c2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ea1132828e6258561c2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff5c62372d4115333f41"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ff5c62372d4115333f41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0a28989c64173b5d087"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0a28989c64173b5d087`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82287d6a32245ca655ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-82287d6a32245ca655ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-188e358360eb5f249e78"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-188e358360eb5f249e78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c2db84f500e0a35f131"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2c2db84f500e0a35f131`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ebb02fe5ef69f1476573"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ebb02fe5ef69f1476573`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12afa61c6027a9db2e69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-12afa61c6027a9db2e69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9c92fb3571df0aef45a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9c92fb3571df0aef45a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a31d9e988fe5fc89fb5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8a31d9e988fe5fc89fb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 1-S-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 64 cases; unverified: 64</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6396ba8f92dba1a6e741">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9ca72e7ac9aebafdc6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e27da894749cad88a2fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9707bd429c1e853899b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b32a95376a0fee894319">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf3540106555971cdcc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3cc676586b01ba6aefb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6329a0eb9034ea11fc9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8443deca56ef38b8cccd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89953c4b8130eb478d7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a38e82f35738c5858472">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69672a28fbda0a79c270">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9af3246dde23d7134dc2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e6398067f78fd897799">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04c8941dcbcec4cf4c3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b35da25fe60bc8009ab3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-884389e7207d1cd5f2d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c26625b6a8df01bab8fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8247811bb987589ac190">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abb19bf01501b5bb0889">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-6; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca60a969d1d75fffdfa9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cae68abaf61713a1426">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-848cab44bd958de16637">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52d75c481f5879f4475b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d10326ecebb2303e86b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd00c201a83c9a5b11e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a644d46ca5dd6fa4d27e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81eb1d796db5c737acce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-11; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0af6c112eeb0627e9de4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbad4707e5a88b590f57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e0577fd1289f4ce1a9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76f49c8379ceb5fb9ac8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c8965a5d9f8fc0bd284c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e679a1ef865f0705974">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6956a6014334ad8ff240">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c355d98db127897fece">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-12; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3892bb836a184adc865">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d4f902d3f00b6831746">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cdc86a0bfe5acf28573">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9daee3c4ca04ebb74171">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0b815c4da87ae0615b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2765134274c0cfc76ba9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-003531fc52ff9ee29dfd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-795679a206376fed9f39">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-13; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9f3f2ac1a3977a668b89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-671a3b232d17e580e637">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c90fa4e916104f1c7137">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8e816eff8d3b006d5bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3587f1b67ec337cfa597">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42ed9c3ff476e0704ba0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5b402179467f9686955">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac440610e7e971ca3055">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-14; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-450c7e45b4718dbe2c4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d49498a07945f0e84813">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e17005195a172907752d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82a5f4449a30db9fee0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cad27adfc5e7115f32f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0c6390c5f8cd98c38d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2bef2da9fa2a51f7d38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80106a9e2a3100ca9dda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-16; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c96b000914e3dc61ffe9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d43363c7490c219e1857">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14ba09a79b84ef1f7fb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-495a3bb15cf223c30411">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-884389e7207d1cd5f2d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-884389e7207d1cd5f2d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c26625b6a8df01bab8fc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c26625b6a8df01bab8fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8247811bb987589ac190"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8247811bb987589ac190`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abb19bf01501b5bb0889"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-abb19bf01501b5bb0889`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-6; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca60a969d1d75fffdfa9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca60a969d1d75fffdfa9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cae68abaf61713a1426"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8cae68abaf61713a1426`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-848cab44bd958de16637"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-848cab44bd958de16637`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52d75c481f5879f4475b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52d75c481f5879f4475b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-6; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d10326ecebb2303e86b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d10326ecebb2303e86b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd00c201a83c9a5b11e7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cd00c201a83c9a5b11e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a644d46ca5dd6fa4d27e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a644d46ca5dd6fa4d27e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81eb1d796db5c737acce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-81eb1d796db5c737acce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-11; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0af6c112eeb0627e9de4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0af6c112eeb0627e9de4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbad4707e5a88b590f57"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fbad4707e5a88b590f57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e0577fd1289f4ce1a9c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9e0577fd1289f4ce1a9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76f49c8379ceb5fb9ac8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-76f49c8379ceb5fb9ac8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-11; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c8965a5d9f8fc0bd284c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c8965a5d9f8fc0bd284c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e679a1ef865f0705974"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e679a1ef865f0705974`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6956a6014334ad8ff240"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6956a6014334ad8ff240`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c355d98db127897fece"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c355d98db127897fece`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-12; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3892bb836a184adc865"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3892bb836a184adc865`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d4f902d3f00b6831746"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d4f902d3f00b6831746`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cdc86a0bfe5acf28573"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6cdc86a0bfe5acf28573`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9daee3c4ca04ebb74171"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9daee3c4ca04ebb74171`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-12; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0b815c4da87ae0615b5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0b815c4da87ae0615b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2765134274c0cfc76ba9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2765134274c0cfc76ba9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-003531fc52ff9ee29dfd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-003531fc52ff9ee29dfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-795679a206376fed9f39"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-795679a206376fed9f39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-13; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9f3f2ac1a3977a668b89"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f3f2ac1a3977a668b89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-671a3b232d17e580e637"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-671a3b232d17e580e637`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c90fa4e916104f1c7137"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c90fa4e916104f1c7137`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8e816eff8d3b006d5bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8e816eff8d3b006d5bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-13; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3587f1b67ec337cfa597"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3587f1b67ec337cfa597`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42ed9c3ff476e0704ba0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-42ed9c3ff476e0704ba0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5b402179467f9686955"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a5b402179467f9686955`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac440610e7e971ca3055"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac440610e7e971ca3055`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-14; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-450c7e45b4718dbe2c4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-450c7e45b4718dbe2c4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d49498a07945f0e84813"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d49498a07945f0e84813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e17005195a172907752d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e17005195a172907752d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82a5f4449a30db9fee0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-82a5f4449a30db9fee0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-14; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cad27adfc5e7115f32f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cad27adfc5e7115f32f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0c6390c5f8cd98c38d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0c6390c5f8cd98c38d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2bef2da9fa2a51f7d38"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2bef2da9fa2a51f7d38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80106a9e2a3100ca9dda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-80106a9e2a3100ca9dda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-16; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c96b000914e3dc61ffe9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c96b000914e3dc61ffe9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d43363c7490c219e1857"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d43363c7490c219e1857`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14ba09a79b84ef1f7fb7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-14ba09a79b84ef1f7fb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-495a3bb15cf223c30411"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-495a3bb15cf223c30411`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-16; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 64 cases; unverified: 64</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c71082290e55ca77a51d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09861aae4c3bb190110a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7a38a1df6ec1649586f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-992242b2025798d563e1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ef156e0f530ad422d88b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df20e3efcff8692f880c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cc8f71d2512af59380f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e8b25ddcc4dafd3fea2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f191a25d81dcfd1b287c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-840beaa134df3c0bf5e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d0548e0a2a04852bed8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df337400477a90480f68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f93c1b87c8c0fd2bb938">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa8b23e2d0d8f99064f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7273c8a35a718a947017">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9198d9179063d121ba16">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad46d98b63be98d1f1e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4eb2c52acf297c2d66ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8791bff2d83e0c987a48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60a73ca0d8503a89ee99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-993d334d37009db4cfad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a602bda5da1684d86bbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5becd6a3a007ff8bb33c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d9dc8b26348dd7e939e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-24843881300d3b2304e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4597f5d144a99218e27c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cffc048899f1fd2694f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ac0250047cac73fc1d3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2b39632aa60755fa6e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4eb2a910774ce969c264">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2797eda998b20eaa4210">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac24dfd2389b0e88f655">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-df3b4de4e128523adb18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b95c2ec4e447325337b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c78e05364f3647061def">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bacbc5b1e9977f3eca71">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8a6414170c90be4a2295">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83f3e5cb7b8316408caf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5589de8f28e5a8c0848f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a4e840a9474d38dda3c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2dd744b0582d0731079">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffe3e4fe34c51e095bf0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9366e2fc82793d7cbf17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90b3130996353499a79f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2aa915dbe0cc7e9d3bd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26c3dbf048a91db8b075">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1fb504081d0722c74b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2cb386c26ee65d10c2d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-641fd5d983da5aeb660c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56b7e800ff763ee48a56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c9a0ff21e0450804eb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52dba3fbb765f19b1bf8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-69e55f4a77d8f056e4b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e9a2c11d764ae8de8af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76ffb436c9bb63e46f53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50813616cb028ce7738a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6eb45c8a85d580d8e4f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7fe96403f6c5941b5e34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a79cf86b67baf5254701">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af2655a7632515aa9a50">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d2ce2ab259185698224">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2106fe782077ba2a3a47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12916902a7a9a8077021">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be1cc51bbb6116295cb3">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad46d98b63be98d1f1e3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad46d98b63be98d1f1e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4eb2c52acf297c2d66ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4eb2c52acf297c2d66ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8791bff2d83e0c987a48"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8791bff2d83e0c987a48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60a73ca0d8503a89ee99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-60a73ca0d8503a89ee99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-993d334d37009db4cfad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-993d334d37009db4cfad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a602bda5da1684d86bbf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a602bda5da1684d86bbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5becd6a3a007ff8bb33c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5becd6a3a007ff8bb33c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d9dc8b26348dd7e939e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d9dc8b26348dd7e939e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-24843881300d3b2304e5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-24843881300d3b2304e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4597f5d144a99218e27c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4597f5d144a99218e27c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cffc048899f1fd2694f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1cffc048899f1fd2694f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ac0250047cac73fc1d3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8ac0250047cac73fc1d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2b39632aa60755fa6e3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2b39632aa60755fa6e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4eb2a910774ce969c264"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4eb2a910774ce969c264`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2797eda998b20eaa4210"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2797eda998b20eaa4210`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac24dfd2389b0e88f655"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac24dfd2389b0e88f655`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-641fd5d983da5aeb660c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-641fd5d983da5aeb660c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56b7e800ff763ee48a56"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-56b7e800ff763ee48a56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c9a0ff21e0450804eb7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7c9a0ff21e0450804eb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52dba3fbb765f19b1bf8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52dba3fbb765f19b1bf8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-69e55f4a77d8f056e4b5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-69e55f4a77d8f056e4b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e9a2c11d764ae8de8af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e9a2c11d764ae8de8af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76ffb436c9bb63e46f53"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-76ffb436c9bb63e46f53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50813616cb028ce7738a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-50813616cb028ce7738a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6eb45c8a85d580d8e4f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6eb45c8a85d580d8e4f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7fe96403f6c5941b5e34"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7fe96403f6c5941b5e34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a79cf86b67baf5254701"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a79cf86b67baf5254701`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af2655a7632515aa9a50"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af2655a7632515aa9a50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d2ce2ab259185698224"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d2ce2ab259185698224`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2106fe782077ba2a3a47"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2106fe782077ba2a3a47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12916902a7a9a8077021"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-12916902a7a9a8077021`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be1cc51bbb6116295cb3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-be1cc51bbb6116295cb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-northwest-junction:canonical-southeast | <a href="#case-preview_review-dc931912ba40eb1296fc">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-northwest-junction:canonical-top | <a href="#case-preview_review-dca9a6ac16d9e1df4047">[ ] unverified</a> | — | — | — | — |


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

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
