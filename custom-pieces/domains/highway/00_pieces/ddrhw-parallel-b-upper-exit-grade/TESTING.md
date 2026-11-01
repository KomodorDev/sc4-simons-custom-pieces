---
title: "Testing: RHW Ramp \u2014 L2 Exit Parallel Grade \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L2 Exit Parallel Grade — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **RHW Ramp — L2 Exit Parallel Grade — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-upper-exit-grade`, as **P14** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 3 cells inside its 2 × 3 bounding footprint. Physical grade between 15 m and 0 m; actual cell-edge ports have their own measured intermediate heights. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -32.970563, 13.253148]; [0.7071067811865476, 0.7071067811865476]; -0.282029195 | `path-interface-481a9f04963a1402d262` |
| `channel-07-out` | road / 1 / primary | out | [0.970563, -24.0, 9.675242]; [0.707106781186558, 0.7071067811865371]; -0.282029323 | `path-interface-55a6a5bf7f0b33d60b89` |
| `channel-02-in` | road / 1 / primary | in | [8.0, -16.970563, 6.871553]; [0.7071067811865476, 0.7071067811865476]; -0.282029319 | `path-interface-6de14d4db7fbc1b8f4fd` |
| `channel-08-out` | road / 1 / primary | out | [8.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-03-in` | road / 1 / primary | in | [8.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-09-out` | road / 1 / primary | out | [8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-04-in` | road / 1 / primary | in | [8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-05-in` | road / 1 / primary | in | [12.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-10-out` | road / 1 / primary | out | [12.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-06-in` | road / 1 / primary | in | [19.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-11-out` | road / 1 / primary | out | [19.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-12-out` | road / 1 / primary | out | [24.0, -0.970563, 0.489958]; [0.7071067811865476, 0.7071067811865476]; -0.282029333 | `path-interface-de2471bc41cdce8bf875` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-07-out` | primary |
| road | `channel-02-in` → `channel-12-out` | primary |
| road | `channel-03-in` → `channel-11-out` | primary |
| road | `channel-04-in` → `channel-10-out` | primary |
| road | `channel-05-in` → `channel-09-out` | primary |
| road | `channel-06-in` → `channel-08-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-upper-exit-grade
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **10,060 indexed triangles** and **7 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
- [ ] Route Query: 0/24 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/24 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 189, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-exit-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-exit-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-3562800f29b9659a653a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-3562800f29b9659a653a"></a>

**General: unverified** — `software_resources-3562800f29b9659a653a`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-3562800f29b9659a653a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-3562800f29b9659a653a"></a>

**General: unverified** — `software_connectivity-3562800f29b9659a653a`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-10b700ece125100ebf4f">[ ] unverified</a> | <a href="#case-in_game_render-af840d7d95a21f0a6b45">[ ] unverified</a> | <a href="#case-in_game_render-61b97ad114aa52b9449c">[ ] unverified</a> | <a href="#case-in_game_render-65dac7f01882fa751a0c">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-10b700ece125100ebf4f"></a>

**0° CCW: unverified** — `in_game_render-10b700ece125100ebf4f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-af840d7d95a21f0a6b45"></a>

**90° CCW: unverified** — `in_game_render-af840d7d95a21f0a6b45`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-61b97ad114aa52b9449c"></a>

**180° CCW: unverified** — `in_game_render-61b97ad114aa52b9449c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-65dac7f01882fa751a0c"></a>

**270° CCW: unverified** — `in_game_render-65dac7f01882fa751a0c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-10b700ece125100ebf4f">[ ] unverified</a> | <a href="#case-in_game_placement-af840d7d95a21f0a6b45">[ ] unverified</a> | <a href="#case-in_game_placement-61b97ad114aa52b9449c">[ ] unverified</a> | <a href="#case-in_game_placement-65dac7f01882fa751a0c">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-10b700ece125100ebf4f"></a>

**0° CCW: unverified** — `in_game_placement-10b700ece125100ebf4f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-af840d7d95a21f0a6b45"></a>

**90° CCW: unverified** — `in_game_placement-af840d7d95a21f0a6b45`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-61b97ad114aa52b9449c"></a>

**180° CCW: unverified** — `in_game_placement-61b97ad114aa52b9449c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-65dac7f01882fa751a0c"></a>

**270° CCW: unverified** — `in_game_placement-65dac7f01882fa751a0c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-10b700ece125100ebf4f">[ ] unverified</a> | <a href="#case-in_game_demolition-af840d7d95a21f0a6b45">[ ] unverified</a> | <a href="#case-in_game_demolition-61b97ad114aa52b9449c">[ ] unverified</a> | <a href="#case-in_game_demolition-65dac7f01882fa751a0c">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-10b700ece125100ebf4f"></a>

**0° CCW: unverified** — `in_game_demolition-10b700ece125100ebf4f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-af840d7d95a21f0a6b45"></a>

**90° CCW: unverified** — `in_game_demolition-af840d7d95a21f0a6b45`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-61b97ad114aa52b9449c"></a>

**180° CCW: unverified** — `in_game_demolition-61b97ad114aa52b9449c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-65dac7f01882fa751a0c"></a>

**270° CCW: unverified** — `in_game_demolition-65dac7f01882fa751a0c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-10b700ece125100ebf4f">[ ] unverified</a> | <a href="#case-in_game_save_reload-af840d7d95a21f0a6b45">[ ] unverified</a> | <a href="#case-in_game_save_reload-61b97ad114aa52b9449c">[ ] unverified</a> | <a href="#case-in_game_save_reload-65dac7f01882fa751a0c">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-10b700ece125100ebf4f"></a>

**0° CCW: unverified** — `in_game_save_reload-10b700ece125100ebf4f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-af840d7d95a21f0a6b45"></a>

**90° CCW: unverified** — `in_game_save_reload-af840d7d95a21f0a6b45`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-61b97ad114aa52b9449c"></a>

**180° CCW: unverified** — `in_game_save_reload-61b97ad114aa52b9449c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-65dac7f01882fa751a0c"></a>

**270° CCW: unverified** — `in_game_save_reload-65dac7f01882fa751a0c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-6109f5bbccb43a432b4c">[ ] unverified</a> | <a href="#case-in_game_route_query-e9025b8c9020c5bfe29b">[ ] unverified</a> | <a href="#case-in_game_route_query-227b6d1fbad202d344e2">[ ] unverified</a> | <a href="#case-in_game_route_query-9a25bb812279972da5f2">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-113c1593c347b43e4c59">[ ] unverified</a> | <a href="#case-in_game_route_query-cdacebe32ae872f8ee60">[ ] unverified</a> | <a href="#case-in_game_route_query-35621915078e648f50dd">[ ] unverified</a> | <a href="#case-in_game_route_query-22fa1c2a6f77440332d1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-0e2c29e55dfa92a72768">[ ] unverified</a> | <a href="#case-in_game_route_query-6ad4ffc2ac133310293c">[ ] unverified</a> | <a href="#case-in_game_route_query-0bf5ad1e159cfce1303e">[ ] unverified</a> | <a href="#case-in_game_route_query-f7cd4f70272f51a3d8aa">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-c5ae8754c045ab810c67">[ ] unverified</a> | <a href="#case-in_game_route_query-45130db8399a5da34d05">[ ] unverified</a> | <a href="#case-in_game_route_query-e134a90b0757d5303875">[ ] unverified</a> | <a href="#case-in_game_route_query-cb6d62ba4bf28c652f77">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-07827aee91f293cf5267">[ ] unverified</a> | <a href="#case-in_game_route_query-f3a95aaf4ae7b486e92a">[ ] unverified</a> | <a href="#case-in_game_route_query-8457f3ab5c3a79477964">[ ] unverified</a> | <a href="#case-in_game_route_query-5710c72fc92beff2059d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-de4761b284e2fef340ee">[ ] unverified</a> | <a href="#case-in_game_route_query-79abae856ccd062af09a">[ ] unverified</a> | <a href="#case-in_game_route_query-daa2c23a5bc68c727e91">[ ] unverified</a> | <a href="#case-in_game_route_query-b2faf053ecd3df9530b9">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-6109f5bbccb43a432b4c"></a>

**0° CCW: unverified** — `in_game_route_query-6109f5bbccb43a432b4c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-e9025b8c9020c5bfe29b"></a>

**90° CCW: unverified** — `in_game_route_query-e9025b8c9020c5bfe29b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-227b6d1fbad202d344e2"></a>

**180° CCW: unverified** — `in_game_route_query-227b6d1fbad202d344e2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-9a25bb812279972da5f2"></a>

**270° CCW: unverified** — `in_game_route_query-9a25bb812279972da5f2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-113c1593c347b43e4c59"></a>

**0° CCW: unverified** — `in_game_route_query-113c1593c347b43e4c59`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-cdacebe32ae872f8ee60"></a>

**90° CCW: unverified** — `in_game_route_query-cdacebe32ae872f8ee60`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-35621915078e648f50dd"></a>

**180° CCW: unverified** — `in_game_route_query-35621915078e648f50dd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-22fa1c2a6f77440332d1"></a>

**270° CCW: unverified** — `in_game_route_query-22fa1c2a6f77440332d1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-0e2c29e55dfa92a72768"></a>

**0° CCW: unverified** — `in_game_route_query-0e2c29e55dfa92a72768`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-6ad4ffc2ac133310293c"></a>

**90° CCW: unverified** — `in_game_route_query-6ad4ffc2ac133310293c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-0bf5ad1e159cfce1303e"></a>

**180° CCW: unverified** — `in_game_route_query-0bf5ad1e159cfce1303e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-f7cd4f70272f51a3d8aa"></a>

**270° CCW: unverified** — `in_game_route_query-f7cd4f70272f51a3d8aa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-c5ae8754c045ab810c67"></a>

**0° CCW: unverified** — `in_game_route_query-c5ae8754c045ab810c67`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-45130db8399a5da34d05"></a>

**90° CCW: unverified** — `in_game_route_query-45130db8399a5da34d05`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-e134a90b0757d5303875"></a>

**180° CCW: unverified** — `in_game_route_query-e134a90b0757d5303875`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-cb6d62ba4bf28c652f77"></a>

**270° CCW: unverified** — `in_game_route_query-cb6d62ba4bf28c652f77`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-07827aee91f293cf5267"></a>

**0° CCW: unverified** — `in_game_route_query-07827aee91f293cf5267`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-f3a95aaf4ae7b486e92a"></a>

**90° CCW: unverified** — `in_game_route_query-f3a95aaf4ae7b486e92a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-8457f3ab5c3a79477964"></a>

**180° CCW: unverified** — `in_game_route_query-8457f3ab5c3a79477964`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-5710c72fc92beff2059d"></a>

**270° CCW: unverified** — `in_game_route_query-5710c72fc92beff2059d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-de4761b284e2fef340ee"></a>

**0° CCW: unverified** — `in_game_route_query-de4761b284e2fef340ee`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-79abae856ccd062af09a"></a>

**90° CCW: unverified** — `in_game_route_query-79abae856ccd062af09a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-daa2c23a5bc68c727e91"></a>

**180° CCW: unverified** — `in_game_route_query-daa2c23a5bc68c727e91`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-b2faf053ecd3df9530b9"></a>

**270° CCW: unverified** — `in_game_route_query-b2faf053ecd3df9530b9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-6109f5bbccb43a432b4c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e9025b8c9020c5bfe29b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-227b6d1fbad202d344e2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9a25bb812279972da5f2">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-113c1593c347b43e4c59">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cdacebe32ae872f8ee60">[ ] unverified</a> | <a href="#case-in_game_visible_travel-35621915078e648f50dd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-22fa1c2a6f77440332d1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-0e2c29e55dfa92a72768">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6ad4ffc2ac133310293c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0bf5ad1e159cfce1303e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f7cd4f70272f51a3d8aa">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-c5ae8754c045ab810c67">[ ] unverified</a> | <a href="#case-in_game_visible_travel-45130db8399a5da34d05">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e134a90b0757d5303875">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cb6d62ba4bf28c652f77">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-07827aee91f293cf5267">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f3a95aaf4ae7b486e92a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8457f3ab5c3a79477964">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5710c72fc92beff2059d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-de4761b284e2fef340ee">[ ] unverified</a> | <a href="#case-in_game_visible_travel-79abae856ccd062af09a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-daa2c23a5bc68c727e91">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b2faf053ecd3df9530b9">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-6109f5bbccb43a432b4c"></a>

**0° CCW: unverified** — `in_game_visible_travel-6109f5bbccb43a432b4c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-e9025b8c9020c5bfe29b"></a>

**90° CCW: unverified** — `in_game_visible_travel-e9025b8c9020c5bfe29b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-227b6d1fbad202d344e2"></a>

**180° CCW: unverified** — `in_game_visible_travel-227b6d1fbad202d344e2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-9a25bb812279972da5f2"></a>

**270° CCW: unverified** — `in_game_visible_travel-9a25bb812279972da5f2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-113c1593c347b43e4c59"></a>

**0° CCW: unverified** — `in_game_visible_travel-113c1593c347b43e4c59`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-cdacebe32ae872f8ee60"></a>

**90° CCW: unverified** — `in_game_visible_travel-cdacebe32ae872f8ee60`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-35621915078e648f50dd"></a>

**180° CCW: unverified** — `in_game_visible_travel-35621915078e648f50dd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-22fa1c2a6f77440332d1"></a>

**270° CCW: unverified** — `in_game_visible_travel-22fa1c2a6f77440332d1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-12-out; entry: channel-02-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-0e2c29e55dfa92a72768"></a>

**0° CCW: unverified** — `in_game_visible_travel-0e2c29e55dfa92a72768`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-6ad4ffc2ac133310293c"></a>

**90° CCW: unverified** — `in_game_visible_travel-6ad4ffc2ac133310293c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-0bf5ad1e159cfce1303e"></a>

**180° CCW: unverified** — `in_game_visible_travel-0bf5ad1e159cfce1303e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-f7cd4f70272f51a3d8aa"></a>

**270° CCW: unverified** — `in_game_visible_travel-f7cd4f70272f51a3d8aa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-c5ae8754c045ab810c67"></a>

**0° CCW: unverified** — `in_game_visible_travel-c5ae8754c045ab810c67`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-45130db8399a5da34d05"></a>

**90° CCW: unverified** — `in_game_visible_travel-45130db8399a5da34d05`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-e134a90b0757d5303875"></a>

**180° CCW: unverified** — `in_game_visible_travel-e134a90b0757d5303875`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-cb6d62ba4bf28c652f77"></a>

**270° CCW: unverified** — `in_game_visible_travel-cb6d62ba4bf28c652f77`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-10-out; entry: channel-04-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-07827aee91f293cf5267"></a>

**0° CCW: unverified** — `in_game_visible_travel-07827aee91f293cf5267`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-f3a95aaf4ae7b486e92a"></a>

**90° CCW: unverified** — `in_game_visible_travel-f3a95aaf4ae7b486e92a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-8457f3ab5c3a79477964"></a>

**180° CCW: unverified** — `in_game_visible_travel-8457f3ab5c3a79477964`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-5710c72fc92beff2059d"></a>

**270° CCW: unverified** — `in_game_visible_travel-5710c72fc92beff2059d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-09-out; entry: channel-05-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-de4761b284e2fef340ee"></a>

**0° CCW: unverified** — `in_game_visible_travel-de4761b284e2fef340ee`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-79abae856ccd062af09a"></a>

**90° CCW: unverified** — `in_game_visible_travel-79abae856ccd062af09a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-daa2c23a5bc68c727e91"></a>

**180° CCW: unverified** — `in_game_visible_travel-daa2c23a5bc68c727e91`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-b2faf053ecd3df9530b9"></a>

**270° CCW: unverified** — `in_game_visible_travel-b2faf053ecd3df9530b9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-08-out; entry: channel-06-in; exit: channel-08-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 120 cases; unverified: 120</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd2ffb9ff0be8f4d9199">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf232555de23c66013d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d53f5778e835a00222c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27482162778ca93d7b3a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b78de417e29fadd1de84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1aaad88d64db2947f349">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-760f7d30e7c6f854d2c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35c905c58f5f1cc6605c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-153eaf778dcfeeee2573">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad3355ae814535260d93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cceb19f4a6e647473c88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-713c5b3c3e79783c41c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-85a8ffd8b41fda3fb9b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6d1a506a7074d002c2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bdadb21e54c3b9b59d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f6b8749802dd03b8abe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ea09be2ee1003a42786b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b45a7f72947d4a626b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f65bcf6d88bc917781a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e5b6fd93694603657cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-884ddec345bb2a60fed2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-601aebe877d16e440908">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd82d2766fc9f725967b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fff6b734abc87dcbd90">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-88fd231939e2e3bbbca2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dcde106a552bd9fa93ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f486ff88c2c773b73a1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-efcf4cc5137b6b181a2e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6714111effcab1d1e345">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d69deb7dc7ddfffeec19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7ea2e6ef67eef538a69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92f50c2122615bb992f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46cdd2bbc752602f142d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-603b18c98fa164ed71ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bcffdae30e8845b459b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a8a0a786792d464814a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-02fc375a1fff09c6b6eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b7e17e108201706cee7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b069033e918a3c023560">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-619b2a9102b619eaacc0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca354d4b5797f6e1f4e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5d2b33104ae234d490f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e8255ec237ebc288e8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f091ff21b38d2fcbe73">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be3b86db48f289dbe9a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-791522b9f33395fd0627">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b23fdbdd0bb43734b4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc0be9d7f6f00c13007a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7b1437175a882ea04c2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d04df7b516bb99936b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdee14b0c0e8d56b52d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28e52489607c96dad674">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0c2e6923ecf8138b8766">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-daab4c8fc7c09023073c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65c1b4a907641e882361">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c59b8a9aa7bdad5a206">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be6d76ce88e7d175135a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3812c9940626b80d33f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07dae20620f315b06b19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4880e50cc2258002bc66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad70236c87933a26ea29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d747342df5882175842c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d36fa4e2e3562781104">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc4e311a4c276285cf17">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f1d61ea758b1271e52ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-627aa67c26189941dbae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2294e13520c063b6bf15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-efce131d6ec01b1ac9f2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-77be9599501353f3c6db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7097f1755cfbe46e124b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc5d262e9899ad122995">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd468fedb391df793dd6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-944e41954ce485f44b63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dff448a743f53a6c4897">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f67700f5baaf949f127">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e90b7c552041b695162d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-85341f7d95c57435ac57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66cf8ad3ab00a4f42cb1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-730e36c65ff8332eeca2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8df4c814839f102459d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-06161d146c98dedf0ffd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6a604870d931c021654">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03513669bed4ddfc4c9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-feca4a8efbe779f19f82">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-986cab59b6b008c49098">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-153c4ddf9b770edfdec2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78edb4c8c03db3882145">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5db7dda27ba7b199f355">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0dd9fda6cad85da3db62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6775544c077c186ce28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ca1e55e2a3424e91cce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10870e7db299550da613">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a60497bee3cf3b04690">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d47b92824f4c1d21a28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-654c339b9d0ecbf8a83b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d95317a1285b7b2b9a09">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9d9f748919a189cf43b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3851e39229b791b0846b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e635e2434cccbcdd565">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98be7eccfe1dd1b90950">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-62d451841e35dcba2bd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7bf2fe8436b451d65ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-daca4e2682de69947297">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa8669792b12b83aab0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-72b25bd2504a8ffd0b54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa326c41b6509d1606ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-efb6e2f8fa21f9f8c27c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c4d8c702ae0ec804e63">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2c5be3266b9bbc61057">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-053b42a5496f716672ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d155da335b217b77c0e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08c008ab65a1f60d82fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-704f77a6e1eb3b945aec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca8d87d9350da3831b0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4715e895036d8c347194">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-214316afafbcfad6968b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f70a3cea6cf377724351">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d58fc6b86abd6511609">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24b73a3e79708664d4e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6c51ddb41debfcc73ae">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd2ffb9ff0be8f4d9199"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd2ffb9ff0be8f4d9199`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf232555de23c66013d9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf232555de23c66013d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d53f5778e835a00222c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d53f5778e835a00222c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27482162778ca93d7b3a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27482162778ca93d7b3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b78de417e29fadd1de84"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b78de417e29fadd1de84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1aaad88d64db2947f349"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1aaad88d64db2947f349`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-760f7d30e7c6f854d2c3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-760f7d30e7c6f854d2c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35c905c58f5f1cc6605c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-35c905c58f5f1cc6605c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-153eaf778dcfeeee2573"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-153eaf778dcfeeee2573`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad3355ae814535260d93"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ad3355ae814535260d93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cceb19f4a6e647473c88"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cceb19f4a6e647473c88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-713c5b3c3e79783c41c7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-713c5b3c3e79783c41c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-85a8ffd8b41fda3fb9b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-85a8ffd8b41fda3fb9b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6d1a506a7074d002c2a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a6d1a506a7074d002c2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bdadb21e54c3b9b59d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8bdadb21e54c3b9b59d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f6b8749802dd03b8abe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f6b8749802dd03b8abe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ea09be2ee1003a42786b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ea09be2ee1003a42786b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b45a7f72947d4a626b9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b45a7f72947d4a626b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f65bcf6d88bc917781a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f65bcf6d88bc917781a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e5b6fd93694603657cb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5e5b6fd93694603657cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-884ddec345bb2a60fed2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-884ddec345bb2a60fed2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-601aebe877d16e440908"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-601aebe877d16e440908`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd82d2766fc9f725967b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dd82d2766fc9f725967b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fff6b734abc87dcbd90"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1fff6b734abc87dcbd90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-88fd231939e2e3bbbca2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-88fd231939e2e3bbbca2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dcde106a552bd9fa93ee"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dcde106a552bd9fa93ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f486ff88c2c773b73a1d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f486ff88c2c773b73a1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-efcf4cc5137b6b181a2e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-efcf4cc5137b6b181a2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6714111effcab1d1e345"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6714111effcab1d1e345`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d69deb7dc7ddfffeec19"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d69deb7dc7ddfffeec19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7ea2e6ef67eef538a69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b7ea2e6ef67eef538a69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92f50c2122615bb992f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92f50c2122615bb992f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46cdd2bbc752602f142d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46cdd2bbc752602f142d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-603b18c98fa164ed71ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-603b18c98fa164ed71ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bcffdae30e8845b459b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5bcffdae30e8845b459b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a8a0a786792d464814a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a8a0a786792d464814a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-02fc375a1fff09c6b6eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-02fc375a1fff09c6b6eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b7e17e108201706cee7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b7e17e108201706cee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b069033e918a3c023560"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b069033e918a3c023560`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-619b2a9102b619eaacc0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-619b2a9102b619eaacc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca354d4b5797f6e1f4e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca354d4b5797f6e1f4e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5d2b33104ae234d490f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b5d2b33104ae234d490f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e8255ec237ebc288e8b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9e8255ec237ebc288e8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f091ff21b38d2fcbe73"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f091ff21b38d2fcbe73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be3b86db48f289dbe9a3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be3b86db48f289dbe9a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-791522b9f33395fd0627"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-791522b9f33395fd0627`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b23fdbdd0bb43734b4a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3b23fdbdd0bb43734b4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc0be9d7f6f00c13007a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc0be9d7f6f00c13007a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7b1437175a882ea04c2a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7b1437175a882ea04c2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d04df7b516bb99936b9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d04df7b516bb99936b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdee14b0c0e8d56b52d5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cdee14b0c0e8d56b52d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28e52489607c96dad674"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-28e52489607c96dad674`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0c2e6923ecf8138b8766"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c2e6923ecf8138b8766`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-daab4c8fc7c09023073c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-daab4c8fc7c09023073c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65c1b4a907641e882361"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65c1b4a907641e882361`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c59b8a9aa7bdad5a206"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2c59b8a9aa7bdad5a206`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be6d76ce88e7d175135a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be6d76ce88e7d175135a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3812c9940626b80d33f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c3812c9940626b80d33f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07dae20620f315b06b19"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-07dae20620f315b06b19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4880e50cc2258002bc66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4880e50cc2258002bc66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad70236c87933a26ea29"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad70236c87933a26ea29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d747342df5882175842c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d747342df5882175842c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d36fa4e2e3562781104"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d36fa4e2e3562781104`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc4e311a4c276285cf17"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bc4e311a4c276285cf17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f1d61ea758b1271e52ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f1d61ea758b1271e52ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-627aa67c26189941dbae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-627aa67c26189941dbae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2294e13520c063b6bf15"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2294e13520c063b6bf15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-efce131d6ec01b1ac9f2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-efce131d6ec01b1ac9f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-77be9599501353f3c6db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-77be9599501353f3c6db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7097f1755cfbe46e124b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7097f1755cfbe46e124b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc5d262e9899ad122995"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fc5d262e9899ad122995`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd468fedb391df793dd6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dd468fedb391df793dd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-944e41954ce485f44b63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-944e41954ce485f44b63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dff448a743f53a6c4897"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dff448a743f53a6c4897`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f67700f5baaf949f127"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7f67700f5baaf949f127`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e90b7c552041b695162d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e90b7c552041b695162d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-85341f7d95c57435ac57"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-85341f7d95c57435ac57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66cf8ad3ab00a4f42cb1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-66cf8ad3ab00a4f42cb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-730e36c65ff8332eeca2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-730e36c65ff8332eeca2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8df4c814839f102459d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a8df4c814839f102459d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-06161d146c98dedf0ffd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-06161d146c98dedf0ffd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6a604870d931c021654"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b6a604870d931c021654`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03513669bed4ddfc4c9c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03513669bed4ddfc4c9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-feca4a8efbe779f19f82"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-feca4a8efbe779f19f82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-986cab59b6b008c49098"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-986cab59b6b008c49098`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-153c4ddf9b770edfdec2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-153c4ddf9b770edfdec2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78edb4c8c03db3882145"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78edb4c8c03db3882145`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5db7dda27ba7b199f355"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5db7dda27ba7b199f355`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0dd9fda6cad85da3db62"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0dd9fda6cad85da3db62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6775544c077c186ce28"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b6775544c077c186ce28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ca1e55e2a3424e91cce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ca1e55e2a3424e91cce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10870e7db299550da613"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10870e7db299550da613`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a60497bee3cf3b04690"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a60497bee3cf3b04690`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d47b92824f4c1d21a28"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2d47b92824f4c1d21a28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-654c339b9d0ecbf8a83b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-654c339b9d0ecbf8a83b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d95317a1285b7b2b9a09"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d95317a1285b7b2b9a09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9d9f748919a189cf43b0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9d9f748919a189cf43b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3851e39229b791b0846b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3851e39229b791b0846b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e635e2434cccbcdd565"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2e635e2434cccbcdd565`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98be7eccfe1dd1b90950"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-98be7eccfe1dd1b90950`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-62d451841e35dcba2bd6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-62d451841e35dcba2bd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7bf2fe8436b451d65ad"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a7bf2fe8436b451d65ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-daca4e2682de69947297"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-daca4e2682de69947297`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa8669792b12b83aab0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa8669792b12b83aab0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-72b25bd2504a8ffd0b54"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-72b25bd2504a8ffd0b54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa326c41b6509d1606ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa326c41b6509d1606ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-efb6e2f8fa21f9f8c27c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-efb6e2f8fa21f9f8c27c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c4d8c702ae0ec804e63"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c4d8c702ae0ec804e63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2c5be3266b9bbc61057"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2c5be3266b9bbc61057`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-053b42a5496f716672ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-053b42a5496f716672ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d155da335b217b77c0e6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d155da335b217b77c0e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08c008ab65a1f60d82fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-08c008ab65a1f60d82fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-704f77a6e1eb3b945aec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-704f77a6e1eb3b945aec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca8d87d9350da3831b0d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ca8d87d9350da3831b0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4715e895036d8c347194"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4715e895036d8c347194`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-214316afafbcfad6968b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-214316afafbcfad6968b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f70a3cea6cf377724351"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f70a3cea6cf377724351`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d58fc6b86abd6511609"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d58fc6b86abd6511609`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24b73a3e79708664d4e5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-24b73a3e79708664d4e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6c51ddb41debfcc73ae"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6c51ddb41debfcc73ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-grade:canonical-southeast | <a href="#case-preview_review-354b95742e3793f77b69">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-grade:canonical-top | <a href="#case-preview_review-f3e76a94ea14c252f45b">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-grade:connection-overview | <a href="#case-preview_review-c5afc5db1358250972c0">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-grade:canonical-southeast</summary>

<a id="case-preview_review-354b95742e3793f77b69"></a>

**General: unverified** — `preview_review-354b95742e3793f77b69`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-grade:canonical-top</summary>

<a id="case-preview_review-f3e76a94ea14c252f45b"></a>

**General: unverified** — `preview_review-f3e76a94ea14c252f45b`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-grade:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-grade:connection-overview</summary>

<a id="case-preview_review-c5afc5db1358250972c0"></a>

**General: unverified** — `preview_review-c5afc5db1358250972c0`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-grade:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the grade function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
