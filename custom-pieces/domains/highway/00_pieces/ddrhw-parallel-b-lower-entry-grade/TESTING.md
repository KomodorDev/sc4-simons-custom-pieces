---
title: "Testing: RHW Ramp \u2014 L1 Entry Parallel Grade \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L1 Entry Parallel Grade — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **RHW Ramp — L1 Entry Parallel Grade — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-lower-entry-grade`, as **P13** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 3 cells inside its 2 × 2 bounding footprint. Physical grade between 7.5 m and 0 m; actual cell-edge ports have their own measured intermediate heights. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-06-out` | road / 1 / primary | out | [-0.970563, -24.0, 6.390578]; [-0.7071067811865668, -0.7071067811865284]; 0.179116236 | `path-interface-758253be5f8ec9e11340` |
| `channel-07-out` | road / 1 / primary | out | [12.8, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [12.8, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-08-out` | road / 1 / primary | out | [19.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-02-in` | road / 1 / primary | in | [19.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-03-in` | road / 1 / primary | in | [24.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-09-out` | road / 1 / primary | out | [24.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-04-in` | road / 1 / primary | in | [24.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-10-out` | road / 1 / primary | out | [24.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-05-in` | road / 1 / primary | in | [24.0, 0.970563, 0.083612]; [-0.7071067811865515, -0.7071067811865436]; 0.115840807 | `path-interface-b5d8c749a9139d051e0c` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-10-out` | primary |
| road | `channel-02-in` → `channel-09-out` | primary |
| road | `channel-03-in` → `channel-08-out` | primary |
| road | `channel-04-in` → `channel-07-out` | primary |
| road | `channel-05-in` → `channel-06-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-lower-entry-grade
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **7,977 indexed triangles** and **7 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
- [ ] Route Query: 0/20 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/20 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 141, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-lower-entry-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-lower-entry-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-75b83547c768d45af3ff">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-75b83547c768d45af3ff"></a>

**General: unverified** — `software_resources-75b83547c768d45af3ff`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-75b83547c768d45af3ff">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-75b83547c768d45af3ff"></a>

**General: unverified** — `software_connectivity-75b83547c768d45af3ff`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-2f81982b55bf2ce2a1f4">[ ] unverified</a> | <a href="#case-in_game_render-b788302e082462acb716">[ ] unverified</a> | <a href="#case-in_game_render-e94c09bfd628cf3528e7">[ ] unverified</a> | <a href="#case-in_game_render-1a4001c8afdcb0eb7aa6">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-2f81982b55bf2ce2a1f4"></a>

**0° CCW: unverified** — `in_game_render-2f81982b55bf2ce2a1f4`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-b788302e082462acb716"></a>

**90° CCW: unverified** — `in_game_render-b788302e082462acb716`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e94c09bfd628cf3528e7"></a>

**180° CCW: unverified** — `in_game_render-e94c09bfd628cf3528e7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1a4001c8afdcb0eb7aa6"></a>

**270° CCW: unverified** — `in_game_render-1a4001c8afdcb0eb7aa6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-2f81982b55bf2ce2a1f4">[ ] unverified</a> | <a href="#case-in_game_placement-b788302e082462acb716">[ ] unverified</a> | <a href="#case-in_game_placement-e94c09bfd628cf3528e7">[ ] unverified</a> | <a href="#case-in_game_placement-1a4001c8afdcb0eb7aa6">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-2f81982b55bf2ce2a1f4"></a>

**0° CCW: unverified** — `in_game_placement-2f81982b55bf2ce2a1f4`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-b788302e082462acb716"></a>

**90° CCW: unverified** — `in_game_placement-b788302e082462acb716`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e94c09bfd628cf3528e7"></a>

**180° CCW: unverified** — `in_game_placement-e94c09bfd628cf3528e7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1a4001c8afdcb0eb7aa6"></a>

**270° CCW: unverified** — `in_game_placement-1a4001c8afdcb0eb7aa6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-2f81982b55bf2ce2a1f4">[ ] unverified</a> | <a href="#case-in_game_demolition-b788302e082462acb716">[ ] unverified</a> | <a href="#case-in_game_demolition-e94c09bfd628cf3528e7">[ ] unverified</a> | <a href="#case-in_game_demolition-1a4001c8afdcb0eb7aa6">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-2f81982b55bf2ce2a1f4"></a>

**0° CCW: unverified** — `in_game_demolition-2f81982b55bf2ce2a1f4`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-b788302e082462acb716"></a>

**90° CCW: unverified** — `in_game_demolition-b788302e082462acb716`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e94c09bfd628cf3528e7"></a>

**180° CCW: unverified** — `in_game_demolition-e94c09bfd628cf3528e7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1a4001c8afdcb0eb7aa6"></a>

**270° CCW: unverified** — `in_game_demolition-1a4001c8afdcb0eb7aa6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-2f81982b55bf2ce2a1f4">[ ] unverified</a> | <a href="#case-in_game_save_reload-b788302e082462acb716">[ ] unverified</a> | <a href="#case-in_game_save_reload-e94c09bfd628cf3528e7">[ ] unverified</a> | <a href="#case-in_game_save_reload-1a4001c8afdcb0eb7aa6">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-2f81982b55bf2ce2a1f4"></a>

**0° CCW: unverified** — `in_game_save_reload-2f81982b55bf2ce2a1f4`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-b788302e082462acb716"></a>

**90° CCW: unverified** — `in_game_save_reload-b788302e082462acb716`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e94c09bfd628cf3528e7"></a>

**180° CCW: unverified** — `in_game_save_reload-e94c09bfd628cf3528e7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1a4001c8afdcb0eb7aa6"></a>

**270° CCW: unverified** — `in_game_save_reload-1a4001c8afdcb0eb7aa6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-7ff2dac135f42aac3a02">[ ] unverified</a> | <a href="#case-in_game_route_query-a91b941e2dc8665dd73f">[ ] unverified</a> | <a href="#case-in_game_route_query-d100b00184df6c597274">[ ] unverified</a> | <a href="#case-in_game_route_query-28c7e9c814ecc19eeff0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-3865139866625ba8c96d">[ ] unverified</a> | <a href="#case-in_game_route_query-8aba4ffce8c7f71505ad">[ ] unverified</a> | <a href="#case-in_game_route_query-dd8dfa55726543fe3be5">[ ] unverified</a> | <a href="#case-in_game_route_query-a671460b367ff2d2a035">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-b8e265afb724d969433e">[ ] unverified</a> | <a href="#case-in_game_route_query-3e95892a20f61fcae5b4">[ ] unverified</a> | <a href="#case-in_game_route_query-7240e7f5c4c6cbe30d5b">[ ] unverified</a> | <a href="#case-in_game_route_query-b00e2a8a44195b2c5062">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-492d3489a2fe59747e92">[ ] unverified</a> | <a href="#case-in_game_route_query-09dc7aa1e7d7314b0a01">[ ] unverified</a> | <a href="#case-in_game_route_query-2cb18322d1f62dd6abce">[ ] unverified</a> | <a href="#case-in_game_route_query-6cd517e8297fa38d2ae1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-76a6e23dc9d117bcd037">[ ] unverified</a> | <a href="#case-in_game_route_query-d3613399807f220fa4c8">[ ] unverified</a> | <a href="#case-in_game_route_query-e261a6f425f9a7704808">[ ] unverified</a> | <a href="#case-in_game_route_query-cc66e28595514ba97604">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-7ff2dac135f42aac3a02"></a>

**0° CCW: unverified** — `in_game_route_query-7ff2dac135f42aac3a02`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-a91b941e2dc8665dd73f"></a>

**90° CCW: unverified** — `in_game_route_query-a91b941e2dc8665dd73f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-d100b00184df6c597274"></a>

**180° CCW: unverified** — `in_game_route_query-d100b00184df6c597274`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-28c7e9c814ecc19eeff0"></a>

**270° CCW: unverified** — `in_game_route_query-28c7e9c814ecc19eeff0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-3865139866625ba8c96d"></a>

**0° CCW: unverified** — `in_game_route_query-3865139866625ba8c96d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-8aba4ffce8c7f71505ad"></a>

**90° CCW: unverified** — `in_game_route_query-8aba4ffce8c7f71505ad`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-dd8dfa55726543fe3be5"></a>

**180° CCW: unverified** — `in_game_route_query-dd8dfa55726543fe3be5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-a671460b367ff2d2a035"></a>

**270° CCW: unverified** — `in_game_route_query-a671460b367ff2d2a035`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-b8e265afb724d969433e"></a>

**0° CCW: unverified** — `in_game_route_query-b8e265afb724d969433e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-3e95892a20f61fcae5b4"></a>

**90° CCW: unverified** — `in_game_route_query-3e95892a20f61fcae5b4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-7240e7f5c4c6cbe30d5b"></a>

**180° CCW: unverified** — `in_game_route_query-7240e7f5c4c6cbe30d5b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-b00e2a8a44195b2c5062"></a>

**270° CCW: unverified** — `in_game_route_query-b00e2a8a44195b2c5062`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-492d3489a2fe59747e92"></a>

**0° CCW: unverified** — `in_game_route_query-492d3489a2fe59747e92`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-09dc7aa1e7d7314b0a01"></a>

**90° CCW: unverified** — `in_game_route_query-09dc7aa1e7d7314b0a01`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-2cb18322d1f62dd6abce"></a>

**180° CCW: unverified** — `in_game_route_query-2cb18322d1f62dd6abce`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-6cd517e8297fa38d2ae1"></a>

**270° CCW: unverified** — `in_game_route_query-6cd517e8297fa38d2ae1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-76a6e23dc9d117bcd037"></a>

**0° CCW: unverified** — `in_game_route_query-76a6e23dc9d117bcd037`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-d3613399807f220fa4c8"></a>

**90° CCW: unverified** — `in_game_route_query-d3613399807f220fa4c8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-e261a6f425f9a7704808"></a>

**180° CCW: unverified** — `in_game_route_query-e261a6f425f9a7704808`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-cc66e28595514ba97604"></a>

**270° CCW: unverified** — `in_game_route_query-cc66e28595514ba97604`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-7ff2dac135f42aac3a02">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a91b941e2dc8665dd73f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d100b00184df6c597274">[ ] unverified</a> | <a href="#case-in_game_visible_travel-28c7e9c814ecc19eeff0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-3865139866625ba8c96d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8aba4ffce8c7f71505ad">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dd8dfa55726543fe3be5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a671460b367ff2d2a035">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-b8e265afb724d969433e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3e95892a20f61fcae5b4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7240e7f5c4c6cbe30d5b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b00e2a8a44195b2c5062">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-492d3489a2fe59747e92">[ ] unverified</a> | <a href="#case-in_game_visible_travel-09dc7aa1e7d7314b0a01">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2cb18322d1f62dd6abce">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6cd517e8297fa38d2ae1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-76a6e23dc9d117bcd037">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d3613399807f220fa4c8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e261a6f425f9a7704808">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cc66e28595514ba97604">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-7ff2dac135f42aac3a02"></a>

**0° CCW: unverified** — `in_game_visible_travel-7ff2dac135f42aac3a02`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-a91b941e2dc8665dd73f"></a>

**90° CCW: unverified** — `in_game_visible_travel-a91b941e2dc8665dd73f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-d100b00184df6c597274"></a>

**180° CCW: unverified** — `in_game_visible_travel-d100b00184df6c597274`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-28c7e9c814ecc19eeff0"></a>

**270° CCW: unverified** — `in_game_visible_travel-28c7e9c814ecc19eeff0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-3865139866625ba8c96d"></a>

**0° CCW: unverified** — `in_game_visible_travel-3865139866625ba8c96d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-8aba4ffce8c7f71505ad"></a>

**90° CCW: unverified** — `in_game_visible_travel-8aba4ffce8c7f71505ad`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-dd8dfa55726543fe3be5"></a>

**180° CCW: unverified** — `in_game_visible_travel-dd8dfa55726543fe3be5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-a671460b367ff2d2a035"></a>

**270° CCW: unverified** — `in_game_visible_travel-a671460b367ff2d2a035`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-b8e265afb724d969433e"></a>

**0° CCW: unverified** — `in_game_visible_travel-b8e265afb724d969433e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-3e95892a20f61fcae5b4"></a>

**90° CCW: unverified** — `in_game_visible_travel-3e95892a20f61fcae5b4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-7240e7f5c4c6cbe30d5b"></a>

**180° CCW: unverified** — `in_game_visible_travel-7240e7f5c4c6cbe30d5b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-b00e2a8a44195b2c5062"></a>

**270° CCW: unverified** — `in_game_visible_travel-b00e2a8a44195b2c5062`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-492d3489a2fe59747e92"></a>

**0° CCW: unverified** — `in_game_visible_travel-492d3489a2fe59747e92`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-09dc7aa1e7d7314b0a01"></a>

**90° CCW: unverified** — `in_game_visible_travel-09dc7aa1e7d7314b0a01`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-2cb18322d1f62dd6abce"></a>

**180° CCW: unverified** — `in_game_visible_travel-2cb18322d1f62dd6abce`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-6cd517e8297fa38d2ae1"></a>

**270° CCW: unverified** — `in_game_visible_travel-6cd517e8297fa38d2ae1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-76a6e23dc9d117bcd037"></a>

**0° CCW: unverified** — `in_game_visible_travel-76a6e23dc9d117bcd037`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-d3613399807f220fa4c8"></a>

**90° CCW: unverified** — `in_game_visible_travel-d3613399807f220fa4c8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-e261a6f425f9a7704808"></a>

**180° CCW: unverified** — `in_game_visible_travel-e261a6f425f9a7704808`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-cc66e28595514ba97604"></a>

**270° CCW: unverified** — `in_game_visible_travel-cc66e28595514ba97604`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7b9cefaff8063e0719b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43d8c1626e8b1fc65870">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa074545f0f429d449a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c39cd04813149f6bd761">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-81cda6b29dbb0b27c824">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aefa9800c3eff4827d78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7f7d975a93fdfd41c2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c88a708c4688825e704b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c5829065c86412159e8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d20057d7e548523aeea0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da81791569118fbecf60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a21fbe0706889ce3b64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-98c41d66581a8544a48e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78501f9b2e065ec9071e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19e2b8725253faeecfde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89f782e9bfb1d4eb9785">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ffa6220bdac40c42999">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b50490f99bce70b91edf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdd2d08bb05a49e46c6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a70eb6695992325dd5ea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8025486b2a8f37811912">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-baf8a012f7b4f8f73b58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1169806858495d332a81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-602c26b2f7b641a28954">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d75ca289b1f938e21118">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01dbf88126720fb47f65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05daaaaa1e1cbdeb24ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c7e0a5d0a1b246133da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6a6b5ad6823142562210">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-307345b3a56b51ce46aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b641b31da29aae7a1cc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3592b5e8864ee8c3437">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2ff94978dc0f036c75a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78ad2a9a85d716f6e65f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-895c724c20d14830d4a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3b235772c9f8b436e1b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d27455d5ee6bf0dceb76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b2e06e18bebc5a49f48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f5db1d2f851316cc076">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65f165495ed62ca78192">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4fa88819770e1fbb26b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b07278654c90f64f03a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c50d24f9d7e7bdc8c33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-099fbf77e3eefb478d37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a64f69ad6ff2beb16081">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa2502815e0b624a19d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a4efbd4535da090109f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cb89cbb98a7c875f47c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bb26929ce51123c465fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc5f81dfc1cb47252224">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87911a9f8d9078cf71b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9dc7f4ccfb3dbfc6209">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-48c2c03c5d6047455530">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0acdc00da09ee1062cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8cb5f64227296551596">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bc9fa653475b43df3f5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-57f2ee447f105c0d8243">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57102d73fd3dcfd0deed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b996deb2e2a472448a00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-281377f12db04ce9a3b0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-faac9829a271a799c834">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24047a71d2252d8da306">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3cdaacc485135da516c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c97d0de9294b55b13ee5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2565bbab95c6646be83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b15d834a0602000decd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b49295fda97b9739da4c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0537504dfda6e460d37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-34f2b5299616fc5d8904">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a4349bd4ba53bb85b7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42d66b0f1a894aa418e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-402e610274af9788f272">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2258fda8f83392b6c727">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-855e0461c61c7cca1bb2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4330ba3c151f278412f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19949cd2842668d5bc23">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-98253f47a69712812063">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11b40423e575b79c420a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d753c51948594df0bc3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99a93859b77c261ad073">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7b9cefaff8063e0719b6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7b9cefaff8063e0719b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43d8c1626e8b1fc65870"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-43d8c1626e8b1fc65870`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa074545f0f429d449a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aa074545f0f429d449a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c39cd04813149f6bd761"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c39cd04813149f6bd761`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-81cda6b29dbb0b27c824"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81cda6b29dbb0b27c824`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aefa9800c3eff4827d78"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aefa9800c3eff4827d78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7f7d975a93fdfd41c2f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c7f7d975a93fdfd41c2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c88a708c4688825e704b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c88a708c4688825e704b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c5829065c86412159e8e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5829065c86412159e8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d20057d7e548523aeea0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d20057d7e548523aeea0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da81791569118fbecf60"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-da81791569118fbecf60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a21fbe0706889ce3b64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a21fbe0706889ce3b64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-98c41d66581a8544a48e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-98c41d66581a8544a48e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78501f9b2e065ec9071e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78501f9b2e065ec9071e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19e2b8725253faeecfde"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-19e2b8725253faeecfde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89f782e9bfb1d4eb9785"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89f782e9bfb1d4eb9785`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ffa6220bdac40c42999"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ffa6220bdac40c42999`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b50490f99bce70b91edf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b50490f99bce70b91edf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdd2d08bb05a49e46c6d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fdd2d08bb05a49e46c6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a70eb6695992325dd5ea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a70eb6695992325dd5ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8025486b2a8f37811912"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8025486b2a8f37811912`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-baf8a012f7b4f8f73b58"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-baf8a012f7b4f8f73b58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1169806858495d332a81"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1169806858495d332a81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-602c26b2f7b641a28954"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-602c26b2f7b641a28954`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d75ca289b1f938e21118"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d75ca289b1f938e21118`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01dbf88126720fb47f65"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-01dbf88126720fb47f65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05daaaaa1e1cbdeb24ea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-05daaaaa1e1cbdeb24ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c7e0a5d0a1b246133da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c7e0a5d0a1b246133da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6a6b5ad6823142562210"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6a6b5ad6823142562210`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-307345b3a56b51ce46aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-307345b3a56b51ce46aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b641b31da29aae7a1cc9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b641b31da29aae7a1cc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3592b5e8864ee8c3437"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b3592b5e8864ee8c3437`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c2ff94978dc0f036c75a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c2ff94978dc0f036c75a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78ad2a9a85d716f6e65f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78ad2a9a85d716f6e65f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-895c724c20d14830d4a1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-895c724c20d14830d4a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3b235772c9f8b436e1b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d3b235772c9f8b436e1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d27455d5ee6bf0dceb76"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d27455d5ee6bf0dceb76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b2e06e18bebc5a49f48"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5b2e06e18bebc5a49f48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f5db1d2f851316cc076"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f5db1d2f851316cc076`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65f165495ed62ca78192"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-65f165495ed62ca78192`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4fa88819770e1fbb26b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4fa88819770e1fbb26b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b07278654c90f64f03a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b07278654c90f64f03a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c50d24f9d7e7bdc8c33"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c50d24f9d7e7bdc8c33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-099fbf77e3eefb478d37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-099fbf77e3eefb478d37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a64f69ad6ff2beb16081"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a64f69ad6ff2beb16081`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa2502815e0b624a19d9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa2502815e0b624a19d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a4efbd4535da090109f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7a4efbd4535da090109f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cb89cbb98a7c875f47c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6cb89cbb98a7c875f47c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bb26929ce51123c465fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bb26929ce51123c465fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc5f81dfc1cb47252224"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fc5f81dfc1cb47252224`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87911a9f8d9078cf71b3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-87911a9f8d9078cf71b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9dc7f4ccfb3dbfc6209"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e9dc7f4ccfb3dbfc6209`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-48c2c03c5d6047455530"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-48c2c03c5d6047455530`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0acdc00da09ee1062cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0acdc00da09ee1062cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8cb5f64227296551596"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f8cb5f64227296551596`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bc9fa653475b43df3f5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0bc9fa653475b43df3f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-57f2ee447f105c0d8243"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-57f2ee447f105c0d8243`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57102d73fd3dcfd0deed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-57102d73fd3dcfd0deed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b996deb2e2a472448a00"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b996deb2e2a472448a00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-281377f12db04ce9a3b0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-281377f12db04ce9a3b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-faac9829a271a799c834"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-faac9829a271a799c834`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24047a71d2252d8da306"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24047a71d2252d8da306`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3cdaacc485135da516c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a3cdaacc485135da516c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c97d0de9294b55b13ee5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c97d0de9294b55b13ee5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2565bbab95c6646be83"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2565bbab95c6646be83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b15d834a0602000decd3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b15d834a0602000decd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b49295fda97b9739da4c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b49295fda97b9739da4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0537504dfda6e460d37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c0537504dfda6e460d37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-34f2b5299616fc5d8904"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-34f2b5299616fc5d8904`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a4349bd4ba53bb85b7c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a4349bd4ba53bb85b7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42d66b0f1a894aa418e3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42d66b0f1a894aa418e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-402e610274af9788f272"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-402e610274af9788f272`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2258fda8f83392b6c727"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2258fda8f83392b6c727`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-855e0461c61c7cca1bb2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-855e0461c61c7cca1bb2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4330ba3c151f278412f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4330ba3c151f278412f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19949cd2842668d5bc23"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-19949cd2842668d5bc23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-98253f47a69712812063"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-98253f47a69712812063`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11b40423e575b79c420a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-11b40423e575b79c420a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d753c51948594df0bc3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3d753c51948594df0bc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99a93859b77c261ad073"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-99a93859b77c261ad073`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-entry-grade:canonical-southeast | <a href="#case-preview_review-d2461642e5800f7faf3c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-entry-grade:canonical-top | <a href="#case-preview_review-7df4fab8d92bbae18d9e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-entry-grade:connection-overview | <a href="#case-preview_review-650b42c452766bc4fc2d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-entry-grade:canonical-southeast</summary>

<a id="case-preview_review-d2461642e5800f7faf3c"></a>

**General: unverified** — `preview_review-d2461642e5800f7faf3c`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-entry-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-entry-grade:canonical-top</summary>

<a id="case-preview_review-7df4fab8d92bbae18d9e"></a>

**General: unverified** — `preview_review-7df4fab8d92bbae18d9e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-entry-grade:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-entry-grade:connection-overview</summary>

<a id="case-preview_review-650b42c452766bc4fc2d"></a>

**General: unverified** — `preview_review-650b42c452766bc4fc2d`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-entry-grade:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the grade function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
