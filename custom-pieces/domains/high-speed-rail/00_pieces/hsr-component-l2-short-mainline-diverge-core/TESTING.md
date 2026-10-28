---
title: "HSR L2 Short Mainline Diverge Core: testing"
summary: "Define this reusable piece’s test scope, setup, software checks, game checks, results, known issues, and design history."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR L2 Short Mainline Diverge Core: testing

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

The [piece overview](README.md) contains the pictures, placement instructions, and intrinsic movement matrix. This document contains the corresponding procedures, exact cases, observations, limitations, and historical evidence.

## 1. Test scope

Use the [connection matrix](README.md#3-connection-matrix) to select a directed journey, then open its exact result link here. The measured connections below describe this reusable piece; they do not certify an arbitrary neighbouring piece.

A case is one exact check under stated conditions. Saved-resource software checks, human preview review, game appearance, Route Query, and visible train travel are separate observations. A Route Query line does not prove that a train visibly completed a journey. Only explicit human confirmation can record a manual pass.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Win` | hsr / 7 / primary | in | [-8.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Wout` | hsr / 7 / primary | out | [-8.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Sout` | hsr / 7 / primary | out | [38.398519, -8.0, 15.5]; [0.9272548089646255, -0.3744309272108488]; 0.0 | `path-interface-d819a6d05c5e43d11db7` |
| `Eout` | hsr / 7 / primary | out | [56.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Ein` | hsr / 7 / primary | in | [56.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Win` → `Sout` | primary |
| hsr | `Win` → `Eout` | primary |
| hsr | `Ein` → `Wout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Win` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Read [Piece and placement](README.md#2-piece-and-placement) for the required construction rectangle, complete joining boundaries, approach types, and supported rotations.
2. Follow the [separate build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md) to prepare the matching candidate and its dependencies before a game trial. Use a disposable flat test city, and keep the documented footprint clear.
3. Record the candidate’s actual file hashes, platform, game version, NAM profile, test-city conditions, and chosen rotation. Preserve those details with each observation through the [shared testing procedure](../../../../docs/TESTING.md).

Setup instructions describe a repeatable future test; they do not record a completed installation or successful game run.

## 3. Software checks

The current [presentation-refresh record](evidence/presentation-refresh.json) identifies the canonical angled view, bright-green top grid, and connection overview rendered from the unchanged verified `dist/trumpet-fan-core-parts-final-01` resources. It records the current connector re-extraction and freshness checks, exact image hashes, and preserved observations. Earlier saved-resource and documentation-refresh reports retain their original native-check facts and picture fingerprints; this presentation refresh does not claim another geometry build or game observation.

### Engineering contract

The current documentation uses the saved piece from the verified X3 right-border extension build, with the previously accepted left curve preserved. A parapet is the raised grey border. Its left side stays straight into X1, then follows the branch's brown ballast outline into the existing grey border at the bottom of X2. There is no perpendicular cap, or closing end face, on this continuous left border. The right border in X3 now follows the branch’s inside ballast outline into the retained curved grey border, with a continuous top and inside wall and no perpendicular end cap. [Saved-resource evidence](evidence/saved-resource-checks.json) identifies the current source DAT, independent border checks, routes, models, construction rules, and shadows. The [before/after comparison](evidence/parapet-alignment.json) records what changed and what remained identical. Construction, traffic demand, demolition, shadows, and save/reload remain separate game checks.

The straight border retains its native 1.5034523 m thickness. The curved continuation follows the existing branch profile: its inside edge lies 2.6 m from the route centreline, and its outside edge lies 4.0 m from that line, giving a nominal 1.4 m band measured perpendicular to the curve. The existing tile boundaries still clip the surface where it leaves this piece. The saved-model audit checks **23 top-surface sections** and **27 inside-wall sections** across the straight sections, accepted left bend, right curved join, and retained wings. It rejects the former perpendicular left and right end caps and checks that the new right top has no duplicate faces. The rails, PATH resources, supports, existing curved border, and directional joining measurements retain their previous geometry.

The right join uses the branch’s existing **2.6 m inside offset**. It replaces the former square end at local east **43.776078283 m**. The following source-backed joining coordinates identify where the new border meets the straight mainline’s inside and outside edges. They are checked against the actual saved model and do not come from image pixels.

| Point on the new right join | Local east (m) | Local south (m) | Extension west from the former end (m) |
| --- | ---: | ---: | ---: |
| Inside edge | 40.361872523 | 5.996547699 | 3.414205759 |
| Outside edge | 43.669002830 | 7.500000000 | 0.107075453 |

East increases toward the right of the top view, and south increases toward its bottom. These local metre coordinates use the centre of X0 as their horizontal reference. X3 spans east **40–56 m**, so both joining points lie in X3. The different extension lengths form the curved join into the existing grey border; the repair does not add a longer rectangular strip with another square end.

The required train corridor remains 5.0 m wide, meaning 2.5 m of clear space on each side of the route centreline. The minimum distance from the actual saved left-border top surface to the complete unchanged branch centreline is 2.599999746 m, approximately the authored 2.6 m offset and approximately 0.1 m beyond the required half-width. The earlier straight-cap corner measurement and its local clipping-mask exception belong only to the superseded attempt; they do not describe the current continuous curve. This border repair does not reduce the required train corridor or certify game operation. The existing custom branch-cut limits and their separate assembly-check requirement remain in force.

The [snapshot before the X3 extension](evidence/design-history/before-right-border-extension/index.json) retains the previous exact source, reports, connector records, observations, and images. Its flat right end remains historical evidence. Original observation dictionaries and dependency fingerprints remain unchanged; the current resource report maps each earlier software result to its preserved report. No new human approval or game observation is inferred. Complete trumpet assembly integration and rendering remain deferred.

## 4. Game checks

Use the [exact test checklist](#test-checklist) for each required orientation and direction. Record Route Query separately from watching a train complete the same journey. Keep appearance, placement, forbidden movements, demolition, and save/reload observations in their own cases.

Follow the [shared observation procedure](../../../../docs/TESTING.md#record-one-observation) with this piece’s [authoritative test record](checks/manual-tests.json). Preserve failures, stale observations, and their original scope. The generated sections below provide the exact recording command and case identifiers.

## 5. Results and known issues

The generated status and checklist below retain the authoritative observations in [checks/manual-tests.json](checks/manual-tests.json), including failures, stale results, and their exact environments. Open an individual case for its evidence and recording scope.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/12 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/12 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 55, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-short-mainline-diverge-core/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-short-mainline-diverge-core/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-1be6a14c7095a92ca6a3">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-1be6a14c7095a92ca6a3"></a>

**General: passed** — `software_resources-1be6a14c7095a92ca6a3`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:34.857695+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Fresh one-piece normal saved-build verification, independent south-parapet audit, and selected actual-resource extraction; confirmed at: 2026-10-28T13:09:27.334362+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Fresh one-piece saved-build verification, continuous-left-border surface/wall audit, and selected actual-resource extraction; confirmed at: 2026-10-28T14:39:59.377541+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Current one-piece native saved-build verification, independent X3 right-border join and preserved-left-curve audits, selected actual PATH extraction, and connector freshness check; confirmed at: 2026-10-28T16:06:04.312391+00:00; evidence: [evidence/saved-resource-checks.json, evidence/parapet-alignment.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-1be6a14c7095a92ca6a3">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-1be6a14c7095a92ca6a3"></a>

**General: passed** — `software_connectivity-1be6a14c7095a92ca6a3`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:34.865101+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Fresh one-piece normal saved-build verification, independent south-parapet audit, and selected actual-resource extraction; confirmed at: 2026-10-28T13:09:27.334362+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Fresh one-piece saved-build verification, continuous-left-border surface/wall audit, and selected actual-resource extraction; confirmed at: 2026-10-28T14:39:59.377541+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Current one-piece native saved-build verification, independent X3 right-border join and preserved-left-curve audits, selected actual PATH extraction, and connector freshness check; confirmed at: 2026-10-28T16:06:04.312391+00:00; evidence: [evidence/saved-resource-checks.json, evidence/parapet-alignment.json]; environment: {}

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-5b28106d377daf5b6fa0">[ ] unverified</a> | <a href="#case-in_game_render-7befb4ecda34633d72ed">[ ] unverified</a> | <a href="#case-in_game_render-150e1f8cad64f39a2e4b">[ ] unverified</a> | <a href="#case-in_game_render-3571a612233cd36909b7">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-5b28106d377daf5b6fa0"></a>

**0° CCW: unverified** — `in_game_render-5b28106d377daf5b6fa0`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7befb4ecda34633d72ed"></a>

**90° CCW: unverified** — `in_game_render-7befb4ecda34633d72ed`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-150e1f8cad64f39a2e4b"></a>

**180° CCW: unverified** — `in_game_render-150e1f8cad64f39a2e4b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3571a612233cd36909b7"></a>

**270° CCW: unverified** — `in_game_render-3571a612233cd36909b7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-5b28106d377daf5b6fa0">[ ] unverified</a> | <a href="#case-in_game_placement-7befb4ecda34633d72ed">[ ] unverified</a> | <a href="#case-in_game_placement-150e1f8cad64f39a2e4b">[ ] unverified</a> | <a href="#case-in_game_placement-3571a612233cd36909b7">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-5b28106d377daf5b6fa0"></a>

**0° CCW: unverified** — `in_game_placement-5b28106d377daf5b6fa0`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7befb4ecda34633d72ed"></a>

**90° CCW: unverified** — `in_game_placement-7befb4ecda34633d72ed`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-150e1f8cad64f39a2e4b"></a>

**180° CCW: unverified** — `in_game_placement-150e1f8cad64f39a2e4b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3571a612233cd36909b7"></a>

**270° CCW: unverified** — `in_game_placement-3571a612233cd36909b7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-5b28106d377daf5b6fa0">[ ] unverified</a> | <a href="#case-in_game_demolition-7befb4ecda34633d72ed">[ ] unverified</a> | <a href="#case-in_game_demolition-150e1f8cad64f39a2e4b">[ ] unverified</a> | <a href="#case-in_game_demolition-3571a612233cd36909b7">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-5b28106d377daf5b6fa0"></a>

**0° CCW: unverified** — `in_game_demolition-5b28106d377daf5b6fa0`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7befb4ecda34633d72ed"></a>

**90° CCW: unverified** — `in_game_demolition-7befb4ecda34633d72ed`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-150e1f8cad64f39a2e4b"></a>

**180° CCW: unverified** — `in_game_demolition-150e1f8cad64f39a2e4b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3571a612233cd36909b7"></a>

**270° CCW: unverified** — `in_game_demolition-3571a612233cd36909b7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-5b28106d377daf5b6fa0">[ ] unverified</a> | <a href="#case-in_game_save_reload-7befb4ecda34633d72ed">[ ] unverified</a> | <a href="#case-in_game_save_reload-150e1f8cad64f39a2e4b">[ ] unverified</a> | <a href="#case-in_game_save_reload-3571a612233cd36909b7">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-5b28106d377daf5b6fa0"></a>

**0° CCW: unverified** — `in_game_save_reload-5b28106d377daf5b6fa0`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7befb4ecda34633d72ed"></a>

**90° CCW: unverified** — `in_game_save_reload-7befb4ecda34633d72ed`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-150e1f8cad64f39a2e4b"></a>

**180° CCW: unverified** — `in_game_save_reload-150e1f8cad64f39a2e4b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3571a612233cd36909b7"></a>

**270° CCW: unverified** — `in_game_save_reload-3571a612233cd36909b7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout | — | <a href="#case-in_game_route_query-6d0026d836d5154be176">[ ] unverified</a> | <a href="#case-in_game_route_query-f080eb7136ac872f4f8d">[ ] unverified</a> | <a href="#case-in_game_route_query-f6edfc9aa1e2ff11c3d8">[ ] unverified</a> | <a href="#case-in_game_route_query-1e8cc484450cd566a0aa">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_route_query-73c9e40447db7eca5d77">[ ] unverified</a> | <a href="#case-in_game_route_query-d36bbc1685e39cff4604">[ ] unverified</a> | <a href="#case-in_game_route_query-820fc48049ad97989483">[ ] unverified</a> | <a href="#case-in_game_route_query-23b20dbb37e7252472f9">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_route_query-184484f7197e20662425">[ ] unverified</a> | <a href="#case-in_game_route_query-1b7f0add07635c0c9883">[ ] unverified</a> | <a href="#case-in_game_route_query-cac25e7640a3a03b10d8">[ ] unverified</a> | <a href="#case-in_game_route_query-8da684985233114279c5">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout</summary>

<a id="case-in_game_route_query-6d0026d836d5154be176"></a>

**0° CCW: unverified** — `in_game_route_query-6d0026d836d5154be176`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-f080eb7136ac872f4f8d"></a>

**90° CCW: unverified** — `in_game_route_query-f080eb7136ac872f4f8d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-f6edfc9aa1e2ff11c3d8"></a>

**180° CCW: unverified** — `in_game_route_query-f6edfc9aa1e2ff11c3d8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-1e8cc484450cd566a0aa"></a>

**270° CCW: unverified** — `in_game_route_query-1e8cc484450cd566a0aa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_route_query-73c9e40447db7eca5d77"></a>

**0° CCW: unverified** — `in_game_route_query-73c9e40447db7eca5d77`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-d36bbc1685e39cff4604"></a>

**90° CCW: unverified** — `in_game_route_query-d36bbc1685e39cff4604`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-820fc48049ad97989483"></a>

**180° CCW: unverified** — `in_game_route_query-820fc48049ad97989483`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-23b20dbb37e7252472f9"></a>

**270° CCW: unverified** — `in_game_route_query-23b20dbb37e7252472f9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_route_query-184484f7197e20662425"></a>

**0° CCW: unverified** — `in_game_route_query-184484f7197e20662425`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-1b7f0add07635c0c9883"></a>

**90° CCW: unverified** — `in_game_route_query-1b7f0add07635c0c9883`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-cac25e7640a3a03b10d8"></a>

**180° CCW: unverified** — `in_game_route_query-cac25e7640a3a03b10d8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-8da684985233114279c5"></a>

**270° CCW: unverified** — `in_game_route_query-8da684985233114279c5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout | — | <a href="#case-in_game_visible_travel-6d0026d836d5154be176">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f080eb7136ac872f4f8d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f6edfc9aa1e2ff11c3d8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1e8cc484450cd566a0aa">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_visible_travel-73c9e40447db7eca5d77">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d36bbc1685e39cff4604">[ ] unverified</a> | <a href="#case-in_game_visible_travel-820fc48049ad97989483">[ ] unverified</a> | <a href="#case-in_game_visible_travel-23b20dbb37e7252472f9">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_visible_travel-184484f7197e20662425">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1b7f0add07635c0c9883">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cac25e7640a3a03b10d8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8da684985233114279c5">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout</summary>

<a id="case-in_game_visible_travel-6d0026d836d5154be176"></a>

**0° CCW: unverified** — `in_game_visible_travel-6d0026d836d5154be176`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-f080eb7136ac872f4f8d"></a>

**90° CCW: unverified** — `in_game_visible_travel-f080eb7136ac872f4f8d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-f6edfc9aa1e2ff11c3d8"></a>

**180° CCW: unverified** — `in_game_visible_travel-f6edfc9aa1e2ff11c3d8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-1e8cc484450cd566a0aa"></a>

**270° CCW: unverified** — `in_game_visible_travel-1e8cc484450cd566a0aa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_visible_travel-73c9e40447db7eca5d77"></a>

**0° CCW: unverified** — `in_game_visible_travel-73c9e40447db7eca5d77`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-d36bbc1685e39cff4604"></a>

**90° CCW: unverified** — `in_game_visible_travel-d36bbc1685e39cff4604`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-820fc48049ad97989483"></a>

**180° CCW: unverified** — `in_game_visible_travel-820fc48049ad97989483`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-23b20dbb37e7252472f9"></a>

**270° CCW: unverified** — `in_game_visible_travel-23b20dbb37e7252472f9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_visible_travel-184484f7197e20662425"></a>

**0° CCW: unverified** — `in_game_visible_travel-184484f7197e20662425`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-1b7f0add07635c0c9883"></a>

**90° CCW: unverified** — `in_game_visible_travel-1b7f0add07635c0c9883`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-cac25e7640a3a03b10d8"></a>

**180° CCW: unverified** — `in_game_visible_travel-cac25e7640a3a03b10d8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-8da684985233114279c5"></a>

**270° CCW: unverified** — `in_game_visible_travel-8da684985233114279c5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-305dc860de6ca3c81de5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cbaea5971ea5d4d66ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3c46a596eba0a86626d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27d0b92decc6925bd802">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-959b05f5b375b9250b7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4c71b2e80b8da6a8859">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a07d73b10cb5071a1f58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7c31ab107da46952bdb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cd77fab872666f8fde8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88fc210200e0877a9132">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df387881032facf6b964">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11c688851431796030a6">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-305dc860de6ca3c81de5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-305dc860de6ca3c81de5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cbaea5971ea5d4d66ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2cbaea5971ea5d4d66ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3c46a596eba0a86626d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b3c46a596eba0a86626d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27d0b92decc6925bd802"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27d0b92decc6925bd802`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-959b05f5b375b9250b7b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-959b05f5b375b9250b7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4c71b2e80b8da6a8859"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a4c71b2e80b8da6a8859`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a07d73b10cb5071a1f58"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a07d73b10cb5071a1f58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7c31ab107da46952bdb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7c31ab107da46952bdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cd77fab872666f8fde8f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd77fab872666f8fde8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88fc210200e0877a9132"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-88fc210200e0877a9132`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df387881032facf6b964"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-df387881032facf6b964`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11c688851431796030a6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-11c688851431796030a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-short-mainline-diverge-core:canonical-southeast | <a href="#case-preview_review-44db441b6df7ca3395fc">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-short-mainline-diverge-core:canonical-top | <a href="#case-preview_review-c0f82e508ffbc60632bb">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-short-mainline-diverge-core:connection-overview | <a href="#case-preview_review-372750160002ee7c7ac4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-mainline-diverge-core:canonical-southeast</summary>

<a id="case-preview_review-44db441b6df7ca3395fc"></a>

**General: unverified** — `preview_review-44db441b6df7ca3395fc`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-short-mainline-diverge-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-mainline-diverge-core:canonical-top</summary>

<a id="case-preview_review-c0f82e508ffbc60632bb"></a>

**General: unverified** — `preview_review-c0f82e508ffbc60632bb`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-short-mainline-diverge-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-mainline-diverge-core:connection-overview</summary>

<a id="case-preview_review-372750160002ee7c7ac4"></a>

**General: unverified** — `preview_review-372750160002ee7c7ac4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-short-mainline-diverge-core:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The retained evidence describes the version and scope recorded by its original report. A documentation reorganization does not create a new test run or extend an earlier observation to different inputs.

The [saved-resource report before the south-parapet repair](evidence/design-history/saved-resource-checks-before-south-parapet-alignment.json) preserves the original measured results. The [superseded straight-cap attempt](evidence/design-history/straight-cap-attempt/index.json) preserves its exact geometry, observations, reports, and images; its left perpendicular end was replaced after clarification that the border must follow the curve into the existing grey wing. That attempt's software passes retain their original scope, and the current continuity audit correctly rejects its old shape. The current repair preserves the original floor and rail triangles, supports, existing curved wing, PATH resources, identifiers, and shadows. Earlier observations keep their original dependency fingerprints; the current saved-resource report maps their software evidence to the retained historical reports. The complete assembly's artwork and integration checks remain deferred while further piece repairs continue.

The construction rectangle is 4 × 1 tiles, with four occupied cells and four authored supports. Source [column,row] cells increase eastward and southward; the picture’s Y axis increases northward. The smaller core was extracted from an earlier longer type: its historical tail deviation was 4.018 mm, and a separate neighbouring smooth-join correction was bounded at 24.5 mm. The [historical atomization ledger](../../01_assemblies/straight-stem-trumpet/checks/atomization.json) records that decision. Those historical measurements do not establish new neighbour compatibility or game operation.
