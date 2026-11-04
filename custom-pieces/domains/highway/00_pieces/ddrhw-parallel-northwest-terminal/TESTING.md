---
title: "Testing: Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: Avenue — Northwest Avenue Right-Turn Terminal — Parallel DD RHW

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

The current policy is **no cast shadow from this component**. Verify that appearance on a fresh placement after restarting with the checked no-shadow revision; older saved-attachment cleanup is a separate pending observation. The assembly’s [current no-shadow test](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#44-independent-module-shadow-test) owns the detailed camera, quality, zoom, and lifecycle procedure.

This record covers **ddrhw-parallel-northwest-terminal**, used once as **P02** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 3 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X3, Y6, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, 3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-06-out` | road / 1 / primary | out | [-3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-07-out` | road / 1 / primary | out | [-0.970563, -24.0, 0.311171]; [-0.7071067811865476, -0.7071067811865476]; 0.179117716 | `path-interface-c97e67b221c113d321e9` |
| `channel-08-out` | road / 1 / primary | out | [3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-09-out` | road / 1 / primary | out | [8.0, -19.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-10-out` | road / 1 / primary | out | [8.0, -12.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-03-in` | road / 1 / primary | in | [12.8, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-04-in` | road / 1 / primary | in | [19.2, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-05-in` | road / 1 / primary | in | [24.0, 0.970563, 0.311171]; [-0.7071067811865476, -0.7071067811865476]; -0.179117716 | `path-interface-efc252caa7500130308e` |
| `channel-11-in` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-13-out` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `channel-14-out` | pedestrian / 2 / primary | out | [8.0, -23.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-12-in` | pedestrian / 2 / primary | in | [23.3, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-07-out` | primary |
| road | `channel-01-in` → `channel-09-out` | primary |
| road | `channel-02-in` → `channel-10-out` | primary |
| road | `channel-03-in` → `channel-06-out` | primary |
| road | `channel-04-in` → `channel-08-out` | primary |
| road | `channel-05-in` → `channel-08-out` | primary |
| pedestrian | `channel-11-in` → `channel-14-out` | primary |
| pedestrian | `channel-12-in` → `channel-13-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-11-in` | pedestrian / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-06-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-07-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-08-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-09-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `channel-12-in` | pedestrian / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X3, Y6), (X4, Y6), (X3, Y5)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-northwest-terminal --build dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-northwest-terminal
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current slip-lane revision changes the highway-shoulder traffic routes and their white markings within the existing construction footprint. Read outward from a through lane toward its ramp: each lower route has an 8 m smooth sideways taper and a 4 m straight shoulder section; each upper route has a 5 m taper and a 1 m straight shoulder section. The lower routes begin 6.788225 m farther upstream in already owned native highway tiles. The upper routes retain their previous outer ports because the unchanged 31-cell layout provides less shoulder distance there. These distances are measured along the straight highway axis. On-ramps follow the same profiles in reverse. The auxiliary-lane centre is 5.5 m from the highway axis; the checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot on the straight section. These are compressed experimental dimensions, not a real-road design standard. Native through PATHs, roadway outside the native 8 m deck edge, grades, ground terminals, permanent identifiers, and construction ownership retain their previous scope. Check the matching saved report before treating this source revision as verified. Adaptive sidewalks are implemented for all three Avenue cells of this component. The game selects a native Avenue pavement appearance from the surrounding development; connecting another Avenue alone does not force a sidewalk to appear. The rotating highway or ramp model is attached above that native ground artwork, and the pedestrian PATHs are separate retained traffic data. The complete new assembly still needs its own game observations. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

The earlier narrow ground mouths are retained: each terminal keeps its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after that 3 m ground taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the ground taper is still narrowing; this is the actual driveway crossing.

## 4. Game checks

1. Select this exact component through the assembly button, match P02 at **X3, Y6**, and confirm that the occupied preview squares match **(X3, Y6), (X4, Y6), (X3, Y5)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect for unwanted cast shadows at Medium and High quality; this component intentionally supplies none. Demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle or old shadow attachment remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-northwest-terminal** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. Its three occupied tiles retain the native two-way Avenue and pedestrian channels. The 3.5 m asphalt leaves 0.5 m on each side of the checked 2.5 m-wide car corridor. Where a ramp runs parallel to an Avenue pedestrian centreline, the retained clearance to its asphalt edge is approximately 1.149 m; this measures a route centreline, not a promised sidewalk width. Each driveway still crosses a pedestrian route on the way into its carriageway. Adaptive pavement can appear beside that driveway, but no continuous sidewalk surface is drawn across the ramp asphalt. The visible turn models extend above some neighbouring owners, while their traffic fragments remain with the city tile they cross. All three native Avenue cells use the implemented adaptive-ground resources and rotating overlay models. The unused local [1,1] corner is the removable placement handle. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

Adaptive pavement is implemented through native texture variants and correctly rotating model props, rather than a fixed sidewalk slab. Its visible appearance depends on the native development rules, and a sidewalk replacement mod needs its own compatibility check. The approximately 1.149 m clearance applies where the terminal asphalt and retained pedestrian centreline run beside one another; the actual driveway crossings are deliberately excluded. A measured route clearance does not establish visible walking, a continuous pavement strip, or a particular pedestrian-versus-car priority in the game.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-northwest-terminal/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-northwest-terminal/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-118633f47b48c078753c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-118633f47b48c078753c"></a>

**General: unverified** — `software_resources-118633f47b48c078753c`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-118633f47b48c078753c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-118633f47b48c078753c"></a>

**General: unverified** — `software_connectivity-118633f47b48c078753c`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-northwest-terminal:canonical-southeast | <a href="#case-preview_review-96631e8c439579739011">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-northwest-terminal:canonical-top | <a href="#case-preview_review-b481ef73a82599e009d8">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-northwest-terminal:connection-overview | <a href="#case-preview_review-a84dbe53513473b904a1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-northwest-terminal:canonical-southeast</summary>

<a id="case-preview_review-96631e8c439579739011"></a>

**General: unverified** — `preview_review-96631e8c439579739011`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-northwest-terminal:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-northwest-terminal:canonical-top</summary>

<a id="case-preview_review-b481ef73a82599e009d8"></a>

**General: unverified** — `preview_review-b481ef73a82599e009d8`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-northwest-terminal:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-northwest-terminal:connection-overview</summary>

<a id="case-preview_review-a84dbe53513473b904a1"></a>

**General: unverified** — `preview_review-a84dbe53513473b904a1`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-northwest-terminal:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-3f154465659fba41604e">[ ] unverified</a> | <a href="#case-in_game_render-c65ed2833012685c8d9f">[ ] unverified</a> | <a href="#case-in_game_render-f79902196d5ae5a3cecb">[ ] unverified</a> | <a href="#case-in_game_render-0c44ec7255069a591adc">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-3f154465659fba41604e"></a>

**0° CCW: unverified** — `in_game_render-3f154465659fba41604e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c65ed2833012685c8d9f"></a>

**90° CCW: unverified** — `in_game_render-c65ed2833012685c8d9f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-f79902196d5ae5a3cecb"></a>

**180° CCW: unverified** — `in_game_render-f79902196d5ae5a3cecb`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0c44ec7255069a591adc"></a>

**270° CCW: unverified** — `in_game_render-0c44ec7255069a591adc`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-3f154465659fba41604e">[ ] unverified</a> | <a href="#case-in_game_placement-c65ed2833012685c8d9f">[ ] unverified</a> | <a href="#case-in_game_placement-f79902196d5ae5a3cecb">[ ] unverified</a> | <a href="#case-in_game_placement-0c44ec7255069a591adc">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-3f154465659fba41604e"></a>

**0° CCW: unverified** — `in_game_placement-3f154465659fba41604e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c65ed2833012685c8d9f"></a>

**90° CCW: unverified** — `in_game_placement-c65ed2833012685c8d9f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-f79902196d5ae5a3cecb"></a>

**180° CCW: unverified** — `in_game_placement-f79902196d5ae5a3cecb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0c44ec7255069a591adc"></a>

**270° CCW: unverified** — `in_game_placement-0c44ec7255069a591adc`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-3f154465659fba41604e">[ ] unverified</a> | <a href="#case-in_game_demolition-c65ed2833012685c8d9f">[ ] unverified</a> | <a href="#case-in_game_demolition-f79902196d5ae5a3cecb">[ ] unverified</a> | <a href="#case-in_game_demolition-0c44ec7255069a591adc">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-3f154465659fba41604e"></a>

**0° CCW: unverified** — `in_game_demolition-3f154465659fba41604e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c65ed2833012685c8d9f"></a>

**90° CCW: unverified** — `in_game_demolition-c65ed2833012685c8d9f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-f79902196d5ae5a3cecb"></a>

**180° CCW: unverified** — `in_game_demolition-f79902196d5ae5a3cecb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0c44ec7255069a591adc"></a>

**270° CCW: unverified** — `in_game_demolition-0c44ec7255069a591adc`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-3f154465659fba41604e">[ ] unverified</a> | <a href="#case-in_game_save_reload-c65ed2833012685c8d9f">[ ] unverified</a> | <a href="#case-in_game_save_reload-f79902196d5ae5a3cecb">[ ] unverified</a> | <a href="#case-in_game_save_reload-0c44ec7255069a591adc">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-3f154465659fba41604e"></a>

**0° CCW: unverified** — `in_game_save_reload-3f154465659fba41604e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c65ed2833012685c8d9f"></a>

**90° CCW: unverified** — `in_game_save_reload-c65ed2833012685c8d9f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-f79902196d5ae5a3cecb"></a>

**180° CCW: unverified** — `in_game_save_reload-f79902196d5ae5a3cecb`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0c44ec7255069a591adc"></a>

**270° CCW: unverified** — `in_game_save_reload-0c44ec7255069a591adc`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out | — | <a href="#case-in_game_route_query-f1a985e02baf99cf2c04">[ ] unverified</a> | <a href="#case-in_game_route_query-78434a7a649f0335a881">[ ] unverified</a> | <a href="#case-in_game_route_query-1d1c3a32a02293529d16">[ ] unverified</a> | <a href="#case-in_game_route_query-9b9638ff685882e192df">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out | — | <a href="#case-in_game_route_query-0912c59dd2e19e4f84f8">[ ] unverified</a> | <a href="#case-in_game_route_query-8ba52a10814e3585a7f7">[ ] unverified</a> | <a href="#case-in_game_route_query-efc37b60abbb6d349aa8">[ ] unverified</a> | <a href="#case-in_game_route_query-31ecbf7481215d41890d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-b22488a4e18858fc5be0">[ ] unverified</a> | <a href="#case-in_game_route_query-65075ea6d7ba3741647b">[ ] unverified</a> | <a href="#case-in_game_route_query-89cb36dd3621871c9954">[ ] unverified</a> | <a href="#case-in_game_route_query-9169d2062a63016e7f48">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out | — | <a href="#case-in_game_route_query-c616a473fefd272719cc">[ ] unverified</a> | <a href="#case-in_game_route_query-12ed302c6a6a35c43e83">[ ] unverified</a> | <a href="#case-in_game_route_query-6266dcf948092007f3a3">[ ] unverified</a> | <a href="#case-in_game_route_query-ebfe24b97097daa5c937">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-757c82fed45f3a38f86c">[ ] unverified</a> | <a href="#case-in_game_route_query-4320ffbe46bc1872408c">[ ] unverified</a> | <a href="#case-in_game_route_query-8f3b662fbf307a96ddff">[ ] unverified</a> | <a href="#case-in_game_route_query-4baffeba1674a213d74e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out | — | <a href="#case-in_game_route_query-7748ada03d4888a35c7a">[ ] unverified</a> | <a href="#case-in_game_route_query-f71d8afda3f571f6c3a3">[ ] unverified</a> | <a href="#case-in_game_route_query-f73537f77d792658f52f">[ ] unverified</a> | <a href="#case-in_game_route_query-d57c1e02af9de9279078">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out</summary>

<a id="case-in_game_route_query-f1a985e02baf99cf2c04"></a>

**0° CCW: unverified** — `in_game_route_query-f1a985e02baf99cf2c04`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-78434a7a649f0335a881"></a>

**90° CCW: unverified** — `in_game_route_query-78434a7a649f0335a881`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-1d1c3a32a02293529d16"></a>

**180° CCW: unverified** — `in_game_route_query-1d1c3a32a02293529d16`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_route_query-9b9638ff685882e192df"></a>

**270° CCW: unverified** — `in_game_route_query-9b9638ff685882e192df`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out</summary>

<a id="case-in_game_route_query-0912c59dd2e19e4f84f8"></a>

**0° CCW: unverified** — `in_game_route_query-0912c59dd2e19e4f84f8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-8ba52a10814e3585a7f7"></a>

**90° CCW: unverified** — `in_game_route_query-8ba52a10814e3585a7f7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-efc37b60abbb6d349aa8"></a>

**180° CCW: unverified** — `in_game_route_query-efc37b60abbb6d349aa8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_route_query-31ecbf7481215d41890d"></a>

**270° CCW: unverified** — `in_game_route_query-31ecbf7481215d41890d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-b22488a4e18858fc5be0"></a>

**0° CCW: unverified** — `in_game_route_query-b22488a4e18858fc5be0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-65075ea6d7ba3741647b"></a>

**90° CCW: unverified** — `in_game_route_query-65075ea6d7ba3741647b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-89cb36dd3621871c9954"></a>

**180° CCW: unverified** — `in_game_route_query-89cb36dd3621871c9954`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-9169d2062a63016e7f48"></a>

**270° CCW: unverified** — `in_game_route_query-9169d2062a63016e7f48`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out</summary>

<a id="case-in_game_route_query-c616a473fefd272719cc"></a>

**0° CCW: unverified** — `in_game_route_query-c616a473fefd272719cc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-12ed302c6a6a35c43e83"></a>

**90° CCW: unverified** — `in_game_route_query-12ed302c6a6a35c43e83`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-6266dcf948092007f3a3"></a>

**180° CCW: unverified** — `in_game_route_query-6266dcf948092007f3a3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_route_query-ebfe24b97097daa5c937"></a>

**270° CCW: unverified** — `in_game_route_query-ebfe24b97097daa5c937`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-757c82fed45f3a38f86c"></a>

**0° CCW: unverified** — `in_game_route_query-757c82fed45f3a38f86c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-4320ffbe46bc1872408c"></a>

**90° CCW: unverified** — `in_game_route_query-4320ffbe46bc1872408c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-8f3b662fbf307a96ddff"></a>

**180° CCW: unverified** — `in_game_route_query-8f3b662fbf307a96ddff`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-4baffeba1674a213d74e"></a>

**270° CCW: unverified** — `in_game_route_query-4baffeba1674a213d74e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out</summary>

<a id="case-in_game_route_query-7748ada03d4888a35c7a"></a>

**0° CCW: unverified** — `in_game_route_query-7748ada03d4888a35c7a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-f71d8afda3f571f6c3a3"></a>

**90° CCW: unverified** — `in_game_route_query-f71d8afda3f571f6c3a3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-f73537f77d792658f52f"></a>

**180° CCW: unverified** — `in_game_route_query-f73537f77d792658f52f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_route_query-d57c1e02af9de9279078"></a>

**270° CCW: unverified** — `in_game_route_query-d57c1e02af9de9279078`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out | — | <a href="#case-in_game_visible_travel-f1a985e02baf99cf2c04">[ ] unverified</a> | <a href="#case-in_game_visible_travel-78434a7a649f0335a881">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1d1c3a32a02293529d16">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9b9638ff685882e192df">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out | — | <a href="#case-in_game_visible_travel-0912c59dd2e19e4f84f8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8ba52a10814e3585a7f7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-efc37b60abbb6d349aa8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-31ecbf7481215d41890d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-b22488a4e18858fc5be0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-65075ea6d7ba3741647b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-89cb36dd3621871c9954">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9169d2062a63016e7f48">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out | — | <a href="#case-in_game_visible_travel-c616a473fefd272719cc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-12ed302c6a6a35c43e83">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6266dcf948092007f3a3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ebfe24b97097daa5c937">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-757c82fed45f3a38f86c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4320ffbe46bc1872408c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8f3b662fbf307a96ddff">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4baffeba1674a213d74e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out | — | <a href="#case-in_game_visible_travel-7748ada03d4888a35c7a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f71d8afda3f571f6c3a3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f73537f77d792658f52f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d57c1e02af9de9279078">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out</summary>

<a id="case-in_game_visible_travel-f1a985e02baf99cf2c04"></a>

**0° CCW: unverified** — `in_game_visible_travel-f1a985e02baf99cf2c04`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-78434a7a649f0335a881"></a>

**90° CCW: unverified** — `in_game_visible_travel-78434a7a649f0335a881`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-1d1c3a32a02293529d16"></a>

**180° CCW: unverified** — `in_game_visible_travel-1d1c3a32a02293529d16`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

<a id="case-in_game_visible_travel-9b9638ff685882e192df"></a>

**270° CCW: unverified** — `in_game_visible_travel-9b9638ff685882e192df`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-07-out; entry: channel-01-in; exit: channel-07-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out</summary>

<a id="case-in_game_visible_travel-0912c59dd2e19e4f84f8"></a>

**0° CCW: unverified** — `in_game_visible_travel-0912c59dd2e19e4f84f8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-8ba52a10814e3585a7f7"></a>

**90° CCW: unverified** — `in_game_visible_travel-8ba52a10814e3585a7f7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-efc37b60abbb6d349aa8"></a>

**180° CCW: unverified** — `in_game_visible_travel-efc37b60abbb6d349aa8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

<a id="case-in_game_visible_travel-31ecbf7481215d41890d"></a>

**270° CCW: unverified** — `in_game_visible_travel-31ecbf7481215d41890d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-09-out; entry: channel-01-in; exit: channel-09-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-b22488a4e18858fc5be0"></a>

**0° CCW: unverified** — `in_game_visible_travel-b22488a4e18858fc5be0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-65075ea6d7ba3741647b"></a>

**90° CCW: unverified** — `in_game_visible_travel-65075ea6d7ba3741647b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-89cb36dd3621871c9954"></a>

**180° CCW: unverified** — `in_game_visible_travel-89cb36dd3621871c9954`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-9169d2062a63016e7f48"></a>

**270° CCW: unverified** — `in_game_visible_travel-9169d2062a63016e7f48`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out</summary>

<a id="case-in_game_visible_travel-c616a473fefd272719cc"></a>

**0° CCW: unverified** — `in_game_visible_travel-c616a473fefd272719cc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-12ed302c6a6a35c43e83"></a>

**90° CCW: unverified** — `in_game_visible_travel-12ed302c6a6a35c43e83`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-6266dcf948092007f3a3"></a>

**180° CCW: unverified** — `in_game_visible_travel-6266dcf948092007f3a3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

<a id="case-in_game_visible_travel-ebfe24b97097daa5c937"></a>

**270° CCW: unverified** — `in_game_visible_travel-ebfe24b97097daa5c937`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-06-out; entry: channel-03-in; exit: channel-06-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-757c82fed45f3a38f86c"></a>

**0° CCW: unverified** — `in_game_visible_travel-757c82fed45f3a38f86c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-4320ffbe46bc1872408c"></a>

**90° CCW: unverified** — `in_game_visible_travel-4320ffbe46bc1872408c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-8f3b662fbf307a96ddff"></a>

**180° CCW: unverified** — `in_game_visible_travel-8f3b662fbf307a96ddff`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-4baffeba1674a213d74e"></a>

**270° CCW: unverified** — `in_game_visible_travel-4baffeba1674a213d74e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-08-out; entry: channel-04-in; exit: channel-08-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out</summary>

<a id="case-in_game_visible_travel-7748ada03d4888a35c7a"></a>

**0° CCW: unverified** — `in_game_visible_travel-7748ada03d4888a35c7a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-f71d8afda3f571f6c3a3"></a>

**90° CCW: unverified** — `in_game_visible_travel-f71d8afda3f571f6c3a3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-f73537f77d792658f52f"></a>

**180° CCW: unverified** — `in_game_visible_travel-f73537f77d792658f52f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

<a id="case-in_game_visible_travel-d57c1e02af9de9279078"></a>

**270° CCW: unverified** — `in_game_visible_travel-d57c1e02af9de9279078`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-08-out; entry: channel-05-in; exit: channel-08-out.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-a59e06a507334b9b0e44">[ ] unverified</a> | <a href="#case-in_game_route_query-151c2aa7e484160c22e8">[ ] unverified</a> | <a href="#case-in_game_route_query-bbef19e409d4123f5626">[ ] unverified</a> | <a href="#case-in_game_route_query-b40b84caeff21b3ee3a0">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-6c4a479f93e3cb4f5e96">[ ] unverified</a> | <a href="#case-in_game_route_query-0c902c67c127b9de6ca1">[ ] unverified</a> | <a href="#case-in_game_route_query-5d146aebe143a27c3b74">[ ] unverified</a> | <a href="#case-in_game_route_query-a45872672c19a8949470">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-a59e06a507334b9b0e44"></a>

**0° CCW: unverified** — `in_game_route_query-a59e06a507334b9b0e44`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-151c2aa7e484160c22e8"></a>

**90° CCW: unverified** — `in_game_route_query-151c2aa7e484160c22e8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-bbef19e409d4123f5626"></a>

**180° CCW: unverified** — `in_game_route_query-bbef19e409d4123f5626`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-b40b84caeff21b3ee3a0"></a>

**270° CCW: unverified** — `in_game_route_query-b40b84caeff21b3ee3a0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-6c4a479f93e3cb4f5e96"></a>

**0° CCW: unverified** — `in_game_route_query-6c4a479f93e3cb4f5e96`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-0c902c67c127b9de6ca1"></a>

**90° CCW: unverified** — `in_game_route_query-0c902c67c127b9de6ca1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-5d146aebe143a27c3b74"></a>

**180° CCW: unverified** — `in_game_route_query-5d146aebe143a27c3b74`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-a45872672c19a8949470"></a>

**270° CCW: unverified** — `in_game_route_query-a45872672c19a8949470`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-a59e06a507334b9b0e44">[ ] unverified</a> | <a href="#case-in_game_visible_travel-151c2aa7e484160c22e8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bbef19e409d4123f5626">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b40b84caeff21b3ee3a0">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-6c4a479f93e3cb4f5e96">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0c902c67c127b9de6ca1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5d146aebe143a27c3b74">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a45872672c19a8949470">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-a59e06a507334b9b0e44"></a>

**0° CCW: unverified** — `in_game_visible_travel-a59e06a507334b9b0e44`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-151c2aa7e484160c22e8"></a>

**90° CCW: unverified** — `in_game_visible_travel-151c2aa7e484160c22e8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-bbef19e409d4123f5626"></a>

**180° CCW: unverified** — `in_game_visible_travel-bbef19e409d4123f5626`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-b40b84caeff21b3ee3a0"></a>

**270° CCW: unverified** — `in_game_visible_travel-b40b84caeff21b3ee3a0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-11-in>channel-14-out; entry: channel-11-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-6c4a479f93e3cb4f5e96"></a>

**0° CCW: unverified** — `in_game_visible_travel-6c4a479f93e3cb4f5e96`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-0c902c67c127b9de6ca1"></a>

**90° CCW: unverified** — `in_game_visible_travel-0c902c67c127b9de6ca1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-5d146aebe143a27c3b74"></a>

**180° CCW: unverified** — `in_game_visible_travel-5d146aebe143a27c3b74`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-a45872672c19a8949470"></a>

**270° CCW: unverified** — `in_game_visible_travel-a45872672c19a8949470`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-12-in>channel-13-out; entry: channel-12-in; exit: channel-13-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 76 cases; unverified: 76</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-88adf1d10e409b71703c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e473384c726dc61f18bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a86fb6433df9c08cbb4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f8077c64bf7ea78cf02">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c9b86c7368ec94764ca9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5190b4b94fa4ad7b1ef9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd92b65681a0c03400fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7db4a03493ac5ea93175">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7a47db55578fcc3f69a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57b08360bf8cbbada7ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f12f27178d5d5a20ca9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45737d73e43ddb1e6f9d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eac8f1216df59858bc08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f12090d794165c166256">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0a04eda748eb6fe89e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9534c14cb1b54f8393fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3ceb87d8baebfa265b10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40ab77742b2e43b475c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3439b4b2133ce40e40a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6bd0a3233484d8b17fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a03cf734c41a215c0af2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3dbb5f6e75390573cff0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-236569f9690b3ced8b8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86f26dd7ac3b0c1f0cc6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93bfa912fd79e86d34f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12a77c0be63016a51c07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2f94e74299a7093c7b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b74952dd04a3812fda7d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e9505f457944463710e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cffb67004835275f77d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1cde61ebe8b99ceaa91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-448aaeb4acf456b7aa07">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9508e6366cca99b2f907">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d49ef691abf509979893">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7073f248474beecf5b06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5adb6f977b5569ba8114">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b41db4dfec76bdc55871">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06129f2ef2a92da62c01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fad3ae641db10a4e42d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77bff8ff6fd49bc4ff2a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fe5187ec4a841d9f3447">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e65f367bb6750039765b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-656d765a02b817b3ee2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-301285e6a7bfd315ba1c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d5be1207b3b397d25c4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-273804d0dd1b45249e9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ae9bda845520c0b85d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a971c3b96f979acb4b83">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93546c578dec5832ce87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d432eff42e0c042de0d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-018667cc587e3a0d8492">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-216b6de0fd38ca4c4205">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5b64b500a41a08319b64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50900a9327351153b35f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ba69c1974d24f92fcc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0693cf7d61c64a6494f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a8ea72cb097ddc0ab6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6691aefa83c206794419">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01d23510cdb404da252e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6adddec0940daebfa84">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-066437f1269f598e56f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01908ed5c119bf47e33f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1b103756c52491b595b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8a265bdff3d8fc9b272">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dab666cb41e67c3c5488">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00123fc76a7e6688e84c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8695fad07163182605e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f59e30e0e714a15d44e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-184fb48f711ce372a4d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4aa077261d88d9fa64d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3388d9a56cecd99acf99">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ecb0d1d692091e0e70b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8204b71799bb9ce925cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9302ae18b15f8449b74a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f14ede3dc5e9fdb2bee2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03bf4458de5fff2d3f42">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-88adf1d10e409b71703c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-88adf1d10e409b71703c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e473384c726dc61f18bd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e473384c726dc61f18bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a86fb6433df9c08cbb4f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a86fb6433df9c08cbb4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f8077c64bf7ea78cf02"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3f8077c64bf7ea78cf02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c9b86c7368ec94764ca9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c9b86c7368ec94764ca9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5190b4b94fa4ad7b1ef9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5190b4b94fa4ad7b1ef9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd92b65681a0c03400fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dd92b65681a0c03400fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7db4a03493ac5ea93175"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7db4a03493ac5ea93175`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7a47db55578fcc3f69a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7a47db55578fcc3f69a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57b08360bf8cbbada7ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-57b08360bf8cbbada7ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f12f27178d5d5a20ca9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2f12f27178d5d5a20ca9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45737d73e43ddb1e6f9d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45737d73e43ddb1e6f9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eac8f1216df59858bc08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eac8f1216df59858bc08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f12090d794165c166256"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f12090d794165c166256`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0a04eda748eb6fe89e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b0a04eda748eb6fe89e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9534c14cb1b54f8393fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9534c14cb1b54f8393fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3ceb87d8baebfa265b10"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3ceb87d8baebfa265b10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40ab77742b2e43b475c5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-40ab77742b2e43b475c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3439b4b2133ce40e40a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3439b4b2133ce40e40a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6bd0a3233484d8b17fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6bd0a3233484d8b17fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a03cf734c41a215c0af2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a03cf734c41a215c0af2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3dbb5f6e75390573cff0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3dbb5f6e75390573cff0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-236569f9690b3ced8b8a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-236569f9690b3ced8b8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86f26dd7ac3b0c1f0cc6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-86f26dd7ac3b0c1f0cc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93bfa912fd79e86d34f2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93bfa912fd79e86d34f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12a77c0be63016a51c07"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-12a77c0be63016a51c07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2f94e74299a7093c7b3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2f94e74299a7093c7b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b74952dd04a3812fda7d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b74952dd04a3812fda7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e9505f457944463710e5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e9505f457944463710e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cffb67004835275f77d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4cffb67004835275f77d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1cde61ebe8b99ceaa91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e1cde61ebe8b99ceaa91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-448aaeb4acf456b7aa07"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-448aaeb4acf456b7aa07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9508e6366cca99b2f907"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9508e6366cca99b2f907`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d49ef691abf509979893"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d49ef691abf509979893`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7073f248474beecf5b06"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7073f248474beecf5b06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5adb6f977b5569ba8114"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5adb6f977b5569ba8114`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-08-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b41db4dfec76bdc55871"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b41db4dfec76bdc55871`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06129f2ef2a92da62c01"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-06129f2ef2a92da62c01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fad3ae641db10a4e42d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0fad3ae641db10a4e42d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77bff8ff6fd49bc4ff2a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77bff8ff6fd49bc4ff2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fe5187ec4a841d9f3447"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fe5187ec4a841d9f3447`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e65f367bb6750039765b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e65f367bb6750039765b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-656d765a02b817b3ee2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-656d765a02b817b3ee2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-301285e6a7bfd315ba1c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-301285e6a7bfd315ba1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d5be1207b3b397d25c4a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d5be1207b3b397d25c4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-273804d0dd1b45249e9a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-273804d0dd1b45249e9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ae9bda845520c0b85d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ae9bda845520c0b85d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a971c3b96f979acb4b83"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a971c3b96f979acb4b83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93546c578dec5832ce87"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93546c578dec5832ce87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d432eff42e0c042de0d9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d432eff42e0c042de0d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-018667cc587e3a0d8492"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-018667cc587e3a0d8492`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-216b6de0fd38ca4c4205"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-216b6de0fd38ca4c4205`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5b64b500a41a08319b64"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5b64b500a41a08319b64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50900a9327351153b35f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-50900a9327351153b35f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ba69c1974d24f92fcc9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ba69c1974d24f92fcc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0693cf7d61c64a6494f8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0693cf7d61c64a6494f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a8ea72cb097ddc0ab6b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a8ea72cb097ddc0ab6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6691aefa83c206794419"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6691aefa83c206794419`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01d23510cdb404da252e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-01d23510cdb404da252e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6adddec0940daebfa84"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b6adddec0940daebfa84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-066437f1269f598e56f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-066437f1269f598e56f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01908ed5c119bf47e33f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-01908ed5c119bf47e33f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1b103756c52491b595b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f1b103756c52491b595b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8a265bdff3d8fc9b272"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e8a265bdff3d8fc9b272`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-06-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dab666cb41e67c3c5488"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dab666cb41e67c3c5488`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00123fc76a7e6688e84c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00123fc76a7e6688e84c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8695fad07163182605e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8695fad07163182605e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f59e30e0e714a15d44e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f59e30e0e714a15d44e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-07-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-184fb48f711ce372a4d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-184fb48f711ce372a4d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4aa077261d88d9fa64d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4aa077261d88d9fa64d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3388d9a56cecd99acf99"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3388d9a56cecd99acf99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ecb0d1d692091e0e70b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8ecb0d1d692091e0e70b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-09-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8204b71799bb9ce925cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8204b71799bb9ce925cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9302ae18b15f8449b74a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9302ae18b15f8449b74a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f14ede3dc5e9fdb2bee2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f14ede3dc5e9fdb2bee2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03bf4458de5fff2d3f42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03bf4458de5fff2d3f42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32faeca94d2b625ca9b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5a6ac4d78642864a2da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-912280e0ce9be2bb8afe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edc5716e28ed38358803">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1484c5c0f687a9a68de9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dcb9661429e2fe6bbba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e2210d8164142cbf498">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1213e0e7f4e230c2e57a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3fa57168b1afda01ab8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7da1fda5dd679e4ddaba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b35a137b4e92be677000">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18e35a7ed7bef2a3816a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d7ffa77e72935ec2ac9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d0d2b62a9b5261d1f86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fda3de2dc48cb604ab7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85550234bf9396566ce7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a0d903472d25b03505af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b03f1892c7fe3178f6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b7bb1b03a46725af012">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-466b7bf9111631c4bfcf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a7130a951b3129a2539a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-621e9bdc79b524be3d86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a958a98030dc2f0cbea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09322afd3efff5a57fd9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e754535de867f195bd1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8be493875f2e216a8140">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c2e66bf8348c3f282be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c407f8e3e1fff1389e2e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e4059c453cc5e7f96b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-294560aead6a3b8738eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e74aca7d4c8cb0f439fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac8505e95198af435013">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ae31cb9868fb5df6e9e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb786377f37cde9b0e4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9be13657b5472aa20a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e7b96f71e35f0c17c0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2614e05187ab014fe037">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce9fc4284b440c85afa2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7be2fc0493874c02d330">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d44932ab86405422f84f">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32faeca94d2b625ca9b6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32faeca94d2b625ca9b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5a6ac4d78642864a2da"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d5a6ac4d78642864a2da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-912280e0ce9be2bb8afe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-912280e0ce9be2bb8afe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edc5716e28ed38358803"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-edc5716e28ed38358803`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1484c5c0f687a9a68de9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1484c5c0f687a9a68de9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dcb9661429e2fe6bbba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0dcb9661429e2fe6bbba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e2210d8164142cbf498"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3e2210d8164142cbf498`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1213e0e7f4e230c2e57a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1213e0e7f4e230c2e57a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3fa57168b1afda01ab8b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3fa57168b1afda01ab8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7da1fda5dd679e4ddaba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7da1fda5dd679e4ddaba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b35a137b4e92be677000"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b35a137b4e92be677000`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18e35a7ed7bef2a3816a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-18e35a7ed7bef2a3816a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d7ffa77e72935ec2ac9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d7ffa77e72935ec2ac9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d0d2b62a9b5261d1f86"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d0d2b62a9b5261d1f86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fda3de2dc48cb604ab7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0fda3de2dc48cb604ab7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85550234bf9396566ce7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-85550234bf9396566ce7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a0d903472d25b03505af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a0d903472d25b03505af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b03f1892c7fe3178f6c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b03f1892c7fe3178f6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b7bb1b03a46725af012"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9b7bb1b03a46725af012`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-466b7bf9111631c4bfcf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-466b7bf9111631c4bfcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a7130a951b3129a2539a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a7130a951b3129a2539a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-621e9bdc79b524be3d86"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-621e9bdc79b524be3d86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a958a98030dc2f0cbea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a958a98030dc2f0cbea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09322afd3efff5a57fd9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-09322afd3efff5a57fd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e754535de867f195bd1e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e754535de867f195bd1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8be493875f2e216a8140"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8be493875f2e216a8140`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c2e66bf8348c3f282be"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c2e66bf8348c3f282be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c407f8e3e1fff1389e2e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c407f8e3e1fff1389e2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9e4059c453cc5e7f96b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e4059c453cc5e7f96b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-294560aead6a3b8738eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-294560aead6a3b8738eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e74aca7d4c8cb0f439fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e74aca7d4c8cb0f439fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac8505e95198af435013"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac8505e95198af435013`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ae31cb9868fb5df6e9e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ae31cb9868fb5df6e9e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb786377f37cde9b0e4a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bb786377f37cde9b0e4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9be13657b5472aa20a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a9be13657b5472aa20a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e7b96f71e35f0c17c0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1e7b96f71e35f0c17c0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2614e05187ab014fe037"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2614e05187ab014fe037`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce9fc4284b440c85afa2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce9fc4284b440c85afa2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7be2fc0493874c02d330"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7be2fc0493874c02d330`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d44932ab86405422f84f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d44932ab86405422f84f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-81cb624a037ffe649e89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1645e0ba159b3dcfb85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbb40f4478572e72a846">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d038d9ce4647f83c08d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-40ccc7492c0198ef859c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0eb7f029a1dd4468576">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9b9f73d0c867fcab417">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5117c9ec95c6a5042868">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35b27a1a52db576dab7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61fe941c08ed966a6015">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cba026eba1b91ca5b0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bd5f2f046b7fd66376c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a537c2777e75e34478bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c72889f47ed3e0f9af26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cba8f80b3a9245e1160">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-253e6cfde255915a7868">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-30b8419ddc16249a4611">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c75c358daed091d4b41c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad71b81f7724341db2a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6f4aa909eab49eaeb86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7274c25e674a2d91f231">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f13d1f17fa52f7c3da9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-728d8cd1753ba962335c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6e59aa0a8810c7310f3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a7af6a727d59ac040b3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eddc6fd380f87c1208f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96c60fb8414ab9dbc7fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e672dee2ecff82d09d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3cac43f7d10f6daf961a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-254a93d4400eee0654a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eaaeb802100e8f08048b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27398dc13c86ae93d51e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fefefb234a9d28e2dc5b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fb2fef82b9307e6f135">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c99b94a1b2253f7aed1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-220412563669e98f53e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e975447c99360e9d119a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a2402cd9e52d3d5faae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c8d056ff997cde76f30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed3a9521fc405c2236f5">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-81cb624a037ffe649e89"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81cb624a037ffe649e89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1645e0ba159b3dcfb85"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c1645e0ba159b3dcfb85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbb40f4478572e72a846"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fbb40f4478572e72a846`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d038d9ce4647f83c08d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d038d9ce4647f83c08d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-40ccc7492c0198ef859c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-40ccc7492c0198ef859c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0eb7f029a1dd4468576"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0eb7f029a1dd4468576`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9b9f73d0c867fcab417"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9b9f73d0c867fcab417`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5117c9ec95c6a5042868"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5117c9ec95c6a5042868`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35b27a1a52db576dab7d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35b27a1a52db576dab7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61fe941c08ed966a6015"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-61fe941c08ed966a6015`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cba026eba1b91ca5b0a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1cba026eba1b91ca5b0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bd5f2f046b7fd66376c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9bd5f2f046b7fd66376c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a537c2777e75e34478bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a537c2777e75e34478bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c72889f47ed3e0f9af26"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c72889f47ed3e0f9af26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cba8f80b3a9245e1160"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6cba8f80b3a9245e1160`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-253e6cfde255915a7868"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-253e6cfde255915a7868`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-30b8419ddc16249a4611"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-30b8419ddc16249a4611`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c75c358daed091d4b41c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c75c358daed091d4b41c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad71b81f7724341db2a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ad71b81f7724341db2a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6f4aa909eab49eaeb86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6f4aa909eab49eaeb86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7274c25e674a2d91f231"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7274c25e674a2d91f231`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f13d1f17fa52f7c3da9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f13d1f17fa52f7c3da9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-728d8cd1753ba962335c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-728d8cd1753ba962335c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6e59aa0a8810c7310f3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a6e59aa0a8810c7310f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-06-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a7af6a727d59ac040b3f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a7af6a727d59ac040b3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eddc6fd380f87c1208f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eddc6fd380f87c1208f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96c60fb8414ab9dbc7fa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-96c60fb8414ab9dbc7fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e672dee2ecff82d09d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e672dee2ecff82d09d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-07-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3cac43f7d10f6daf961a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3cac43f7d10f6daf961a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-254a93d4400eee0654a5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-254a93d4400eee0654a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eaaeb802100e8f08048b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eaaeb802100e8f08048b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27398dc13c86ae93d51e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27398dc13c86ae93d51e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-08-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fefefb234a9d28e2dc5b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fefefb234a9d28e2dc5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fb2fef82b9307e6f135"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5fb2fef82b9307e6f135`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c99b94a1b2253f7aed1a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c99b94a1b2253f7aed1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-220412563669e98f53e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-220412563669e98f53e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-09-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e975447c99360e9d119a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e975447c99360e9d119a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a2402cd9e52d3d5faae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4a2402cd9e52d3d5faae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c8d056ff997cde76f30"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6c8d056ff997cde76f30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed3a9521fc405c2236f5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed3a9521fc405c2236f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-10-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4b9a96331cbb3f95d232">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28bb59050a3c7b955192">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0cfd91cfa6eedb09377c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ace1521cd5e42350e211">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bed24ece32a5f8c8d64f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1abc3d247219195909a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ab7f6e40930d5e7b2bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9611bd73c5be7d5c8ed0">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4b9a96331cbb3f95d232"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4b9a96331cbb3f95d232`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28bb59050a3c7b955192"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-28bb59050a3c7b955192`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0cfd91cfa6eedb09377c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0cfd91cfa6eedb09377c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ace1521cd5e42350e211"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ace1521cd5e42350e211`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-13-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bed24ece32a5f8c8d64f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bed24ece32a5f8c8d64f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1abc3d247219195909a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e1abc3d247219195909a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ab7f6e40930d5e7b2bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ab7f6e40930d5e7b2bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9611bd73c5be7d5c8ed0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9611bd73c5be7d5c8ed0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-14-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrowed terminal asphalt while preserving the 6 m grade interfaces and its saved traffic routes. The later slip-lane revision lengthens the shoulder treatment and changes its access PATHs and white markings, while retaining all fifteen permanent types, the 31-cell union, and those narrow ground mouths. The earlier `ddrhw-parallel-diamond-parts-01` and `ddrhw-parallel-diamond-pedestrian-mouths-01` build identities retain their original scopes. The current revision uses `ddrhw-parallel-diamond-slip-lanes-02`; only its own matching saved-resource report can establish its software result.
