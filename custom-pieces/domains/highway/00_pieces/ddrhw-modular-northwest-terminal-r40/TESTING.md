---
title: "Testing: RHW Ramp \u2014 Northwest Avenue Ramp Terminal \u2014 R40"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — Northwest Avenue Ramp Terminal — R40

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-northwest-terminal-r40` resources, its complete intrinsic journeys, and its separately placed joins in the [modular assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). These are fixed-height click-to-place components. Their geometry does not follow sloping terrain.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-in-1` | road / 1 / primary | in | [-8.0, -3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-W-in-2` | road / 1 / primary | in | [-8.0, 3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-N-out-3` | road / 1 / primary | out | [-3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-N-out-4` | road / 1 / primary | out | [3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-S-out-5` | road / 1 / primary | out | [12.231458, -40.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-0aa85c099c852f580fff` |
| `1-S-out-6` | road / 1 / primary | out | [28.8, -40.0, 0.0]; [0.7071067811865478, -0.7071067811865474]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-S-out-7` | road / 1 / primary | out | [35.2, -40.0, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-E-in-8` | road / 1 / primary | in | [40.0, -35.2, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-E-in-9` | road / 1 / primary | in | [40.0, -28.8, 0.0]; [-0.7071067811865474, 0.7071067811865478]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-in-10` | road / 1 / primary | in | [40.0, -12.231458, 0.0]; [-1.0, 0.0]; 0.0 | `path-interface-0fdd8de01bc6c8b7b1c8` |
| `2-W-in-1` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-N-out-2` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-S-out-3` | pedestrian / 2 / primary | out | [24.7, -40.0, 0.0]; [0.7071067811865458, -0.7071067811865493]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-E-in-4` | pedestrian / 2 / primary | in | [40.0, -24.7, 0.0]; [-0.7071067811865493, 0.7071067811865458]; 0.0 | `path-interface-ef45fb4474012bf121a0` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-1` → `1-S-out-5` | primary |
| road | `1-W-in-1` → `1-S-out-6` | primary |
| road | `1-W-in-2` → `1-S-out-7` | primary |
| road | `1-E-in-8` → `1-N-out-3` | primary |
| road | `1-E-in-9` → `1-N-out-4` | primary |
| road | `1-E-in-10` → `1-N-out-4` | primary |
| pedestrian | `2-W-in-1` → `2-S-out-3` | primary |
| pedestrian | `2-E-in-4` → `2-N-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-1` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-8` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-S-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-S-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-northwest-terminal-r40/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-northwest-terminal-r40/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-028a031f9d17c33e3fed">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-028a031f9d17c33e3fed"></a>

**General: unverified** — `software_resources-028a031f9d17c33e3fed`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-028a031f9d17c33e3fed">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-028a031f9d17c33e3fed"></a>

**General: unverified** — `software_connectivity-028a031f9d17c33e3fed`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-e2a49c50612fed492b91">[ ] unverified</a> | <a href="#case-in_game_render-9e3266cf168a1d572603">[ ] unverified</a> | <a href="#case-in_game_render-e7ce6f13dc3d01f0c584">[ ] unverified</a> | <a href="#case-in_game_render-e52404218a9f9bb1ee63">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-e2a49c50612fed492b91"></a>

**0° CCW: unverified** — `in_game_render-e2a49c50612fed492b91`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9e3266cf168a1d572603"></a>

**90° CCW: unverified** — `in_game_render-9e3266cf168a1d572603`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e7ce6f13dc3d01f0c584"></a>

**180° CCW: unverified** — `in_game_render-e7ce6f13dc3d01f0c584`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e52404218a9f9bb1ee63"></a>

**270° CCW: unverified** — `in_game_render-e52404218a9f9bb1ee63`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-e2a49c50612fed492b91">[ ] unverified</a> | <a href="#case-in_game_placement-9e3266cf168a1d572603">[ ] unverified</a> | <a href="#case-in_game_placement-e7ce6f13dc3d01f0c584">[ ] unverified</a> | <a href="#case-in_game_placement-e52404218a9f9bb1ee63">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-e2a49c50612fed492b91"></a>

**0° CCW: unverified** — `in_game_placement-e2a49c50612fed492b91`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9e3266cf168a1d572603"></a>

**90° CCW: unverified** — `in_game_placement-9e3266cf168a1d572603`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e7ce6f13dc3d01f0c584"></a>

**180° CCW: unverified** — `in_game_placement-e7ce6f13dc3d01f0c584`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e52404218a9f9bb1ee63"></a>

**270° CCW: unverified** — `in_game_placement-e52404218a9f9bb1ee63`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-e2a49c50612fed492b91">[ ] unverified</a> | <a href="#case-in_game_demolition-9e3266cf168a1d572603">[ ] unverified</a> | <a href="#case-in_game_demolition-e7ce6f13dc3d01f0c584">[ ] unverified</a> | <a href="#case-in_game_demolition-e52404218a9f9bb1ee63">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-e2a49c50612fed492b91"></a>

**0° CCW: unverified** — `in_game_demolition-e2a49c50612fed492b91`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9e3266cf168a1d572603"></a>

**90° CCW: unverified** — `in_game_demolition-9e3266cf168a1d572603`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e7ce6f13dc3d01f0c584"></a>

**180° CCW: unverified** — `in_game_demolition-e7ce6f13dc3d01f0c584`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e52404218a9f9bb1ee63"></a>

**270° CCW: unverified** — `in_game_demolition-e52404218a9f9bb1ee63`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-e2a49c50612fed492b91">[ ] unverified</a> | <a href="#case-in_game_save_reload-9e3266cf168a1d572603">[ ] unverified</a> | <a href="#case-in_game_save_reload-e7ce6f13dc3d01f0c584">[ ] unverified</a> | <a href="#case-in_game_save_reload-e52404218a9f9bb1ee63">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-e2a49c50612fed492b91"></a>

**0° CCW: unverified** — `in_game_save_reload-e2a49c50612fed492b91`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9e3266cf168a1d572603"></a>

**90° CCW: unverified** — `in_game_save_reload-9e3266cf168a1d572603`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e7ce6f13dc3d01f0c584"></a>

**180° CCW: unverified** — `in_game_save_reload-e7ce6f13dc3d01f0c584`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e52404218a9f9bb1ee63"></a>

**270° CCW: unverified** — `in_game_save_reload-e52404218a9f9bb1ee63`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5 | — | <a href="#case-in_game_route_query-ce8d4363c2deb92734aa">[ ] unverified</a> | <a href="#case-in_game_route_query-09ab8b0ec4068e43849d">[ ] unverified</a> | <a href="#case-in_game_route_query-0589706e9f93316abacc">[ ] unverified</a> | <a href="#case-in_game_route_query-2f5a548560c288dab2c1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6 | — | <a href="#case-in_game_route_query-defbaeda3f166704bd68">[ ] unverified</a> | <a href="#case-in_game_route_query-604aef478fb18c265347">[ ] unverified</a> | <a href="#case-in_game_route_query-d5119cdf80998fecdef6">[ ] unverified</a> | <a href="#case-in_game_route_query-2f8a6c9b5a045231a5d2">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7 | — | <a href="#case-in_game_route_query-e8f749a1ea8aa424773f">[ ] unverified</a> | <a href="#case-in_game_route_query-e8d8a9389685f2251c3d">[ ] unverified</a> | <a href="#case-in_game_route_query-650c02ae56d54ef50034">[ ] unverified</a> | <a href="#case-in_game_route_query-36db7666de35cad99dc0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3 | — | <a href="#case-in_game_route_query-17b760468406f1fc497b">[ ] unverified</a> | <a href="#case-in_game_route_query-5312b368e03500a47b63">[ ] unverified</a> | <a href="#case-in_game_route_query-1b9c62d1eb6393d80263">[ ] unverified</a> | <a href="#case-in_game_route_query-7fd9ab6eff629d7db4c8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4 | — | <a href="#case-in_game_route_query-9212b76073da68376b89">[ ] unverified</a> | <a href="#case-in_game_route_query-2d745cd81ab3958f86c4">[ ] unverified</a> | <a href="#case-in_game_route_query-fa87c1e3e9750490b6c7">[ ] unverified</a> | <a href="#case-in_game_route_query-30a07a2a9170367664c3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4 | — | <a href="#case-in_game_route_query-1d2800bc2cd3da3b60cc">[ ] unverified</a> | <a href="#case-in_game_route_query-238ae7849d9a45833a37">[ ] unverified</a> | <a href="#case-in_game_route_query-d2da4ba9f1f9c5203e30">[ ] unverified</a> | <a href="#case-in_game_route_query-73aecc00d13eae56fa8c">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5</summary>

<a id="case-in_game_route_query-ce8d4363c2deb92734aa"></a>

**0° CCW: unverified** — `in_game_route_query-ce8d4363c2deb92734aa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5.

No observation recorded.

<a id="case-in_game_route_query-09ab8b0ec4068e43849d"></a>

**90° CCW: unverified** — `in_game_route_query-09ab8b0ec4068e43849d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5.

No observation recorded.

<a id="case-in_game_route_query-0589706e9f93316abacc"></a>

**180° CCW: unverified** — `in_game_route_query-0589706e9f93316abacc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5.

No observation recorded.

<a id="case-in_game_route_query-2f5a548560c288dab2c1"></a>

**270° CCW: unverified** — `in_game_route_query-2f5a548560c288dab2c1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6</summary>

<a id="case-in_game_route_query-defbaeda3f166704bd68"></a>

**0° CCW: unverified** — `in_game_route_query-defbaeda3f166704bd68`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_route_query-604aef478fb18c265347"></a>

**90° CCW: unverified** — `in_game_route_query-604aef478fb18c265347`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_route_query-d5119cdf80998fecdef6"></a>

**180° CCW: unverified** — `in_game_route_query-d5119cdf80998fecdef6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_route_query-2f8a6c9b5a045231a5d2"></a>

**270° CCW: unverified** — `in_game_route_query-2f8a6c9b5a045231a5d2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7</summary>

<a id="case-in_game_route_query-e8f749a1ea8aa424773f"></a>

**0° CCW: unverified** — `in_game_route_query-e8f749a1ea8aa424773f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-e8d8a9389685f2251c3d"></a>

**90° CCW: unverified** — `in_game_route_query-e8d8a9389685f2251c3d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-650c02ae56d54ef50034"></a>

**180° CCW: unverified** — `in_game_route_query-650c02ae56d54ef50034`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-36db7666de35cad99dc0"></a>

**270° CCW: unverified** — `in_game_route_query-36db7666de35cad99dc0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3</summary>

<a id="case-in_game_route_query-17b760468406f1fc497b"></a>

**0° CCW: unverified** — `in_game_route_query-17b760468406f1fc497b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-5312b368e03500a47b63"></a>

**90° CCW: unverified** — `in_game_route_query-5312b368e03500a47b63`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-1b9c62d1eb6393d80263"></a>

**180° CCW: unverified** — `in_game_route_query-1b9c62d1eb6393d80263`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-7fd9ab6eff629d7db4c8"></a>

**270° CCW: unverified** — `in_game_route_query-7fd9ab6eff629d7db4c8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4</summary>

<a id="case-in_game_route_query-9212b76073da68376b89"></a>

**0° CCW: unverified** — `in_game_route_query-9212b76073da68376b89`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-2d745cd81ab3958f86c4"></a>

**90° CCW: unverified** — `in_game_route_query-2d745cd81ab3958f86c4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-fa87c1e3e9750490b6c7"></a>

**180° CCW: unverified** — `in_game_route_query-fa87c1e3e9750490b6c7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-30a07a2a9170367664c3"></a>

**270° CCW: unverified** — `in_game_route_query-30a07a2a9170367664c3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4</summary>

<a id="case-in_game_route_query-1d2800bc2cd3da3b60cc"></a>

**0° CCW: unverified** — `in_game_route_query-1d2800bc2cd3da3b60cc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-238ae7849d9a45833a37"></a>

**90° CCW: unverified** — `in_game_route_query-238ae7849d9a45833a37`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-d2da4ba9f1f9c5203e30"></a>

**180° CCW: unverified** — `in_game_route_query-d2da4ba9f1f9c5203e30`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-73aecc00d13eae56fa8c"></a>

**270° CCW: unverified** — `in_game_route_query-73aecc00d13eae56fa8c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5 | — | <a href="#case-in_game_visible_travel-ce8d4363c2deb92734aa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-09ab8b0ec4068e43849d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0589706e9f93316abacc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2f5a548560c288dab2c1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6 | — | <a href="#case-in_game_visible_travel-defbaeda3f166704bd68">[ ] unverified</a> | <a href="#case-in_game_visible_travel-604aef478fb18c265347">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d5119cdf80998fecdef6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2f8a6c9b5a045231a5d2">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7 | — | <a href="#case-in_game_visible_travel-e8f749a1ea8aa424773f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e8d8a9389685f2251c3d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-650c02ae56d54ef50034">[ ] unverified</a> | <a href="#case-in_game_visible_travel-36db7666de35cad99dc0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3 | — | <a href="#case-in_game_visible_travel-17b760468406f1fc497b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5312b368e03500a47b63">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1b9c62d1eb6393d80263">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7fd9ab6eff629d7db4c8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4 | — | <a href="#case-in_game_visible_travel-9212b76073da68376b89">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2d745cd81ab3958f86c4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fa87c1e3e9750490b6c7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-30a07a2a9170367664c3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4 | — | <a href="#case-in_game_visible_travel-1d2800bc2cd3da3b60cc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-238ae7849d9a45833a37">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d2da4ba9f1f9c5203e30">[ ] unverified</a> | <a href="#case-in_game_visible_travel-73aecc00d13eae56fa8c">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5</summary>

<a id="case-in_game_visible_travel-ce8d4363c2deb92734aa"></a>

**0° CCW: unverified** — `in_game_visible_travel-ce8d4363c2deb92734aa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-09ab8b0ec4068e43849d"></a>

**90° CCW: unverified** — `in_game_visible_travel-09ab8b0ec4068e43849d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-0589706e9f93316abacc"></a>

**180° CCW: unverified** — `in_game_visible_travel-0589706e9f93316abacc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-2f5a548560c288dab2c1"></a>

**270° CCW: unverified** — `in_game_visible_travel-2f5a548560c288dab2c1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-5; entry: 1-W-in-1; exit: 1-S-out-5.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6</summary>

<a id="case-in_game_visible_travel-defbaeda3f166704bd68"></a>

**0° CCW: unverified** — `in_game_visible_travel-defbaeda3f166704bd68`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-604aef478fb18c265347"></a>

**90° CCW: unverified** — `in_game_visible_travel-604aef478fb18c265347`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-d5119cdf80998fecdef6"></a>

**180° CCW: unverified** — `in_game_visible_travel-d5119cdf80998fecdef6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-2f8a6c9b5a045231a5d2"></a>

**270° CCW: unverified** — `in_game_visible_travel-2f8a6c9b5a045231a5d2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-6; entry: 1-W-in-1; exit: 1-S-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7</summary>

<a id="case-in_game_visible_travel-e8f749a1ea8aa424773f"></a>

**0° CCW: unverified** — `in_game_visible_travel-e8f749a1ea8aa424773f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-e8d8a9389685f2251c3d"></a>

**90° CCW: unverified** — `in_game_visible_travel-e8d8a9389685f2251c3d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-650c02ae56d54ef50034"></a>

**180° CCW: unverified** — `in_game_visible_travel-650c02ae56d54ef50034`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-36db7666de35cad99dc0"></a>

**270° CCW: unverified** — `in_game_visible_travel-36db7666de35cad99dc0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-7; entry: 1-W-in-2; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3</summary>

<a id="case-in_game_visible_travel-17b760468406f1fc497b"></a>

**0° CCW: unverified** — `in_game_visible_travel-17b760468406f1fc497b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-5312b368e03500a47b63"></a>

**90° CCW: unverified** — `in_game_visible_travel-5312b368e03500a47b63`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-1b9c62d1eb6393d80263"></a>

**180° CCW: unverified** — `in_game_visible_travel-1b9c62d1eb6393d80263`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-7fd9ab6eff629d7db4c8"></a>

**270° CCW: unverified** — `in_game_visible_travel-7fd9ab6eff629d7db4c8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-8>1-N-out-3; entry: 1-E-in-8; exit: 1-N-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4</summary>

<a id="case-in_game_visible_travel-9212b76073da68376b89"></a>

**0° CCW: unverified** — `in_game_visible_travel-9212b76073da68376b89`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-2d745cd81ab3958f86c4"></a>

**90° CCW: unverified** — `in_game_visible_travel-2d745cd81ab3958f86c4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-fa87c1e3e9750490b6c7"></a>

**180° CCW: unverified** — `in_game_visible_travel-fa87c1e3e9750490b6c7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-30a07a2a9170367664c3"></a>

**270° CCW: unverified** — `in_game_visible_travel-30a07a2a9170367664c3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-4; entry: 1-E-in-9; exit: 1-N-out-4.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4</summary>

<a id="case-in_game_visible_travel-1d2800bc2cd3da3b60cc"></a>

**0° CCW: unverified** — `in_game_visible_travel-1d2800bc2cd3da3b60cc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-238ae7849d9a45833a37"></a>

**90° CCW: unverified** — `in_game_visible_travel-238ae7849d9a45833a37`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-d2da4ba9f1f9c5203e30"></a>

**180° CCW: unverified** — `in_game_visible_travel-d2da4ba9f1f9c5203e30`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-73aecc00d13eae56fa8c"></a>

**270° CCW: unverified** — `in_game_visible_travel-73aecc00d13eae56fa8c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3 | — | <a href="#case-in_game_route_query-0fe1ce6a13ac3561200f">[ ] unverified</a> | <a href="#case-in_game_route_query-65836432f61ed3c8ffda">[ ] unverified</a> | <a href="#case-in_game_route_query-117fbcfd6c9fbb7b29d6">[ ] unverified</a> | <a href="#case-in_game_route_query-81141a41dfd3b28c389c">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2 | — | <a href="#case-in_game_route_query-69fde5827566fb64fbf9">[ ] unverified</a> | <a href="#case-in_game_route_query-f0734d54f037207d94d7">[ ] unverified</a> | <a href="#case-in_game_route_query-2d2e3da535817e61e6a3">[ ] unverified</a> | <a href="#case-in_game_route_query-cae043e867782fb772dd">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3</summary>

<a id="case-in_game_route_query-0fe1ce6a13ac3561200f"></a>

**0° CCW: unverified** — `in_game_route_query-0fe1ce6a13ac3561200f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-65836432f61ed3c8ffda"></a>

**90° CCW: unverified** — `in_game_route_query-65836432f61ed3c8ffda`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-117fbcfd6c9fbb7b29d6"></a>

**180° CCW: unverified** — `in_game_route_query-117fbcfd6c9fbb7b29d6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-81141a41dfd3b28c389c"></a>

**270° CCW: unverified** — `in_game_route_query-81141a41dfd3b28c389c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2</summary>

<a id="case-in_game_route_query-69fde5827566fb64fbf9"></a>

**0° CCW: unverified** — `in_game_route_query-69fde5827566fb64fbf9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-f0734d54f037207d94d7"></a>

**90° CCW: unverified** — `in_game_route_query-f0734d54f037207d94d7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-2d2e3da535817e61e6a3"></a>

**180° CCW: unverified** — `in_game_route_query-2d2e3da535817e61e6a3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-cae043e867782fb772dd"></a>

**270° CCW: unverified** — `in_game_route_query-cae043e867782fb772dd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3 | — | <a href="#case-in_game_visible_travel-0fe1ce6a13ac3561200f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-65836432f61ed3c8ffda">[ ] unverified</a> | <a href="#case-in_game_visible_travel-117fbcfd6c9fbb7b29d6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-81141a41dfd3b28c389c">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2 | — | <a href="#case-in_game_visible_travel-69fde5827566fb64fbf9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f0734d54f037207d94d7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2d2e3da535817e61e6a3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cae043e867782fb772dd">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3</summary>

<a id="case-in_game_visible_travel-0fe1ce6a13ac3561200f"></a>

**0° CCW: unverified** — `in_game_visible_travel-0fe1ce6a13ac3561200f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-65836432f61ed3c8ffda"></a>

**90° CCW: unverified** — `in_game_visible_travel-65836432f61ed3c8ffda`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-117fbcfd6c9fbb7b29d6"></a>

**180° CCW: unverified** — `in_game_visible_travel-117fbcfd6c9fbb7b29d6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-81141a41dfd3b28c389c"></a>

**270° CCW: unverified** — `in_game_visible_travel-81141a41dfd3b28c389c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2</summary>

<a id="case-in_game_visible_travel-69fde5827566fb64fbf9"></a>

**0° CCW: unverified** — `in_game_visible_travel-69fde5827566fb64fbf9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-f0734d54f037207d94d7"></a>

**90° CCW: unverified** — `in_game_visible_travel-f0734d54f037207d94d7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-2d2e3da535817e61e6a3"></a>

**180° CCW: unverified** — `in_game_visible_travel-2d2e3da535817e61e6a3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-cae043e867782fb772dd"></a>

**270° CCW: unverified** — `in_game_visible_travel-cae043e867782fb772dd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 76 cases; unverified: 76</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-794f78df7ace66b31445">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca2c3d4ddb2f6f279caa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f20a71831953e58924a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da8d0cfcf2d70b6028e1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2bc30df448265ac5e99d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e248b1de5690497e8ce8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb5b477bda5296c82482">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5dc7a2d15008e874b5f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d3db8448714a53559a9f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d88a369130714cbbfea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac5cb3389d05ed099d50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60abc4962902341772c4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-90d004fd56a2b9c4d252">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-649004226a417c7c59e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e56776a594c4d437d82d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5421983ba4c2c85466b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-726eb705aea6cbd00c4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c734393ae253585a3d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ecf7f0e388680ece1fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18c4a341a41edeacb8a5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4f268d3b8156d6c5e5be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90853391c0dec1a618c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d1b8be30cf5ae785ba0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a0d0e298d0999b5d7a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8c88672b3ce6be33722f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20e94c3badfddcb6e65b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0166539f1c00b53c572b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05b3aa114f2fd116a81e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e8600b0532417eee9cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0406a326d2e420837fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7edd7c5ebc406834c387">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af6daa086eaea6dc8ec3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a39bb5b7461edc3c2342">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53d54aeea40fb28cf7f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a05c94a73e7724cb0d38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-296d699a86483658fbd1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-376cc0f3765aded4d254">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b7a176e7099e72882ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c22062251c8cdd94b0c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63687014b7c280dbb61c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-218eb53cc5c937aae5a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c23b60c54832953b287">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea99749bdfde553bc7de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70d4982775ec5ab64bb8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-11c69b118241d661bde9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a167cc5f5eac61f4f7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32fa79d9c8f54f426dce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62791a263258f9afb393">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a9e0d1e17d136d3fe9f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bec4fb422d2af2652f58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9233e162ec6da061c5ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-615b9ca9412a90d92503">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d81ac7d3f50d4613227">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d07f75076d75f240561e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35be2750d443e9d30521">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff430b4562417f678e22">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7191a3d028818282e6df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32e22c6152bb5bc4e551">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a1912612d7c8c708e2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcd35463b773a14c2114">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9d5cada0022479ec9ff5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18ccb7593cd5b8eace2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03580e26fd1f6f8c6b85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6dc01b9d80ab517729b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95d423d97ded68229b38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e46303f10d3ef2d84faf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dc1b91e22e2eafb074f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-414853d3e284bcd4a8ed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c1fa89eaacc5a17049b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ee4802a25f6afeb6e5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ac17cfe81d1a361f90a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b2e61569df761256fa7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2d5f61e8d75d6067f2fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f530d17ac00e6d2f1aae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3a98c683f29f19c2490">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45d2e74e9b8e11798b2d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-794f78df7ace66b31445"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-794f78df7ace66b31445`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca2c3d4ddb2f6f279caa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ca2c3d4ddb2f6f279caa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f20a71831953e58924a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f20a71831953e58924a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da8d0cfcf2d70b6028e1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-da8d0cfcf2d70b6028e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2bc30df448265ac5e99d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2bc30df448265ac5e99d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e248b1de5690497e8ce8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e248b1de5690497e8ce8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb5b477bda5296c82482"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eb5b477bda5296c82482`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5dc7a2d15008e874b5f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5dc7a2d15008e874b5f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d3db8448714a53559a9f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d3db8448714a53559a9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d88a369130714cbbfea"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9d88a369130714cbbfea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac5cb3389d05ed099d50"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ac5cb3389d05ed099d50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60abc4962902341772c4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-60abc4962902341772c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-90d004fd56a2b9c4d252"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-90d004fd56a2b9c4d252`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-649004226a417c7c59e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-649004226a417c7c59e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e56776a594c4d437d82d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e56776a594c4d437d82d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5421983ba4c2c85466b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c5421983ba4c2c85466b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-726eb705aea6cbd00c4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-726eb705aea6cbd00c4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c734393ae253585a3d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c734393ae253585a3d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ecf7f0e388680ece1fa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ecf7f0e388680ece1fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18c4a341a41edeacb8a5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-18c4a341a41edeacb8a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4f268d3b8156d6c5e5be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4f268d3b8156d6c5e5be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90853391c0dec1a618c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-90853391c0dec1a618c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d1b8be30cf5ae785ba0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d1b8be30cf5ae785ba0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a0d0e298d0999b5d7a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a0d0e298d0999b5d7a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8c88672b3ce6be33722f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8c88672b3ce6be33722f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20e94c3badfddcb6e65b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20e94c3badfddcb6e65b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0166539f1c00b53c572b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0166539f1c00b53c572b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05b3aa114f2fd116a81e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-05b3aa114f2fd116a81e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e8600b0532417eee9cb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e8600b0532417eee9cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0406a326d2e420837fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0406a326d2e420837fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7edd7c5ebc406834c387"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7edd7c5ebc406834c387`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af6daa086eaea6dc8ec3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af6daa086eaea6dc8ec3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a39bb5b7461edc3c2342"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a39bb5b7461edc3c2342`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53d54aeea40fb28cf7f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-53d54aeea40fb28cf7f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a05c94a73e7724cb0d38"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a05c94a73e7724cb0d38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-296d699a86483658fbd1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-296d699a86483658fbd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-376cc0f3765aded4d254"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-376cc0f3765aded4d254`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b7a176e7099e72882ed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0b7a176e7099e72882ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c22062251c8cdd94b0c3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c22062251c8cdd94b0c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63687014b7c280dbb61c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-63687014b7c280dbb61c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-218eb53cc5c937aae5a1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-218eb53cc5c937aae5a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c23b60c54832953b287"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5c23b60c54832953b287`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea99749bdfde553bc7de"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ea99749bdfde553bc7de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70d4982775ec5ab64bb8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-70d4982775ec5ab64bb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-11c69b118241d661bde9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-11c69b118241d661bde9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a167cc5f5eac61f4f7a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a167cc5f5eac61f4f7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32fa79d9c8f54f426dce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-32fa79d9c8f54f426dce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62791a263258f9afb393"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-62791a263258f9afb393`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a9e0d1e17d136d3fe9f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a9e0d1e17d136d3fe9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bec4fb422d2af2652f58"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bec4fb422d2af2652f58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9233e162ec6da061c5ec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9233e162ec6da061c5ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-615b9ca9412a90d92503"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-615b9ca9412a90d92503`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d81ac7d3f50d4613227"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d81ac7d3f50d4613227`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d07f75076d75f240561e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d07f75076d75f240561e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35be2750d443e9d30521"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35be2750d443e9d30521`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff430b4562417f678e22"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ff430b4562417f678e22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7191a3d028818282e6df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7191a3d028818282e6df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32e22c6152bb5bc4e551"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-32e22c6152bb5bc4e551`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a1912612d7c8c708e2f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4a1912612d7c8c708e2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcd35463b773a14c2114"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fcd35463b773a14c2114`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9d5cada0022479ec9ff5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9d5cada0022479ec9ff5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18ccb7593cd5b8eace2f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-18ccb7593cd5b8eace2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03580e26fd1f6f8c6b85"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03580e26fd1f6f8c6b85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6dc01b9d80ab517729b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6dc01b9d80ab517729b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-95d423d97ded68229b38"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-95d423d97ded68229b38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e46303f10d3ef2d84faf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e46303f10d3ef2d84faf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dc1b91e22e2eafb074f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1dc1b91e22e2eafb074f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-414853d3e284bcd4a8ed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-414853d3e284bcd4a8ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c1fa89eaacc5a17049b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c1fa89eaacc5a17049b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ee4802a25f6afeb6e5d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0ee4802a25f6afeb6e5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ac17cfe81d1a361f90a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ac17cfe81d1a361f90a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b2e61569df761256fa7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9b2e61569df761256fa7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2d5f61e8d75d6067f2fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d5f61e8d75d6067f2fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f530d17ac00e6d2f1aae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f530d17ac00e6d2f1aae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3a98c683f29f19c2490"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e3a98c683f29f19c2490`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45d2e74e9b8e11798b2d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45d2e74e9b8e11798b2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-11e8bec5f3f26593cda7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b8753a9fe8cb4b5374f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-669f20ca334fa2725521">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53c669b9e0d560734100">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-34ab8cc1941c1679694d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9eb2984cf1042f57d50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c49d85e1e0458fc09a90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2103333f1061216de96f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-979c8bd0d5a8b80bbe88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa56b2910ee47931a245">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cda0b86b4b6e8fce092b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7386920d7b7437e0ccb5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-014113cbb1977cf94807">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ace5c3e9d2cd928fd2fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79d0c14211186bc9bfeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3284df051f74668cc241">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-21049933365281dd4f50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-faa9ef385ccb901b363c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-863ba7d175ec5436ce08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8406170aa2c3513026c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9a4c5df0add87193f73e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3d1f6ca131e728c3160">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3171339f53ed784241c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31a89b0715dc82a38b6a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-471f7d2a26723ae14e03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07fec809481ded71abe7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e903048a5ab9a9db368">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4110d4dda6c522e87d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0b892e6ed15e9c6dca3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c53f09663d68065e1e34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ced574c7d26932c9c58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-902637fd0a51ff5aa031">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e18aafa92a3754b7322">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab3bb946e6f1cc08746f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ebe02fd80ca6fe99140">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca56896e8178ac287d15">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd98a4730353f517f91e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0148c64eb2c453a01505">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be908efbf51b3f1436d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13891ae362ca95c4c0b3">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-11e8bec5f3f26593cda7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-11e8bec5f3f26593cda7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b8753a9fe8cb4b5374f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b8753a9fe8cb4b5374f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-669f20ca334fa2725521"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-669f20ca334fa2725521`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53c669b9e0d560734100"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-53c669b9e0d560734100`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-34ab8cc1941c1679694d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-34ab8cc1941c1679694d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9eb2984cf1042f57d50"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a9eb2984cf1042f57d50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c49d85e1e0458fc09a90"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c49d85e1e0458fc09a90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2103333f1061216de96f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2103333f1061216de96f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-979c8bd0d5a8b80bbe88"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-979c8bd0d5a8b80bbe88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa56b2910ee47931a245"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa56b2910ee47931a245`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cda0b86b4b6e8fce092b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cda0b86b4b6e8fce092b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7386920d7b7437e0ccb5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7386920d7b7437e0ccb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-014113cbb1977cf94807"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-014113cbb1977cf94807`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ace5c3e9d2cd928fd2fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ace5c3e9d2cd928fd2fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79d0c14211186bc9bfeb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-79d0c14211186bc9bfeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3284df051f74668cc241"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3284df051f74668cc241`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-21049933365281dd4f50"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-21049933365281dd4f50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-faa9ef385ccb901b363c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-faa9ef385ccb901b363c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-863ba7d175ec5436ce08"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-863ba7d175ec5436ce08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8406170aa2c3513026c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8406170aa2c3513026c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9a4c5df0add87193f73e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9a4c5df0add87193f73e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3d1f6ca131e728c3160"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a3d1f6ca131e728c3160`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3171339f53ed784241c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3171339f53ed784241c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31a89b0715dc82a38b6a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-31a89b0715dc82a38b6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-8; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-471f7d2a26723ae14e03"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-471f7d2a26723ae14e03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07fec809481ded71abe7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-07fec809481ded71abe7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e903048a5ab9a9db368"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7e903048a5ab9a9db368`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4110d4dda6c522e87d6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b4110d4dda6c522e87d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0b892e6ed15e9c6dca3e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b892e6ed15e9c6dca3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c53f09663d68065e1e34"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c53f09663d68065e1e34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ced574c7d26932c9c58"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ced574c7d26932c9c58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-902637fd0a51ff5aa031"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-902637fd0a51ff5aa031`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e18aafa92a3754b7322"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e18aafa92a3754b7322`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab3bb946e6f1cc08746f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ab3bb946e6f1cc08746f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ebe02fd80ca6fe99140"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ebe02fd80ca6fe99140`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca56896e8178ac287d15"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ca56896e8178ac287d15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd98a4730353f517f91e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd98a4730353f517f91e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0148c64eb2c453a01505"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0148c64eb2c453a01505`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be908efbf51b3f1436d3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be908efbf51b3f1436d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13891ae362ca95c4c0b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-13891ae362ca95c4c0b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e53434db7e2a16f3a5a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a9f9f942db917ecf63f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67a405292853fa780990">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52616854acdf9459c48f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b2371a54ce5ca5fd6c63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db2fbc9c66f42556af70">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21616b51b3bb9dd58fc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5e7df4d76c535f19466">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-deb9d6331c8235bb4f15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e109f20278b0aaaf7e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77933e9efdc4a68e909a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60c19f50a7b5f83ab704">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f770c2b4409d7802860a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5638bee876e44ae4fe76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8310e5f7aeb06aa037c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9560c7821c80ce2c4158">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b2726aecdd7f48acb77e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4e9de82932928e12e9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ab5981d8b6f1004b37a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-012b418bd8866d6cb08f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be3b10a10b844b05d8d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26ff479961c8f63ba205">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8793362f1141d0c3f650">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5d79c1a1c2a4364425f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-00ccd21e13c2bebc50d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3946b8d532f94adf089a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b38d983d1d7e2d7a8b05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccd286ae78a1c6a4dae0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a0d5ab5f8dd229f82294">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2aaaddbae778462db275">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7aa7fedb6377d1cd3a17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a322421a63c6b8028f2d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6a2935a10d4aa3365316">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06b5cce717ceee9adfe4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65ade75219da08b182c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef1e9c29eaeace033791">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-420652fb7d92a9637d37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c81d45aa67ae8f9e23e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0195ce068cc3cccce898">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f18a55edcd5ba4a945c">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e53434db7e2a16f3a5a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e53434db7e2a16f3a5a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a9f9f942db917ecf63f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a9f9f942db917ecf63f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67a405292853fa780990"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67a405292853fa780990`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52616854acdf9459c48f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52616854acdf9459c48f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b2371a54ce5ca5fd6c63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2371a54ce5ca5fd6c63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db2fbc9c66f42556af70"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-db2fbc9c66f42556af70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21616b51b3bb9dd58fc7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-21616b51b3bb9dd58fc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5e7df4d76c535f19466"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5e7df4d76c535f19466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-deb9d6331c8235bb4f15"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-deb9d6331c8235bb4f15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e109f20278b0aaaf7e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3e109f20278b0aaaf7e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77933e9efdc4a68e909a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-77933e9efdc4a68e909a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60c19f50a7b5f83ab704"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-60c19f50a7b5f83ab704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f770c2b4409d7802860a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f770c2b4409d7802860a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5638bee876e44ae4fe76"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5638bee876e44ae4fe76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8310e5f7aeb06aa037c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8310e5f7aeb06aa037c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9560c7821c80ce2c4158"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9560c7821c80ce2c4158`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b2726aecdd7f48acb77e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2726aecdd7f48acb77e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4e9de82932928e12e9a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4e9de82932928e12e9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ab5981d8b6f1004b37a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ab5981d8b6f1004b37a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-012b418bd8866d6cb08f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-012b418bd8866d6cb08f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be3b10a10b844b05d8d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be3b10a10b844b05d8d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26ff479961c8f63ba205"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-26ff479961c8f63ba205`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8793362f1141d0c3f650"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8793362f1141d0c3f650`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5d79c1a1c2a4364425f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c5d79c1a1c2a4364425f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-00ccd21e13c2bebc50d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-00ccd21e13c2bebc50d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3946b8d532f94adf089a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3946b8d532f94adf089a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b38d983d1d7e2d7a8b05"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b38d983d1d7e2d7a8b05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccd286ae78a1c6a4dae0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ccd286ae78a1c6a4dae0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a0d5ab5f8dd229f82294"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a0d5ab5f8dd229f82294`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2aaaddbae778462db275"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2aaaddbae778462db275`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7aa7fedb6377d1cd3a17"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7aa7fedb6377d1cd3a17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a322421a63c6b8028f2d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a322421a63c6b8028f2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6a2935a10d4aa3365316"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6a2935a10d4aa3365316`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06b5cce717ceee9adfe4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-06b5cce717ceee9adfe4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65ade75219da08b182c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65ade75219da08b182c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef1e9c29eaeace033791"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ef1e9c29eaeace033791`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-420652fb7d92a9637d37"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-420652fb7d92a9637d37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c81d45aa67ae8f9e23e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c81d45aa67ae8f9e23e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0195ce068cc3cccce898"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0195ce068cc3cccce898`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f18a55edcd5ba4a945c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f18a55edcd5ba4a945c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e58bafe38f51157719bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64caf4bee100b5594fac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5ee5ac66b6c034b3a9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b353b669c94a881a0f6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3235e2921b48ab00e374">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a40cd19e2b191304658">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e20a1ee6f5bc4b3f15a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a58f5a93f9ab08752139">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e58bafe38f51157719bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e58bafe38f51157719bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64caf4bee100b5594fac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-64caf4bee100b5594fac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5ee5ac66b6c034b3a9a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a5ee5ac66b6c034b3a9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b353b669c94a881a0f6c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b353b669c94a881a0f6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3235e2921b48ab00e374"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3235e2921b48ab00e374`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a40cd19e2b191304658"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a40cd19e2b191304658`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e20a1ee6f5bc4b3f15a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e20a1ee6f5bc4b3f15a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a58f5a93f9ab08752139"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a58f5a93f9ab08752139`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-northwest-terminal-r40:canonical-southeast | <a href="#case-preview_review-610b7207df80db958d0c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-northwest-terminal-r40:canonical-top | <a href="#case-preview_review-02b84b0005dd157d4a30">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-northwest-terminal-r40:connection-overview | <a href="#case-preview_review-abc1b74c50c892f043f2">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-northwest-terminal-r40:canonical-southeast</summary>

<a id="case-preview_review-610b7207df80db958d0c"></a>

**General: unverified** — `preview_review-610b7207df80db958d0c`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-northwest-terminal-r40:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-northwest-terminal-r40:canonical-top</summary>

<a id="case-preview_review-02b84b0005dd157d4a30"></a>

**General: unverified** — `preview_review-02b84b0005dd157d4a30`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-northwest-terminal-r40:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-northwest-terminal-r40:connection-overview</summary>

<a id="case-preview_review-abc1b74c50c892f043f2"></a>

**General: unverified** — `preview_review-abc1b74c50c892f043f2`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-northwest-terminal-r40:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The modular experiment preserves the accepted compact diamond on its original branch. A new highway stamp retains 25 canonical cell models and all 27 canonical PATHs; two Avenue-only cells restore pristine native pavement. Four R40 ramp continuations and two new terminals attach separately. The retained compact grades and junctions remain independently available under their original identifiers.
