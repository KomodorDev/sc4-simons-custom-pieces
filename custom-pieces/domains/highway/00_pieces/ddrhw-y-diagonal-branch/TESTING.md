---
title: "Testing: DD RHW-4 — Diagonal Branch and Paired Graded Links — L1/L2"
summary: "Verify the exact Y-junction component, its native socket, its saved resources, and its separate human game observations."
audience: "Contributors and testers"
document_type: "reference"
---

# Testing: DD RHW-4 — Diagonal Branch and Paired Graded Links — L1/L2

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This document covers `ddrhw-y-diagonal-branch`, the **northwest branch** component of the [compact DD RHW Y junction](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md). Its scope includes 8 owned cells in a 5 × 3-tile rectangle, their full models and traffic fragments, and one separate unowned native DD socket. The lower 7.5 m deck enters from the northwest, and the upper 15 m deck leaves toward the northwest. The exact owned mask and socket address are explained in the [piece placement guide](README.md#21-owned-cells-and-native-approach).

Check B→C from the northwest lower deck to the east upper deck, and C→B from the east lower deck to the northwest upper deck. Also check the separate level B→A and A→B lanes. A working return to the stem does not establish either graded branch connection. Each external deck retains two same-direction native lanes. In the completed assembly, each of the six arm-to-arm movements uses one lane. No authored journey permits a U-turn, travel against an external deck’s direction, or an arbitrary switch between opposing deck services. Internal module cuts can expose several routes at different heights; consult the measured connections below instead of treating one endpoint as the complete boundary.

Require all four proper placement rotations, both diagonal traffic directions where present, and separate camera rotations. A source calculation, a rendered model, a coloured Route Query line, and an observed moving car establish different facts. Only a matching human observation can pass a game case.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `b-a-in` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `a-b-out` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `b-c-in` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [0.7071067811865119, -0.7071067811865831]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `c-b-out` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [-0.7071067811865119, 0.7071067811865831]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `b-a-out` | road / 1 / primary | out | [22.332766, -40.0, 7.5]; [0.25725570106816964, -0.9663433676845538]; 0.0 | `path-interface-90ec3d32f6aca0b2bd9d` |
| `a-b-in` | road / 1 / primary | in | [22.332766, -40.0, 15.0]; [-0.25725570106816964, 0.9663433676845538]; 0.0 | `path-interface-1406061631c7ec05d39a` |
| `c-b-in` | road / 1 / primary | in | [39.700047, -40.0, 12.159544]; [-0.8923143763223463, 0.45141450332090804]; 0.248976814 | `path-interface-9d95f94d02139a7871b0` |
| `b-c-out` | road / 1 / primary | out | [62.247886, -40.0, 14.711544]; [0.8870803545357738, -0.4616150393961248]; 0.085894374 | `path-interface-927eefb98159e68726cc` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `b-a-in` → `b-a-out` | primary |
| road | `b-c-in` → `b-c-out` | primary |
| road | `a-b-in` → `a-b-out` | primary |
| road | `c-b-in` → `c-b-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `b-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Prepare the audited NAM 50 right-hand-traffic profile through the [shared build and input guide](../../../../docs/BUILD_AND_INSTALL.md). The definition requires the native controller, DD RHW-4, RHW core, and MIS inputs listed in [piece.jsonc](piece.jsonc). Record the actual SimCity 4 version, NAM version, traffic handedness, operating system, compatibility layer if used, and installed build identity.
2. Verify the exact build intended for a deliberate installation before copying it into the game. Close the game completely during installation. Restart it, open a disposable flat city, and place new copies; a previously placed experimental object is not the fresh-placement control for a changed construction, model, or PATH revision.
3. For complete journeys, install all three Y components together and follow the [assembly placement table](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md#3-placements). This component is **P02**, with source reference **(-2, -3)** in world `(column,row)` addresses. Its displayed assembly reference is **(X0, Y6), an unowned reference**. Read those as coordinate references, not a verified mouse-cursor anchor.
4. Keep the native socket and the repeating native approach available. The next outward native cell is local (0,0), immediately north of the socket and also this component’s unowned reference. Further native cells follow the northwest staircase; do not fill that reference with another custom piece. Prepare a separate working native DD control using the ordinary DD starter and **RealHighway (RHW-2)** before judging a failed connection against the custom construction.
5. Connect the completed junction to occupied development and useful destinations on all three arms, run the simulation, and confirm moving traffic on the native controls. Demand for only one destination cannot demonstrate the other five allowed journeys.

## 3. Software checks

### 3.1 Source and native contracts

The [native input measurements](../../01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/native-design-inputs.jsonc) pin the original lane classes, heights, models, and controller resources. The [centreline source verification](../../01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/source-verification.jsonc) checks the six reviewed source journeys. Those reports retain their historical source scope. The later ordinary `dist/ddrhw-y-junction-native` build passed saved-resource verification and the whole-assembly physical check; installation and human game observations remain unverified.

A **PATH** resource stores directed traffic routes, while an **S3D** resource stores a visible model. **UV coordinates** identify which part of a texture image appears at each model point.

**RUL1** contains rules that resolve construction markers into a native network tile. **RUL2** contains rules for continuing ordinary draggable networks. A network **exemplar** is metadata linking a resolved tile to its native model.

Its reviewed diagonal socket uses native `57530900` at pose 3. Four diagonal RUL1 solutions cover its proper rotations; the combined selection shares those same four inserted rows with the stem. Six pinned dependencies cover the socket’s model, PATH, and exemplar, plus the outward `57530200` continuation’s model, PATH, and exemplar. The [native socket adapter](../../implementation/scp_highway/y_junction_approaches.py) checks all four proper rotations, flat three-metre collars, actual lane classes and compatibility fields, and the original inward and outward continuation states without replacing native RUL2. The ordinary build also passed this component’s actual saved native-boundary check; fixture and original-input tests retain their separate scope.

The [physical source](../../implementation/scp_highway/y_junction_geometry.py) and [whole-cell layout](../../implementation/scp_highway/y_junction_layout.py) compiled this component. Independent checks passed its actual emitted PATHs, models, construction fields, all five zooms, support geometry, and saved preview, followed by the complete assembly’s physical check. The [accepted connector contract](checks/accepted-connector-contract.jsonc) binds the checked ordinary build and canonical PATH fingerprints. Exact finite native profiles, inherited interior faces, and measured overhang are governed by the [assembly’s software-check scopes](../../01_assemblies/ddrhw-compact-diagonal-y-junction/TESTING.md#3-software-checks).

Its source maximum grade is approximately 26.5725%, below the declared 30% experimental limit. Intermediate link fragments have their actual authored heights between 7.5 m and 15 m; they are not additional standard DD sockets. A **grade** is vertical change divided by horizontal route length; a 20% grade gains 2 m over 10 m horizontally. Actual saved PATHs passed the independent 30% grade ceiling and retain `UseElevation=1` for their authored heights. The declared car envelope is 2.5 m wide × 3.8 m high; software clearance against that envelope is not a structural-capacity calculation or a guarantee for every vehicle replacement.

### 3.2 Reproduce the checks

Run these commands from the repository root. Replace `BUILD_NAME` with a new descriptive reproduction-folder name. The first command writes a standalone build of this component; use the [assembly’s full-selection procedure](../../01_assemblies/ddrhw-compact-diagonal-y-junction/TESTING.md#3-software-checks) to reproduce the checked three-component build and whole-junction verification. `verify` reads that same saved build. None of these commands installs the result. Use `python` instead of `python3` inside an activated Windows Python environment.

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-y-diagonal-branch --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-y-diagonal-branch --build dist/BUILD_NAME
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-y-diagonal-branch
python3 -B tools/run_tests.py
```

The configured verification run passed **51 focused Y regression tests without skips**. To reproduce the focused family, run `python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p 'test_y_junction*.py'`. To isolate native-helper controls, use the pattern `test_y_junction_approaches.py`. Original-input tests may skip in another environment when proprietary NAM inputs are unavailable; report those skips explicitly. The [accepted connector contract](checks/accepted-connector-contract.jsonc) records the checked build identity and canonical PATH fingerprints. A document-layout result and a human game observation retain their own scopes.

## 4. Game checks

### 4.1 Placement and native construction

1. Follow [README placement](README.md#22-place-the-component), using the exact component name and complete owned-cell pattern. Inspect every owned tile, including model-only shoulders and supports. Leave native socket **(0,1)** unowned, and record whether the expected ordinary DD tile is actually seeded there.
2. Select **RealHighway (RHW-2)**, start at that native socket, and drag at least three tiles toward the **northwest**. Inspect the full staggered pattern for a diagonal approach, or the straight row for an orthogonal approach. Record whether the native network retains both heights and correct directions.
3. At a second site, make a working native approach first, leave a short straight gap, place a fresh component at the planned reference, and drag from the existing line inward to its native socket. Stop outside the fixed owned tiles. At a third site, place beside an already completed matching native approach. Record these construction orders independently.
4. Repeat at 90°, 180°, and 270° using **Home** and **End**. Check that model, owned cells, unowned native socket, native continuation, and preview rotate together. Record actual mouse-cursor alignment separately from the source reference; do not replace the source reference with the first visible custom road tile.

### 4.2 Routes and visible cars

1. Assemble all three pieces at the exact references, connect the three native approaches to development and destinations, and run the simulation. Confirm the native control traffic still works.
2. Use **Route Query** to inspect the component’s generated allowed journeys and the six whole-junction directions. Record each displayed route separately from visible movement.
3. Check B→C from the northwest lower deck to the east upper deck, and C→B from the east lower deck to the northwest upper deck. Also check the separate level B→A and A→B lanes. A working return to the stem does not establish either graded branch connection. Follow actual cars from native approach to native approach, checking every module seam and both deck levels. Record the exact journey, placement rotation, and tile where a car stops, disappears, jumps in height, or clips a barrier or support.
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
- [ ] Route Query: 0/16 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/16 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 101, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-y-diagonal-branch/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-y-diagonal-branch/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ec376e6fa1716751b556">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ec376e6fa1716751b556"></a>

**General: unverified** — `software_resources-ec376e6fa1716751b556`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ec376e6fa1716751b556">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ec376e6fa1716751b556"></a>

**General: unverified** — `software_connectivity-ec376e6fa1716751b556`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-60fbce2bda6789f974ad">[ ] unverified</a> | <a href="#case-in_game_render-eea3137779401dc2110e">[ ] unverified</a> | <a href="#case-in_game_render-a4d398aef1df3dbab818">[ ] unverified</a> | <a href="#case-in_game_render-1527caacd71f2fe7d7b3">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-60fbce2bda6789f974ad"></a>

**0° CCW: unverified** — `in_game_render-60fbce2bda6789f974ad`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-eea3137779401dc2110e"></a>

**90° CCW: unverified** — `in_game_render-eea3137779401dc2110e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a4d398aef1df3dbab818"></a>

**180° CCW: unverified** — `in_game_render-a4d398aef1df3dbab818`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1527caacd71f2fe7d7b3"></a>

**270° CCW: unverified** — `in_game_render-1527caacd71f2fe7d7b3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-60fbce2bda6789f974ad">[ ] unverified</a> | <a href="#case-in_game_placement-eea3137779401dc2110e">[ ] unverified</a> | <a href="#case-in_game_placement-a4d398aef1df3dbab818">[ ] unverified</a> | <a href="#case-in_game_placement-1527caacd71f2fe7d7b3">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-60fbce2bda6789f974ad"></a>

**0° CCW: unverified** — `in_game_placement-60fbce2bda6789f974ad`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-eea3137779401dc2110e"></a>

**90° CCW: unverified** — `in_game_placement-eea3137779401dc2110e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a4d398aef1df3dbab818"></a>

**180° CCW: unverified** — `in_game_placement-a4d398aef1df3dbab818`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1527caacd71f2fe7d7b3"></a>

**270° CCW: unverified** — `in_game_placement-1527caacd71f2fe7d7b3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-60fbce2bda6789f974ad">[ ] unverified</a> | <a href="#case-in_game_demolition-eea3137779401dc2110e">[ ] unverified</a> | <a href="#case-in_game_demolition-a4d398aef1df3dbab818">[ ] unverified</a> | <a href="#case-in_game_demolition-1527caacd71f2fe7d7b3">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-60fbce2bda6789f974ad"></a>

**0° CCW: unverified** — `in_game_demolition-60fbce2bda6789f974ad`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-eea3137779401dc2110e"></a>

**90° CCW: unverified** — `in_game_demolition-eea3137779401dc2110e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a4d398aef1df3dbab818"></a>

**180° CCW: unverified** — `in_game_demolition-a4d398aef1df3dbab818`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1527caacd71f2fe7d7b3"></a>

**270° CCW: unverified** — `in_game_demolition-1527caacd71f2fe7d7b3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-60fbce2bda6789f974ad">[ ] unverified</a> | <a href="#case-in_game_save_reload-eea3137779401dc2110e">[ ] unverified</a> | <a href="#case-in_game_save_reload-a4d398aef1df3dbab818">[ ] unverified</a> | <a href="#case-in_game_save_reload-1527caacd71f2fe7d7b3">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-60fbce2bda6789f974ad"></a>

**0° CCW: unverified** — `in_game_save_reload-60fbce2bda6789f974ad`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-eea3137779401dc2110e"></a>

**90° CCW: unverified** — `in_game_save_reload-eea3137779401dc2110e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a4d398aef1df3dbab818"></a>

**180° CCW: unverified** — `in_game_save_reload-a4d398aef1df3dbab818`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1527caacd71f2fe7d7b3"></a>

**270° CCW: unverified** — `in_game_save_reload-1527caacd71f2fe7d7b3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_route_query-15ba8bd904b6b832725b">[ ] unverified</a> | <a href="#case-in_game_route_query-d744276a15fd2cdad10d">[ ] unverified</a> | <a href="#case-in_game_route_query-17d046475f8bcf5b14ea">[ ] unverified</a> | <a href="#case-in_game_route_query-12ea0eb9d29990bbbedb">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out | — | <a href="#case-in_game_route_query-ee5f31d25c79064c4daf">[ ] unverified</a> | <a href="#case-in_game_route_query-653d0eb5e1290ea00df9">[ ] unverified</a> | <a href="#case-in_game_route_query-da1fb87ad5d5ddea79d9">[ ] unverified</a> | <a href="#case-in_game_route_query-6b2f6363784eb5c6dea1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_route_query-2ad590bfc17e792e0a14">[ ] unverified</a> | <a href="#case-in_game_route_query-e5ddf4f2611c7b5f7bb0">[ ] unverified</a> | <a href="#case-in_game_route_query-6e1764bd5c0a861e7993">[ ] unverified</a> | <a href="#case-in_game_route_query-85e7b36a97eab04cdcb3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out | — | <a href="#case-in_game_route_query-09d9eba8ffc415b5d352">[ ] unverified</a> | <a href="#case-in_game_route_query-59850ca4aa14f410718d">[ ] unverified</a> | <a href="#case-in_game_route_query-1c674ccf8d5d1a2f5eda">[ ] unverified</a> | <a href="#case-in_game_route_query-8d09656de772b2b4a653">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_route_query-15ba8bd904b6b832725b"></a>

**0° CCW: unverified** — `in_game_route_query-15ba8bd904b6b832725b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-d744276a15fd2cdad10d"></a>

**90° CCW: unverified** — `in_game_route_query-d744276a15fd2cdad10d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-17d046475f8bcf5b14ea"></a>

**180° CCW: unverified** — `in_game_route_query-17d046475f8bcf5b14ea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-12ea0eb9d29990bbbedb"></a>

**270° CCW: unverified** — `in_game_route_query-12ea0eb9d29990bbbedb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out</summary>

<a id="case-in_game_route_query-ee5f31d25c79064c4daf"></a>

**0° CCW: unverified** — `in_game_route_query-ee5f31d25c79064c4daf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-653d0eb5e1290ea00df9"></a>

**90° CCW: unverified** — `in_game_route_query-653d0eb5e1290ea00df9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-da1fb87ad5d5ddea79d9"></a>

**180° CCW: unverified** — `in_game_route_query-da1fb87ad5d5ddea79d9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-6b2f6363784eb5c6dea1"></a>

**270° CCW: unverified** — `in_game_route_query-6b2f6363784eb5c6dea1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_route_query-2ad590bfc17e792e0a14"></a>

**0° CCW: unverified** — `in_game_route_query-2ad590bfc17e792e0a14`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-e5ddf4f2611c7b5f7bb0"></a>

**90° CCW: unverified** — `in_game_route_query-e5ddf4f2611c7b5f7bb0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-6e1764bd5c0a861e7993"></a>

**180° CCW: unverified** — `in_game_route_query-6e1764bd5c0a861e7993`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-85e7b36a97eab04cdcb3"></a>

**270° CCW: unverified** — `in_game_route_query-85e7b36a97eab04cdcb3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out</summary>

<a id="case-in_game_route_query-09d9eba8ffc415b5d352"></a>

**0° CCW: unverified** — `in_game_route_query-09d9eba8ffc415b5d352`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-59850ca4aa14f410718d"></a>

**90° CCW: unverified** — `in_game_route_query-59850ca4aa14f410718d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-1c674ccf8d5d1a2f5eda"></a>

**180° CCW: unverified** — `in_game_route_query-1c674ccf8d5d1a2f5eda`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-8d09656de772b2b4a653"></a>

**270° CCW: unverified** — `in_game_route_query-8d09656de772b2b4a653`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_visible_travel-15ba8bd904b6b832725b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d744276a15fd2cdad10d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-17d046475f8bcf5b14ea">[ ] unverified</a> | <a href="#case-in_game_visible_travel-12ea0eb9d29990bbbedb">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out | — | <a href="#case-in_game_visible_travel-ee5f31d25c79064c4daf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-653d0eb5e1290ea00df9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-da1fb87ad5d5ddea79d9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6b2f6363784eb5c6dea1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_visible_travel-2ad590bfc17e792e0a14">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e5ddf4f2611c7b5f7bb0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6e1764bd5c0a861e7993">[ ] unverified</a> | <a href="#case-in_game_visible_travel-85e7b36a97eab04cdcb3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out | — | <a href="#case-in_game_visible_travel-09d9eba8ffc415b5d352">[ ] unverified</a> | <a href="#case-in_game_visible_travel-59850ca4aa14f410718d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1c674ccf8d5d1a2f5eda">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8d09656de772b2b4a653">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_visible_travel-15ba8bd904b6b832725b"></a>

**0° CCW: unverified** — `in_game_visible_travel-15ba8bd904b6b832725b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-d744276a15fd2cdad10d"></a>

**90° CCW: unverified** — `in_game_visible_travel-d744276a15fd2cdad10d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-17d046475f8bcf5b14ea"></a>

**180° CCW: unverified** — `in_game_visible_travel-17d046475f8bcf5b14ea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-12ea0eb9d29990bbbedb"></a>

**270° CCW: unverified** — `in_game_visible_travel-12ea0eb9d29990bbbedb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out</summary>

<a id="case-in_game_visible_travel-ee5f31d25c79064c4daf"></a>

**0° CCW: unverified** — `in_game_visible_travel-ee5f31d25c79064c4daf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-653d0eb5e1290ea00df9"></a>

**90° CCW: unverified** — `in_game_visible_travel-653d0eb5e1290ea00df9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-da1fb87ad5d5ddea79d9"></a>

**180° CCW: unverified** — `in_game_visible_travel-da1fb87ad5d5ddea79d9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-6b2f6363784eb5c6dea1"></a>

**270° CCW: unverified** — `in_game_visible_travel-6b2f6363784eb5c6dea1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_visible_travel-2ad590bfc17e792e0a14"></a>

**0° CCW: unverified** — `in_game_visible_travel-2ad590bfc17e792e0a14`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-e5ddf4f2611c7b5f7bb0"></a>

**90° CCW: unverified** — `in_game_visible_travel-e5ddf4f2611c7b5f7bb0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-6e1764bd5c0a861e7993"></a>

**180° CCW: unverified** — `in_game_visible_travel-6e1764bd5c0a861e7993`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-85e7b36a97eab04cdcb3"></a>

**270° CCW: unverified** — `in_game_visible_travel-85e7b36a97eab04cdcb3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out</summary>

<a id="case-in_game_visible_travel-09d9eba8ffc415b5d352"></a>

**0° CCW: unverified** — `in_game_visible_travel-09d9eba8ffc415b5d352`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-59850ca4aa14f410718d"></a>

**90° CCW: unverified** — `in_game_visible_travel-59850ca4aa14f410718d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-1c674ccf8d5d1a2f5eda"></a>

**180° CCW: unverified** — `in_game_visible_travel-1c674ccf8d5d1a2f5eda`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-8d09656de772b2b4a653"></a>

**270° CCW: unverified** — `in_game_visible_travel-8d09656de772b2b4a653`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7fa8b9592f6a639ee36e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c531f35de660c2bd5029">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c3498d1dad7068c1cfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0deedeff7b8c0409fb1a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c06936a1bff2f63c1977">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00441479a8ae5e67bc38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee66136ecf1b0034f1c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dda5f27b4d8e71138bc4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cacfa795515477b82029">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e19f0ec8d491d5526136">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cebb8e3a8f8b8c768236">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d32116481c47158e5b1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2a0312013b1d659a3669">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63c958416d75ff7595b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04cd734bad4dd434b7ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-325130a3fd04e0a9092f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d621aecb7eb220cbc0f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76a11e0eb58442ea0952">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-245f25c8dc192a7847ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-253d931c75407a78dd37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c599d6a9553cea12c6b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9e6a4d6c6f1718170de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1398f95329a1b322f8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-befbca0ec7ec7bb91a7e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dec454c8ba455651efef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e691d4e8eda81b91bee1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7dd2d4c805f7a4a5963">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da3d01d380a8436d6af7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0eeb6efdb601854a5d00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3cf6f0e9ede947154f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fc19770b17763a666ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-681e119fddabdddff0b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a723fd8968e20243fd4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-413dcc0fab1c2fa85d6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e222a23b9c121d34b160">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7adfbf4b056621e0e85f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-09b8c450622528744501">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9af8d79ebe6c14f99f08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25a2ee0afe47fa9f1d98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b37c86f83a81cc636a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8526b9072a32b582b26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ea5e3126d8d33a2600d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d64cdd917a70477a50f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-399399315fe1f906ca29">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c163d04f1fda03d67ef1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35af87a35428f928bf26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc5762f5f6b6976d505e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-912f9a3155c113e6d431">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7fa8b9592f6a639ee36e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7fa8b9592f6a639ee36e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c531f35de660c2bd5029"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c531f35de660c2bd5029`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c3498d1dad7068c1cfa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c3498d1dad7068c1cfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0deedeff7b8c0409fb1a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0deedeff7b8c0409fb1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c06936a1bff2f63c1977"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c06936a1bff2f63c1977`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00441479a8ae5e67bc38"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00441479a8ae5e67bc38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee66136ecf1b0034f1c5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee66136ecf1b0034f1c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dda5f27b4d8e71138bc4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dda5f27b4d8e71138bc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cacfa795515477b82029"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cacfa795515477b82029`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e19f0ec8d491d5526136"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e19f0ec8d491d5526136`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cebb8e3a8f8b8c768236"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cebb8e3a8f8b8c768236`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d32116481c47158e5b1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0d32116481c47158e5b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2a0312013b1d659a3669"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2a0312013b1d659a3669`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63c958416d75ff7595b6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63c958416d75ff7595b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04cd734bad4dd434b7ee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-04cd734bad4dd434b7ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-325130a3fd04e0a9092f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-325130a3fd04e0a9092f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d621aecb7eb220cbc0f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d621aecb7eb220cbc0f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76a11e0eb58442ea0952"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-76a11e0eb58442ea0952`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-245f25c8dc192a7847ee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-245f25c8dc192a7847ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-253d931c75407a78dd37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-253d931c75407a78dd37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c599d6a9553cea12c6b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c599d6a9553cea12c6b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9e6a4d6c6f1718170de"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c9e6a4d6c6f1718170de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1398f95329a1b322f8f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d1398f95329a1b322f8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-befbca0ec7ec7bb91a7e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-befbca0ec7ec7bb91a7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dec454c8ba455651efef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dec454c8ba455651efef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e691d4e8eda81b91bee1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e691d4e8eda81b91bee1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7dd2d4c805f7a4a5963"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b7dd2d4c805f7a4a5963`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da3d01d380a8436d6af7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-da3d01d380a8436d6af7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0eeb6efdb601854a5d00"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0eeb6efdb601854a5d00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3cf6f0e9ede947154f6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e3cf6f0e9ede947154f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fc19770b17763a666ba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1fc19770b17763a666ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-681e119fddabdddff0b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-681e119fddabdddff0b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a723fd8968e20243fd4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a723fd8968e20243fd4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-413dcc0fab1c2fa85d6b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-413dcc0fab1c2fa85d6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e222a23b9c121d34b160"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e222a23b9c121d34b160`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7adfbf4b056621e0e85f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7adfbf4b056621e0e85f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-09b8c450622528744501"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09b8c450622528744501`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9af8d79ebe6c14f99f08"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9af8d79ebe6c14f99f08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25a2ee0afe47fa9f1d98"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25a2ee0afe47fa9f1d98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b37c86f83a81cc636a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2b37c86f83a81cc636a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8526b9072a32b582b26"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8526b9072a32b582b26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ea5e3126d8d33a2600d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ea5e3126d8d33a2600d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d64cdd917a70477a50f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d64cdd917a70477a50f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-399399315fe1f906ca29"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-399399315fe1f906ca29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c163d04f1fda03d67ef1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c163d04f1fda03d67ef1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35af87a35428f928bf26"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35af87a35428f928bf26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc5762f5f6b6976d505e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dc5762f5f6b6976d505e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-912f9a3155c113e6d431"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-912f9a3155c113e6d431`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-y-diagonal-branch:canonical-southeast | <a href="#case-preview_review-c4f0da6d707c19db663f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-diagonal-branch:canonical-top | <a href="#case-preview_review-57c94d0cf03e0d6a5ac0">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-diagonal-branch:connection-overview | <a href="#case-preview_review-cc172b3105492aff5c78">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-y-diagonal-branch:canonical-southeast</summary>

<a id="case-preview_review-c4f0da6d707c19db663f"></a>

**General: unverified** — `preview_review-c4f0da6d707c19db663f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-diagonal-branch:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-diagonal-branch:canonical-top</summary>

<a id="case-preview_review-57c94d0cf03e0d6a5ac0"></a>

**General: unverified** — `preview_review-57c94d0cf03e0d6a5ac0`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-diagonal-branch:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-diagonal-branch:connection-overview</summary>

<a id="case-preview_review-cc172b3105492aff5c78"></a>

**General: unverified** — `preview_review-cc172b3105492aff5c78`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-diagonal-branch:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested a compact southwest diagonal stem dividing into a northwest diagonal branch and an east orthogonal branch. The lane allocation retains one lane per destination instead of duplicating two lanes onto both branches. Because each ordinary DD deck remains one-way, both branch-to-branch journeys enter on L1 and leave on L2; they therefore use two separate climbs. The complete assembly has three reusable whole-cell owners, keeping every route fragment on a shared city tile with one construction owner.

This component retains its own permanent identity from [piece.jsonc](piece.jsonc). The first physical partition includes native shoulder and support cells as well as routed cells. Model-only cells remain genuinely owned and use empty PATH resources, rather than artificial traffic routes. These design choices are distinct from software acceptance and human game observations.
