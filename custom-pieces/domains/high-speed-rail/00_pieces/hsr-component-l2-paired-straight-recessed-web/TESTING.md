---
title: "HSR Level 2 Paired Straight with Recessed Web: testing"
summary: "Define the exact extracted tile, distinct concrete profile, saved-resource checks, and separate game observations."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR Level 2 Paired Straight with Recessed Web: testing

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

The [piece overview](README.md) contains its pictures, placement steps, and intrinsic movement matrix. This document defines the exact checks, software evidence, observations, and limits.

## 1. Test scope

A port is one directional transport-path endpoint. A complete physical boundary also includes the surrounding concrete profile, tracks, direction, height, heading, and clearance. The generated connections describe this one-tile type; they do not certify an arbitrary neighbour.

Saved-resource validation, human preview review, game appearance, Route Query, and visible train travel are separate observations. A successful software build does not establish a game result, and a Route Query line does not prove that a train completed the journey.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | hsr / 7 / primary | out | [-2.0, -8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Read [Piece and placement](README.md#2-piece-and-placement) for the 1 × 1 footprint, supported directions, and required recessed-web neighbours.
2. Follow the [shared build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md) before a game trial. Use a disposable flat test city, the matching dependencies, and one declared rotation at a time.
3. Record the actual candidate file hashes, platform, game version, NAM profile, terrain, neighbouring types, and rotation through the [shared testing procedure](../../../../docs/TESTING.md).

These instructions prepare a future repeatable game check. They do not record installation or game success.

## 3. Software checks

The current [presentation-refresh record](evidence/presentation-refresh.json) identifies the canonical angled view, bright-green top grid, and connection overview rendered from the unchanged verified `dist/trumpet-fan-core-parts-final-01` resources. It records the current connector re-extraction and freshness checks, exact image hashes, and preserved observations. Earlier saved-resource and documentation-refresh reports retain their original native-check facts and picture fingerprints; this presentation refresh does not claim another geometry build or game observation.

### Exact saved interior tile

The canonical model comes from source cell `[3,1]` of the former complete Compact Paired Fan Join, identified as a measured historical source in the [immutable extraction proof](evidence/straight-extraction.json). The complete predecessor has been removed. The extraction allocates a separate one-tile identity and retains the canonical tile's five model zooms, PATH resource, five shadow resources, complete concrete body, rails, ballast, and single support. Its two routes are straight at local east −2 m and +2 m, travelling in opposite directions. Its support is centred in the tile.

The [native extraction proof](evidence/straight-extraction.json) records actual saved resource hashes and exact comparisons with the approved parent. The [current saved-resource report](evidence/saved-resource-checks.json) records independent checks of routes, geometry, supports, train clearance, and model budgets. Building the piece does not establish appearance or traffic inside the game.

### Complete concrete profile and extraction cleanup

The exposed structural web lies approximately 6.963052 m from the paired centreline through its body height, rather than the ordinary paired straight's approximately 7 m. The difference is about 36.949 mm per side. Both types still have matching horizontal underside, ballast, and grey border sections, and a 15 m outer concrete envelope. Those limited measurements do not prove full-body equality; the new type therefore uses its own recessed-web profile declaration.

The [assembly-owned input audit](../../01_assemblies/straight-stem-trumpet/evidence/fan-atomization-review.json) compares both original straight tiles through complete saved surfaces, material bytes, supports, repeating texture coordinates, and outer-solid sections around every native vertex-height transition. Non-cap geometry agrees within the unchanged 20 micrometre plane and in-plane check, and the complete 26-triangle support and material bytes are identical. Whole-model byte identity between the two original tiles is not claimed: their triangle counts are 438 and 365, their tessellation differs, and some texture coordinates differ by whole repeats.

The canonical interior tile has no longitudinal end caps. Replacing original cell `[3,0]` removes fourteen northern cap triangles and ten texture slivers whose longitudinal width is below one micrometre. Repeating the old outer tile instead would propagate exposed zero-thickness end fins into the new internal joins. The cleanup does not reshape the nine-cell core or widen physical tolerances.

At the trumpet's existing northern native-curve transition, the unchanged neighbour retains ten south-facing end-plane triangles. Continuous triangle-union coverage proves that they cover every removed original north-cap triangle, including the inherited web-width step; no new closure face is required. This is a placement-specific preserved transition, not a declaration that ordinary native and recessed-web profiles are equal.

### Reproduce the checks

Run these commands from the repository root, the folder containing `custom-pieces/`, after the [shared dependency and native-input preparation](../../../../docs/BUILD_AND_INSTALL.md). Replace `/path/to/Plugins` with the existing NAM Plugins directory, keep the quotes if needed, and use a new output directory to preserve earlier evidence.

```sh
python3 -B custom-pieces/scp.py build --include hsr-component-l2-paired-straight-recessed-web --output custom-pieces/dist/hsr-l2-recessed-straight-review --plugins '/path/to/Plugins'
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/hsr-l2-recessed-straight-review
```

The [portable extraction-input audit](../../01_assemblies/straight-stem-trumpet/evidence/fan-atomization-audit.py) separately replays the historical comparison. Its default mode checks embedded end-face coverage; its full mode requires the exact pinned saved parent and neighbour DATs. It reports those scopes separately and writes no source geometry or integration ledger.

## 4. Game checks

Use the generated exact cases below and the [shared observation procedure](../../../../docs/TESTING.md#record-one-observation). Check placement, appearance, Route Query, visible train travel, unavailable track transfers, demolition, and save/reload separately. Record the exact direction, rotation, neighbouring types, candidate hashes, and environment.

Only explicit human confirmation records a manual pass. The parent fan's old image observations, current software checks, and another assembly's results do not approve this new type's game cases.

## 5. Results and known issues

The generated checklist and observations below define current results for each exact case. Use a matching recessed-web physical boundary or a separately verified, documented transition. Matching PATH endpoints, nominal height, and outer deck width alone do not establish a complete neighbour fit.

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-straight-recessed-web/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-straight-recessed-web/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b8a2cc708326e6c9dc0d">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b8a2cc708326e6c9dc0d"></a>

**General: passed** — `software_resources-b8a2cc708326e6c9dc0d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual current descriptor-bound native saved build, exact parent-tile resource audit, selected actual PATH extraction, and connector freshness check; confirmed at: 2026-10-28T18:01:23.008888+00:00; evidence: [evidence/saved-resource-checks.json, evidence/straight-extraction.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b8a2cc708326e6c9dc0d">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b8a2cc708326e6c9dc0d"></a>

**General: passed** — `software_connectivity-b8a2cc708326e6c9dc0d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual current descriptor-bound native saved build, exact parent-tile resource audit, selected actual PATH extraction, and connector freshness check; confirmed at: 2026-10-28T18:01:23.008888+00:00; evidence: [evidence/saved-resource-checks.json, evidence/straight-extraction.json]; environment: {}

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-59e71d6d15e1c9c7a550">[ ] unverified</a> | <a href="#case-in_game_render-b86691899648516c73d7">[ ] unverified</a> | <a href="#case-in_game_render-e57a4bf5322a572a8f82">[ ] unverified</a> | <a href="#case-in_game_render-3e71aea3557fbef9b6f4">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-59e71d6d15e1c9c7a550"></a>

**0° CCW: unverified** — `in_game_render-59e71d6d15e1c9c7a550`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-b86691899648516c73d7"></a>

**90° CCW: unverified** — `in_game_render-b86691899648516c73d7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e57a4bf5322a572a8f82"></a>

**180° CCW: unverified** — `in_game_render-e57a4bf5322a572a8f82`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3e71aea3557fbef9b6f4"></a>

**270° CCW: unverified** — `in_game_render-3e71aea3557fbef9b6f4`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-59e71d6d15e1c9c7a550">[ ] unverified</a> | <a href="#case-in_game_placement-b86691899648516c73d7">[ ] unverified</a> | <a href="#case-in_game_placement-e57a4bf5322a572a8f82">[ ] unverified</a> | <a href="#case-in_game_placement-3e71aea3557fbef9b6f4">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-59e71d6d15e1c9c7a550"></a>

**0° CCW: unverified** — `in_game_placement-59e71d6d15e1c9c7a550`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-b86691899648516c73d7"></a>

**90° CCW: unverified** — `in_game_placement-b86691899648516c73d7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e57a4bf5322a572a8f82"></a>

**180° CCW: unverified** — `in_game_placement-e57a4bf5322a572a8f82`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3e71aea3557fbef9b6f4"></a>

**270° CCW: unverified** — `in_game_placement-3e71aea3557fbef9b6f4`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-59e71d6d15e1c9c7a550">[ ] unverified</a> | <a href="#case-in_game_demolition-b86691899648516c73d7">[ ] unverified</a> | <a href="#case-in_game_demolition-e57a4bf5322a572a8f82">[ ] unverified</a> | <a href="#case-in_game_demolition-3e71aea3557fbef9b6f4">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-59e71d6d15e1c9c7a550"></a>

**0° CCW: unverified** — `in_game_demolition-59e71d6d15e1c9c7a550`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-b86691899648516c73d7"></a>

**90° CCW: unverified** — `in_game_demolition-b86691899648516c73d7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e57a4bf5322a572a8f82"></a>

**180° CCW: unverified** — `in_game_demolition-e57a4bf5322a572a8f82`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3e71aea3557fbef9b6f4"></a>

**270° CCW: unverified** — `in_game_demolition-3e71aea3557fbef9b6f4`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-59e71d6d15e1c9c7a550">[ ] unverified</a> | <a href="#case-in_game_save_reload-b86691899648516c73d7">[ ] unverified</a> | <a href="#case-in_game_save_reload-e57a4bf5322a572a8f82">[ ] unverified</a> | <a href="#case-in_game_save_reload-3e71aea3557fbef9b6f4">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-59e71d6d15e1c9c7a550"></a>

**0° CCW: unverified** — `in_game_save_reload-59e71d6d15e1c9c7a550`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-b86691899648516c73d7"></a>

**90° CCW: unverified** — `in_game_save_reload-b86691899648516c73d7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e57a4bf5322a572a8f82"></a>

**180° CCW: unverified** — `in_game_save_reload-e57a4bf5322a572a8f82`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3e71aea3557fbef9b6f4"></a>

**270° CCW: unverified** — `in_game_save_reload-3e71aea3557fbef9b6f4`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_route_query-1d57267cb4171468a0bd">[ ] unverified</a> | <a href="#case-in_game_route_query-760ca4e788aa18e05679">[ ] unverified</a> | <a href="#case-in_game_route_query-fa92aadf87b16c3f687b">[ ] unverified</a> | <a href="#case-in_game_route_query-560c5cba39e89d2d9202">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_route_query-e8e9abdd02a4e8bf8831">[ ] unverified</a> | <a href="#case-in_game_route_query-0abe78e872684ae92f6f">[ ] unverified</a> | <a href="#case-in_game_route_query-f7340087315826e951c3">[ ] unverified</a> | <a href="#case-in_game_route_query-df5eb60b9eb3612cd12b">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_route_query-1d57267cb4171468a0bd"></a>

**0° CCW: unverified** — `in_game_route_query-1d57267cb4171468a0bd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-760ca4e788aa18e05679"></a>

**90° CCW: unverified** — `in_game_route_query-760ca4e788aa18e05679`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-fa92aadf87b16c3f687b"></a>

**180° CCW: unverified** — `in_game_route_query-fa92aadf87b16c3f687b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-560c5cba39e89d2d9202"></a>

**270° CCW: unverified** — `in_game_route_query-560c5cba39e89d2d9202`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_route_query-e8e9abdd02a4e8bf8831"></a>

**0° CCW: unverified** — `in_game_route_query-e8e9abdd02a4e8bf8831`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-0abe78e872684ae92f6f"></a>

**90° CCW: unverified** — `in_game_route_query-0abe78e872684ae92f6f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-f7340087315826e951c3"></a>

**180° CCW: unverified** — `in_game_route_query-f7340087315826e951c3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-df5eb60b9eb3612cd12b"></a>

**270° CCW: unverified** — `in_game_route_query-df5eb60b9eb3612cd12b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_visible_travel-1d57267cb4171468a0bd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-760ca4e788aa18e05679">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fa92aadf87b16c3f687b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-560c5cba39e89d2d9202">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_visible_travel-e8e9abdd02a4e8bf8831">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0abe78e872684ae92f6f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f7340087315826e951c3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-df5eb60b9eb3612cd12b">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_visible_travel-1d57267cb4171468a0bd"></a>

**0° CCW: unverified** — `in_game_visible_travel-1d57267cb4171468a0bd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-760ca4e788aa18e05679"></a>

**90° CCW: unverified** — `in_game_visible_travel-760ca4e788aa18e05679`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-fa92aadf87b16c3f687b"></a>

**180° CCW: unverified** — `in_game_visible_travel-fa92aadf87b16c3f687b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-560c5cba39e89d2d9202"></a>

**270° CCW: unverified** — `in_game_visible_travel-560c5cba39e89d2d9202`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_visible_travel-e8e9abdd02a4e8bf8831"></a>

**0° CCW: unverified** — `in_game_visible_travel-e8e9abdd02a4e8bf8831`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-0abe78e872684ae92f6f"></a>

**90° CCW: unverified** — `in_game_visible_travel-0abe78e872684ae92f6f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-f7340087315826e951c3"></a>

**180° CCW: unverified** — `in_game_visible_travel-f7340087315826e951c3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-df5eb60b9eb3612cd12b"></a>

**270° CCW: unverified** — `in_game_visible_travel-df5eb60b9eb3612cd12b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-963fd57cc0ae1392fdd4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ec140bb8141a74f4bfc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9da97ef48a042371863">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-317d4584ecddc5e83f56">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5ed9ae0a20c291e6963c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdb7e3442ea079f16060">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fdd6a25d3234e12165a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c1a9ab4b6d25a9d4df8">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-963fd57cc0ae1392fdd4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-963fd57cc0ae1392fdd4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ec140bb8141a74f4bfc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4ec140bb8141a74f4bfc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9da97ef48a042371863"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9da97ef48a042371863`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-317d4584ecddc5e83f56"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-317d4584ecddc5e83f56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5ed9ae0a20c291e6963c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5ed9ae0a20c291e6963c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdb7e3442ea079f16060"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bdb7e3442ea079f16060`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fdd6a25d3234e12165a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5fdd6a25d3234e12165a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c1a9ab4b6d25a9d4df8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2c1a9ab4b6d25a9d4df8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-paired-straight-recessed-web:canonical-southeast | <a href="#case-preview_review-8c3e391242a4ad599836">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-straight-recessed-web:canonical-top | <a href="#case-preview_review-4358f8f3af649c0baed0">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-straight-recessed-web:connection-overview | <a href="#case-preview_review-a40c515e02082685aa86">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-straight-recessed-web:canonical-southeast</summary>

<a id="case-preview_review-8c3e391242a4ad599836"></a>

**General: unverified** — `preview_review-8c3e391242a4ad599836`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-paired-straight-recessed-web:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-straight-recessed-web:canonical-top</summary>

<a id="case-preview_review-4358f8f3af649c0baed0"></a>

**General: unverified** — `preview_review-4358f8f3af649c0baed0`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-paired-straight-recessed-web:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-straight-recessed-web:connection-overview</summary>

<a id="case-preview_review-a40c515e02082685aa86"></a>

**General: unverified** — `preview_review-a40c515e02082685aa86`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-paired-straight-recessed-web:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The [coordinate-labelled extraction drawing and measured decision](../../01_assemblies/straight-stem-trumpet/evidence/fan-atomization-review.json) split the accepted eleven-cell fan into a nine-cell curved core and two copies of this straight. The existing ordinary straight was rejected because its complete structural profile differs. This separately allocated type preserves the fan's recessed web rather than changing the accepted core to fit another type.

The complete fan's superseded definition, standalone artwork, and registration have been removed. This piece's immutable extraction proof preserves its measured source identity and exact comparisons. Software and game results belong to this type's own cases; predecessor results are not copied as approvals.
