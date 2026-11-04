---
title: "Testing: RHW Ramp \u2014 L2 Entry Parallel Grade \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L2 Entry Parallel Grade — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **RHW Ramp — L2 Entry Parallel Grade — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-upper-entry-grade`, as **P15** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 3 cells inside its 3 × 2 bounding footprint. Physical grade between 15 m and 0 m; actual cell-edge ports have their own measured intermediate heights. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-07-out` | road / 1 / primary | out | [-8.0, -19.2, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -19.2, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-08-out` | road / 1 / primary | out | [-8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-03-in` | road / 1 / primary | in | [-3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-09-out` | road / 1 / primary | out | [-3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-04-in` | road / 1 / primary | in | [0.970563, -24.0, 0.489958]; [0.7071067811865476, 0.7071067811865476]; 0.282029333 | `path-interface-0c5a35d75bc5b6dfb609` |
| `channel-05-in` | road / 1 / primary | in | [3.2, -8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-10-out` | road / 1 / primary | out | [3.2, -8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-11-out` | road / 1 / primary | out | [16.970563, -8.0, 6.871553]; [0.7071067811865476, 0.7071067811865476]; 0.282029319 | `path-interface-3c3a1e090aa258f38443` |
| `channel-06-in` | road / 1 / primary | in | [24.0, -0.970563, 9.675242]; [0.7071067811865476, 0.7071067811865476]; 0.282029323 | `path-interface-faa05cf1692a3270eed8` |
| `channel-12-out` | road / 1 / primary | out | [32.970563, 8.0, 13.253148]; [0.7071067811865476, 0.7071067811865476]; 0.282029195 | `path-interface-765b9df16671d9826fa4` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-10-out` | primary |
| road | `channel-02-in` → `channel-09-out` | primary |
| road | `channel-03-in` → `channel-08-out` | primary |
| road | `channel-04-in` → `channel-11-out` | primary |
| road | `channel-05-in` → `channel-07-out` | primary |
| road | `channel-06-in` → `channel-12-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-upper-entry-grade
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **10,050 indexed triangles** and **7 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-entry-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-entry-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-1934396b4f14a6c9f18e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-1934396b4f14a6c9f18e"></a>

**General: unverified** — `software_resources-1934396b4f14a6c9f18e`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-1934396b4f14a6c9f18e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-1934396b4f14a6c9f18e"></a>

**General: unverified** — `software_connectivity-1934396b4f14a6c9f18e`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-a4ae690c50aff3ee8c32">[ ] unverified</a> | <a href="#case-in_game_render-5942aad954db902dab7d">[ ] unverified</a> | <a href="#case-in_game_render-02077d16cc44e6980cba">[ ] unverified</a> | <a href="#case-in_game_render-050630b1c0afb028dc73">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-a4ae690c50aff3ee8c32"></a>

**0° CCW: unverified** — `in_game_render-a4ae690c50aff3ee8c32`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5942aad954db902dab7d"></a>

**90° CCW: unverified** — `in_game_render-5942aad954db902dab7d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-02077d16cc44e6980cba"></a>

**180° CCW: unverified** — `in_game_render-02077d16cc44e6980cba`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-050630b1c0afb028dc73"></a>

**270° CCW: unverified** — `in_game_render-050630b1c0afb028dc73`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-a4ae690c50aff3ee8c32">[ ] unverified</a> | <a href="#case-in_game_placement-5942aad954db902dab7d">[ ] unverified</a> | <a href="#case-in_game_placement-02077d16cc44e6980cba">[ ] unverified</a> | <a href="#case-in_game_placement-050630b1c0afb028dc73">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-a4ae690c50aff3ee8c32"></a>

**0° CCW: unverified** — `in_game_placement-a4ae690c50aff3ee8c32`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5942aad954db902dab7d"></a>

**90° CCW: unverified** — `in_game_placement-5942aad954db902dab7d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-02077d16cc44e6980cba"></a>

**180° CCW: unverified** — `in_game_placement-02077d16cc44e6980cba`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-050630b1c0afb028dc73"></a>

**270° CCW: unverified** — `in_game_placement-050630b1c0afb028dc73`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-a4ae690c50aff3ee8c32">[ ] unverified</a> | <a href="#case-in_game_demolition-5942aad954db902dab7d">[ ] unverified</a> | <a href="#case-in_game_demolition-02077d16cc44e6980cba">[ ] unverified</a> | <a href="#case-in_game_demolition-050630b1c0afb028dc73">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-a4ae690c50aff3ee8c32"></a>

**0° CCW: unverified** — `in_game_demolition-a4ae690c50aff3ee8c32`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5942aad954db902dab7d"></a>

**90° CCW: unverified** — `in_game_demolition-5942aad954db902dab7d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-02077d16cc44e6980cba"></a>

**180° CCW: unverified** — `in_game_demolition-02077d16cc44e6980cba`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-050630b1c0afb028dc73"></a>

**270° CCW: unverified** — `in_game_demolition-050630b1c0afb028dc73`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-a4ae690c50aff3ee8c32">[ ] unverified</a> | <a href="#case-in_game_save_reload-5942aad954db902dab7d">[ ] unverified</a> | <a href="#case-in_game_save_reload-02077d16cc44e6980cba">[ ] unverified</a> | <a href="#case-in_game_save_reload-050630b1c0afb028dc73">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-a4ae690c50aff3ee8c32"></a>

**0° CCW: unverified** — `in_game_save_reload-a4ae690c50aff3ee8c32`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5942aad954db902dab7d"></a>

**90° CCW: unverified** — `in_game_save_reload-5942aad954db902dab7d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-02077d16cc44e6980cba"></a>

**180° CCW: unverified** — `in_game_save_reload-02077d16cc44e6980cba`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-050630b1c0afb028dc73"></a>

**270° CCW: unverified** — `in_game_save_reload-050630b1c0afb028dc73`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-c6ed5787adc0d320bfe7">[ ] unverified</a> | <a href="#case-in_game_route_query-f65953f57000fe4e4965">[ ] unverified</a> | <a href="#case-in_game_route_query-8ddb0aad8e7a6361b5b9">[ ] unverified</a> | <a href="#case-in_game_route_query-21b51fb2f0f915656d1b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-f880f87bfb94c76cfbc6">[ ] unverified</a> | <a href="#case-in_game_route_query-6e84962d3710b7eab0a0">[ ] unverified</a> | <a href="#case-in_game_route_query-e038ed4f33f19ed15c5d">[ ] unverified</a> | <a href="#case-in_game_route_query-7eca2e11de005c8129d3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-51a3f802ca067c76d0cd">[ ] unverified</a> | <a href="#case-in_game_route_query-98805a063c8fd58b8614">[ ] unverified</a> | <a href="#case-in_game_route_query-37aa533a9a49dc20abb1">[ ] unverified</a> | <a href="#case-in_game_route_query-f2c04d77354ef436b495">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-3a73632d07d3d345d116">[ ] unverified</a> | <a href="#case-in_game_route_query-5ad106c452ec1fce7234">[ ] unverified</a> | <a href="#case-in_game_route_query-0f8f456815129b954910">[ ] unverified</a> | <a href="#case-in_game_route_query-3135ee47684577a68b3e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-2337a652e855fe2f2448">[ ] unverified</a> | <a href="#case-in_game_route_query-eb715fe5c9929cfae469">[ ] unverified</a> | <a href="#case-in_game_route_query-b1e07a4cdb10a2956d7c">[ ] unverified</a> | <a href="#case-in_game_route_query-a1876b1d2d1e783532bf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-75e547b0bcf8bcf29de9">[ ] unverified</a> | <a href="#case-in_game_route_query-f0ef6a8e4a588739d2fa">[ ] unverified</a> | <a href="#case-in_game_route_query-44d1dec807f9a70b73df">[ ] unverified</a> | <a href="#case-in_game_route_query-48b6caa9efb3b7248799">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-c6ed5787adc0d320bfe7"></a>

**0° CCW: unverified** — `in_game_route_query-c6ed5787adc0d320bfe7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-f65953f57000fe4e4965"></a>

**90° CCW: unverified** — `in_game_route_query-f65953f57000fe4e4965`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-8ddb0aad8e7a6361b5b9"></a>

**180° CCW: unverified** — `in_game_route_query-8ddb0aad8e7a6361b5b9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-21b51fb2f0f915656d1b"></a>

**270° CCW: unverified** — `in_game_route_query-21b51fb2f0f915656d1b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-f880f87bfb94c76cfbc6"></a>

**0° CCW: unverified** — `in_game_route_query-f880f87bfb94c76cfbc6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-6e84962d3710b7eab0a0"></a>

**90° CCW: unverified** — `in_game_route_query-6e84962d3710b7eab0a0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-e038ed4f33f19ed15c5d"></a>

**180° CCW: unverified** — `in_game_route_query-e038ed4f33f19ed15c5d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-7eca2e11de005c8129d3"></a>

**270° CCW: unverified** — `in_game_route_query-7eca2e11de005c8129d3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-51a3f802ca067c76d0cd"></a>

**0° CCW: unverified** — `in_game_route_query-51a3f802ca067c76d0cd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-98805a063c8fd58b8614"></a>

**90° CCW: unverified** — `in_game_route_query-98805a063c8fd58b8614`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-37aa533a9a49dc20abb1"></a>

**180° CCW: unverified** — `in_game_route_query-37aa533a9a49dc20abb1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-f2c04d77354ef436b495"></a>

**270° CCW: unverified** — `in_game_route_query-f2c04d77354ef436b495`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-3a73632d07d3d345d116"></a>

**0° CCW: unverified** — `in_game_route_query-3a73632d07d3d345d116`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-5ad106c452ec1fce7234"></a>

**90° CCW: unverified** — `in_game_route_query-5ad106c452ec1fce7234`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-0f8f456815129b954910"></a>

**180° CCW: unverified** — `in_game_route_query-0f8f456815129b954910`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-3135ee47684577a68b3e"></a>

**270° CCW: unverified** — `in_game_route_query-3135ee47684577a68b3e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-2337a652e855fe2f2448"></a>

**0° CCW: unverified** — `in_game_route_query-2337a652e855fe2f2448`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-eb715fe5c9929cfae469"></a>

**90° CCW: unverified** — `in_game_route_query-eb715fe5c9929cfae469`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-b1e07a4cdb10a2956d7c"></a>

**180° CCW: unverified** — `in_game_route_query-b1e07a4cdb10a2956d7c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-a1876b1d2d1e783532bf"></a>

**270° CCW: unverified** — `in_game_route_query-a1876b1d2d1e783532bf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-75e547b0bcf8bcf29de9"></a>

**0° CCW: unverified** — `in_game_route_query-75e547b0bcf8bcf29de9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-f0ef6a8e4a588739d2fa"></a>

**90° CCW: unverified** — `in_game_route_query-f0ef6a8e4a588739d2fa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-44d1dec807f9a70b73df"></a>

**180° CCW: unverified** — `in_game_route_query-44d1dec807f9a70b73df`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-48b6caa9efb3b7248799"></a>

**270° CCW: unverified** — `in_game_route_query-48b6caa9efb3b7248799`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-c6ed5787adc0d320bfe7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f65953f57000fe4e4965">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8ddb0aad8e7a6361b5b9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-21b51fb2f0f915656d1b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-f880f87bfb94c76cfbc6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6e84962d3710b7eab0a0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e038ed4f33f19ed15c5d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7eca2e11de005c8129d3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-51a3f802ca067c76d0cd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-98805a063c8fd58b8614">[ ] unverified</a> | <a href="#case-in_game_visible_travel-37aa533a9a49dc20abb1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f2c04d77354ef436b495">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-3a73632d07d3d345d116">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5ad106c452ec1fce7234">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0f8f456815129b954910">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3135ee47684577a68b3e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-2337a652e855fe2f2448">[ ] unverified</a> | <a href="#case-in_game_visible_travel-eb715fe5c9929cfae469">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b1e07a4cdb10a2956d7c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a1876b1d2d1e783532bf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-75e547b0bcf8bcf29de9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f0ef6a8e4a588739d2fa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-44d1dec807f9a70b73df">[ ] unverified</a> | <a href="#case-in_game_visible_travel-48b6caa9efb3b7248799">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-c6ed5787adc0d320bfe7"></a>

**0° CCW: unverified** — `in_game_visible_travel-c6ed5787adc0d320bfe7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-f65953f57000fe4e4965"></a>

**90° CCW: unverified** — `in_game_visible_travel-f65953f57000fe4e4965`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-8ddb0aad8e7a6361b5b9"></a>

**180° CCW: unverified** — `in_game_visible_travel-8ddb0aad8e7a6361b5b9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-21b51fb2f0f915656d1b"></a>

**270° CCW: unverified** — `in_game_visible_travel-21b51fb2f0f915656d1b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-f880f87bfb94c76cfbc6"></a>

**0° CCW: unverified** — `in_game_visible_travel-f880f87bfb94c76cfbc6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-6e84962d3710b7eab0a0"></a>

**90° CCW: unverified** — `in_game_visible_travel-6e84962d3710b7eab0a0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-e038ed4f33f19ed15c5d"></a>

**180° CCW: unverified** — `in_game_visible_travel-e038ed4f33f19ed15c5d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-7eca2e11de005c8129d3"></a>

**270° CCW: unverified** — `in_game_visible_travel-7eca2e11de005c8129d3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-51a3f802ca067c76d0cd"></a>

**0° CCW: unverified** — `in_game_visible_travel-51a3f802ca067c76d0cd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-98805a063c8fd58b8614"></a>

**90° CCW: unverified** — `in_game_visible_travel-98805a063c8fd58b8614`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-37aa533a9a49dc20abb1"></a>

**180° CCW: unverified** — `in_game_visible_travel-37aa533a9a49dc20abb1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-f2c04d77354ef436b495"></a>

**270° CCW: unverified** — `in_game_visible_travel-f2c04d77354ef436b495`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-3a73632d07d3d345d116"></a>

**0° CCW: unverified** — `in_game_visible_travel-3a73632d07d3d345d116`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-5ad106c452ec1fce7234"></a>

**90° CCW: unverified** — `in_game_visible_travel-5ad106c452ec1fce7234`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-0f8f456815129b954910"></a>

**180° CCW: unverified** — `in_game_visible_travel-0f8f456815129b954910`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-3135ee47684577a68b3e"></a>

**270° CCW: unverified** — `in_game_visible_travel-3135ee47684577a68b3e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-11-out; entry: channel-04-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-2337a652e855fe2f2448"></a>

**0° CCW: unverified** — `in_game_visible_travel-2337a652e855fe2f2448`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-eb715fe5c9929cfae469"></a>

**90° CCW: unverified** — `in_game_visible_travel-eb715fe5c9929cfae469`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-b1e07a4cdb10a2956d7c"></a>

**180° CCW: unverified** — `in_game_visible_travel-b1e07a4cdb10a2956d7c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-a1876b1d2d1e783532bf"></a>

**270° CCW: unverified** — `in_game_visible_travel-a1876b1d2d1e783532bf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-75e547b0bcf8bcf29de9"></a>

**0° CCW: unverified** — `in_game_visible_travel-75e547b0bcf8bcf29de9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-f0ef6a8e4a588739d2fa"></a>

**90° CCW: unverified** — `in_game_visible_travel-f0ef6a8e4a588739d2fa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-44d1dec807f9a70b73df"></a>

**180° CCW: unverified** — `in_game_visible_travel-44d1dec807f9a70b73df`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-48b6caa9efb3b7248799"></a>

**270° CCW: unverified** — `in_game_visible_travel-48b6caa9efb3b7248799`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-12-out; entry: channel-06-in; exit: channel-12-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 120 cases; unverified: 120</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-78f256bf952b8fca10e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-715b5c2d3c84eb16898c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c886572f369ebb30f95a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d1ebceffff018cc5c8b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6601fc7fbb202bdf60b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c0dc21aaa837e7053da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2d992d58596d64f3d83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15b97eef9255fb45cccd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4be11ac3caaad789ae8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b81b6830dd09d1ffa79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a42e18313b207ccdafad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-088b53ac30d4585e1f9e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-17ea5ab92f31d666db45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ed429f1c960cef07286">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29d78463f9e74b7b162b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45cccf9c0fb24b50ad2c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-255a76c0bb2e3b132af4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83980e40ec6781f41711">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-baf71d54338c988ec2ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbccca9dd69886594c38">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e20bae55a25f61127ff0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef690af192bd603b0466">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f46940be244e0c50343">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a362664b3369773221a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a1fbcb8d99d6f019c85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2705c3df9d8741d83e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a187ff22060891eb54a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d2b7d54e1a669bdb891">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c170569b71e8b0c9b2e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7f86e6e65772340b64e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d349b1db025857c360a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3476d4b093a54b2060a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4308de265fe58bcb429">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8f1348b73ce31cc549e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d2b7cfb229276d5ddf6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5abb917bc9d80dbe3bd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fe9778c69fc4ae8b5fca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73fa0e28027b5284eb8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5886cbe0f47cad1b459b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91a683ce13384e8d49e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-889fa9dd52378dde5cd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22e6674cc51a60db498b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5989d9e1439ec4ec4233">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e67009aabc0d3f6ab69b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c145116de015174e036">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09c9abbdd10df56ff0f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83e3b22c0dfe289b47fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e01bcfaf6a98fccde6e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-50302fea8fa125eaf0dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ddc498ba3454f550455">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5490e4480e7e2200d937">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39b0bf80cbc4b8bd4c3e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ef5296a4f740c7c46754">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36178a99d7e402ca0495">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c8b263885f4f2fe3d91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-774cca0ac4c5a90d84f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e6b7f2142b8b678a606">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b0b12a27c6510460695">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a61ac88bfe2f30eb3753">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7662e23c7cc913825978">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f6ac3ce249d4c7ee0816">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6fd8ea3783f09f59148">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8be78fbd83450dae874f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac683e8eb4e83eb69dd0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-042a69751ceca1aed582">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31bd0168aa1cedd0f6bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14ba18a53d1cb57573ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3ba1e9eb9e0a4134710">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4e44125b1149a50e9b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b26a9c8c3840e4ee6e00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37d77f627a87170a3710">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d7ec8d333079c7a164b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f637e35e3bdd7269b4c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7b2eaeab55cea6f4d1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffd0b10cb411424da52b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cedb32e9c532d9553632">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c943912b676e46f77984">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a615431250a7d9dbc5d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85e60772d215c91754a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f026f3893b1b22245bc5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c232a10531df4ab2f843">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-610d4152248bc40fbd69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86012bce8aa88c1082f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cf4d2e97ff2bb55a3b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0c964109d1f9c6368559">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f1d15912d1bdb0c5b39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c32df5a274896b153a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c711be90182d356f933a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3828f671a8e8fa25ca92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1d8f8749e972dd56674">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9ab5ba366e73b9e2b04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-028f8d440bd3e7d703a5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a849f332698d35368f6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddb1277804843b8e99a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66765b1e359348dd4868">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-378c189fd844f39e50f0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d8ce18ac2d1ca0d07abf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-caf672d37a7f152a4b1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d125d6c6af54d9f44f94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f6960a243c99307ede5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc132acd026941825c7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04bab40868e8b515ff14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00995c5f9328e2ed902e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7984cfd65ec18c153afd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-37c4519c10456ab2642e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5431030ffef1c41fa9c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97ba805dc76115f96969">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b9571162a4a26ff1b54">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a08f27909278b2342700">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5de234adacb4040ff3b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-154cb9d90c546dd58049">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-043b60f8288766a1e831">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2f638eed47fc1518ca96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a6861e6837dc0a450b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e21c9ea6324a91859e3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c59ce55cf7edba68939">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-deb9b02e1b507a17535d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-126d655530ef531ccb8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-860b67e90f119a621033">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd946b554fd12488bfc1">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-78f256bf952b8fca10e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-78f256bf952b8fca10e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-715b5c2d3c84eb16898c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-715b5c2d3c84eb16898c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c886572f369ebb30f95a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c886572f369ebb30f95a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d1ebceffff018cc5c8b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d1ebceffff018cc5c8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6601fc7fbb202bdf60b8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6601fc7fbb202bdf60b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c0dc21aaa837e7053da"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6c0dc21aaa837e7053da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2d992d58596d64f3d83"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2d992d58596d64f3d83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15b97eef9255fb45cccd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-15b97eef9255fb45cccd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4be11ac3caaad789ae8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4be11ac3caaad789ae8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b81b6830dd09d1ffa79"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b81b6830dd09d1ffa79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a42e18313b207ccdafad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a42e18313b207ccdafad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-088b53ac30d4585e1f9e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-088b53ac30d4585e1f9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-17ea5ab92f31d666db45"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-17ea5ab92f31d666db45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ed429f1c960cef07286"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6ed429f1c960cef07286`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29d78463f9e74b7b162b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-29d78463f9e74b7b162b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45cccf9c0fb24b50ad2c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45cccf9c0fb24b50ad2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-255a76c0bb2e3b132af4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-255a76c0bb2e3b132af4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83980e40ec6781f41711"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-83980e40ec6781f41711`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-baf71d54338c988ec2ec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-baf71d54338c988ec2ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbccca9dd69886594c38"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fbccca9dd69886594c38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e20bae55a25f61127ff0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e20bae55a25f61127ff0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef690af192bd603b0466"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef690af192bd603b0466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f46940be244e0c50343"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6f46940be244e0c50343`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a362664b3369773221a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9a362664b3369773221a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a1fbcb8d99d6f019c85"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a1fbcb8d99d6f019c85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2705c3df9d8741d83e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c2705c3df9d8741d83e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a187ff22060891eb54a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a187ff22060891eb54a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d2b7d54e1a669bdb891"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7d2b7d54e1a669bdb891`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c170569b71e8b0c9b2e2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c170569b71e8b0c9b2e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7f86e6e65772340b64e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f7f86e6e65772340b64e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d349b1db025857c360a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d349b1db025857c360a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3476d4b093a54b2060a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e3476d4b093a54b2060a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4308de265fe58bcb429"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4308de265fe58bcb429`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8f1348b73ce31cc549e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e8f1348b73ce31cc549e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d2b7cfb229276d5ddf6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d2b7cfb229276d5ddf6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5abb917bc9d80dbe3bd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e5abb917bc9d80dbe3bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fe9778c69fc4ae8b5fca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fe9778c69fc4ae8b5fca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73fa0e28027b5284eb8a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-73fa0e28027b5284eb8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5886cbe0f47cad1b459b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5886cbe0f47cad1b459b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91a683ce13384e8d49e0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-91a683ce13384e8d49e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-889fa9dd52378dde5cd3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-889fa9dd52378dde5cd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22e6674cc51a60db498b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-22e6674cc51a60db498b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5989d9e1439ec4ec4233"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5989d9e1439ec4ec4233`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e67009aabc0d3f6ab69b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e67009aabc0d3f6ab69b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c145116de015174e036"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c145116de015174e036`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09c9abbdd10df56ff0f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-09c9abbdd10df56ff0f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83e3b22c0dfe289b47fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-83e3b22c0dfe289b47fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e01bcfaf6a98fccde6e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2e01bcfaf6a98fccde6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-50302fea8fa125eaf0dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-50302fea8fa125eaf0dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ddc498ba3454f550455"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ddc498ba3454f550455`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5490e4480e7e2200d937"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5490e4480e7e2200d937`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39b0bf80cbc4b8bd4c3e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39b0bf80cbc4b8bd4c3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ef5296a4f740c7c46754"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ef5296a4f740c7c46754`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36178a99d7e402ca0495"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-36178a99d7e402ca0495`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c8b263885f4f2fe3d91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2c8b263885f4f2fe3d91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-774cca0ac4c5a90d84f8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-774cca0ac4c5a90d84f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7e6b7f2142b8b678a606"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7e6b7f2142b8b678a606`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b0b12a27c6510460695"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b0b12a27c6510460695`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a61ac88bfe2f30eb3753"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a61ac88bfe2f30eb3753`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7662e23c7cc913825978"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7662e23c7cc913825978`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f6ac3ce249d4c7ee0816"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f6ac3ce249d4c7ee0816`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6fd8ea3783f09f59148"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a6fd8ea3783f09f59148`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8be78fbd83450dae874f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8be78fbd83450dae874f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac683e8eb4e83eb69dd0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac683e8eb4e83eb69dd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-042a69751ceca1aed582"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-042a69751ceca1aed582`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31bd0168aa1cedd0f6bd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-31bd0168aa1cedd0f6bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14ba18a53d1cb57573ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-14ba18a53d1cb57573ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3ba1e9eb9e0a4134710"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c3ba1e9eb9e0a4134710`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4e44125b1149a50e9b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4e44125b1149a50e9b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b26a9c8c3840e4ee6e00"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b26a9c8c3840e4ee6e00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37d77f627a87170a3710"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-37d77f627a87170a3710`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d7ec8d333079c7a164b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6d7ec8d333079c7a164b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f637e35e3bdd7269b4c1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f637e35e3bdd7269b4c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7b2eaeab55cea6f4d1e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f7b2eaeab55cea6f4d1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffd0b10cb411424da52b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ffd0b10cb411424da52b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cedb32e9c532d9553632"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cedb32e9c532d9553632`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c943912b676e46f77984"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c943912b676e46f77984`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a615431250a7d9dbc5d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a615431250a7d9dbc5d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85e60772d215c91754a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85e60772d215c91754a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f026f3893b1b22245bc5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f026f3893b1b22245bc5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c232a10531df4ab2f843"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c232a10531df4ab2f843`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-610d4152248bc40fbd69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-610d4152248bc40fbd69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86012bce8aa88c1082f8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-86012bce8aa88c1082f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cf4d2e97ff2bb55a3b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8cf4d2e97ff2bb55a3b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0c964109d1f9c6368559"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c964109d1f9c6368559`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f1d15912d1bdb0c5b39"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0f1d15912d1bdb0c5b39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c32df5a274896b153a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2c32df5a274896b153a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c711be90182d356f933a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c711be90182d356f933a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3828f671a8e8fa25ca92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3828f671a8e8fa25ca92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1d8f8749e972dd56674"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b1d8f8749e972dd56674`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9ab5ba366e73b9e2b04"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9ab5ba366e73b9e2b04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-028f8d440bd3e7d703a5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-028f8d440bd3e7d703a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a849f332698d35368f6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a849f332698d35368f6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddb1277804843b8e99a0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ddb1277804843b8e99a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66765b1e359348dd4868"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-66765b1e359348dd4868`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-378c189fd844f39e50f0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-378c189fd844f39e50f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d8ce18ac2d1ca0d07abf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d8ce18ac2d1ca0d07abf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-caf672d37a7f152a4b1d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-caf672d37a7f152a4b1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d125d6c6af54d9f44f94"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d125d6c6af54d9f44f94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f6960a243c99307ede5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f6960a243c99307ede5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc132acd026941825c7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc132acd026941825c7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04bab40868e8b515ff14"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04bab40868e8b515ff14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00995c5f9328e2ed902e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-00995c5f9328e2ed902e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7984cfd65ec18c153afd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7984cfd65ec18c153afd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-37c4519c10456ab2642e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-37c4519c10456ab2642e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5431030ffef1c41fa9c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5431030ffef1c41fa9c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97ba805dc76115f96969"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-97ba805dc76115f96969`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b9571162a4a26ff1b54"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b9571162a4a26ff1b54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a08f27909278b2342700"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a08f27909278b2342700`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5de234adacb4040ff3b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5de234adacb4040ff3b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-154cb9d90c546dd58049"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-154cb9d90c546dd58049`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-043b60f8288766a1e831"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-043b60f8288766a1e831`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2f638eed47fc1518ca96"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f638eed47fc1518ca96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a6861e6837dc0a450b1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a6861e6837dc0a450b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e21c9ea6324a91859e3f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e21c9ea6324a91859e3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c59ce55cf7edba68939"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3c59ce55cf7edba68939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-deb9b02e1b507a17535d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-deb9b02e1b507a17535d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-126d655530ef531ccb8f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-126d655530ef531ccb8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-860b67e90f119a621033"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-860b67e90f119a621033`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd946b554fd12488bfc1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dd946b554fd12488bfc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-entry-grade:canonical-southeast | <a href="#case-preview_review-c90a34f40dd0c9a50f1c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-entry-grade:canonical-top | <a href="#case-preview_review-a0f671b0a7f9e2b73ab2">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-entry-grade:connection-overview | <a href="#case-preview_review-4b4489a9e6eefc5ef263">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-entry-grade:canonical-southeast</summary>

<a id="case-preview_review-c90a34f40dd0c9a50f1c"></a>

**General: unverified** — `preview_review-c90a34f40dd0c9a50f1c`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-entry-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-entry-grade:canonical-top</summary>

<a id="case-preview_review-a0f671b0a7f9e2b73ab2"></a>

**General: unverified** — `preview_review-a0f671b0a7f9e2b73ab2`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-entry-grade:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-entry-grade:connection-overview</summary>

<a id="case-preview_review-4b4489a9e6eefc5ef263"></a>

**General: unverified** — `preview_review-4b4489a9e6eefc5ef263`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-entry-grade:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the grade function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
