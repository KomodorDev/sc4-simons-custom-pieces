---
title: "Testing: DD RHW-4 — Diagonal Two-Branch Stem — L1/L2"
summary: "Verify the exact Y-junction component, its native socket, its saved resources, and its separate human game observations."
audience: "Contributors and testers"
document_type: "reference"
---

# Testing: DD RHW-4 — Diagonal Two-Branch Stem — L1/L2

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This document covers `ddrhw-y-diagonal-stem-split`, the **southwest stem** component of the [compact DD RHW Y junction](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md). Its scope includes 8 owned cells in a 5 × 3-tile rectangle, their full models and traffic fragments, and one separate unowned native DD socket. The upper 15 m deck enters from the southwest, and the lower 7.5 m deck leaves toward the southwest. The exact owned mask and socket address are explained in the [piece placement guide](README.md#21-owned-cells-and-native-approach).

Follow the two upper incoming lanes separately: one must reach B, and the other must reach C after all three components are assembled. Follow the two lower returning lanes from B and C back to A. Do not accept only one of the two split choices as a complete stem test. Each external deck retains two same-direction native lanes. In the completed assembly, each of the six arm-to-arm movements uses one lane. No authored journey permits a U-turn, travel against an external deck’s direction, or an arbitrary switch between opposing deck services. Internal module cuts can expose several routes at different heights; consult the measured connections below instead of treating one endpoint as the complete boundary.

Require all four proper placement rotations, both diagonal traffic directions where present, and separate camera rotations. A source calculation, a rendered model, a coloured Route Query line, and an observed moving car establish different facts. Only a matching human observation can pass a game case.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `c-a-out` | road / 1 / primary | out | [8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `a-c-in` | road / 1 / primary | in | [8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `b-a-out` | road / 1 / primary | out | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `a-b-in` | road / 1 / primary | in | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `b-a-in` | road / 1 / primary | in | [22.332766, 8.0, 7.5]; [-0.25725570106816964, -0.9663433676845538]; 0.0 | `path-interface-248f7bfc0338ffae18d4` |
| `a-b-out` | road / 1 / primary | out | [22.332766, 8.0, 15.0]; [0.25725570106816964, 0.9663433676845538]; 0.0 | `path-interface-c34990f0463212897200` |
| `c-a-in` | road / 1 / primary | in | [53.321807, 8.0, 7.5]; [-0.9475295370856598, -0.31966822855929156]; 0.0 | `path-interface-58ff10c976f8cd198ffb` |
| `a-c-out` | road / 1 / primary | out | [53.321807, 8.0, 15.0]; [0.9475295370856598, 0.31966822855929156]; 0.0 | `path-interface-96b79c79f51bfeae1ef8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `a-c-in` → `a-c-out` | primary |
| road | `a-b-in` → `a-b-out` | primary |
| road | `b-a-in` → `b-a-out` | primary |
| road | `c-a-in` → `c-a-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `a-c-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Prepare the audited NAM 50 right-hand-traffic profile through the [shared build and input guide](../../../../docs/BUILD_AND_INSTALL.md). The definition requires the native controller, DD RHW-4, RHW core, and MIS inputs listed in [piece.jsonc](piece.jsonc). Record the actual SimCity 4 version, NAM version, traffic handedness, operating system, compatibility layer if used, and installed build identity.
2. Verify the exact build intended for a deliberate installation before copying it into the game. Close the game completely during installation. Restart it, open a disposable flat city, and place new copies; a previously placed experimental object is not the fresh-placement control for a changed construction, model, or PATH revision.
3. For complete journeys, install all three Y components together and follow the [assembly placement table](../../01_assemblies/ddrhw-compact-diagonal-y-junction/README.md#3-placements). This component is **P01**, with source reference **(-2, 1)** in world `(column,row)` addresses. Its displayed assembly reference is **(X0, Y2)**. Read those as coordinate references, not a verified mouse-cursor anchor.
4. Keep the native socket and the repeating native approach available. The next outward native cell is local (0,2), immediately south of the socket. Further native cells follow the southwest staircase; keep both rows of that diagonal pattern available. Prepare a separate working native DD control using the ordinary DD starter and **RealHighway (RHW-2)** before judging a failed connection against the custom construction.
5. Connect the completed junction to occupied development and useful destinations on all three arms, run the simulation, and confirm moving traffic on the native controls. Demand for only one destination cannot demonstrate the other five allowed journeys.

## 3. Software checks

### 3.1 Source and native contracts

The [native input measurements](../../01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/native-design-inputs.jsonc) pin the original lane classes, heights, models, and controller resources. The [centreline source verification](../../01_assemblies/ddrhw-compact-diagonal-y-junction/evidence/source-verification.jsonc) checks the six reviewed source journeys. Those reports retain their historical source scope. The later ordinary `dist/ddrhw-y-junction-native` build passed saved-resource verification and the whole-assembly physical check; installation and human game observations remain unverified.

A **PATH** resource stores directed traffic routes, while an **S3D** resource stores a visible model. **UV coordinates** identify which part of a texture image appears at each model point.

**RUL1** contains rules that resolve construction markers into a native network tile. **RUL2** contains rules for continuing ordinary draggable networks. A network **exemplar** is metadata linking a resolved tile to its native model.

Its reviewed diagonal socket uses native `57530900` at pose 0. Four diagonal RUL1 solutions cover its proper rotations; the combined selection shares those same four inserted rows with the northwest component. Six pinned dependencies cover the socket’s model, PATH, and exemplar, plus the outward `57530200` continuation’s model, PATH, and exemplar. The [native socket adapter](../../implementation/scp_highway/y_junction_approaches.py) checks all four proper rotations, flat three-metre collars, actual lane classes and compatibility fields, and the original inward and outward continuation states without replacing native RUL2. The ordinary build also passed this component’s actual saved native-boundary check; fixture and original-input tests retain their separate scope.

The [physical source](../../implementation/scp_highway/y_junction_geometry.py) and [whole-cell layout](../../implementation/scp_highway/y_junction_layout.py) compiled this component. Independent checks passed its actual emitted PATHs, models, construction fields, all five zooms, support geometry, and saved preview, followed by the complete assembly’s physical check. The [accepted connector contract](checks/accepted-connector-contract.jsonc) binds the checked ordinary build and canonical PATH fingerprints. Exact finite native profiles, inherited interior faces, and measured overhang are governed by the [assembly’s software-check scopes](../../01_assemblies/ddrhw-compact-diagonal-y-junction/TESTING.md#3-software-checks).

Every traffic fragment in this component is level at either 7.5 m or 15 m; its source maximum grade is 0%. A **grade** is vertical change divided by horizontal route length; a 20% grade gains 2 m over 10 m horizontally. Actual saved PATHs passed the independent 30% grade ceiling and retain `UseElevation=1` for their authored heights. The declared car envelope is 2.5 m wide × 3.8 m high; software clearance against that envelope is not a structural-capacity calculation or a guarantee for every vehicle replacement.

### 3.2 Reproduce the checks

Run these commands from the repository root. Replace `BUILD_NAME` with a new descriptive reproduction-folder name. The first command writes a standalone build of this component; use the [assembly’s full-selection procedure](../../01_assemblies/ddrhw-compact-diagonal-y-junction/TESTING.md#3-software-checks) to reproduce the checked three-component build and whole-junction verification. `verify` reads that same saved build. None of these commands installs the result. Use `python` instead of `python3` inside an activated Windows Python environment.

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-y-diagonal-stem-split --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-y-diagonal-stem-split --build dist/BUILD_NAME
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-y-diagonal-stem-split
python3 -B tools/run_tests.py
```

The configured verification run passed **51 focused Y regression tests without skips**. To reproduce the focused family, run `python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p 'test_y_junction*.py'`. To isolate native-helper controls, use the pattern `test_y_junction_approaches.py`. Original-input tests may skip in another environment when proprietary NAM inputs are unavailable; report those skips explicitly. The [accepted connector contract](checks/accepted-connector-contract.jsonc) records the checked build identity and canonical PATH fingerprints. A document-layout result and a human game observation retain their own scopes.

## 4. Game checks

### 4.1 Placement and native construction

1. Follow [README placement](README.md#22-place-the-component), using the exact component name and complete owned-cell pattern. Inspect every owned tile, including model-only shoulders and supports. Leave native socket **(0,1)** unowned, and record whether the expected ordinary DD tile is actually seeded there.
2. Select **RealHighway (RHW-2)**, start at that native socket, and drag at least three tiles toward the **southwest**. Inspect the full staggered pattern for a diagonal approach, or the straight row for an orthogonal approach. Record whether the native network retains both heights and correct directions.
3. At a second site, make a working native approach first, leave a short straight gap, place a fresh component at the planned reference, and drag from the existing line inward to its native socket. Stop outside the fixed owned tiles. At a third site, place beside an already completed matching native approach. Record these construction orders independently.
4. Repeat at 90°, 180°, and 270° using **Home** and **End**. Check that model, owned cells, unowned native socket, native continuation, and preview rotate together. Record actual mouse-cursor alignment separately from the source reference; do not replace the source reference with the first visible custom road tile.

### 4.2 Routes and visible cars

1. Assemble all three pieces at the exact references, connect the three native approaches to development and destinations, and run the simulation. Confirm the native control traffic still works.
2. Use **Route Query** to inspect the component’s generated allowed journeys and the six whole-junction directions. Record each displayed route separately from visible movement.
3. Follow the two upper incoming lanes separately: one must reach B, and the other must reach C after all three components are assembled. Follow the two lower returning lanes from B and C back to A. Do not accept only one of the two split choices as a complete stem test. Follow actual cars from native approach to native approach, checking every module seam and both deck levels. Record the exact journey, placement rotation, and tile where a car stops, disappears, jumps in height, or clips a barrier or support.
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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-y-diagonal-stem-split/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-y-diagonal-stem-split/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-f58fa0449b197b459b98">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-f58fa0449b197b459b98"></a>

**General: unverified** — `software_resources-f58fa0449b197b459b98`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-f58fa0449b197b459b98">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-f58fa0449b197b459b98"></a>

**General: unverified** — `software_connectivity-f58fa0449b197b459b98`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-8dd3f87e7afcfba00d9f">[ ] unverified</a> | <a href="#case-in_game_render-cd293fb2db840140e9d0">[ ] unverified</a> | <a href="#case-in_game_render-88cf2aca049b374e1371">[ ] unverified</a> | <a href="#case-in_game_render-628504faf9c0d507d0dc">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-8dd3f87e7afcfba00d9f"></a>

**0° CCW: unverified** — `in_game_render-8dd3f87e7afcfba00d9f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-cd293fb2db840140e9d0"></a>

**90° CCW: unverified** — `in_game_render-cd293fb2db840140e9d0`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-88cf2aca049b374e1371"></a>

**180° CCW: unverified** — `in_game_render-88cf2aca049b374e1371`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-628504faf9c0d507d0dc"></a>

**270° CCW: unverified** — `in_game_render-628504faf9c0d507d0dc`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-8dd3f87e7afcfba00d9f">[ ] unverified</a> | <a href="#case-in_game_placement-cd293fb2db840140e9d0">[ ] unverified</a> | <a href="#case-in_game_placement-88cf2aca049b374e1371">[ ] unverified</a> | <a href="#case-in_game_placement-628504faf9c0d507d0dc">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-8dd3f87e7afcfba00d9f"></a>

**0° CCW: unverified** — `in_game_placement-8dd3f87e7afcfba00d9f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-cd293fb2db840140e9d0"></a>

**90° CCW: unverified** — `in_game_placement-cd293fb2db840140e9d0`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-88cf2aca049b374e1371"></a>

**180° CCW: unverified** — `in_game_placement-88cf2aca049b374e1371`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-628504faf9c0d507d0dc"></a>

**270° CCW: unverified** — `in_game_placement-628504faf9c0d507d0dc`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-8dd3f87e7afcfba00d9f">[ ] unverified</a> | <a href="#case-in_game_demolition-cd293fb2db840140e9d0">[ ] unverified</a> | <a href="#case-in_game_demolition-88cf2aca049b374e1371">[ ] unverified</a> | <a href="#case-in_game_demolition-628504faf9c0d507d0dc">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-8dd3f87e7afcfba00d9f"></a>

**0° CCW: unverified** — `in_game_demolition-8dd3f87e7afcfba00d9f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-cd293fb2db840140e9d0"></a>

**90° CCW: unverified** — `in_game_demolition-cd293fb2db840140e9d0`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-88cf2aca049b374e1371"></a>

**180° CCW: unverified** — `in_game_demolition-88cf2aca049b374e1371`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-628504faf9c0d507d0dc"></a>

**270° CCW: unverified** — `in_game_demolition-628504faf9c0d507d0dc`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-8dd3f87e7afcfba00d9f">[ ] unverified</a> | <a href="#case-in_game_save_reload-cd293fb2db840140e9d0">[ ] unverified</a> | <a href="#case-in_game_save_reload-88cf2aca049b374e1371">[ ] unverified</a> | <a href="#case-in_game_save_reload-628504faf9c0d507d0dc">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-8dd3f87e7afcfba00d9f"></a>

**0° CCW: unverified** — `in_game_save_reload-8dd3f87e7afcfba00d9f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-cd293fb2db840140e9d0"></a>

**90° CCW: unverified** — `in_game_save_reload-cd293fb2db840140e9d0`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-88cf2aca049b374e1371"></a>

**180° CCW: unverified** — `in_game_save_reload-88cf2aca049b374e1371`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-628504faf9c0d507d0dc"></a>

**270° CCW: unverified** — `in_game_save_reload-628504faf9c0d507d0dc`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out | — | <a href="#case-in_game_route_query-ae295232fcc6398d685f">[ ] unverified</a> | <a href="#case-in_game_route_query-5b7c8da403e0e8d2593f">[ ] unverified</a> | <a href="#case-in_game_route_query-2ae4e7e1cf8955e52c07">[ ] unverified</a> | <a href="#case-in_game_route_query-b143230d3c08acd52a6a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_route_query-26ff03bc2f7d4df07262">[ ] unverified</a> | <a href="#case-in_game_route_query-4bffd437fda3c098dc92">[ ] unverified</a> | <a href="#case-in_game_route_query-b52ccedcf191462332e7">[ ] unverified</a> | <a href="#case-in_game_route_query-d4402e3bcb0d306c6686">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_route_query-14dc9ca383d5e46eefe9">[ ] unverified</a> | <a href="#case-in_game_route_query-9d552db31acd47b36893">[ ] unverified</a> | <a href="#case-in_game_route_query-a2e5d1703c454ee5007c">[ ] unverified</a> | <a href="#case-in_game_route_query-338b5c73874e056792bc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out | — | <a href="#case-in_game_route_query-98c763da81280e67def4">[ ] unverified</a> | <a href="#case-in_game_route_query-d76bdfbf564c697dd2f9">[ ] unverified</a> | <a href="#case-in_game_route_query-071b50c71752a7ded5b0">[ ] unverified</a> | <a href="#case-in_game_route_query-2c870b7eaba0167e6699">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out</summary>

<a id="case-in_game_route_query-ae295232fcc6398d685f"></a>

**0° CCW: unverified** — `in_game_route_query-ae295232fcc6398d685f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-5b7c8da403e0e8d2593f"></a>

**90° CCW: unverified** — `in_game_route_query-5b7c8da403e0e8d2593f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-2ae4e7e1cf8955e52c07"></a>

**180° CCW: unverified** — `in_game_route_query-2ae4e7e1cf8955e52c07`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-b143230d3c08acd52a6a"></a>

**270° CCW: unverified** — `in_game_route_query-b143230d3c08acd52a6a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_route_query-26ff03bc2f7d4df07262"></a>

**0° CCW: unverified** — `in_game_route_query-26ff03bc2f7d4df07262`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-4bffd437fda3c098dc92"></a>

**90° CCW: unverified** — `in_game_route_query-4bffd437fda3c098dc92`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-b52ccedcf191462332e7"></a>

**180° CCW: unverified** — `in_game_route_query-b52ccedcf191462332e7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-d4402e3bcb0d306c6686"></a>

**270° CCW: unverified** — `in_game_route_query-d4402e3bcb0d306c6686`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_route_query-14dc9ca383d5e46eefe9"></a>

**0° CCW: unverified** — `in_game_route_query-14dc9ca383d5e46eefe9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-9d552db31acd47b36893"></a>

**90° CCW: unverified** — `in_game_route_query-9d552db31acd47b36893`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-a2e5d1703c454ee5007c"></a>

**180° CCW: unverified** — `in_game_route_query-a2e5d1703c454ee5007c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-338b5c73874e056792bc"></a>

**270° CCW: unverified** — `in_game_route_query-338b5c73874e056792bc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out</summary>

<a id="case-in_game_route_query-98c763da81280e67def4"></a>

**0° CCW: unverified** — `in_game_route_query-98c763da81280e67def4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-d76bdfbf564c697dd2f9"></a>

**90° CCW: unverified** — `in_game_route_query-d76bdfbf564c697dd2f9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-071b50c71752a7ded5b0"></a>

**180° CCW: unverified** — `in_game_route_query-071b50c71752a7ded5b0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-2c870b7eaba0167e6699"></a>

**270° CCW: unverified** — `in_game_route_query-2c870b7eaba0167e6699`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out | — | <a href="#case-in_game_visible_travel-ae295232fcc6398d685f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5b7c8da403e0e8d2593f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2ae4e7e1cf8955e52c07">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b143230d3c08acd52a6a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_visible_travel-26ff03bc2f7d4df07262">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4bffd437fda3c098dc92">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b52ccedcf191462332e7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d4402e3bcb0d306c6686">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_visible_travel-14dc9ca383d5e46eefe9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9d552db31acd47b36893">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a2e5d1703c454ee5007c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-338b5c73874e056792bc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out | — | <a href="#case-in_game_visible_travel-98c763da81280e67def4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d76bdfbf564c697dd2f9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-071b50c71752a7ded5b0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2c870b7eaba0167e6699">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out</summary>

<a id="case-in_game_visible_travel-ae295232fcc6398d685f"></a>

**0° CCW: unverified** — `in_game_visible_travel-ae295232fcc6398d685f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-5b7c8da403e0e8d2593f"></a>

**90° CCW: unverified** — `in_game_visible_travel-5b7c8da403e0e8d2593f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-2ae4e7e1cf8955e52c07"></a>

**180° CCW: unverified** — `in_game_visible_travel-2ae4e7e1cf8955e52c07`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-b143230d3c08acd52a6a"></a>

**270° CCW: unverified** — `in_game_visible_travel-b143230d3c08acd52a6a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_visible_travel-26ff03bc2f7d4df07262"></a>

**0° CCW: unverified** — `in_game_visible_travel-26ff03bc2f7d4df07262`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-4bffd437fda3c098dc92"></a>

**90° CCW: unverified** — `in_game_visible_travel-4bffd437fda3c098dc92`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-b52ccedcf191462332e7"></a>

**180° CCW: unverified** — `in_game_visible_travel-b52ccedcf191462332e7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-d4402e3bcb0d306c6686"></a>

**270° CCW: unverified** — `in_game_visible_travel-d4402e3bcb0d306c6686`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_visible_travel-14dc9ca383d5e46eefe9"></a>

**0° CCW: unverified** — `in_game_visible_travel-14dc9ca383d5e46eefe9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-9d552db31acd47b36893"></a>

**90° CCW: unverified** — `in_game_visible_travel-9d552db31acd47b36893`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-a2e5d1703c454ee5007c"></a>

**180° CCW: unverified** — `in_game_visible_travel-a2e5d1703c454ee5007c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-338b5c73874e056792bc"></a>

**270° CCW: unverified** — `in_game_visible_travel-338b5c73874e056792bc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out</summary>

<a id="case-in_game_visible_travel-98c763da81280e67def4"></a>

**0° CCW: unverified** — `in_game_visible_travel-98c763da81280e67def4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-d76bdfbf564c697dd2f9"></a>

**90° CCW: unverified** — `in_game_visible_travel-d76bdfbf564c697dd2f9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-071b50c71752a7ded5b0"></a>

**180° CCW: unverified** — `in_game_visible_travel-071b50c71752a7ded5b0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-2c870b7eaba0167e6699"></a>

**270° CCW: unverified** — `in_game_visible_travel-2c870b7eaba0167e6699`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-77f1c900fe258b7d5ff6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b962b6fe536ab68e2ba5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9e42dbe4d8c032e7b69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de58fa94186672b975b1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c1aa9898b74e78fb2ee7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-596cdda2693897db3299">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aabb8a48204de7204cae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f4f91ef7b4fca15619e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f14f906a332b7beae134">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8e0a8387e970bd7f992">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3431dc10d050044d250">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5968bbcaa52b5543554c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fee520848d6106a41efb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acf05906bedec2d2d32f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eaebf1882733a7c9b277">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15e77d73893e8821c3b2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-286c0dd116f6c195ab83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6ef3bc7d27318c6558c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33136a42ec848cec0198">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b4392b7f29fc4baf932">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-245829ffeaf2fdc2ed4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1fc63f5cb15724262e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33a0bbcecf440f200b96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-539eafa8cfea6d4633ff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5f0dcfd2577fd69658f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a1aeba0c94dc1e1997c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22dc187fb7e74f7cb76b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-945daddc6cb16755f966">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-75bc57c11797c9a1a2bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d2fc132defe18c3d17d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ea9bbee8550ba963589">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a81e35f2d1daf87de937">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c871d332efb39158e9d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2719ba4aa94648dff06a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-765fc20d0157d94f4a04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11d123647dda3b8c9557">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce3e0bada17c8bf3c396">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-436493512f3c59d66840">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c11f3dae1251bb60b75">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8ae5aff2f093177aeab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2473d075ac8d7e555aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43a3beda6d2bb6ba6f69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-167043f04011f3a5b776">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-568ebe503f17dac6cbab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-363ae083d8a0a11e1ea9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3174fd5558d7ce72ef82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d4128241c22ef33ad78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8207f758d399fca50cc8">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-77f1c900fe258b7d5ff6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-77f1c900fe258b7d5ff6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b962b6fe536ab68e2ba5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b962b6fe536ab68e2ba5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9e42dbe4d8c032e7b69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a9e42dbe4d8c032e7b69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de58fa94186672b975b1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de58fa94186672b975b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c1aa9898b74e78fb2ee7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c1aa9898b74e78fb2ee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-596cdda2693897db3299"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-596cdda2693897db3299`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aabb8a48204de7204cae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aabb8a48204de7204cae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f4f91ef7b4fca15619e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6f4f91ef7b4fca15619e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f14f906a332b7beae134"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f14f906a332b7beae134`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8e0a8387e970bd7f992"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e8e0a8387e970bd7f992`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3431dc10d050044d250"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f3431dc10d050044d250`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5968bbcaa52b5543554c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5968bbcaa52b5543554c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fee520848d6106a41efb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fee520848d6106a41efb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acf05906bedec2d2d32f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-acf05906bedec2d2d32f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eaebf1882733a7c9b277"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eaebf1882733a7c9b277`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15e77d73893e8821c3b2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-15e77d73893e8821c3b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-286c0dd116f6c195ab83"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-286c0dd116f6c195ab83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6ef3bc7d27318c6558c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a6ef3bc7d27318c6558c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33136a42ec848cec0198"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-33136a42ec848cec0198`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b4392b7f29fc4baf932"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1b4392b7f29fc4baf932`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-245829ffeaf2fdc2ed4e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-245829ffeaf2fdc2ed4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1fc63f5cb15724262e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a1fc63f5cb15724262e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33a0bbcecf440f200b96"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-33a0bbcecf440f200b96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-539eafa8cfea6d4633ff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-539eafa8cfea6d4633ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5f0dcfd2577fd69658f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5f0dcfd2577fd69658f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a1aeba0c94dc1e1997c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9a1aeba0c94dc1e1997c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22dc187fb7e74f7cb76b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-22dc187fb7e74f7cb76b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-945daddc6cb16755f966"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-945daddc6cb16755f966`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-75bc57c11797c9a1a2bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-75bc57c11797c9a1a2bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d2fc132defe18c3d17d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d2fc132defe18c3d17d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ea9bbee8550ba963589"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ea9bbee8550ba963589`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a81e35f2d1daf87de937"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a81e35f2d1daf87de937`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c871d332efb39158e9d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c871d332efb39158e9d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2719ba4aa94648dff06a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2719ba4aa94648dff06a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-765fc20d0157d94f4a04"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-765fc20d0157d94f4a04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11d123647dda3b8c9557"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-11d123647dda3b8c9557`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce3e0bada17c8bf3c396"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce3e0bada17c8bf3c396`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-436493512f3c59d66840"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-436493512f3c59d66840`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c11f3dae1251bb60b75"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c11f3dae1251bb60b75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8ae5aff2f093177aeab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a8ae5aff2f093177aeab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c2473d075ac8d7e555aa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c2473d075ac8d7e555aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43a3beda6d2bb6ba6f69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-43a3beda6d2bb6ba6f69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-167043f04011f3a5b776"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-167043f04011f3a5b776`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-568ebe503f17dac6cbab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-568ebe503f17dac6cbab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-363ae083d8a0a11e1ea9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-363ae083d8a0a11e1ea9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3174fd5558d7ce72ef82"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3174fd5558d7ce72ef82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d4128241c22ef33ad78"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d4128241c22ef33ad78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8207f758d399fca50cc8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8207f758d399fca50cc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-y-diagonal-stem-split:canonical-southeast | <a href="#case-preview_review-143a57f9e110950ca912">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-diagonal-stem-split:canonical-top | <a href="#case-preview_review-40e2de52e93d437bec09">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-diagonal-stem-split:connection-overview | <a href="#case-preview_review-322df27e759eaaefbbeb">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-y-diagonal-stem-split:canonical-southeast</summary>

<a id="case-preview_review-143a57f9e110950ca912"></a>

**General: unverified** — `preview_review-143a57f9e110950ca912`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-diagonal-stem-split:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-diagonal-stem-split:canonical-top</summary>

<a id="case-preview_review-40e2de52e93d437bec09"></a>

**General: unverified** — `preview_review-40e2de52e93d437bec09`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-diagonal-stem-split:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-diagonal-stem-split:connection-overview</summary>

<a id="case-preview_review-322df27e759eaaefbbeb"></a>

**General: unverified** — `preview_review-322df27e759eaaefbbeb`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-diagonal-stem-split:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested a compact southwest diagonal stem dividing into a northwest diagonal branch and an east orthogonal branch. The lane allocation retains one lane per destination instead of duplicating two lanes onto both branches. Because each ordinary DD deck remains one-way, both branch-to-branch journeys enter on L1 and leave on L2; they therefore use two separate climbs. The complete assembly has three reusable whole-cell owners, keeping every route fragment on a shared city tile with one construction owner.

This component retains its own permanent identity from [piece.jsonc](piece.jsonc). The first physical partition includes native shoulder and support cells as well as routed cells. Model-only cells remain genuinely owned and use empty PATH resources, rather than artificial traffic routes. These design choices are distinct from software acceptance and human game observations.
