---
title: "Testing: Avenue \u2014 Southeast Avenue Right-Turn Terminal \u2014 Parallel DD RHW \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW — Alignment B**, permanent ID `ddrhw-parallel-b-southeast-terminal`, as **P03** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 2 cells inside its 2 × 2 bounding footprint. Ground Avenue and right-turn pavement at 0 m. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -16.970563, 0.489958]; [0.7071067811865476, 0.7071067811865476]; -0.282029322 | `path-interface-de2471bc41cdce8bf875` |
| `channel-02-in` | road / 1 / primary | in | [-3.2, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-03-in` | road / 1 / primary | in | [3.2, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-06-out` | road / 1 / primary | out | [8.0, -19.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-07-out` | road / 1 / primary | out | [8.0, -12.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-08-out` | road / 1 / primary | out | [8.0, -3.2, 0.0]; [-0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-09-out` | road / 1 / primary | out | [8.0, 3.2, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-04-in` | road / 1 / primary | in | [12.8, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-10-out` | road / 1 / primary | out | [16.970563, 8.0, 0.489958]; [0.7071067811865732, 0.7071067811865218]; 0.282029322 | `path-interface-0c5a35d75bc5b6dfb609` |
| `channel-05-in` | road / 1 / primary | in | [19.2, -8.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-11-in` | pedestrian / 2 / primary | in | [-7.3, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `channel-13-out` | pedestrian / 2 / primary | out | [8.0, -23.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-14-out` | pedestrian / 2 / primary | out | [8.0, 7.3, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-12-in` | pedestrian / 2 / primary | in | [23.3, -8.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-06-out` | primary |
| road | `channel-02-in` → `channel-06-out` | primary |
| road | `channel-03-in` → `channel-07-out` | primary |
| road | `channel-04-in` → `channel-08-out` | primary |
| road | `channel-05-in` → `channel-10-out` | primary |
| road | `channel-05-in` → `channel-09-out` | primary |
| pedestrian | `channel-11-in` → `channel-13-out` | primary |
| pedestrian | `channel-12-in` → `channel-14-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component owns 2 adaptive Avenue cells. Native ground textures can change with surrounding development, while rotating model props retain this component's non-ground geometry. Its temporary Road helper is local **[1,1]** and is not permanent ownership. Keep the helper plot clear for placement, then connect the ordinary native Avenue centre at assembly **X6, Y4**. That centre is not one of this piece's two custom cells; all six native incident car and pedestrian members require a complete match. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-southeast-terminal
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **10,772 indexed triangles** and **8 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-southeast-terminal/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-southeast-terminal/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-386171de80eb568ccc2c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-386171de80eb568ccc2c"></a>

**General: unverified** — `software_resources-386171de80eb568ccc2c`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-386171de80eb568ccc2c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-386171de80eb568ccc2c"></a>

**General: unverified** — `software_connectivity-386171de80eb568ccc2c`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-1342999c395a7317a27e">[ ] unverified</a> | <a href="#case-in_game_render-2b2644bf8a13d75c104f">[ ] unverified</a> | <a href="#case-in_game_render-7115dd140007229fb165">[ ] unverified</a> | <a href="#case-in_game_render-20207775d9296905ea45">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-1342999c395a7317a27e"></a>

**0° CCW: unverified** — `in_game_render-1342999c395a7317a27e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2b2644bf8a13d75c104f"></a>

**90° CCW: unverified** — `in_game_render-2b2644bf8a13d75c104f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7115dd140007229fb165"></a>

**180° CCW: unverified** — `in_game_render-7115dd140007229fb165`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-20207775d9296905ea45"></a>

**270° CCW: unverified** — `in_game_render-20207775d9296905ea45`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-1342999c395a7317a27e">[ ] unverified</a> | <a href="#case-in_game_placement-2b2644bf8a13d75c104f">[ ] unverified</a> | <a href="#case-in_game_placement-7115dd140007229fb165">[ ] unverified</a> | <a href="#case-in_game_placement-20207775d9296905ea45">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-1342999c395a7317a27e"></a>

**0° CCW: unverified** — `in_game_placement-1342999c395a7317a27e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2b2644bf8a13d75c104f"></a>

**90° CCW: unverified** — `in_game_placement-2b2644bf8a13d75c104f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7115dd140007229fb165"></a>

**180° CCW: unverified** — `in_game_placement-7115dd140007229fb165`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-20207775d9296905ea45"></a>

**270° CCW: unverified** — `in_game_placement-20207775d9296905ea45`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-1342999c395a7317a27e">[ ] unverified</a> | <a href="#case-in_game_demolition-2b2644bf8a13d75c104f">[ ] unverified</a> | <a href="#case-in_game_demolition-7115dd140007229fb165">[ ] unverified</a> | <a href="#case-in_game_demolition-20207775d9296905ea45">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-1342999c395a7317a27e"></a>

**0° CCW: unverified** — `in_game_demolition-1342999c395a7317a27e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2b2644bf8a13d75c104f"></a>

**90° CCW: unverified** — `in_game_demolition-2b2644bf8a13d75c104f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7115dd140007229fb165"></a>

**180° CCW: unverified** — `in_game_demolition-7115dd140007229fb165`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-20207775d9296905ea45"></a>

**270° CCW: unverified** — `in_game_demolition-20207775d9296905ea45`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-1342999c395a7317a27e">[ ] unverified</a> | <a href="#case-in_game_save_reload-2b2644bf8a13d75c104f">[ ] unverified</a> | <a href="#case-in_game_save_reload-7115dd140007229fb165">[ ] unverified</a> | <a href="#case-in_game_save_reload-20207775d9296905ea45">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-1342999c395a7317a27e"></a>

**0° CCW: unverified** — `in_game_save_reload-1342999c395a7317a27e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2b2644bf8a13d75c104f"></a>

**90° CCW: unverified** — `in_game_save_reload-2b2644bf8a13d75c104f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7115dd140007229fb165"></a>

**180° CCW: unverified** — `in_game_save_reload-7115dd140007229fb165`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-20207775d9296905ea45"></a>

**270° CCW: unverified** — `in_game_save_reload-20207775d9296905ea45`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-01c1ecf582f2703ccc7c">[ ] unverified</a> | <a href="#case-in_game_route_query-8853c02967547150ff81">[ ] unverified</a> | <a href="#case-in_game_route_query-c4cc83d24f07b90eda0e">[ ] unverified</a> | <a href="#case-in_game_route_query-366a69071ce942adb669">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-7021e7e4885cd7bd076e">[ ] unverified</a> | <a href="#case-in_game_route_query-60d4c5be26c1fe1f0a01">[ ] unverified</a> | <a href="#case-in_game_route_query-e70fac0bd73c73741b1a">[ ] unverified</a> | <a href="#case-in_game_route_query-4759f5bbd69578b96d66">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-74f358cb941f0243a1eb">[ ] unverified</a> | <a href="#case-in_game_route_query-12a488f402982d2b0fec">[ ] unverified</a> | <a href="#case-in_game_route_query-c3fdfcd9e39c2b940a00">[ ] unverified</a> | <a href="#case-in_game_route_query-79e3772e433b931c295c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-a515410a0225945ee779">[ ] unverified</a> | <a href="#case-in_game_route_query-4e75313d34e97bbb6b25">[ ] unverified</a> | <a href="#case-in_game_route_query-cd87a6ce7f63fbe2f92b">[ ] unverified</a> | <a href="#case-in_game_route_query-8e461b44c8dcaa4b2e0f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-140a611da1f747106525">[ ] unverified</a> | <a href="#case-in_game_route_query-3d3f7489b21495b809e0">[ ] unverified</a> | <a href="#case-in_game_route_query-ba1496ece6d8f625461f">[ ] unverified</a> | <a href="#case-in_game_route_query-a6246562dfe94bea77bb">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-ea087424863a7f0b61ca">[ ] unverified</a> | <a href="#case-in_game_route_query-8e97ea9a19818108fc46">[ ] unverified</a> | <a href="#case-in_game_route_query-57c178597fd63a03ffe3">[ ] unverified</a> | <a href="#case-in_game_route_query-7ddf5cb5bdc006ec0379">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-01c1ecf582f2703ccc7c"></a>

**0° CCW: unverified** — `in_game_route_query-01c1ecf582f2703ccc7c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-8853c02967547150ff81"></a>

**90° CCW: unverified** — `in_game_route_query-8853c02967547150ff81`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-c4cc83d24f07b90eda0e"></a>

**180° CCW: unverified** — `in_game_route_query-c4cc83d24f07b90eda0e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-366a69071ce942adb669"></a>

**270° CCW: unverified** — `in_game_route_query-366a69071ce942adb669`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-7021e7e4885cd7bd076e"></a>

**0° CCW: unverified** — `in_game_route_query-7021e7e4885cd7bd076e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-60d4c5be26c1fe1f0a01"></a>

**90° CCW: unverified** — `in_game_route_query-60d4c5be26c1fe1f0a01`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-e70fac0bd73c73741b1a"></a>

**180° CCW: unverified** — `in_game_route_query-e70fac0bd73c73741b1a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-4759f5bbd69578b96d66"></a>

**270° CCW: unverified** — `in_game_route_query-4759f5bbd69578b96d66`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-74f358cb941f0243a1eb"></a>

**0° CCW: unverified** — `in_game_route_query-74f358cb941f0243a1eb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-12a488f402982d2b0fec"></a>

**90° CCW: unverified** — `in_game_route_query-12a488f402982d2b0fec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-c3fdfcd9e39c2b940a00"></a>

**180° CCW: unverified** — `in_game_route_query-c3fdfcd9e39c2b940a00`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-79e3772e433b931c295c"></a>

**270° CCW: unverified** — `in_game_route_query-79e3772e433b931c295c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-a515410a0225945ee779"></a>

**0° CCW: unverified** — `in_game_route_query-a515410a0225945ee779`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-4e75313d34e97bbb6b25"></a>

**90° CCW: unverified** — `in_game_route_query-4e75313d34e97bbb6b25`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-cd87a6ce7f63fbe2f92b"></a>

**180° CCW: unverified** — `in_game_route_query-cd87a6ce7f63fbe2f92b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-8e461b44c8dcaa4b2e0f"></a>

**270° CCW: unverified** — `in_game_route_query-8e461b44c8dcaa4b2e0f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-140a611da1f747106525"></a>

**0° CCW: unverified** — `in_game_route_query-140a611da1f747106525`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-3d3f7489b21495b809e0"></a>

**90° CCW: unverified** — `in_game_route_query-3d3f7489b21495b809e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-ba1496ece6d8f625461f"></a>

**180° CCW: unverified** — `in_game_route_query-ba1496ece6d8f625461f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-a6246562dfe94bea77bb"></a>

**270° CCW: unverified** — `in_game_route_query-a6246562dfe94bea77bb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-ea087424863a7f0b61ca"></a>

**0° CCW: unverified** — `in_game_route_query-ea087424863a7f0b61ca`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-8e97ea9a19818108fc46"></a>

**90° CCW: unverified** — `in_game_route_query-8e97ea9a19818108fc46`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-57c178597fd63a03ffe3"></a>

**180° CCW: unverified** — `in_game_route_query-57c178597fd63a03ffe3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-7ddf5cb5bdc006ec0379"></a>

**270° CCW: unverified** — `in_game_route_query-7ddf5cb5bdc006ec0379`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-01c1ecf582f2703ccc7c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8853c02967547150ff81">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c4cc83d24f07b90eda0e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-366a69071ce942adb669">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-7021e7e4885cd7bd076e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-60d4c5be26c1fe1f0a01">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e70fac0bd73c73741b1a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4759f5bbd69578b96d66">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-74f358cb941f0243a1eb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-12a488f402982d2b0fec">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c3fdfcd9e39c2b940a00">[ ] unverified</a> | <a href="#case-in_game_visible_travel-79e3772e433b931c295c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-a515410a0225945ee779">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4e75313d34e97bbb6b25">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cd87a6ce7f63fbe2f92b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8e461b44c8dcaa4b2e0f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-140a611da1f747106525">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3d3f7489b21495b809e0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ba1496ece6d8f625461f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a6246562dfe94bea77bb">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-ea087424863a7f0b61ca">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8e97ea9a19818108fc46">[ ] unverified</a> | <a href="#case-in_game_visible_travel-57c178597fd63a03ffe3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7ddf5cb5bdc006ec0379">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-01c1ecf582f2703ccc7c"></a>

**0° CCW: unverified** — `in_game_visible_travel-01c1ecf582f2703ccc7c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-8853c02967547150ff81"></a>

**90° CCW: unverified** — `in_game_visible_travel-8853c02967547150ff81`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-c4cc83d24f07b90eda0e"></a>

**180° CCW: unverified** — `in_game_visible_travel-c4cc83d24f07b90eda0e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-366a69071ce942adb669"></a>

**270° CCW: unverified** — `in_game_visible_travel-366a69071ce942adb669`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-06-out; entry: channel-01-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-7021e7e4885cd7bd076e"></a>

**0° CCW: unverified** — `in_game_visible_travel-7021e7e4885cd7bd076e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-60d4c5be26c1fe1f0a01"></a>

**90° CCW: unverified** — `in_game_visible_travel-60d4c5be26c1fe1f0a01`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-e70fac0bd73c73741b1a"></a>

**180° CCW: unverified** — `in_game_visible_travel-e70fac0bd73c73741b1a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-4759f5bbd69578b96d66"></a>

**270° CCW: unverified** — `in_game_visible_travel-4759f5bbd69578b96d66`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-74f358cb941f0243a1eb"></a>

**0° CCW: unverified** — `in_game_visible_travel-74f358cb941f0243a1eb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-12a488f402982d2b0fec"></a>

**90° CCW: unverified** — `in_game_visible_travel-12a488f402982d2b0fec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-c3fdfcd9e39c2b940a00"></a>

**180° CCW: unverified** — `in_game_visible_travel-c3fdfcd9e39c2b940a00`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-79e3772e433b931c295c"></a>

**270° CCW: unverified** — `in_game_visible_travel-79e3772e433b931c295c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-07-out; entry: channel-03-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-a515410a0225945ee779"></a>

**0° CCW: unverified** — `in_game_visible_travel-a515410a0225945ee779`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-4e75313d34e97bbb6b25"></a>

**90° CCW: unverified** — `in_game_visible_travel-4e75313d34e97bbb6b25`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-cd87a6ce7f63fbe2f92b"></a>

**180° CCW: unverified** — `in_game_visible_travel-cd87a6ce7f63fbe2f92b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-8e461b44c8dcaa4b2e0f"></a>

**270° CCW: unverified** — `in_game_visible_travel-8e461b44c8dcaa4b2e0f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-140a611da1f747106525"></a>

**0° CCW: unverified** — `in_game_visible_travel-140a611da1f747106525`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-3d3f7489b21495b809e0"></a>

**90° CCW: unverified** — `in_game_visible_travel-3d3f7489b21495b809e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-ba1496ece6d8f625461f"></a>

**180° CCW: unverified** — `in_game_visible_travel-ba1496ece6d8f625461f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-a6246562dfe94bea77bb"></a>

**270° CCW: unverified** — `in_game_visible_travel-a6246562dfe94bea77bb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-10-out; entry: channel-05-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-ea087424863a7f0b61ca"></a>

**0° CCW: unverified** — `in_game_visible_travel-ea087424863a7f0b61ca`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-8e97ea9a19818108fc46"></a>

**90° CCW: unverified** — `in_game_visible_travel-8e97ea9a19818108fc46`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-57c178597fd63a03ffe3"></a>

**180° CCW: unverified** — `in_game_visible_travel-57c178597fd63a03ffe3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-7ddf5cb5bdc006ec0379"></a>

**270° CCW: unverified** — `in_game_visible_travel-7ddf5cb5bdc006ec0379`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-25016f2e462296328c86">[ ] unverified</a> | <a href="#case-in_game_route_query-2ab7d44ba4a20f37937e">[ ] unverified</a> | <a href="#case-in_game_route_query-cfa6cd9d421db85b91e7">[ ] unverified</a> | <a href="#case-in_game_route_query-5179552df31853a24102">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-e8eef2a6ea6f938ed82d">[ ] unverified</a> | <a href="#case-in_game_route_query-685ce84377b77dafba6e">[ ] unverified</a> | <a href="#case-in_game_route_query-8329f45dadce41e10832">[ ] unverified</a> | <a href="#case-in_game_route_query-dd4f007d62ca42137f55">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-25016f2e462296328c86"></a>

**0° CCW: unverified** — `in_game_route_query-25016f2e462296328c86`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-2ab7d44ba4a20f37937e"></a>

**90° CCW: unverified** — `in_game_route_query-2ab7d44ba4a20f37937e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-cfa6cd9d421db85b91e7"></a>

**180° CCW: unverified** — `in_game_route_query-cfa6cd9d421db85b91e7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-5179552df31853a24102"></a>

**270° CCW: unverified** — `in_game_route_query-5179552df31853a24102`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-e8eef2a6ea6f938ed82d"></a>

**0° CCW: unverified** — `in_game_route_query-e8eef2a6ea6f938ed82d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-685ce84377b77dafba6e"></a>

**90° CCW: unverified** — `in_game_route_query-685ce84377b77dafba6e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-8329f45dadce41e10832"></a>

**180° CCW: unverified** — `in_game_route_query-8329f45dadce41e10832`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-dd4f007d62ca42137f55"></a>

**270° CCW: unverified** — `in_game_route_query-dd4f007d62ca42137f55`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-25016f2e462296328c86">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2ab7d44ba4a20f37937e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cfa6cd9d421db85b91e7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5179552df31853a24102">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-e8eef2a6ea6f938ed82d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-685ce84377b77dafba6e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8329f45dadce41e10832">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dd4f007d62ca42137f55">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-25016f2e462296328c86"></a>

**0° CCW: unverified** — `in_game_visible_travel-25016f2e462296328c86`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-2ab7d44ba4a20f37937e"></a>

**90° CCW: unverified** — `in_game_visible_travel-2ab7d44ba4a20f37937e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-cfa6cd9d421db85b91e7"></a>

**180° CCW: unverified** — `in_game_visible_travel-cfa6cd9d421db85b91e7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-5179552df31853a24102"></a>

**270° CCW: unverified** — `in_game_visible_travel-5179552df31853a24102`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-13-out; entry: channel-11-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-e8eef2a6ea6f938ed82d"></a>

**0° CCW: unverified** — `in_game_visible_travel-e8eef2a6ea6f938ed82d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-685ce84377b77dafba6e"></a>

**90° CCW: unverified** — `in_game_visible_travel-685ce84377b77dafba6e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-8329f45dadce41e10832"></a>

**180° CCW: unverified** — `in_game_visible_travel-8329f45dadce41e10832`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-dd4f007d62ca42137f55"></a>

**270° CCW: unverified** — `in_game_visible_travel-dd4f007d62ca42137f55`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-14-out; entry: channel-12-in; exit: channel-14-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 76 cases; unverified: 76</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0d67ff62cbcd7413587">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfe71bb5bdd03eb0ab47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39c50145892207eb4aac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-004b555de65634cc8eb0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c50ec9759b164be3cd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69998060bbf7181e2f34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88249dc6431334385fab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0db4bb294fa8a630ef9e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e30eb794c29e937e0e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f54babe99095e416973e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9b364d03a22bac56bb0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3bbd2b55dc7077d2f686">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-abf26401b39aa601cd00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25ae70eb373042ec6eda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14ff4784f930054fbff8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-157651d1731e76d7338d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5ee1eb01f7d567776fbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0e8f6e2791ecac6ac37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d3a189263c2eff7acc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1f094aed0e77d50af91">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bb1b9fa275493bb94aef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ae97a7f5177f0fb42c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15220223bc2027757384">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89cbf3147dc5f48318b2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cea55d8d766306a03c9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-003bd2540612054b4ff7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dba42f0847bea32f22b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05e85ecb38281bc3bda2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-030c4e37fe1dcef0263a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e521512703ed55cfcfa1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b9b98be9d99b6037943">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2714e662a7ef782d56c9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bc49529964c36936409">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c6edb7a51d1ca5de953">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d4763e4f81893386cc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2febc3f2092063182f8b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-daeff732f8b8b81de60e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa6a2864860a6a09c6ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a210127a67ae8d3e04c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-759f886b261e801e93eb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bcb3da1360c7d521d995">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc724539b65c2a4e6741">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8704d7b69f624152f10a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af90da1869f9f98657e6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e87f9b57b5afdc2f815">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9daa35b2a95dd00c4fae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d848f2b70b93c115eaf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1aecf995425b390d316">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9387868768ab124a2696">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7837c5819d1f5bce626d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbe18138d90883425591">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18570139c15f4ae0781c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bfd01c84c062b59fec39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc181529d880f37ee199">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d6737efe904765204f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03010fc153d4d7602031">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a588e8b2a11e837a9efa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96a94c11d788b4d061d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a11fa38ffa148b110a90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0295f79fdd5380987775">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3e0c54e6d11eecef4e54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3547ce5a6208d30d63a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0431b11780f43c7f7d56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78d917317bb2ecb5c9cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-70b770346daa51998d6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dbf75dcda69d1f41f2f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2c3a508f62f96806e84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-457a67d55551f7e5e99a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f33d8794509a75534f9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe6c5cfae590d8c8a3a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94fc3b4ef51426cba30c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d31f3bae14f2c7b21f02">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c4d9ebd161f0a83b19e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c1cf74a6c0f7628574c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9759d834fcd98c33b0bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c98d1f38cbea9e24a3d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0d67ff62cbcd7413587"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0d67ff62cbcd7413587`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfe71bb5bdd03eb0ab47"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cfe71bb5bdd03eb0ab47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39c50145892207eb4aac"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-39c50145892207eb4aac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-004b555de65634cc8eb0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-004b555de65634cc8eb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c50ec9759b164be3cd1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c50ec9759b164be3cd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69998060bbf7181e2f34"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-69998060bbf7181e2f34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88249dc6431334385fab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-88249dc6431334385fab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0db4bb294fa8a630ef9e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0db4bb294fa8a630ef9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e30eb794c29e937e0e1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e30eb794c29e937e0e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f54babe99095e416973e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f54babe99095e416973e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9b364d03a22bac56bb0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9b364d03a22bac56bb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3bbd2b55dc7077d2f686"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3bbd2b55dc7077d2f686`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-abf26401b39aa601cd00"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-abf26401b39aa601cd00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25ae70eb373042ec6eda"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25ae70eb373042ec6eda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14ff4784f930054fbff8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-14ff4784f930054fbff8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-157651d1731e76d7338d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-157651d1731e76d7338d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5ee1eb01f7d567776fbb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5ee1eb01f7d567776fbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0e8f6e2791ecac6ac37"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a0e8f6e2791ecac6ac37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d3a189263c2eff7acc0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d3a189263c2eff7acc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1f094aed0e77d50af91"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b1f094aed0e77d50af91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bb1b9fa275493bb94aef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bb1b9fa275493bb94aef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ae97a7f5177f0fb42c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ae97a7f5177f0fb42c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15220223bc2027757384"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-15220223bc2027757384`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89cbf3147dc5f48318b2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89cbf3147dc5f48318b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cea55d8d766306a03c9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cea55d8d766306a03c9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-003bd2540612054b4ff7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-003bd2540612054b4ff7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dba42f0847bea32f22b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9dba42f0847bea32f22b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05e85ecb38281bc3bda2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-05e85ecb38281bc3bda2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-030c4e37fe1dcef0263a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-030c4e37fe1dcef0263a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e521512703ed55cfcfa1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e521512703ed55cfcfa1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b9b98be9d99b6037943"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6b9b98be9d99b6037943`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2714e662a7ef782d56c9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2714e662a7ef782d56c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bc49529964c36936409"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bc49529964c36936409`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c6edb7a51d1ca5de953"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c6edb7a51d1ca5de953`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d4763e4f81893386cc4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0d4763e4f81893386cc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2febc3f2092063182f8b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2febc3f2092063182f8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-daeff732f8b8b81de60e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-daeff732f8b8b81de60e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa6a2864860a6a09c6ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa6a2864860a6a09c6ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a210127a67ae8d3e04c7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a210127a67ae8d3e04c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-759f886b261e801e93eb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-759f886b261e801e93eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bcb3da1360c7d521d995"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bcb3da1360c7d521d995`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc724539b65c2a4e6741"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dc724539b65c2a4e6741`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8704d7b69f624152f10a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8704d7b69f624152f10a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af90da1869f9f98657e6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af90da1869f9f98657e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e87f9b57b5afdc2f815"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e87f9b57b5afdc2f815`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9daa35b2a95dd00c4fae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9daa35b2a95dd00c4fae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d848f2b70b93c115eaf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d848f2b70b93c115eaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1aecf995425b390d316"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d1aecf995425b390d316`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9387868768ab124a2696"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9387868768ab124a2696`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7837c5819d1f5bce626d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7837c5819d1f5bce626d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbe18138d90883425591"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fbe18138d90883425591`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18570139c15f4ae0781c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-18570139c15f4ae0781c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bfd01c84c062b59fec39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bfd01c84c062b59fec39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc181529d880f37ee199"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fc181529d880f37ee199`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d6737efe904765204f7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d6737efe904765204f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03010fc153d4d7602031"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03010fc153d4d7602031`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a588e8b2a11e837a9efa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a588e8b2a11e837a9efa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96a94c11d788b4d061d0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-96a94c11d788b4d061d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a11fa38ffa148b110a90"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a11fa38ffa148b110a90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0295f79fdd5380987775"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0295f79fdd5380987775`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3e0c54e6d11eecef4e54"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e0c54e6d11eecef4e54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3547ce5a6208d30d63a1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3547ce5a6208d30d63a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0431b11780f43c7f7d56"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0431b11780f43c7f7d56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78d917317bb2ecb5c9cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-78d917317bb2ecb5c9cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-70b770346daa51998d6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-70b770346daa51998d6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dbf75dcda69d1f41f2f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dbf75dcda69d1f41f2f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2c3a508f62f96806e84"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a2c3a508f62f96806e84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-457a67d55551f7e5e99a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-457a67d55551f7e5e99a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f33d8794509a75534f9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f33d8794509a75534f9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe6c5cfae590d8c8a3a6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe6c5cfae590d8c8a3a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94fc3b4ef51426cba30c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94fc3b4ef51426cba30c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d31f3bae14f2c7b21f02"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d31f3bae14f2c7b21f02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c4d9ebd161f0a83b19e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c4d9ebd161f0a83b19e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c1cf74a6c0f7628574c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9c1cf74a6c0f7628574c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9759d834fcd98c33b0bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9759d834fcd98c33b0bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c98d1f38cbea9e24a3d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5c98d1f38cbea9e24a3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-75e51d9ef5706687f2dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80a60a5ccbc55e650627">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88fc0d5d0e8fcdefd8e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d08eb21ece4c78c45c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa4b2d5aa5ddeb722158">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b82a65a1ca9871247884">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aabfc769d4899ae3f778">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62ec62bdc5fc42d1752e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-af66965c04a76452c0c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-812e8be50eb59c25a996">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85eb1d9121474d11bd0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9ff376caae80161647b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fa8326391a46f47bdff4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a07e6bf57a2b4bbc14c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-238ee14fb7a80e36ba33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-445099b987b4bc45f2f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-705393fad4087211b3d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53be992da905a2c33e03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1cc97ad0b9cf1ca8a15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acbf470a7b85fa0c4512">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c8da558937682434ba5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3d1d2cbf86cca26e442">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acedfd9f0a462abb9cb6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39da720da6bbc1d09d6b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4b77a7846b5d33fe1af0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b35c6e05cae01d3d9eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-198268693373b9592705">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5386d24c4eae588cd74">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee082d8e9b5577ade6d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d2a68247390bd37d113">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68bab5f2e723c854cf77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a491d27ade9085a9cfac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e4cb3f08e2cb719e543">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a39e8fb5923c7cb3ca41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a2e0490d7a3903791b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b142d99350506c57e61">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-afd0e1bd0afd37b71cb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-076722ee75c86474c6a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8f7abc0f48cc239da3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3949904bc3bb7ed28103">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-75e51d9ef5706687f2dd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-75e51d9ef5706687f2dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80a60a5ccbc55e650627"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-80a60a5ccbc55e650627`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88fc0d5d0e8fcdefd8e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-88fc0d5d0e8fcdefd8e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d08eb21ece4c78c45c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6d08eb21ece4c78c45c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa4b2d5aa5ddeb722158"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa4b2d5aa5ddeb722158`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b82a65a1ca9871247884"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b82a65a1ca9871247884`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aabfc769d4899ae3f778"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aabfc769d4899ae3f778`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62ec62bdc5fc42d1752e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-62ec62bdc5fc42d1752e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-af66965c04a76452c0c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-af66965c04a76452c0c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-812e8be50eb59c25a996"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-812e8be50eb59c25a996`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85eb1d9121474d11bd0e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85eb1d9121474d11bd0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9ff376caae80161647b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c9ff376caae80161647b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fa8326391a46f47bdff4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa8326391a46f47bdff4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a07e6bf57a2b4bbc14c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a07e6bf57a2b4bbc14c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-238ee14fb7a80e36ba33"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-238ee14fb7a80e36ba33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-445099b987b4bc45f2f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-445099b987b4bc45f2f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-705393fad4087211b3d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-705393fad4087211b3d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53be992da905a2c33e03"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-53be992da905a2c33e03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1cc97ad0b9cf1ca8a15"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d1cc97ad0b9cf1ca8a15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acbf470a7b85fa0c4512"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acbf470a7b85fa0c4512`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c8da558937682434ba5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c8da558937682434ba5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3d1d2cbf86cca26e442"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e3d1d2cbf86cca26e442`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acedfd9f0a462abb9cb6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-acedfd9f0a462abb9cb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39da720da6bbc1d09d6b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39da720da6bbc1d09d6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4b77a7846b5d33fe1af0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4b77a7846b5d33fe1af0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b35c6e05cae01d3d9eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5b35c6e05cae01d3d9eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-198268693373b9592705"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-198268693373b9592705`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5386d24c4eae588cd74"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b5386d24c4eae588cd74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee082d8e9b5577ade6d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee082d8e9b5577ade6d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d2a68247390bd37d113"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9d2a68247390bd37d113`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68bab5f2e723c854cf77"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-68bab5f2e723c854cf77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a491d27ade9085a9cfac"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a491d27ade9085a9cfac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e4cb3f08e2cb719e543"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e4cb3f08e2cb719e543`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a39e8fb5923c7cb3ca41"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a39e8fb5923c7cb3ca41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a2e0490d7a3903791b9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4a2e0490d7a3903791b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b142d99350506c57e61"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b142d99350506c57e61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-afd0e1bd0afd37b71cb9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-afd0e1bd0afd37b71cb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-076722ee75c86474c6a5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-076722ee75c86474c6a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8f7abc0f48cc239da3b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8f7abc0f48cc239da3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3949904bc3bb7ed28103"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3949904bc3bb7ed28103`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6bdeeea5e5e179a3de5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1abd1325607f9412d6be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f5cabd81bb422ab834d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dffd50c9b5c3e42f1dbe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1943ffb88c87f0869664">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a5861396927a1401d3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1b02241f1b8e6d47987">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8cb0e4d49ca6e895aab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-26f3768c42af43b9f66c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f0e40fe1babc7fa33b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07a6411aa2bef0260326">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a28e8d29672a8cd50c00">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a8699a3e424914896d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e837141778222362e506">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd88d266029a57465dfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab4e24df3ff773e5fb1b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-74995d127454cabcc375">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa09ceaeb236e6402876">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d2cee4bd7370f0c1c60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ae52843bbb7cb8ebd4d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8f57ddf859dd2126b6c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68e1d070a2697e4cd432">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87d9b1ad3f45bf974627">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f891505e506ff24ef5d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc24a234567dd6474339">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c348a46d58a16fa777fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd88e296f5f62ecd7e5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e6ee5224bfff1401477">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-18e42e6ea11f92934b76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afb4d05516d4f477a0f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20767c974df146e8c5fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ace709db1ddf351954c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-74e38e1e3a9711b8a9c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d9740c7db6c28140b69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5dffd1d56386bb35916">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae5de85454e6e21f409a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7ff6d60d69b99c0ddf5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67b5ea26759def756655">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-483f18620f92c5595c48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f03cdcd7352c6d608c99">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6bdeeea5e5e179a3de5f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6bdeeea5e5e179a3de5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1abd1325607f9412d6be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1abd1325607f9412d6be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f5cabd81bb422ab834d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3f5cabd81bb422ab834d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dffd50c9b5c3e42f1dbe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dffd50c9b5c3e42f1dbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1943ffb88c87f0869664"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1943ffb88c87f0869664`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a5861396927a1401d3d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a5861396927a1401d3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1b02241f1b8e6d47987"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c1b02241f1b8e6d47987`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8cb0e4d49ca6e895aab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8cb0e4d49ca6e895aab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-26f3768c42af43b9f66c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-26f3768c42af43b9f66c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f0e40fe1babc7fa33b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f0e40fe1babc7fa33b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07a6411aa2bef0260326"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-07a6411aa2bef0260326`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a28e8d29672a8cd50c00"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a28e8d29672a8cd50c00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a8699a3e424914896d0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a8699a3e424914896d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e837141778222362e506"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e837141778222362e506`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd88d266029a57465dfe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dd88d266029a57465dfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab4e24df3ff773e5fb1b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab4e24df3ff773e5fb1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-74995d127454cabcc375"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-74995d127454cabcc375`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa09ceaeb236e6402876"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa09ceaeb236e6402876`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d2cee4bd7370f0c1c60"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d2cee4bd7370f0c1c60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ae52843bbb7cb8ebd4d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8ae52843bbb7cb8ebd4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8f57ddf859dd2126b6c6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f57ddf859dd2126b6c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68e1d070a2697e4cd432"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-68e1d070a2697e4cd432`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87d9b1ad3f45bf974627"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-87d9b1ad3f45bf974627`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f891505e506ff24ef5d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0f891505e506ff24ef5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc24a234567dd6474339"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc24a234567dd6474339`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c348a46d58a16fa777fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c348a46d58a16fa777fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd88e296f5f62ecd7e5d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd88e296f5f62ecd7e5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e6ee5224bfff1401477"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6e6ee5224bfff1401477`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-18e42e6ea11f92934b76"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-18e42e6ea11f92934b76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afb4d05516d4f477a0f3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-afb4d05516d4f477a0f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20767c974df146e8c5fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-20767c974df146e8c5fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ace709db1ddf351954c0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ace709db1ddf351954c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-74e38e1e3a9711b8a9c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-74e38e1e3a9711b8a9c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d9740c7db6c28140b69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d9740c7db6c28140b69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5dffd1d56386bb35916"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5dffd1d56386bb35916`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae5de85454e6e21f409a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ae5de85454e6e21f409a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7ff6d60d69b99c0ddf5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7ff6d60d69b99c0ddf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67b5ea26759def756655"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67b5ea26759def756655`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-483f18620f92c5595c48"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-483f18620f92c5595c48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f03cdcd7352c6d608c99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f03cdcd7352c6d608c99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a20742de450b43fe2cea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e61d77029cf2b477a7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b73ef6c24c7167a2f76b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bea84ef75b5754e2049b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a451e67dd9ea924b5524">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2efb8833f7e0630177d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20b9a36ed68da319e4f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a9b88c52b25cc256cc5">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a20742de450b43fe2cea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a20742de450b43fe2cea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e61d77029cf2b477a7f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e61d77029cf2b477a7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b73ef6c24c7167a2f76b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b73ef6c24c7167a2f76b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bea84ef75b5754e2049b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bea84ef75b5754e2049b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a451e67dd9ea924b5524"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a451e67dd9ea924b5524`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2efb8833f7e0630177d7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2efb8833f7e0630177d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20b9a36ed68da319e4f4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-20b9a36ed68da319e4f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a9b88c52b25cc256cc5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0a9b88c52b25cc256cc5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-southeast-terminal:canonical-southeast | <a href="#case-preview_review-3d5bc709e0539b06accd">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-southeast-terminal:canonical-top | <a href="#case-preview_review-b92af96938fe0656bab5">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-southeast-terminal:connection-overview | <a href="#case-preview_review-6ee1a132dd2c2ea8599d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-southeast-terminal:canonical-southeast</summary>

<a id="case-preview_review-3d5bc709e0539b06accd"></a>

**General: unverified** — `preview_review-3d5bc709e0539b06accd`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-southeast-terminal:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-southeast-terminal:canonical-top</summary>

<a id="case-preview_review-b92af96938fe0656bab5"></a>

**General: unverified** — `preview_review-b92af96938fe0656bab5`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-southeast-terminal:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-southeast-terminal:connection-overview</summary>

<a id="case-preview_review-6ee1a132dd2c2ea8599d"></a>

**General: unverified** — `preview_review-6ee1a132dd2c2ea8599d`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-southeast-terminal:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the terminal function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
