---
title: "Testing: RHW Ramp \u2014 L1 Exit Parallel Grade \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L1 Exit Parallel Grade — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **RHW Ramp — L1 Exit Parallel Grade — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-lower-exit-grade`, as **P12** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 3 cells inside its 2 × 2 bounding footprint. Physical grade between 7.5 m and 0 m; actual cell-edge ports have their own measured intermediate heights. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-06-out` | road / 1 / primary | out | [-0.970563, -24.0, 0.083612]; [-0.7071067811865476, -0.7071067811865476]; -0.115840807 | `path-interface-42edd41fff244415427a` |
| `channel-07-out` | road / 1 / primary | out | [12.8, -24.0, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [12.8, -24.0, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-08-out` | road / 1 / primary | out | [19.2, -24.0, 7.5]; [-0.7071067811865474, -0.7071067811865478]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-02-in` | road / 1 / primary | in | [19.2, -24.0, 15.0]; [0.7071067811865474, 0.7071067811865478]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-03-in` | road / 1 / primary | in | [24.0, -19.2, 7.5]; [-0.7071067811865474, -0.7071067811865478]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-09-out` | road / 1 / primary | out | [24.0, -19.2, 15.0]; [0.7071067811865474, 0.7071067811865478]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-04-in` | road / 1 / primary | in | [24.0, -12.8, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-10-out` | road / 1 / primary | out | [24.0, -12.8, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-05-in` | road / 1 / primary | in | [24.0, 0.970563, 6.390578]; [-0.7071067811865284, -0.7071067811865668]; -0.179116236 | `path-interface-bead969a8cb1cad1321c` |

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
| road / `channel-01-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-lower-exit-grade
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **7,983 indexed triangles** and **7 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-lower-exit-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-lower-exit-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-cd6ef8699667b39256d1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-cd6ef8699667b39256d1"></a>

**General: unverified** — `software_resources-cd6ef8699667b39256d1`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-cd6ef8699667b39256d1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-cd6ef8699667b39256d1"></a>

**General: unverified** — `software_connectivity-cd6ef8699667b39256d1`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-cba106bb4ad8315df48b">[ ] unverified</a> | <a href="#case-in_game_render-0d6b37574db323640c1c">[ ] unverified</a> | <a href="#case-in_game_render-2adef88b18d80fd623ae">[ ] unverified</a> | <a href="#case-in_game_render-a86918edc592c7095880">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-cba106bb4ad8315df48b"></a>

**0° CCW: unverified** — `in_game_render-cba106bb4ad8315df48b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0d6b37574db323640c1c"></a>

**90° CCW: unverified** — `in_game_render-0d6b37574db323640c1c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2adef88b18d80fd623ae"></a>

**180° CCW: unverified** — `in_game_render-2adef88b18d80fd623ae`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a86918edc592c7095880"></a>

**270° CCW: unverified** — `in_game_render-a86918edc592c7095880`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-cba106bb4ad8315df48b">[ ] unverified</a> | <a href="#case-in_game_placement-0d6b37574db323640c1c">[ ] unverified</a> | <a href="#case-in_game_placement-2adef88b18d80fd623ae">[ ] unverified</a> | <a href="#case-in_game_placement-a86918edc592c7095880">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-cba106bb4ad8315df48b"></a>

**0° CCW: unverified** — `in_game_placement-cba106bb4ad8315df48b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0d6b37574db323640c1c"></a>

**90° CCW: unverified** — `in_game_placement-0d6b37574db323640c1c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2adef88b18d80fd623ae"></a>

**180° CCW: unverified** — `in_game_placement-2adef88b18d80fd623ae`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a86918edc592c7095880"></a>

**270° CCW: unverified** — `in_game_placement-a86918edc592c7095880`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-cba106bb4ad8315df48b">[ ] unverified</a> | <a href="#case-in_game_demolition-0d6b37574db323640c1c">[ ] unverified</a> | <a href="#case-in_game_demolition-2adef88b18d80fd623ae">[ ] unverified</a> | <a href="#case-in_game_demolition-a86918edc592c7095880">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-cba106bb4ad8315df48b"></a>

**0° CCW: unverified** — `in_game_demolition-cba106bb4ad8315df48b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0d6b37574db323640c1c"></a>

**90° CCW: unverified** — `in_game_demolition-0d6b37574db323640c1c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2adef88b18d80fd623ae"></a>

**180° CCW: unverified** — `in_game_demolition-2adef88b18d80fd623ae`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a86918edc592c7095880"></a>

**270° CCW: unverified** — `in_game_demolition-a86918edc592c7095880`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-cba106bb4ad8315df48b">[ ] unverified</a> | <a href="#case-in_game_save_reload-0d6b37574db323640c1c">[ ] unverified</a> | <a href="#case-in_game_save_reload-2adef88b18d80fd623ae">[ ] unverified</a> | <a href="#case-in_game_save_reload-a86918edc592c7095880">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-cba106bb4ad8315df48b"></a>

**0° CCW: unverified** — `in_game_save_reload-cba106bb4ad8315df48b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0d6b37574db323640c1c"></a>

**90° CCW: unverified** — `in_game_save_reload-0d6b37574db323640c1c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2adef88b18d80fd623ae"></a>

**180° CCW: unverified** — `in_game_save_reload-2adef88b18d80fd623ae`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a86918edc592c7095880"></a>

**270° CCW: unverified** — `in_game_save_reload-a86918edc592c7095880`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-f6958aeda0f28ca23f86">[ ] unverified</a> | <a href="#case-in_game_route_query-ff614b6f743282f94989">[ ] unverified</a> | <a href="#case-in_game_route_query-e78bd620e6603689d37a">[ ] unverified</a> | <a href="#case-in_game_route_query-4e8cc0a7062ab023bc12">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-76675f6031011131a644">[ ] unverified</a> | <a href="#case-in_game_route_query-14e41f1ec504a3cadaeb">[ ] unverified</a> | <a href="#case-in_game_route_query-fbc39adb71ffa4d858db">[ ] unverified</a> | <a href="#case-in_game_route_query-08a797e7a79b0fe56a64">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-96978424072b191c5c62">[ ] unverified</a> | <a href="#case-in_game_route_query-a8fd2c51e6f70dc0578a">[ ] unverified</a> | <a href="#case-in_game_route_query-cbf096947770f7335353">[ ] unverified</a> | <a href="#case-in_game_route_query-e14e9691cf92feb966ba">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-78c586f4c51eb7b94544">[ ] unverified</a> | <a href="#case-in_game_route_query-cb1007a53cc804672f8c">[ ] unverified</a> | <a href="#case-in_game_route_query-c335d3310ff66db6e0be">[ ] unverified</a> | <a href="#case-in_game_route_query-3d8d507a894506008b8f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-89b625e3e98cb78d1f82">[ ] unverified</a> | <a href="#case-in_game_route_query-58a8b948a122cfe48e82">[ ] unverified</a> | <a href="#case-in_game_route_query-dfeb7614eb222980bb38">[ ] unverified</a> | <a href="#case-in_game_route_query-c20d45bd4b9cd1e2d297">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-f6958aeda0f28ca23f86"></a>

**0° CCW: unverified** — `in_game_route_query-f6958aeda0f28ca23f86`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-ff614b6f743282f94989"></a>

**90° CCW: unverified** — `in_game_route_query-ff614b6f743282f94989`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-e78bd620e6603689d37a"></a>

**180° CCW: unverified** — `in_game_route_query-e78bd620e6603689d37a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-4e8cc0a7062ab023bc12"></a>

**270° CCW: unverified** — `in_game_route_query-4e8cc0a7062ab023bc12`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-76675f6031011131a644"></a>

**0° CCW: unverified** — `in_game_route_query-76675f6031011131a644`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-14e41f1ec504a3cadaeb"></a>

**90° CCW: unverified** — `in_game_route_query-14e41f1ec504a3cadaeb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-fbc39adb71ffa4d858db"></a>

**180° CCW: unverified** — `in_game_route_query-fbc39adb71ffa4d858db`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-08a797e7a79b0fe56a64"></a>

**270° CCW: unverified** — `in_game_route_query-08a797e7a79b0fe56a64`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-96978424072b191c5c62"></a>

**0° CCW: unverified** — `in_game_route_query-96978424072b191c5c62`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-a8fd2c51e6f70dc0578a"></a>

**90° CCW: unverified** — `in_game_route_query-a8fd2c51e6f70dc0578a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-cbf096947770f7335353"></a>

**180° CCW: unverified** — `in_game_route_query-cbf096947770f7335353`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-e14e9691cf92feb966ba"></a>

**270° CCW: unverified** — `in_game_route_query-e14e9691cf92feb966ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-78c586f4c51eb7b94544"></a>

**0° CCW: unverified** — `in_game_route_query-78c586f4c51eb7b94544`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-cb1007a53cc804672f8c"></a>

**90° CCW: unverified** — `in_game_route_query-cb1007a53cc804672f8c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-c335d3310ff66db6e0be"></a>

**180° CCW: unverified** — `in_game_route_query-c335d3310ff66db6e0be`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-3d8d507a894506008b8f"></a>

**270° CCW: unverified** — `in_game_route_query-3d8d507a894506008b8f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-89b625e3e98cb78d1f82"></a>

**0° CCW: unverified** — `in_game_route_query-89b625e3e98cb78d1f82`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-58a8b948a122cfe48e82"></a>

**90° CCW: unverified** — `in_game_route_query-58a8b948a122cfe48e82`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-dfeb7614eb222980bb38"></a>

**180° CCW: unverified** — `in_game_route_query-dfeb7614eb222980bb38`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-c20d45bd4b9cd1e2d297"></a>

**270° CCW: unverified** — `in_game_route_query-c20d45bd4b9cd1e2d297`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-f6958aeda0f28ca23f86">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff614b6f743282f94989">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e78bd620e6603689d37a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4e8cc0a7062ab023bc12">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-76675f6031011131a644">[ ] unverified</a> | <a href="#case-in_game_visible_travel-14e41f1ec504a3cadaeb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fbc39adb71ffa4d858db">[ ] unverified</a> | <a href="#case-in_game_visible_travel-08a797e7a79b0fe56a64">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-96978424072b191c5c62">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a8fd2c51e6f70dc0578a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cbf096947770f7335353">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e14e9691cf92feb966ba">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-78c586f4c51eb7b94544">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cb1007a53cc804672f8c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c335d3310ff66db6e0be">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3d8d507a894506008b8f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-89b625e3e98cb78d1f82">[ ] unverified</a> | <a href="#case-in_game_visible_travel-58a8b948a122cfe48e82">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dfeb7614eb222980bb38">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c20d45bd4b9cd1e2d297">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-f6958aeda0f28ca23f86"></a>

**0° CCW: unverified** — `in_game_visible_travel-f6958aeda0f28ca23f86`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-ff614b6f743282f94989"></a>

**90° CCW: unverified** — `in_game_visible_travel-ff614b6f743282f94989`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-e78bd620e6603689d37a"></a>

**180° CCW: unverified** — `in_game_visible_travel-e78bd620e6603689d37a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-4e8cc0a7062ab023bc12"></a>

**270° CCW: unverified** — `in_game_visible_travel-4e8cc0a7062ab023bc12`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-76675f6031011131a644"></a>

**0° CCW: unverified** — `in_game_visible_travel-76675f6031011131a644`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-14e41f1ec504a3cadaeb"></a>

**90° CCW: unverified** — `in_game_visible_travel-14e41f1ec504a3cadaeb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-fbc39adb71ffa4d858db"></a>

**180° CCW: unverified** — `in_game_visible_travel-fbc39adb71ffa4d858db`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-08a797e7a79b0fe56a64"></a>

**270° CCW: unverified** — `in_game_visible_travel-08a797e7a79b0fe56a64`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-96978424072b191c5c62"></a>

**0° CCW: unverified** — `in_game_visible_travel-96978424072b191c5c62`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-a8fd2c51e6f70dc0578a"></a>

**90° CCW: unverified** — `in_game_visible_travel-a8fd2c51e6f70dc0578a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-cbf096947770f7335353"></a>

**180° CCW: unverified** — `in_game_visible_travel-cbf096947770f7335353`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-e14e9691cf92feb966ba"></a>

**270° CCW: unverified** — `in_game_visible_travel-e14e9691cf92feb966ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-78c586f4c51eb7b94544"></a>

**0° CCW: unverified** — `in_game_visible_travel-78c586f4c51eb7b94544`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-cb1007a53cc804672f8c"></a>

**90° CCW: unverified** — `in_game_visible_travel-cb1007a53cc804672f8c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-c335d3310ff66db6e0be"></a>

**180° CCW: unverified** — `in_game_visible_travel-c335d3310ff66db6e0be`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-3d8d507a894506008b8f"></a>

**270° CCW: unverified** — `in_game_visible_travel-3d8d507a894506008b8f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-89b625e3e98cb78d1f82"></a>

**0° CCW: unverified** — `in_game_visible_travel-89b625e3e98cb78d1f82`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-58a8b948a122cfe48e82"></a>

**90° CCW: unverified** — `in_game_visible_travel-58a8b948a122cfe48e82`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-dfeb7614eb222980bb38"></a>

**180° CCW: unverified** — `in_game_visible_travel-dfeb7614eb222980bb38`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-c20d45bd4b9cd1e2d297"></a>

**270° CCW: unverified** — `in_game_visible_travel-c20d45bd4b9cd1e2d297`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0abfa60825a3893fd532">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a82640d4284fee2451e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3be7d90877defd17628f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa46811b8b34e287052e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45b4831acc645af3d69b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4789cb71a3c1a29dff8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6f736db1ba4a57ea635">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-325a67f1c7466bd64ac0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-56b6e6d7b10b0ea08199">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1f7fdd7f660de9fb37c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68043411cead083d10a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a2c3670a49a921fb402">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f61e7c71f2cc3ea9e8a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c344f00c2356aaa7c52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe29963c9dbb96e0ab0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1bff952e004ca273b6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-183cf862fdf8c78aaf21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4a1c64f1fe630ca5a35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54e8df3dd8ff87e977c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68e4abfa36fb9b69d1d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e20fdedd6dcdfaa28fbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e9b6373fe15e885fd69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f523384de0194544b25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f96911105828e60eb78">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5289583f8f9ccd3b23c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ff741be124b709c2dee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ee3cc826acf9ff185c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11869401b7548d493c59">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-303c919070023aa85af9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f062c716736e1a59391">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ee692d3558462e301c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fa713d514799968dad3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fa2c29d9c564dc02add8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01dc5bbf8f43b05638a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ce867a0fdbd740cd912">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c42678e7e3f5e741e516">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32f9fe59d92cdd730bab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39fdba7785c8012a0fb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f73d78ea433c37b39bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41dd01c13e596a1c8efb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-60720423451037c1bb4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b682b548f99193f77e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a05a74b0f09e0f3aa632">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a22589b9da4e2303532">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f91351ee308b4efd17e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dc7152057785962f06b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7eac44d3b70098dc6e9f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3de617ebba35415cdca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-da73272878213120dc00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-739f2f1c9bb3a73b84eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89c0398a34eb926bdc5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46c5e72688df33aafbc7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a351a22d1cf0972986cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e16c24cc89ca2d82910">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0890dae3ec128ad7eb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-def00fb0f777b777a823">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-882ba1fd45c16490cf6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4e01baa748083704430">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3d63cfcd2a9b095ff1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7f423aac8aca522b715">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c942a9251b96bd2e3fe2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d60211020a917caadf1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de3e88e18e566348450d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-736bcb5c99ec1541eba7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8cac6c9d1ee708c59af6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a2d5b3305dccb06d7b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d3f99bc854284f1e489">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69f65dae972e5b4af825">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d81c810ecdd588da297">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0571f6c828d4c8e64f25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-456a75d6239dfc51291c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e3adf249d24e39fc195">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e80038be273a48627565">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24455b923c166b9c0cbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54e3dd99842594fc3c03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7bc1db8b2d204d357357">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9f2db22bec1dd28608ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f73dc03b52567689aecf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f78f153f6146fcc9164">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1585f28b0f0a56844376">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0abfa60825a3893fd532"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0abfa60825a3893fd532`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a82640d4284fee2451e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a82640d4284fee2451e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3be7d90877defd17628f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3be7d90877defd17628f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa46811b8b34e287052e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa46811b8b34e287052e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45b4831acc645af3d69b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45b4831acc645af3d69b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4789cb71a3c1a29dff8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c4789cb71a3c1a29dff8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6f736db1ba4a57ea635"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a6f736db1ba4a57ea635`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-325a67f1c7466bd64ac0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-325a67f1c7466bd64ac0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-56b6e6d7b10b0ea08199"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-56b6e6d7b10b0ea08199`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1f7fdd7f660de9fb37c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a1f7fdd7f660de9fb37c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68043411cead083d10a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-68043411cead083d10a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a2c3670a49a921fb402"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2a2c3670a49a921fb402`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f61e7c71f2cc3ea9e8a4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f61e7c71f2cc3ea9e8a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c344f00c2356aaa7c52"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2c344f00c2356aaa7c52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe29963c9dbb96e0ab0a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fe29963c9dbb96e0ab0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1bff952e004ca273b6c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a1bff952e004ca273b6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-183cf862fdf8c78aaf21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-183cf862fdf8c78aaf21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4a1c64f1fe630ca5a35"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f4a1c64f1fe630ca5a35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54e8df3dd8ff87e977c1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54e8df3dd8ff87e977c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68e4abfa36fb9b69d1d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68e4abfa36fb9b69d1d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e20fdedd6dcdfaa28fbd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e20fdedd6dcdfaa28fbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e9b6373fe15e885fd69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e9b6373fe15e885fd69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f523384de0194544b25"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9f523384de0194544b25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f96911105828e60eb78"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f96911105828e60eb78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5289583f8f9ccd3b23c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5289583f8f9ccd3b23c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ff741be124b709c2dee"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ff741be124b709c2dee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ee3cc826acf9ff185c1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ee3cc826acf9ff185c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11869401b7548d493c59"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-11869401b7548d493c59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-303c919070023aa85af9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-303c919070023aa85af9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f062c716736e1a59391"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f062c716736e1a59391`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ee692d3558462e301c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ee692d3558462e301c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fa713d514799968dad3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1fa713d514799968dad3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fa2c29d9c564dc02add8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa2c29d9c564dc02add8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01dc5bbf8f43b05638a6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-01dc5bbf8f43b05638a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ce867a0fdbd740cd912"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ce867a0fdbd740cd912`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c42678e7e3f5e741e516"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c42678e7e3f5e741e516`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32f9fe59d92cdd730bab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32f9fe59d92cdd730bab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39fdba7785c8012a0fb7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39fdba7785c8012a0fb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f73d78ea433c37b39bd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3f73d78ea433c37b39bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41dd01c13e596a1c8efb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-41dd01c13e596a1c8efb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-60720423451037c1bb4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60720423451037c1bb4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b682b548f99193f77e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b682b548f99193f77e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a05a74b0f09e0f3aa632"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a05a74b0f09e0f3aa632`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a22589b9da4e2303532"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a22589b9da4e2303532`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f91351ee308b4efd17e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f91351ee308b4efd17e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dc7152057785962f06b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6dc7152057785962f06b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7eac44d3b70098dc6e9f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7eac44d3b70098dc6e9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3de617ebba35415cdca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c3de617ebba35415cdca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-da73272878213120dc00"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-da73272878213120dc00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-739f2f1c9bb3a73b84eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-739f2f1c9bb3a73b84eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89c0398a34eb926bdc5e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-89c0398a34eb926bdc5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46c5e72688df33aafbc7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-46c5e72688df33aafbc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a351a22d1cf0972986cb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a351a22d1cf0972986cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e16c24cc89ca2d82910"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3e16c24cc89ca2d82910`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0890dae3ec128ad7eb4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f0890dae3ec128ad7eb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-def00fb0f777b777a823"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-def00fb0f777b777a823`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-882ba1fd45c16490cf6d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-882ba1fd45c16490cf6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4e01baa748083704430"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a4e01baa748083704430`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3d63cfcd2a9b095ff1e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e3d63cfcd2a9b095ff1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7f423aac8aca522b715"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b7f423aac8aca522b715`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c942a9251b96bd2e3fe2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c942a9251b96bd2e3fe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d60211020a917caadf1c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d60211020a917caadf1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de3e88e18e566348450d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de3e88e18e566348450d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-736bcb5c99ec1541eba7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-736bcb5c99ec1541eba7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8cac6c9d1ee708c59af6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8cac6c9d1ee708c59af6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a2d5b3305dccb06d7b3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9a2d5b3305dccb06d7b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d3f99bc854284f1e489"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7d3f99bc854284f1e489`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69f65dae972e5b4af825"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69f65dae972e5b4af825`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d81c810ecdd588da297"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d81c810ecdd588da297`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0571f6c828d4c8e64f25"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0571f6c828d4c8e64f25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-456a75d6239dfc51291c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-456a75d6239dfc51291c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e3adf249d24e39fc195"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e3adf249d24e39fc195`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e80038be273a48627565"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e80038be273a48627565`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24455b923c166b9c0cbc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24455b923c166b9c0cbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54e3dd99842594fc3c03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54e3dd99842594fc3c03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7bc1db8b2d204d357357"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7bc1db8b2d204d357357`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9f2db22bec1dd28608ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f2db22bec1dd28608ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f73dc03b52567689aecf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f73dc03b52567689aecf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f78f153f6146fcc9164"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1f78f153f6146fcc9164`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1585f28b0f0a56844376"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1585f28b0f0a56844376`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-exit-grade:canonical-southeast | <a href="#case-preview_review-f5e801ea8a0575627868">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-exit-grade:canonical-top | <a href="#case-preview_review-f0a45ae23c97ea952261">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-exit-grade:connection-overview | <a href="#case-preview_review-81f08007b918487ef1c6">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-exit-grade:canonical-southeast</summary>

<a id="case-preview_review-f5e801ea8a0575627868"></a>

**General: unverified** — `preview_review-f5e801ea8a0575627868`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-exit-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-exit-grade:canonical-top</summary>

<a id="case-preview_review-f0a45ae23c97ea952261"></a>

**General: unverified** — `preview_review-f0a45ae23c97ea952261`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-exit-grade:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-exit-grade:connection-overview</summary>

<a id="case-preview_review-81f08007b918487ef1c6"></a>

**General: unverified** — `preview_review-81f08007b918487ef1c6`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-exit-grade:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the grade function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
