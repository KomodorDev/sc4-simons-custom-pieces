---
title: "HSR Modular Symmetric Split and Return: testing"
summary: "Define this reusable piece’s test scope, setup, software checks, game checks, results, known issues, and design history."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR Modular Symmetric Split and Return: testing

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
| `Lin` | hsr / 7 / primary | in | [0.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-365752af76285c80cd0b` |
| `Sout` | hsr / 7 / primary | out | [14.0, -88.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [14.0, -24.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [18.0, -88.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [18.0, -24.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Rout` | hsr / 7 / primary | out | [32.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Lin` → `Sout` | primary |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Sin` → `Rout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Lin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Lin` | hsr / `Rout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Rout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Read [Piece and placement](README.md#2-piece-and-placement) for the required construction rectangle, complete joining boundaries, approach types, and supported rotations.
2. Follow the [separate build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md) to prepare the matching candidate and its dependencies before a game trial. Use a disposable flat test city, and keep the documented footprint clear.
3. Record the candidate’s actual file hashes, platform, game version, NAM profile, test-city conditions, and chosen rotation. Preserve those details with each observation through the [shared testing procedure](../../../../docs/TESTING.md).

Setup instructions describe a repeatable future test; they do not record a completed installation or successful game run.

## 3. Software checks

### Engineering contract

The construction rectangle is 3 × 6 tiles, containing fourteen occupied cells and eight authored supports. Two occupied cells carry structure without a traffic path; the other empty positions remain absent from the owned-cell mask. Source [column,row] cells increase eastward and southward, while picture X/Y increase eastward and northward. Use the generated grid conversion to identify the recessed central connection rather than treating a source row as a picture Y label.

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

Current totals: unverified: 71, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-modular-south-junction/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-modular-south-junction/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-8d7f9e5f7613da7f657b">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-8d7f9e5f7613da7f657b"></a>

**General: passed** — `software_resources-8d7f9e5f7613da7f657b`.

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
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-8d7f9e5f7613da7f657b">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-8d7f9e5f7613da7f657b"></a>

**General: passed** — `software_connectivity-8d7f9e5f7613da7f657b`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-modular-south-junction:canonical-southeast | <a href="#case-preview_review-8219039bd1a0abdc25dc">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-modular-south-junction:canonical-top | <a href="#case-preview_review-90d1cf88eac08860d51c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-modular-south-junction:connection-overview | <a href="#case-preview_review-ebf8d0f8e2241af4df75">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-modular-south-junction:canonical-southeast</summary>

<a id="case-preview_review-8219039bd1a0abdc25dc"></a>

**General: unverified** — `preview_review-8219039bd1a0abdc25dc`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-modular-south-junction:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-modular-south-junction:canonical-top</summary>

<a id="case-preview_review-90d1cf88eac08860d51c"></a>

**General: unverified** — `preview_review-90d1cf88eac08860d51c`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-modular-south-junction:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-modular-south-junction:connection-overview</summary>

<a id="case-preview_review-ebf8d0f8e2241af4df75"></a>

**General: unverified** — `preview_review-ebf8d0f8e2241af4df75`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-modular-south-junction:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-c8a33b58b9fbd61e4079">[ ] unverified</a> | <a href="#case-in_game_render-83ce8d8482bf01462b30">[ ] unverified</a> | <a href="#case-in_game_render-2c791739a570cb0cb251">[ ] unverified</a> | <a href="#case-in_game_render-e105e9ecce2223cd9f80">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-c8a33b58b9fbd61e4079"></a>

**0° CCW: unverified** — `in_game_render-c8a33b58b9fbd61e4079`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-83ce8d8482bf01462b30"></a>

**90° CCW: unverified** — `in_game_render-83ce8d8482bf01462b30`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2c791739a570cb0cb251"></a>

**180° CCW: unverified** — `in_game_render-2c791739a570cb0cb251`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e105e9ecce2223cd9f80"></a>

**270° CCW: unverified** — `in_game_render-e105e9ecce2223cd9f80`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-c8a33b58b9fbd61e4079">[ ] unverified</a> | <a href="#case-in_game_placement-83ce8d8482bf01462b30">[ ] unverified</a> | <a href="#case-in_game_placement-2c791739a570cb0cb251">[ ] unverified</a> | <a href="#case-in_game_placement-e105e9ecce2223cd9f80">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-c8a33b58b9fbd61e4079"></a>

**0° CCW: unverified** — `in_game_placement-c8a33b58b9fbd61e4079`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-83ce8d8482bf01462b30"></a>

**90° CCW: unverified** — `in_game_placement-83ce8d8482bf01462b30`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2c791739a570cb0cb251"></a>

**180° CCW: unverified** — `in_game_placement-2c791739a570cb0cb251`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e105e9ecce2223cd9f80"></a>

**270° CCW: unverified** — `in_game_placement-e105e9ecce2223cd9f80`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-c8a33b58b9fbd61e4079">[ ] unverified</a> | <a href="#case-in_game_demolition-83ce8d8482bf01462b30">[ ] unverified</a> | <a href="#case-in_game_demolition-2c791739a570cb0cb251">[ ] unverified</a> | <a href="#case-in_game_demolition-e105e9ecce2223cd9f80">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-c8a33b58b9fbd61e4079"></a>

**0° CCW: unverified** — `in_game_demolition-c8a33b58b9fbd61e4079`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-83ce8d8482bf01462b30"></a>

**90° CCW: unverified** — `in_game_demolition-83ce8d8482bf01462b30`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2c791739a570cb0cb251"></a>

**180° CCW: unverified** — `in_game_demolition-2c791739a570cb0cb251`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e105e9ecce2223cd9f80"></a>

**270° CCW: unverified** — `in_game_demolition-e105e9ecce2223cd9f80`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-c8a33b58b9fbd61e4079">[ ] unverified</a> | <a href="#case-in_game_save_reload-83ce8d8482bf01462b30">[ ] unverified</a> | <a href="#case-in_game_save_reload-2c791739a570cb0cb251">[ ] unverified</a> | <a href="#case-in_game_save_reload-e105e9ecce2223cd9f80">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-c8a33b58b9fbd61e4079"></a>

**0° CCW: unverified** — `in_game_save_reload-c8a33b58b9fbd61e4079`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-83ce8d8482bf01462b30"></a>

**90° CCW: unverified** — `in_game_save_reload-83ce8d8482bf01462b30`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2c791739a570cb0cb251"></a>

**180° CCW: unverified** — `in_game_save_reload-2c791739a570cb0cb251`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e105e9ecce2223cd9f80"></a>

**270° CCW: unverified** — `in_game_save_reload-e105e9ecce2223cd9f80`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout | — | <a href="#case-in_game_route_query-cf0d19c93952223d47d1">[ ] unverified</a> | <a href="#case-in_game_route_query-99a86489e9fc55d03118">[ ] unverified</a> | <a href="#case-in_game_route_query-1af95c8b8bd42ddd5cf3">[ ] unverified</a> | <a href="#case-in_game_route_query-bebbb44b56b8a04d8932">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_route_query-591b8068a7af8a82744c">[ ] unverified</a> | <a href="#case-in_game_route_query-3aa7411072ac6311c728">[ ] unverified</a> | <a href="#case-in_game_route_query-7f7a05c21e7430a434d9">[ ] unverified</a> | <a href="#case-in_game_route_query-b952d326e1ae3d4859d5">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_route_query-3e9107af6496c7d3ac4a">[ ] unverified</a> | <a href="#case-in_game_route_query-4fcbc6382af0ddca4f05">[ ] unverified</a> | <a href="#case-in_game_route_query-1031f63a625910d37042">[ ] unverified</a> | <a href="#case-in_game_route_query-4bc1a9ed3b5f661138ac">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout | — | <a href="#case-in_game_route_query-abb9d42e6ab5a4275279">[ ] unverified</a> | <a href="#case-in_game_route_query-0da4374c45481e6e306e">[ ] unverified</a> | <a href="#case-in_game_route_query-9cdb0e38746c7f11a766">[ ] unverified</a> | <a href="#case-in_game_route_query-63f9dff6f384ed46d433">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout</summary>

<a id="case-in_game_route_query-cf0d19c93952223d47d1"></a>

**0° CCW: unverified** — `in_game_route_query-cf0d19c93952223d47d1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-99a86489e9fc55d03118"></a>

**90° CCW: unverified** — `in_game_route_query-99a86489e9fc55d03118`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-1af95c8b8bd42ddd5cf3"></a>

**180° CCW: unverified** — `in_game_route_query-1af95c8b8bd42ddd5cf3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-bebbb44b56b8a04d8932"></a>

**270° CCW: unverified** — `in_game_route_query-bebbb44b56b8a04d8932`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_route_query-591b8068a7af8a82744c"></a>

**0° CCW: unverified** — `in_game_route_query-591b8068a7af8a82744c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-3aa7411072ac6311c728"></a>

**90° CCW: unverified** — `in_game_route_query-3aa7411072ac6311c728`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-7f7a05c21e7430a434d9"></a>

**180° CCW: unverified** — `in_game_route_query-7f7a05c21e7430a434d9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-b952d326e1ae3d4859d5"></a>

**270° CCW: unverified** — `in_game_route_query-b952d326e1ae3d4859d5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_route_query-3e9107af6496c7d3ac4a"></a>

**0° CCW: unverified** — `in_game_route_query-3e9107af6496c7d3ac4a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-4fcbc6382af0ddca4f05"></a>

**90° CCW: unverified** — `in_game_route_query-4fcbc6382af0ddca4f05`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-1031f63a625910d37042"></a>

**180° CCW: unverified** — `in_game_route_query-1031f63a625910d37042`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-4bc1a9ed3b5f661138ac"></a>

**270° CCW: unverified** — `in_game_route_query-4bc1a9ed3b5f661138ac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout</summary>

<a id="case-in_game_route_query-abb9d42e6ab5a4275279"></a>

**0° CCW: unverified** — `in_game_route_query-abb9d42e6ab5a4275279`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_route_query-0da4374c45481e6e306e"></a>

**90° CCW: unverified** — `in_game_route_query-0da4374c45481e6e306e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_route_query-9cdb0e38746c7f11a766"></a>

**180° CCW: unverified** — `in_game_route_query-9cdb0e38746c7f11a766`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_route_query-63f9dff6f384ed46d433"></a>

**270° CCW: unverified** — `in_game_route_query-63f9dff6f384ed46d433`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout | — | <a href="#case-in_game_visible_travel-cf0d19c93952223d47d1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-99a86489e9fc55d03118">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1af95c8b8bd42ddd5cf3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bebbb44b56b8a04d8932">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_visible_travel-591b8068a7af8a82744c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3aa7411072ac6311c728">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7f7a05c21e7430a434d9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b952d326e1ae3d4859d5">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_visible_travel-3e9107af6496c7d3ac4a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4fcbc6382af0ddca4f05">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1031f63a625910d37042">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4bc1a9ed3b5f661138ac">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout | — | <a href="#case-in_game_visible_travel-abb9d42e6ab5a4275279">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0da4374c45481e6e306e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9cdb0e38746c7f11a766">[ ] unverified</a> | <a href="#case-in_game_visible_travel-63f9dff6f384ed46d433">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout</summary>

<a id="case-in_game_visible_travel-cf0d19c93952223d47d1"></a>

**0° CCW: unverified** — `in_game_visible_travel-cf0d19c93952223d47d1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-99a86489e9fc55d03118"></a>

**90° CCW: unverified** — `in_game_visible_travel-99a86489e9fc55d03118`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-1af95c8b8bd42ddd5cf3"></a>

**180° CCW: unverified** — `in_game_visible_travel-1af95c8b8bd42ddd5cf3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-bebbb44b56b8a04d8932"></a>

**270° CCW: unverified** — `in_game_visible_travel-bebbb44b56b8a04d8932`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Lin>Sout; entry: Lin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_visible_travel-591b8068a7af8a82744c"></a>

**0° CCW: unverified** — `in_game_visible_travel-591b8068a7af8a82744c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-3aa7411072ac6311c728"></a>

**90° CCW: unverified** — `in_game_visible_travel-3aa7411072ac6311c728`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-7f7a05c21e7430a434d9"></a>

**180° CCW: unverified** — `in_game_visible_travel-7f7a05c21e7430a434d9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-b952d326e1ae3d4859d5"></a>

**270° CCW: unverified** — `in_game_visible_travel-b952d326e1ae3d4859d5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_visible_travel-3e9107af6496c7d3ac4a"></a>

**0° CCW: unverified** — `in_game_visible_travel-3e9107af6496c7d3ac4a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-4fcbc6382af0ddca4f05"></a>

**90° CCW: unverified** — `in_game_visible_travel-4fcbc6382af0ddca4f05`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-1031f63a625910d37042"></a>

**180° CCW: unverified** — `in_game_visible_travel-1031f63a625910d37042`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-4bc1a9ed3b5f661138ac"></a>

**270° CCW: unverified** — `in_game_visible_travel-4bc1a9ed3b5f661138ac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout</summary>

<a id="case-in_game_visible_travel-abb9d42e6ab5a4275279"></a>

**0° CCW: unverified** — `in_game_visible_travel-abb9d42e6ab5a4275279`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_visible_travel-0da4374c45481e6e306e"></a>

**90° CCW: unverified** — `in_game_visible_travel-0da4374c45481e6e306e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_visible_travel-9cdb0e38746c7f11a766"></a>

**180° CCW: unverified** — `in_game_visible_travel-9cdb0e38746c7f11a766`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

<a id="case-in_game_visible_travel-63f9dff6f384ed46d433"></a>

**270° CCW: unverified** — `in_game_visible_travel-63f9dff6f384ed46d433`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Rout; entry: Sin; exit: Rout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cebd07ace4c23e3b0b40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6af57208b707bbb8e7c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2c013174b190ad8b2e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64e5d198fa7cc0119c64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9cc44127a3b0a3f352f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af3a0f5fb09ced1d69f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c82342e14491e73e5037">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbeb843b0c323e9069db">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0d1db4aa8702d16edfa7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20e86055ec33ded7deac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-005550f717d3e9b45afb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47ced1859cc3164352a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b1c116c697c9ef2bdbe6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7424b989a88c17338451">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2fc295f6a8a69b769cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9373805b37c05012014b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0f95ab42ea20b9fade96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97dbc0b5c378dc5ed20f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f2892e0d17c7c4dcfbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86fde97704dd30bcc3b3">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cebd07ace4c23e3b0b40"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cebd07ace4c23e3b0b40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6af57208b707bbb8e7c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6af57208b707bbb8e7c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2c013174b190ad8b2e5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2c013174b190ad8b2e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64e5d198fa7cc0119c64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64e5d198fa7cc0119c64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9cc44127a3b0a3f352f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9cc44127a3b0a3f352f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af3a0f5fb09ced1d69f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-af3a0f5fb09ced1d69f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c82342e14491e73e5037"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c82342e14491e73e5037`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbeb843b0c323e9069db"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bbeb843b0c323e9069db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Lin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0d1db4aa8702d16edfa7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0d1db4aa8702d16edfa7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20e86055ec33ded7deac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20e86055ec33ded7deac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-005550f717d3e9b45afb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-005550f717d3e9b45afb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47ced1859cc3164352a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-47ced1859cc3164352a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b1c116c697c9ef2bdbe6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1c116c697c9ef2bdbe6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7424b989a88c17338451"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7424b989a88c17338451`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2fc295f6a8a69b769cd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2fc295f6a8a69b769cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9373805b37c05012014b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9373805b37c05012014b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Rout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0f95ab42ea20b9fade96"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0f95ab42ea20b9fade96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97dbc0b5c378dc5ed20f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-97dbc0b5c378dc5ed20f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f2892e0d17c7c4dcfbd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f2892e0d17c7c4dcfbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86fde97704dd30bcc3b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-86fde97704dd30bcc3b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The retained evidence describes the version and scope recorded by its original report. A documentation reorganization does not create a new test run or extend an earlier observation to different inputs.
