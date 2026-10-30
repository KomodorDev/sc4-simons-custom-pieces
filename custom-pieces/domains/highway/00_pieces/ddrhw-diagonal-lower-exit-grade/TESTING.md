---
title: "Testing: DD RHW-4 \u2014 Compact Lower Diagonal Exit Grade"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Compact Lower Diagonal Exit Grade

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Carries part of the lower off-ramp between its highway branch and northwest surface junction. The complete authored ramp curve is about 70.33 m long, including its shoulder lane and level joins; its active height transition is about 35.08 m. Several components share this curve. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -14.245568, 3.000444]; [-0.9442561859245556, -0.3292115662354699]; -0.226761428 | `path-interface-aeabf380377c95bbb5f1` |
| `1-E-in-2` | road / 1 / primary | in | [8.0, -10.207444, 6.745132]; [-0.9793492239542138, -0.2021759074179693]; -0.226757443 | `path-interface-daca863776677fe500f2` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-E-in-2` → `1-W-out-1` | primary |

#### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-lower-exit-grade --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
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

Current totals: unverified: 28, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-lower-exit-grade/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-lower-exit-grade/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-70c60453512517b46bdf">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-70c60453512517b46bdf"></a>

**General: unverified** — `software_resources-70c60453512517b46bdf`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-70c60453512517b46bdf">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-70c60453512517b46bdf"></a>

**General: unverified** — `software_connectivity-70c60453512517b46bdf`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-exit-grade:canonical-southeast | <a href="#case-preview_review-4107bd88756cff6d4f70">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-lower-exit-grade:canonical-top | <a href="#case-preview_review-316304790f3d3b715540">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-exit-grade:canonical-southeast</summary>

<a id="case-preview_review-4107bd88756cff6d4f70"></a>

**General: unverified** — `preview_review-4107bd88756cff6d4f70`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-diagonal-lower-exit-grade:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-lower-exit-grade:canonical-top</summary>

<a id="case-preview_review-316304790f3d3b715540"></a>

**General: unverified** — `preview_review-316304790f3d3b715540`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-diagonal-lower-exit-grade:canonical-top.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-40d510a66cbd1268b779">[ ] unverified</a> | <a href="#case-in_game_render-74244c0e309133b4fafd">[ ] unverified</a> | <a href="#case-in_game_render-0ba0f06d04aee37c5b23">[ ] unverified</a> | <a href="#case-in_game_render-0136ff9b236a76a0709f">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-40d510a66cbd1268b779"></a>

**0° CCW: unverified** — `in_game_render-40d510a66cbd1268b779`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-74244c0e309133b4fafd"></a>

**90° CCW: unverified** — `in_game_render-74244c0e309133b4fafd`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0ba0f06d04aee37c5b23"></a>

**180° CCW: unverified** — `in_game_render-0ba0f06d04aee37c5b23`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0136ff9b236a76a0709f"></a>

**270° CCW: unverified** — `in_game_render-0136ff9b236a76a0709f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-40d510a66cbd1268b779">[ ] unverified</a> | <a href="#case-in_game_placement-74244c0e309133b4fafd">[ ] unverified</a> | <a href="#case-in_game_placement-0ba0f06d04aee37c5b23">[ ] unverified</a> | <a href="#case-in_game_placement-0136ff9b236a76a0709f">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-40d510a66cbd1268b779"></a>

**0° CCW: unverified** — `in_game_placement-40d510a66cbd1268b779`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-74244c0e309133b4fafd"></a>

**90° CCW: unverified** — `in_game_placement-74244c0e309133b4fafd`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0ba0f06d04aee37c5b23"></a>

**180° CCW: unverified** — `in_game_placement-0ba0f06d04aee37c5b23`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0136ff9b236a76a0709f"></a>

**270° CCW: unverified** — `in_game_placement-0136ff9b236a76a0709f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-40d510a66cbd1268b779">[ ] unverified</a> | <a href="#case-in_game_demolition-74244c0e309133b4fafd">[ ] unverified</a> | <a href="#case-in_game_demolition-0ba0f06d04aee37c5b23">[ ] unverified</a> | <a href="#case-in_game_demolition-0136ff9b236a76a0709f">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-40d510a66cbd1268b779"></a>

**0° CCW: unverified** — `in_game_demolition-40d510a66cbd1268b779`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-74244c0e309133b4fafd"></a>

**90° CCW: unverified** — `in_game_demolition-74244c0e309133b4fafd`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0ba0f06d04aee37c5b23"></a>

**180° CCW: unverified** — `in_game_demolition-0ba0f06d04aee37c5b23`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0136ff9b236a76a0709f"></a>

**270° CCW: unverified** — `in_game_demolition-0136ff9b236a76a0709f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-40d510a66cbd1268b779">[ ] unverified</a> | <a href="#case-in_game_save_reload-74244c0e309133b4fafd">[ ] unverified</a> | <a href="#case-in_game_save_reload-0ba0f06d04aee37c5b23">[ ] unverified</a> | <a href="#case-in_game_save_reload-0136ff9b236a76a0709f">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-40d510a66cbd1268b779"></a>

**0° CCW: unverified** — `in_game_save_reload-40d510a66cbd1268b779`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-74244c0e309133b4fafd"></a>

**90° CCW: unverified** — `in_game_save_reload-74244c0e309133b4fafd`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0ba0f06d04aee37c5b23"></a>

**180° CCW: unverified** — `in_game_save_reload-0ba0f06d04aee37c5b23`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0136ff9b236a76a0709f"></a>

**270° CCW: unverified** — `in_game_save_reload-0136ff9b236a76a0709f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-0683906e44185e677044">[ ] unverified</a> | <a href="#case-in_game_route_query-6b743234dd0a07cbabb3">[ ] unverified</a> | <a href="#case-in_game_route_query-e00e1253ee840422c086">[ ] unverified</a> | <a href="#case-in_game_route_query-dc0ec2f87bcd7646751d">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-0683906e44185e677044"></a>

**0° CCW: unverified** — `in_game_route_query-0683906e44185e677044`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-6b743234dd0a07cbabb3"></a>

**90° CCW: unverified** — `in_game_route_query-6b743234dd0a07cbabb3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-e00e1253ee840422c086"></a>

**180° CCW: unverified** — `in_game_route_query-e00e1253ee840422c086`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-dc0ec2f87bcd7646751d"></a>

**270° CCW: unverified** — `in_game_route_query-dc0ec2f87bcd7646751d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-0683906e44185e677044">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6b743234dd0a07cbabb3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e00e1253ee840422c086">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dc0ec2f87bcd7646751d">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-0683906e44185e677044"></a>

**0° CCW: unverified** — `in_game_visible_travel-0683906e44185e677044`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-6b743234dd0a07cbabb3"></a>

**90° CCW: unverified** — `in_game_visible_travel-6b743234dd0a07cbabb3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-e00e1253ee840422c086"></a>

**180° CCW: unverified** — `in_game_visible_travel-e00e1253ee840422c086`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-dc0ec2f87bcd7646751d"></a>

**270° CCW: unverified** — `in_game_visible_travel-dc0ec2f87bcd7646751d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
