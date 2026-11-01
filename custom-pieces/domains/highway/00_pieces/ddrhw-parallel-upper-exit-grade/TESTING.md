---
title: "Testing: RHW Ramp — L2 Exit Parallel Grade — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L2 Exit Parallel Grade — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-upper-exit-grade**, used once as **P14** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 3 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X3, Y3, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -16.970563, 10.06235]; [0.7071067811865678, 0.7071067811865273]; -0.282020177 | `path-interface-18bc8998b3c8e8765f76` |
| `channel-06-out` | road / 1 / primary | out | [-8.0, -3.2, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -3.2, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-07-out` | road / 1 / primary | out | [-8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-03-in` | road / 1 / primary | in | [-8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-04-in` | road / 1 / primary | in | [-3.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-08-out` | road / 1 / primary | out | [-3.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-05-in` | road / 1 / primary | in | [3.2, 8.0, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-09-out` | road / 1 / primary | out | [3.2, 8.0, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-10-out` | road / 1 / primary | out | [16.970563, 8.0, 0.131713]; [0.7071067811865476, 0.7071067811865476]; -0.183238121 | `path-interface-e3cc651d01db26df1e9d` |

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

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X3, Y3), (X4, Y3), (X3, Y2)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-upper-exit-grade --build dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-upper-exit-grade
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current slip-lane revision changes the highway-shoulder traffic routes and their white markings within the existing construction footprint. Read outward from a through lane toward its ramp: each lower route has an 8 m smooth sideways taper and a 4 m straight shoulder section; each upper route has a 5 m taper and a 1 m straight shoulder section. The lower routes begin 6.788225 m farther upstream in already owned native highway tiles. The upper routes retain their previous outer ports because the unchanged 31-cell layout provides less shoulder distance there. These distances are measured along the straight highway axis. On-ramps follow the same profiles in reverse. The auxiliary-lane centre is 5.5 m from the highway axis; the checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot on the straight section. These are compressed experimental dimensions, not a real-road design standard. Native through PATHs, roadway outside the native 8 m deck edge, grades, ground terminals, permanent identifiers, and construction ownership retain their previous scope. Check the matching saved report before treating this source revision as verified. This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

The earlier narrow ground mouths are retained: each terminal keeps its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after that 3 m ground taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the ground taper is still narrowing; this is the actual driveway crossing.

## 4. Game checks

1. Select this exact component through the assembly button, match P14 at **X3, Y3**, and confirm that the occupied preview squares match **(X3, Y3), (X4, Y3), (X3, Y2)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-upper-exit-grade** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. This is a fixed-height transition, not a straight slope that can be repeated to obtain any chosen height. Its visible grade model overhangs neighbouring departure and terminal tiles. Its whole-cell traffic ownership also includes one native highway half, so the model and traffic boundaries differ. The native through PATHs and outside-deck ramp route remain with those owned cells. The visible native highway half and its centre pier instead belong to the adjacent straight slip-lane model through overhang, leaving this component’s physical model as a pure graded ramp. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

Adaptive pavement is implemented through native texture variants and correctly rotating model props, rather than a fixed sidewalk slab. Its visible appearance depends on the native development rules, and a sidewalk replacement mod needs its own compatibility check. The approximately 1.149 m clearance applies where the terminal asphalt and retained pedestrian centreline run beside one another; the actual driveway crossings are deliberately excluded. A measured route clearance does not establish visible walking, a continuous pavement strip, or a particular pedestrian-versus-car priority in the game.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-upper-exit-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-upper-exit-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-79012443a3bbc8d4eb57">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-79012443a3bbc8d4eb57"></a>

**General: unverified** — `software_resources-79012443a3bbc8d4eb57`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-79012443a3bbc8d4eb57">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-79012443a3bbc8d4eb57"></a>

**General: unverified** — `software_connectivity-79012443a3bbc8d4eb57`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-exit-grade:canonical-southeast | <a href="#case-preview_review-e41422cf7c62bd7bdc4c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-exit-grade:canonical-top | <a href="#case-preview_review-1ff3943b2913fab8cac6">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-exit-grade:connection-overview | <a href="#case-preview_review-fed33c6076ab36d66c7c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-exit-grade:canonical-southeast</summary>

<a id="case-preview_review-e41422cf7c62bd7bdc4c"></a>

**General: unverified** — `preview_review-e41422cf7c62bd7bdc4c`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-exit-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-exit-grade:canonical-top</summary>

<a id="case-preview_review-1ff3943b2913fab8cac6"></a>

**General: unverified** — `preview_review-1ff3943b2913fab8cac6`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-exit-grade:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-exit-grade:connection-overview</summary>

<a id="case-preview_review-fed33c6076ab36d66c7c"></a>

**General: unverified** — `preview_review-fed33c6076ab36d66c7c`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-exit-grade:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-0336998525a8d477398d">[ ] unverified</a> | <a href="#case-in_game_render-9e3b1071fb7e03f5097a">[ ] unverified</a> | <a href="#case-in_game_render-6dc4970c34d54928db6d">[ ] unverified</a> | <a href="#case-in_game_render-80d3c577e4eaba9034fc">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-0336998525a8d477398d"></a>

**0° CCW: unverified** — `in_game_render-0336998525a8d477398d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9e3b1071fb7e03f5097a"></a>

**90° CCW: unverified** — `in_game_render-9e3b1071fb7e03f5097a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-6dc4970c34d54928db6d"></a>

**180° CCW: unverified** — `in_game_render-6dc4970c34d54928db6d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-80d3c577e4eaba9034fc"></a>

**270° CCW: unverified** — `in_game_render-80d3c577e4eaba9034fc`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-0336998525a8d477398d">[ ] unverified</a> | <a href="#case-in_game_placement-9e3b1071fb7e03f5097a">[ ] unverified</a> | <a href="#case-in_game_placement-6dc4970c34d54928db6d">[ ] unverified</a> | <a href="#case-in_game_placement-80d3c577e4eaba9034fc">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-0336998525a8d477398d"></a>

**0° CCW: unverified** — `in_game_placement-0336998525a8d477398d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9e3b1071fb7e03f5097a"></a>

**90° CCW: unverified** — `in_game_placement-9e3b1071fb7e03f5097a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-6dc4970c34d54928db6d"></a>

**180° CCW: unverified** — `in_game_placement-6dc4970c34d54928db6d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-80d3c577e4eaba9034fc"></a>

**270° CCW: unverified** — `in_game_placement-80d3c577e4eaba9034fc`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-0336998525a8d477398d">[ ] unverified</a> | <a href="#case-in_game_demolition-9e3b1071fb7e03f5097a">[ ] unverified</a> | <a href="#case-in_game_demolition-6dc4970c34d54928db6d">[ ] unverified</a> | <a href="#case-in_game_demolition-80d3c577e4eaba9034fc">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-0336998525a8d477398d"></a>

**0° CCW: unverified** — `in_game_demolition-0336998525a8d477398d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9e3b1071fb7e03f5097a"></a>

**90° CCW: unverified** — `in_game_demolition-9e3b1071fb7e03f5097a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-6dc4970c34d54928db6d"></a>

**180° CCW: unverified** — `in_game_demolition-6dc4970c34d54928db6d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-80d3c577e4eaba9034fc"></a>

**270° CCW: unverified** — `in_game_demolition-80d3c577e4eaba9034fc`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-0336998525a8d477398d">[ ] unverified</a> | <a href="#case-in_game_save_reload-9e3b1071fb7e03f5097a">[ ] unverified</a> | <a href="#case-in_game_save_reload-6dc4970c34d54928db6d">[ ] unverified</a> | <a href="#case-in_game_save_reload-80d3c577e4eaba9034fc">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-0336998525a8d477398d"></a>

**0° CCW: unverified** — `in_game_save_reload-0336998525a8d477398d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9e3b1071fb7e03f5097a"></a>

**90° CCW: unverified** — `in_game_save_reload-9e3b1071fb7e03f5097a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-6dc4970c34d54928db6d"></a>

**180° CCW: unverified** — `in_game_save_reload-6dc4970c34d54928db6d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-80d3c577e4eaba9034fc"></a>

**270° CCW: unverified** — `in_game_save_reload-80d3c577e4eaba9034fc`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-232fe54cc3f3474601f2">[ ] unverified</a> | <a href="#case-in_game_route_query-345d0a71ec7bf00189fa">[ ] unverified</a> | <a href="#case-in_game_route_query-fb2e778a491cac530b24">[ ] unverified</a> | <a href="#case-in_game_route_query-0666165e3fbc20077abb">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-1c1ae1e3f9a94ec021e0">[ ] unverified</a> | <a href="#case-in_game_route_query-a1b28374053462bfefcf">[ ] unverified</a> | <a href="#case-in_game_route_query-be3583a823d977695431">[ ] unverified</a> | <a href="#case-in_game_route_query-518774c6a8293d6891e3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-23d999f4bad43fe92088">[ ] unverified</a> | <a href="#case-in_game_route_query-f322b894e1695a7eb890">[ ] unverified</a> | <a href="#case-in_game_route_query-330166c248703eb11fec">[ ] unverified</a> | <a href="#case-in_game_route_query-3478218ab4f5c40d452a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-535903121452f6f091db">[ ] unverified</a> | <a href="#case-in_game_route_query-0e0ac9ddca55f8749004">[ ] unverified</a> | <a href="#case-in_game_route_query-26aa779e3f9a20fbc68a">[ ] unverified</a> | <a href="#case-in_game_route_query-a479038666127a15e39a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-fe525a2dfe6d1a3d8135">[ ] unverified</a> | <a href="#case-in_game_route_query-d0cc3ddeba7733acebc0">[ ] unverified</a> | <a href="#case-in_game_route_query-e5f9fab2211d80cf7f34">[ ] unverified</a> | <a href="#case-in_game_route_query-5b27b8128430ee66e77f">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-232fe54cc3f3474601f2"></a>

**0° CCW: unverified** — `in_game_route_query-232fe54cc3f3474601f2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-345d0a71ec7bf00189fa"></a>

**90° CCW: unverified** — `in_game_route_query-345d0a71ec7bf00189fa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-fb2e778a491cac530b24"></a>

**180° CCW: unverified** — `in_game_route_query-fb2e778a491cac530b24`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-0666165e3fbc20077abb"></a>

**270° CCW: unverified** — `in_game_route_query-0666165e3fbc20077abb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-1c1ae1e3f9a94ec021e0"></a>

**0° CCW: unverified** — `in_game_route_query-1c1ae1e3f9a94ec021e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-a1b28374053462bfefcf"></a>

**90° CCW: unverified** — `in_game_route_query-a1b28374053462bfefcf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-be3583a823d977695431"></a>

**180° CCW: unverified** — `in_game_route_query-be3583a823d977695431`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-518774c6a8293d6891e3"></a>

**270° CCW: unverified** — `in_game_route_query-518774c6a8293d6891e3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-23d999f4bad43fe92088"></a>

**0° CCW: unverified** — `in_game_route_query-23d999f4bad43fe92088`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-f322b894e1695a7eb890"></a>

**90° CCW: unverified** — `in_game_route_query-f322b894e1695a7eb890`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-330166c248703eb11fec"></a>

**180° CCW: unverified** — `in_game_route_query-330166c248703eb11fec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-3478218ab4f5c40d452a"></a>

**270° CCW: unverified** — `in_game_route_query-3478218ab4f5c40d452a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-535903121452f6f091db"></a>

**0° CCW: unverified** — `in_game_route_query-535903121452f6f091db`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-0e0ac9ddca55f8749004"></a>

**90° CCW: unverified** — `in_game_route_query-0e0ac9ddca55f8749004`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-26aa779e3f9a20fbc68a"></a>

**180° CCW: unverified** — `in_game_route_query-26aa779e3f9a20fbc68a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-a479038666127a15e39a"></a>

**270° CCW: unverified** — `in_game_route_query-a479038666127a15e39a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-fe525a2dfe6d1a3d8135"></a>

**0° CCW: unverified** — `in_game_route_query-fe525a2dfe6d1a3d8135`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-d0cc3ddeba7733acebc0"></a>

**90° CCW: unverified** — `in_game_route_query-d0cc3ddeba7733acebc0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-e5f9fab2211d80cf7f34"></a>

**180° CCW: unverified** — `in_game_route_query-e5f9fab2211d80cf7f34`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-5b27b8128430ee66e77f"></a>

**270° CCW: unverified** — `in_game_route_query-5b27b8128430ee66e77f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-232fe54cc3f3474601f2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-345d0a71ec7bf00189fa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fb2e778a491cac530b24">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0666165e3fbc20077abb">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-1c1ae1e3f9a94ec021e0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a1b28374053462bfefcf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be3583a823d977695431">[ ] unverified</a> | <a href="#case-in_game_visible_travel-518774c6a8293d6891e3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-23d999f4bad43fe92088">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f322b894e1695a7eb890">[ ] unverified</a> | <a href="#case-in_game_visible_travel-330166c248703eb11fec">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3478218ab4f5c40d452a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-535903121452f6f091db">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0e0ac9ddca55f8749004">[ ] unverified</a> | <a href="#case-in_game_visible_travel-26aa779e3f9a20fbc68a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a479038666127a15e39a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-fe525a2dfe6d1a3d8135">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d0cc3ddeba7733acebc0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e5f9fab2211d80cf7f34">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5b27b8128430ee66e77f">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-232fe54cc3f3474601f2"></a>

**0° CCW: unverified** — `in_game_visible_travel-232fe54cc3f3474601f2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-345d0a71ec7bf00189fa"></a>

**90° CCW: unverified** — `in_game_visible_travel-345d0a71ec7bf00189fa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-fb2e778a491cac530b24"></a>

**180° CCW: unverified** — `in_game_visible_travel-fb2e778a491cac530b24`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-0666165e3fbc20077abb"></a>

**270° CCW: unverified** — `in_game_visible_travel-0666165e3fbc20077abb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-1c1ae1e3f9a94ec021e0"></a>

**0° CCW: unverified** — `in_game_visible_travel-1c1ae1e3f9a94ec021e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-a1b28374053462bfefcf"></a>

**90° CCW: unverified** — `in_game_visible_travel-a1b28374053462bfefcf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-be3583a823d977695431"></a>

**180° CCW: unverified** — `in_game_visible_travel-be3583a823d977695431`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-518774c6a8293d6891e3"></a>

**270° CCW: unverified** — `in_game_visible_travel-518774c6a8293d6891e3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-23d999f4bad43fe92088"></a>

**0° CCW: unverified** — `in_game_visible_travel-23d999f4bad43fe92088`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-f322b894e1695a7eb890"></a>

**90° CCW: unverified** — `in_game_visible_travel-f322b894e1695a7eb890`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-330166c248703eb11fec"></a>

**180° CCW: unverified** — `in_game_visible_travel-330166c248703eb11fec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-3478218ab4f5c40d452a"></a>

**270° CCW: unverified** — `in_game_visible_travel-3478218ab4f5c40d452a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-535903121452f6f091db"></a>

**0° CCW: unverified** — `in_game_visible_travel-535903121452f6f091db`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-0e0ac9ddca55f8749004"></a>

**90° CCW: unverified** — `in_game_visible_travel-0e0ac9ddca55f8749004`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-26aa779e3f9a20fbc68a"></a>

**180° CCW: unverified** — `in_game_visible_travel-26aa779e3f9a20fbc68a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-a479038666127a15e39a"></a>

**270° CCW: unverified** — `in_game_visible_travel-a479038666127a15e39a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-fe525a2dfe6d1a3d8135"></a>

**0° CCW: unverified** — `in_game_visible_travel-fe525a2dfe6d1a3d8135`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-d0cc3ddeba7733acebc0"></a>

**90° CCW: unverified** — `in_game_visible_travel-d0cc3ddeba7733acebc0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-e5f9fab2211d80cf7f34"></a>

**180° CCW: unverified** — `in_game_visible_travel-e5f9fab2211d80cf7f34`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-5b27b8128430ee66e77f"></a>

**270° CCW: unverified** — `in_game_visible_travel-5b27b8128430ee66e77f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-06bc1e8fe6d0d9e68964">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d3651620ce43552f017">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e51db4dd1b85ed4866d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03549863bb8d9af4d559">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac5c2903ada82abe05c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e84ef483f3d4f389cbde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8133eb4da8013268d483">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bd582cde72026453938">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f70411370829ae1835b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-906b6e1af1b02f74bceb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21b85aa3329503baf9a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77d605b4721c8be3808b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-42f0ddc8b74b0b57a86b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3f7be9c202bad7786b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3bbb0358acda45da746a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b94aabb100a7bfac52cf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cbbf9f25aa4757b208d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30963b90b095fbc398d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a12c341a510902b7d339">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ef5d655f044910efcb4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8432590a80ec35fef389">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4ea92568c44fbe5eaca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9090b3818d01e082e906">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eac840f235197dae867d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4268d33b687d934bef4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d81573a004539fedef45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a03298e539f60b1b2f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1a4f1658fcd0d446af5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f086f701d2e58cd29312">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-227d81bdf9b5fc6e050a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b91fb12f62e095d6ece6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d3ad2f7bdc05756bd2b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce395ba727bb842462f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b184ff13f4ec42825657">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24001211c8ba9a3ad677">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25bf3c8bb17749d30006">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a92fe59a9dd60f0af439">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f0eb9a768fe0be1b4f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be6c72defdb286f30447">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b9ed78e6e570d2f5011">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32d9aececb48f09c4777">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21293024e6522b4541ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f27995d321dc052a6b64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-affda2e2b84f16af560e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f576fc9e422b73f067b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0ab4c51549b9ed25143">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f985749bce962293fd3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92370e9fd7b4dd722c32">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-19542bc27f0195183f7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cda313975d71e573a483">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdec5c548c61224bb1a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba3ae5a45db849539094">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-21897fe29d869c3434b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53c759127483c5a31f91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5f2bf50b6a0c370d979">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f31f8636f7c16f9d839">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1dca6e87a52aa88003dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd268089b0f8cbff3b6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ff4886779159db35a35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97c24f8d5876ae8817ec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-21514df48349928528db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f91b0d242a87e9f3a3e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fd80599f263d765b4c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68b884f5db2b6d3e5a8e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b1fe012b07a68b84e7f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46b73b070e848f84b74d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03491f1889926774873c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04251ad1ed71b2e9332c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e31d741395452c6faa6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23de5367474ca8f594af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-785e3e2df97595413543">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c9be1b224744c4abeb8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41d46cf661c67e793183">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3bb32aa489b667bb07c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0363fc88ecd4cadb7b2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f01efda8a8486faa0aea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-098e6163cb2b2ce0bdb1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07d321df9510b02a52e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d2ed8bfa4d59eac540a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e25e04e39d07b478331e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-06bc1e8fe6d0d9e68964"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-06bc1e8fe6d0d9e68964`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d3651620ce43552f017"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6d3651620ce43552f017`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e51db4dd1b85ed4866d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e51db4dd1b85ed4866d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03549863bb8d9af4d559"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03549863bb8d9af4d559`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac5c2903ada82abe05c5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac5c2903ada82abe05c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e84ef483f3d4f389cbde"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e84ef483f3d4f389cbde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8133eb4da8013268d483"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8133eb4da8013268d483`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bd582cde72026453938"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9bd582cde72026453938`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f70411370829ae1835b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f70411370829ae1835b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-906b6e1af1b02f74bceb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-906b6e1af1b02f74bceb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21b85aa3329503baf9a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-21b85aa3329503baf9a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77d605b4721c8be3808b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77d605b4721c8be3808b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-42f0ddc8b74b0b57a86b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-42f0ddc8b74b0b57a86b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3f7be9c202bad7786b2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d3f7be9c202bad7786b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3bbb0358acda45da746a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3bbb0358acda45da746a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b94aabb100a7bfac52cf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b94aabb100a7bfac52cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cbbf9f25aa4757b208d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cbbf9f25aa4757b208d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30963b90b095fbc398d9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-30963b90b095fbc398d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a12c341a510902b7d339"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a12c341a510902b7d339`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ef5d655f044910efcb4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ef5d655f044910efcb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8432590a80ec35fef389"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8432590a80ec35fef389`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4ea92568c44fbe5eaca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d4ea92568c44fbe5eaca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9090b3818d01e082e906"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9090b3818d01e082e906`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eac840f235197dae867d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eac840f235197dae867d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4268d33b687d934bef4b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4268d33b687d934bef4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d81573a004539fedef45"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d81573a004539fedef45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a03298e539f60b1b2f5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6a03298e539f60b1b2f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1a4f1658fcd0d446af5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a1a4f1658fcd0d446af5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f086f701d2e58cd29312"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f086f701d2e58cd29312`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-227d81bdf9b5fc6e050a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-227d81bdf9b5fc6e050a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b91fb12f62e095d6ece6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b91fb12f62e095d6ece6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d3ad2f7bdc05756bd2b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7d3ad2f7bdc05756bd2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce395ba727bb842462f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce395ba727bb842462f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b184ff13f4ec42825657"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b184ff13f4ec42825657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24001211c8ba9a3ad677"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-24001211c8ba9a3ad677`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25bf3c8bb17749d30006"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-25bf3c8bb17749d30006`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a92fe59a9dd60f0af439"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a92fe59a9dd60f0af439`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f0eb9a768fe0be1b4f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1f0eb9a768fe0be1b4f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be6c72defdb286f30447"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be6c72defdb286f30447`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b9ed78e6e570d2f5011"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b9ed78e6e570d2f5011`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32d9aececb48f09c4777"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32d9aececb48f09c4777`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21293024e6522b4541ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-21293024e6522b4541ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f27995d321dc052a6b64"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f27995d321dc052a6b64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-affda2e2b84f16af560e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-affda2e2b84f16af560e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f576fc9e422b73f067b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f576fc9e422b73f067b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0ab4c51549b9ed25143"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0ab4c51549b9ed25143`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f985749bce962293fd3f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f985749bce962293fd3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92370e9fd7b4dd722c32"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92370e9fd7b4dd722c32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-19542bc27f0195183f7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-19542bc27f0195183f7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cda313975d71e573a483"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cda313975d71e573a483`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdec5c548c61224bb1a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cdec5c548c61224bb1a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba3ae5a45db849539094"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ba3ae5a45db849539094`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-21897fe29d869c3434b5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-21897fe29d869c3434b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53c759127483c5a31f91"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-53c759127483c5a31f91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5f2bf50b6a0c370d979"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b5f2bf50b6a0c370d979`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f31f8636f7c16f9d839"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0f31f8636f7c16f9d839`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1dca6e87a52aa88003dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1dca6e87a52aa88003dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd268089b0f8cbff3b6b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cd268089b0f8cbff3b6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ff4886779159db35a35"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ff4886779159db35a35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97c24f8d5876ae8817ec"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-97c24f8d5876ae8817ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-21514df48349928528db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-21514df48349928528db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f91b0d242a87e9f3a3e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f91b0d242a87e9f3a3e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fd80599f263d765b4c0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5fd80599f263d765b4c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68b884f5db2b6d3e5a8e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68b884f5db2b6d3e5a8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b1fe012b07a68b84e7f6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1fe012b07a68b84e7f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46b73b070e848f84b74d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-46b73b070e848f84b74d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03491f1889926774873c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03491f1889926774873c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04251ad1ed71b2e9332c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-04251ad1ed71b2e9332c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e31d741395452c6faa6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e31d741395452c6faa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23de5367474ca8f594af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23de5367474ca8f594af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-785e3e2df97595413543"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-785e3e2df97595413543`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c9be1b224744c4abeb8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c9be1b224744c4abeb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41d46cf661c67e793183"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41d46cf661c67e793183`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3bb32aa489b667bb07c0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3bb32aa489b667bb07c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0363fc88ecd4cadb7b2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0363fc88ecd4cadb7b2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f01efda8a8486faa0aea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f01efda8a8486faa0aea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-098e6163cb2b2ce0bdb1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-098e6163cb2b2ce0bdb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07d321df9510b02a52e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-07d321df9510b02a52e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d2ed8bfa4d59eac540a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0d2ed8bfa4d59eac540a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e25e04e39d07b478331e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e25e04e39d07b478331e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrowed terminal asphalt while preserving the 6 m grade interfaces and its saved traffic routes. The later slip-lane revision lengthens the shoulder treatment and changes its access PATHs and white markings, while retaining all fifteen permanent types, the 31-cell union, and those narrow ground mouths. The earlier `ddrhw-parallel-diamond-parts-01` and `ddrhw-parallel-diamond-pedestrian-mouths-01` build identities retain their original scopes. The current revision uses `ddrhw-parallel-diamond-slip-lanes-02`; only its own matching saved-resource report can establish its software result.
