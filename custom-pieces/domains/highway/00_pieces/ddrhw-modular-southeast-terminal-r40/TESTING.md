---
title: "Testing: RHW Ramp \u2014 Southeast Avenue Ramp Terminal \u2014 R40"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — Southeast Avenue Ramp Terminal — R40

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-southeast-terminal-r40` resources, its complete intrinsic journeys, and its separately placed joins in the [modular assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). These are fixed-height click-to-place components. Their geometry does not follow sloping terrain.

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
| `1-W-in-5` | road / 1 / primary | in | [8.0, -35.768542, 0.0]; [1.0, 0.0]; 0.0 | `path-interface-0aa85c099c852f580fff` |
| `1-N-out-6` | road / 1 / primary | out | [35.768542, -8.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-0fdd8de01bc6c8b7b1c8` |
| `1-S-out-7` | road / 1 / primary | out | [44.8, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-S-out-8` | road / 1 / primary | out | [51.2, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-E-in-9` | road / 1 / primary | in | [56.0, -51.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-E-in-10` | road / 1 / primary | in | [56.0, -44.8, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `2-W-in-1` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-N-out-2` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-S-out-3` | pedestrian / 2 / primary | out | [40.7, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-E-in-4` | pedestrian / 2 / primary | in | [56.0, -40.7, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-1` → `1-S-out-7` | primary |
| road | `1-W-in-2` → `1-S-out-8` | primary |
| road | `1-W-in-5` → `1-S-out-7` | primary |
| road | `1-E-in-9` → `1-N-out-3` | primary |
| road | `1-E-in-10` → `1-N-out-6` | primary |
| road | `1-E-in-10` → `1-N-out-4` | primary |
| pedestrian | `2-W-in-1` → `2-S-out-3` | primary |
| pedestrian | `2-E-in-4` → `2-N-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-1` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-1` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-5` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-5` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-5` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-5` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-5` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-5` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-9` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-10` | pedestrian / `2-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-W-in-1` | pedestrian / `2-N-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-4` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-E-in-4` | road / `1-S-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-southeast-terminal-r40/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-southeast-terminal-r40/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b6efdc00b8593789a710">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b6efdc00b8593789a710"></a>

**General: unverified** — `software_resources-b6efdc00b8593789a710`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b6efdc00b8593789a710">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b6efdc00b8593789a710"></a>

**General: unverified** — `software_connectivity-b6efdc00b8593789a710`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-0ba22ff44a0fce73cad8">[ ] unverified</a> | <a href="#case-in_game_render-cfbacf05b3484c4873bd">[ ] unverified</a> | <a href="#case-in_game_render-a0e8aa3be77ba0f6eb4a">[ ] unverified</a> | <a href="#case-in_game_render-64ed38df9e8f2e3e9796">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-0ba22ff44a0fce73cad8"></a>

**0° CCW: unverified** — `in_game_render-0ba22ff44a0fce73cad8`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-cfbacf05b3484c4873bd"></a>

**90° CCW: unverified** — `in_game_render-cfbacf05b3484c4873bd`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a0e8aa3be77ba0f6eb4a"></a>

**180° CCW: unverified** — `in_game_render-a0e8aa3be77ba0f6eb4a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-64ed38df9e8f2e3e9796"></a>

**270° CCW: unverified** — `in_game_render-64ed38df9e8f2e3e9796`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-0ba22ff44a0fce73cad8">[ ] unverified</a> | <a href="#case-in_game_placement-cfbacf05b3484c4873bd">[ ] unverified</a> | <a href="#case-in_game_placement-a0e8aa3be77ba0f6eb4a">[ ] unverified</a> | <a href="#case-in_game_placement-64ed38df9e8f2e3e9796">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-0ba22ff44a0fce73cad8"></a>

**0° CCW: unverified** — `in_game_placement-0ba22ff44a0fce73cad8`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-cfbacf05b3484c4873bd"></a>

**90° CCW: unverified** — `in_game_placement-cfbacf05b3484c4873bd`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a0e8aa3be77ba0f6eb4a"></a>

**180° CCW: unverified** — `in_game_placement-a0e8aa3be77ba0f6eb4a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-64ed38df9e8f2e3e9796"></a>

**270° CCW: unverified** — `in_game_placement-64ed38df9e8f2e3e9796`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-0ba22ff44a0fce73cad8">[ ] unverified</a> | <a href="#case-in_game_demolition-cfbacf05b3484c4873bd">[ ] unverified</a> | <a href="#case-in_game_demolition-a0e8aa3be77ba0f6eb4a">[ ] unverified</a> | <a href="#case-in_game_demolition-64ed38df9e8f2e3e9796">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-0ba22ff44a0fce73cad8"></a>

**0° CCW: unverified** — `in_game_demolition-0ba22ff44a0fce73cad8`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-cfbacf05b3484c4873bd"></a>

**90° CCW: unverified** — `in_game_demolition-cfbacf05b3484c4873bd`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a0e8aa3be77ba0f6eb4a"></a>

**180° CCW: unverified** — `in_game_demolition-a0e8aa3be77ba0f6eb4a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-64ed38df9e8f2e3e9796"></a>

**270° CCW: unverified** — `in_game_demolition-64ed38df9e8f2e3e9796`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-0ba22ff44a0fce73cad8">[ ] unverified</a> | <a href="#case-in_game_save_reload-cfbacf05b3484c4873bd">[ ] unverified</a> | <a href="#case-in_game_save_reload-a0e8aa3be77ba0f6eb4a">[ ] unverified</a> | <a href="#case-in_game_save_reload-64ed38df9e8f2e3e9796">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-0ba22ff44a0fce73cad8"></a>

**0° CCW: unverified** — `in_game_save_reload-0ba22ff44a0fce73cad8`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-cfbacf05b3484c4873bd"></a>

**90° CCW: unverified** — `in_game_save_reload-cfbacf05b3484c4873bd`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a0e8aa3be77ba0f6eb4a"></a>

**180° CCW: unverified** — `in_game_save_reload-a0e8aa3be77ba0f6eb4a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-64ed38df9e8f2e3e9796"></a>

**270° CCW: unverified** — `in_game_save_reload-64ed38df9e8f2e3e9796`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7 | — | <a href="#case-in_game_route_query-f86768c787cd597f11ef">[ ] unverified</a> | <a href="#case-in_game_route_query-d4542d20ebefaa4e95f7">[ ] unverified</a> | <a href="#case-in_game_route_query-ff94ccf86e678163fa9a">[ ] unverified</a> | <a href="#case-in_game_route_query-37e0b9b5db23c54e8ed6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8 | — | <a href="#case-in_game_route_query-430419d30f4ee1c87cb2">[ ] unverified</a> | <a href="#case-in_game_route_query-77c6899665e5e7e19994">[ ] unverified</a> | <a href="#case-in_game_route_query-182dafa0c62328ae6c95">[ ] unverified</a> | <a href="#case-in_game_route_query-93afc98b590803d80ddf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7 | — | <a href="#case-in_game_route_query-a820a0d14e530178a493">[ ] unverified</a> | <a href="#case-in_game_route_query-9222c0db2711460d7447">[ ] unverified</a> | <a href="#case-in_game_route_query-23cb57928dc22f483105">[ ] unverified</a> | <a href="#case-in_game_route_query-826f254043a277808b36">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3 | — | <a href="#case-in_game_route_query-0b71e593c96f69838f53">[ ] unverified</a> | <a href="#case-in_game_route_query-9d0c933500de302ef576">[ ] unverified</a> | <a href="#case-in_game_route_query-097e5925eb93d1f0e88e">[ ] unverified</a> | <a href="#case-in_game_route_query-3a6421a349b81dbf39c5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6 | — | <a href="#case-in_game_route_query-d45666cc8bbd549a700b">[ ] unverified</a> | <a href="#case-in_game_route_query-a2c4b01510e73307f1a3">[ ] unverified</a> | <a href="#case-in_game_route_query-766e890e23e08b02e9e0">[ ] unverified</a> | <a href="#case-in_game_route_query-df5183457b98c4610d5c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4 | — | <a href="#case-in_game_route_query-3bcca2e8d74867acfbea">[ ] unverified</a> | <a href="#case-in_game_route_query-fcd1d7ba7a3eacbeda39">[ ] unverified</a> | <a href="#case-in_game_route_query-15bdcad166968e011012">[ ] unverified</a> | <a href="#case-in_game_route_query-eb0c85067d272f1830f4">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7</summary>

<a id="case-in_game_route_query-f86768c787cd597f11ef"></a>

**0° CCW: unverified** — `in_game_route_query-f86768c787cd597f11ef`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-d4542d20ebefaa4e95f7"></a>

**90° CCW: unverified** — `in_game_route_query-d4542d20ebefaa4e95f7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-ff94ccf86e678163fa9a"></a>

**180° CCW: unverified** — `in_game_route_query-ff94ccf86e678163fa9a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-37e0b9b5db23c54e8ed6"></a>

**270° CCW: unverified** — `in_game_route_query-37e0b9b5db23c54e8ed6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8</summary>

<a id="case-in_game_route_query-430419d30f4ee1c87cb2"></a>

**0° CCW: unverified** — `in_game_route_query-430419d30f4ee1c87cb2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_route_query-77c6899665e5e7e19994"></a>

**90° CCW: unverified** — `in_game_route_query-77c6899665e5e7e19994`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_route_query-182dafa0c62328ae6c95"></a>

**180° CCW: unverified** — `in_game_route_query-182dafa0c62328ae6c95`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_route_query-93afc98b590803d80ddf"></a>

**270° CCW: unverified** — `in_game_route_query-93afc98b590803d80ddf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7</summary>

<a id="case-in_game_route_query-a820a0d14e530178a493"></a>

**0° CCW: unverified** — `in_game_route_query-a820a0d14e530178a493`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-9222c0db2711460d7447"></a>

**90° CCW: unverified** — `in_game_route_query-9222c0db2711460d7447`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-23cb57928dc22f483105"></a>

**180° CCW: unverified** — `in_game_route_query-23cb57928dc22f483105`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_route_query-826f254043a277808b36"></a>

**270° CCW: unverified** — `in_game_route_query-826f254043a277808b36`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3</summary>

<a id="case-in_game_route_query-0b71e593c96f69838f53"></a>

**0° CCW: unverified** — `in_game_route_query-0b71e593c96f69838f53`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-9d0c933500de302ef576"></a>

**90° CCW: unverified** — `in_game_route_query-9d0c933500de302ef576`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-097e5925eb93d1f0e88e"></a>

**180° CCW: unverified** — `in_game_route_query-097e5925eb93d1f0e88e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_route_query-3a6421a349b81dbf39c5"></a>

**270° CCW: unverified** — `in_game_route_query-3a6421a349b81dbf39c5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6</summary>

<a id="case-in_game_route_query-d45666cc8bbd549a700b"></a>

**0° CCW: unverified** — `in_game_route_query-d45666cc8bbd549a700b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-a2c4b01510e73307f1a3"></a>

**90° CCW: unverified** — `in_game_route_query-a2c4b01510e73307f1a3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-766e890e23e08b02e9e0"></a>

**180° CCW: unverified** — `in_game_route_query-766e890e23e08b02e9e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-df5183457b98c4610d5c"></a>

**270° CCW: unverified** — `in_game_route_query-df5183457b98c4610d5c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4</summary>

<a id="case-in_game_route_query-3bcca2e8d74867acfbea"></a>

**0° CCW: unverified** — `in_game_route_query-3bcca2e8d74867acfbea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-fcd1d7ba7a3eacbeda39"></a>

**90° CCW: unverified** — `in_game_route_query-fcd1d7ba7a3eacbeda39`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-15bdcad166968e011012"></a>

**180° CCW: unverified** — `in_game_route_query-15bdcad166968e011012`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_route_query-eb0c85067d272f1830f4"></a>

**270° CCW: unverified** — `in_game_route_query-eb0c85067d272f1830f4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7 | — | <a href="#case-in_game_visible_travel-f86768c787cd597f11ef">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d4542d20ebefaa4e95f7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff94ccf86e678163fa9a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-37e0b9b5db23c54e8ed6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8 | — | <a href="#case-in_game_visible_travel-430419d30f4ee1c87cb2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-77c6899665e5e7e19994">[ ] unverified</a> | <a href="#case-in_game_visible_travel-182dafa0c62328ae6c95">[ ] unverified</a> | <a href="#case-in_game_visible_travel-93afc98b590803d80ddf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7 | — | <a href="#case-in_game_visible_travel-a820a0d14e530178a493">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9222c0db2711460d7447">[ ] unverified</a> | <a href="#case-in_game_visible_travel-23cb57928dc22f483105">[ ] unverified</a> | <a href="#case-in_game_visible_travel-826f254043a277808b36">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3 | — | <a href="#case-in_game_visible_travel-0b71e593c96f69838f53">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9d0c933500de302ef576">[ ] unverified</a> | <a href="#case-in_game_visible_travel-097e5925eb93d1f0e88e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3a6421a349b81dbf39c5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6 | — | <a href="#case-in_game_visible_travel-d45666cc8bbd549a700b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a2c4b01510e73307f1a3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-766e890e23e08b02e9e0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-df5183457b98c4610d5c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4 | — | <a href="#case-in_game_visible_travel-3bcca2e8d74867acfbea">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fcd1d7ba7a3eacbeda39">[ ] unverified</a> | <a href="#case-in_game_visible_travel-15bdcad166968e011012">[ ] unverified</a> | <a href="#case-in_game_visible_travel-eb0c85067d272f1830f4">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7</summary>

<a id="case-in_game_visible_travel-f86768c787cd597f11ef"></a>

**0° CCW: unverified** — `in_game_visible_travel-f86768c787cd597f11ef`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-d4542d20ebefaa4e95f7"></a>

**90° CCW: unverified** — `in_game_visible_travel-d4542d20ebefaa4e95f7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-ff94ccf86e678163fa9a"></a>

**180° CCW: unverified** — `in_game_visible_travel-ff94ccf86e678163fa9a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-37e0b9b5db23c54e8ed6"></a>

**270° CCW: unverified** — `in_game_visible_travel-37e0b9b5db23c54e8ed6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-1>1-S-out-7; entry: 1-W-in-1; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8</summary>

<a id="case-in_game_visible_travel-430419d30f4ee1c87cb2"></a>

**0° CCW: unverified** — `in_game_visible_travel-430419d30f4ee1c87cb2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-77c6899665e5e7e19994"></a>

**90° CCW: unverified** — `in_game_visible_travel-77c6899665e5e7e19994`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-182dafa0c62328ae6c95"></a>

**180° CCW: unverified** — `in_game_visible_travel-182dafa0c62328ae6c95`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-93afc98b590803d80ddf"></a>

**270° CCW: unverified** — `in_game_visible_travel-93afc98b590803d80ddf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-S-out-8; entry: 1-W-in-2; exit: 1-S-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7</summary>

<a id="case-in_game_visible_travel-a820a0d14e530178a493"></a>

**0° CCW: unverified** — `in_game_visible_travel-a820a0d14e530178a493`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-9222c0db2711460d7447"></a>

**90° CCW: unverified** — `in_game_visible_travel-9222c0db2711460d7447`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-23cb57928dc22f483105"></a>

**180° CCW: unverified** — `in_game_visible_travel-23cb57928dc22f483105`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-826f254043a277808b36"></a>

**270° CCW: unverified** — `in_game_visible_travel-826f254043a277808b36`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-5>1-S-out-7; entry: 1-W-in-5; exit: 1-S-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3</summary>

<a id="case-in_game_visible_travel-0b71e593c96f69838f53"></a>

**0° CCW: unverified** — `in_game_visible_travel-0b71e593c96f69838f53`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-9d0c933500de302ef576"></a>

**90° CCW: unverified** — `in_game_visible_travel-9d0c933500de302ef576`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-097e5925eb93d1f0e88e"></a>

**180° CCW: unverified** — `in_game_visible_travel-097e5925eb93d1f0e88e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-3a6421a349b81dbf39c5"></a>

**270° CCW: unverified** — `in_game_visible_travel-3a6421a349b81dbf39c5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-9>1-N-out-3; entry: 1-E-in-9; exit: 1-N-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6</summary>

<a id="case-in_game_visible_travel-d45666cc8bbd549a700b"></a>

**0° CCW: unverified** — `in_game_visible_travel-d45666cc8bbd549a700b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-a2c4b01510e73307f1a3"></a>

**90° CCW: unverified** — `in_game_visible_travel-a2c4b01510e73307f1a3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-766e890e23e08b02e9e0"></a>

**180° CCW: unverified** — `in_game_visible_travel-766e890e23e08b02e9e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-df5183457b98c4610d5c"></a>

**270° CCW: unverified** — `in_game_visible_travel-df5183457b98c4610d5c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-6; entry: 1-E-in-10; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4</summary>

<a id="case-in_game_visible_travel-3bcca2e8d74867acfbea"></a>

**0° CCW: unverified** — `in_game_visible_travel-3bcca2e8d74867acfbea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-fcd1d7ba7a3eacbeda39"></a>

**90° CCW: unverified** — `in_game_visible_travel-fcd1d7ba7a3eacbeda39`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-15bdcad166968e011012"></a>

**180° CCW: unverified** — `in_game_visible_travel-15bdcad166968e011012`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

<a id="case-in_game_visible_travel-eb0c85067d272f1830f4"></a>

**270° CCW: unverified** — `in_game_visible_travel-eb0c85067d272f1830f4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-10>1-N-out-4; entry: 1-E-in-10; exit: 1-N-out-4.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3 | — | <a href="#case-in_game_route_query-185ae6aae6d39dda2e7b">[ ] unverified</a> | <a href="#case-in_game_route_query-815a624e771bb9342dc9">[ ] unverified</a> | <a href="#case-in_game_route_query-008b23c83b4686908a3a">[ ] unverified</a> | <a href="#case-in_game_route_query-cf7be28e5e20c9f75f6d">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2 | — | <a href="#case-in_game_route_query-e728b4f1c2be1ff9f2d4">[ ] unverified</a> | <a href="#case-in_game_route_query-141f34c3442f9e6208fd">[ ] unverified</a> | <a href="#case-in_game_route_query-22c218ed1fafc4cfbb88">[ ] unverified</a> | <a href="#case-in_game_route_query-c1b707ff05f9aae89eec">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3</summary>

<a id="case-in_game_route_query-185ae6aae6d39dda2e7b"></a>

**0° CCW: unverified** — `in_game_route_query-185ae6aae6d39dda2e7b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-815a624e771bb9342dc9"></a>

**90° CCW: unverified** — `in_game_route_query-815a624e771bb9342dc9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-008b23c83b4686908a3a"></a>

**180° CCW: unverified** — `in_game_route_query-008b23c83b4686908a3a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-cf7be28e5e20c9f75f6d"></a>

**270° CCW: unverified** — `in_game_route_query-cf7be28e5e20c9f75f6d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2</summary>

<a id="case-in_game_route_query-e728b4f1c2be1ff9f2d4"></a>

**0° CCW: unverified** — `in_game_route_query-e728b4f1c2be1ff9f2d4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-141f34c3442f9e6208fd"></a>

**90° CCW: unverified** — `in_game_route_query-141f34c3442f9e6208fd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-22c218ed1fafc4cfbb88"></a>

**180° CCW: unverified** — `in_game_route_query-22c218ed1fafc4cfbb88`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_route_query-c1b707ff05f9aae89eec"></a>

**270° CCW: unverified** — `in_game_route_query-c1b707ff05f9aae89eec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3 | — | <a href="#case-in_game_visible_travel-185ae6aae6d39dda2e7b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-815a624e771bb9342dc9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-008b23c83b4686908a3a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cf7be28e5e20c9f75f6d">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2 | — | <a href="#case-in_game_visible_travel-e728b4f1c2be1ff9f2d4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-141f34c3442f9e6208fd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-22c218ed1fafc4cfbb88">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c1b707ff05f9aae89eec">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3</summary>

<a id="case-in_game_visible_travel-185ae6aae6d39dda2e7b"></a>

**0° CCW: unverified** — `in_game_visible_travel-185ae6aae6d39dda2e7b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-815a624e771bb9342dc9"></a>

**90° CCW: unverified** — `in_game_visible_travel-815a624e771bb9342dc9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-008b23c83b4686908a3a"></a>

**180° CCW: unverified** — `in_game_visible_travel-008b23c83b4686908a3a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-cf7be28e5e20c9f75f6d"></a>

**270° CCW: unverified** — `in_game_visible_travel-cf7be28e5e20c9f75f6d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-W-in-1>2-S-out-3; entry: 2-W-in-1; exit: 2-S-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2</summary>

<a id="case-in_game_visible_travel-e728b4f1c2be1ff9f2d4"></a>

**0° CCW: unverified** — `in_game_visible_travel-e728b4f1c2be1ff9f2d4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-141f34c3442f9e6208fd"></a>

**90° CCW: unverified** — `in_game_visible_travel-141f34c3442f9e6208fd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-22c218ed1fafc4cfbb88"></a>

**180° CCW: unverified** — `in_game_visible_travel-22c218ed1fafc4cfbb88`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-c1b707ff05f9aae89eec"></a>

**270° CCW: unverified** — `in_game_visible_travel-c1b707ff05f9aae89eec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-E-in-4>2-N-out-2; entry: 2-E-in-4; exit: 2-N-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 76 cases; unverified: 76</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7b49c5bf0b1c4638caf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f775bf1a4d5538cadca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-748015963de5beeee08c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-125e527bdad926747110">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-087e6dd948144da3d942">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b6b0199451f4e88b9c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c5031ca3ac0e2df5c4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1661f813d1866057ca30">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95084b033c3e2ce52325">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f756b326b55659f1c9bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2e1b8064b1f7821c104">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c2d9b4699c7c9011e48">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a5485ae0924e8a5a877">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef8d83b41f693fd8b7a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94beb6e3f3f11094de20">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d8499119ef194ef00ba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1fa33831b943553ec362">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8a6366ca6c40c5d043a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f5e848dae74096c6580">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8f89da80a4cf5130b66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fd4a93eab00880b85a8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d396145e6eb13800d107">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd6910851c9122f90278">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2735146da23aa9f5cc21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d6939790f340d80a4624">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d958a68a1baa6d8664a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f17d488a3d3ee69be0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29ad2c269779b4f43734">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f93bcc178c21851de17b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d49c1466ef94648d7485">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f872f0b95a8d901c575">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c4d1ed7486f753c6468">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-5; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a163fa84f06745d658f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0b99aa2ae9d62e2509e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-016ab310d1d4ab5ae5ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6a407cc594c3c4e6ee9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-5; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-862d9327e9353f65d4ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-330d086c641ebf4dda04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d88a1ec6c783a7177f13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c582cd7459059d15a02e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bae7e4b910fd7d3acd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15af6eaca4174e8a36f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ce19aa65dae10c7301e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42bcf352c3a183cea848">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-5; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2c1e2dabac160a490eeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-781b625bf91b4d2c6104">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0372c7a3b70033fe500b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ec4d59ce2d98bd48030">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8019354560e0e2b22827">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48f5ece206eaaab66781">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0528526d06676c675882">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dbd0ef92010d8b63511">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6aa3de870cacb4aa2a90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8fb7fd582c90176a1a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25b1b53ceca3939e91ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c55c00ef24c02b891e6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7e7a3474f6420a88be9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-210b6a22d720868d2d54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e6702454f06ddaad6e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba21cff78bfa70469906">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-249c0726b2e89caf4658">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-679dac69489ffb65a727">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0720c4724539f28d6400">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2adcb437758aff2e5103">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-38aa41fd5a28d70337ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18046cbe58f2d72bc0d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8f5ff4d4b2e5463ad95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68268ee539a9079a6a11">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-49aed7aeeeb3ad36b2a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3efe97557ba108d3df7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3cc0ea5b6b2935a0e124">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d520d5c2effd82c2013">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f652f871da4a493b5f9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13e3072062083efe6d03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8633d42e9a79123b9e72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-521ae751fe8f57ff13dc">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7b49c5bf0b1c4638caf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7b49c5bf0b1c4638caf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f775bf1a4d5538cadca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3f775bf1a4d5538cadca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-748015963de5beeee08c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-748015963de5beeee08c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-125e527bdad926747110"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-125e527bdad926747110`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-087e6dd948144da3d942"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-087e6dd948144da3d942`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b6b0199451f4e88b9c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b6b0199451f4e88b9c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c5031ca3ac0e2df5c4f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7c5031ca3ac0e2df5c4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1661f813d1866057ca30"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1661f813d1866057ca30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-95084b033c3e2ce52325"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-95084b033c3e2ce52325`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f756b326b55659f1c9bc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f756b326b55659f1c9bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2e1b8064b1f7821c104"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2e1b8064b1f7821c104`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c2d9b4699c7c9011e48"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9c2d9b4699c7c9011e48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a5485ae0924e8a5a877"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a5485ae0924e8a5a877`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef8d83b41f693fd8b7a2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef8d83b41f693fd8b7a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94beb6e3f3f11094de20"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94beb6e3f3f11094de20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d8499119ef194ef00ba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d8499119ef194ef00ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1fa33831b943553ec362"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1fa33831b943553ec362`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8a6366ca6c40c5d043a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b8a6366ca6c40c5d043a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f5e848dae74096c6580"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7f5e848dae74096c6580`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8f89da80a4cf5130b66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8f89da80a4cf5130b66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fd4a93eab00880b85a8d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fd4a93eab00880b85a8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d396145e6eb13800d107"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d396145e6eb13800d107`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd6910851c9122f90278"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd6910851c9122f90278`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2735146da23aa9f5cc21"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2735146da23aa9f5cc21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d6939790f340d80a4624"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d6939790f340d80a4624`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d958a68a1baa6d8664a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d958a68a1baa6d8664a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f17d488a3d3ee69be0d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f17d488a3d3ee69be0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29ad2c269779b4f43734"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-29ad2c269779b4f43734`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f93bcc178c21851de17b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f93bcc178c21851de17b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d49c1466ef94648d7485"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d49c1466ef94648d7485`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f872f0b95a8d901c575"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2f872f0b95a8d901c575`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c4d1ed7486f753c6468"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c4d1ed7486f753c6468`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-5; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a163fa84f06745d658f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a163fa84f06745d658f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0b99aa2ae9d62e2509e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b0b99aa2ae9d62e2509e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-016ab310d1d4ab5ae5ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-016ab310d1d4ab5ae5ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6a407cc594c3c4e6ee9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a6a407cc594c3c4e6ee9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-5; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-862d9327e9353f65d4ed"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-862d9327e9353f65d4ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-330d086c641ebf4dda04"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-330d086c641ebf4dda04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d88a1ec6c783a7177f13"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d88a1ec6c783a7177f13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c582cd7459059d15a02e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c582cd7459059d15a02e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bae7e4b910fd7d3acd3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bae7e4b910fd7d3acd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15af6eaca4174e8a36f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-15af6eaca4174e8a36f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ce19aa65dae10c7301e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ce19aa65dae10c7301e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42bcf352c3a183cea848"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-42bcf352c3a183cea848`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-5; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2c1e2dabac160a490eeb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2c1e2dabac160a490eeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-781b625bf91b4d2c6104"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-781b625bf91b4d2c6104`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0372c7a3b70033fe500b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0372c7a3b70033fe500b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ec4d59ce2d98bd48030"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ec4d59ce2d98bd48030`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8019354560e0e2b22827"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8019354560e0e2b22827`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48f5ece206eaaab66781"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48f5ece206eaaab66781`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0528526d06676c675882"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0528526d06676c675882`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dbd0ef92010d8b63511"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6dbd0ef92010d8b63511`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-4; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6aa3de870cacb4aa2a90"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6aa3de870cacb4aa2a90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8fb7fd582c90176a1a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e8fb7fd582c90176a1a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25b1b53ceca3939e91ea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25b1b53ceca3939e91ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c55c00ef24c02b891e6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1c55c00ef24c02b891e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7e7a3474f6420a88be9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7e7a3474f6420a88be9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-210b6a22d720868d2d54"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-210b6a22d720868d2d54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e6702454f06ddaad6e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e6702454f06ddaad6e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba21cff78bfa70469906"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ba21cff78bfa70469906`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-249c0726b2e89caf4658"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-249c0726b2e89caf4658`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-679dac69489ffb65a727"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-679dac69489ffb65a727`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0720c4724539f28d6400"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0720c4724539f28d6400`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2adcb437758aff2e5103"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2adcb437758aff2e5103`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-38aa41fd5a28d70337ce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-38aa41fd5a28d70337ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18046cbe58f2d72bc0d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-18046cbe58f2d72bc0d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8f5ff4d4b2e5463ad95"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8f5ff4d4b2e5463ad95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68268ee539a9079a6a11"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68268ee539a9079a6a11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-N-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-49aed7aeeeb3ad36b2a1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49aed7aeeeb3ad36b2a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3efe97557ba108d3df7b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3efe97557ba108d3df7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3cc0ea5b6b2935a0e124"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3cc0ea5b6b2935a0e124`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d520d5c2effd82c2013"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7d520d5c2effd82c2013`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f652f871da4a493b5f9c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f652f871da4a493b5f9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13e3072062083efe6d03"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-13e3072062083efe6d03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8633d42e9a79123b9e72"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8633d42e9a79123b9e72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-521ae751fe8f57ff13dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-521ae751fe8f57ff13dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 1-S-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3cc346cb27c2964a31ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-412baf56fc3016bcb28a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe140930b0004c9b0e5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df4f460d2ac56eb65d6a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bef7574ac25eab6801c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4f5cd57c8bc78936d4c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dff955de9e196506432d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfa895654d5ec42838ef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a85e7ead6e784661967">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1632c839509b979dbe4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cad59c5446540384bbb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abb7a2c79d5d6f07bb1d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce3968629509680681df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf3385cf8402f6f877dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db67252d8df23da44abe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78e9a73545ccd12c8c84">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-5; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-498c378cf8ce2bef9492">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1a65e05b784006df622">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6f1aa20d69542986448">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-effbfd9805f25dff2df2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-5; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c0969c18ca8e8b6963c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-607633e8839bb19793f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73952270dc8abb60ba89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b0a686c6a712dc3f415">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f18ed201fb7336c192ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6457adfd2d7d60c5365">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f03417298ae077a957f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d27ff8b84a62b2535e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-37656fbb4ecc83c83675">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3793941996d769ee506">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bb0b40a63374b0ca827">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9931b40d5b11988ecc4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca169386123b49ebe400">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48ec21fed2aaf6772a59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d9f7b24e5888898bfe0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5915fa26b492850ce90">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c997743d951f10536961">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3536a89bbd72f962f2b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cda66eb2b53ef622cef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9b462231d6ae45f2d89">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3cc346cb27c2964a31ed"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3cc346cb27c2964a31ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-412baf56fc3016bcb28a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-412baf56fc3016bcb28a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe140930b0004c9b0e5d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fe140930b0004c9b0e5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df4f460d2ac56eb65d6a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-df4f460d2ac56eb65d6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bef7574ac25eab6801c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bef7574ac25eab6801c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4f5cd57c8bc78936d4c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e4f5cd57c8bc78936d4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dff955de9e196506432d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dff955de9e196506432d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfa895654d5ec42838ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cfa895654d5ec42838ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-1; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a85e7ead6e784661967"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a85e7ead6e784661967`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1632c839509b979dbe4f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1632c839509b979dbe4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cad59c5446540384bbb9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cad59c5446540384bbb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abb7a2c79d5d6f07bb1d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-abb7a2c79d5d6f07bb1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce3968629509680681df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce3968629509680681df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf3385cf8402f6f877dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bf3385cf8402f6f877dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db67252d8df23da44abe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-db67252d8df23da44abe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78e9a73545ccd12c8c84"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-78e9a73545ccd12c8c84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-5; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-498c378cf8ce2bef9492"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-498c378cf8ce2bef9492`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1a65e05b784006df622"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d1a65e05b784006df622`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6f1aa20d69542986448"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b6f1aa20d69542986448`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-effbfd9805f25dff2df2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-effbfd9805f25dff2df2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-5; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c0969c18ca8e8b6963c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c0969c18ca8e8b6963c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-607633e8839bb19793f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-607633e8839bb19793f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73952270dc8abb60ba89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-73952270dc8abb60ba89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b0a686c6a712dc3f415"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b0a686c6a712dc3f415`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-5; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f18ed201fb7336c192ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f18ed201fb7336c192ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6457adfd2d7d60c5365"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f6457adfd2d7d60c5365`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f03417298ae077a957f7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f03417298ae077a957f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d27ff8b84a62b2535e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d27ff8b84a62b2535e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-37656fbb4ecc83c83675"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-37656fbb4ecc83c83675`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3793941996d769ee506"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d3793941996d769ee506`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bb0b40a63374b0ca827"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5bb0b40a63374b0ca827`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9931b40d5b11988ecc4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d9931b40d5b11988ecc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-9; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca169386123b49ebe400"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca169386123b49ebe400`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48ec21fed2aaf6772a59"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48ec21fed2aaf6772a59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d9f7b24e5888898bfe0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d9f7b24e5888898bfe0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5915fa26b492850ce90"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b5915fa26b492850ce90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-N-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c997743d951f10536961"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c997743d951f10536961`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3536a89bbd72f962f2b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3536a89bbd72f962f2b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cda66eb2b53ef622cef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9cda66eb2b53ef622cef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9b462231d6ae45f2d89"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f9b462231d6ae45f2d89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-10; to port: 2-S-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-53722bb41725bcf6e838">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-004a79eed4057cab573d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eaa4299e2b77f4e5d77c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb3a96b9fbc4242505b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c0e7d4af4d2c38b8639">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97e66e5302544a8786d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-452450991d119517efec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e6c48c98d7b5adf7f6d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-207acf04558cbdb4ab87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d8d08a90251ea531b04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f7efb2d93fac234a422">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6cd318f9541095c2e2e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32a0b7d9aa20a5cc1c4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f714f84332939c5ea078">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8358f2a0e84717e5becc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13a227edcc567a015bc4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c3f9f6c1f2726c6f5356">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-940586f97cc1a48f468d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3014868f242691c91588">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f4f9dcaee3f95ec739b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a7f15f649af8daf77741">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dbed78ea0c1a12389e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad5692ddfc5354db9bf2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87cfa1bd2039da6311e8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de5b9d10bb3bb1e44a28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13114f69f3f49220e04c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a69d2f9c6fdb78bcb91c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b4a26c5b8c6422d00d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c31ad6f5930aa45c977c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5c127990afcdb9270aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2c2149d5183ef742ee4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccfc59ae6929f58dd0de">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e1a46a0e4d537191efa5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7455865aedaab1afe5ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-659aae3541b7f70cf4cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-905eaaa9c6a00163dddc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ebbb62dcd732e1c9b011">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1d52bf0610ef871e5ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-660f0c24a63332944822">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d0da67b60354b758f06">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-53722bb41725bcf6e838"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53722bb41725bcf6e838`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-004a79eed4057cab573d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-004a79eed4057cab573d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eaa4299e2b77f4e5d77c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eaa4299e2b77f4e5d77c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb3a96b9fbc4242505b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fb3a96b9fbc4242505b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c0e7d4af4d2c38b8639"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c0e7d4af4d2c38b8639`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97e66e5302544a8786d7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-97e66e5302544a8786d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-452450991d119517efec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-452450991d119517efec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e6c48c98d7b5adf7f6d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6e6c48c98d7b5adf7f6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-207acf04558cbdb4ab87"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-207acf04558cbdb4ab87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d8d08a90251ea531b04"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d8d08a90251ea531b04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f7efb2d93fac234a422"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2f7efb2d93fac234a422`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6cd318f9541095c2e2e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a6cd318f9541095c2e2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32a0b7d9aa20a5cc1c4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32a0b7d9aa20a5cc1c4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f714f84332939c5ea078"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f714f84332939c5ea078`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8358f2a0e84717e5becc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8358f2a0e84717e5becc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13a227edcc567a015bc4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-13a227edcc567a015bc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c3f9f6c1f2726c6f5356"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c3f9f6c1f2726c6f5356`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-940586f97cc1a48f468d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-940586f97cc1a48f468d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3014868f242691c91588"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3014868f242691c91588`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f4f9dcaee3f95ec739b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f4f9dcaee3f95ec739b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a7f15f649af8daf77741"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a7f15f649af8daf77741`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dbed78ea0c1a12389e9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6dbed78ea0c1a12389e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad5692ddfc5354db9bf2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ad5692ddfc5354db9bf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87cfa1bd2039da6311e8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-87cfa1bd2039da6311e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de5b9d10bb3bb1e44a28"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de5b9d10bb3bb1e44a28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13114f69f3f49220e04c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-13114f69f3f49220e04c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a69d2f9c6fdb78bcb91c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a69d2f9c6fdb78bcb91c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b4a26c5b8c6422d00d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7b4a26c5b8c6422d00d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-4; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c31ad6f5930aa45c977c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c31ad6f5930aa45c977c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5c127990afcdb9270aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d5c127990afcdb9270aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2c2149d5183ef742ee4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2c2149d5183ef742ee4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccfc59ae6929f58dd0de"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ccfc59ae6929f58dd0de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-N-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e1a46a0e4d537191efa5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e1a46a0e4d537191efa5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7455865aedaab1afe5ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7455865aedaab1afe5ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-659aae3541b7f70cf4cf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-659aae3541b7f70cf4cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-905eaaa9c6a00163dddc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-905eaaa9c6a00163dddc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ebbb62dcd732e1c9b011"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ebbb62dcd732e1c9b011`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1d52bf0610ef871e5ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e1d52bf0610ef871e5ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-660f0c24a63332944822"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-660f0c24a63332944822`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d0da67b60354b758f06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d0da67b60354b758f06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 1-S-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9cb9c104e41637a415de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00ccb7b5ea1743b1f5ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e09876325c485a75f16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84de9313b2037b2b23dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ed76464a75038b11c03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e44e239c6773bd1c8bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb26167166c24dba91a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9d4e3bbedef8a649b8d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9cb9c104e41637a415de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9cb9c104e41637a415de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00ccb7b5ea1743b1f5ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00ccb7b5ea1743b1f5ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e09876325c485a75f16"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9e09876325c485a75f16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84de9313b2037b2b23dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84de9313b2037b2b23dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-W-in-1; to port: 2-N-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ed76464a75038b11c03"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ed76464a75038b11c03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e44e239c6773bd1c8bb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e44e239c6773bd1c8bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb26167166c24dba91a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cb26167166c24dba91a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9d4e3bbedef8a649b8d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f9d4e3bbedef8a649b8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-E-in-4; to port: 2-S-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-southeast-terminal-r40:canonical-southeast | <a href="#case-preview_review-f7cc7407cf67eb63e0bd">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-southeast-terminal-r40:canonical-top | <a href="#case-preview_review-fe67b6607533f0b9ff2a">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-southeast-terminal-r40:connection-overview | <a href="#case-preview_review-c74f09c2d195a3e4ed86">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-southeast-terminal-r40:canonical-southeast</summary>

<a id="case-preview_review-f7cc7407cf67eb63e0bd"></a>

**General: unverified** — `preview_review-f7cc7407cf67eb63e0bd`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-southeast-terminal-r40:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-southeast-terminal-r40:canonical-top</summary>

<a id="case-preview_review-fe67b6607533f0b9ff2a"></a>

**General: unverified** — `preview_review-fe67b6607533f0b9ff2a`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-southeast-terminal-r40:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-southeast-terminal-r40:connection-overview</summary>

<a id="case-preview_review-c74f09c2d195a3e4ed86"></a>

**General: unverified** — `preview_review-c74f09c2d195a3e4ed86`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-southeast-terminal-r40:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The modular experiment preserves the accepted compact diamond on its original branch. A new highway stamp retains 25 canonical cell models and all 27 canonical PATHs; two Avenue-only cells restore pristine native pavement. Four R40 ramp continuations and two new terminals attach separately. The retained compact grades and junctions remain independently available under their original identifiers.
