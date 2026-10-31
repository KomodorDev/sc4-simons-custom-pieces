---
title: "Testing: RHW Ramp — L1 Exit Parallel Grade — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L1 Exit Parallel Grade — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-lower-exit-grade**, used once as **P12** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 2 occupied tiles in a 1 × 2 rectangle, the exact authored 0° reference at X5, Y7, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-06-out` | road / 1 / primary | out | [-8.0, -15.029437, 0.311171]; [-0.7071067811865647, -0.7071067811865305]; -0.179120116 | `path-interface-efc252caa7500130308e` |
| `channel-07-out` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-08-out` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-02-in` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-03-in` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-09-out` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-04-in` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-10-out` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-05-in` | road / 1 / primary | in | [8.0, 0.970563, 4.364109]; [-0.7071067811865476, -0.7071067811865476]; -0.179117565 | `path-interface-6f98c9419d701c4a592c` |

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
| road / `channel-01-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X5, Y7), (X5, Y6)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-parts-01
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-lower-exit-grade --build dist/ddrhw-parallel-diamond-parts-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-lower-exit-grade
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

## 4. Game checks

1. Select this exact component through the assembly button, match P12 at **X5, Y7**, and confirm that the occupied preview squares match **(X5, Y7), (X5, Y6)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and check its pavement variant. Then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-lower-exit-grade** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. This is a fixed-height transition, not a straight slope that can be repeated to obtain any chosen height. Its visible grade model overhangs neighbouring departure and terminal tiles. Its whole-cell traffic ownership also includes one native highway half, so the model and traffic boundaries differ. The native through PATHs and outside-deck ramp route remain with those owned cells. The visible native highway half and its centre pier instead belong to the adjacent straight slip-lane model through overhang, leaving this component’s physical model as a pure graded ramp. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-exit-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-exit-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-73ce58b3aa2bea0a5e33">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-73ce58b3aa2bea0a5e33"></a>

**General: unverified** — `software_resources-73ce58b3aa2bea0a5e33`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-73ce58b3aa2bea0a5e33">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-73ce58b3aa2bea0a5e33"></a>

**General: unverified** — `software_connectivity-73ce58b3aa2bea0a5e33`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-2d2853c71e11568cafed">[ ] unverified</a> | <a href="#case-in_game_render-fdc192467bb147e65da7">[ ] unverified</a> | <a href="#case-in_game_render-bc7770c581c8d8464450">[ ] unverified</a> | <a href="#case-in_game_render-ec70ebd94e9fa4c9e547">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-2d2853c71e11568cafed"></a>

**0° CCW: unverified** — `in_game_render-2d2853c71e11568cafed`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-fdc192467bb147e65da7"></a>

**90° CCW: unverified** — `in_game_render-fdc192467bb147e65da7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-bc7770c581c8d8464450"></a>

**180° CCW: unverified** — `in_game_render-bc7770c581c8d8464450`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ec70ebd94e9fa4c9e547"></a>

**270° CCW: unverified** — `in_game_render-ec70ebd94e9fa4c9e547`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-2d2853c71e11568cafed">[ ] unverified</a> | <a href="#case-in_game_placement-fdc192467bb147e65da7">[ ] unverified</a> | <a href="#case-in_game_placement-bc7770c581c8d8464450">[ ] unverified</a> | <a href="#case-in_game_placement-ec70ebd94e9fa4c9e547">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-2d2853c71e11568cafed"></a>

**0° CCW: unverified** — `in_game_placement-2d2853c71e11568cafed`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-fdc192467bb147e65da7"></a>

**90° CCW: unverified** — `in_game_placement-fdc192467bb147e65da7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-bc7770c581c8d8464450"></a>

**180° CCW: unverified** — `in_game_placement-bc7770c581c8d8464450`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ec70ebd94e9fa4c9e547"></a>

**270° CCW: unverified** — `in_game_placement-ec70ebd94e9fa4c9e547`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-2d2853c71e11568cafed">[ ] unverified</a> | <a href="#case-in_game_demolition-fdc192467bb147e65da7">[ ] unverified</a> | <a href="#case-in_game_demolition-bc7770c581c8d8464450">[ ] unverified</a> | <a href="#case-in_game_demolition-ec70ebd94e9fa4c9e547">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-2d2853c71e11568cafed"></a>

**0° CCW: unverified** — `in_game_demolition-2d2853c71e11568cafed`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-fdc192467bb147e65da7"></a>

**90° CCW: unverified** — `in_game_demolition-fdc192467bb147e65da7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-bc7770c581c8d8464450"></a>

**180° CCW: unverified** — `in_game_demolition-bc7770c581c8d8464450`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ec70ebd94e9fa4c9e547"></a>

**270° CCW: unverified** — `in_game_demolition-ec70ebd94e9fa4c9e547`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-2d2853c71e11568cafed">[ ] unverified</a> | <a href="#case-in_game_save_reload-fdc192467bb147e65da7">[ ] unverified</a> | <a href="#case-in_game_save_reload-bc7770c581c8d8464450">[ ] unverified</a> | <a href="#case-in_game_save_reload-ec70ebd94e9fa4c9e547">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-2d2853c71e11568cafed"></a>

**0° CCW: unverified** — `in_game_save_reload-2d2853c71e11568cafed`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-fdc192467bb147e65da7"></a>

**90° CCW: unverified** — `in_game_save_reload-fdc192467bb147e65da7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-bc7770c581c8d8464450"></a>

**180° CCW: unverified** — `in_game_save_reload-bc7770c581c8d8464450`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ec70ebd94e9fa4c9e547"></a>

**270° CCW: unverified** — `in_game_save_reload-ec70ebd94e9fa4c9e547`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-ab06d3dbef912fed9466">[ ] unverified</a> | <a href="#case-in_game_route_query-d1496f8f349d9ae5bbac">[ ] unverified</a> | <a href="#case-in_game_route_query-14b5f925209034a4f110">[ ] unverified</a> | <a href="#case-in_game_route_query-9d1dedb510b22a5152d3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-84997d2d034d47498603">[ ] unverified</a> | <a href="#case-in_game_route_query-f238acd78db333277537">[ ] unverified</a> | <a href="#case-in_game_route_query-df1905fc42142369ec7a">[ ] unverified</a> | <a href="#case-in_game_route_query-af2eff162fef6b21d6e0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-8cbefa13e87ae2d85aa8">[ ] unverified</a> | <a href="#case-in_game_route_query-04f24960b289f92b3a93">[ ] unverified</a> | <a href="#case-in_game_route_query-7021169158b4a1aab304">[ ] unverified</a> | <a href="#case-in_game_route_query-8e5977de733ef806cb59">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-61b49ccc3d6d49ffcf3b">[ ] unverified</a> | <a href="#case-in_game_route_query-62eae7ea4910357afb7e">[ ] unverified</a> | <a href="#case-in_game_route_query-9e16a176ac3492f9c410">[ ] unverified</a> | <a href="#case-in_game_route_query-0a4473de6bc121cfbe40">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-71588425edfd7bde1643">[ ] unverified</a> | <a href="#case-in_game_route_query-a25b26e1a9af753b6bef">[ ] unverified</a> | <a href="#case-in_game_route_query-263c6e0c57ec3199fdfb">[ ] unverified</a> | <a href="#case-in_game_route_query-436560ee0e1209d6657e">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-ab06d3dbef912fed9466"></a>

**0° CCW: unverified** — `in_game_route_query-ab06d3dbef912fed9466`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-d1496f8f349d9ae5bbac"></a>

**90° CCW: unverified** — `in_game_route_query-d1496f8f349d9ae5bbac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-14b5f925209034a4f110"></a>

**180° CCW: unverified** — `in_game_route_query-14b5f925209034a4f110`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-9d1dedb510b22a5152d3"></a>

**270° CCW: unverified** — `in_game_route_query-9d1dedb510b22a5152d3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-84997d2d034d47498603"></a>

**0° CCW: unverified** — `in_game_route_query-84997d2d034d47498603`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-f238acd78db333277537"></a>

**90° CCW: unverified** — `in_game_route_query-f238acd78db333277537`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-df1905fc42142369ec7a"></a>

**180° CCW: unverified** — `in_game_route_query-df1905fc42142369ec7a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-af2eff162fef6b21d6e0"></a>

**270° CCW: unverified** — `in_game_route_query-af2eff162fef6b21d6e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-8cbefa13e87ae2d85aa8"></a>

**0° CCW: unverified** — `in_game_route_query-8cbefa13e87ae2d85aa8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-04f24960b289f92b3a93"></a>

**90° CCW: unverified** — `in_game_route_query-04f24960b289f92b3a93`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-7021169158b4a1aab304"></a>

**180° CCW: unverified** — `in_game_route_query-7021169158b4a1aab304`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-8e5977de733ef806cb59"></a>

**270° CCW: unverified** — `in_game_route_query-8e5977de733ef806cb59`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-61b49ccc3d6d49ffcf3b"></a>

**0° CCW: unverified** — `in_game_route_query-61b49ccc3d6d49ffcf3b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-62eae7ea4910357afb7e"></a>

**90° CCW: unverified** — `in_game_route_query-62eae7ea4910357afb7e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-9e16a176ac3492f9c410"></a>

**180° CCW: unverified** — `in_game_route_query-9e16a176ac3492f9c410`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-0a4473de6bc121cfbe40"></a>

**270° CCW: unverified** — `in_game_route_query-0a4473de6bc121cfbe40`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-71588425edfd7bde1643"></a>

**0° CCW: unverified** — `in_game_route_query-71588425edfd7bde1643`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-a25b26e1a9af753b6bef"></a>

**90° CCW: unverified** — `in_game_route_query-a25b26e1a9af753b6bef`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-263c6e0c57ec3199fdfb"></a>

**180° CCW: unverified** — `in_game_route_query-263c6e0c57ec3199fdfb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-436560ee0e1209d6657e"></a>

**270° CCW: unverified** — `in_game_route_query-436560ee0e1209d6657e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-ab06d3dbef912fed9466">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d1496f8f349d9ae5bbac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-14b5f925209034a4f110">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9d1dedb510b22a5152d3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-84997d2d034d47498603">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f238acd78db333277537">[ ] unverified</a> | <a href="#case-in_game_visible_travel-df1905fc42142369ec7a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-af2eff162fef6b21d6e0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-8cbefa13e87ae2d85aa8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-04f24960b289f92b3a93">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7021169158b4a1aab304">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8e5977de733ef806cb59">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-61b49ccc3d6d49ffcf3b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-62eae7ea4910357afb7e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9e16a176ac3492f9c410">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0a4473de6bc121cfbe40">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-71588425edfd7bde1643">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a25b26e1a9af753b6bef">[ ] unverified</a> | <a href="#case-in_game_visible_travel-263c6e0c57ec3199fdfb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-436560ee0e1209d6657e">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-ab06d3dbef912fed9466"></a>

**0° CCW: unverified** — `in_game_visible_travel-ab06d3dbef912fed9466`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-d1496f8f349d9ae5bbac"></a>

**90° CCW: unverified** — `in_game_visible_travel-d1496f8f349d9ae5bbac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-14b5f925209034a4f110"></a>

**180° CCW: unverified** — `in_game_visible_travel-14b5f925209034a4f110`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-9d1dedb510b22a5152d3"></a>

**270° CCW: unverified** — `in_game_visible_travel-9d1dedb510b22a5152d3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-84997d2d034d47498603"></a>

**0° CCW: unverified** — `in_game_visible_travel-84997d2d034d47498603`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-f238acd78db333277537"></a>

**90° CCW: unverified** — `in_game_visible_travel-f238acd78db333277537`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-df1905fc42142369ec7a"></a>

**180° CCW: unverified** — `in_game_visible_travel-df1905fc42142369ec7a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-af2eff162fef6b21d6e0"></a>

**270° CCW: unverified** — `in_game_visible_travel-af2eff162fef6b21d6e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-8cbefa13e87ae2d85aa8"></a>

**0° CCW: unverified** — `in_game_visible_travel-8cbefa13e87ae2d85aa8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-04f24960b289f92b3a93"></a>

**90° CCW: unverified** — `in_game_visible_travel-04f24960b289f92b3a93`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-7021169158b4a1aab304"></a>

**180° CCW: unverified** — `in_game_visible_travel-7021169158b4a1aab304`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-8e5977de733ef806cb59"></a>

**270° CCW: unverified** — `in_game_visible_travel-8e5977de733ef806cb59`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-61b49ccc3d6d49ffcf3b"></a>

**0° CCW: unverified** — `in_game_visible_travel-61b49ccc3d6d49ffcf3b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-62eae7ea4910357afb7e"></a>

**90° CCW: unverified** — `in_game_visible_travel-62eae7ea4910357afb7e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-9e16a176ac3492f9c410"></a>

**180° CCW: unverified** — `in_game_visible_travel-9e16a176ac3492f9c410`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-0a4473de6bc121cfbe40"></a>

**270° CCW: unverified** — `in_game_visible_travel-0a4473de6bc121cfbe40`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-71588425edfd7bde1643"></a>

**0° CCW: unverified** — `in_game_visible_travel-71588425edfd7bde1643`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-a25b26e1a9af753b6bef"></a>

**90° CCW: unverified** — `in_game_visible_travel-a25b26e1a9af753b6bef`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-263c6e0c57ec3199fdfb"></a>

**180° CCW: unverified** — `in_game_visible_travel-263c6e0c57ec3199fdfb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-436560ee0e1209d6657e"></a>

**270° CCW: unverified** — `in_game_visible_travel-436560ee0e1209d6657e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-355602b326dd9da7b5de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39b04f16155b0f5b3d0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee2fc9f7bbf17816aee5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58a70491f36e15d518e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f44e95182c82dd73f82c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-699397fe98b2f0ccaa08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b3afd26a96ceed18d06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ac911ac704ab114a5d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a5ec5a5eefc4612336ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4348ceafcd7d2625b82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84b6a7896195606f9181">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a95121f79aa1489193bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-81f51d969e28135a6be4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d101cdb1550db39b6485">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79c6d3c1c588e171cc66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb9c1760d0f196d4ec58">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4049587fc6ca01fb9a0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-346e804179353d70f6fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1288f9d91f9c36bb68f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ddc0ef310cc8362a527">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-796b6a47f72c98ee91f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-972cc5abc78c5b84ead4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2dac023c3968569e8bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7999afda4d42eb8ad3e8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20a37ae833c63d9c09ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6dc4f7d176e7d94e798">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d72b23f5cf91e8c1ae74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-791a3048e3f38a5e918e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-30dbf2e9a42436af44e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78193b1ad0fd5b37ba73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d84164a7cd06f00b3bab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f819f03aa8202c23fd4f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-30fb20335e553cac809f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1defee3a470513b79a5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eedf2b5343584edc3f43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb3470042578b8d6ad77">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-85550d117bca22999b59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebedab9eb13b8d02abf1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-594873dda44456727879">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec15740638e3a7795eeb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0c4b61f34e6d3325fc5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cef62e06cb9582f91971">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20b1727b14b6c91e3bb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e9f7be49ebe7215cac5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8645c64b5e7d1a60def7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3272c3ecb34cf5f6fcf1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a50602240a68b12dc48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d49af86b7eb793b6d21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-912ad5d89754a86580de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98e8afe2bab52b032158">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35f662599a68127aa9a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e17d71f4e57040ee375">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9abaf01524b0724d6803">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-136aa91a5d1680512742">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6da39f0105c215fba2e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8e16427f2b030848a87">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7c2f1e95308c5e0ed1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7005e21e3a1b42cafd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0035a974fd06b635349a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6a286d9c9c802250420">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e49d5211ce6db8af969d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c6df902cea073d3bace">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27ce5428bd5817998689">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-316e85d78dc561719712">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-477b7a77a7bc4e29940e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9513c2f79089b32eefd5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c6a199651307336b835">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a0869f8fb8daf05944e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bc7621202625bf4f9bc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53724e9676f9d20f1f7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-810d92e3b2ad6d7567da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5888e4fc121e6d076606">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de7862840e5fb4942195">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60afe2d4150ce275763e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdb15c3842afb177a49d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e0fa9ebc2b1adb0f2b7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0413c3a7f7bae6d4dc04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d46282dff3b7966a2045">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bcacec788d9c8b3b0d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c971e3a0dd506261dad2">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-355602b326dd9da7b5de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-355602b326dd9da7b5de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39b04f16155b0f5b3d0e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39b04f16155b0f5b3d0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee2fc9f7bbf17816aee5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee2fc9f7bbf17816aee5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58a70491f36e15d518e2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-58a70491f36e15d518e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f44e95182c82dd73f82c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f44e95182c82dd73f82c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-699397fe98b2f0ccaa08"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-699397fe98b2f0ccaa08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b3afd26a96ceed18d06"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0b3afd26a96ceed18d06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ac911ac704ab114a5d6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ac911ac704ab114a5d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a5ec5a5eefc4612336ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a5ec5a5eefc4612336ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4348ceafcd7d2625b82"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d4348ceafcd7d2625b82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84b6a7896195606f9181"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-84b6a7896195606f9181`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a95121f79aa1489193bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a95121f79aa1489193bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-81f51d969e28135a6be4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81f51d969e28135a6be4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d101cdb1550db39b6485"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d101cdb1550db39b6485`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79c6d3c1c588e171cc66"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-79c6d3c1c588e171cc66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb9c1760d0f196d4ec58"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb9c1760d0f196d4ec58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4049587fc6ca01fb9a0e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4049587fc6ca01fb9a0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-346e804179353d70f6fc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-346e804179353d70f6fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1288f9d91f9c36bb68f8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1288f9d91f9c36bb68f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ddc0ef310cc8362a527"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8ddc0ef310cc8362a527`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-796b6a47f72c98ee91f0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-796b6a47f72c98ee91f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-972cc5abc78c5b84ead4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-972cc5abc78c5b84ead4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2dac023c3968569e8bb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2dac023c3968569e8bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7999afda4d42eb8ad3e8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7999afda4d42eb8ad3e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20a37ae833c63d9c09ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20a37ae833c63d9c09ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6dc4f7d176e7d94e798"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f6dc4f7d176e7d94e798`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d72b23f5cf91e8c1ae74"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d72b23f5cf91e8c1ae74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-791a3048e3f38a5e918e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-791a3048e3f38a5e918e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-30dbf2e9a42436af44e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-30dbf2e9a42436af44e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78193b1ad0fd5b37ba73"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78193b1ad0fd5b37ba73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d84164a7cd06f00b3bab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d84164a7cd06f00b3bab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f819f03aa8202c23fd4f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f819f03aa8202c23fd4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-30fb20335e553cac809f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-30fb20335e553cac809f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1defee3a470513b79a5f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1defee3a470513b79a5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eedf2b5343584edc3f43"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eedf2b5343584edc3f43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb3470042578b8d6ad77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fb3470042578b8d6ad77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-85550d117bca22999b59"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-85550d117bca22999b59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebedab9eb13b8d02abf1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ebedab9eb13b8d02abf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-594873dda44456727879"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-594873dda44456727879`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec15740638e3a7795eeb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec15740638e3a7795eeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0c4b61f34e6d3325fc5d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c4b61f34e6d3325fc5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cef62e06cb9582f91971"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cef62e06cb9582f91971`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20b1727b14b6c91e3bb9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-20b1727b14b6c91e3bb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e9f7be49ebe7215cac5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5e9f7be49ebe7215cac5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8645c64b5e7d1a60def7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8645c64b5e7d1a60def7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3272c3ecb34cf5f6fcf1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3272c3ecb34cf5f6fcf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a50602240a68b12dc48"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a50602240a68b12dc48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d49af86b7eb793b6d21"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4d49af86b7eb793b6d21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-912ad5d89754a86580de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-912ad5d89754a86580de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98e8afe2bab52b032158"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-98e8afe2bab52b032158`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35f662599a68127aa9a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35f662599a68127aa9a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e17d71f4e57040ee375"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e17d71f4e57040ee375`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9abaf01524b0724d6803"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9abaf01524b0724d6803`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-136aa91a5d1680512742"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-136aa91a5d1680512742`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6da39f0105c215fba2e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6da39f0105c215fba2e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8e16427f2b030848a87"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c8e16427f2b030848a87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7c2f1e95308c5e0ed1a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7c2f1e95308c5e0ed1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7005e21e3a1b42cafd3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c7005e21e3a1b42cafd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0035a974fd06b635349a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0035a974fd06b635349a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6a286d9c9c802250420"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f6a286d9c9c802250420`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e49d5211ce6db8af969d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e49d5211ce6db8af969d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c6df902cea073d3bace"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5c6df902cea073d3bace`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27ce5428bd5817998689"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27ce5428bd5817998689`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-316e85d78dc561719712"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-316e85d78dc561719712`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-477b7a77a7bc4e29940e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-477b7a77a7bc4e29940e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9513c2f79089b32eefd5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9513c2f79089b32eefd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c6a199651307336b835"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c6a199651307336b835`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a0869f8fb8daf05944e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6a0869f8fb8daf05944e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bc7621202625bf4f9bc0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bc7621202625bf4f9bc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53724e9676f9d20f1f7a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-53724e9676f9d20f1f7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-810d92e3b2ad6d7567da"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-810d92e3b2ad6d7567da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5888e4fc121e6d076606"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5888e4fc121e6d076606`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de7862840e5fb4942195"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de7862840e5fb4942195`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60afe2d4150ce275763e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-60afe2d4150ce275763e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdb15c3842afb177a49d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fdb15c3842afb177a49d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e0fa9ebc2b1adb0f2b7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e0fa9ebc2b1adb0f2b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0413c3a7f7bae6d4dc04"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0413c3a7f7bae6d4dc04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d46282dff3b7966a2045"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d46282dff3b7966a2045`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bcacec788d9c8b3b0d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5bcacec788d9c8b3b0d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c971e3a0dd506261dad2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c971e3a0dd506261dad2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-grade:canonical-southeast | <a href="#case-preview_review-7c1dedab2aceba419ceb">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-grade:canonical-top | <a href="#case-preview_review-a0dfd317477331ea7ac8">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-grade:connection-overview | <a href="#case-preview_review-f510428a1e4541548701">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-grade:canonical-southeast</summary>

<a id="case-preview_review-7c1dedab2aceba419ceb"></a>

**General: unverified** — `preview_review-7c1dedab2aceba419ceb`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-exit-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-grade:canonical-top</summary>

<a id="case-preview_review-a0dfd317477331ea7ac8"></a>

**General: unverified** — `preview_review-a0dfd317477331ea7ac8`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-exit-grade:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-grade:connection-overview</summary>

<a id="case-preview_review-f510428a1e4541548701"></a>

**General: unverified** — `preview_review-f510428a1e4541548701`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-exit-grade:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).
