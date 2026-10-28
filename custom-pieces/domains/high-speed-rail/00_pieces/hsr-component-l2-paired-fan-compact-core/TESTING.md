---
title: "HSR Level 2 Compact Paired Fan Core: testing"
summary: "Define the retained nine-cell fork, recessed-web joining profile, software evidence, and separate game checks."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR Level 2 Compact Paired Fan Core: testing

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

The [piece overview](README.md) contains the pictures, placement steps, and intrinsic movement matrix. This document defines the exact test scope, saved-resource evidence, observations, and limitations.

## 1. Test scope

A port is one directional transport-path endpoint. A complete joining boundary also includes the surrounding concrete profile, physical tracks, direction, height, heading, and clearance. Select a journey in the [connection matrix](README.md#3-connection-matrix), and open its exact result link here. The measured interfaces describe this reusable core; they do not certify an arbitrary neighbour.

Software resource validation, human preview review, game appearance, Route Query, and visible train travel are separate observations. A Route Query line does not prove that a train completed the journey, and a successful build does not establish either game result.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Wout` | hsr / 7 / primary | out | [6.398519, -40.0, 15.5]; [-0.9272548089646255, -0.3744309272108488]; 0.0 | `path-interface-0f4b8204e68941486c48` |
| `Nin` | hsr / 7 / primary | in | [30.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nout` | hsr / 7 / primary | out | [34.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Ein` | hsr / 7 / primary | in | [57.601481, -40.0, 15.5]; [-0.9272548089646255, 0.3744309272108488]; 0.0 | `path-interface-d819a6d05c5e43d11db7` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Wout` | primary |
| hsr | `Ein` → `Nout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Read [Piece and placement](README.md#2-piece-and-placement) for the complete 5 × 3 construction rectangle, matching recessed-web north approach, and curved southern connections. Reserve the two structural cells as well as the cells with train paths.
2. Follow the [shared build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md) before a game trial. Use a disposable flat test city, the matching dependencies, and one declared rotation at a time.
3. Record the actual candidate file hashes, platform, game version, NAM profile, terrain, neighbouring pieces, and chosen rotation with each observation through the [shared testing procedure](../../../../docs/TESTING.md).

These steps describe a future repeatable game trial. They do not record an installation or a successful game observation.

## 3. Software checks

The current [presentation-refresh record](evidence/presentation-refresh.json) identifies the canonical angled view, bright-green top grid, and connection overview rendered from the unchanged verified `dist/trumpet-fan-core-parts-final-01` resources. It records the current connector re-extraction and freshness checks, exact image hashes, and preserved observations. Earlier saved-resource and documentation-refresh reports retain their original native-check facts and picture fingerprints; this presentation refresh does not claim another geometry build or game observation.

### Exact retained fork

The new core owns nine cells of the accepted complete fan: original source cells `[3,2]`, `[2,3]`, `[3,3]`, `[4,3]`, `[1,4]`, `[2,4]`, `[3,4]`, `[4,4]`, and `[5,4]`. Subtract `[1,2]` from each original [column, row] to obtain this core's local cells. Its footprint is 5 × 3 tiles, including two structural cells and four supports.

The extraction preserves every retained cell's five saved model zooms, PATH resource, and five shadow resources. Rebased coordinates and newly allocated game identifiers do not authorize reshaping the fork. Its full eleven-cell sweep context is retained for compilation, while only the selected nine outputs belong to the core. The [native extraction proof](evidence/fan-core-extraction.json) records actual resource hashes and the exact comparison. The [current saved-resource report](evidence/saved-resource-checks.json) records the normal build's independent checks.

The central raised grey triangle and its vertical inside faces retain the accepted full-fan repair. Separate saved-model checks still inspect the fork's raised top, inside walls, train clearance, bed coverage, visible rails, supports, and model budgets. No newly authored taper is used to force the core to fit an ordinary straight.

### Recessed-web northern interface

The structural web is the vertical concrete body below the track bed. In the accepted fan it lies approximately 6.963052 m from the paired centreline; the corresponding ordinary straight face lies approximately 7 m from that centreline. That exposed difference is about 36.949 mm per side. Measuring only the underside, ballast floor, and grey border tops missed this difference, even though those horizontal sections agreed within the existing 0.05 mm tolerance.

The [input-only extraction audit](../../01_assemblies/straight-stem-trumpet/evidence/fan-atomization-review.json) compares complete saved surfaces, materials, supports, texture phases, and outer-solid sections. It also continuously compares every saved surface in the retained fork's first 0.25 m of north collar with the matching straight. The new profile ID describes this recessed body; matching route classes remain separate facts. None of the physical tolerances is widened.

The original complete fan's northern native curve already had a small structural-web step. That transition belongs to its documented assembly placement, outside this core's shorter north boundary. The unchanged native neighbour supplies end-plane faces covering the entire inherited transition. Its exact closure proof does not establish universal full-profile compatibility between native and recessed-web pieces.

### Reproduce the checks

Run these commands from the repository root, the folder containing `custom-pieces/`, after the [shared dependency and native-input preparation](../../../../docs/BUILD_AND_INSTALL.md). Replace `/path/to/Plugins` with the existing NAM Plugins directory. Keep the quotes if the path contains spaces, and use a new output directory to preserve earlier evidence.

```sh
python3 -B custom-pieces/scp.py build --include hsr-component-l2-paired-fan-compact-core --output custom-pieces/dist/hsr-l2-fan-core-review --plugins '/path/to/Plugins'
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/hsr-l2-fan-core-review
```

The [portable input audit](../../01_assemblies/straight-stem-trumpet/evidence/fan-atomization-audit.py) documents a separate replay of the historical saved-input comparison. Its default mode replays embedded cap coverage only; its full mode requires the exact original saved DATs and reports that broader scope explicitly. Building, verifying, installing, and testing inside the game remain separate actions.

## 4. Game checks

Follow the [shared observation procedure](../../../../docs/TESTING.md#record-one-observation), using the generated exact cases below. Check placement, appearance, Route Query, visible train travel, forbidden movements, demolition, and save/reload separately. Record one rotation and direction at a time, with the actual neighbouring types and candidate hashes.

Only explicit human confirmation records a manual pass. Resource checks, software pictures, the original full fan's old image approval, and another assembly's results do not approve this new type's game cases.

## 5. Results and known issues

The generated checklist and observations below define the current result for each exact case. The north boundary requires the matching recessed-web profile; the curved southern cuts require their measured continuations. A common height, matching PATH endpoint, or matching outer deck width alone does not establish complete physical compatibility.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/8 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/8 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 43, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-core/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-core/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-57b9c10edb4753a8a805">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-57b9c10edb4753a8a805"></a>

**General: passed** — `software_resources-57b9c10edb4753a8a805`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual current descriptor-bound native saved build, exact parent-tile resource audit, selected actual PATH extraction, and connector freshness check; confirmed at: 2026-10-28T18:01:22.987704+00:00; evidence: [evidence/saved-resource-checks.json, evidence/fan-core-extraction.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-57b9c10edb4753a8a805">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-57b9c10edb4753a8a805"></a>

**General: passed** — `software_connectivity-57b9c10edb4753a8a805`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual current descriptor-bound native saved build, exact parent-tile resource audit, selected actual PATH extraction, and connector freshness check; confirmed at: 2026-10-28T18:01:22.987704+00:00; evidence: [evidence/saved-resource-checks.json, evidence/fan-core-extraction.json]; environment: {}

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-70fd682fc6b9d93afc79">[ ] unverified</a> | <a href="#case-in_game_render-91c7566e2d1d7b72e52c">[ ] unverified</a> | <a href="#case-in_game_render-04b6db0635a62373d078">[ ] unverified</a> | <a href="#case-in_game_render-ff3afef0e502ea325bde">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-70fd682fc6b9d93afc79"></a>

**0° CCW: unverified** — `in_game_render-70fd682fc6b9d93afc79`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-91c7566e2d1d7b72e52c"></a>

**90° CCW: unverified** — `in_game_render-91c7566e2d1d7b72e52c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-04b6db0635a62373d078"></a>

**180° CCW: unverified** — `in_game_render-04b6db0635a62373d078`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ff3afef0e502ea325bde"></a>

**270° CCW: unverified** — `in_game_render-ff3afef0e502ea325bde`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-70fd682fc6b9d93afc79">[ ] unverified</a> | <a href="#case-in_game_placement-91c7566e2d1d7b72e52c">[ ] unverified</a> | <a href="#case-in_game_placement-04b6db0635a62373d078">[ ] unverified</a> | <a href="#case-in_game_placement-ff3afef0e502ea325bde">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-70fd682fc6b9d93afc79"></a>

**0° CCW: unverified** — `in_game_placement-70fd682fc6b9d93afc79`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-91c7566e2d1d7b72e52c"></a>

**90° CCW: unverified** — `in_game_placement-91c7566e2d1d7b72e52c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-04b6db0635a62373d078"></a>

**180° CCW: unverified** — `in_game_placement-04b6db0635a62373d078`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ff3afef0e502ea325bde"></a>

**270° CCW: unverified** — `in_game_placement-ff3afef0e502ea325bde`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-70fd682fc6b9d93afc79">[ ] unverified</a> | <a href="#case-in_game_demolition-91c7566e2d1d7b72e52c">[ ] unverified</a> | <a href="#case-in_game_demolition-04b6db0635a62373d078">[ ] unverified</a> | <a href="#case-in_game_demolition-ff3afef0e502ea325bde">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-70fd682fc6b9d93afc79"></a>

**0° CCW: unverified** — `in_game_demolition-70fd682fc6b9d93afc79`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-91c7566e2d1d7b72e52c"></a>

**90° CCW: unverified** — `in_game_demolition-91c7566e2d1d7b72e52c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-04b6db0635a62373d078"></a>

**180° CCW: unverified** — `in_game_demolition-04b6db0635a62373d078`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ff3afef0e502ea325bde"></a>

**270° CCW: unverified** — `in_game_demolition-ff3afef0e502ea325bde`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-70fd682fc6b9d93afc79">[ ] unverified</a> | <a href="#case-in_game_save_reload-91c7566e2d1d7b72e52c">[ ] unverified</a> | <a href="#case-in_game_save_reload-04b6db0635a62373d078">[ ] unverified</a> | <a href="#case-in_game_save_reload-ff3afef0e502ea325bde">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-70fd682fc6b9d93afc79"></a>

**0° CCW: unverified** — `in_game_save_reload-70fd682fc6b9d93afc79`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-91c7566e2d1d7b72e52c"></a>

**90° CCW: unverified** — `in_game_save_reload-91c7566e2d1d7b72e52c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-04b6db0635a62373d078"></a>

**180° CCW: unverified** — `in_game_save_reload-04b6db0635a62373d078`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ff3afef0e502ea325bde"></a>

**270° CCW: unverified** — `in_game_save_reload-ff3afef0e502ea325bde`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_route_query-5b0c76d60139570dba48">[ ] unverified</a> | <a href="#case-in_game_route_query-0b3fee2ea2c2ad4f14eb">[ ] unverified</a> | <a href="#case-in_game_route_query-1e0dba72f2f8d351b2c2">[ ] unverified</a> | <a href="#case-in_game_route_query-6464efe38d27e83bf7ba">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout | — | <a href="#case-in_game_route_query-5ddc26ca3524d0653959">[ ] unverified</a> | <a href="#case-in_game_route_query-ff939fd9d16206071b8a">[ ] unverified</a> | <a href="#case-in_game_route_query-1f53c54c0b850698ce75">[ ] unverified</a> | <a href="#case-in_game_route_query-8e7cf07838d5287fc802">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_route_query-5b0c76d60139570dba48"></a>

**0° CCW: unverified** — `in_game_route_query-5b0c76d60139570dba48`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-0b3fee2ea2c2ad4f14eb"></a>

**90° CCW: unverified** — `in_game_route_query-0b3fee2ea2c2ad4f14eb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-1e0dba72f2f8d351b2c2"></a>

**180° CCW: unverified** — `in_game_route_query-1e0dba72f2f8d351b2c2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-6464efe38d27e83bf7ba"></a>

**270° CCW: unverified** — `in_game_route_query-6464efe38d27e83bf7ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout</summary>

<a id="case-in_game_route_query-5ddc26ca3524d0653959"></a>

**0° CCW: unverified** — `in_game_route_query-5ddc26ca3524d0653959`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-ff939fd9d16206071b8a"></a>

**90° CCW: unverified** — `in_game_route_query-ff939fd9d16206071b8a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-1f53c54c0b850698ce75"></a>

**180° CCW: unverified** — `in_game_route_query-1f53c54c0b850698ce75`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-8e7cf07838d5287fc802"></a>

**270° CCW: unverified** — `in_game_route_query-8e7cf07838d5287fc802`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_visible_travel-5b0c76d60139570dba48">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0b3fee2ea2c2ad4f14eb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1e0dba72f2f8d351b2c2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6464efe38d27e83bf7ba">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout | — | <a href="#case-in_game_visible_travel-5ddc26ca3524d0653959">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff939fd9d16206071b8a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1f53c54c0b850698ce75">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8e7cf07838d5287fc802">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_visible_travel-5b0c76d60139570dba48"></a>

**0° CCW: unverified** — `in_game_visible_travel-5b0c76d60139570dba48`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-0b3fee2ea2c2ad4f14eb"></a>

**90° CCW: unverified** — `in_game_visible_travel-0b3fee2ea2c2ad4f14eb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-1e0dba72f2f8d351b2c2"></a>

**180° CCW: unverified** — `in_game_visible_travel-1e0dba72f2f8d351b2c2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-6464efe38d27e83bf7ba"></a>

**270° CCW: unverified** — `in_game_visible_travel-6464efe38d27e83bf7ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout</summary>

<a id="case-in_game_visible_travel-5ddc26ca3524d0653959"></a>

**0° CCW: unverified** — `in_game_visible_travel-5ddc26ca3524d0653959`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-ff939fd9d16206071b8a"></a>

**90° CCW: unverified** — `in_game_visible_travel-ff939fd9d16206071b8a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-1f53c54c0b850698ce75"></a>

**180° CCW: unverified** — `in_game_visible_travel-1f53c54c0b850698ce75`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-8e7cf07838d5287fc802"></a>

**270° CCW: unverified** — `in_game_visible_travel-8e7cf07838d5287fc802`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a3457011d2eed1496e51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e50412f60ba8132a405c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2287dcbbeab7fbf61c9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f67d94c12524a45c288">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c7143e735af35441d23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6eb73456f25dc859c13a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de3d425e1d2db776f50e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1c95f4c0e206b8828ab">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a3457011d2eed1496e51"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a3457011d2eed1496e51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e50412f60ba8132a405c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e50412f60ba8132a405c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2287dcbbeab7fbf61c9d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2287dcbbeab7fbf61c9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f67d94c12524a45c288"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7f67d94c12524a45c288`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c7143e735af35441d23"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c7143e735af35441d23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6eb73456f25dc859c13a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6eb73456f25dc859c13a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de3d425e1d2db776f50e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de3d425e1d2db776f50e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1c95f4c0e206b8828ab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b1c95f4c0e206b8828ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-core:canonical-southeast | <a href="#case-preview_review-e8dab6d6285bb8c2a771">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-core:canonical-top | <a href="#case-preview_review-777f16828e11488ba372">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-core:connection-overview | <a href="#case-preview_review-a88bed6e6634ae40c020">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-core:canonical-southeast</summary>

<a id="case-preview_review-e8dab6d6285bb8c2a771"></a>

**General: unverified** — `preview_review-e8dab6d6285bb8c2a771`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-paired-fan-compact-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-core:canonical-top</summary>

<a id="case-preview_review-777f16828e11488ba372"></a>

**General: unverified** — `preview_review-777f16828e11488ba372`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-paired-fan-compact-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-core:connection-overview</summary>

<a id="case-preview_review-a88bed6e6634ae40c020"></a>

**General: unverified** — `preview_review-a88bed6e6634ae40c020`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-paired-fan-compact-core:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The original complete fan has been removed after its approach was separated into reusable straight tiles. Its accepted central border remains in every saved core cell; the [immutable extraction proof](evidence/fan-core-extraction.json) retains the measured predecessor identity and exact retained-resource comparisons. The [assembly-owned extraction decision and drawing](../../01_assemblies/straight-stem-trumpet/evidence/fan-atomization-review.json) explain the two straight cuts and the three resulting placements.

The new matching straight uses the original interior tile `[3,1]` twice. Replacing the original outer tile `[3,0]` changes triangulation and whole-repeat texture phases, removes fourteen redundant northern cap triangles, and replaces ten submicrometre texture slivers. Continuous saved-face coverage, exact support/material checks, and the retained native neighbour's closing faces bound that cleanup. The nine core models are preserved exactly; the extraction does not reinterpret a source layout change as a human or game pass.
