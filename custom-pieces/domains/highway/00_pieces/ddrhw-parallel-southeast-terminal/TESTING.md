---
title: "Testing: Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: Avenue — Southeast Avenue Right-Turn Terminal — Parallel DD RHW

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-southeast-terminal**, used once as **P03** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 3 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X5, Y4, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -4.675154, 0.0]; [0.983505074872391, -0.18088053433206316]; 0.0 | `path-interface-eb8edd053c1b618ae382` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-03-in` | road / 1 / primary | in | [-8.0, 3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-06-out` | road / 1 / primary | out | [-3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-07-out` | road / 1 / primary | out | [3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-08-out` | road / 1 / primary | out | [4.675154, 8.0, 0.0]; [-0.18088053433206316, 0.983505074872391]; 0.0 | `path-interface-ab0dc819ba4c7fec9f5c` |
| `channel-09-out` | road / 1 / primary | out | [8.0, -19.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-10-out` | road / 1 / primary | out | [8.0, -12.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-04-in` | road / 1 / primary | in | [12.8, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-05-in` | road / 1 / primary | in | [19.2, -8.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-11-in` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-13-out` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `channel-14-out` | pedestrian / 2 / primary | out | [8.0, -23.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-12-in` | pedestrian / 2 / primary | in | [23.3, -8.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-09-out` | primary |
| road | `channel-02-in` → `channel-09-out` | primary |
| road | `channel-03-in` → `channel-10-out` | primary |
| road | `channel-04-in` → `channel-06-out` | primary |
| road | `channel-05-in` → `channel-08-out` | primary |
| road | `channel-05-in` → `channel-07-out` | primary |
| pedestrian | `channel-11-in` → `channel-14-out` | primary |
| pedestrian | `channel-12-in` → `channel-13-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-11-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-11-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-11-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-11-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-11-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-11-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-12-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-12-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-12-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-12-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-12-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-12-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X5, Y4), (X6, Y4), (X5, Y3)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-parts-01
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-southeast-terminal --build dist/ddrhw-parallel-diamond-parts-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-southeast-terminal
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

## 4. Game checks

1. Select this exact component through the assembly button, match P03 at **X5, Y4**, and confirm that the occupied preview squares match **(X5, Y4), (X6, Y4), (X5, Y3)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and check its pavement variant. Then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-southeast-terminal** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. Its three occupied tiles retain the native two-way Avenue and pedestrian channels. The visible turn models extend above some neighbouring owners, while their traffic fragments remain with the city tile they cross. All three native Avenue cells use adaptive ground textures and retained overlay models. The unused local [1,1] corner is the removable placement handle. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-southeast-terminal/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-southeast-terminal/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-e7127b767359efa32b5e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-e7127b767359efa32b5e"></a>

**General: unverified** — `software_resources-e7127b767359efa32b5e`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-e7127b767359efa32b5e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-e7127b767359efa32b5e"></a>

**General: unverified** — `software_connectivity-e7127b767359efa32b5e`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-1299f176a9f2715662e1">[ ] unverified</a> | <a href="#case-in_game_render-8d8833b017f543a94291">[ ] unverified</a> | <a href="#case-in_game_render-a440695d4ab6709f2bfc">[ ] unverified</a> | <a href="#case-in_game_render-c0cdf89f7d2b59b3a3e5">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-1299f176a9f2715662e1"></a>

**0° CCW: unverified** — `in_game_render-1299f176a9f2715662e1`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8d8833b017f543a94291"></a>

**90° CCW: unverified** — `in_game_render-8d8833b017f543a94291`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a440695d4ab6709f2bfc"></a>

**180° CCW: unverified** — `in_game_render-a440695d4ab6709f2bfc`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c0cdf89f7d2b59b3a3e5"></a>

**270° CCW: unverified** — `in_game_render-c0cdf89f7d2b59b3a3e5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-1299f176a9f2715662e1">[ ] unverified</a> | <a href="#case-in_game_placement-8d8833b017f543a94291">[ ] unverified</a> | <a href="#case-in_game_placement-a440695d4ab6709f2bfc">[ ] unverified</a> | <a href="#case-in_game_placement-c0cdf89f7d2b59b3a3e5">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-1299f176a9f2715662e1"></a>

**0° CCW: unverified** — `in_game_placement-1299f176a9f2715662e1`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8d8833b017f543a94291"></a>

**90° CCW: unverified** — `in_game_placement-8d8833b017f543a94291`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a440695d4ab6709f2bfc"></a>

**180° CCW: unverified** — `in_game_placement-a440695d4ab6709f2bfc`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c0cdf89f7d2b59b3a3e5"></a>

**270° CCW: unverified** — `in_game_placement-c0cdf89f7d2b59b3a3e5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-1299f176a9f2715662e1">[ ] unverified</a> | <a href="#case-in_game_demolition-8d8833b017f543a94291">[ ] unverified</a> | <a href="#case-in_game_demolition-a440695d4ab6709f2bfc">[ ] unverified</a> | <a href="#case-in_game_demolition-c0cdf89f7d2b59b3a3e5">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-1299f176a9f2715662e1"></a>

**0° CCW: unverified** — `in_game_demolition-1299f176a9f2715662e1`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8d8833b017f543a94291"></a>

**90° CCW: unverified** — `in_game_demolition-8d8833b017f543a94291`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a440695d4ab6709f2bfc"></a>

**180° CCW: unverified** — `in_game_demolition-a440695d4ab6709f2bfc`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c0cdf89f7d2b59b3a3e5"></a>

**270° CCW: unverified** — `in_game_demolition-c0cdf89f7d2b59b3a3e5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-1299f176a9f2715662e1">[ ] unverified</a> | <a href="#case-in_game_save_reload-8d8833b017f543a94291">[ ] unverified</a> | <a href="#case-in_game_save_reload-a440695d4ab6709f2bfc">[ ] unverified</a> | <a href="#case-in_game_save_reload-c0cdf89f7d2b59b3a3e5">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-1299f176a9f2715662e1"></a>

**0° CCW: unverified** — `in_game_save_reload-1299f176a9f2715662e1`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8d8833b017f543a94291"></a>

**90° CCW: unverified** — `in_game_save_reload-8d8833b017f543a94291`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a440695d4ab6709f2bfc"></a>

**180° CCW: unverified** — `in_game_save_reload-a440695d4ab6709f2bfc`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c0cdf89f7d2b59b3a3e5"></a>

**270° CCW: unverified** — `in_game_save_reload-c0cdf89f7d2b59b3a3e5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-f1f3a3adb8761bd4394f">[ ] unverified</a> | <a href="#case-in_game_route_query-e01e2b0222ab8d3ec184">[ ] unverified</a> | <a href="#case-in_game_route_query-d7c3c42a3347940c63ba">[ ] unverified</a> | <a href="#case-in_game_route_query-f87110ff16c3ba7c2ad4">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-7913d9835c08c5437360">[ ] unverified</a> | <a href="#case-in_game_route_query-3c52b67aa88beafb101d">[ ] unverified</a> | <a href="#case-in_game_route_query-ac174465e61df1ae99e5">[ ] unverified</a> | <a href="#case-in_game_route_query-03d6f8094e3d0c630ab8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-f77a11a467ab4fee0a90">[ ] unverified</a> | <a href="#case-in_game_route_query-0f7cd0e86500cc505f1a">[ ] unverified</a> | <a href="#case-in_game_route_query-34e426384763720fb5d2">[ ] unverified</a> | <a href="#case-in_game_route_query-cd3f460ad792f4cf81e8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-dde6ddba312e61808ffa">[ ] unverified</a> | <a href="#case-in_game_route_query-84234f10ae0a3dfe1e4d">[ ] unverified</a> | <a href="#case-in_game_route_query-5951c74fcaa3983aab87">[ ] unverified</a> | <a href="#case-in_game_route_query-4d49f731f02ea26bedaa">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-1cab22d8daf6dfcb2735">[ ] unverified</a> | <a href="#case-in_game_route_query-e4e490f635136e57a0bc">[ ] unverified</a> | <a href="#case-in_game_route_query-59ec651e74d3602cd462">[ ] unverified</a> | <a href="#case-in_game_route_query-68a6ef40907d39cb91ea">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-83e959532d623cd67798">[ ] unverified</a> | <a href="#case-in_game_route_query-0d1c79c5bda19a588348">[ ] unverified</a> | <a href="#case-in_game_route_query-ff6d9c15dcb9cd142d45">[ ] unverified</a> | <a href="#case-in_game_route_query-98b174db0d7e11cc7b21">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-f1f3a3adb8761bd4394f"></a>

**0° CCW: unverified** — `in_game_route_query-f1f3a3adb8761bd4394f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-e01e2b0222ab8d3ec184"></a>

**90° CCW: unverified** — `in_game_route_query-e01e2b0222ab8d3ec184`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-d7c3c42a3347940c63ba"></a>

**180° CCW: unverified** — `in_game_route_query-d7c3c42a3347940c63ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-f87110ff16c3ba7c2ad4"></a>

**270° CCW: unverified** — `in_game_route_query-f87110ff16c3ba7c2ad4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-7913d9835c08c5437360"></a>

**0° CCW: unverified** — `in_game_route_query-7913d9835c08c5437360`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-3c52b67aa88beafb101d"></a>

**90° CCW: unverified** — `in_game_route_query-3c52b67aa88beafb101d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-ac174465e61df1ae99e5"></a>

**180° CCW: unverified** — `in_game_route_query-ac174465e61df1ae99e5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-03d6f8094e3d0c630ab8"></a>

**270° CCW: unverified** — `in_game_route_query-03d6f8094e3d0c630ab8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-f77a11a467ab4fee0a90"></a>

**0° CCW: unverified** — `in_game_route_query-f77a11a467ab4fee0a90`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-0f7cd0e86500cc505f1a"></a>

**90° CCW: unverified** — `in_game_route_query-0f7cd0e86500cc505f1a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-34e426384763720fb5d2"></a>

**180° CCW: unverified** — `in_game_route_query-34e426384763720fb5d2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-cd3f460ad792f4cf81e8"></a>

**270° CCW: unverified** — `in_game_route_query-cd3f460ad792f4cf81e8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-dde6ddba312e61808ffa"></a>

**0° CCW: unverified** — `in_game_route_query-dde6ddba312e61808ffa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-84234f10ae0a3dfe1e4d"></a>

**90° CCW: unverified** — `in_game_route_query-84234f10ae0a3dfe1e4d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-5951c74fcaa3983aab87"></a>

**180° CCW: unverified** — `in_game_route_query-5951c74fcaa3983aab87`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-4d49f731f02ea26bedaa"></a>

**270° CCW: unverified** — `in_game_route_query-4d49f731f02ea26bedaa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-1cab22d8daf6dfcb2735"></a>

**0° CCW: unverified** — `in_game_route_query-1cab22d8daf6dfcb2735`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-e4e490f635136e57a0bc"></a>

**90° CCW: unverified** — `in_game_route_query-e4e490f635136e57a0bc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-59ec651e74d3602cd462"></a>

**180° CCW: unverified** — `in_game_route_query-59ec651e74d3602cd462`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-68a6ef40907d39cb91ea"></a>

**270° CCW: unverified** — `in_game_route_query-68a6ef40907d39cb91ea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-83e959532d623cd67798"></a>

**0° CCW: unverified** — `in_game_route_query-83e959532d623cd67798`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-0d1c79c5bda19a588348"></a>

**90° CCW: unverified** — `in_game_route_query-0d1c79c5bda19a588348`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-ff6d9c15dcb9cd142d45"></a>

**180° CCW: unverified** — `in_game_route_query-ff6d9c15dcb9cd142d45`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-98b174db0d7e11cc7b21"></a>

**270° CCW: unverified** — `in_game_route_query-98b174db0d7e11cc7b21`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-f1f3a3adb8761bd4394f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e01e2b0222ab8d3ec184">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d7c3c42a3347940c63ba">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f87110ff16c3ba7c2ad4">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-7913d9835c08c5437360">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3c52b67aa88beafb101d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ac174465e61df1ae99e5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-03d6f8094e3d0c630ab8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-f77a11a467ab4fee0a90">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0f7cd0e86500cc505f1a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-34e426384763720fb5d2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cd3f460ad792f4cf81e8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-dde6ddba312e61808ffa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-84234f10ae0a3dfe1e4d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5951c74fcaa3983aab87">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4d49f731f02ea26bedaa">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-1cab22d8daf6dfcb2735">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e4e490f635136e57a0bc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-59ec651e74d3602cd462">[ ] unverified</a> | <a href="#case-in_game_visible_travel-68a6ef40907d39cb91ea">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-83e959532d623cd67798">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0d1c79c5bda19a588348">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff6d9c15dcb9cd142d45">[ ] unverified</a> | <a href="#case-in_game_visible_travel-98b174db0d7e11cc7b21">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-f1f3a3adb8761bd4394f"></a>

**0° CCW: unverified** — `in_game_visible_travel-f1f3a3adb8761bd4394f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-e01e2b0222ab8d3ec184"></a>

**90° CCW: unverified** — `in_game_visible_travel-e01e2b0222ab8d3ec184`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-d7c3c42a3347940c63ba"></a>

**180° CCW: unverified** — `in_game_visible_travel-d7c3c42a3347940c63ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-f87110ff16c3ba7c2ad4"></a>

**270° CCW: unverified** — `in_game_visible_travel-f87110ff16c3ba7c2ad4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-7913d9835c08c5437360"></a>

**0° CCW: unverified** — `in_game_visible_travel-7913d9835c08c5437360`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-3c52b67aa88beafb101d"></a>

**90° CCW: unverified** — `in_game_visible_travel-3c52b67aa88beafb101d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-ac174465e61df1ae99e5"></a>

**180° CCW: unverified** — `in_game_visible_travel-ac174465e61df1ae99e5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-03d6f8094e3d0c630ab8"></a>

**270° CCW: unverified** — `in_game_visible_travel-03d6f8094e3d0c630ab8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-f77a11a467ab4fee0a90"></a>

**0° CCW: unverified** — `in_game_visible_travel-f77a11a467ab4fee0a90`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-0f7cd0e86500cc505f1a"></a>

**90° CCW: unverified** — `in_game_visible_travel-0f7cd0e86500cc505f1a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-34e426384763720fb5d2"></a>

**180° CCW: unverified** — `in_game_visible_travel-34e426384763720fb5d2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-cd3f460ad792f4cf81e8"></a>

**270° CCW: unverified** — `in_game_visible_travel-cd3f460ad792f4cf81e8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-10-out; entry: channel-03-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-dde6ddba312e61808ffa"></a>

**0° CCW: unverified** — `in_game_visible_travel-dde6ddba312e61808ffa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-84234f10ae0a3dfe1e4d"></a>

**90° CCW: unverified** — `in_game_visible_travel-84234f10ae0a3dfe1e4d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-5951c74fcaa3983aab87"></a>

**180° CCW: unverified** — `in_game_visible_travel-5951c74fcaa3983aab87`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-4d49f731f02ea26bedaa"></a>

**270° CCW: unverified** — `in_game_visible_travel-4d49f731f02ea26bedaa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-06-out; entry: channel-04-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-1cab22d8daf6dfcb2735"></a>

**0° CCW: unverified** — `in_game_visible_travel-1cab22d8daf6dfcb2735`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-e4e490f635136e57a0bc"></a>

**90° CCW: unverified** — `in_game_visible_travel-e4e490f635136e57a0bc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-59ec651e74d3602cd462"></a>

**180° CCW: unverified** — `in_game_visible_travel-59ec651e74d3602cd462`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-68a6ef40907d39cb91ea"></a>

**270° CCW: unverified** — `in_game_visible_travel-68a6ef40907d39cb91ea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-83e959532d623cd67798"></a>

**0° CCW: unverified** — `in_game_visible_travel-83e959532d623cd67798`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-0d1c79c5bda19a588348"></a>

**90° CCW: unverified** — `in_game_visible_travel-0d1c79c5bda19a588348`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-ff6d9c15dcb9cd142d45"></a>

**180° CCW: unverified** — `in_game_visible_travel-ff6d9c15dcb9cd142d45`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-98b174db0d7e11cc7b21"></a>

**270° CCW: unverified** — `in_game_visible_travel-98b174db0d7e11cc7b21`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-f04154c4f70c1a3c142a">[ ] unverified</a> | <a href="#case-in_game_route_query-56bd6fcbdf0c7fd6a23f">[ ] unverified</a> | <a href="#case-in_game_route_query-7c4d59b738baa6b5600c">[ ] unverified</a> | <a href="#case-in_game_route_query-61da79d2894644128f3c">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-4aeb553200bd52ae4341">[ ] unverified</a> | <a href="#case-in_game_route_query-0f045cad0fbcf73ac607">[ ] unverified</a> | <a href="#case-in_game_route_query-6442457beeab6e4cfc29">[ ] unverified</a> | <a href="#case-in_game_route_query-f24978277cd4dada263f">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-f04154c4f70c1a3c142a"></a>

**0° CCW: unverified** — `in_game_route_query-f04154c4f70c1a3c142a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-56bd6fcbdf0c7fd6a23f"></a>

**90° CCW: unverified** — `in_game_route_query-56bd6fcbdf0c7fd6a23f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-7c4d59b738baa6b5600c"></a>

**180° CCW: unverified** — `in_game_route_query-7c4d59b738baa6b5600c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-61da79d2894644128f3c"></a>

**270° CCW: unverified** — `in_game_route_query-61da79d2894644128f3c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-4aeb553200bd52ae4341"></a>

**0° CCW: unverified** — `in_game_route_query-4aeb553200bd52ae4341`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-0f045cad0fbcf73ac607"></a>

**90° CCW: unverified** — `in_game_route_query-0f045cad0fbcf73ac607`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-6442457beeab6e4cfc29"></a>

**180° CCW: unverified** — `in_game_route_query-6442457beeab6e4cfc29`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-f24978277cd4dada263f"></a>

**270° CCW: unverified** — `in_game_route_query-f24978277cd4dada263f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-f04154c4f70c1a3c142a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-56bd6fcbdf0c7fd6a23f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7c4d59b738baa6b5600c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-61da79d2894644128f3c">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-4aeb553200bd52ae4341">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0f045cad0fbcf73ac607">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6442457beeab6e4cfc29">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f24978277cd4dada263f">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-f04154c4f70c1a3c142a"></a>

**0° CCW: unverified** — `in_game_visible_travel-f04154c4f70c1a3c142a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-56bd6fcbdf0c7fd6a23f"></a>

**90° CCW: unverified** — `in_game_visible_travel-56bd6fcbdf0c7fd6a23f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-7c4d59b738baa6b5600c"></a>

**180° CCW: unverified** — `in_game_visible_travel-7c4d59b738baa6b5600c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-61da79d2894644128f3c"></a>

**270° CCW: unverified** — `in_game_visible_travel-61da79d2894644128f3c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-4aeb553200bd52ae4341"></a>

**0° CCW: unverified** — `in_game_visible_travel-4aeb553200bd52ae4341`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-0f045cad0fbcf73ac607"></a>

**90° CCW: unverified** — `in_game_visible_travel-0f045cad0fbcf73ac607`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-6442457beeab6e4cfc29"></a>

**180° CCW: unverified** — `in_game_visible_travel-6442457beeab6e4cfc29`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-f24978277cd4dada263f"></a>

**270° CCW: unverified** — `in_game_visible_travel-f24978277cd4dada263f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 76 cases; unverified: 76</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e14f82208382a71f170">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2017e19176a5cbd1242f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b785ab33fadebef7854c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ea42a8a62e9b0b4f36c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a2bb053161908030ef8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4fd71f3df2f7bd56440">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f54a2e92568e95d388b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afcaef05f39142657901">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2544a94456d75ac78985">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5683ae94fd4a4ff6015">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a810d1eb0e147cc341eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-685707ef471e458b47bd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1057754f626888e6322d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69a9d5210b433033dd48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6b4bd86c554b68674e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ae367663e57eb3e21d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a80209bee990964aaa7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2623a8bffe77a91ec27c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-560078ffbdb229e3083d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45e2e7c43d229f0ac2fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0f95c175f39d120db88c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a4ca1e62f35f5b708d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02a764fd705673d21c5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50ccd66ef9f00ae74919">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cf2e326512a068a7ec2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9320635e974f45e07512">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed38eb05fc4d5c7d620a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e86119c26069525ac7d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e050c94512722c883b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24c93b42e83166df1087">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fd209842b06c1737ca1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f18d5a0eee097d27cda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0366f32a8a1fff7d0fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-121a7cb33b9f6d702dda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-409671ba517f2a7801df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb03309548701f1f2425">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d135479ed97b42257912">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81af796b17d427f7d5ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e1dd9f74f232839fcbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2e087052a81f3a0ec0a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01d3c61ebbb94759b073">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b697f561cc725c69fb10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6562295f573a8eb45c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01a6628d29d882f9fc42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc604a3c4604f49361e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7917db5981ed413f34de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-628e340fb9268cce952b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-618766fc02515deaf319">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79813c45d99feb01e5ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ac95e7229932c644981">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ece09cfba029329855a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83c874121fa3cecdf7d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20c18bbc05fbd091a92e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23e45c6ce64f3f14a8db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76950275a015ca6c40a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cc4fb8e1c89e5d73cd8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4c347d79d4242e65a16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab7a73935931102ad81f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc7962151410b06636a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8d6e54abd7368dd7540">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-44a57e242701427950ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e0b3ca1dda14f552c9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2921c23f3237aca4a97c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5a8fa516248dfc2e527">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7e4d01ff4786ca4f570">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8922a0ffea0ff08e27cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-402afdc978d7aa2f6ed7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d16028be3d89d2835d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93b4267c1870233619dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b4688a07a4a2b8163d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58f73e5d840d565d1fdf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b7e989c4ced93aaa954">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a1511b0b3f8d25bb65ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0227b74f12e2ef7538b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-005c23131739295ca456">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7608d1326a8c870392c">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e14f82208382a71f170"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e14f82208382a71f170`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2017e19176a5cbd1242f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2017e19176a5cbd1242f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b785ab33fadebef7854c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b785ab33fadebef7854c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ea42a8a62e9b0b4f36c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0ea42a8a62e9b0b4f36c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a2bb053161908030ef8d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a2bb053161908030ef8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4fd71f3df2f7bd56440"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e4fd71f3df2f7bd56440`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f54a2e92568e95d388b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f54a2e92568e95d388b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afcaef05f39142657901"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afcaef05f39142657901`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2544a94456d75ac78985"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2544a94456d75ac78985`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5683ae94fd4a4ff6015"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e5683ae94fd4a4ff6015`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a810d1eb0e147cc341eb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a810d1eb0e147cc341eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-685707ef471e458b47bd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-685707ef471e458b47bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1057754f626888e6322d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1057754f626888e6322d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69a9d5210b433033dd48"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-69a9d5210b433033dd48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6b4bd86c554b68674e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d6b4bd86c554b68674e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ae367663e57eb3e21d8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8ae367663e57eb3e21d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a80209bee990964aaa7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a80209bee990964aaa7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2623a8bffe77a91ec27c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2623a8bffe77a91ec27c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-560078ffbdb229e3083d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-560078ffbdb229e3083d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45e2e7c43d229f0ac2fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45e2e7c43d229f0ac2fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0f95c175f39d120db88c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0f95c175f39d120db88c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a4ca1e62f35f5b708d3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a4ca1e62f35f5b708d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02a764fd705673d21c5d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-02a764fd705673d21c5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50ccd66ef9f00ae74919"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-50ccd66ef9f00ae74919`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cf2e326512a068a7ec2e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cf2e326512a068a7ec2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9320635e974f45e07512"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9320635e974f45e07512`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed38eb05fc4d5c7d620a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed38eb05fc4d5c7d620a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e86119c26069525ac7d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e86119c26069525ac7d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e050c94512722c883b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e050c94512722c883b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24c93b42e83166df1087"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24c93b42e83166df1087`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fd209842b06c1737ca1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4fd209842b06c1737ca1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f18d5a0eee097d27cda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0f18d5a0eee097d27cda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0366f32a8a1fff7d0fa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0366f32a8a1fff7d0fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-121a7cb33b9f6d702dda"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-121a7cb33b9f6d702dda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-409671ba517f2a7801df"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-409671ba517f2a7801df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb03309548701f1f2425"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fb03309548701f1f2425`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d135479ed97b42257912"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d135479ed97b42257912`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81af796b17d427f7d5ed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81af796b17d427f7d5ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e1dd9f74f232839fcbf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3e1dd9f74f232839fcbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2e087052a81f3a0ec0a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f2e087052a81f3a0ec0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-01d3c61ebbb94759b073"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01d3c61ebbb94759b073`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b697f561cc725c69fb10"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b697f561cc725c69fb10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6562295f573a8eb45c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d6562295f573a8eb45c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01a6628d29d882f9fc42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-01a6628d29d882f9fc42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc604a3c4604f49361e3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc604a3c4604f49361e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7917db5981ed413f34de"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7917db5981ed413f34de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-628e340fb9268cce952b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-628e340fb9268cce952b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-618766fc02515deaf319"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-618766fc02515deaf319`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79813c45d99feb01e5ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79813c45d99feb01e5ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ac95e7229932c644981"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ac95e7229932c644981`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ece09cfba029329855a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ece09cfba029329855a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83c874121fa3cecdf7d8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83c874121fa3cecdf7d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20c18bbc05fbd091a92e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20c18bbc05fbd091a92e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23e45c6ce64f3f14a8db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23e45c6ce64f3f14a8db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76950275a015ca6c40a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-76950275a015ca6c40a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cc4fb8e1c89e5d73cd8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5cc4fb8e1c89e5d73cd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4c347d79d4242e65a16"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4c347d79d4242e65a16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab7a73935931102ad81f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ab7a73935931102ad81f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc7962151410b06636a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc7962151410b06636a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8d6e54abd7368dd7540"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b8d6e54abd7368dd7540`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-44a57e242701427950ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-44a57e242701427950ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e0b3ca1dda14f552c9e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1e0b3ca1dda14f552c9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2921c23f3237aca4a97c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2921c23f3237aca4a97c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5a8fa516248dfc2e527"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5a8fa516248dfc2e527`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7e4d01ff4786ca4f570"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7e4d01ff4786ca4f570`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8922a0ffea0ff08e27cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8922a0ffea0ff08e27cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-402afdc978d7aa2f6ed7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-402afdc978d7aa2f6ed7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d16028be3d89d2835d6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4d16028be3d89d2835d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93b4267c1870233619dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93b4267c1870233619dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b4688a07a4a2b8163d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0b4688a07a4a2b8163d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58f73e5d840d565d1fdf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-58f73e5d840d565d1fdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b7e989c4ced93aaa954"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b7e989c4ced93aaa954`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a1511b0b3f8d25bb65ce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a1511b0b3f8d25bb65ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0227b74f12e2ef7538b8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0227b74f12e2ef7538b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-005c23131739295ca456"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-005c23131739295ca456`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7608d1326a8c870392c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7608d1326a8c870392c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c3691b679bea36802e18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04271ccd31e4a7159638">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8ec82cfcd4b9e174126">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b07b21e876286dd2c87">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f62c40f0942fc78815d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d79d0ff64f73bc0aedca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2414f5050f200ff34cd8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-811a3ad4e25f26a9607f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0564caff8654ec8d6be7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-feacb14f67a98d01c496">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fdbcbdee8167ae22be4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2781a00dc8f4ada6d5e1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0f64abd5f89070c4a635">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-425682cc3fe5f3e26784">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b36a2721e09667b42340">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78e3e0f0d4c1e6623ec3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3bf53d3cb9ef692d34f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2aeb67f3c168012a353a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aded84d50eed9432a760">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b28386c887f3c85d8d49">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9c952ee5b5823a85311c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7841da008e78065d6f06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ff0535d1c4520cef62e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3141430c739cc140ea4f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-70bf29af85c714b9e49f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-516be6956bd5bae9977d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9612f06ad10e99e31d0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a54ebf67fb58138e7c17">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-383c2942b58644dcf72c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cc64bb28ddaeb272c5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3dfa455f478985d1338d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3225275c939a96d8e84b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-522d1e164d0be3cd7c5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62ffed676dd8b247166e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d980b569c5ece4b3b2f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-534673c48207d33f8316">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a736ccd73fce5dd88b92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3b2f45f4db8e364ff53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-323cbacfd75881e248ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-284f8f1e9cce32269a34">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c3691b679bea36802e18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c3691b679bea36802e18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04271ccd31e4a7159638"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04271ccd31e4a7159638`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8ec82cfcd4b9e174126"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a8ec82cfcd4b9e174126`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b07b21e876286dd2c87"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b07b21e876286dd2c87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f62c40f0942fc78815d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f62c40f0942fc78815d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d79d0ff64f73bc0aedca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d79d0ff64f73bc0aedca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2414f5050f200ff34cd8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2414f5050f200ff34cd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-811a3ad4e25f26a9607f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-811a3ad4e25f26a9607f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0564caff8654ec8d6be7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0564caff8654ec8d6be7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-feacb14f67a98d01c496"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-feacb14f67a98d01c496`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fdbcbdee8167ae22be4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1fdbcbdee8167ae22be4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2781a00dc8f4ada6d5e1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2781a00dc8f4ada6d5e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0f64abd5f89070c4a635"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0f64abd5f89070c4a635`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-425682cc3fe5f3e26784"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-425682cc3fe5f3e26784`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b36a2721e09667b42340"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b36a2721e09667b42340`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78e3e0f0d4c1e6623ec3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-78e3e0f0d4c1e6623ec3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3bf53d3cb9ef692d34f4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3bf53d3cb9ef692d34f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2aeb67f3c168012a353a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2aeb67f3c168012a353a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aded84d50eed9432a760"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aded84d50eed9432a760`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b28386c887f3c85d8d49"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b28386c887f3c85d8d49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9c952ee5b5823a85311c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9c952ee5b5823a85311c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7841da008e78065d6f06"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7841da008e78065d6f06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ff0535d1c4520cef62e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ff0535d1c4520cef62e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3141430c739cc140ea4f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3141430c739cc140ea4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-70bf29af85c714b9e49f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-70bf29af85c714b9e49f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-516be6956bd5bae9977d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-516be6956bd5bae9977d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9612f06ad10e99e31d0b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9612f06ad10e99e31d0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a54ebf67fb58138e7c17"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a54ebf67fb58138e7c17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-383c2942b58644dcf72c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-383c2942b58644dcf72c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cc64bb28ddaeb272c5a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7cc64bb28ddaeb272c5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3dfa455f478985d1338d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3dfa455f478985d1338d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3225275c939a96d8e84b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3225275c939a96d8e84b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-522d1e164d0be3cd7c5a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-522d1e164d0be3cd7c5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62ffed676dd8b247166e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62ffed676dd8b247166e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d980b569c5ece4b3b2f9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d980b569c5ece4b3b2f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-534673c48207d33f8316"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-534673c48207d33f8316`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a736ccd73fce5dd88b92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a736ccd73fce5dd88b92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3b2f45f4db8e364ff53"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e3b2f45f4db8e364ff53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-323cbacfd75881e248ee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-323cbacfd75881e248ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-284f8f1e9cce32269a34"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-284f8f1e9cce32269a34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-417881c5dab0d59589e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73213ec1eb86c58e5faa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4319449c788ddfa226c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-685e2b5316a54c7ea7cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3e60cf6078bbb857fc91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2b9b675f81d0f48bda9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b723f3ac4f498bd2d105">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b7ec8a75e3d38bde4cf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e42926d586af641e7097">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69603d0ea0779608dbb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a7186ea58bb9a6044f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b6ce39310929004f8ba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2363faeb784f66d4bece">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d1154a9b6beacf3e63d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0bdc180c6e2aceb56fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a08179d0ab2bc23b71e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1524f783bf26a1c6d1af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7fab5e2e38dd0a37af61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9eb1ed8668c036e8f009">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9af758fddf31b2989c08">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a758233b6f9e533a4804">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9ef94414ca9b1e863af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e03a2dd805d76126d067">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ecca1a016e11a2eee93c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0b30e2c60d6cead6b4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44eae998c11701cc20ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b36a72f53633ddfb3c40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06bf7a7988b574b20590">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fd04c81ca5b6b1d6834f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab3866f6187767d8d23b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8db58f30e1bc1812b8fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42c2ff4a887f1cf9927e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2d174dd4e7fea5b3259b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c268774d1882b55387c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8878bd85063d31e1cc1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-460101a5c2c8a4235a75">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3dc854da2cfe913ad888">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94c78eff17f7e17cada4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fe0857625d44e6f2d5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6860cdcc3fd3a12ccf05">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-417881c5dab0d59589e8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-417881c5dab0d59589e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73213ec1eb86c58e5faa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-73213ec1eb86c58e5faa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4319449c788ddfa226c1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4319449c788ddfa226c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-685e2b5316a54c7ea7cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-685e2b5316a54c7ea7cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3e60cf6078bbb857fc91"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e60cf6078bbb857fc91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2b9b675f81d0f48bda9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f2b9b675f81d0f48bda9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b723f3ac4f498bd2d105"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b723f3ac4f498bd2d105`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b7ec8a75e3d38bde4cf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1b7ec8a75e3d38bde4cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e42926d586af641e7097"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e42926d586af641e7097`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69603d0ea0779608dbb3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-69603d0ea0779608dbb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a7186ea58bb9a6044f9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6a7186ea58bb9a6044f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b6ce39310929004f8ba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7b6ce39310929004f8ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2363faeb784f66d4bece"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2363faeb784f66d4bece`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d1154a9b6beacf3e63d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1d1154a9b6beacf3e63d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0bdc180c6e2aceb56fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a0bdc180c6e2aceb56fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a08179d0ab2bc23b71e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a08179d0ab2bc23b71e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1524f783bf26a1c6d1af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1524f783bf26a1c6d1af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7fab5e2e38dd0a37af61"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7fab5e2e38dd0a37af61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9eb1ed8668c036e8f009"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9eb1ed8668c036e8f009`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9af758fddf31b2989c08"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9af758fddf31b2989c08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a758233b6f9e533a4804"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a758233b6f9e533a4804`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9ef94414ca9b1e863af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c9ef94414ca9b1e863af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e03a2dd805d76126d067"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e03a2dd805d76126d067`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ecca1a016e11a2eee93c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ecca1a016e11a2eee93c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0b30e2c60d6cead6b4e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0b30e2c60d6cead6b4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44eae998c11701cc20ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-44eae998c11701cc20ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b36a72f53633ddfb3c40"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b36a72f53633ddfb3c40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06bf7a7988b574b20590"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-06bf7a7988b574b20590`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fd04c81ca5b6b1d6834f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fd04c81ca5b6b1d6834f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab3866f6187767d8d23b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ab3866f6187767d8d23b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8db58f30e1bc1812b8fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8db58f30e1bc1812b8fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42c2ff4a887f1cf9927e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-42c2ff4a887f1cf9927e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2d174dd4e7fea5b3259b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d174dd4e7fea5b3259b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c268774d1882b55387c1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c268774d1882b55387c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8878bd85063d31e1cc1d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8878bd85063d31e1cc1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-460101a5c2c8a4235a75"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-460101a5c2c8a4235a75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3dc854da2cfe913ad888"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3dc854da2cfe913ad888`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94c78eff17f7e17cada4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94c78eff17f7e17cada4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fe0857625d44e6f2d5e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0fe0857625d44e6f2d5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6860cdcc3fd3a12ccf05"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6860cdcc3fd3a12ccf05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5873ac2a9efda77b3d66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0282ab8ab135bd48bd41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a94c6b3531da913fb09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96d26c7fa43652557db4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e52589fbaca8992c87a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-933570b2531fd1fce606">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d177a54cc299c8e3a60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43822031067f99d0d90f">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5873ac2a9efda77b3d66"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5873ac2a9efda77b3d66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0282ab8ab135bd48bd41"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0282ab8ab135bd48bd41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a94c6b3531da913fb09"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7a94c6b3531da913fb09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96d26c7fa43652557db4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-96d26c7fa43652557db4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e52589fbaca8992c87a9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e52589fbaca8992c87a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-933570b2531fd1fce606"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-933570b2531fd1fce606`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d177a54cc299c8e3a60"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d177a54cc299c8e3a60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43822031067f99d0d90f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43822031067f99d0d90f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-southeast-terminal:canonical-southeast | <a href="#case-preview_review-d7bc0629de79899ded2e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-southeast-terminal:canonical-top | <a href="#case-preview_review-5d9b9c3a385d2710d97e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-southeast-terminal:connection-overview | <a href="#case-preview_review-b7a5ebfb1b3c69deebc7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-southeast-terminal:canonical-southeast</summary>

<a id="case-preview_review-d7bc0629de79899ded2e"></a>

**General: unverified** — `preview_review-d7bc0629de79899ded2e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-southeast-terminal:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-southeast-terminal:canonical-top</summary>

<a id="case-preview_review-5d9b9c3a385d2710d97e"></a>

**General: unverified** — `preview_review-5d9b9c3a385d2710d97e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-southeast-terminal:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-southeast-terminal:connection-overview</summary>

<a id="case-preview_review-b7a5ebfb1b3c69deebc7"></a>

**General: unverified** — `preview_review-b7a5ebfb1b3c69deebc7`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-southeast-terminal:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).
