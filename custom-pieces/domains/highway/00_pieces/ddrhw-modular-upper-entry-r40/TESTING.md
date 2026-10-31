---
title: "Testing: RHW Ramp \u2014 Upper Entry Ramp \u2014 R40"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — Upper Entry Ramp — R40

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-upper-entry-r40` resources, its complete intrinsic journeys, and its separately placed joins in the [modular assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). The upper ramp retains a short original high collar whose measured minimum radius is approximately 29.50 m; only the newly authored circular section is R40.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-S-in-1` | road / 1 / primary | in | [3.768542, -40.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-0fdd8de01bc6c8b7b1c8` |
| `1-N-out-2` | road / 1 / primary | out | [8.142765, 8.0, 12.25824]; [0.37427694900935327, 0.927316971396647]; 0.296096203 | `path-interface-6724cf294af8c13dace3` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-S-in-1` → `1-N-out-2` | primary |

#### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including Wine or CrossOver. Follow the [shared build guide](../../../../docs/BUILD_AND_INSTALL.md) for exact input hashes and the captured Avenue dependency. Build the `ddrhw-modular-ramp-kit` set, then prepare the `modular-diagonal-diamond` Highways menu. Building does not install the result. Use flat terrain in a disposable city.

## 3. Software checks

From the repository root, run `python3 -B tools/run_tests.py`. After a local build, run `python3 -B custom-pieces/scp.py verify --output <build directory>`. The domain verifier reads saved PATH and S3D resources: it checks literal ownership, traffic direction, joins, grades below the 30% experimental ceiling, exact stamp references, adaptive resources where declared, model topology, and car corridors. The assembly evidence adds physical joining-profile and support checks. A software pass cannot confirm game appearance or vehicle travel.

## 4. Game checks

Place this component as described in the README and complete the assembly. Inspect each of the four rotations after clicking, rather than relying on the placement preview. For the stamp and terminals, extend the ordinary Avenue, develop nearby zoning, and inspect whether the sidewalk appears and rotates with the roads. Use Route Query on each permitted movement, watch a car complete it, confirm opposing-carriageway turns remain unavailable, save, close the city, and reload. Record an observation only for the exact checklist case actually inspected.

## 5. Results and known issues

The independent source tests and saved-resource reports have separate scopes. The generated checklist below retains their case states and explicit human observations. Every game result for this new subject starts unverified. The experimental 30% grade ceiling exceeds normal real-world highway practice; this compact game family does not claim real-road design approval or native MIS/FLEX interoperability.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/4 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 29, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-upper-entry-r40/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-upper-entry-r40/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-d3975890182d15048d6c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-d3975890182d15048d6c"></a>

**General: unverified** — `software_resources-d3975890182d15048d6c`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-d3975890182d15048d6c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-d3975890182d15048d6c"></a>

**General: unverified** — `software_connectivity-d3975890182d15048d6c`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-9ab11444c9d7b0c8ab06">[ ] unverified</a> | <a href="#case-in_game_render-3aececbd614276ea85ee">[ ] unverified</a> | <a href="#case-in_game_render-3b0746fd4c01df5ba9f2">[ ] unverified</a> | <a href="#case-in_game_render-62e8c027039d03c7731d">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-9ab11444c9d7b0c8ab06"></a>

**0° CCW: unverified** — `in_game_render-9ab11444c9d7b0c8ab06`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3aececbd614276ea85ee"></a>

**90° CCW: unverified** — `in_game_render-3aececbd614276ea85ee`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3b0746fd4c01df5ba9f2"></a>

**180° CCW: unverified** — `in_game_render-3b0746fd4c01df5ba9f2`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-62e8c027039d03c7731d"></a>

**270° CCW: unverified** — `in_game_render-62e8c027039d03c7731d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-9ab11444c9d7b0c8ab06">[ ] unverified</a> | <a href="#case-in_game_placement-3aececbd614276ea85ee">[ ] unverified</a> | <a href="#case-in_game_placement-3b0746fd4c01df5ba9f2">[ ] unverified</a> | <a href="#case-in_game_placement-62e8c027039d03c7731d">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-9ab11444c9d7b0c8ab06"></a>

**0° CCW: unverified** — `in_game_placement-9ab11444c9d7b0c8ab06`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3aececbd614276ea85ee"></a>

**90° CCW: unverified** — `in_game_placement-3aececbd614276ea85ee`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3b0746fd4c01df5ba9f2"></a>

**180° CCW: unverified** — `in_game_placement-3b0746fd4c01df5ba9f2`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-62e8c027039d03c7731d"></a>

**270° CCW: unverified** — `in_game_placement-62e8c027039d03c7731d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-9ab11444c9d7b0c8ab06">[ ] unverified</a> | <a href="#case-in_game_demolition-3aececbd614276ea85ee">[ ] unverified</a> | <a href="#case-in_game_demolition-3b0746fd4c01df5ba9f2">[ ] unverified</a> | <a href="#case-in_game_demolition-62e8c027039d03c7731d">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-9ab11444c9d7b0c8ab06"></a>

**0° CCW: unverified** — `in_game_demolition-9ab11444c9d7b0c8ab06`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3aececbd614276ea85ee"></a>

**90° CCW: unverified** — `in_game_demolition-3aececbd614276ea85ee`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3b0746fd4c01df5ba9f2"></a>

**180° CCW: unverified** — `in_game_demolition-3b0746fd4c01df5ba9f2`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-62e8c027039d03c7731d"></a>

**270° CCW: unverified** — `in_game_demolition-62e8c027039d03c7731d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-9ab11444c9d7b0c8ab06">[ ] unverified</a> | <a href="#case-in_game_save_reload-3aececbd614276ea85ee">[ ] unverified</a> | <a href="#case-in_game_save_reload-3b0746fd4c01df5ba9f2">[ ] unverified</a> | <a href="#case-in_game_save_reload-62e8c027039d03c7731d">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-9ab11444c9d7b0c8ab06"></a>

**0° CCW: unverified** — `in_game_save_reload-9ab11444c9d7b0c8ab06`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3aececbd614276ea85ee"></a>

**90° CCW: unverified** — `in_game_save_reload-3aececbd614276ea85ee`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3b0746fd4c01df5ba9f2"></a>

**180° CCW: unverified** — `in_game_save_reload-3b0746fd4c01df5ba9f2`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-62e8c027039d03c7731d"></a>

**270° CCW: unverified** — `in_game_save_reload-62e8c027039d03c7731d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2 | — | <a href="#case-in_game_route_query-e3b351baf41a6d4a3f95">[ ] unverified</a> | <a href="#case-in_game_route_query-982054d4391019f8e275">[ ] unverified</a> | <a href="#case-in_game_route_query-177bbb65fdb36bcae1f1">[ ] unverified</a> | <a href="#case-in_game_route_query-486d1aaabaa04665cdea">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2</summary>

<a id="case-in_game_route_query-e3b351baf41a6d4a3f95"></a>

**0° CCW: unverified** — `in_game_route_query-e3b351baf41a6d4a3f95`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-982054d4391019f8e275"></a>

**90° CCW: unverified** — `in_game_route_query-982054d4391019f8e275`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-177bbb65fdb36bcae1f1"></a>

**180° CCW: unverified** — `in_game_route_query-177bbb65fdb36bcae1f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-486d1aaabaa04665cdea"></a>

**270° CCW: unverified** — `in_game_route_query-486d1aaabaa04665cdea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2 | — | <a href="#case-in_game_visible_travel-e3b351baf41a6d4a3f95">[ ] unverified</a> | <a href="#case-in_game_visible_travel-982054d4391019f8e275">[ ] unverified</a> | <a href="#case-in_game_visible_travel-177bbb65fdb36bcae1f1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-486d1aaabaa04665cdea">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2</summary>

<a id="case-in_game_visible_travel-e3b351baf41a6d4a3f95"></a>

**0° CCW: unverified** — `in_game_visible_travel-e3b351baf41a6d4a3f95`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-982054d4391019f8e275"></a>

**90° CCW: unverified** — `in_game_visible_travel-982054d4391019f8e275`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-177bbb65fdb36bcae1f1"></a>

**180° CCW: unverified** — `in_game_visible_travel-177bbb65fdb36bcae1f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-486d1aaabaa04665cdea"></a>

**270° CCW: unverified** — `in_game_visible_travel-486d1aaabaa04665cdea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-1>1-N-out-2; entry: 1-S-in-1; exit: 1-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-upper-entry-r40:canonical-southeast | <a href="#case-preview_review-eea6c983e06045ca8116">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-upper-entry-r40:canonical-top | <a href="#case-preview_review-5b981f91895a68f22082">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-upper-entry-r40:connection-overview | <a href="#case-preview_review-e87d6800dc0dd9c4a529">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-entry-r40:canonical-southeast</summary>

<a id="case-preview_review-eea6c983e06045ca8116"></a>

**General: unverified** — `preview_review-eea6c983e06045ca8116`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-entry-r40:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-entry-r40:canonical-top</summary>

<a id="case-preview_review-5b981f91895a68f22082"></a>

**General: unverified** — `preview_review-5b981f91895a68f22082`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-entry-r40:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-upper-entry-r40:connection-overview</summary>

<a id="case-preview_review-e87d6800dc0dd9c4a529"></a>

**General: unverified** — `preview_review-e87d6800dc0dd9c4a529`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-upper-entry-r40:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The modular experiment preserves the accepted compact diamond on its original branch. A new highway stamp retains 25 canonical cell models and all 27 canonical PATHs; two Avenue-only cells restore pristine native pavement. Four R40 ramp continuations and two new terminals attach separately. The retained compact grades and junctions remain independently available under their original identifiers.
