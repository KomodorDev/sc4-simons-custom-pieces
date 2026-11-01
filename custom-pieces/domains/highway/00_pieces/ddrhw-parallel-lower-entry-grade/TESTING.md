---
title: "Testing: RHW Ramp — L1 Entry Parallel Grade — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L1 Entry Parallel Grade — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

The current policy is **no cast shadow from this component**. Verify that appearance on a fresh placement after restarting with the checked no-shadow revision; older saved-attachment cleanup is a separate pending observation. The assembly’s [current no-shadow test](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#44-independent-module-shadow-test) owns the detailed camera, quality, zoom, and lifecycle procedure.

This record covers **ddrhw-parallel-lower-entry-grade**, used once as **P13** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 2 occupied tiles in a 2 × 1 rectangle, the exact authored 0° reference at X2, Y4, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-06-out` | road / 1 / primary | out | [-0.970563, -8.0, 4.364109]; [-0.7071067811865476, -0.7071067811865476]; 0.179117565 | `path-interface-58833f9593752a9d0c32` |
| `channel-07-out` | road / 1 / primary | out | [12.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [12.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-02-in` | road / 1 / primary | in | [15.029437, 8.0, 0.311171]; [-0.7071067811865305, -0.7071067811865647]; 0.179120116 | `path-interface-c97e67b221c113d321e9` |
| `channel-08-out` | road / 1 / primary | out | [19.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-03-in` | road / 1 / primary | in | [19.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-04-in` | road / 1 / primary | in | [24.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-09-out` | road / 1 / primary | out | [24.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-05-in` | road / 1 / primary | in | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-10-out` | road / 1 / primary | out | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-10-out` | primary |
| road | `channel-02-in` → `channel-06-out` | primary |
| road | `channel-03-in` → `channel-09-out` | primary |
| road | `channel-04-in` → `channel-08-out` | primary |
| road | `channel-05-in` → `channel-07-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X2, Y4), (X3, Y4)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-lower-entry-grade --build dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-lower-entry-grade
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current slip-lane revision changes the highway-shoulder traffic routes and their white markings within the existing construction footprint. Read outward from a through lane toward its ramp: each lower route has an 8 m smooth sideways taper and a 4 m straight shoulder section; each upper route has a 5 m taper and a 1 m straight shoulder section. The lower routes begin 6.788225 m farther upstream in already owned native highway tiles. The upper routes retain their previous outer ports because the unchanged 31-cell layout provides less shoulder distance there. These distances are measured along the straight highway axis. On-ramps follow the same profiles in reverse. The auxiliary-lane centre is 5.5 m from the highway axis; the checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot on the straight section. These are compressed experimental dimensions, not a real-road design standard. Native through PATHs, roadway outside the native 8 m deck edge, grades, ground terminals, permanent identifiers, and construction ownership retain their previous scope. Check the matching saved report before treating this source revision as verified. This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

The earlier narrow ground mouths are retained: each terminal keeps its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after that 3 m ground taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the ground taper is still narrowing; this is the actual driveway crossing.

## 4. Game checks

1. Select this exact component through the assembly button, match P13 at **X2, Y4**, and confirm that the occupied preview squares match **(X2, Y4), (X3, Y4)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect for unwanted cast shadows at Medium and High quality; this component intentionally supplies none. Demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle or old shadow attachment remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-lower-entry-grade** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-entry-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-entry-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-1c565b761ac92812f117">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-1c565b761ac92812f117"></a>

**General: unverified** — `software_resources-1c565b761ac92812f117`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-1c565b761ac92812f117">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-1c565b761ac92812f117"></a>

**General: unverified** — `software_connectivity-1c565b761ac92812f117`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-entry-grade:canonical-southeast | <a href="#case-preview_review-ca075894addf07593fa2">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-entry-grade:canonical-top | <a href="#case-preview_review-449a6a9b42c27fc0d273">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-entry-grade:connection-overview | <a href="#case-preview_review-a588cee2c4faa9bec2b4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-entry-grade:canonical-southeast</summary>

<a id="case-preview_review-ca075894addf07593fa2"></a>

**General: unverified** — `preview_review-ca075894addf07593fa2`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-entry-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-entry-grade:canonical-top</summary>

<a id="case-preview_review-449a6a9b42c27fc0d273"></a>

**General: unverified** — `preview_review-449a6a9b42c27fc0d273`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-entry-grade:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-entry-grade:connection-overview</summary>

<a id="case-preview_review-a588cee2c4faa9bec2b4"></a>

**General: unverified** — `preview_review-a588cee2c4faa9bec2b4`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-entry-grade:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-73298d60b51d673cf7de">[ ] unverified</a> | <a href="#case-in_game_render-df2ff6ec8954bed8066d">[ ] unverified</a> | <a href="#case-in_game_render-8101b918b3de522fbfa2">[ ] unverified</a> | <a href="#case-in_game_render-11752f003bdd401522e2">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-73298d60b51d673cf7de"></a>

**0° CCW: unverified** — `in_game_render-73298d60b51d673cf7de`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-df2ff6ec8954bed8066d"></a>

**90° CCW: unverified** — `in_game_render-df2ff6ec8954bed8066d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8101b918b3de522fbfa2"></a>

**180° CCW: unverified** — `in_game_render-8101b918b3de522fbfa2`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-11752f003bdd401522e2"></a>

**270° CCW: unverified** — `in_game_render-11752f003bdd401522e2`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-73298d60b51d673cf7de">[ ] unverified</a> | <a href="#case-in_game_placement-df2ff6ec8954bed8066d">[ ] unverified</a> | <a href="#case-in_game_placement-8101b918b3de522fbfa2">[ ] unverified</a> | <a href="#case-in_game_placement-11752f003bdd401522e2">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-73298d60b51d673cf7de"></a>

**0° CCW: unverified** — `in_game_placement-73298d60b51d673cf7de`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-df2ff6ec8954bed8066d"></a>

**90° CCW: unverified** — `in_game_placement-df2ff6ec8954bed8066d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8101b918b3de522fbfa2"></a>

**180° CCW: unverified** — `in_game_placement-8101b918b3de522fbfa2`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-11752f003bdd401522e2"></a>

**270° CCW: unverified** — `in_game_placement-11752f003bdd401522e2`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-73298d60b51d673cf7de">[ ] unverified</a> | <a href="#case-in_game_demolition-df2ff6ec8954bed8066d">[ ] unverified</a> | <a href="#case-in_game_demolition-8101b918b3de522fbfa2">[ ] unverified</a> | <a href="#case-in_game_demolition-11752f003bdd401522e2">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-73298d60b51d673cf7de"></a>

**0° CCW: unverified** — `in_game_demolition-73298d60b51d673cf7de`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-df2ff6ec8954bed8066d"></a>

**90° CCW: unverified** — `in_game_demolition-df2ff6ec8954bed8066d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8101b918b3de522fbfa2"></a>

**180° CCW: unverified** — `in_game_demolition-8101b918b3de522fbfa2`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-11752f003bdd401522e2"></a>

**270° CCW: unverified** — `in_game_demolition-11752f003bdd401522e2`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-73298d60b51d673cf7de">[ ] unverified</a> | <a href="#case-in_game_save_reload-df2ff6ec8954bed8066d">[ ] unverified</a> | <a href="#case-in_game_save_reload-8101b918b3de522fbfa2">[ ] unverified</a> | <a href="#case-in_game_save_reload-11752f003bdd401522e2">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-73298d60b51d673cf7de"></a>

**0° CCW: unverified** — `in_game_save_reload-73298d60b51d673cf7de`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-df2ff6ec8954bed8066d"></a>

**90° CCW: unverified** — `in_game_save_reload-df2ff6ec8954bed8066d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8101b918b3de522fbfa2"></a>

**180° CCW: unverified** — `in_game_save_reload-8101b918b3de522fbfa2`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-11752f003bdd401522e2"></a>

**270° CCW: unverified** — `in_game_save_reload-11752f003bdd401522e2`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-ace3e59dbb8237483938">[ ] unverified</a> | <a href="#case-in_game_route_query-77c92ac4c64213d8b124">[ ] unverified</a> | <a href="#case-in_game_route_query-421d46715a9f1a3f77a3">[ ] unverified</a> | <a href="#case-in_game_route_query-8a625b9d27181df0919d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-44024dd261e654216c31">[ ] unverified</a> | <a href="#case-in_game_route_query-310a57095c56095d048b">[ ] unverified</a> | <a href="#case-in_game_route_query-267a7d2f43b6737f365f">[ ] unverified</a> | <a href="#case-in_game_route_query-5d947a4f5f3b643fdea0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-739a4336d40735397629">[ ] unverified</a> | <a href="#case-in_game_route_query-0e77ac2cc1f0f11c9104">[ ] unverified</a> | <a href="#case-in_game_route_query-a2fab3b289f2cedd5aa5">[ ] unverified</a> | <a href="#case-in_game_route_query-ff01ee387aba0852b6a6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-06b96dcde2c053b52509">[ ] unverified</a> | <a href="#case-in_game_route_query-44c136e53eb0cf361d62">[ ] unverified</a> | <a href="#case-in_game_route_query-06f9e206f74084da8fae">[ ] unverified</a> | <a href="#case-in_game_route_query-5574e45064ffbcade437">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-e746ce8e25ac9ddef8b9">[ ] unverified</a> | <a href="#case-in_game_route_query-1e170fd3cfa1a8317dc9">[ ] unverified</a> | <a href="#case-in_game_route_query-4e613fb025821d0f786a">[ ] unverified</a> | <a href="#case-in_game_route_query-e5aca8b6ab2e409ad677">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-ace3e59dbb8237483938"></a>

**0° CCW: unverified** — `in_game_route_query-ace3e59dbb8237483938`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-77c92ac4c64213d8b124"></a>

**90° CCW: unverified** — `in_game_route_query-77c92ac4c64213d8b124`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-421d46715a9f1a3f77a3"></a>

**180° CCW: unverified** — `in_game_route_query-421d46715a9f1a3f77a3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-8a625b9d27181df0919d"></a>

**270° CCW: unverified** — `in_game_route_query-8a625b9d27181df0919d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-44024dd261e654216c31"></a>

**0° CCW: unverified** — `in_game_route_query-44024dd261e654216c31`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-310a57095c56095d048b"></a>

**90° CCW: unverified** — `in_game_route_query-310a57095c56095d048b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-267a7d2f43b6737f365f"></a>

**180° CCW: unverified** — `in_game_route_query-267a7d2f43b6737f365f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-5d947a4f5f3b643fdea0"></a>

**270° CCW: unverified** — `in_game_route_query-5d947a4f5f3b643fdea0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-739a4336d40735397629"></a>

**0° CCW: unverified** — `in_game_route_query-739a4336d40735397629`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-0e77ac2cc1f0f11c9104"></a>

**90° CCW: unverified** — `in_game_route_query-0e77ac2cc1f0f11c9104`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-a2fab3b289f2cedd5aa5"></a>

**180° CCW: unverified** — `in_game_route_query-a2fab3b289f2cedd5aa5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-ff01ee387aba0852b6a6"></a>

**270° CCW: unverified** — `in_game_route_query-ff01ee387aba0852b6a6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-06b96dcde2c053b52509"></a>

**0° CCW: unverified** — `in_game_route_query-06b96dcde2c053b52509`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-44c136e53eb0cf361d62"></a>

**90° CCW: unverified** — `in_game_route_query-44c136e53eb0cf361d62`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-06f9e206f74084da8fae"></a>

**180° CCW: unverified** — `in_game_route_query-06f9e206f74084da8fae`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-5574e45064ffbcade437"></a>

**270° CCW: unverified** — `in_game_route_query-5574e45064ffbcade437`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-e746ce8e25ac9ddef8b9"></a>

**0° CCW: unverified** — `in_game_route_query-e746ce8e25ac9ddef8b9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-1e170fd3cfa1a8317dc9"></a>

**90° CCW: unverified** — `in_game_route_query-1e170fd3cfa1a8317dc9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-4e613fb025821d0f786a"></a>

**180° CCW: unverified** — `in_game_route_query-4e613fb025821d0f786a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-e5aca8b6ab2e409ad677"></a>

**270° CCW: unverified** — `in_game_route_query-e5aca8b6ab2e409ad677`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-ace3e59dbb8237483938">[ ] unverified</a> | <a href="#case-in_game_visible_travel-77c92ac4c64213d8b124">[ ] unverified</a> | <a href="#case-in_game_visible_travel-421d46715a9f1a3f77a3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8a625b9d27181df0919d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-44024dd261e654216c31">[ ] unverified</a> | <a href="#case-in_game_visible_travel-310a57095c56095d048b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-267a7d2f43b6737f365f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5d947a4f5f3b643fdea0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-739a4336d40735397629">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0e77ac2cc1f0f11c9104">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a2fab3b289f2cedd5aa5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff01ee387aba0852b6a6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-06b96dcde2c053b52509">[ ] unverified</a> | <a href="#case-in_game_visible_travel-44c136e53eb0cf361d62">[ ] unverified</a> | <a href="#case-in_game_visible_travel-06f9e206f74084da8fae">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5574e45064ffbcade437">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-e746ce8e25ac9ddef8b9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1e170fd3cfa1a8317dc9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4e613fb025821d0f786a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e5aca8b6ab2e409ad677">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-ace3e59dbb8237483938"></a>

**0° CCW: unverified** — `in_game_visible_travel-ace3e59dbb8237483938`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-77c92ac4c64213d8b124"></a>

**90° CCW: unverified** — `in_game_visible_travel-77c92ac4c64213d8b124`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-421d46715a9f1a3f77a3"></a>

**180° CCW: unverified** — `in_game_visible_travel-421d46715a9f1a3f77a3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-8a625b9d27181df0919d"></a>

**270° CCW: unverified** — `in_game_visible_travel-8a625b9d27181df0919d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-44024dd261e654216c31"></a>

**0° CCW: unverified** — `in_game_visible_travel-44024dd261e654216c31`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-310a57095c56095d048b"></a>

**90° CCW: unverified** — `in_game_visible_travel-310a57095c56095d048b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-267a7d2f43b6737f365f"></a>

**180° CCW: unverified** — `in_game_visible_travel-267a7d2f43b6737f365f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-5d947a4f5f3b643fdea0"></a>

**270° CCW: unverified** — `in_game_visible_travel-5d947a4f5f3b643fdea0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-06-out; entry: channel-02-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-739a4336d40735397629"></a>

**0° CCW: unverified** — `in_game_visible_travel-739a4336d40735397629`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-0e77ac2cc1f0f11c9104"></a>

**90° CCW: unverified** — `in_game_visible_travel-0e77ac2cc1f0f11c9104`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-a2fab3b289f2cedd5aa5"></a>

**180° CCW: unverified** — `in_game_visible_travel-a2fab3b289f2cedd5aa5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-ff01ee387aba0852b6a6"></a>

**270° CCW: unverified** — `in_game_visible_travel-ff01ee387aba0852b6a6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-09-out; entry: channel-03-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-06b96dcde2c053b52509"></a>

**0° CCW: unverified** — `in_game_visible_travel-06b96dcde2c053b52509`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-44c136e53eb0cf361d62"></a>

**90° CCW: unverified** — `in_game_visible_travel-44c136e53eb0cf361d62`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-06f9e206f74084da8fae"></a>

**180° CCW: unverified** — `in_game_visible_travel-06f9e206f74084da8fae`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-5574e45064ffbcade437"></a>

**270° CCW: unverified** — `in_game_visible_travel-5574e45064ffbcade437`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-e746ce8e25ac9ddef8b9"></a>

**0° CCW: unverified** — `in_game_visible_travel-e746ce8e25ac9ddef8b9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-1e170fd3cfa1a8317dc9"></a>

**90° CCW: unverified** — `in_game_visible_travel-1e170fd3cfa1a8317dc9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-4e613fb025821d0f786a"></a>

**180° CCW: unverified** — `in_game_visible_travel-4e613fb025821d0f786a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-e5aca8b6ab2e409ad677"></a>

**270° CCW: unverified** — `in_game_visible_travel-e5aca8b6ab2e409ad677`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-07-out; entry: channel-05-in; exit: channel-07-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e27361ceafaf5fa0d536">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-469f0282f809dc671125">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e322faa023696d4c304">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c35ed00ab08cc094d11c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c08b91ae37389c9552d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bc6df833d3848776dd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa2a84111b885510220e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-358e3159873f6256e068">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4037cad9d9d7e3a72de0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d76f2df65a8caaf5f54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad99cfec7aa864c46e52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82a2c267b098fa55536f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-16e41796e16de87a992d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3ee770d080f325803f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4bb8c6f58201828f4ba7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41de395a9e8a50cc65e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9346ab26c70bf62cc189">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24ad9c109bc5b8421f8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45a445b7f35f40ed06e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a672ed2dd5883bc15f7d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a18bb6927b46dc908030">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29f1bd9f72ce0f9a2fe4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c21728bfa7c104d5329">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0ad7bdb05f7a2fc8323">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a261db6b6f5e8043c8fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a35faef039aa1ad2641">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd627dc1c8f026a54838">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-336fb9cb1de11667a391">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-869fc9b99e4ffe373223">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-619cfd2e3e59005031ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97ca1d7febde7941c8b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1678c2aa8855d7308b1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-211d0bc517a7ad4b538d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b49642cf642e1f39b9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94faff48084f249cb149">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e2e5d64b9f7aed1fe9f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5e462fe617cf01bb33d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5312224f1110473d43c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77af5e5850c274063469">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bed5c5ff79b2ede5ee7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-56ebbbd3304953ad160f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be3605e6fa70a75950bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca784cbbd285c909c74c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f7da07276373e37a872">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de60dae125de6d33ee4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-536d740409e6025fbafd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ef6e779512138fa023b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00434bf6357b63217b2d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7324414a66167193e06f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5ff9c7acd92e87a2e93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-744d68d75a20f53e810f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ceea5675ee7880543689">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6575c0663abe2fa1a5e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f933f3d4373723371a97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ad24fda107018654d8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28aa5e347b6f195e5fc4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9d1cbdb4c334c9f36362">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ea479640545b61cb8a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f2719b1799a6faf04ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7618bfe03a67f2f44de9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f48c23b2511b98532f02">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7a9e3ebd432362bbb85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09accd62a6e8acbe1b39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-656b0d3712e111574033">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa300ce36fac53605c64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc9f59407980f605bf9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13d15ce15911e00e836c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06a1ec09f3ee4135048e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c4edaede883922d2e4ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aed0b1b8382a9ad0a072">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39faf068d91cc6e8a7b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e534d8d0070c82d5793">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-71aeabf04f965b21cf0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b5d2384bf6e76f10e7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05b5c1636176a7ea2e2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-987461291069d022d098">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-86f671242d3bd6f5b5b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-790fedd4e4d890b21229">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d42b77e634bafe69824f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc588bf74b359cc13b45">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e27361ceafaf5fa0d536"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e27361ceafaf5fa0d536`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-469f0282f809dc671125"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-469f0282f809dc671125`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e322faa023696d4c304"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e322faa023696d4c304`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c35ed00ab08cc094d11c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c35ed00ab08cc094d11c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c08b91ae37389c9552d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c08b91ae37389c9552d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bc6df833d3848776dd3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0bc6df833d3848776dd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa2a84111b885510220e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aa2a84111b885510220e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-358e3159873f6256e068"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-358e3159873f6256e068`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4037cad9d9d7e3a72de0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4037cad9d9d7e3a72de0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d76f2df65a8caaf5f54"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9d76f2df65a8caaf5f54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad99cfec7aa864c46e52"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ad99cfec7aa864c46e52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82a2c267b098fa55536f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-82a2c267b098fa55536f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-16e41796e16de87a992d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-16e41796e16de87a992d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3ee770d080f325803f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d3ee770d080f325803f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4bb8c6f58201828f4ba7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4bb8c6f58201828f4ba7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41de395a9e8a50cc65e4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-41de395a9e8a50cc65e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9346ab26c70bf62cc189"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9346ab26c70bf62cc189`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24ad9c109bc5b8421f8f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24ad9c109bc5b8421f8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45a445b7f35f40ed06e6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-45a445b7f35f40ed06e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a672ed2dd5883bc15f7d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a672ed2dd5883bc15f7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a18bb6927b46dc908030"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a18bb6927b46dc908030`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29f1bd9f72ce0f9a2fe4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-29f1bd9f72ce0f9a2fe4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c21728bfa7c104d5329"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4c21728bfa7c104d5329`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0ad7bdb05f7a2fc8323"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a0ad7bdb05f7a2fc8323`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a261db6b6f5e8043c8fd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a261db6b6f5e8043c8fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a35faef039aa1ad2641"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a35faef039aa1ad2641`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd627dc1c8f026a54838"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd627dc1c8f026a54838`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-336fb9cb1de11667a391"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-336fb9cb1de11667a391`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-869fc9b99e4ffe373223"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-869fc9b99e4ffe373223`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-619cfd2e3e59005031ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-619cfd2e3e59005031ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97ca1d7febde7941c8b2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-97ca1d7febde7941c8b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1678c2aa8855d7308b1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a1678c2aa8855d7308b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-211d0bc517a7ad4b538d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-211d0bc517a7ad4b538d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b49642cf642e1f39b9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b49642cf642e1f39b9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94faff48084f249cb149"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94faff48084f249cb149`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e2e5d64b9f7aed1fe9f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8e2e5d64b9f7aed1fe9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5e462fe617cf01bb33d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5e462fe617cf01bb33d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5312224f1110473d43c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5312224f1110473d43c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77af5e5850c274063469"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-77af5e5850c274063469`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bed5c5ff79b2ede5ee7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9bed5c5ff79b2ede5ee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-56ebbbd3304953ad160f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-56ebbbd3304953ad160f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be3605e6fa70a75950bd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-be3605e6fa70a75950bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca784cbbd285c909c74c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ca784cbbd285c909c74c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f7da07276373e37a872"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0f7da07276373e37a872`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de60dae125de6d33ee4f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de60dae125de6d33ee4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-536d740409e6025fbafd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-536d740409e6025fbafd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ef6e779512138fa023b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ef6e779512138fa023b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00434bf6357b63217b2d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-00434bf6357b63217b2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7324414a66167193e06f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7324414a66167193e06f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5ff9c7acd92e87a2e93"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a5ff9c7acd92e87a2e93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-744d68d75a20f53e810f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-744d68d75a20f53e810f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ceea5675ee7880543689"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ceea5675ee7880543689`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6575c0663abe2fa1a5e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6575c0663abe2fa1a5e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f933f3d4373723371a97"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f933f3d4373723371a97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ad24fda107018654d8e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ad24fda107018654d8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28aa5e347b6f195e5fc4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-28aa5e347b6f195e5fc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9d1cbdb4c334c9f36362"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9d1cbdb4c334c9f36362`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ea479640545b61cb8a1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6ea479640545b61cb8a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f2719b1799a6faf04ec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f2719b1799a6faf04ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7618bfe03a67f2f44de9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7618bfe03a67f2f44de9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f48c23b2511b98532f02"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f48c23b2511b98532f02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7a9e3ebd432362bbb85"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7a9e3ebd432362bbb85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09accd62a6e8acbe1b39"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-09accd62a6e8acbe1b39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-656b0d3712e111574033"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-656b0d3712e111574033`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa300ce36fac53605c64"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa300ce36fac53605c64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc9f59407980f605bf9a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bc9f59407980f605bf9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13d15ce15911e00e836c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-13d15ce15911e00e836c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06a1ec09f3ee4135048e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-06a1ec09f3ee4135048e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c4edaede883922d2e4ed"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c4edaede883922d2e4ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aed0b1b8382a9ad0a072"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aed0b1b8382a9ad0a072`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39faf068d91cc6e8a7b8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-39faf068d91cc6e8a7b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e534d8d0070c82d5793"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2e534d8d0070c82d5793`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-71aeabf04f965b21cf0d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-71aeabf04f965b21cf0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b5d2384bf6e76f10e7d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4b5d2384bf6e76f10e7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05b5c1636176a7ea2e2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-05b5c1636176a7ea2e2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-987461291069d022d098"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-987461291069d022d098`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-86f671242d3bd6f5b5b9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-86f671242d3bd6f5b5b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-790fedd4e4d890b21229"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-790fedd4e4d890b21229`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d42b77e634bafe69824f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d42b77e634bafe69824f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc588bf74b359cc13b45"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bc588bf74b359cc13b45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrowed terminal asphalt while preserving the 6 m grade interfaces and its saved traffic routes. The later slip-lane revision lengthens the shoulder treatment and changes its access PATHs and white markings, while retaining all fifteen permanent types, the 31-cell union, and those narrow ground mouths. The earlier `ddrhw-parallel-diamond-parts-01` and `ddrhw-parallel-diamond-pedestrian-mouths-01` build identities retain their original scopes. The current revision uses `ddrhw-parallel-diamond-slip-lanes-02`; only its own matching saved-resource report can establish its software result.
