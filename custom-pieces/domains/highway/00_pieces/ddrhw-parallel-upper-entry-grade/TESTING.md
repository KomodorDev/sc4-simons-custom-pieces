---
title: "Testing: RHW Ramp — L2 Entry Parallel Grade — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L2 Entry Parallel Grade — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-upper-entry-grade**, used once as **P15** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 3 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X6, Y6, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -16.970563, 0.131713]; [0.7071067811865476, 0.7071067811865476]; 0.183238121 | `path-interface-e362ca9b6cb3a77b1c9a` |
| `channel-06-out` | road / 1 / primary | out | [-8.0, -3.2, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -3.2, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-07-out` | road / 1 / primary | out | [-8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-03-in` | road / 1 / primary | in | [-8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-04-in` | road / 1 / primary | in | [-3.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-08-out` | road / 1 / primary | out | [-3.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-05-in` | road / 1 / primary | in | [3.2, 8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-09-out` | road / 1 / primary | out | [3.2, 8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-10-out` | road / 1 / primary | out | [16.970563, 8.0, 10.06235]; [0.7071067811865273, 0.7071067811865678]; 0.282020177 | `path-interface-e8e293f72dffb05f48c3` |

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

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X6, Y6), (X7, Y6), (X6, Y5)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-upper-entry-grade --build dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-upper-entry-grade
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current slip-lane revision changes the highway-shoulder traffic routes and their white markings within the existing construction footprint. Read outward from a through lane toward its ramp: each lower route has an 8 m smooth sideways taper and a 4 m straight shoulder section; each upper route has a 5 m taper and a 1 m straight shoulder section. The lower routes begin 6.788225 m farther upstream in already owned native highway tiles. The upper routes retain their previous outer ports because the unchanged 31-cell layout provides less shoulder distance there. These distances are measured along the straight highway axis. On-ramps follow the same profiles in reverse. The auxiliary-lane centre is 5.5 m from the highway axis; the checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot on the straight section. These are compressed experimental dimensions, not a real-road design standard. Native through PATHs, roadway outside the native 8 m deck edge, grades, ground terminals, permanent identifiers, and construction ownership retain their previous scope. Check the matching saved report before treating this source revision as verified. This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

The earlier narrow ground mouths are retained: each terminal keeps its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after that 3 m ground taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the ground taper is still narrowing; this is the actual driveway crossing.

## 4. Game checks

1. Select this exact component through the assembly button, match P15 at **X6, Y6**, and confirm that the occupied preview squares match **(X6, Y6), (X7, Y6), (X6, Y5)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-upper-entry-grade** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-upper-entry-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-upper-entry-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-298d860ac53ac7eaec4c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-298d860ac53ac7eaec4c"></a>

**General: unverified** — `software_resources-298d860ac53ac7eaec4c`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-298d860ac53ac7eaec4c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-298d860ac53ac7eaec4c"></a>

**General: unverified** — `software_connectivity-298d860ac53ac7eaec4c`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-entry-grade:canonical-southeast | <a href="#case-preview_review-2449632d742805ac5f7b">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-entry-grade:canonical-top | <a href="#case-preview_review-c46351794c4cb07ffca5">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-entry-grade:connection-overview | <a href="#case-preview_review-ba0bd3816de7dabde3b5">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-entry-grade:canonical-southeast</summary>

<a id="case-preview_review-2449632d742805ac5f7b"></a>

**General: unverified** — `preview_review-2449632d742805ac5f7b`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-entry-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-entry-grade:canonical-top</summary>

<a id="case-preview_review-c46351794c4cb07ffca5"></a>

**General: unverified** — `preview_review-c46351794c4cb07ffca5`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-entry-grade:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-entry-grade:connection-overview</summary>

<a id="case-preview_review-ba0bd3816de7dabde3b5"></a>

**General: unverified** — `preview_review-ba0bd3816de7dabde3b5`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-entry-grade:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-997dc686b8e60bd3e6d5">[ ] unverified</a> | <a href="#case-in_game_render-26b06501233629c098ae">[ ] unverified</a> | <a href="#case-in_game_render-7583ed07ae5647c4de95">[ ] unverified</a> | <a href="#case-in_game_render-02714bbffb624b6b0781">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-997dc686b8e60bd3e6d5"></a>

**0° CCW: unverified** — `in_game_render-997dc686b8e60bd3e6d5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-26b06501233629c098ae"></a>

**90° CCW: unverified** — `in_game_render-26b06501233629c098ae`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7583ed07ae5647c4de95"></a>

**180° CCW: unverified** — `in_game_render-7583ed07ae5647c4de95`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-02714bbffb624b6b0781"></a>

**270° CCW: unverified** — `in_game_render-02714bbffb624b6b0781`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-997dc686b8e60bd3e6d5">[ ] unverified</a> | <a href="#case-in_game_placement-26b06501233629c098ae">[ ] unverified</a> | <a href="#case-in_game_placement-7583ed07ae5647c4de95">[ ] unverified</a> | <a href="#case-in_game_placement-02714bbffb624b6b0781">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-997dc686b8e60bd3e6d5"></a>

**0° CCW: unverified** — `in_game_placement-997dc686b8e60bd3e6d5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-26b06501233629c098ae"></a>

**90° CCW: unverified** — `in_game_placement-26b06501233629c098ae`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7583ed07ae5647c4de95"></a>

**180° CCW: unverified** — `in_game_placement-7583ed07ae5647c4de95`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-02714bbffb624b6b0781"></a>

**270° CCW: unverified** — `in_game_placement-02714bbffb624b6b0781`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-997dc686b8e60bd3e6d5">[ ] unverified</a> | <a href="#case-in_game_demolition-26b06501233629c098ae">[ ] unverified</a> | <a href="#case-in_game_demolition-7583ed07ae5647c4de95">[ ] unverified</a> | <a href="#case-in_game_demolition-02714bbffb624b6b0781">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-997dc686b8e60bd3e6d5"></a>

**0° CCW: unverified** — `in_game_demolition-997dc686b8e60bd3e6d5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-26b06501233629c098ae"></a>

**90° CCW: unverified** — `in_game_demolition-26b06501233629c098ae`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7583ed07ae5647c4de95"></a>

**180° CCW: unverified** — `in_game_demolition-7583ed07ae5647c4de95`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-02714bbffb624b6b0781"></a>

**270° CCW: unverified** — `in_game_demolition-02714bbffb624b6b0781`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-997dc686b8e60bd3e6d5">[ ] unverified</a> | <a href="#case-in_game_save_reload-26b06501233629c098ae">[ ] unverified</a> | <a href="#case-in_game_save_reload-7583ed07ae5647c4de95">[ ] unverified</a> | <a href="#case-in_game_save_reload-02714bbffb624b6b0781">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-997dc686b8e60bd3e6d5"></a>

**0° CCW: unverified** — `in_game_save_reload-997dc686b8e60bd3e6d5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-26b06501233629c098ae"></a>

**90° CCW: unverified** — `in_game_save_reload-26b06501233629c098ae`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7583ed07ae5647c4de95"></a>

**180° CCW: unverified** — `in_game_save_reload-7583ed07ae5647c4de95`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-02714bbffb624b6b0781"></a>

**270° CCW: unverified** — `in_game_save_reload-02714bbffb624b6b0781`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-6eac2dca015695dcc59e">[ ] unverified</a> | <a href="#case-in_game_route_query-5ba8675af0d2a7d73a6d">[ ] unverified</a> | <a href="#case-in_game_route_query-72b8be325d01b8704ac4">[ ] unverified</a> | <a href="#case-in_game_route_query-eba4f88f6f68a15e1d15">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-02efe5c6f1249c731466">[ ] unverified</a> | <a href="#case-in_game_route_query-3fa7b7a3bc5d324ff93a">[ ] unverified</a> | <a href="#case-in_game_route_query-510a320e8b8cd29c73dd">[ ] unverified</a> | <a href="#case-in_game_route_query-c734fdf99a30e7526dbe">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-b4332e1c142006ef55be">[ ] unverified</a> | <a href="#case-in_game_route_query-ad4a1d0d7f6e681e8d43">[ ] unverified</a> | <a href="#case-in_game_route_query-5de3a58ed7a86b5e39ba">[ ] unverified</a> | <a href="#case-in_game_route_query-9e09a7ae0dd7e6827fd8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-064823633e22c5505c8c">[ ] unverified</a> | <a href="#case-in_game_route_query-792eefe1cd0897e6ed72">[ ] unverified</a> | <a href="#case-in_game_route_query-76623516117cb30edc6b">[ ] unverified</a> | <a href="#case-in_game_route_query-74681e3b4c47892d33f5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-c758be223a5c39a1109c">[ ] unverified</a> | <a href="#case-in_game_route_query-dc246b88660d32a67b69">[ ] unverified</a> | <a href="#case-in_game_route_query-36db970cd16742132c42">[ ] unverified</a> | <a href="#case-in_game_route_query-96ac501176527c5d71f8">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-6eac2dca015695dcc59e"></a>

**0° CCW: unverified** — `in_game_route_query-6eac2dca015695dcc59e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-5ba8675af0d2a7d73a6d"></a>

**90° CCW: unverified** — `in_game_route_query-5ba8675af0d2a7d73a6d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-72b8be325d01b8704ac4"></a>

**180° CCW: unverified** — `in_game_route_query-72b8be325d01b8704ac4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-eba4f88f6f68a15e1d15"></a>

**270° CCW: unverified** — `in_game_route_query-eba4f88f6f68a15e1d15`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-02efe5c6f1249c731466"></a>

**0° CCW: unverified** — `in_game_route_query-02efe5c6f1249c731466`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-3fa7b7a3bc5d324ff93a"></a>

**90° CCW: unverified** — `in_game_route_query-3fa7b7a3bc5d324ff93a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-510a320e8b8cd29c73dd"></a>

**180° CCW: unverified** — `in_game_route_query-510a320e8b8cd29c73dd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-c734fdf99a30e7526dbe"></a>

**270° CCW: unverified** — `in_game_route_query-c734fdf99a30e7526dbe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-b4332e1c142006ef55be"></a>

**0° CCW: unverified** — `in_game_route_query-b4332e1c142006ef55be`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-ad4a1d0d7f6e681e8d43"></a>

**90° CCW: unverified** — `in_game_route_query-ad4a1d0d7f6e681e8d43`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-5de3a58ed7a86b5e39ba"></a>

**180° CCW: unverified** — `in_game_route_query-5de3a58ed7a86b5e39ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-9e09a7ae0dd7e6827fd8"></a>

**270° CCW: unverified** — `in_game_route_query-9e09a7ae0dd7e6827fd8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-064823633e22c5505c8c"></a>

**0° CCW: unverified** — `in_game_route_query-064823633e22c5505c8c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-792eefe1cd0897e6ed72"></a>

**90° CCW: unverified** — `in_game_route_query-792eefe1cd0897e6ed72`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-76623516117cb30edc6b"></a>

**180° CCW: unverified** — `in_game_route_query-76623516117cb30edc6b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-74681e3b4c47892d33f5"></a>

**270° CCW: unverified** — `in_game_route_query-74681e3b4c47892d33f5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-c758be223a5c39a1109c"></a>

**0° CCW: unverified** — `in_game_route_query-c758be223a5c39a1109c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-dc246b88660d32a67b69"></a>

**90° CCW: unverified** — `in_game_route_query-dc246b88660d32a67b69`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-36db970cd16742132c42"></a>

**180° CCW: unverified** — `in_game_route_query-36db970cd16742132c42`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-96ac501176527c5d71f8"></a>

**270° CCW: unverified** — `in_game_route_query-96ac501176527c5d71f8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 20 cases; unverified: 20</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-6eac2dca015695dcc59e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5ba8675af0d2a7d73a6d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-72b8be325d01b8704ac4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-eba4f88f6f68a15e1d15">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-02efe5c6f1249c731466">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3fa7b7a3bc5d324ff93a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-510a320e8b8cd29c73dd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c734fdf99a30e7526dbe">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-b4332e1c142006ef55be">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ad4a1d0d7f6e681e8d43">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5de3a58ed7a86b5e39ba">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9e09a7ae0dd7e6827fd8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-064823633e22c5505c8c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-792eefe1cd0897e6ed72">[ ] unverified</a> | <a href="#case-in_game_visible_travel-76623516117cb30edc6b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-74681e3b4c47892d33f5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-c758be223a5c39a1109c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dc246b88660d32a67b69">[ ] unverified</a> | <a href="#case-in_game_visible_travel-36db970cd16742132c42">[ ] unverified</a> | <a href="#case-in_game_visible_travel-96ac501176527c5d71f8">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-6eac2dca015695dcc59e"></a>

**0° CCW: unverified** — `in_game_visible_travel-6eac2dca015695dcc59e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-5ba8675af0d2a7d73a6d"></a>

**90° CCW: unverified** — `in_game_visible_travel-5ba8675af0d2a7d73a6d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-72b8be325d01b8704ac4"></a>

**180° CCW: unverified** — `in_game_visible_travel-72b8be325d01b8704ac4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-eba4f88f6f68a15e1d15"></a>

**270° CCW: unverified** — `in_game_visible_travel-eba4f88f6f68a15e1d15`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-10-out; entry: channel-01-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-02efe5c6f1249c731466"></a>

**0° CCW: unverified** — `in_game_visible_travel-02efe5c6f1249c731466`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-3fa7b7a3bc5d324ff93a"></a>

**90° CCW: unverified** — `in_game_visible_travel-3fa7b7a3bc5d324ff93a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-510a320e8b8cd29c73dd"></a>

**180° CCW: unverified** — `in_game_visible_travel-510a320e8b8cd29c73dd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-c734fdf99a30e7526dbe"></a>

**270° CCW: unverified** — `in_game_visible_travel-c734fdf99a30e7526dbe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-09-out; entry: channel-02-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-b4332e1c142006ef55be"></a>

**0° CCW: unverified** — `in_game_visible_travel-b4332e1c142006ef55be`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-ad4a1d0d7f6e681e8d43"></a>

**90° CCW: unverified** — `in_game_visible_travel-ad4a1d0d7f6e681e8d43`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-5de3a58ed7a86b5e39ba"></a>

**180° CCW: unverified** — `in_game_visible_travel-5de3a58ed7a86b5e39ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-9e09a7ae0dd7e6827fd8"></a>

**270° CCW: unverified** — `in_game_visible_travel-9e09a7ae0dd7e6827fd8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-08-out; entry: channel-03-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-064823633e22c5505c8c"></a>

**0° CCW: unverified** — `in_game_visible_travel-064823633e22c5505c8c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-792eefe1cd0897e6ed72"></a>

**90° CCW: unverified** — `in_game_visible_travel-792eefe1cd0897e6ed72`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-76623516117cb30edc6b"></a>

**180° CCW: unverified** — `in_game_visible_travel-76623516117cb30edc6b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-74681e3b4c47892d33f5"></a>

**270° CCW: unverified** — `in_game_visible_travel-74681e3b4c47892d33f5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-07-out; entry: channel-04-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-c758be223a5c39a1109c"></a>

**0° CCW: unverified** — `in_game_visible_travel-c758be223a5c39a1109c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-dc246b88660d32a67b69"></a>

**90° CCW: unverified** — `in_game_visible_travel-dc246b88660d32a67b69`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-36db970cd16742132c42"></a>

**180° CCW: unverified** — `in_game_visible_travel-36db970cd16742132c42`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-96ac501176527c5d71f8"></a>

**270° CCW: unverified** — `in_game_visible_travel-96ac501176527c5d71f8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-06-out; entry: channel-05-in; exit: channel-06-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a5c83bae5e441fb8c74f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-231068c376b6710a2629">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c79c1ab89f2dbbc80a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce77653b847c0e3ebf2e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-efc59b802d30296af99e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e01237d70948ce2cd751">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e75efb085827051af137">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7012292a791e2626509">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-999da127997e25a6547d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7e75863866b9105d7ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4cfded793797f31b75f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64e6999ce0f79b73008f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0f763d694356b8d5ad77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e24695e16ac51ce1ee47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c2e11354f5d4aad27bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a712ebbdfdcff46ec5d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e833283489e97bcd4a53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a46caa4c0e98e2d1646">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ca25a2a32ac8c10aea4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c699577df0e6eede036c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e4d28c0136c21a1b0ebb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a64d1f1d5a4a0fda604">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46c216027c60360e5363">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af75f9fa8296e74e26e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4efc2b6bf073d3978c61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1121dc267e91d666822e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c85179030eb2b570c5ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ddf394cb01ba19f4cab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f23870d94ae7d1505a6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7dd5190e599d6edde0e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3bea94a618b186107ea3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d74f98838e544fdbc4c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1ebd8e4fa068013e6d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-079c958f0fd35896c5e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-602a2b967c2dcafa2b53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd71d47db3b71b94dcc1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ae55f6c7981f80b63d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41e544166bbc39437798">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1b19a5a4f7096726713">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f28e836bc63a153f89fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-89608eba1d19e21966ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca81f2efa311ac056afb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00e75bb2b80460c97c6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a17401ba887422e5e41c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-47fca21d239449beff63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d9a49c8a73f8e5bc36f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-013baa8e83a24b30a432">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d2e0c6503aa0bef7dee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-345637f6998cd28a7951">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7da9d630b039dee8a4d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abb5c928cdd879295a96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93bac3ed561150fd33dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93b3a3dab11e9c527c87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ac66122340ea063078d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0de93256a1797521ecd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-362010c6718a60a9a32e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23350299d69ea859e440">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3663943e05696b8dc6d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f1a3cef6a669ed9bd5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb4079e23ccb533d5162">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3362a4fca3dabc2d5b08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-695523a773bdc96946e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a72054e0d484779bf20">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93bc8a2b26daa2ed3870">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7884bb5f0276171ec73d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a89393899c40a1825a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ae80b49a3952e30c08a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c47f9e1b279eaf280e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca0e63e2e374bd21a140">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9e3fc382e6947c19187">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed4ab94e587eaf17a08c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81e29ccecd8060e9ec93">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-636b24a798a7b4a91e88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b6aa45af0e5af9d7ce9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49498893c2a51741da2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74065c9cd0c0fa7d6cf4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-39b738a7e6da6286c07c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0740c81c8904e487ada">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8ff3317f600de29c7fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f45c82667cf421c2453e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a5c83bae5e441fb8c74f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a5c83bae5e441fb8c74f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-231068c376b6710a2629"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-231068c376b6710a2629`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c79c1ab89f2dbbc80a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7c79c1ab89f2dbbc80a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce77653b847c0e3ebf2e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ce77653b847c0e3ebf2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-efc59b802d30296af99e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-efc59b802d30296af99e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e01237d70948ce2cd751"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e01237d70948ce2cd751`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e75efb085827051af137"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e75efb085827051af137`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7012292a791e2626509"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a7012292a791e2626509`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-999da127997e25a6547d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-999da127997e25a6547d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7e75863866b9105d7ae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a7e75863866b9105d7ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4cfded793797f31b75f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a4cfded793797f31b75f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64e6999ce0f79b73008f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64e6999ce0f79b73008f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0f763d694356b8d5ad77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0f763d694356b8d5ad77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e24695e16ac51ce1ee47"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e24695e16ac51ce1ee47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c2e11354f5d4aad27bf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c2e11354f5d4aad27bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a712ebbdfdcff46ec5d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a712ebbdfdcff46ec5d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e833283489e97bcd4a53"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e833283489e97bcd4a53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a46caa4c0e98e2d1646"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a46caa4c0e98e2d1646`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ca25a2a32ac8c10aea4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ca25a2a32ac8c10aea4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c699577df0e6eede036c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c699577df0e6eede036c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e4d28c0136c21a1b0ebb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e4d28c0136c21a1b0ebb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a64d1f1d5a4a0fda604"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a64d1f1d5a4a0fda604`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46c216027c60360e5363"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-46c216027c60360e5363`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af75f9fa8296e74e26e2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af75f9fa8296e74e26e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4efc2b6bf073d3978c61"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4efc2b6bf073d3978c61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1121dc267e91d666822e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1121dc267e91d666822e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c85179030eb2b570c5ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c85179030eb2b570c5ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ddf394cb01ba19f4cab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3ddf394cb01ba19f4cab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f23870d94ae7d1505a6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f23870d94ae7d1505a6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7dd5190e599d6edde0e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7dd5190e599d6edde0e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3bea94a618b186107ea3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3bea94a618b186107ea3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d74f98838e544fdbc4c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8d74f98838e544fdbc4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d1ebd8e4fa068013e6d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1ebd8e4fa068013e6d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-079c958f0fd35896c5e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-079c958f0fd35896c5e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-602a2b967c2dcafa2b53"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-602a2b967c2dcafa2b53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd71d47db3b71b94dcc1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dd71d47db3b71b94dcc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ae55f6c7981f80b63d2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ae55f6c7981f80b63d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41e544166bbc39437798"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-41e544166bbc39437798`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1b19a5a4f7096726713"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d1b19a5a4f7096726713`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f28e836bc63a153f89fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f28e836bc63a153f89fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-89608eba1d19e21966ff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-89608eba1d19e21966ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca81f2efa311ac056afb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ca81f2efa311ac056afb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00e75bb2b80460c97c6a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-00e75bb2b80460c97c6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a17401ba887422e5e41c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a17401ba887422e5e41c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-47fca21d239449beff63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-47fca21d239449beff63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d9a49c8a73f8e5bc36f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d9a49c8a73f8e5bc36f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-013baa8e83a24b30a432"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-013baa8e83a24b30a432`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d2e0c6503aa0bef7dee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d2e0c6503aa0bef7dee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-345637f6998cd28a7951"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-345637f6998cd28a7951`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7da9d630b039dee8a4d9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7da9d630b039dee8a4d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abb5c928cdd879295a96"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-abb5c928cdd879295a96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93bac3ed561150fd33dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-93bac3ed561150fd33dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93b3a3dab11e9c527c87"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93b3a3dab11e9c527c87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ac66122340ea063078d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ac66122340ea063078d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0de93256a1797521ecd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0de93256a1797521ecd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-362010c6718a60a9a32e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-362010c6718a60a9a32e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23350299d69ea859e440"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23350299d69ea859e440`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3663943e05696b8dc6d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3663943e05696b8dc6d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f1a3cef6a669ed9bd5c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0f1a3cef6a669ed9bd5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb4079e23ccb533d5162"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb4079e23ccb533d5162`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3362a4fca3dabc2d5b08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3362a4fca3dabc2d5b08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-695523a773bdc96946e7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-695523a773bdc96946e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a72054e0d484779bf20"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0a72054e0d484779bf20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93bc8a2b26daa2ed3870"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-93bc8a2b26daa2ed3870`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7884bb5f0276171ec73d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7884bb5f0276171ec73d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a89393899c40a1825a1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a89393899c40a1825a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ae80b49a3952e30c08a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ae80b49a3952e30c08a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c47f9e1b279eaf280e0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c47f9e1b279eaf280e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca0e63e2e374bd21a140"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca0e63e2e374bd21a140`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9e3fc382e6947c19187"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d9e3fc382e6947c19187`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed4ab94e587eaf17a08c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed4ab94e587eaf17a08c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81e29ccecd8060e9ec93"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-81e29ccecd8060e9ec93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-636b24a798a7b4a91e88"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-636b24a798a7b4a91e88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b6aa45af0e5af9d7ce9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0b6aa45af0e5af9d7ce9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49498893c2a51741da2c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-49498893c2a51741da2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74065c9cd0c0fa7d6cf4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-74065c9cd0c0fa7d6cf4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-39b738a7e6da6286c07c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-39b738a7e6da6286c07c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0740c81c8904e487ada"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e0740c81c8904e487ada`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8ff3317f600de29c7fd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b8ff3317f600de29c7fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f45c82667cf421c2453e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f45c82667cf421c2453e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrowed terminal asphalt while preserving the 6 m grade interfaces and its saved traffic routes. The later slip-lane revision lengthens the shoulder treatment and changes its access PATHs and white markings, while retaining all fifteen permanent types, the 31-cell union, and those narrow ground mouths. The earlier `ddrhw-parallel-diamond-parts-01` and `ddrhw-parallel-diamond-pedestrian-mouths-01` build identities retain their original scopes. The current revision uses `ddrhw-parallel-diamond-slip-lanes-02`; only its own matching saved-resource report can establish its software result.
