---
title: "HSR Modular One-Tile Two-Level Crossing: testing"
summary: "Define this reusable piece’s test scope, setup, software checks, game checks, results, known issues, and design history."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR Modular One-Tile Two-Level Crossing: testing

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

The [piece overview](README.md) contains the pictures, placement instructions, and intrinsic movement matrix. This document contains the corresponding procedures, exact cases, observations, limitations, and historical evidence.

## 1. Test scope

Use the [connection matrix](README.md#3-connection-matrix) to select a directed journey, then open its exact result link here. The measured connections below describe this reusable piece; they do not certify an arbitrary neighbouring piece.

A case is one exact check under stated conditions. Saved-resource software checks, human preview review, game appearance, Route Query, and visible train travel are separate observations. A Route Query line does not prove that a train visibly completed a journey. Only explicit human confirmation can record a manual pass.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Win` | hsr / 7 / primary | in | [-8.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Wout` | hsr / 7 / primary | out | [-8.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Sout` | hsr / 7 / primary | out | [-2.0, -8.0, 30.5]; [0.0, -1.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 30.5]; [0.0, -1.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |
| `Sin` | hsr / 7 / primary | in | [2.0, -8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-9b897a8bacb659f807fe` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-9b897a8bacb659f807fe` |
| `Eout` | hsr / 7 / primary | out | [8.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Ein` | hsr / 7 / primary | in | [8.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Win` → `Eout` | primary |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Ein` → `Wout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Win` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Win` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Win` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Read [Piece and placement](README.md#2-piece-and-placement) for the required construction rectangle, complete joining boundaries, approach types, and supported rotations.
2. Follow the [separate build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md) to prepare the matching candidate and its dependencies before a game trial. Use a disposable flat test city, and keep the documented footprint clear.
3. Record the candidate’s actual file hashes, platform, game version, NAM profile, test-city conditions, and chosen rotation. Preserve those details with each observation through the [shared testing procedure](../../../../docs/TESTING.md).

Setup instructions describe a repeatable future test; they do not record a completed installation or successful game run.

## 3. Software checks

The current [presentation-refresh record](evidence/presentation-refresh.json) identifies the canonical angled view, bright-green top grid, and connection overview rendered from the unchanged verified `dist/trumpet-fan-core-parts-final-01` resources. It records the current connector re-extraction and freshness checks, exact image hashes, and preserved observations. Earlier saved-resource and documentation-refresh reports retain their original native-check facts and picture fingerprints; this presentation refresh does not claim another geometry build or game observation.

### Engineering contract

Both paired levels meet in one occupied cell: upper north/south paths are at 30.5 m, and lower east/west paths are at 15.5 m. The encoded graph has four grade-separated track crossings with no turning transfer. Use matching separately placed standard straight approaches when assembling a larger crossing. Encoded no-transfer checks do not establish actual in-game level isolation.

Use the [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and this type’s [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.

The current documentation uses the unchanged compiled piece from a verified source build. [Saved-resource evidence](evidence/saved-resource-checks.json) identifies the source DAT and the exact software-report scope; refreshing a guide does not claim another game test. Construction, traffic demand, demolition, shadows, and save/reload remain separate game checks.

## 4. Game checks

Use the [exact test checklist](#test-checklist) for each required orientation and direction. Record Route Query separately from watching a train complete the same journey. Keep appearance, placement, forbidden movements, demolition, and save/reload observations in their own cases.

Follow the [shared observation procedure](../../../../docs/TESTING.md#record-one-observation) with this piece’s [authoritative test record](checks/manual-tests.json). Preserve failures, stale observations, and their original scope. The generated sections below provide the exact recording command and case identifiers.

## 5. Results and known issues

The generated status and checklist below retain the authoritative observations in [checks/manual-tests.json](checks/manual-tests.json), including failures, stale results, and their exact environments. Open an individual case for its evidence and recording scope.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/16 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/16 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 99, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-modular-crossing-core/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-modular-crossing-core/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0ce2c7625a107ac300a9">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0ce2c7625a107ac300a9"></a>

**General: passed** — `software_resources-0ce2c7625a107ac300a9`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0ce2c7625a107ac300a9">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0ce2c7625a107ac300a9"></a>

**General: passed** — `software_connectivity-0ce2c7625a107ac300a9`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-60bb45d1c468daf9127a">[ ] unverified</a> | <a href="#case-in_game_render-5dd9163ea7feb4d233d9">[ ] unverified</a> | <a href="#case-in_game_render-aac75d58babe92d0df66">[ ] unverified</a> | <a href="#case-in_game_render-8c67ccb3f983d252d251">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-60bb45d1c468daf9127a"></a>

**0° CCW: unverified** — `in_game_render-60bb45d1c468daf9127a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5dd9163ea7feb4d233d9"></a>

**90° CCW: unverified** — `in_game_render-5dd9163ea7feb4d233d9`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-aac75d58babe92d0df66"></a>

**180° CCW: unverified** — `in_game_render-aac75d58babe92d0df66`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8c67ccb3f983d252d251"></a>

**270° CCW: unverified** — `in_game_render-8c67ccb3f983d252d251`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-60bb45d1c468daf9127a">[ ] unverified</a> | <a href="#case-in_game_placement-5dd9163ea7feb4d233d9">[ ] unverified</a> | <a href="#case-in_game_placement-aac75d58babe92d0df66">[ ] unverified</a> | <a href="#case-in_game_placement-8c67ccb3f983d252d251">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-60bb45d1c468daf9127a"></a>

**0° CCW: unverified** — `in_game_placement-60bb45d1c468daf9127a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5dd9163ea7feb4d233d9"></a>

**90° CCW: unverified** — `in_game_placement-5dd9163ea7feb4d233d9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-aac75d58babe92d0df66"></a>

**180° CCW: unverified** — `in_game_placement-aac75d58babe92d0df66`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8c67ccb3f983d252d251"></a>

**270° CCW: unverified** — `in_game_placement-8c67ccb3f983d252d251`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-60bb45d1c468daf9127a">[ ] unverified</a> | <a href="#case-in_game_demolition-5dd9163ea7feb4d233d9">[ ] unverified</a> | <a href="#case-in_game_demolition-aac75d58babe92d0df66">[ ] unverified</a> | <a href="#case-in_game_demolition-8c67ccb3f983d252d251">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-60bb45d1c468daf9127a"></a>

**0° CCW: unverified** — `in_game_demolition-60bb45d1c468daf9127a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5dd9163ea7feb4d233d9"></a>

**90° CCW: unverified** — `in_game_demolition-5dd9163ea7feb4d233d9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-aac75d58babe92d0df66"></a>

**180° CCW: unverified** — `in_game_demolition-aac75d58babe92d0df66`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8c67ccb3f983d252d251"></a>

**270° CCW: unverified** — `in_game_demolition-8c67ccb3f983d252d251`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-60bb45d1c468daf9127a">[ ] unverified</a> | <a href="#case-in_game_save_reload-5dd9163ea7feb4d233d9">[ ] unverified</a> | <a href="#case-in_game_save_reload-aac75d58babe92d0df66">[ ] unverified</a> | <a href="#case-in_game_save_reload-8c67ccb3f983d252d251">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-60bb45d1c468daf9127a"></a>

**0° CCW: unverified** — `in_game_save_reload-60bb45d1c468daf9127a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5dd9163ea7feb4d233d9"></a>

**90° CCW: unverified** — `in_game_save_reload-5dd9163ea7feb4d233d9`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-aac75d58babe92d0df66"></a>

**180° CCW: unverified** — `in_game_save_reload-aac75d58babe92d0df66`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8c67ccb3f983d252d251"></a>

**270° CCW: unverified** — `in_game_save_reload-8c67ccb3f983d252d251`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_route_query-f4d9cf8f9cd43b3ed436">[ ] unverified</a> | <a href="#case-in_game_route_query-5ea57b050a0a108944d2">[ ] unverified</a> | <a href="#case-in_game_route_query-389d267436dcf471fba4">[ ] unverified</a> | <a href="#case-in_game_route_query-9e0ac6b5dbf02c9f3695">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_route_query-c784d630dc08288b2fdf">[ ] unverified</a> | <a href="#case-in_game_route_query-481ea42c7e9a990d906d">[ ] unverified</a> | <a href="#case-in_game_route_query-fed4803926213bf8e9a9">[ ] unverified</a> | <a href="#case-in_game_route_query-73116eb4a175a83f4b9f">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_route_query-f5ef54272d07300cac9a">[ ] unverified</a> | <a href="#case-in_game_route_query-5b79e6464c43e4f6948a">[ ] unverified</a> | <a href="#case-in_game_route_query-d95471d14adcbf720bc7">[ ] unverified</a> | <a href="#case-in_game_route_query-cfc5120864436a36cad0">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_route_query-4fe45956037912e0b05c">[ ] unverified</a> | <a href="#case-in_game_route_query-6d8268095588e8c01445">[ ] unverified</a> | <a href="#case-in_game_route_query-3296eead8f9757864acb">[ ] unverified</a> | <a href="#case-in_game_route_query-ad335f8c4d250bee4c7d">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_route_query-f4d9cf8f9cd43b3ed436"></a>

**0° CCW: unverified** — `in_game_route_query-f4d9cf8f9cd43b3ed436`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-5ea57b050a0a108944d2"></a>

**90° CCW: unverified** — `in_game_route_query-5ea57b050a0a108944d2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-389d267436dcf471fba4"></a>

**180° CCW: unverified** — `in_game_route_query-389d267436dcf471fba4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-9e0ac6b5dbf02c9f3695"></a>

**270° CCW: unverified** — `in_game_route_query-9e0ac6b5dbf02c9f3695`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_route_query-c784d630dc08288b2fdf"></a>

**0° CCW: unverified** — `in_game_route_query-c784d630dc08288b2fdf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-481ea42c7e9a990d906d"></a>

**90° CCW: unverified** — `in_game_route_query-481ea42c7e9a990d906d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-fed4803926213bf8e9a9"></a>

**180° CCW: unverified** — `in_game_route_query-fed4803926213bf8e9a9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-73116eb4a175a83f4b9f"></a>

**270° CCW: unverified** — `in_game_route_query-73116eb4a175a83f4b9f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_route_query-f5ef54272d07300cac9a"></a>

**0° CCW: unverified** — `in_game_route_query-f5ef54272d07300cac9a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-5b79e6464c43e4f6948a"></a>

**90° CCW: unverified** — `in_game_route_query-5b79e6464c43e4f6948a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-d95471d14adcbf720bc7"></a>

**180° CCW: unverified** — `in_game_route_query-d95471d14adcbf720bc7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-cfc5120864436a36cad0"></a>

**270° CCW: unverified** — `in_game_route_query-cfc5120864436a36cad0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_route_query-4fe45956037912e0b05c"></a>

**0° CCW: unverified** — `in_game_route_query-4fe45956037912e0b05c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-6d8268095588e8c01445"></a>

**90° CCW: unverified** — `in_game_route_query-6d8268095588e8c01445`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-3296eead8f9757864acb"></a>

**180° CCW: unverified** — `in_game_route_query-3296eead8f9757864acb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-ad335f8c4d250bee4c7d"></a>

**270° CCW: unverified** — `in_game_route_query-ad335f8c4d250bee4c7d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_visible_travel-f4d9cf8f9cd43b3ed436">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5ea57b050a0a108944d2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-389d267436dcf471fba4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9e0ac6b5dbf02c9f3695">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_visible_travel-c784d630dc08288b2fdf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-481ea42c7e9a990d906d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fed4803926213bf8e9a9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-73116eb4a175a83f4b9f">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_visible_travel-f5ef54272d07300cac9a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5b79e6464c43e4f6948a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d95471d14adcbf720bc7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cfc5120864436a36cad0">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_visible_travel-4fe45956037912e0b05c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6d8268095588e8c01445">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3296eead8f9757864acb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ad335f8c4d250bee4c7d">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_visible_travel-f4d9cf8f9cd43b3ed436"></a>

**0° CCW: unverified** — `in_game_visible_travel-f4d9cf8f9cd43b3ed436`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-5ea57b050a0a108944d2"></a>

**90° CCW: unverified** — `in_game_visible_travel-5ea57b050a0a108944d2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-389d267436dcf471fba4"></a>

**180° CCW: unverified** — `in_game_visible_travel-389d267436dcf471fba4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-9e0ac6b5dbf02c9f3695"></a>

**270° CCW: unverified** — `in_game_visible_travel-9e0ac6b5dbf02c9f3695`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_visible_travel-c784d630dc08288b2fdf"></a>

**0° CCW: unverified** — `in_game_visible_travel-c784d630dc08288b2fdf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-481ea42c7e9a990d906d"></a>

**90° CCW: unverified** — `in_game_visible_travel-481ea42c7e9a990d906d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-fed4803926213bf8e9a9"></a>

**180° CCW: unverified** — `in_game_visible_travel-fed4803926213bf8e9a9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-73116eb4a175a83f4b9f"></a>

**270° CCW: unverified** — `in_game_visible_travel-73116eb4a175a83f4b9f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_visible_travel-f5ef54272d07300cac9a"></a>

**0° CCW: unverified** — `in_game_visible_travel-f5ef54272d07300cac9a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-5b79e6464c43e4f6948a"></a>

**90° CCW: unverified** — `in_game_visible_travel-5b79e6464c43e4f6948a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-d95471d14adcbf720bc7"></a>

**180° CCW: unverified** — `in_game_visible_travel-d95471d14adcbf720bc7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-cfc5120864436a36cad0"></a>

**270° CCW: unverified** — `in_game_visible_travel-cfc5120864436a36cad0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_visible_travel-4fe45956037912e0b05c"></a>

**0° CCW: unverified** — `in_game_visible_travel-4fe45956037912e0b05c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-6d8268095588e8c01445"></a>

**90° CCW: unverified** — `in_game_visible_travel-6d8268095588e8c01445`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-3296eead8f9757864acb"></a>

**180° CCW: unverified** — `in_game_visible_travel-3296eead8f9757864acb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-ad335f8c4d250bee4c7d"></a>

**270° CCW: unverified** — `in_game_visible_travel-ad335f8c4d250bee4c7d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a21b5e58377bc7e9477c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0ea1e21f7e35e149c7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-257e260a5e0e3b46a9e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fce588ed8dcd146cf3a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4bd98de4f164984e9fc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04bd9840b8539a8f8669">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b83c83d81ecdbec41c03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da2dbf17021ee893ab1e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-898e76225b3e7c1300bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7e9e410a4f607066a8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4d436a9d0258fac92d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7efe47c4aaa7818decc3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d5e030b5e7d39415eb3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cba7df633e5c115d8642">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa78c871f4b77f24f7c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48157237cfd256c6c89c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a95f8121f4d8cc51c61f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41eab0006cd4606d5a6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63f875e919b33922cf5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dea39cc8508b7e50759c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c46dbac8020aa6f92ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4392e3b07173e215988d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c40d120ea97eb620863e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f25975adc643b7822604">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6bfa6d9a37f3aca18752">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8107929d9878d5a0959b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86114342dcaea8ef890a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d4512ef952b7702bd6a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab64d46ede8871adbd9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-571462c9653682c72a53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6c9ee6a90c983908971">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88224e287710de4e97f4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cf09a5bd45e2e7752d29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a10f3750f8b93a66835e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c98dfe0574ea9fcec70f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43f984a6b23af0f0537f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2eb11d5412e3c60c6e77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b5dbaad2c39a779f15d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d2182f2123024b2c4e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68688ab62c7015e5d104">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bd1568734121623c4fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3b58e424ac234cab0a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-851548d1526b194b0c9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-772ed9de71e4631fbc0d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e4a8eca7572428aaafc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49ba649326bcc2ae7336">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-089f52e1911ce6fbb622">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d0fc335efa31bfb639c">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a21b5e58377bc7e9477c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a21b5e58377bc7e9477c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0ea1e21f7e35e149c7e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0ea1e21f7e35e149c7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-257e260a5e0e3b46a9e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-257e260a5e0e3b46a9e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fce588ed8dcd146cf3a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3fce588ed8dcd146cf3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4bd98de4f164984e9fc4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4bd98de4f164984e9fc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04bd9840b8539a8f8669"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04bd9840b8539a8f8669`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b83c83d81ecdbec41c03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b83c83d81ecdbec41c03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da2dbf17021ee893ab1e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-da2dbf17021ee893ab1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-898e76225b3e7c1300bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-898e76225b3e7c1300bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7e9e410a4f607066a8b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7e9e410a4f607066a8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4d436a9d0258fac92d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b4d436a9d0258fac92d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7efe47c4aaa7818decc3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7efe47c4aaa7818decc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d5e030b5e7d39415eb3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d5e030b5e7d39415eb3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cba7df633e5c115d8642"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cba7df633e5c115d8642`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa78c871f4b77f24f7c4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aa78c871f4b77f24f7c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48157237cfd256c6c89c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-48157237cfd256c6c89c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a95f8121f4d8cc51c61f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a95f8121f4d8cc51c61f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41eab0006cd4606d5a6c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-41eab0006cd4606d5a6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63f875e919b33922cf5e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63f875e919b33922cf5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dea39cc8508b7e50759c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dea39cc8508b7e50759c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c46dbac8020aa6f92ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c46dbac8020aa6f92ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4392e3b07173e215988d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4392e3b07173e215988d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c40d120ea97eb620863e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c40d120ea97eb620863e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f25975adc643b7822604"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f25975adc643b7822604`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6bfa6d9a37f3aca18752"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6bfa6d9a37f3aca18752`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8107929d9878d5a0959b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8107929d9878d5a0959b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86114342dcaea8ef890a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-86114342dcaea8ef890a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d4512ef952b7702bd6a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d4512ef952b7702bd6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab64d46ede8871adbd9a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab64d46ede8871adbd9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-571462c9653682c72a53"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-571462c9653682c72a53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6c9ee6a90c983908971"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c6c9ee6a90c983908971`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88224e287710de4e97f4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-88224e287710de4e97f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cf09a5bd45e2e7752d29"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cf09a5bd45e2e7752d29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a10f3750f8b93a66835e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a10f3750f8b93a66835e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c98dfe0574ea9fcec70f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c98dfe0574ea9fcec70f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43f984a6b23af0f0537f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43f984a6b23af0f0537f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2eb11d5412e3c60c6e77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2eb11d5412e3c60c6e77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b5dbaad2c39a779f15d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b5dbaad2c39a779f15d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d2182f2123024b2c4e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8d2182f2123024b2c4e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68688ab62c7015e5d104"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68688ab62c7015e5d104`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bd1568734121623c4fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bd1568734121623c4fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3b58e424ac234cab0a0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a3b58e424ac234cab0a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-851548d1526b194b0c9a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-851548d1526b194b0c9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-772ed9de71e4631fbc0d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-772ed9de71e4631fbc0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e4a8eca7572428aaafc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e4a8eca7572428aaafc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49ba649326bcc2ae7336"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-49ba649326bcc2ae7336`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-089f52e1911ce6fbb622"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-089f52e1911ce6fbb622`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d0fc335efa31bfb639c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d0fc335efa31bfb639c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-modular-crossing-core:canonical-southeast | <a href="#case-preview_review-d05a525f61d0bcb557b7">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-modular-crossing-core:canonical-top | <a href="#case-preview_review-f5e92b1e244c8ca1bd7e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-modular-crossing-core:connection-overview | <a href="#case-preview_review-11ea34ddb70834f03b05">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-modular-crossing-core:canonical-southeast</summary>

<a id="case-preview_review-d05a525f61d0bcb557b7"></a>

**General: unverified** — `preview_review-d05a525f61d0bcb557b7`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-modular-crossing-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-modular-crossing-core:canonical-top</summary>

<a id="case-preview_review-f5e92b1e244c8ca1bd7e"></a>

**General: unverified** — `preview_review-f5e92b1e244c8ca1bd7e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-modular-crossing-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-modular-crossing-core:connection-overview</summary>

<a id="case-preview_review-11ea34ddb70834f03b05"></a>

**General: unverified** — `preview_review-11ea34ddb70834f03b05`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-modular-crossing-core:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The retained evidence describes the version and scope recorded by its original report. A documentation reorganization does not create a new test run or extend an earlier observation to different inputs.
