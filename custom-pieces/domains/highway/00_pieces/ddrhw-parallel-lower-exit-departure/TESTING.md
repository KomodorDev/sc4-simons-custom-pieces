---
title: "Testing: RHW Ramp — L1 Exit Lateral Departure — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L1 Exit Lateral Departure — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-lower-exit-departure**, used once as **P08** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 1 occupied tiles in a 1 × 1 rectangle, the exact authored 0° reference at X6, Y8, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-02-out` | road / 1 / primary | out | [-0.970563, -8.0, 6.144726]; [-0.7071067811865569, -0.7071067811865382]; -0.17911515 | `path-interface-61a771345641cff0130a` |
| `channel-01-in` | road / 1 / primary | in | [8.0, 0.104467, 7.5]; [-0.9404586044447427, -0.3399082425094264]; 0.0 | `path-interface-dd0badef63ec6dee79f2` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-02-out` | primary |

#### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X6, Y8)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-lower-exit-departure --build dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-lower-exit-departure
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current slip-lane revision changes the highway-shoulder traffic routes and their white markings within the existing construction footprint. Read outward from a through lane toward its ramp: each lower route has an 8 m smooth sideways taper and a 4 m straight shoulder section; each upper route has a 5 m taper and a 1 m straight shoulder section. The lower routes begin 6.788225 m farther upstream in already owned native highway tiles. The upper routes retain their previous outer ports because the unchanged 31-cell layout provides less shoulder distance there. These distances are measured along the straight highway axis. On-ramps follow the same profiles in reverse. The auxiliary-lane centre is 5.5 m from the highway axis; the checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot on the straight section. These are compressed experimental dimensions, not a real-road design standard. Native through PATHs, roadway outside the native 8 m deck edge, grades, ground terminals, permanent identifiers, and construction ownership retain their previous scope. Check the matching saved report before treating this source revision as verified. This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

The earlier narrow ground mouths are retained: each terminal keeps its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after that 3 m ground taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the ground taper is still narrowing; this is the actual driveway crossing.

## 4. Game checks

1. Select this exact component through the assembly button, match P08 at **X6, Y8**, and confirm that the occupied preview squares match **(X6, Y8)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-lower-exit-departure** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. One city tile owns this component, but its curved model extends over adjacent slip-lane tiles. That model overhang does not add another traffic owner. Because traffic is stored by complete city tile, this owner also retains the beginning of the neighbouring straight grade route. Its saved traffic edge and its physical flat joining section therefore occur at different places. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

Adaptive pavement is implemented through native texture variants and correctly rotating model props, rather than a fixed sidewalk slab. Its visible appearance depends on the native development rules, and a sidewalk replacement mod needs its own compatibility check. The approximately 1.149 m clearance applies where the terminal asphalt and retained pedestrian centreline run beside one another; the actual driveway crossings are deliberately excluded. A measured route clearance does not establish visible walking, a continuous pavement strip, or a particular pedestrian-versus-car priority in the game.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-exit-departure/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-exit-departure/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-f94440fcccc1d9225923">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-f94440fcccc1d9225923"></a>

**General: unverified** — `software_resources-f94440fcccc1d9225923`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-f94440fcccc1d9225923">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-f94440fcccc1d9225923"></a>

**General: unverified** — `software_connectivity-f94440fcccc1d9225923`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-departure:canonical-southeast | <a href="#case-preview_review-b6fc5f0a3a923561e6c7">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-departure:canonical-top | <a href="#case-preview_review-996257aad0905e7e2a28">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-departure:connection-overview | <a href="#case-preview_review-61043ff34424311b6dfb">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-departure:canonical-southeast</summary>

<a id="case-preview_review-b6fc5f0a3a923561e6c7"></a>

**General: unverified** — `preview_review-b6fc5f0a3a923561e6c7`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-exit-departure:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-departure:canonical-top</summary>

<a id="case-preview_review-996257aad0905e7e2a28"></a>

**General: unverified** — `preview_review-996257aad0905e7e2a28`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-exit-departure:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-departure:connection-overview</summary>

<a id="case-preview_review-61043ff34424311b6dfb"></a>

**General: unverified** — `preview_review-61043ff34424311b6dfb`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-exit-departure:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-365d7f4c771ada9aa7e6">[ ] unverified</a> | <a href="#case-in_game_render-35b43a832552d22431b6">[ ] unverified</a> | <a href="#case-in_game_render-1e9c59d22504476bc021">[ ] unverified</a> | <a href="#case-in_game_render-b6d29dd793af69beddae">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-365d7f4c771ada9aa7e6"></a>

**0° CCW: unverified** — `in_game_render-365d7f4c771ada9aa7e6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-35b43a832552d22431b6"></a>

**90° CCW: unverified** — `in_game_render-35b43a832552d22431b6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1e9c59d22504476bc021"></a>

**180° CCW: unverified** — `in_game_render-1e9c59d22504476bc021`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-b6d29dd793af69beddae"></a>

**270° CCW: unverified** — `in_game_render-b6d29dd793af69beddae`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-365d7f4c771ada9aa7e6">[ ] unverified</a> | <a href="#case-in_game_placement-35b43a832552d22431b6">[ ] unverified</a> | <a href="#case-in_game_placement-1e9c59d22504476bc021">[ ] unverified</a> | <a href="#case-in_game_placement-b6d29dd793af69beddae">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-365d7f4c771ada9aa7e6"></a>

**0° CCW: unverified** — `in_game_placement-365d7f4c771ada9aa7e6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-35b43a832552d22431b6"></a>

**90° CCW: unverified** — `in_game_placement-35b43a832552d22431b6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1e9c59d22504476bc021"></a>

**180° CCW: unverified** — `in_game_placement-1e9c59d22504476bc021`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-b6d29dd793af69beddae"></a>

**270° CCW: unverified** — `in_game_placement-b6d29dd793af69beddae`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-365d7f4c771ada9aa7e6">[ ] unverified</a> | <a href="#case-in_game_demolition-35b43a832552d22431b6">[ ] unverified</a> | <a href="#case-in_game_demolition-1e9c59d22504476bc021">[ ] unverified</a> | <a href="#case-in_game_demolition-b6d29dd793af69beddae">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-365d7f4c771ada9aa7e6"></a>

**0° CCW: unverified** — `in_game_demolition-365d7f4c771ada9aa7e6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-35b43a832552d22431b6"></a>

**90° CCW: unverified** — `in_game_demolition-35b43a832552d22431b6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1e9c59d22504476bc021"></a>

**180° CCW: unverified** — `in_game_demolition-1e9c59d22504476bc021`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-b6d29dd793af69beddae"></a>

**270° CCW: unverified** — `in_game_demolition-b6d29dd793af69beddae`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-365d7f4c771ada9aa7e6">[ ] unverified</a> | <a href="#case-in_game_save_reload-35b43a832552d22431b6">[ ] unverified</a> | <a href="#case-in_game_save_reload-1e9c59d22504476bc021">[ ] unverified</a> | <a href="#case-in_game_save_reload-b6d29dd793af69beddae">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-365d7f4c771ada9aa7e6"></a>

**0° CCW: unverified** — `in_game_save_reload-365d7f4c771ada9aa7e6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-35b43a832552d22431b6"></a>

**90° CCW: unverified** — `in_game_save_reload-35b43a832552d22431b6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1e9c59d22504476bc021"></a>

**180° CCW: unverified** — `in_game_save_reload-1e9c59d22504476bc021`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-b6d29dd793af69beddae"></a>

**270° CCW: unverified** — `in_game_save_reload-b6d29dd793af69beddae`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out | — | <a href="#case-in_game_route_query-08414c45bdec2122c0ab">[ ] unverified</a> | <a href="#case-in_game_route_query-db9e0f3f17bf32d5bca4">[ ] unverified</a> | <a href="#case-in_game_route_query-3acd439dfce2a79cddcb">[ ] unverified</a> | <a href="#case-in_game_route_query-1a97d1a3e2ff33efaa4d">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out</summary>

<a id="case-in_game_route_query-08414c45bdec2122c0ab"></a>

**0° CCW: unverified** — `in_game_route_query-08414c45bdec2122c0ab`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_route_query-db9e0f3f17bf32d5bca4"></a>

**90° CCW: unverified** — `in_game_route_query-db9e0f3f17bf32d5bca4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_route_query-3acd439dfce2a79cddcb"></a>

**180° CCW: unverified** — `in_game_route_query-3acd439dfce2a79cddcb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_route_query-1a97d1a3e2ff33efaa4d"></a>

**270° CCW: unverified** — `in_game_route_query-1a97d1a3e2ff33efaa4d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out | — | <a href="#case-in_game_visible_travel-08414c45bdec2122c0ab">[ ] unverified</a> | <a href="#case-in_game_visible_travel-db9e0f3f17bf32d5bca4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3acd439dfce2a79cddcb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1a97d1a3e2ff33efaa4d">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out</summary>

<a id="case-in_game_visible_travel-08414c45bdec2122c0ab"></a>

**0° CCW: unverified** — `in_game_visible_travel-08414c45bdec2122c0ab`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-db9e0f3f17bf32d5bca4"></a>

**90° CCW: unverified** — `in_game_visible_travel-db9e0f3f17bf32d5bca4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-3acd439dfce2a79cddcb"></a>

**180° CCW: unverified** — `in_game_visible_travel-3acd439dfce2a79cddcb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-1a97d1a3e2ff33efaa4d"></a>

**270° CCW: unverified** — `in_game_visible_travel-1a97d1a3e2ff33efaa4d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrowed terminal asphalt while preserving the 6 m grade interfaces and its saved traffic routes. The later slip-lane revision lengthens the shoulder treatment and changes its access PATHs and white markings, while retaining all fifteen permanent types, the 31-cell union, and those narrow ground mouths. The earlier `ddrhw-parallel-diamond-parts-01` and `ddrhw-parallel-diamond-pedestrian-mouths-01` build identities retain their original scopes. The current revision uses `ddrhw-parallel-diamond-slip-lanes-02`; only its own matching saved-resource report can establish its software result.
