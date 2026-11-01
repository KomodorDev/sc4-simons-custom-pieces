---
title: "Testing: Avenue \u2014 Northwest Avenue Right-Turn Terminal \u2014 Parallel DD RHW \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW — Alignment B**, permanent ID `ddrhw-parallel-b-northwest-terminal`, as **P02** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 3 cells inside its 2 × 2 bounding footprint. Ground Avenue and right-turn pavement at 0 m. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-01-in` | road / 1 / primary | in | [-3.2, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-02-in` | road / 1 / primary | in | [3.2, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-06-out` | road / 1 / primary | out | [8.0, -3.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-07-out` | road / 1 / primary | out | [8.0, 3.2, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-08-out` | road / 1 / primary | out | [11.324846, -24.0, 0.0]; [0.18088053433206316, -0.983505074872391]; 0.0 | `path-interface-ab0dc819ba4c7fec9f5c` |
| `channel-09-out` | road / 1 / primary | out | [12.8, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-10-out` | road / 1 / primary | out | [19.2, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-03-in` | road / 1 / primary | in | [24.0, -19.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-04-in` | road / 1 / primary | in | [24.0, -12.8, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-05-in` | road / 1 / primary | in | [24.0, -11.324846, 0.0]; [-0.983505074872391, 0.18088053433206316]; 0.0 | `path-interface-eb8edd053c1b618ae382` |
| `channel-11-in` | pedestrian / 2 / primary | in | [-7.3, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `channel-13-out` | pedestrian / 2 / primary | out | [8.0, 7.3, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-14-out` | pedestrian / 2 / primary | out | [8.7, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `channel-12-in` | pedestrian / 2 / primary | in | [24.0, -8.7, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-08-out` | primary |
| road | `channel-01-in` → `channel-09-out` | primary |
| road | `channel-02-in` → `channel-10-out` | primary |
| road | `channel-03-in` → `channel-06-out` | primary |
| road | `channel-04-in` → `channel-07-out` | primary |
| road | `channel-05-in` → `channel-07-out` | primary |
| pedestrian | `channel-11-in` → `channel-14-out` | primary |
| pedestrian | `channel-12-in` → `channel-13-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component owns 3 adaptive Avenue cells. Native ground textures can change with surrounding development, while rotating model props retain this component's non-ground geometry. Its temporary Road helper is local **[0,0]** and is not permanent ownership. Place the crossing first, this terminal second, and the southeast terminal third in the first reference layout. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-northwest-terminal
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **8,122 indexed triangles** and **16 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

This type’s complete measured ports, movements, channel associations, and saved-chord witnesses are frozen in the [B accepted connector contract](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/checks/accepted-connector-contracts.jsonc). That source passed the independent saved-resource and whole-assembly checks before extraction; the generated views retain their own freshness requirements. Its precise saved grades and separately retained reviewed and sampled tangents follow the [shared precision convention](../../../../docs/CONNECTOR_METADATA.md#5-matching-procedure-and-evidence). Arbitrary-neighbour matching and game operation remain outside that record.

## 4. Game checks

1. Select this exact B type from its assembly cycle, place a fresh copy at the reference coordinate, and inspect its model, markings, barriers, and supports. Repeat proper construction rotations with Home or End; rotating the camera alone is insufficient.
2. Place the matching B neighbours from the assembly plan, connect the required native approaches, and let new traffic enter. Record Route Query separately from an actual car crossing each required join. Check both through decks wherever this type owns their fragments.
3. For ground Avenue ownership, separately inspect changing pavement appearance and moving pedestrians. A ramp driveway crosses its adjacent pedestrian route; road asphalt at that crossing is distinct from a missing sidewalk elsewhere.
4. At Medium and High shadow quality, inspect all camera views and zoom levels for unwanted custom shadows. The source's no-shadow policy is not an observed game result.
5. Save, quit, reload, and repeat representative joins. In a separate saved copy, demolish this component, inspect neighbouring native tiles and attachments, replace it, and retest.

Use the [shared observation procedure](../../../../docs/TESTING.md#4-record-one-observation), recording the exact candidate, component, orientation, neighbours, and environment. Native draggable joins, occupied-neighbour placement, visible traffic, redraw, demolition, and save/reload remain unverified without a matching human observation.

## 5. Results and known issues

This piece passed its saved-resource checks in the first native B build; its [assembly evidence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) records the exact candidate and placed-layout scope. Final connector exports and the assembly-menu package retain their own source fingerprints and checks. **Installation and all game observations remain unverified.** The assembly’s [TESTING document](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/TESTING.md) owns the complete layout’s evidence and limits.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-northwest-terminal/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-northwest-terminal/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-d1d54d9b686404070a61">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-d1d54d9b686404070a61"></a>

**General: unverified** — `software_resources-d1d54d9b686404070a61`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-d1d54d9b686404070a61">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-d1d54d9b686404070a61"></a>

**General: unverified** — `software_connectivity-d1d54d9b686404070a61`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-6a814a55c65a0dbf71c7">[ ] unverified</a> | <a href="#case-in_game_render-bb41b1baffec3b9c1ede">[ ] unverified</a> | <a href="#case-in_game_render-1cccd3e0f7c02bb7cbbf">[ ] unverified</a> | <a href="#case-in_game_render-1e3e455b69997d101e59">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-6a814a55c65a0dbf71c7"></a>

**0° CCW: unverified** — `in_game_render-6a814a55c65a0dbf71c7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-bb41b1baffec3b9c1ede"></a>

**90° CCW: unverified** — `in_game_render-bb41b1baffec3b9c1ede`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1cccd3e0f7c02bb7cbbf"></a>

**180° CCW: unverified** — `in_game_render-1cccd3e0f7c02bb7cbbf`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1e3e455b69997d101e59"></a>

**270° CCW: unverified** — `in_game_render-1e3e455b69997d101e59`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-6a814a55c65a0dbf71c7">[ ] unverified</a> | <a href="#case-in_game_placement-bb41b1baffec3b9c1ede">[ ] unverified</a> | <a href="#case-in_game_placement-1cccd3e0f7c02bb7cbbf">[ ] unverified</a> | <a href="#case-in_game_placement-1e3e455b69997d101e59">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-6a814a55c65a0dbf71c7"></a>

**0° CCW: unverified** — `in_game_placement-6a814a55c65a0dbf71c7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-bb41b1baffec3b9c1ede"></a>

**90° CCW: unverified** — `in_game_placement-bb41b1baffec3b9c1ede`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1cccd3e0f7c02bb7cbbf"></a>

**180° CCW: unverified** — `in_game_placement-1cccd3e0f7c02bb7cbbf`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1e3e455b69997d101e59"></a>

**270° CCW: unverified** — `in_game_placement-1e3e455b69997d101e59`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-6a814a55c65a0dbf71c7">[ ] unverified</a> | <a href="#case-in_game_demolition-bb41b1baffec3b9c1ede">[ ] unverified</a> | <a href="#case-in_game_demolition-1cccd3e0f7c02bb7cbbf">[ ] unverified</a> | <a href="#case-in_game_demolition-1e3e455b69997d101e59">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-6a814a55c65a0dbf71c7"></a>

**0° CCW: unverified** — `in_game_demolition-6a814a55c65a0dbf71c7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-bb41b1baffec3b9c1ede"></a>

**90° CCW: unverified** — `in_game_demolition-bb41b1baffec3b9c1ede`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1cccd3e0f7c02bb7cbbf"></a>

**180° CCW: unverified** — `in_game_demolition-1cccd3e0f7c02bb7cbbf`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1e3e455b69997d101e59"></a>

**270° CCW: unverified** — `in_game_demolition-1e3e455b69997d101e59`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-6a814a55c65a0dbf71c7">[ ] unverified</a> | <a href="#case-in_game_save_reload-bb41b1baffec3b9c1ede">[ ] unverified</a> | <a href="#case-in_game_save_reload-1cccd3e0f7c02bb7cbbf">[ ] unverified</a> | <a href="#case-in_game_save_reload-1e3e455b69997d101e59">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-6a814a55c65a0dbf71c7"></a>

**0° CCW: unverified** — `in_game_save_reload-6a814a55c65a0dbf71c7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-bb41b1baffec3b9c1ede"></a>

**90° CCW: unverified** — `in_game_save_reload-bb41b1baffec3b9c1ede`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1cccd3e0f7c02bb7cbbf"></a>

**180° CCW: unverified** — `in_game_save_reload-1cccd3e0f7c02bb7cbbf`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1e3e455b69997d101e59"></a>

**270° CCW: unverified** — `in_game_save_reload-1e3e455b69997d101e59`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-d461cf9834d1b33fc3cd">[ ] unverified</a> | <a href="#case-in_game_route_query-d74c2a849213080cbfef">[ ] unverified</a> | <a href="#case-in_game_route_query-5573dc8d79cf9f3b94d0">[ ] unverified</a> | <a href="#case-in_game_route_query-aa1042af8dff06721f01">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-d75c8762eb16a1183478">[ ] unverified</a> | <a href="#case-in_game_route_query-b07066ec0d0e8a757fee">[ ] unverified</a> | <a href="#case-in_game_route_query-4079c8c1f7e2153d6c69">[ ] unverified</a> | <a href="#case-in_game_route_query-70d9a65b72b4a6663149">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-e9f9727f357958e14d55">[ ] unverified</a> | <a href="#case-in_game_route_query-ee1879ba61998453d933">[ ] unverified</a> | <a href="#case-in_game_route_query-aa3a524b0554580672e9">[ ] unverified</a> | <a href="#case-in_game_route_query-7079786117218d43d15a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-1d8914e889763933b12d">[ ] unverified</a> | <a href="#case-in_game_route_query-b1e7fe67bb2c8f6098c4">[ ] unverified</a> | <a href="#case-in_game_route_query-fa5661dd4ff00f4d57e2">[ ] unverified</a> | <a href="#case-in_game_route_query-0095c09f8551d5536f5c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-ec4190a0cfad85dd389a">[ ] unverified</a> | <a href="#case-in_game_route_query-568bdc0c1e4b38fa88be">[ ] unverified</a> | <a href="#case-in_game_route_query-a620cd59acf4adf50ab3">[ ] unverified</a> | <a href="#case-in_game_route_query-f61457c710581b7917f3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-59c535c72530c5389b73">[ ] unverified</a> | <a href="#case-in_game_route_query-ca1ccfa54e9b2e1244eb">[ ] unverified</a> | <a href="#case-in_game_route_query-97bec618238643041b86">[ ] unverified</a> | <a href="#case-in_game_route_query-73a8e016fafd171a1fab">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-d461cf9834d1b33fc3cd"></a>

**0° CCW: unverified** — `in_game_route_query-d461cf9834d1b33fc3cd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-d74c2a849213080cbfef"></a>

**90° CCW: unverified** — `in_game_route_query-d74c2a849213080cbfef`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-5573dc8d79cf9f3b94d0"></a>

**180° CCW: unverified** — `in_game_route_query-5573dc8d79cf9f3b94d0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-aa1042af8dff06721f01"></a>

**270° CCW: unverified** — `in_game_route_query-aa1042af8dff06721f01`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-d75c8762eb16a1183478"></a>

**0° CCW: unverified** — `in_game_route_query-d75c8762eb16a1183478`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-b07066ec0d0e8a757fee"></a>

**90° CCW: unverified** — `in_game_route_query-b07066ec0d0e8a757fee`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-4079c8c1f7e2153d6c69"></a>

**180° CCW: unverified** — `in_game_route_query-4079c8c1f7e2153d6c69`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-70d9a65b72b4a6663149"></a>

**270° CCW: unverified** — `in_game_route_query-70d9a65b72b4a6663149`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-e9f9727f357958e14d55"></a>

**0° CCW: unverified** — `in_game_route_query-e9f9727f357958e14d55`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-ee1879ba61998453d933"></a>

**90° CCW: unverified** — `in_game_route_query-ee1879ba61998453d933`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-aa3a524b0554580672e9"></a>

**180° CCW: unverified** — `in_game_route_query-aa3a524b0554580672e9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-7079786117218d43d15a"></a>

**270° CCW: unverified** — `in_game_route_query-7079786117218d43d15a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-1d8914e889763933b12d"></a>

**0° CCW: unverified** — `in_game_route_query-1d8914e889763933b12d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-b1e7fe67bb2c8f6098c4"></a>

**90° CCW: unverified** — `in_game_route_query-b1e7fe67bb2c8f6098c4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-fa5661dd4ff00f4d57e2"></a>

**180° CCW: unverified** — `in_game_route_query-fa5661dd4ff00f4d57e2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-0095c09f8551d5536f5c"></a>

**270° CCW: unverified** — `in_game_route_query-0095c09f8551d5536f5c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-ec4190a0cfad85dd389a"></a>

**0° CCW: unverified** — `in_game_route_query-ec4190a0cfad85dd389a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-568bdc0c1e4b38fa88be"></a>

**90° CCW: unverified** — `in_game_route_query-568bdc0c1e4b38fa88be`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-a620cd59acf4adf50ab3"></a>

**180° CCW: unverified** — `in_game_route_query-a620cd59acf4adf50ab3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-f61457c710581b7917f3"></a>

**270° CCW: unverified** — `in_game_route_query-f61457c710581b7917f3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-59c535c72530c5389b73"></a>

**0° CCW: unverified** — `in_game_route_query-59c535c72530c5389b73`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-ca1ccfa54e9b2e1244eb"></a>

**90° CCW: unverified** — `in_game_route_query-ca1ccfa54e9b2e1244eb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-97bec618238643041b86"></a>

**180° CCW: unverified** — `in_game_route_query-97bec618238643041b86`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-73a8e016fafd171a1fab"></a>

**270° CCW: unverified** — `in_game_route_query-73a8e016fafd171a1fab`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-d461cf9834d1b33fc3cd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d74c2a849213080cbfef">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5573dc8d79cf9f3b94d0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aa1042af8dff06721f01">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-d75c8762eb16a1183478">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b07066ec0d0e8a757fee">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4079c8c1f7e2153d6c69">[ ] unverified</a> | <a href="#case-in_game_visible_travel-70d9a65b72b4a6663149">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-e9f9727f357958e14d55">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ee1879ba61998453d933">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aa3a524b0554580672e9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7079786117218d43d15a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-1d8914e889763933b12d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b1e7fe67bb2c8f6098c4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fa5661dd4ff00f4d57e2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0095c09f8551d5536f5c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-ec4190a0cfad85dd389a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-568bdc0c1e4b38fa88be">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a620cd59acf4adf50ab3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f61457c710581b7917f3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-59c535c72530c5389b73">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ca1ccfa54e9b2e1244eb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-97bec618238643041b86">[ ] unverified</a> | <a href="#case-in_game_visible_travel-73a8e016fafd171a1fab">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-d461cf9834d1b33fc3cd"></a>

**0° CCW: unverified** — `in_game_visible_travel-d461cf9834d1b33fc3cd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-d74c2a849213080cbfef"></a>

**90° CCW: unverified** — `in_game_visible_travel-d74c2a849213080cbfef`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-5573dc8d79cf9f3b94d0"></a>

**180° CCW: unverified** — `in_game_visible_travel-5573dc8d79cf9f3b94d0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-aa1042af8dff06721f01"></a>

**270° CCW: unverified** — `in_game_visible_travel-aa1042af8dff06721f01`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-08-out; entry: channel-01-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-d75c8762eb16a1183478"></a>

**0° CCW: unverified** — `in_game_visible_travel-d75c8762eb16a1183478`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-b07066ec0d0e8a757fee"></a>

**90° CCW: unverified** — `in_game_visible_travel-b07066ec0d0e8a757fee`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-4079c8c1f7e2153d6c69"></a>

**180° CCW: unverified** — `in_game_visible_travel-4079c8c1f7e2153d6c69`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-70d9a65b72b4a6663149"></a>

**270° CCW: unverified** — `in_game_visible_travel-70d9a65b72b4a6663149`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-e9f9727f357958e14d55"></a>

**0° CCW: unverified** — `in_game_visible_travel-e9f9727f357958e14d55`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-ee1879ba61998453d933"></a>

**90° CCW: unverified** — `in_game_visible_travel-ee1879ba61998453d933`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-aa3a524b0554580672e9"></a>

**180° CCW: unverified** — `in_game_visible_travel-aa3a524b0554580672e9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-7079786117218d43d15a"></a>

**270° CCW: unverified** — `in_game_visible_travel-7079786117218d43d15a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-1d8914e889763933b12d"></a>

**0° CCW: unverified** — `in_game_visible_travel-1d8914e889763933b12d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-b1e7fe67bb2c8f6098c4"></a>

**90° CCW: unverified** — `in_game_visible_travel-b1e7fe67bb2c8f6098c4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-fa5661dd4ff00f4d57e2"></a>

**180° CCW: unverified** — `in_game_visible_travel-fa5661dd4ff00f4d57e2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-0095c09f8551d5536f5c"></a>

**270° CCW: unverified** — `in_game_visible_travel-0095c09f8551d5536f5c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-ec4190a0cfad85dd389a"></a>

**0° CCW: unverified** — `in_game_visible_travel-ec4190a0cfad85dd389a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-568bdc0c1e4b38fa88be"></a>

**90° CCW: unverified** — `in_game_visible_travel-568bdc0c1e4b38fa88be`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-a620cd59acf4adf50ab3"></a>

**180° CCW: unverified** — `in_game_visible_travel-a620cd59acf4adf50ab3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-f61457c710581b7917f3"></a>

**270° CCW: unverified** — `in_game_visible_travel-f61457c710581b7917f3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-59c535c72530c5389b73"></a>

**0° CCW: unverified** — `in_game_visible_travel-59c535c72530c5389b73`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-ca1ccfa54e9b2e1244eb"></a>

**90° CCW: unverified** — `in_game_visible_travel-ca1ccfa54e9b2e1244eb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-97bec618238643041b86"></a>

**180° CCW: unverified** — `in_game_visible_travel-97bec618238643041b86`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-73a8e016fafd171a1fab"></a>

**270° CCW: unverified** — `in_game_visible_travel-73a8e016fafd171a1fab`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-0f386be2704f32416ef8">[ ] unverified</a> | <a href="#case-in_game_route_query-1a7477bc6612b8ffee7f">[ ] unverified</a> | <a href="#case-in_game_route_query-25ca15a07dfd95832c6f">[ ] unverified</a> | <a href="#case-in_game_route_query-9f2cdde5140f09619ac2">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-e070ecd2183609a7fc12">[ ] unverified</a> | <a href="#case-in_game_route_query-f1137d5cc98cee012b15">[ ] unverified</a> | <a href="#case-in_game_route_query-c2c741504ee31decb93d">[ ] unverified</a> | <a href="#case-in_game_route_query-1b8067c3a59398ea11b0">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-0f386be2704f32416ef8"></a>

**0° CCW: unverified** — `in_game_route_query-0f386be2704f32416ef8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-1a7477bc6612b8ffee7f"></a>

**90° CCW: unverified** — `in_game_route_query-1a7477bc6612b8ffee7f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-25ca15a07dfd95832c6f"></a>

**180° CCW: unverified** — `in_game_route_query-25ca15a07dfd95832c6f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-9f2cdde5140f09619ac2"></a>

**270° CCW: unverified** — `in_game_route_query-9f2cdde5140f09619ac2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-e070ecd2183609a7fc12"></a>

**0° CCW: unverified** — `in_game_route_query-e070ecd2183609a7fc12`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-f1137d5cc98cee012b15"></a>

**90° CCW: unverified** — `in_game_route_query-f1137d5cc98cee012b15`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-c2c741504ee31decb93d"></a>

**180° CCW: unverified** — `in_game_route_query-c2c741504ee31decb93d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-1b8067c3a59398ea11b0"></a>

**270° CCW: unverified** — `in_game_route_query-1b8067c3a59398ea11b0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-0f386be2704f32416ef8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1a7477bc6612b8ffee7f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-25ca15a07dfd95832c6f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9f2cdde5140f09619ac2">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-e070ecd2183609a7fc12">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f1137d5cc98cee012b15">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c2c741504ee31decb93d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1b8067c3a59398ea11b0">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-0f386be2704f32416ef8"></a>

**0° CCW: unverified** — `in_game_visible_travel-0f386be2704f32416ef8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-1a7477bc6612b8ffee7f"></a>

**90° CCW: unverified** — `in_game_visible_travel-1a7477bc6612b8ffee7f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-25ca15a07dfd95832c6f"></a>

**180° CCW: unverified** — `in_game_visible_travel-25ca15a07dfd95832c6f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-9f2cdde5140f09619ac2"></a>

**270° CCW: unverified** — `in_game_visible_travel-9f2cdde5140f09619ac2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-e070ecd2183609a7fc12"></a>

**0° CCW: unverified** — `in_game_visible_travel-e070ecd2183609a7fc12`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-f1137d5cc98cee012b15"></a>

**90° CCW: unverified** — `in_game_visible_travel-f1137d5cc98cee012b15`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-c2c741504ee31decb93d"></a>

**180° CCW: unverified** — `in_game_visible_travel-c2c741504ee31decb93d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-1b8067c3a59398ea11b0"></a>

**270° CCW: unverified** — `in_game_visible_travel-1b8067c3a59398ea11b0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 76 cases; unverified: 76</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bcaa416767c4750a934a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9fd7dcdb47596eb951f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d5dd47f0490947f1985">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22e35ffda115bcba6c73">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-648b08469aa2b3d918b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb974a1637fd1e67a101">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0b3e53835450083d151">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b50df76129c9116f727f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f78408f2e753deec3b71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e2870d2a28fc76bb8de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18e1951c7eee5990d436">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48383dff28df4d70a0bd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8a3a867775064b5a4b3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf7c5e1448110a5a4406">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf65e19093a5d12b2d4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7d06de5c5449226eb76">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d27a3aabe5453beedca8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b36c1adc3e2af4d531d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-692943e1b6062bd495e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-556bf40836c3b97f44d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-178860975f3197a81304">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e42303374c3a7784cfd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c9c056cc90631ff2ba4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eef7d62e677557e09355">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a3f0c734e079bd543a19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4defdbdff93e43d89f89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0251faf09589e6f1ce8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82ad7eaf3f0da0711ac8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-94aeac1b231261130655">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e97504ce1edba2de0b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9c2b0a5543c56744aca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45e0eba94a77769b3f56">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-44c6ffb1dc8295736657">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b51b4fb4241fb57683ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-345da9c1fb18edd8615e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f104a377b8bbb78ad63">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a2353a7fdcb5f5d441b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67c617ed909e9cb94264">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c24ea6b39182d9ccb758">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4573aa187f2788557d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12be828cbbbb4c660c27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de782503896df3833364">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d943a55b1c4a06956c73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aac1ca8cf90952c62bf9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8501bd85cde3e477cc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-041a8e99b8859a12090c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-608a0936a49bcfe9a935">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-655aa1551b7d1aeb769a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4906c4fe5bd855d75af4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a4849c83fa722f8a74c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d42aee156af7644c5491">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-520292f230e6e72aef46">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-72bc52a8fc23f9f008de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8fad7fc03875c5bcc30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfc4e9ca69ed74070c61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0b2ffce6075709dbec8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66348725ec698b8587b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-534fcdc62a0b4ede2432">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-375ff1329d02b741dd2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f9e5b803a2297adef8d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ae5e406283f2b3762234">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-903c63c08f17bca7d610">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b0a76b6ce93b281d822">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-397abc4b504d43f59628">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2d3905d2d69b21cb9d06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cde0ad3f17f19db6629">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c338f0fd2c37381bb294">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d863cd21968781aeee4d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8e131a560c70e7a80cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ca01bdec9230a0055d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28608d6391789e89664b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28264689712b6d9d6db7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-525d59308eed0ecd5d74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59ce3dc15efcaf66740d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84c20b5136e18bf695cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2932c41d147c52b99b86">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bcaa416767c4750a934a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bcaa416767c4750a934a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9fd7dcdb47596eb951f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9fd7dcdb47596eb951f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d5dd47f0490947f1985"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0d5dd47f0490947f1985`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22e35ffda115bcba6c73"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22e35ffda115bcba6c73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-648b08469aa2b3d918b5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-648b08469aa2b3d918b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb974a1637fd1e67a101"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bb974a1637fd1e67a101`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0b3e53835450083d151"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e0b3e53835450083d151`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b50df76129c9116f727f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b50df76129c9116f727f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f78408f2e753deec3b71"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f78408f2e753deec3b71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e2870d2a28fc76bb8de"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e2870d2a28fc76bb8de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18e1951c7eee5990d436"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-18e1951c7eee5990d436`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48383dff28df4d70a0bd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-48383dff28df4d70a0bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8a3a867775064b5a4b3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8a3a867775064b5a4b3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf7c5e1448110a5a4406"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf7c5e1448110a5a4406`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf65e19093a5d12b2d4e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bf65e19093a5d12b2d4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7d06de5c5449226eb76"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c7d06de5c5449226eb76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d27a3aabe5453beedca8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d27a3aabe5453beedca8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b36c1adc3e2af4d531d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b36c1adc3e2af4d531d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-692943e1b6062bd495e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-692943e1b6062bd495e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-556bf40836c3b97f44d8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-556bf40836c3b97f44d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-178860975f3197a81304"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-178860975f3197a81304`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e42303374c3a7784cfd0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e42303374c3a7784cfd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c9c056cc90631ff2ba4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c9c056cc90631ff2ba4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eef7d62e677557e09355"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eef7d62e677557e09355`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a3f0c734e079bd543a19"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a3f0c734e079bd543a19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4defdbdff93e43d89f89"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4defdbdff93e43d89f89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0251faf09589e6f1ce8e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0251faf09589e6f1ce8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82ad7eaf3f0da0711ac8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-82ad7eaf3f0da0711ac8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-94aeac1b231261130655"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-94aeac1b231261130655`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e97504ce1edba2de0b4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0e97504ce1edba2de0b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9c2b0a5543c56744aca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e9c2b0a5543c56744aca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45e0eba94a77769b3f56"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45e0eba94a77769b3f56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-44c6ffb1dc8295736657"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-44c6ffb1dc8295736657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b51b4fb4241fb57683ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b51b4fb4241fb57683ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-345da9c1fb18edd8615e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-345da9c1fb18edd8615e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f104a377b8bbb78ad63"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f104a377b8bbb78ad63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a2353a7fdcb5f5d441b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a2353a7fdcb5f5d441b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67c617ed909e9cb94264"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67c617ed909e9cb94264`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c24ea6b39182d9ccb758"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c24ea6b39182d9ccb758`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4573aa187f2788557d6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b4573aa187f2788557d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12be828cbbbb4c660c27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12be828cbbbb4c660c27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de782503896df3833364"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-de782503896df3833364`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d943a55b1c4a06956c73"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d943a55b1c4a06956c73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aac1ca8cf90952c62bf9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aac1ca8cf90952c62bf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8501bd85cde3e477cc9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8501bd85cde3e477cc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-041a8e99b8859a12090c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-041a8e99b8859a12090c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-608a0936a49bcfe9a935"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-608a0936a49bcfe9a935`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-655aa1551b7d1aeb769a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-655aa1551b7d1aeb769a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4906c4fe5bd855d75af4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4906c4fe5bd855d75af4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a4849c83fa722f8a74c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8a4849c83fa722f8a74c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d42aee156af7644c5491"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d42aee156af7644c5491`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-520292f230e6e72aef46"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-520292f230e6e72aef46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-72bc52a8fc23f9f008de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-72bc52a8fc23f9f008de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8fad7fc03875c5bcc30"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c8fad7fc03875c5bcc30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfc4e9ca69ed74070c61"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cfc4e9ca69ed74070c61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0b2ffce6075709dbec8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c0b2ffce6075709dbec8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-66348725ec698b8587b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66348725ec698b8587b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-534fcdc62a0b4ede2432"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-534fcdc62a0b4ede2432`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-375ff1329d02b741dd2e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-375ff1329d02b741dd2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f9e5b803a2297adef8d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7f9e5b803a2297adef8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ae5e406283f2b3762234"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ae5e406283f2b3762234`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-903c63c08f17bca7d610"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-903c63c08f17bca7d610`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b0a76b6ce93b281d822"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7b0a76b6ce93b281d822`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-397abc4b504d43f59628"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-397abc4b504d43f59628`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2d3905d2d69b21cb9d06"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d3905d2d69b21cb9d06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cde0ad3f17f19db6629"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2cde0ad3f17f19db6629`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c338f0fd2c37381bb294"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c338f0fd2c37381bb294`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d863cd21968781aeee4d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d863cd21968781aeee4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8e131a560c70e7a80cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8e131a560c70e7a80cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ca01bdec9230a0055d3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ca01bdec9230a0055d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28608d6391789e89664b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-28608d6391789e89664b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28264689712b6d9d6db7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-28264689712b6d9d6db7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-525d59308eed0ecd5d74"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-525d59308eed0ecd5d74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59ce3dc15efcaf66740d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-59ce3dc15efcaf66740d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84c20b5136e18bf695cc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-84c20b5136e18bf695cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2932c41d147c52b99b86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2932c41d147c52b99b86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f0e9923ebddcd0ebce9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-188942a42d84fbd387c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e2c3a9cf1a16f015f7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37d4df784bd50b4f64bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-80be77e474df83953e3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ebe35d301be4f1617b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06819d71f8d66bc3e878">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58a31d318e5e7dc3bf5e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-55a6f37cd7abed2be5f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f00abf10da160b8faf1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8029a2ee571b17338917">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f59b34abd5558c764af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7a245703f2a59c3d0722">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1348aa8f7fd38f443767">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb6ccd86bf90c077f454">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b90b0ddfb3481f0f8485">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-28a91235f4fb2bf4fc6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b11338da637fe484c23a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d402dda0f302cbe92b34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4446d888cef0a030c424">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8896d99f23fe2f054908">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e1f29dff1368c4c4731">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-072e9fefde163d7391ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c48fdbbd407a2a98e633">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2363bc0a3648a5055722">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1495b7a938de401a6aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d121102edaca535f0537">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6b18fffbe28298901b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-732c709f651a4faa0616">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4374eebccb06a31c70be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd59c4a2eafbe798d843">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af5198f363567835734d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-33aa7f9143763d27336c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d155d92bd3ca3317cb1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7e033465a09c4f71b20">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe3f02f49e777c8e0f86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-38bb223c10d1fc0fe2a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-867ff0147871b5d6d26a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbe70fb38445e56c5ad3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b8133f2bb0efa5fbd67">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f0e9923ebddcd0ebce9d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f0e9923ebddcd0ebce9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-188942a42d84fbd387c1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-188942a42d84fbd387c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e2c3a9cf1a16f015f7b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7e2c3a9cf1a16f015f7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37d4df784bd50b4f64bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-37d4df784bd50b4f64bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-80be77e474df83953e3e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-80be77e474df83953e3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ebe35d301be4f1617b3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ebe35d301be4f1617b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06819d71f8d66bc3e878"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-06819d71f8d66bc3e878`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58a31d318e5e7dc3bf5e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-58a31d318e5e7dc3bf5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-55a6f37cd7abed2be5f2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-55a6f37cd7abed2be5f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f00abf10da160b8faf1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8f00abf10da160b8faf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8029a2ee571b17338917"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8029a2ee571b17338917`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f59b34abd5558c764af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7f59b34abd5558c764af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7a245703f2a59c3d0722"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7a245703f2a59c3d0722`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1348aa8f7fd38f443767"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1348aa8f7fd38f443767`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb6ccd86bf90c077f454"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cb6ccd86bf90c077f454`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b90b0ddfb3481f0f8485"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b90b0ddfb3481f0f8485`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-28a91235f4fb2bf4fc6b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-28a91235f4fb2bf4fc6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b11338da637fe484c23a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b11338da637fe484c23a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d402dda0f302cbe92b34"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d402dda0f302cbe92b34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4446d888cef0a030c424"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4446d888cef0a030c424`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8896d99f23fe2f054908"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8896d99f23fe2f054908`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e1f29dff1368c4c4731"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0e1f29dff1368c4c4731`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-072e9fefde163d7391ed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-072e9fefde163d7391ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c48fdbbd407a2a98e633"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c48fdbbd407a2a98e633`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2363bc0a3648a5055722"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2363bc0a3648a5055722`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1495b7a938de401a6aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b1495b7a938de401a6aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d121102edaca535f0537"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d121102edaca535f0537`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6b18fffbe28298901b9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b6b18fffbe28298901b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-732c709f651a4faa0616"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-732c709f651a4faa0616`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4374eebccb06a31c70be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4374eebccb06a31c70be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd59c4a2eafbe798d843"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd59c4a2eafbe798d843`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af5198f363567835734d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af5198f363567835734d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-33aa7f9143763d27336c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-33aa7f9143763d27336c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d155d92bd3ca3317cb1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d155d92bd3ca3317cb1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7e033465a09c4f71b20"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f7e033465a09c4f71b20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe3f02f49e777c8e0f86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe3f02f49e777c8e0f86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-38bb223c10d1fc0fe2a3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-38bb223c10d1fc0fe2a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-867ff0147871b5d6d26a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-867ff0147871b5d6d26a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbe70fb38445e56c5ad3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bbe70fb38445e56c5ad3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b8133f2bb0efa5fbd67"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b8133f2bb0efa5fbd67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d99589a260fe07588ae0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-791cb1cd024c31d2355a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5f86f6bda6d11954efd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb9d51b582f0b458b877">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4d34c644765a504f706">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-342cefdea3f969d2d61c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e670bb10b3969935a1d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-732e51be5e9a954f7921">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cf71efabf9c08b8ef385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9b3a87911fd7fc34872">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c66ff9059519985b13f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3c7558f5da0272f8305">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a7591296d23ca3f34ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-818e4e261eb78a7ea21b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83cd1106af78dbbd14e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a03b27ca0c9b2b650c34">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-91e547563dff4a917057">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfa3427a2492cb2c1f69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6b20f2c85a1b24aa9d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afd5b842f055657cb8a2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fe0e595e7017497ff802">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa6a5a45a96694b96404">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-804ed18fcae8207c8298">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51e212526f00ec02d2b2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32df7371ae8effc5f6d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d66657628d4110e4ffe2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e89df37e30e654d8d89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fd5465506ad13319af0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be22a35d9b23c4d4c194">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d564a3fbe6ef77347299">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78e0ece4adc9c366300b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a14d5fdb68b908886e00">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aaa8b1e5c6f852453daa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e9e2800045ed2eb8cec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-964098238bde1a6f09ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a9f06021fafa11bc208">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8b5e74cfd63b64684925">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-850c188d34288298ca52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c4101ea0ae323b6729d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9049fd8a4b9fba4ec8cf">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d99589a260fe07588ae0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d99589a260fe07588ae0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-791cb1cd024c31d2355a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-791cb1cd024c31d2355a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5f86f6bda6d11954efd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5f86f6bda6d11954efd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb9d51b582f0b458b877"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb9d51b582f0b458b877`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4d34c644765a504f706"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4d34c644765a504f706`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-342cefdea3f969d2d61c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-342cefdea3f969d2d61c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e670bb10b3969935a1d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e670bb10b3969935a1d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-732e51be5e9a954f7921"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-732e51be5e9a954f7921`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cf71efabf9c08b8ef385"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cf71efabf9c08b8ef385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9b3a87911fd7fc34872"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e9b3a87911fd7fc34872`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c66ff9059519985b13f1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c66ff9059519985b13f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3c7558f5da0272f8305"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a3c7558f5da0272f8305`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a7591296d23ca3f34ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a7591296d23ca3f34ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-818e4e261eb78a7ea21b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-818e4e261eb78a7ea21b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83cd1106af78dbbd14e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-83cd1106af78dbbd14e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a03b27ca0c9b2b650c34"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a03b27ca0c9b2b650c34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-91e547563dff4a917057"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-91e547563dff4a917057`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfa3427a2492cb2c1f69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bfa3427a2492cb2c1f69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6b20f2c85a1b24aa9d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c6b20f2c85a1b24aa9d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afd5b842f055657cb8a2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afd5b842f055657cb8a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fe0e595e7017497ff802"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fe0e595e7017497ff802`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa6a5a45a96694b96404"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa6a5a45a96694b96404`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-804ed18fcae8207c8298"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-804ed18fcae8207c8298`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51e212526f00ec02d2b2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-51e212526f00ec02d2b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32df7371ae8effc5f6d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32df7371ae8effc5f6d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d66657628d4110e4ffe2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d66657628d4110e4ffe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e89df37e30e654d8d89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2e89df37e30e654d8d89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fd5465506ad13319af0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0fd5465506ad13319af0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be22a35d9b23c4d4c194"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be22a35d9b23c4d4c194`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d564a3fbe6ef77347299"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d564a3fbe6ef77347299`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78e0ece4adc9c366300b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78e0ece4adc9c366300b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a14d5fdb68b908886e00"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a14d5fdb68b908886e00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aaa8b1e5c6f852453daa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aaa8b1e5c6f852453daa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e9e2800045ed2eb8cec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e9e2800045ed2eb8cec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-964098238bde1a6f09ba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-964098238bde1a6f09ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a9f06021fafa11bc208"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a9f06021fafa11bc208`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8b5e74cfd63b64684925"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b5e74cfd63b64684925`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-850c188d34288298ca52"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-850c188d34288298ca52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c4101ea0ae323b6729d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c4101ea0ae323b6729d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9049fd8a4b9fba4ec8cf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9049fd8a4b9fba4ec8cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-edd25bf37cb67b0cea61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de00d1e630130c17a0ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a042638d502de42647b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5af52ae942ea745931a0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d92a6d887e3fd9e316df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce05dc0d2074d381cb6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9f0c2d8af4864f4b128">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bdd6b7c5121ced7008d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-edd25bf37cb67b0cea61"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-edd25bf37cb67b0cea61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de00d1e630130c17a0ed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-de00d1e630130c17a0ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a042638d502de42647b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a042638d502de42647b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5af52ae942ea745931a0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5af52ae942ea745931a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d92a6d887e3fd9e316df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d92a6d887e3fd9e316df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce05dc0d2074d381cb6e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce05dc0d2074d381cb6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9f0c2d8af4864f4b128"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9f0c2d8af4864f4b128`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bdd6b7c5121ced7008d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0bdd6b7c5121ced7008d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-northwest-terminal:canonical-southeast | <a href="#case-preview_review-f5a74572091fffdfa6ae">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-northwest-terminal:canonical-top | <a href="#case-preview_review-ec0faa52c744caf61c7c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-northwest-terminal:connection-overview | <a href="#case-preview_review-28e03addbf9c8f09df68">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-northwest-terminal:canonical-southeast</summary>

<a id="case-preview_review-f5a74572091fffdfa6ae"></a>

**General: unverified** — `preview_review-f5a74572091fffdfa6ae`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-northwest-terminal:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-northwest-terminal:canonical-top</summary>

<a id="case-preview_review-ec0faa52c744caf61c7c"></a>

**General: unverified** — `preview_review-ec0faa52c744caf61c7c`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-northwest-terminal:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-northwest-terminal:connection-overview</summary>

<a id="case-preview_review-28e03addbf9c8f09df68"></a>

**General: unverified** — `preview_review-28e03addbf9c8f09df68`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-northwest-terminal:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the terminal function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
