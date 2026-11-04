---
title: "Testing: DD RHW-4 — Orthogonal Y Connection Core — L1/L2"
summary: "Verify the exact Y-junction component, its native socket, its saved resources, and its separate human game observations."
audience: "Contributors and testers"
document_type: "reference"
---

# Testing: DD RHW-4 — Orthogonal Y Connection Core — L1/L2

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This document covers `ddrhw-y-orthogonal-core`, the **east branch and centre band** component of the [compact DD RHW Y junction](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md). Its scope includes 5 owned cells in a 5 × 1-tile rectangle, their full models and traffic fragments, and one separate unowned native DD socket. The lower 7.5 m deck enters from the east, and the upper 15 m deck leaves toward the east. The exact owned mask and socket address are explained in the [piece placement guide](README.md#21-owned-cells-and-native-approach).

Check the two east upper outgoing lanes independently: one receives A→C, and the other receives B→C. The two lower incoming lanes must continue separately toward A and B. Also observe A→B and B→A through the centre band, without exchanging decks. Each external deck retains two same-direction native lanes. In the completed assembly, each of the six arm-to-arm movements uses one lane. No authored journey permits a U-turn, travel against an external deck’s direction, or an arbitrary switch between opposing deck services. Internal module cuts can expose several routes at different heights; consult the measured connections below instead of treating one endpoint as the complete boundary.

Require all four proper placement rotations, both diagonal traffic directions where present, and separate camera rotations. A source calculation, a rendered model, a coloured Route Query line, and an observed moving car establish different facts. Only a matching human observation can pass a game case.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `b-a-out` | road / 1 / primary | out | [6.332766, -8.0, 7.5]; [-0.2572557340982241, -0.9663433588914366]; 0.0 | `path-interface-248f7bfc0338ffae18d4` |
| `a-b-in` | road / 1 / primary | in | [6.332766, -8.0, 15.0]; [0.2572557340982241, 0.9663433588914366]; 0.0 | `path-interface-c34990f0463212897200` |
| `b-a-in` | road / 1 / primary | in | [6.332766, 8.0, 7.5]; [0.2572557340982241, -0.9663433588914366]; 0.0 | `path-interface-90ec3d32f6aca0b2bd9d` |
| `a-b-out` | road / 1 / primary | out | [6.332766, 8.0, 15.0]; [-0.2572557340982241, 0.9663433588914366]; 0.0 | `path-interface-1406061631c7ec05d39a` |
| `c-b-out` | road / 1 / primary | out | [23.700047, 8.0, 12.159544]; [-0.8923143757368847, 0.45141450447819453]; 0.248976792 | `path-interface-9d95f94d02139a7871b0` |
| `c-a-out` | road / 1 / primary | out | [37.321807, -8.0, 7.5]; [-0.9475295413188497, -0.31966821601168016]; 0.0 | `path-interface-58ff10c976f8cd198ffb` |
| `a-c-in` | road / 1 / primary | in | [37.321807, -8.0, 15.0]; [0.9475295413188497, 0.31966821601168016]; 0.0 | `path-interface-96b79c79f51bfeae1ef8` |
| `b-c-in` | road / 1 / primary | in | [46.247886, 8.0, 14.711544]; [0.8870803546319371, -0.4616150392113289]; 0.085894367 | `path-interface-927eefb98159e68726cc` |
| `c-a-in` | road / 1 / primary | in | [72.0, -2.5, 7.5]; [-1.0, 0.0]; 0.0 | `path-interface-00480ef66d1c683adb2c` |
| `a-c-out` | road / 1 / primary | out | [72.0, -2.5, 15.0]; [1.0, 0.0]; 0.0 | `path-interface-aef756dec28195473947` |
| `c-b-in` | road / 1 / primary | in | [72.0, 2.5, 7.5]; [-1.0, 0.0]; 0.0 | `path-interface-28cd03e10e6e40a3c0fa` |
| `b-c-out` | road / 1 / primary | out | [72.0, 2.5, 15.0]; [1.0, 0.0]; 0.0 | `path-interface-c5c8334a7156c02c488c` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `a-b-in` → `a-b-out` | primary |
| road | `b-a-in` → `b-a-out` | primary |
| road | `a-c-in` → `a-c-out` | primary |
| road | `b-c-in` → `b-c-out` | primary |
| road | `c-a-in` → `c-a-out` | primary |
| road | `c-b-in` → `c-b-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `a-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Prepare the audited NAM 50 right-hand-traffic profile through the [shared build and input guide](../../../../docs/BUILD_AND_INSTALL.md). The definition requires the native controller, DD RHW-4, RHW core, and MIS inputs listed in [piece.jsonc](piece.jsonc). Record the actual SimCity 4 version, NAM version, traffic handedness, operating system, compatibility layer if used, and installed build identity.
2. Verify the exact build intended for a deliberate installation before copying it into the game. Close the game completely during installation. Restart it, open a disposable flat city, and place new copies; a previously placed experimental object is not the fresh-placement control for a changed construction, model, or PATH revision.
3. For complete journeys, install all three Y components together and follow the [assembly placement table](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md#3-placements). This component is **P03**, with source reference **(-1, 0)** in world `(column,row)` addresses. Its displayed assembly reference is **(X1, Y3)**. Read those as coordinate references, not a verified mouse-cursor anchor.
4. Keep the native socket and the repeating native approach available. The next outward native cell is local (6,0), followed by the same straight row. Keep that eastward continuation clear. Prepare a separate working native DD control using the ordinary DD starter and **RealHighway (RHW-2)** before judging a failed connection against the custom construction.
5. Connect the completed junction to occupied development and useful destinations on all three arms, run the simulation, and confirm moving traffic on the native controls. Demand for only one destination cannot demonstrate the other five allowed journeys.

## 3. Software checks

### 3.1 Source and native contracts

The [native input measurements](../../01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/native-design-inputs.jsonc) pin the original lane classes, heights, models, and controller resources. The [centreline source verification](../../01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/source-verification.jsonc) checks the six reviewed source journeys. Those reports retain their historical source scope. The later ordinary `dist/ddrhw-y-junction-native` build passed saved-resource verification and the whole-assembly physical check; installation and human game observations remain unverified.

A **PATH** resource stores directed traffic routes, while an **S3D** resource stores a visible model. **UV coordinates** identify which part of a texture image appears at each model point.

**RUL1** contains rules that resolve construction markers into a native network tile. **RUL2** contains rules for continuing ordinary draggable networks. A network **exemplar** is metadata linking a resolved tile to its native model.

Its reviewed orthogonal socket uses native `57530000` at pose 3. Four original orthogonal DD RUL1 rows are reused, and no orthogonal solution is inserted. Three pinned dependencies cover its original model, PATH, and network exemplar. The combined three-component selection additionally inserts four diagonal rows and protects nine native resources in total. The [native socket adapter](../../implementation/scp_highway/y_junction_approaches.py) checks all four proper rotations, flat three-metre collars, actual lane classes and compatibility fields, and the original inward and outward continuation states without replacing native RUL2. The ordinary build also passed this component’s actual saved native-boundary check; fixture and original-input tests retain their separate scope.

The [physical source](../../implementation/scp_highway/y_junction_geometry.py) and [whole-cell layout](../../implementation/scp_highway/y_junction_layout.py) compiled this component. Independent checks passed its actual emitted PATHs, models, construction fields, all five zooms, support geometry, and saved preview, followed by the complete assembly’s physical check. The [accepted connector contract](checks/accepted-connector-contract.jsonc) binds the checked ordinary build and canonical PATH fingerprints. Exact finite native profiles, inherited interior faces, and measured overhang are governed by the [assembly’s software-check scopes](../../01_assemblies/ddrhw-compact-diagonal-y-junction/TESTING.md#3-software-checks).

Its source maximum grade is approximately 25.7614%, below the declared 30% experimental limit. Some internal fragments are graded between 7.5 m and 15 m, even though both lanes are level where they meet the ordinary east DD socket. A **grade** is vertical change divided by horizontal route length; a 20% grade gains 2 m over 10 m horizontally. Actual saved PATHs passed the independent 30% grade ceiling and retain `UseElevation=1` for their authored heights. The declared car envelope is 2.5 m wide × 3.8 m high; software clearance against that envelope is not a structural-capacity calculation or a guarantee for every vehicle replacement.

### 3.2 Reproduce the checks

Run these commands from the repository root. Replace `BUILD_NAME` with a new descriptive reproduction-folder name. The first command writes a standalone build of this component; use the [assembly’s full-selection procedure](../../01_assemblies/ddrhw-compact-diagonal-y-junction/TESTING.md#3-software-checks) to reproduce the checked three-component build and whole-junction verification. `verify` reads that same saved build. None of these commands installs the result. Use `python` instead of `python3` inside an activated Windows Python environment.

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-y-orthogonal-core --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-y-orthogonal-core --build dist/BUILD_NAME
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-y-orthogonal-core
python3 -B tools/run_tests.py
```

The configured verification run passed **51 focused Y regression tests without skips**. To reproduce the focused family, run `python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p 'test_y_junction*.py'`. To isolate native-helper controls, use the pattern `test_y_junction_approaches.py`. Original-input tests may skip in another environment when proprietary NAM inputs are unavailable; report those skips explicitly. The [accepted connector contract](checks/accepted-connector-contract.jsonc) records the checked build identity and canonical PATH fingerprints. A document-layout result and a human game observation retain their own scopes.

## 4. Game checks

### 4.1 Placement and native construction

1. Follow [README placement](README.md#22-place-the-component), using the exact component name and complete owned-cell pattern. Inspect every owned tile, including model-only shoulders and supports. Leave native socket **(5,0)** unowned, and record whether the expected ordinary DD tile is actually seeded there.
2. Select **RealHighway (RHW-2)**, start at that native socket, and drag at least three tiles toward the **east**. Inspect the full staggered pattern for a diagonal approach, or the straight row for an orthogonal approach. Record whether the native network retains both heights and correct directions.
3. At a second site, make a working native approach first, leave a short straight gap, place a fresh component at the planned reference, and drag from the existing line inward to its native socket. Stop outside the fixed owned tiles. At a third site, place beside an already completed matching native approach. Record these construction orders independently.
4. Repeat at 90°, 180°, and 270° using **Home** and **End**. Check that model, owned cells, unowned native socket, native continuation, and preview rotate together. Record actual mouse-cursor alignment separately from the source reference; do not replace the source reference with the first visible custom road tile.

### 4.2 Routes and visible cars

1. Assemble all three pieces at the exact references, connect the three native approaches to development and destinations, and run the simulation. Confirm the native control traffic still works.
2. Use **Route Query** to inspect the component’s generated allowed journeys and the six whole-junction directions. Record each displayed route separately from visible movement.
3. Check the two east upper outgoing lanes independently: one receives A→C, and the other receives B→C. The two lower incoming lanes must continue separately toward A and B. Also observe A→B and B→A through the centre band, without exchanging decks. Follow actual cars from native approach to native approach, checking every module seam and both deck levels. Record the exact journey, placement rotation, and tile where a car stops, disappears, jumps in height, or clips a barrier or support.
4. Check that A→A, B→B, and C→C remain unavailable in the complete layout. Also inspect the component’s generated forbidden transfers. A missing observation stays unverified; it does not establish either a pass or a failure.

### 4.3 Appearance, shadows, and lifetime

1. Inspect all five zoom levels and all four city-camera views. Check native pavement and lane markings, finite shoulder joins, barriers, deck bodies, and supports. Camera rotation is a separate check from rotating the placed piece.
2. Inspect Medium and High game-shadow settings. The custom components intentionally disable cast shadows. Record detached triangles, residual shadows, or phantom geometry separately from the ordinary native approaches’ own appearance.
3. Save the disposable city, quit fully, reopen it, and repeat a permitted journey, native redraw, and height check. Demolish the component, inspect the former owned cells and unowned native socket separately, rebuild fresh copies, and repeat the journey.

Record only explicitly observed results through [the shared observation procedure](../../../../docs/TESTING.md). Earlier DD transitions, GHSR crossings, or diamond junctions do not pass this type’s cases.

## 5. Results and known issues

The ordinary **`dist/ddrhw-y-junction-native`** build passed this component’s saved PATH, model, and native-boundary verification, together with the whole-assembly physical check. All **21 canonical S3D/PATH pairs** across the three components have exactly the same file bytes as the accepted final UV snapshot. The configured focused Y run passed **51 tests without skips**. These results are bound to the actual saved build. At that capture, installation and all human game observations were unverified. The later [additive assembly installation](../../01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/additive-installation-20261103.jsonc) verifies that this component was added while all 225 existing piece files stayed in place unchanged. The user later reported **“okay good it works.”** for the original installed assembly; the [installation-linked general report](../../01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/human-general-operation-20261103.jsonc) preserves the exact statement. It does not confirm this component’s individual game cases or another variant, and generated case coverage remains unchanged.

No human placement, native-dragging, cursor-anchor, Route Query, visible-travel, game-rendering, demolition, or save/reload result is asserted here. The generated records below retain the recorded case states; software verification does not supply a missing human observation.

Only the first measured native alignment is supplied. Reflections and another adjacent grid phase are outside this implementation. Internal module cuts require the coordinated companion pieces, and ordinary highway dragging through owned cells is not an accepted construction method. Consult the [assembly’s software-check scopes](../../01_assemblies/ddrhw-compact-diagonal-y-junction/TESTING.md#3-software-checks) for the exact native-source, interior-face, and overhang cases retained by the physical verifier.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/24 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/24 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 189, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-y-orthogonal-core/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-y-orthogonal-core/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b5f3464132ecedeb9f50">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b5f3464132ecedeb9f50"></a>

**General: unverified** — `software_resources-b5f3464132ecedeb9f50`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b5f3464132ecedeb9f50">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b5f3464132ecedeb9f50"></a>

**General: unverified** — `software_connectivity-b5f3464132ecedeb9f50`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-7b47c61cd93d472d23bf">[ ] unverified</a> | <a href="#case-in_game_render-29c4acb0c7c5a6414bab">[ ] unverified</a> | <a href="#case-in_game_render-583b6c295e705b38ebc2">[ ] unverified</a> | <a href="#case-in_game_render-5390678d38536fd1500a">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-7b47c61cd93d472d23bf"></a>

**0° CCW: unverified** — `in_game_render-7b47c61cd93d472d23bf`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-29c4acb0c7c5a6414bab"></a>

**90° CCW: unverified** — `in_game_render-29c4acb0c7c5a6414bab`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-583b6c295e705b38ebc2"></a>

**180° CCW: unverified** — `in_game_render-583b6c295e705b38ebc2`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5390678d38536fd1500a"></a>

**270° CCW: unverified** — `in_game_render-5390678d38536fd1500a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-7b47c61cd93d472d23bf">[ ] unverified</a> | <a href="#case-in_game_placement-29c4acb0c7c5a6414bab">[ ] unverified</a> | <a href="#case-in_game_placement-583b6c295e705b38ebc2">[ ] unverified</a> | <a href="#case-in_game_placement-5390678d38536fd1500a">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-7b47c61cd93d472d23bf"></a>

**0° CCW: unverified** — `in_game_placement-7b47c61cd93d472d23bf`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-29c4acb0c7c5a6414bab"></a>

**90° CCW: unverified** — `in_game_placement-29c4acb0c7c5a6414bab`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-583b6c295e705b38ebc2"></a>

**180° CCW: unverified** — `in_game_placement-583b6c295e705b38ebc2`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5390678d38536fd1500a"></a>

**270° CCW: unverified** — `in_game_placement-5390678d38536fd1500a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-7b47c61cd93d472d23bf">[ ] unverified</a> | <a href="#case-in_game_demolition-29c4acb0c7c5a6414bab">[ ] unverified</a> | <a href="#case-in_game_demolition-583b6c295e705b38ebc2">[ ] unverified</a> | <a href="#case-in_game_demolition-5390678d38536fd1500a">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-7b47c61cd93d472d23bf"></a>

**0° CCW: unverified** — `in_game_demolition-7b47c61cd93d472d23bf`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-29c4acb0c7c5a6414bab"></a>

**90° CCW: unverified** — `in_game_demolition-29c4acb0c7c5a6414bab`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-583b6c295e705b38ebc2"></a>

**180° CCW: unverified** — `in_game_demolition-583b6c295e705b38ebc2`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5390678d38536fd1500a"></a>

**270° CCW: unverified** — `in_game_demolition-5390678d38536fd1500a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-7b47c61cd93d472d23bf">[ ] unverified</a> | <a href="#case-in_game_save_reload-29c4acb0c7c5a6414bab">[ ] unverified</a> | <a href="#case-in_game_save_reload-583b6c295e705b38ebc2">[ ] unverified</a> | <a href="#case-in_game_save_reload-5390678d38536fd1500a">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-7b47c61cd93d472d23bf"></a>

**0° CCW: unverified** — `in_game_save_reload-7b47c61cd93d472d23bf`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-29c4acb0c7c5a6414bab"></a>

**90° CCW: unverified** — `in_game_save_reload-29c4acb0c7c5a6414bab`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-583b6c295e705b38ebc2"></a>

**180° CCW: unverified** — `in_game_save_reload-583b6c295e705b38ebc2`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5390678d38536fd1500a"></a>

**270° CCW: unverified** — `in_game_save_reload-5390678d38536fd1500a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_route_query-ad3a62fb3abdf9bd32da">[ ] unverified</a> | <a href="#case-in_game_route_query-e8ca89d6cfc0a2949f30">[ ] unverified</a> | <a href="#case-in_game_route_query-2c66085f0410d97b2280">[ ] unverified</a> | <a href="#case-in_game_route_query-90a8fd9567a5804bd3b4">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_route_query-c00a9157f52df70eed63">[ ] unverified</a> | <a href="#case-in_game_route_query-8049f4be419c605f1ff1">[ ] unverified</a> | <a href="#case-in_game_route_query-8b209453f692c9263118">[ ] unverified</a> | <a href="#case-in_game_route_query-2ecc94c34154a053cf00">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out | — | <a href="#case-in_game_route_query-eff29eba74f513fffcf6">[ ] unverified</a> | <a href="#case-in_game_route_query-5338a1f155911648c2cd">[ ] unverified</a> | <a href="#case-in_game_route_query-ea1439b9e4ce95e40db6">[ ] unverified</a> | <a href="#case-in_game_route_query-4da1d7798913fae20467">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out | — | <a href="#case-in_game_route_query-d4ec97c3ec60731a7f8f">[ ] unverified</a> | <a href="#case-in_game_route_query-b799315a735ce40957ab">[ ] unverified</a> | <a href="#case-in_game_route_query-f590be0074b01b077146">[ ] unverified</a> | <a href="#case-in_game_route_query-3ec538c16d0ec71b4c17">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out | — | <a href="#case-in_game_route_query-fc3d67bfd91d39d5603e">[ ] unverified</a> | <a href="#case-in_game_route_query-33bb84f1969a566367f3">[ ] unverified</a> | <a href="#case-in_game_route_query-5b3de8cd4a32c22048b2">[ ] unverified</a> | <a href="#case-in_game_route_query-0f1c7a90c623bfa69cbb">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out | — | <a href="#case-in_game_route_query-dcc1d39b9b93f6ccba9d">[ ] unverified</a> | <a href="#case-in_game_route_query-65423f3f859b05f1af94">[ ] unverified</a> | <a href="#case-in_game_route_query-7edc251b32115ddbfad1">[ ] unverified</a> | <a href="#case-in_game_route_query-aba12684ac53adb33a34">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_route_query-ad3a62fb3abdf9bd32da"></a>

**0° CCW: unverified** — `in_game_route_query-ad3a62fb3abdf9bd32da`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-e8ca89d6cfc0a2949f30"></a>

**90° CCW: unverified** — `in_game_route_query-e8ca89d6cfc0a2949f30`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-2c66085f0410d97b2280"></a>

**180° CCW: unverified** — `in_game_route_query-2c66085f0410d97b2280`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-90a8fd9567a5804bd3b4"></a>

**270° CCW: unverified** — `in_game_route_query-90a8fd9567a5804bd3b4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_route_query-c00a9157f52df70eed63"></a>

**0° CCW: unverified** — `in_game_route_query-c00a9157f52df70eed63`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-8049f4be419c605f1ff1"></a>

**90° CCW: unverified** — `in_game_route_query-8049f4be419c605f1ff1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-8b209453f692c9263118"></a>

**180° CCW: unverified** — `in_game_route_query-8b209453f692c9263118`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-2ecc94c34154a053cf00"></a>

**270° CCW: unverified** — `in_game_route_query-2ecc94c34154a053cf00`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out</summary>

<a id="case-in_game_route_query-eff29eba74f513fffcf6"></a>

**0° CCW: unverified** — `in_game_route_query-eff29eba74f513fffcf6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-5338a1f155911648c2cd"></a>

**90° CCW: unverified** — `in_game_route_query-5338a1f155911648c2cd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-ea1439b9e4ce95e40db6"></a>

**180° CCW: unverified** — `in_game_route_query-ea1439b9e4ce95e40db6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-4da1d7798913fae20467"></a>

**270° CCW: unverified** — `in_game_route_query-4da1d7798913fae20467`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out</summary>

<a id="case-in_game_route_query-d4ec97c3ec60731a7f8f"></a>

**0° CCW: unverified** — `in_game_route_query-d4ec97c3ec60731a7f8f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-b799315a735ce40957ab"></a>

**90° CCW: unverified** — `in_game_route_query-b799315a735ce40957ab`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-f590be0074b01b077146"></a>

**180° CCW: unverified** — `in_game_route_query-f590be0074b01b077146`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-3ec538c16d0ec71b4c17"></a>

**270° CCW: unverified** — `in_game_route_query-3ec538c16d0ec71b4c17`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out</summary>

<a id="case-in_game_route_query-fc3d67bfd91d39d5603e"></a>

**0° CCW: unverified** — `in_game_route_query-fc3d67bfd91d39d5603e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-33bb84f1969a566367f3"></a>

**90° CCW: unverified** — `in_game_route_query-33bb84f1969a566367f3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-5b3de8cd4a32c22048b2"></a>

**180° CCW: unverified** — `in_game_route_query-5b3de8cd4a32c22048b2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-0f1c7a90c623bfa69cbb"></a>

**270° CCW: unverified** — `in_game_route_query-0f1c7a90c623bfa69cbb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out</summary>

<a id="case-in_game_route_query-dcc1d39b9b93f6ccba9d"></a>

**0° CCW: unverified** — `in_game_route_query-dcc1d39b9b93f6ccba9d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-65423f3f859b05f1af94"></a>

**90° CCW: unverified** — `in_game_route_query-65423f3f859b05f1af94`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-7edc251b32115ddbfad1"></a>

**180° CCW: unverified** — `in_game_route_query-7edc251b32115ddbfad1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-aba12684ac53adb33a34"></a>

**270° CCW: unverified** — `in_game_route_query-aba12684ac53adb33a34`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_visible_travel-ad3a62fb3abdf9bd32da">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e8ca89d6cfc0a2949f30">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2c66085f0410d97b2280">[ ] unverified</a> | <a href="#case-in_game_visible_travel-90a8fd9567a5804bd3b4">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_visible_travel-c00a9157f52df70eed63">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8049f4be419c605f1ff1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8b209453f692c9263118">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2ecc94c34154a053cf00">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out | — | <a href="#case-in_game_visible_travel-eff29eba74f513fffcf6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5338a1f155911648c2cd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ea1439b9e4ce95e40db6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4da1d7798913fae20467">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out | — | <a href="#case-in_game_visible_travel-d4ec97c3ec60731a7f8f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b799315a735ce40957ab">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f590be0074b01b077146">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3ec538c16d0ec71b4c17">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out | — | <a href="#case-in_game_visible_travel-fc3d67bfd91d39d5603e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-33bb84f1969a566367f3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5b3de8cd4a32c22048b2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0f1c7a90c623bfa69cbb">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out | — | <a href="#case-in_game_visible_travel-dcc1d39b9b93f6ccba9d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-65423f3f859b05f1af94">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7edc251b32115ddbfad1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aba12684ac53adb33a34">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_visible_travel-ad3a62fb3abdf9bd32da"></a>

**0° CCW: unverified** — `in_game_visible_travel-ad3a62fb3abdf9bd32da`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-e8ca89d6cfc0a2949f30"></a>

**90° CCW: unverified** — `in_game_visible_travel-e8ca89d6cfc0a2949f30`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-2c66085f0410d97b2280"></a>

**180° CCW: unverified** — `in_game_visible_travel-2c66085f0410d97b2280`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-90a8fd9567a5804bd3b4"></a>

**270° CCW: unverified** — `in_game_visible_travel-90a8fd9567a5804bd3b4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_visible_travel-c00a9157f52df70eed63"></a>

**0° CCW: unverified** — `in_game_visible_travel-c00a9157f52df70eed63`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-8049f4be419c605f1ff1"></a>

**90° CCW: unverified** — `in_game_visible_travel-8049f4be419c605f1ff1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-8b209453f692c9263118"></a>

**180° CCW: unverified** — `in_game_visible_travel-8b209453f692c9263118`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-2ecc94c34154a053cf00"></a>

**270° CCW: unverified** — `in_game_visible_travel-2ecc94c34154a053cf00`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out</summary>

<a id="case-in_game_visible_travel-eff29eba74f513fffcf6"></a>

**0° CCW: unverified** — `in_game_visible_travel-eff29eba74f513fffcf6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-5338a1f155911648c2cd"></a>

**90° CCW: unverified** — `in_game_visible_travel-5338a1f155911648c2cd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-ea1439b9e4ce95e40db6"></a>

**180° CCW: unverified** — `in_game_visible_travel-ea1439b9e4ce95e40db6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-4da1d7798913fae20467"></a>

**270° CCW: unverified** — `in_game_visible_travel-4da1d7798913fae20467`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out</summary>

<a id="case-in_game_visible_travel-d4ec97c3ec60731a7f8f"></a>

**0° CCW: unverified** — `in_game_visible_travel-d4ec97c3ec60731a7f8f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-b799315a735ce40957ab"></a>

**90° CCW: unverified** — `in_game_visible_travel-b799315a735ce40957ab`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-f590be0074b01b077146"></a>

**180° CCW: unverified** — `in_game_visible_travel-f590be0074b01b077146`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-3ec538c16d0ec71b4c17"></a>

**270° CCW: unverified** — `in_game_visible_travel-3ec538c16d0ec71b4c17`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out</summary>

<a id="case-in_game_visible_travel-fc3d67bfd91d39d5603e"></a>

**0° CCW: unverified** — `in_game_visible_travel-fc3d67bfd91d39d5603e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-33bb84f1969a566367f3"></a>

**90° CCW: unverified** — `in_game_visible_travel-33bb84f1969a566367f3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-5b3de8cd4a32c22048b2"></a>

**180° CCW: unverified** — `in_game_visible_travel-5b3de8cd4a32c22048b2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-0f1c7a90c623bfa69cbb"></a>

**270° CCW: unverified** — `in_game_visible_travel-0f1c7a90c623bfa69cbb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out</summary>

<a id="case-in_game_visible_travel-dcc1d39b9b93f6ccba9d"></a>

**0° CCW: unverified** — `in_game_visible_travel-dcc1d39b9b93f6ccba9d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-65423f3f859b05f1af94"></a>

**90° CCW: unverified** — `in_game_visible_travel-65423f3f859b05f1af94`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-7edc251b32115ddbfad1"></a>

**180° CCW: unverified** — `in_game_visible_travel-7edc251b32115ddbfad1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-aba12684ac53adb33a34"></a>

**270° CCW: unverified** — `in_game_visible_travel-aba12684ac53adb33a34`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 120 cases; unverified: 120</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8a598487f2cb8723053d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9344000a89419751bab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae45e16bff3c668ee669">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd9a1ab1fa83db0f120d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-399e6a82d788131de970">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14e03fdffe2de703ccc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37e9aca951a9e04cd53a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84d9466e591cf60bfed7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b264301f08efa140cde0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed0684273d3e637cdc19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfcf8bd710928ee6000a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b75d771884a7d6a35585">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ff359998dc787fd0bf7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d78c66c63ac4a7638466">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-103eaecd609c6525c595">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b435077ff12a1c2426e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-711418f31c8083859399">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6346246b543e928152cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-132969d3616cafd67c86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91d3826a0308fbcb3dbb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5cc2830b759159391b8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a292d9c16b1611b7576e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54587d669267c40386ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b38f3983cdd4b4d5c815">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a848f5ac095e237a98eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f8689bb5c92a7b5922b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-baef774b1432cfa1b866">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1cec8f44f99cc4f77ed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e571dcadba671e7852c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11241f52340319cd3c21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca879b701d2e5de63ca3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b6a7791daa4d7d40617">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-448c8498f83da7f41448">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00c15204d86ae1be58d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dc28411717fc08d5604">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd873b8bfbdb80010657">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2f4759c325df88453ec7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f92bc18c48f1aebb4a46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c822e9403cf6c289485">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16ab396b22e4f5ce8c6f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23728c801a8cc82a9247">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8908118e5776c2f333b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-973cb9022fd44ecb8747">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b492d90772efdb5b940">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e09d314a4c4c70b0771f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdbd5b0cf33ff6985545">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5388dd99572c7e1d19ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3e609be7ae8fcdb2bd6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-929810e76bde033a26dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a42a391d356d227484ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e29b789d05f5548688c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-626975a949ea3e7c070a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9ac5e8636e303a7525a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f497f0e87559bc556620">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de89d90ac1b61421d596">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16ba693605364c612e5a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-60077694812620e0914d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-847bfa719971d90dbcfb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4767658df84fe4a00b94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-769fb89efb25c4e514f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9cb3397e2ac3145193ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66658286b0aee9e817d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0cab3ff55d60de89331">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24a9954fd95a6f9c7e38">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-02daadb9c2f5a0631ee1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9c51f8dac18e30f7216">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a54abff301db754a7802">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea540f8d6302214425ae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b3288e87f7248b179b02">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8256dffeb25141019a8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4983920adf44f71985f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-459722cebb9e1b714152">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b1fb86aca9a9132d2a5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb73f23b677c70be7db8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a31e7cf47a1783f3481a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6100cdde6c79b49d1dc3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee4dab0ddd2d1be2f3de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b0f398b4a0de37c67bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-995ebc76bd57ed743451">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c995301b40a1f12c7618">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9f7499e94d3bf51fe408">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06aae7c41699a0d9a05e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61a31dc8ac1b82636fe8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85d575ee1902491b48a5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8da99f05598d72bd7e63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abe18025ba7c1145b602">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0e8e5d221fa0751edbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-990a92b2e28ec07741eb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-27a318cb6a0874bed1e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4b5c24efde3eb0f70e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-347f21c0a2a870b6060b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf003da53e0f00c12c01">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8b58476523ff247c8324">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2682faf1cd053147066f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c06891bd876e10b0648c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1ef9ef1c48d7be66fac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a62bae02a28c582b021">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38b74a41e51ba33f920f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-984e5966e46dbadf4450">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b48d1c38291566f31445">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a510a5a2e0a9f7349b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cd2d79a1a1709c41c83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74de4d47059185fd3f63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfa0d379970db3f64179">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-15e50f715ddcfde5d058">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9279eec531dcf26dc113">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7849425c49d7d6c51a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62ce242eed57593a6441">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0c24aa42330514462b9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c458ca8f0d2c03ab1425">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-477278d58a7dea339cdf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d87935faeec6a5c93e8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-58996679166633727c4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b84e4912f8d499a3ef94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3aff46bda4980c60e796">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dccc50ab92d643512915">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66a07baa459df102ae1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc8f891c8fd69de2debe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80f318b23c8299ddd9b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dfaae773fb077e432d5">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8a598487f2cb8723053d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8a598487f2cb8723053d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9344000a89419751bab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d9344000a89419751bab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae45e16bff3c668ee669"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ae45e16bff3c668ee669`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd9a1ab1fa83db0f120d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd9a1ab1fa83db0f120d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-399e6a82d788131de970"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-399e6a82d788131de970`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14e03fdffe2de703ccc0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-14e03fdffe2de703ccc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37e9aca951a9e04cd53a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-37e9aca951a9e04cd53a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84d9466e591cf60bfed7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84d9466e591cf60bfed7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b264301f08efa140cde0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b264301f08efa140cde0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed0684273d3e637cdc19"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ed0684273d3e637cdc19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfcf8bd710928ee6000a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dfcf8bd710928ee6000a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b75d771884a7d6a35585"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b75d771884a7d6a35585`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ff359998dc787fd0bf7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ff359998dc787fd0bf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d78c66c63ac4a7638466"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d78c66c63ac4a7638466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-103eaecd609c6525c595"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-103eaecd609c6525c595`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b435077ff12a1c2426e2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b435077ff12a1c2426e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-711418f31c8083859399"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-711418f31c8083859399`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6346246b543e928152cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6346246b543e928152cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-132969d3616cafd67c86"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-132969d3616cafd67c86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91d3826a0308fbcb3dbb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-91d3826a0308fbcb3dbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5cc2830b759159391b8e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5cc2830b759159391b8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a292d9c16b1611b7576e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a292d9c16b1611b7576e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54587d669267c40386ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54587d669267c40386ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b38f3983cdd4b4d5c815"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b38f3983cdd4b4d5c815`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a848f5ac095e237a98eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a848f5ac095e237a98eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f8689bb5c92a7b5922b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1f8689bb5c92a7b5922b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-baef774b1432cfa1b866"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-baef774b1432cfa1b866`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1cec8f44f99cc4f77ed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f1cec8f44f99cc4f77ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e571dcadba671e7852c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e571dcadba671e7852c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11241f52340319cd3c21"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-11241f52340319cd3c21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca879b701d2e5de63ca3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ca879b701d2e5de63ca3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b6a7791daa4d7d40617"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b6a7791daa4d7d40617`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-448c8498f83da7f41448"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-448c8498f83da7f41448`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00c15204d86ae1be58d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00c15204d86ae1be58d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dc28411717fc08d5604"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1dc28411717fc08d5604`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd873b8bfbdb80010657"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd873b8bfbdb80010657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2f4759c325df88453ec7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f4759c325df88453ec7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f92bc18c48f1aebb4a46"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f92bc18c48f1aebb4a46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c822e9403cf6c289485"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9c822e9403cf6c289485`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16ab396b22e4f5ce8c6f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-16ab396b22e4f5ce8c6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23728c801a8cc82a9247"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23728c801a8cc82a9247`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8908118e5776c2f333b3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8908118e5776c2f333b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-973cb9022fd44ecb8747"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-973cb9022fd44ecb8747`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b492d90772efdb5b940"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8b492d90772efdb5b940`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e09d314a4c4c70b0771f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e09d314a4c4c70b0771f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdbd5b0cf33ff6985545"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fdbd5b0cf33ff6985545`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5388dd99572c7e1d19ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5388dd99572c7e1d19ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3e609be7ae8fcdb2bd6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b3e609be7ae8fcdb2bd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-929810e76bde033a26dd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-929810e76bde033a26dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a42a391d356d227484ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a42a391d356d227484ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e29b789d05f5548688c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1e29b789d05f5548688c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-626975a949ea3e7c070a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-626975a949ea3e7c070a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9ac5e8636e303a7525a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9ac5e8636e303a7525a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f497f0e87559bc556620"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f497f0e87559bc556620`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de89d90ac1b61421d596"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de89d90ac1b61421d596`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16ba693605364c612e5a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-16ba693605364c612e5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-60077694812620e0914d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60077694812620e0914d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-847bfa719971d90dbcfb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-847bfa719971d90dbcfb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4767658df84fe4a00b94"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4767658df84fe4a00b94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-769fb89efb25c4e514f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-769fb89efb25c4e514f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9cb3397e2ac3145193ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9cb3397e2ac3145193ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66658286b0aee9e817d8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-66658286b0aee9e817d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0cab3ff55d60de89331"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0cab3ff55d60de89331`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24a9954fd95a6f9c7e38"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-24a9954fd95a6f9c7e38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-02daadb9c2f5a0631ee1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-02daadb9c2f5a0631ee1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9c51f8dac18e30f7216"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c9c51f8dac18e30f7216`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a54abff301db754a7802"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a54abff301db754a7802`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea540f8d6302214425ae"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ea540f8d6302214425ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b3288e87f7248b179b02"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b3288e87f7248b179b02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8256dffeb25141019a8c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8256dffeb25141019a8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4983920adf44f71985f9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4983920adf44f71985f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-459722cebb9e1b714152"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-459722cebb9e1b714152`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b1fb86aca9a9132d2a5d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1fb86aca9a9132d2a5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb73f23b677c70be7db8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cb73f23b677c70be7db8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a31e7cf47a1783f3481a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a31e7cf47a1783f3481a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6100cdde6c79b49d1dc3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6100cdde6c79b49d1dc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee4dab0ddd2d1be2f3de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee4dab0ddd2d1be2f3de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b0f398b4a0de37c67bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b0f398b4a0de37c67bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-995ebc76bd57ed743451"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-995ebc76bd57ed743451`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c995301b40a1f12c7618"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c995301b40a1f12c7618`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9f7499e94d3bf51fe408"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f7499e94d3bf51fe408`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06aae7c41699a0d9a05e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-06aae7c41699a0d9a05e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61a31dc8ac1b82636fe8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-61a31dc8ac1b82636fe8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85d575ee1902491b48a5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-85d575ee1902491b48a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8da99f05598d72bd7e63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8da99f05598d72bd7e63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abe18025ba7c1145b602"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-abe18025ba7c1145b602`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0e8e5d221fa0751edbe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e0e8e5d221fa0751edbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-990a92b2e28ec07741eb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-990a92b2e28ec07741eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-27a318cb6a0874bed1e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-27a318cb6a0874bed1e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4b5c24efde3eb0f70e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c4b5c24efde3eb0f70e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-347f21c0a2a870b6060b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-347f21c0a2a870b6060b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf003da53e0f00c12c01"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cf003da53e0f00c12c01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8b58476523ff247c8324"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b58476523ff247c8324`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2682faf1cd053147066f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2682faf1cd053147066f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c06891bd876e10b0648c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c06891bd876e10b0648c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1ef9ef1c48d7be66fac"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d1ef9ef1c48d7be66fac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a62bae02a28c582b021"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a62bae02a28c582b021`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38b74a41e51ba33f920f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-38b74a41e51ba33f920f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-984e5966e46dbadf4450"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-984e5966e46dbadf4450`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b48d1c38291566f31445"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b48d1c38291566f31445`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a510a5a2e0a9f7349b8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a510a5a2e0a9f7349b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cd2d79a1a1709c41c83"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6cd2d79a1a1709c41c83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74de4d47059185fd3f63"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74de4d47059185fd3f63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfa0d379970db3f64179"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bfa0d379970db3f64179`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-15e50f715ddcfde5d058"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-15e50f715ddcfde5d058`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9279eec531dcf26dc113"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9279eec531dcf26dc113`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7849425c49d7d6c51a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c7849425c49d7d6c51a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62ce242eed57593a6441"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-62ce242eed57593a6441`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0c24aa42330514462b9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c24aa42330514462b9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c458ca8f0d2c03ab1425"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c458ca8f0d2c03ab1425`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-477278d58a7dea339cdf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-477278d58a7dea339cdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d87935faeec6a5c93e8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d87935faeec6a5c93e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-58996679166633727c4a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-58996679166633727c4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b84e4912f8d499a3ef94"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b84e4912f8d499a3ef94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3aff46bda4980c60e796"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3aff46bda4980c60e796`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dccc50ab92d643512915"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dccc50ab92d643512915`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-66a07baa459df102ae1c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66a07baa459df102ae1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc8f891c8fd69de2debe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bc8f891c8fd69de2debe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80f318b23c8299ddd9b6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-80f318b23c8299ddd9b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dfaae773fb077e432d5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1dfaae773fb077e432d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-y-orthogonal-core:canonical-southeast | <a href="#case-preview_review-8f77e8111e8b37958b0e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-orthogonal-core:canonical-top | <a href="#case-preview_review-884ad14bc8724e8a5c99">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-orthogonal-core:connection-overview | <a href="#case-preview_review-40de692c037cf3810e6a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-y-orthogonal-core:canonical-southeast</summary>

<a id="case-preview_review-8f77e8111e8b37958b0e"></a>

**General: unverified** — `preview_review-8f77e8111e8b37958b0e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-orthogonal-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-orthogonal-core:canonical-top</summary>

<a id="case-preview_review-884ad14bc8724e8a5c99"></a>

**General: unverified** — `preview_review-884ad14bc8724e8a5c99`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-orthogonal-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-orthogonal-core:connection-overview</summary>

<a id="case-preview_review-40de692c037cf3810e6a"></a>

**General: unverified** — `preview_review-40de692c037cf3810e6a`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-orthogonal-core:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested a compact southwest diagonal stem dividing into a northwest diagonal branch and an east orthogonal branch. The lane allocation retains one lane per destination instead of duplicating two lanes onto both branches. Because each ordinary DD deck remains one-way, both branch-to-branch journeys enter on L1 and leave on L2; they therefore use two separate climbs. The complete assembly has three reusable whole-cell owners, keeping every route fragment on a shared city tile with one construction owner.

This component retains its own permanent identity from [piece.jsonc](piece.jsonc). The first physical partition includes native shoulder and support cells as well as routed cells. Model-only cells remain genuinely owned and use empty PATH resources, rather than artificial traffic routes. These design choices are distinct from software acceptance and human game observations.
