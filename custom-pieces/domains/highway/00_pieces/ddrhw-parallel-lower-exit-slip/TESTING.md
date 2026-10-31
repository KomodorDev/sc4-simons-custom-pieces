---
title: "Testing: DD RHW-4 — L1 Exit Slip Lanes — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1 Exit Slip Lanes — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-lower-exit-slip**, used once as **P04** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 2 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X6, Y8, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-10-out` | road / 1 / primary | out | [-8.0, -15.029437, 4.364109]; [-0.7071067811865587, -0.7071067811865365]; -0.179118533 | `path-interface-6f98c9419d701c4a592c` |
| `channel-11-out` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-02-in` | road / 1 / primary | in | [-0.970563, -8.0, 6.144726]; [-0.7071067811865476, -0.7071067811865476]; -0.17907534 | `path-interface-61a771345641cff0130a` |
| `channel-12-out` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865474, -0.7071067811865478]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-03-in` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865474, 0.7071067811865478]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-04-in` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [-0.7071067811865474, -0.7071067811865478]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-13-out` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [0.7071067811865474, 0.7071067811865478]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-05-in` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-14-out` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-15-out` | road / 1 / primary | out | [8.0, 0.104467, 7.5]; [-0.9404586044448431, -0.3399082425091487]; 0.0 | `path-interface-dd0badef63ec6dee79f2` |
| `channel-16-out` | road / 1 / primary | out | [12.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-06-in` | road / 1 / primary | in | [12.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-17-out` | road / 1 / primary | out | [19.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-07-in` | road / 1 / primary | in | [19.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-08-in` | road / 1 / primary | in | [24.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-18-out` | road / 1 / primary | out | [24.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-09-in` | road / 1 / primary | in | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-19-out` | road / 1 / primary | out | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-14-out` | primary |
| road | `channel-02-in` → `channel-10-out` | primary |
| road | `channel-03-in` → `channel-13-out` | primary |
| road | `channel-04-in` → `channel-12-out` | primary |
| road | `channel-05-in` → `channel-11-out` | primary |
| road | `channel-06-in` → `channel-19-out` | primary |
| road | `channel-07-in` → `channel-18-out` | primary |
| road | `channel-08-in` → `channel-17-out` | primary |
| road | `channel-09-in` → `channel-15-out` | primary |
| road | `channel-09-in` → `channel-16-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X7, Y8), (X6, Y7)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-parts-01
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-lower-exit-slip --build dist/ddrhw-parallel-diamond-parts-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-lower-exit-slip
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

## 4. Game checks

1. Select this exact component through the assembly button, match P04 at **X6, Y8**, and confirm that the occupied preview squares match **(X7, Y8), (X6, Y7)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and check its pavement variant. Then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-lower-exit-slip** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. The two occupied cells lie diagonally inside a sparse 2 × 2 rectangle. Its construction reference is an empty corner, so align both occupied preview cells instead of assuming that the reference position is a third tile. Complete boundary cards include both highway levels and every access fragment; matching only the named ramp is insufficient. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/40 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/40 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 421, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-exit-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-exit-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b0fa3bba38db48447050">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b0fa3bba38db48447050"></a>

**General: unverified** — `software_resources-b0fa3bba38db48447050`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b0fa3bba38db48447050">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b0fa3bba38db48447050"></a>

**General: unverified** — `software_connectivity-b0fa3bba38db48447050`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-2e95d1a948c33f76e34f">[ ] unverified</a> | <a href="#case-in_game_render-4df8b5dca435e10b4af6">[ ] unverified</a> | <a href="#case-in_game_render-0fa702a194362fff1761">[ ] unverified</a> | <a href="#case-in_game_render-0821a24e8076663aefb3">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-2e95d1a948c33f76e34f"></a>

**0° CCW: unverified** — `in_game_render-2e95d1a948c33f76e34f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-4df8b5dca435e10b4af6"></a>

**90° CCW: unverified** — `in_game_render-4df8b5dca435e10b4af6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0fa702a194362fff1761"></a>

**180° CCW: unverified** — `in_game_render-0fa702a194362fff1761`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0821a24e8076663aefb3"></a>

**270° CCW: unverified** — `in_game_render-0821a24e8076663aefb3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-2e95d1a948c33f76e34f">[ ] unverified</a> | <a href="#case-in_game_placement-4df8b5dca435e10b4af6">[ ] unverified</a> | <a href="#case-in_game_placement-0fa702a194362fff1761">[ ] unverified</a> | <a href="#case-in_game_placement-0821a24e8076663aefb3">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-2e95d1a948c33f76e34f"></a>

**0° CCW: unverified** — `in_game_placement-2e95d1a948c33f76e34f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-4df8b5dca435e10b4af6"></a>

**90° CCW: unverified** — `in_game_placement-4df8b5dca435e10b4af6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0fa702a194362fff1761"></a>

**180° CCW: unverified** — `in_game_placement-0fa702a194362fff1761`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0821a24e8076663aefb3"></a>

**270° CCW: unverified** — `in_game_placement-0821a24e8076663aefb3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-2e95d1a948c33f76e34f">[ ] unverified</a> | <a href="#case-in_game_demolition-4df8b5dca435e10b4af6">[ ] unverified</a> | <a href="#case-in_game_demolition-0fa702a194362fff1761">[ ] unverified</a> | <a href="#case-in_game_demolition-0821a24e8076663aefb3">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-2e95d1a948c33f76e34f"></a>

**0° CCW: unverified** — `in_game_demolition-2e95d1a948c33f76e34f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-4df8b5dca435e10b4af6"></a>

**90° CCW: unverified** — `in_game_demolition-4df8b5dca435e10b4af6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0fa702a194362fff1761"></a>

**180° CCW: unverified** — `in_game_demolition-0fa702a194362fff1761`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0821a24e8076663aefb3"></a>

**270° CCW: unverified** — `in_game_demolition-0821a24e8076663aefb3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-2e95d1a948c33f76e34f">[ ] unverified</a> | <a href="#case-in_game_save_reload-4df8b5dca435e10b4af6">[ ] unverified</a> | <a href="#case-in_game_save_reload-0fa702a194362fff1761">[ ] unverified</a> | <a href="#case-in_game_save_reload-0821a24e8076663aefb3">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-2e95d1a948c33f76e34f"></a>

**0° CCW: unverified** — `in_game_save_reload-2e95d1a948c33f76e34f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-4df8b5dca435e10b4af6"></a>

**90° CCW: unverified** — `in_game_save_reload-4df8b5dca435e10b4af6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0fa702a194362fff1761"></a>

**180° CCW: unverified** — `in_game_save_reload-0fa702a194362fff1761`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0821a24e8076663aefb3"></a>

**270° CCW: unverified** — `in_game_save_reload-0821a24e8076663aefb3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-2f6a6c53c3a7c53eb495">[ ] unverified</a> | <a href="#case-in_game_route_query-74c65900d1c2feb33e3d">[ ] unverified</a> | <a href="#case-in_game_route_query-77f9d197779d1b9f3392">[ ] unverified</a> | <a href="#case-in_game_route_query-d43aa9ecce57b5b9ab0e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-8fc881bd8a14cf7a2f31">[ ] unverified</a> | <a href="#case-in_game_route_query-c687a5362cd14bb59219">[ ] unverified</a> | <a href="#case-in_game_route_query-6ae6ec21c1f234a50e8a">[ ] unverified</a> | <a href="#case-in_game_route_query-639a617ee850de339951">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-918d417cfadc80d8527a">[ ] unverified</a> | <a href="#case-in_game_route_query-d2fd422957ef6ae171d4">[ ] unverified</a> | <a href="#case-in_game_route_query-f77a3ceec4b41a1eba81">[ ] unverified</a> | <a href="#case-in_game_route_query-05821264049523f481d7">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-bce52dcdabf34ade2368">[ ] unverified</a> | <a href="#case-in_game_route_query-9d993cd78d8b14155340">[ ] unverified</a> | <a href="#case-in_game_route_query-be25f1d18cd0a8eab00a">[ ] unverified</a> | <a href="#case-in_game_route_query-3a036477341c337b8cd3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-ec8cee665d96e8e60a3e">[ ] unverified</a> | <a href="#case-in_game_route_query-2be86a9dbf12be283e19">[ ] unverified</a> | <a href="#case-in_game_route_query-4641a34c9cb43074ddde">[ ] unverified</a> | <a href="#case-in_game_route_query-2f6c48ef83360d2734c3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-678c7032212ee15551ba">[ ] unverified</a> | <a href="#case-in_game_route_query-f2c1c3331d5c47a4d2c6">[ ] unverified</a> | <a href="#case-in_game_route_query-7efa700fd3bffabcf46c">[ ] unverified</a> | <a href="#case-in_game_route_query-101e12849aa25da5dbfd">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-eaf03e63d94cd414ba9a">[ ] unverified</a> | <a href="#case-in_game_route_query-7365663e8f625b3f186d">[ ] unverified</a> | <a href="#case-in_game_route_query-b4dd95a0d192ddc963cf">[ ] unverified</a> | <a href="#case-in_game_route_query-c08361f444089aaca003">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-1a621c2f861869aba8a2">[ ] unverified</a> | <a href="#case-in_game_route_query-e8b707971ab9bdf54946">[ ] unverified</a> | <a href="#case-in_game_route_query-196fe7a9ef95501fba2f">[ ] unverified</a> | <a href="#case-in_game_route_query-ea196e9dbcb501e9c234">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-4dbec316513eae3f5eb6">[ ] unverified</a> | <a href="#case-in_game_route_query-7e0dfb45ebc25884fcdc">[ ] unverified</a> | <a href="#case-in_game_route_query-4c07e6218d8d0cf7f7aa">[ ] unverified</a> | <a href="#case-in_game_route_query-6d146a53559a73b337ad">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-e3b9f578932830cafc74">[ ] unverified</a> | <a href="#case-in_game_route_query-767dae756abe7d765a8a">[ ] unverified</a> | <a href="#case-in_game_route_query-ca10d684c5df13233260">[ ] unverified</a> | <a href="#case-in_game_route_query-ea5d6639c5851d578729">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-2f6a6c53c3a7c53eb495"></a>

**0° CCW: unverified** — `in_game_route_query-2f6a6c53c3a7c53eb495`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-74c65900d1c2feb33e3d"></a>

**90° CCW: unverified** — `in_game_route_query-74c65900d1c2feb33e3d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-77f9d197779d1b9f3392"></a>

**180° CCW: unverified** — `in_game_route_query-77f9d197779d1b9f3392`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-d43aa9ecce57b5b9ab0e"></a>

**270° CCW: unverified** — `in_game_route_query-d43aa9ecce57b5b9ab0e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-8fc881bd8a14cf7a2f31"></a>

**0° CCW: unverified** — `in_game_route_query-8fc881bd8a14cf7a2f31`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-c687a5362cd14bb59219"></a>

**90° CCW: unverified** — `in_game_route_query-c687a5362cd14bb59219`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-6ae6ec21c1f234a50e8a"></a>

**180° CCW: unverified** — `in_game_route_query-6ae6ec21c1f234a50e8a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-639a617ee850de339951"></a>

**270° CCW: unverified** — `in_game_route_query-639a617ee850de339951`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-918d417cfadc80d8527a"></a>

**0° CCW: unverified** — `in_game_route_query-918d417cfadc80d8527a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-d2fd422957ef6ae171d4"></a>

**90° CCW: unverified** — `in_game_route_query-d2fd422957ef6ae171d4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-f77a3ceec4b41a1eba81"></a>

**180° CCW: unverified** — `in_game_route_query-f77a3ceec4b41a1eba81`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-05821264049523f481d7"></a>

**270° CCW: unverified** — `in_game_route_query-05821264049523f481d7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-bce52dcdabf34ade2368"></a>

**0° CCW: unverified** — `in_game_route_query-bce52dcdabf34ade2368`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-9d993cd78d8b14155340"></a>

**90° CCW: unverified** — `in_game_route_query-9d993cd78d8b14155340`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-be25f1d18cd0a8eab00a"></a>

**180° CCW: unverified** — `in_game_route_query-be25f1d18cd0a8eab00a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-3a036477341c337b8cd3"></a>

**270° CCW: unverified** — `in_game_route_query-3a036477341c337b8cd3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-ec8cee665d96e8e60a3e"></a>

**0° CCW: unverified** — `in_game_route_query-ec8cee665d96e8e60a3e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-2be86a9dbf12be283e19"></a>

**90° CCW: unverified** — `in_game_route_query-2be86a9dbf12be283e19`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-4641a34c9cb43074ddde"></a>

**180° CCW: unverified** — `in_game_route_query-4641a34c9cb43074ddde`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-2f6c48ef83360d2734c3"></a>

**270° CCW: unverified** — `in_game_route_query-2f6c48ef83360d2734c3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-678c7032212ee15551ba"></a>

**0° CCW: unverified** — `in_game_route_query-678c7032212ee15551ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-f2c1c3331d5c47a4d2c6"></a>

**90° CCW: unverified** — `in_game_route_query-f2c1c3331d5c47a4d2c6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-7efa700fd3bffabcf46c"></a>

**180° CCW: unverified** — `in_game_route_query-7efa700fd3bffabcf46c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-101e12849aa25da5dbfd"></a>

**270° CCW: unverified** — `in_game_route_query-101e12849aa25da5dbfd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-eaf03e63d94cd414ba9a"></a>

**0° CCW: unverified** — `in_game_route_query-eaf03e63d94cd414ba9a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-7365663e8f625b3f186d"></a>

**90° CCW: unverified** — `in_game_route_query-7365663e8f625b3f186d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-b4dd95a0d192ddc963cf"></a>

**180° CCW: unverified** — `in_game_route_query-b4dd95a0d192ddc963cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-c08361f444089aaca003"></a>

**270° CCW: unverified** — `in_game_route_query-c08361f444089aaca003`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-1a621c2f861869aba8a2"></a>

**0° CCW: unverified** — `in_game_route_query-1a621c2f861869aba8a2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-e8b707971ab9bdf54946"></a>

**90° CCW: unverified** — `in_game_route_query-e8b707971ab9bdf54946`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-196fe7a9ef95501fba2f"></a>

**180° CCW: unverified** — `in_game_route_query-196fe7a9ef95501fba2f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-ea196e9dbcb501e9c234"></a>

**270° CCW: unverified** — `in_game_route_query-ea196e9dbcb501e9c234`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-4dbec316513eae3f5eb6"></a>

**0° CCW: unverified** — `in_game_route_query-4dbec316513eae3f5eb6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-7e0dfb45ebc25884fcdc"></a>

**90° CCW: unverified** — `in_game_route_query-7e0dfb45ebc25884fcdc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-4c07e6218d8d0cf7f7aa"></a>

**180° CCW: unverified** — `in_game_route_query-4c07e6218d8d0cf7f7aa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-6d146a53559a73b337ad"></a>

**270° CCW: unverified** — `in_game_route_query-6d146a53559a73b337ad`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-e3b9f578932830cafc74"></a>

**0° CCW: unverified** — `in_game_route_query-e3b9f578932830cafc74`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-767dae756abe7d765a8a"></a>

**90° CCW: unverified** — `in_game_route_query-767dae756abe7d765a8a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-ca10d684c5df13233260"></a>

**180° CCW: unverified** — `in_game_route_query-ca10d684c5df13233260`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-ea5d6639c5851d578729"></a>

**270° CCW: unverified** — `in_game_route_query-ea5d6639c5851d578729`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-2f6a6c53c3a7c53eb495">[ ] unverified</a> | <a href="#case-in_game_visible_travel-74c65900d1c2feb33e3d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-77f9d197779d1b9f3392">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d43aa9ecce57b5b9ab0e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-8fc881bd8a14cf7a2f31">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c687a5362cd14bb59219">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6ae6ec21c1f234a50e8a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-639a617ee850de339951">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-918d417cfadc80d8527a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d2fd422957ef6ae171d4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f77a3ceec4b41a1eba81">[ ] unverified</a> | <a href="#case-in_game_visible_travel-05821264049523f481d7">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-bce52dcdabf34ade2368">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9d993cd78d8b14155340">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be25f1d18cd0a8eab00a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3a036477341c337b8cd3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-ec8cee665d96e8e60a3e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2be86a9dbf12be283e19">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4641a34c9cb43074ddde">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2f6c48ef83360d2734c3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-678c7032212ee15551ba">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f2c1c3331d5c47a4d2c6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7efa700fd3bffabcf46c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-101e12849aa25da5dbfd">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-eaf03e63d94cd414ba9a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7365663e8f625b3f186d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b4dd95a0d192ddc963cf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c08361f444089aaca003">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-1a621c2f861869aba8a2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e8b707971ab9bdf54946">[ ] unverified</a> | <a href="#case-in_game_visible_travel-196fe7a9ef95501fba2f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ea196e9dbcb501e9c234">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-4dbec316513eae3f5eb6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7e0dfb45ebc25884fcdc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4c07e6218d8d0cf7f7aa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6d146a53559a73b337ad">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-e3b9f578932830cafc74">[ ] unverified</a> | <a href="#case-in_game_visible_travel-767dae756abe7d765a8a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ca10d684c5df13233260">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ea5d6639c5851d578729">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-2f6a6c53c3a7c53eb495"></a>

**0° CCW: unverified** — `in_game_visible_travel-2f6a6c53c3a7c53eb495`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-74c65900d1c2feb33e3d"></a>

**90° CCW: unverified** — `in_game_visible_travel-74c65900d1c2feb33e3d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-77f9d197779d1b9f3392"></a>

**180° CCW: unverified** — `in_game_visible_travel-77f9d197779d1b9f3392`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-d43aa9ecce57b5b9ab0e"></a>

**270° CCW: unverified** — `in_game_visible_travel-d43aa9ecce57b5b9ab0e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-8fc881bd8a14cf7a2f31"></a>

**0° CCW: unverified** — `in_game_visible_travel-8fc881bd8a14cf7a2f31`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-c687a5362cd14bb59219"></a>

**90° CCW: unverified** — `in_game_visible_travel-c687a5362cd14bb59219`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-6ae6ec21c1f234a50e8a"></a>

**180° CCW: unverified** — `in_game_visible_travel-6ae6ec21c1f234a50e8a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-639a617ee850de339951"></a>

**270° CCW: unverified** — `in_game_visible_travel-639a617ee850de339951`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-918d417cfadc80d8527a"></a>

**0° CCW: unverified** — `in_game_visible_travel-918d417cfadc80d8527a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-d2fd422957ef6ae171d4"></a>

**90° CCW: unverified** — `in_game_visible_travel-d2fd422957ef6ae171d4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-f77a3ceec4b41a1eba81"></a>

**180° CCW: unverified** — `in_game_visible_travel-f77a3ceec4b41a1eba81`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-05821264049523f481d7"></a>

**270° CCW: unverified** — `in_game_visible_travel-05821264049523f481d7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-bce52dcdabf34ade2368"></a>

**0° CCW: unverified** — `in_game_visible_travel-bce52dcdabf34ade2368`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-9d993cd78d8b14155340"></a>

**90° CCW: unverified** — `in_game_visible_travel-9d993cd78d8b14155340`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-be25f1d18cd0a8eab00a"></a>

**180° CCW: unverified** — `in_game_visible_travel-be25f1d18cd0a8eab00a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-3a036477341c337b8cd3"></a>

**270° CCW: unverified** — `in_game_visible_travel-3a036477341c337b8cd3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-ec8cee665d96e8e60a3e"></a>

**0° CCW: unverified** — `in_game_visible_travel-ec8cee665d96e8e60a3e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-2be86a9dbf12be283e19"></a>

**90° CCW: unverified** — `in_game_visible_travel-2be86a9dbf12be283e19`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-4641a34c9cb43074ddde"></a>

**180° CCW: unverified** — `in_game_visible_travel-4641a34c9cb43074ddde`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-2f6c48ef83360d2734c3"></a>

**270° CCW: unverified** — `in_game_visible_travel-2f6c48ef83360d2734c3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-678c7032212ee15551ba"></a>

**0° CCW: unverified** — `in_game_visible_travel-678c7032212ee15551ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-f2c1c3331d5c47a4d2c6"></a>

**90° CCW: unverified** — `in_game_visible_travel-f2c1c3331d5c47a4d2c6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-7efa700fd3bffabcf46c"></a>

**180° CCW: unverified** — `in_game_visible_travel-7efa700fd3bffabcf46c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-101e12849aa25da5dbfd"></a>

**270° CCW: unverified** — `in_game_visible_travel-101e12849aa25da5dbfd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-eaf03e63d94cd414ba9a"></a>

**0° CCW: unverified** — `in_game_visible_travel-eaf03e63d94cd414ba9a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-7365663e8f625b3f186d"></a>

**90° CCW: unverified** — `in_game_visible_travel-7365663e8f625b3f186d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-b4dd95a0d192ddc963cf"></a>

**180° CCW: unverified** — `in_game_visible_travel-b4dd95a0d192ddc963cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-c08361f444089aaca003"></a>

**270° CCW: unverified** — `in_game_visible_travel-c08361f444089aaca003`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-1a621c2f861869aba8a2"></a>

**0° CCW: unverified** — `in_game_visible_travel-1a621c2f861869aba8a2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-e8b707971ab9bdf54946"></a>

**90° CCW: unverified** — `in_game_visible_travel-e8b707971ab9bdf54946`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-196fe7a9ef95501fba2f"></a>

**180° CCW: unverified** — `in_game_visible_travel-196fe7a9ef95501fba2f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-ea196e9dbcb501e9c234"></a>

**270° CCW: unverified** — `in_game_visible_travel-ea196e9dbcb501e9c234`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-4dbec316513eae3f5eb6"></a>

**0° CCW: unverified** — `in_game_visible_travel-4dbec316513eae3f5eb6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-7e0dfb45ebc25884fcdc"></a>

**90° CCW: unverified** — `in_game_visible_travel-7e0dfb45ebc25884fcdc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-4c07e6218d8d0cf7f7aa"></a>

**180° CCW: unverified** — `in_game_visible_travel-4c07e6218d8d0cf7f7aa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-6d146a53559a73b337ad"></a>

**270° CCW: unverified** — `in_game_visible_travel-6d146a53559a73b337ad`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-e3b9f578932830cafc74"></a>

**0° CCW: unverified** — `in_game_visible_travel-e3b9f578932830cafc74`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-767dae756abe7d765a8a"></a>

**90° CCW: unverified** — `in_game_visible_travel-767dae756abe7d765a8a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-ca10d684c5df13233260"></a>

**180° CCW: unverified** — `in_game_visible_travel-ca10d684c5df13233260`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-ea5d6639c5851d578729"></a>

**270° CCW: unverified** — `in_game_visible_travel-ea5d6639c5851d578729`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 320 cases; unverified: 320</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1b47d8de9a446ac90375">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-580fd7468f509582dbbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47a6c5ced60f78169eef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27ed3d0f61e44efb9353">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e19317eb88c3c9b9aae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afc9902b769c50aa3ff5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53eb06b86597620a3dfb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d29adc892e7237f6545">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6087de923aaf5be3823">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f787a28cc572aa3fb63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1541f8172c66aa625537">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ccb89060a3d9f1bdf7c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1d293b217f34f699af94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-602ecf47c382982c2282">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6838083068899e6db5b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aef1b60690b32534eb86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-90ff5bb2e9d59752e888">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61db688bd2d77be12028">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e1eb2a09265d8c74fd8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10eaf2b0083e368f1a95">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e18e21820a6767425c62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e3093f11c0f96e1deb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a17f6e7db262a474b12b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8dd36f177746cf2c759">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ceb9022d9c04387777e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e422500e79a6f641b65a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26fd2e363556aabd99a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fd894e45f154482bf3a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3abddb3b6785ba1d5457">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d46963cefb2994549d0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78418648c7d01a827ddc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ce91b96a15b0a607e42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3049cd6ca39c33b7f6e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbf212c3c7d4882304a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02b4836fb7d98cf91cbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2320da9854178cb64e85">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f754ba797f84969bad57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08e6aa71a63e3d9e6fae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa00687568fe6be350e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eefa9084658f0a3a9e4f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-beaac1309ddbd009e9f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b15a4ce71cdd6b5af419">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6b54dacbae6e5e55dbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-623663cae04e7724be14">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12e30c98f69302a54128">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2aae65a8ab527975935">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91d5671fd06517f5aa43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fe9dc9d18e2a255be16">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-05f2c4aa2138dce9c28e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-714a9b10c51c2a2bd3ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-328dec7be73778a02c6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b33a8269dbc1856edd92">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e0f4f033dbdcb5915cdf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36b4bdd3afce7c70990a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9a0653d86f92dfda680">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2103dda7e3e2569c6761">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7a9b89b924ee50b2981">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ffbcb6a9aec4a012c97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5edbd459202756a3c7ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca13b8aa56e07e3cf2c4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c9d0955f81d8226a817">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b088cc26dda648428fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2abc6c030a5cd7b4617e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8e0a0ee072e0a6656d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cb4d80c2d0bf944e4175">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a5f493424a8d1444957">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fd2e44ad9de46609b89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a3de178a5001384ed73">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f4ea71a24372d720b23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0af8d6de53e10a617329">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43884f14888c0edee4a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffb1cd8214b29484e1a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d026dabdc747ecdc3f30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-508200fb5b5ef8857683">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78e20a4ae3d3057ca573">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d54d757f719662b1d2b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec42db807cad000a383a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba253204c56936f64566">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70ec6e0dd156380a7676">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64986bf5d85ca37a4439">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9f9fe139944f70a85d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-848b70045084fc2a46fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fad6420e6ae74ece305d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8454fa00ea3e92033fb2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-edc1bab55470d7a0a71c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b27dbf75af9ede10d44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1320369ecbf65506957a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6d95712bec88a1e3d23">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a6a02fdfb9faab980a21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-903e93da8bda912d1d80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e466fea0923aa521799">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc64b106226ca275fa75">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f481357e2bcc14133f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e04de8d257168cce3f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc02e163c88047c7cc57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23e72e23aa613936582f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7d6095d6966fc47f687">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ad5a15126f480cfee1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bde6d47499f9fb0fdcc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c1f4c4dc44e61ac53bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac84551be725eb2eca26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dc2c98ee33baed947d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfdeb9acd270b61641a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ba2a23a722ec78c0c99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-119b5fe658fe952cb707">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74b465cbc2e045dde739">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb898bc2d69334289149">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07f2e5399bd1ca8799b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9452cbda0b546f26c335">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-616185ffe4042c3e246e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49ff1060e74f7b62893e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5441d0fc61b90d915120">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-363cd96f9801137cf988">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d9933a545ba09c2203f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-374f88cfd838907cb681">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a78a6d77df7393f0dfbb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2dd3f91217d217850582">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b349de25fa90a497321">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-641501463020ca4daed5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4a9e45f7e9f3379c46f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b222f748ad4042326d6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8679c90bfc8302de6fb6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d329637006115fbb3b48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2121d83fb49a995c59e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5ee8cd717645d3554ae4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f3772478f311565cafc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92ccbefdf49404076658">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de5f6e9ad99277522680">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c217b99c9b08561eca7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b4b847bcaf14aac33f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbf9e4d9bce762b06fce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22ec1bb77985f4c5069d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9aff43ccc7e363890fff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33bd76698aa20bd655e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1f595be449028422c46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66fcf2a326ca676cf038">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab2c3e8b5e058c06531e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f6acf68b313fb1a52c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f525c9ade0cdb0be6801">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cb29963e518a616a523">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2da18ec045e7b9828e6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20e0d921f230b18b23d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edc851c2c5954925127a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36b48d8b2d6a5ec03758">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0960f5d67cb4dcc756a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e73228688e527532cca9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bffc08d6b3e86c9086e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdada16c2bec1d73a1f3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-890d863c16f460ed280a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b10286fe9bc1ed24702f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e03f6fe4367972a9b49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-313509f2e74909566dc8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b542d09c2577ae4da250">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0a47a617e5b5c10fc62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c84485c672cc7ad89fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee8276c2dec2515bd8d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-14b5f287aeef64137dbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e836107014b20f496f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfe9ff84af077c5b181d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8b08a8baded41ac61a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8582b3300a20544ecc84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63616c8123ddbaed1f53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0518384faf865023c83c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e37377888ff2be87898">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e958c35eba65c60e2838">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e9a7f673c2c8f9a166e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b455a3932f4ada3655b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-292d5e07b551345da245">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d6dc60c1ad6e4384e59d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a71b06d1374685709e1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67e1ebdb442a6f0f1d63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afbe69eae8c7c75a3ccd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce5f39adcfd352c55f5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e574a3ae2e1bfda1a321">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae13415c211217d4dea4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e75a044bdfdd330b9fda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e4e8b76268eba35a640">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d96dff6a92d09bdb2548">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-248dbd2a6b9c490dacb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71c9f4bbb042589812fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2fbd613d629b11b25470">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-281557eccc1f5e8b1a11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7ef6ddd7b36b7ff1156">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2348d5aa3be3337451b8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20de0deb91457a7441f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9fec90152b9e8eb4a77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6c114c072d604780179">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-572c74e25839f40efd89">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10ac1adb5581470143b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b09ff6ef05f1fde5ba87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5840fb642d68a94fea5b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02eca90790cb34fb32d3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-117c29001974da1f2d40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2862ce01423ac8d3825">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8edbbfe9bfc4a201df32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4789a1716eefbbd180f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8d42a2cd65414a18311d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58d828ae0a2f32b5d950">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d41c3c22e2182f945466">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0358a3c877611bd9c7f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7206f4d09bea82636cb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75b3d329afce6e63fc82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a55ee24e09f7566f397">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-553832dd684136b021b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a229aa4fdbbe8e2f5e78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ead3dd9d9feb7d81f19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0f38c9b249f76346609">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc3d0ad7db1201159598">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab06d5f5ffd6e60d0410">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-badd86565876a40fe8f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aeaec9bcd3babe557f99">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9efa58525bff8b43888">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51063ac521bda54b89f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-099d01520f09931dbcd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f320f046fae39c0a4c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df162d033e6c03529d49">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c3a134791406386b662e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b222a6dda6e6918ab28f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-773d476f7cabfecf3980">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec7fc9e13ee7705a778b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e6c21dd157beccc107ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b426d0ae772f10701c2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5ea31ff5ff4a55bb28b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36532e4d549c86f6f9b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a693f70432bd048c579a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b84957b2aa3ca03e6dd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-670a351927c7f3d0da76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-377e89250a64eeb8f812">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-70b1715ae1379c541398">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da76252d439206b5c2da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a5282410dd55efa2609">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffcbd4bba75bedaefeb1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a019ba45b7443c73633f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69fe7255f69c60e9039e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4187dbf51bb4b37718cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c423103e0cc5f906301e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4cbf1ae2e1fd08144792">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec7537da7a281332cfbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a0dbbc2df2cea7a3a10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9ad47dc892b4c369702">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f400e0c746fe6219e612">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05fa68bc786e0ddeea64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7094b68204a26618788a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5d828efecb0b8dfe095">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45cdc8c145f615173c17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a57eade8b88b7016a375">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5a72917985591636295">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a16f45bbde141cc002e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9daabe7264d57a9e20fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-994ddb6ff937e7ab2f7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67a2656c2a0cd03c9ee9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ee782d287fd23ec7a10">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8bd6c7a14b8d5929a1d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3b2e60bd2e2d321a29f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6125fe0dd6607e0472da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59bdc95495acef3ade2a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36d37664c569038db2d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0a8e3322a9b784a914c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51b140d06789937b736d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48abc0ae2a1dc056ad6b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-22c56716f1d0ab2fa822">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25b8fa74a144275a8787">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-822d849d5ad46d346774">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6115ea1f4b39a7c17ac1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5378e79bc92aae38bef3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93201d419762b57f9d88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a08cca8723a4b06a4a8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61074bd62f33ff5b9724">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-49acb456a4ef30a2c4f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc5edd4f209ecb72dcac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d35321bea2fd74e1fb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4008034355224e811ce7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbfb321e6abba462ad72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a2aab80df6c2bf294a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-583a89985bc78a1ca14f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c02d1b5a119ac45db51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-317aa026d3b84a6c99f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a233bd957f1e0675c4db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-188df4e924c0dc83bd8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be0e603e4e94a8ed2bf9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4ae09b21ba4feada7f7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf877d52c50d5ba43a92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d88dc29f7acb48a9fd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc313fbcb3a74c8f76d3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-821dd7831fbfaccb1645">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8634a2431ae2d7d00cc1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9274a5630f724db9efc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb1c04571248acc5fee0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e649e35b1f530e6f47ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d651a6ee829eaf60ad9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c6361be9014bcbd9cff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-684f6e04c3efb103bc37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b24e81414eaa779aad65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c36b196c27b7614efeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4dda14d30d618e4bacc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e4299c86e3f8c205f15">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d55e18b1fa1e70e1beb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-669e57ae04bcade76190">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de0cbaebbbd6f0e12af0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cf455e6681a0c28c1f0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01a1d7c04707bb42ec78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50e5c7cba47700d498c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c27389bb6240dda63956">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee3dfaaaeac26bd885c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fad920843a69c051878e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b41a83e32be517b7e041">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6db5ba0b16deb89c985a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd034e541f8ba52f3259">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e89af407803775d5f6c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13e935fa2a0b705727e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bddc44a6bd675b5face">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65fdd000c119d969d1bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9894437b1ed0e090ab47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f02ffbbb5bf77146699c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b672e6da36b69cf7a77e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c197994d054a03c0bf97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-903337fe6ec2f4262ead">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dab23f79501c833d65ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebf1527efb5c8a825c09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1adb691e450a452937aa">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1b47d8de9a446ac90375"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1b47d8de9a446ac90375`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-580fd7468f509582dbbe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-580fd7468f509582dbbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47a6c5ced60f78169eef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-47a6c5ced60f78169eef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27ed3d0f61e44efb9353"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27ed3d0f61e44efb9353`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e19317eb88c3c9b9aae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e19317eb88c3c9b9aae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afc9902b769c50aa3ff5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-afc9902b769c50aa3ff5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53eb06b86597620a3dfb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-53eb06b86597620a3dfb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d29adc892e7237f6545"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d29adc892e7237f6545`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6087de923aaf5be3823"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6087de923aaf5be3823`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f787a28cc572aa3fb63"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f787a28cc572aa3fb63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1541f8172c66aa625537"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1541f8172c66aa625537`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ccb89060a3d9f1bdf7c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ccb89060a3d9f1bdf7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1d293b217f34f699af94"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1d293b217f34f699af94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-602ecf47c382982c2282"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-602ecf47c382982c2282`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6838083068899e6db5b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6838083068899e6db5b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aef1b60690b32534eb86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aef1b60690b32534eb86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-90ff5bb2e9d59752e888"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-90ff5bb2e9d59752e888`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61db688bd2d77be12028"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-61db688bd2d77be12028`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e1eb2a09265d8c74fd8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6e1eb2a09265d8c74fd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10eaf2b0083e368f1a95"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10eaf2b0083e368f1a95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e18e21820a6767425c62"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e18e21820a6767425c62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e3093f11c0f96e1deb9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e3093f11c0f96e1deb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a17f6e7db262a474b12b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a17f6e7db262a474b12b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8dd36f177746cf2c759"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e8dd36f177746cf2c759`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ceb9022d9c04387777e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ceb9022d9c04387777e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e422500e79a6f641b65a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e422500e79a6f641b65a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26fd2e363556aabd99a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-26fd2e363556aabd99a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fd894e45f154482bf3a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1fd894e45f154482bf3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3abddb3b6785ba1d5457"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3abddb3b6785ba1d5457`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d46963cefb2994549d0a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d46963cefb2994549d0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78418648c7d01a827ddc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78418648c7d01a827ddc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ce91b96a15b0a607e42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ce91b96a15b0a607e42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3049cd6ca39c33b7f6e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3049cd6ca39c33b7f6e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbf212c3c7d4882304a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cbf212c3c7d4882304a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02b4836fb7d98cf91cbb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-02b4836fb7d98cf91cbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2320da9854178cb64e85"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2320da9854178cb64e85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f754ba797f84969bad57"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f754ba797f84969bad57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08e6aa71a63e3d9e6fae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-08e6aa71a63e3d9e6fae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa00687568fe6be350e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aa00687568fe6be350e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eefa9084658f0a3a9e4f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eefa9084658f0a3a9e4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-beaac1309ddbd009e9f2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-beaac1309ddbd009e9f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b15a4ce71cdd6b5af419"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b15a4ce71cdd6b5af419`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6b54dacbae6e5e55dbd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a6b54dacbae6e5e55dbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-623663cae04e7724be14"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-623663cae04e7724be14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12e30c98f69302a54128"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12e30c98f69302a54128`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2aae65a8ab527975935"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c2aae65a8ab527975935`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91d5671fd06517f5aa43"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-91d5671fd06517f5aa43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fe9dc9d18e2a255be16"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0fe9dc9d18e2a255be16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-05f2c4aa2138dce9c28e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-05f2c4aa2138dce9c28e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-714a9b10c51c2a2bd3ed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-714a9b10c51c2a2bd3ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-328dec7be73778a02c6e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-328dec7be73778a02c6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b33a8269dbc1856edd92"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b33a8269dbc1856edd92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e0f4f033dbdcb5915cdf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e0f4f033dbdcb5915cdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36b4bdd3afce7c70990a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-36b4bdd3afce7c70990a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9a0653d86f92dfda680"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9a0653d86f92dfda680`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2103dda7e3e2569c6761"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2103dda7e3e2569c6761`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7a9b89b924ee50b2981"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7a9b89b924ee50b2981`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ffbcb6a9aec4a012c97"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ffbcb6a9aec4a012c97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5edbd459202756a3c7ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5edbd459202756a3c7ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca13b8aa56e07e3cf2c4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ca13b8aa56e07e3cf2c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c9d0955f81d8226a817"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c9d0955f81d8226a817`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b088cc26dda648428fc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b088cc26dda648428fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2abc6c030a5cd7b4617e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2abc6c030a5cd7b4617e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8e0a0ee072e0a6656d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8e0a0ee072e0a6656d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cb4d80c2d0bf944e4175"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb4d80c2d0bf944e4175`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a5f493424a8d1444957"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a5f493424a8d1444957`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fd2e44ad9de46609b89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8fd2e44ad9de46609b89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a3de178a5001384ed73"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0a3de178a5001384ed73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7f4ea71a24372d720b23"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f4ea71a24372d720b23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0af8d6de53e10a617329"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0af8d6de53e10a617329`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43884f14888c0edee4a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-43884f14888c0edee4a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffb1cd8214b29484e1a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffb1cd8214b29484e1a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d026dabdc747ecdc3f30"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d026dabdc747ecdc3f30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-508200fb5b5ef8857683"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-508200fb5b5ef8857683`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78e20a4ae3d3057ca573"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78e20a4ae3d3057ca573`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d54d757f719662b1d2b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4d54d757f719662b1d2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ec42db807cad000a383a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec42db807cad000a383a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba253204c56936f64566"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ba253204c56936f64566`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70ec6e0dd156380a7676"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-70ec6e0dd156380a7676`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64986bf5d85ca37a4439"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64986bf5d85ca37a4439`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9f9fe139944f70a85d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9f9fe139944f70a85d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-848b70045084fc2a46fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-848b70045084fc2a46fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fad6420e6ae74ece305d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fad6420e6ae74ece305d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8454fa00ea3e92033fb2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8454fa00ea3e92033fb2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-edc1bab55470d7a0a71c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-edc1bab55470d7a0a71c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b27dbf75af9ede10d44"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9b27dbf75af9ede10d44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1320369ecbf65506957a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1320369ecbf65506957a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6d95712bec88a1e3d23"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d6d95712bec88a1e3d23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a6a02fdfb9faab980a21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6a02fdfb9faab980a21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-903e93da8bda912d1d80"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-903e93da8bda912d1d80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e466fea0923aa521799"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e466fea0923aa521799`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc64b106226ca275fa75"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc64b106226ca275fa75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f481357e2bcc14133f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f481357e2bcc14133f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e04de8d257168cce3f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7e04de8d257168cce3f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc02e163c88047c7cc57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc02e163c88047c7cc57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23e72e23aa613936582f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-23e72e23aa613936582f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7d6095d6966fc47f687"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7d6095d6966fc47f687`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ad5a15126f480cfee1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9ad5a15126f480cfee1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bde6d47499f9fb0fdcc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6bde6d47499f9fb0fdcc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c1f4c4dc44e61ac53bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c1f4c4dc44e61ac53bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac84551be725eb2eca26"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac84551be725eb2eca26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dc2c98ee33baed947d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0dc2c98ee33baed947d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfdeb9acd270b61641a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bfdeb9acd270b61641a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ba2a23a722ec78c0c99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ba2a23a722ec78c0c99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-119b5fe658fe952cb707"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-119b5fe658fe952cb707`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74b465cbc2e045dde739"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74b465cbc2e045dde739`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb898bc2d69334289149"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fb898bc2d69334289149`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07f2e5399bd1ca8799b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07f2e5399bd1ca8799b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9452cbda0b546f26c335"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9452cbda0b546f26c335`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-616185ffe4042c3e246e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-616185ffe4042c3e246e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49ff1060e74f7b62893e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-49ff1060e74f7b62893e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5441d0fc61b90d915120"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5441d0fc61b90d915120`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-363cd96f9801137cf988"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-363cd96f9801137cf988`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d9933a545ba09c2203f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d9933a545ba09c2203f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-374f88cfd838907cb681"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-374f88cfd838907cb681`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a78a6d77df7393f0dfbb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a78a6d77df7393f0dfbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2dd3f91217d217850582"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2dd3f91217d217850582`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b349de25fa90a497321"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b349de25fa90a497321`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-641501463020ca4daed5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-641501463020ca4daed5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4a9e45f7e9f3379c46f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4a9e45f7e9f3379c46f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b222f748ad4042326d6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b222f748ad4042326d6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8679c90bfc8302de6fb6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8679c90bfc8302de6fb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d329637006115fbb3b48"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d329637006115fbb3b48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2121d83fb49a995c59e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2121d83fb49a995c59e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5ee8cd717645d3554ae4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5ee8cd717645d3554ae4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f3772478f311565cafc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1f3772478f311565cafc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92ccbefdf49404076658"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-92ccbefdf49404076658`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de5f6e9ad99277522680"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de5f6e9ad99277522680`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c217b99c9b08561eca7e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c217b99c9b08561eca7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b4b847bcaf14aac33f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b4b847bcaf14aac33f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbf9e4d9bce762b06fce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cbf9e4d9bce762b06fce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22ec1bb77985f4c5069d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22ec1bb77985f4c5069d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9aff43ccc7e363890fff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9aff43ccc7e363890fff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33bd76698aa20bd655e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-33bd76698aa20bd655e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1f595be449028422c46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a1f595be449028422c46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66fcf2a326ca676cf038"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-66fcf2a326ca676cf038`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab2c3e8b5e058c06531e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab2c3e8b5e058c06531e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f6acf68b313fb1a52c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8f6acf68b313fb1a52c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f525c9ade0cdb0be6801"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f525c9ade0cdb0be6801`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cb29963e518a616a523"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4cb29963e518a616a523`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2da18ec045e7b9828e6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2da18ec045e7b9828e6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20e0d921f230b18b23d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20e0d921f230b18b23d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edc851c2c5954925127a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-edc851c2c5954925127a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36b48d8b2d6a5ec03758"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36b48d8b2d6a5ec03758`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0960f5d67cb4dcc756a0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0960f5d67cb4dcc756a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e73228688e527532cca9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e73228688e527532cca9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bffc08d6b3e86c9086e3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bffc08d6b3e86c9086e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdada16c2bec1d73a1f3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fdada16c2bec1d73a1f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-890d863c16f460ed280a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-890d863c16f460ed280a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b10286fe9bc1ed24702f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b10286fe9bc1ed24702f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e03f6fe4367972a9b49"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3e03f6fe4367972a9b49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-313509f2e74909566dc8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-313509f2e74909566dc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b542d09c2577ae4da250"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b542d09c2577ae4da250`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0a47a617e5b5c10fc62"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0a47a617e5b5c10fc62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c84485c672cc7ad89fa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c84485c672cc7ad89fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee8276c2dec2515bd8d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee8276c2dec2515bd8d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-14b5f287aeef64137dbc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-14b5f287aeef64137dbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e836107014b20f496f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8e836107014b20f496f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfe9ff84af077c5b181d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cfe9ff84af077c5b181d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8b08a8baded41ac61a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d8b08a8baded41ac61a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8582b3300a20544ecc84"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8582b3300a20544ecc84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63616c8123ddbaed1f53"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63616c8123ddbaed1f53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0518384faf865023c83c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0518384faf865023c83c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e37377888ff2be87898"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e37377888ff2be87898`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e958c35eba65c60e2838"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e958c35eba65c60e2838`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e9a7f673c2c8f9a166e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e9a7f673c2c8f9a166e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b455a3932f4ada3655b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b455a3932f4ada3655b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-292d5e07b551345da245"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-292d5e07b551345da245`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d6dc60c1ad6e4384e59d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d6dc60c1ad6e4384e59d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a71b06d1374685709e1e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a71b06d1374685709e1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67e1ebdb442a6f0f1d63"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67e1ebdb442a6f0f1d63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afbe69eae8c7c75a3ccd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afbe69eae8c7c75a3ccd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce5f39adcfd352c55f5c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce5f39adcfd352c55f5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e574a3ae2e1bfda1a321"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e574a3ae2e1bfda1a321`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae13415c211217d4dea4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ae13415c211217d4dea4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e75a044bdfdd330b9fda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e75a044bdfdd330b9fda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7e4e8b76268eba35a640"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7e4e8b76268eba35a640`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d96dff6a92d09bdb2548"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d96dff6a92d09bdb2548`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-248dbd2a6b9c490dacb4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-248dbd2a6b9c490dacb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71c9f4bbb042589812fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71c9f4bbb042589812fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2fbd613d629b11b25470"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2fbd613d629b11b25470`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-281557eccc1f5e8b1a11"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-281557eccc1f5e8b1a11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7ef6ddd7b36b7ff1156"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f7ef6ddd7b36b7ff1156`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2348d5aa3be3337451b8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2348d5aa3be3337451b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20de0deb91457a7441f6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20de0deb91457a7441f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9fec90152b9e8eb4a77"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9fec90152b9e8eb4a77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6c114c072d604780179"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d6c114c072d604780179`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-572c74e25839f40efd89"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-572c74e25839f40efd89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10ac1adb5581470143b4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10ac1adb5581470143b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b09ff6ef05f1fde5ba87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b09ff6ef05f1fde5ba87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5840fb642d68a94fea5b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5840fb642d68a94fea5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02eca90790cb34fb32d3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-02eca90790cb34fb32d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-117c29001974da1f2d40"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-117c29001974da1f2d40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2862ce01423ac8d3825"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2862ce01423ac8d3825`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8edbbfe9bfc4a201df32"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8edbbfe9bfc4a201df32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4789a1716eefbbd180f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d4789a1716eefbbd180f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8d42a2cd65414a18311d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8d42a2cd65414a18311d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58d828ae0a2f32b5d950"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-58d828ae0a2f32b5d950`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d41c3c22e2182f945466"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d41c3c22e2182f945466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0358a3c877611bd9c7f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d0358a3c877611bd9c7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7206f4d09bea82636cb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7206f4d09bea82636cb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75b3d329afce6e63fc82"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-75b3d329afce6e63fc82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a55ee24e09f7566f397"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a55ee24e09f7566f397`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-553832dd684136b021b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-553832dd684136b021b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a229aa4fdbbe8e2f5e78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a229aa4fdbbe8e2f5e78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ead3dd9d9feb7d81f19"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0ead3dd9d9feb7d81f19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0f38c9b249f76346609"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0f38c9b249f76346609`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc3d0ad7db1201159598"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc3d0ad7db1201159598`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab06d5f5ffd6e60d0410"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab06d5f5ffd6e60d0410`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-badd86565876a40fe8f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-badd86565876a40fe8f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aeaec9bcd3babe557f99"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aeaec9bcd3babe557f99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9efa58525bff8b43888"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a9efa58525bff8b43888`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51063ac521bda54b89f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51063ac521bda54b89f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-099d01520f09931dbcd3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-099d01520f09931dbcd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f320f046fae39c0a4c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4f320f046fae39c0a4c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df162d033e6c03529d49"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-df162d033e6c03529d49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c3a134791406386b662e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c3a134791406386b662e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b222a6dda6e6918ab28f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b222a6dda6e6918ab28f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-773d476f7cabfecf3980"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-773d476f7cabfecf3980`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec7fc9e13ee7705a778b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec7fc9e13ee7705a778b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e6c21dd157beccc107ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e6c21dd157beccc107ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b426d0ae772f10701c2b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b426d0ae772f10701c2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5ea31ff5ff4a55bb28b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f5ea31ff5ff4a55bb28b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36532e4d549c86f6f9b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36532e4d549c86f6f9b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a693f70432bd048c579a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a693f70432bd048c579a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b84957b2aa3ca03e6dd1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b84957b2aa3ca03e6dd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-670a351927c7f3d0da76"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-670a351927c7f3d0da76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-377e89250a64eeb8f812"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-377e89250a64eeb8f812`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-70b1715ae1379c541398"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-70b1715ae1379c541398`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da76252d439206b5c2da"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-da76252d439206b5c2da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a5282410dd55efa2609"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a5282410dd55efa2609`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffcbd4bba75bedaefeb1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffcbd4bba75bedaefeb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a019ba45b7443c73633f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a019ba45b7443c73633f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69fe7255f69c60e9039e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-69fe7255f69c60e9039e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4187dbf51bb4b37718cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4187dbf51bb4b37718cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c423103e0cc5f906301e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c423103e0cc5f906301e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4cbf1ae2e1fd08144792"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4cbf1ae2e1fd08144792`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec7537da7a281332cfbb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec7537da7a281332cfbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a0dbbc2df2cea7a3a10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5a0dbbc2df2cea7a3a10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9ad47dc892b4c369702"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e9ad47dc892b4c369702`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f400e0c746fe6219e612"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f400e0c746fe6219e612`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05fa68bc786e0ddeea64"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-05fa68bc786e0ddeea64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7094b68204a26618788a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7094b68204a26618788a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5d828efecb0b8dfe095"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5d828efecb0b8dfe095`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45cdc8c145f615173c17"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45cdc8c145f615173c17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a57eade8b88b7016a375"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a57eade8b88b7016a375`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5a72917985591636295"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5a72917985591636295`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a16f45bbde141cc002e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5a16f45bbde141cc002e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9daabe7264d57a9e20fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9daabe7264d57a9e20fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-994ddb6ff937e7ab2f7c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-994ddb6ff937e7ab2f7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67a2656c2a0cd03c9ee9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67a2656c2a0cd03c9ee9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ee782d287fd23ec7a10"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0ee782d287fd23ec7a10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8bd6c7a14b8d5929a1d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8bd6c7a14b8d5929a1d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3b2e60bd2e2d321a29f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d3b2e60bd2e2d321a29f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6125fe0dd6607e0472da"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6125fe0dd6607e0472da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59bdc95495acef3ade2a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-59bdc95495acef3ade2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36d37664c569038db2d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36d37664c569038db2d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0a8e3322a9b784a914c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e0a8e3322a9b784a914c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51b140d06789937b736d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-51b140d06789937b736d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48abc0ae2a1dc056ad6b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-48abc0ae2a1dc056ad6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-22c56716f1d0ab2fa822"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-22c56716f1d0ab2fa822`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25b8fa74a144275a8787"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25b8fa74a144275a8787`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-822d849d5ad46d346774"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-822d849d5ad46d346774`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6115ea1f4b39a7c17ac1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6115ea1f4b39a7c17ac1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5378e79bc92aae38bef3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5378e79bc92aae38bef3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93201d419762b57f9d88"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-93201d419762b57f9d88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a08cca8723a4b06a4a8f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a08cca8723a4b06a4a8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61074bd62f33ff5b9724"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-61074bd62f33ff5b9724`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-49acb456a4ef30a2c4f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49acb456a4ef30a2c4f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc5edd4f209ecb72dcac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bc5edd4f209ecb72dcac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d35321bea2fd74e1fb4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3d35321bea2fd74e1fb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4008034355224e811ce7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4008034355224e811ce7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bbfb321e6abba462ad72"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bbfb321e6abba462ad72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a2aab80df6c2bf294a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a2aab80df6c2bf294a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-583a89985bc78a1ca14f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-583a89985bc78a1ca14f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c02d1b5a119ac45db51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c02d1b5a119ac45db51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-317aa026d3b84a6c99f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-317aa026d3b84a6c99f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a233bd957f1e0675c4db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a233bd957f1e0675c4db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-188df4e924c0dc83bd8b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-188df4e924c0dc83bd8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be0e603e4e94a8ed2bf9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-be0e603e4e94a8ed2bf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4ae09b21ba4feada7f7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4ae09b21ba4feada7f7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf877d52c50d5ba43a92"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bf877d52c50d5ba43a92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d88dc29f7acb48a9fd1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3d88dc29f7acb48a9fd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc313fbcb3a74c8f76d3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc313fbcb3a74c8f76d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-821dd7831fbfaccb1645"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-821dd7831fbfaccb1645`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8634a2431ae2d7d00cc1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8634a2431ae2d7d00cc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9274a5630f724db9efc7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9274a5630f724db9efc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb1c04571248acc5fee0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb1c04571248acc5fee0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e649e35b1f530e6f47ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e649e35b1f530e6f47ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d651a6ee829eaf60ad9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2d651a6ee829eaf60ad9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c6361be9014bcbd9cff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4c6361be9014bcbd9cff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-684f6e04c3efb103bc37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-684f6e04c3efb103bc37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b24e81414eaa779aad65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b24e81414eaa779aad65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c36b196c27b7614efeb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c36b196c27b7614efeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4dda14d30d618e4bacc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c4dda14d30d618e4bacc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e4299c86e3f8c205f15"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e4299c86e3f8c205f15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d55e18b1fa1e70e1beb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d55e18b1fa1e70e1beb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-669e57ae04bcade76190"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-669e57ae04bcade76190`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de0cbaebbbd6f0e12af0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de0cbaebbbd6f0e12af0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cf455e6681a0c28c1f0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8cf455e6681a0c28c1f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-01a1d7c04707bb42ec78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01a1d7c04707bb42ec78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50e5c7cba47700d498c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-50e5c7cba47700d498c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c27389bb6240dda63956"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c27389bb6240dda63956`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee3dfaaaeac26bd885c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee3dfaaaeac26bd885c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fad920843a69c051878e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fad920843a69c051878e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b41a83e32be517b7e041"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b41a83e32be517b7e041`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6db5ba0b16deb89c985a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6db5ba0b16deb89c985a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd034e541f8ba52f3259"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd034e541f8ba52f3259`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e89af407803775d5f6c4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e89af407803775d5f6c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13e935fa2a0b705727e7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-13e935fa2a0b705727e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bddc44a6bd675b5face"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0bddc44a6bd675b5face`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65fdd000c119d969d1bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-65fdd000c119d969d1bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9894437b1ed0e090ab47"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9894437b1ed0e090ab47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f02ffbbb5bf77146699c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f02ffbbb5bf77146699c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b672e6da36b69cf7a77e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b672e6da36b69cf7a77e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c197994d054a03c0bf97"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c197994d054a03c0bf97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-903337fe6ec2f4262ead"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-903337fe6ec2f4262ead`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dab23f79501c833d65ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dab23f79501c833d65ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebf1527efb5c8a825c09"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ebf1527efb5c8a825c09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1adb691e450a452937aa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1adb691e450a452937aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-slip:canonical-southeast | <a href="#case-preview_review-5c6fc8b99f5b1e38e23f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-slip:canonical-top | <a href="#case-preview_review-57f7ce273d5d5ea6fb03">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-slip:connection-overview | <a href="#case-preview_review-043636f03a9217c2fde3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-slip:canonical-southeast</summary>

<a id="case-preview_review-5c6fc8b99f5b1e38e23f"></a>

**General: unverified** — `preview_review-5c6fc8b99f5b1e38e23f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-exit-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-slip:canonical-top</summary>

<a id="case-preview_review-57f7ce273d5d5ea6fb03"></a>

**General: unverified** — `preview_review-57f7ce273d5d5ea6fb03`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-exit-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-slip:connection-overview</summary>

<a id="case-preview_review-043636f03a9217c2fde3"></a>

**General: unverified** — `preview_review-043636f03a9217c2fde3`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-exit-slip:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).
