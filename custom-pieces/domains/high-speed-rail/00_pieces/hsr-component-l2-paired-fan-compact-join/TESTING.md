---
title: "HSR L2 Compact Paired Fan Join: testing"
summary: "Define this reusable piece’s test scope, setup, software checks, game checks, results, known issues, and design history."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR L2 Compact Paired Fan Join: testing

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

The [piece overview](README.md) contains the pictures, placement instructions, and intrinsic movement matrix. This document contains the corresponding procedures, exact cases, observations, limitations, and historical evidence.

## 1. Test scope

Use the [connection matrix](README.md#3-connection-matrix) to select a directed journey, then open its exact result link here. The measured connections below describe this reusable piece; they do not certify an arbitrary neighbouring piece.

A case is one exact check under stated conditions. Software resource validation, human preview review, game appearance, Route Query, and visible train travel are separate observations. A Route Query line does not prove that a train visibly completed the journey; a software build does not approve either game observation.

The generated sections below supply the exact saved-resource interfaces, supported states, current checklist, and recording command. They do not establish compatibility with an arbitrary neighbour.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Wout` | hsr / 7 / primary | out | [22.398519, -72.0, 15.5]; [-0.9272548089646255, -0.3744309272108488]; 0.0 | `path-interface-0f4b8204e68941486c48` |
| `Nin` | hsr / 7 / primary | in | [46.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nout` | hsr / 7 / primary | out | [50.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Ein` | hsr / 7 / primary | in | [73.601481, -72.0, 15.5]; [-0.9272548089646255, 0.3744309272108488]; 0.0 | `path-interface-d819a6d05c5e43d11db7` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Wout` | primary |
| hsr | `Ein` → `Nout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Read [Piece and placement](README.md#2-piece-and-placement) for the required construction rectangle, complete joining boundaries, approach types, and supported rotations.
2. Follow the [separate build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md) to prepare the matching candidate and its dependencies before a game trial. Use a disposable flat test city, and keep the documented footprint clear.
3. Record the candidate’s actual file hashes, platform, game version, NAM profile, test-city conditions, and chosen rotation. Preserve those details with each observation through the [shared testing procedure](../../../../docs/TESTING.md).

Setup instructions describe a repeatable future test; they do not record a completed installation or successful game run.

## 3. Software checks

### Engineering sources and limits

The construction rectangle remains **7 × 5 tiles**, with **11 owned cells** and **six supports**. Its outer source columns 0 and 6 are empty, while its authoring anchor and retained resource identifiers remain fixed. A structural cell contains physical geometry without a train path; the two current structural cells must remain reserved.

The two fan arms retain opposite travel directions and share the branch angles of the Short Mainline Diverge Core. Their north-facing ends form one paired boundary. Their southern cuts meet curved continuations obliquely, so they have no declared paired-straight profile, section origin, or section offset. The connection cards preserve each cut’s measured endpoint, outward heading, path height, and direction without inventing a centred section.

The [geometry source](geometry.json) owns route samples, physical sweeps, selected cells, and support positions. Independent software contracts inspect encoded endpoints, direction, L2 height, route continuity, curvature, bed coverage, visible rail alignment, supports, and model budgets. These checks do not approve arbitrary neighbours, terrain behaviour, game appearance, or train operation. The generated matrix and checklist retain the scope and current state of each measured or observed result.

Actual saved-resource software checks are recorded in [the current resource-check report](evidence/saved-resource-checks.json). Current canonical picture provenance belongs in [angled-view evidence](evidence/preview.json), [top-view evidence](evidence/preview-top.json), and [connection-overview evidence](evidence/connection-overview.json). The [earlier combined preview report](evidence/design-history/preview-before-junction-rework.json) is preserved as historical evidence for the geometry before this redesign. It does not describe the current pictures.

### Reproduce this piece’s software checks

Run these commands from the repository root, the folder containing `custom-pieces/`, after completing the [shared dependency and native-input preparation](../../../../docs/BUILD_AND_INSTALL.md). Replace `/path/to/Plugins` with the existing NAM Plugins directory, and keep the quotation marks if its path contains spaces. Use a new output directory so an earlier build remains available for comparison.

```sh
python3 -B custom-pieces/scp.py build --include hsr-component-l2-paired-fan-compact-join --output custom-pieces/dist/hsr-l2-paired-fan-review --plugins '/path/to/Plugins'
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/hsr-l2-paired-fan-review
```

Building writes a local development build; verification inspects its saved resources. Neither command installs files or records a game pass. After changing actual resources, follow the [documented extraction, connector, and picture refresh sequence](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md#before-refreshing) for this exact type before using regenerated documentation.

## 4. Game checks

Use the [exact test checklist](#test-checklist) for each required orientation and direction. Record Route Query separately from watching a train complete the same journey. Keep appearance, placement, forbidden movements, demolition, and save/reload observations in their own cases.

Follow the [shared observation procedure](../../../../docs/TESTING.md#record-one-observation) using this piece's [authoritative manual record](checks/manual-tests.json). Record the direction, rotation, platform, game version, NAM profile, and actual evidence for each game result. Only explicit human confirmation records a manual pass. Keep failures, stale results, and historical observations with their original scope.

## 5. Results and known issues

The generated status and checklist below retain the authoritative observations in [checks/manual-tests.json](checks/manual-tests.json), including failures, stale results, and their exact environments. Open an individual case for its evidence and recording scope.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 2/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/8 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/8 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 41, passed: 4, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-join/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-paired-fan-compact-join/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-bc65ebc1e8aece8c8a6d">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-bc65ebc1e8aece8c8a6d"></a>

**General: passed** — `software_resources-bc65ebc1e8aece8c8a6d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus current compiled-resource checks; confirmed at: 2026-10-20T11:45:51.432103+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent compact-fan PATH and model contracts; confirmed at: 2026-10-27T18:29:02.017861+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent compact-fan PATH and model contracts; confirmed at: 2026-10-27T18:41:49.586746+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-bc65ebc1e8aece8c8a6d">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-bc65ebc1e8aece8c8a6d"></a>

**General: passed** — `software_connectivity-bc65ebc1e8aece8c8a6d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus current compiled-resource checks; confirmed at: 2026-10-20T11:45:51.438799+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent compact-fan PATH and model contracts; confirmed at: 2026-10-27T18:29:02.017861+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent compact-fan PATH and model contracts; confirmed at: 2026-10-27T18:41:49.586746+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 1, passed: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast | <a href="#case-preview_review-3cb6c2661802b929620d">[x] passed</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top | <a href="#case-preview_review-f59bcfa100a7ff0db938">[x] passed</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-paired-fan-compact-join:connection-overview | <a href="#case-preview_review-407c1640d6da76516db5">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast</summary>

<a id="case-preview_review-3cb6c2661802b929620d"></a>

**General: passed** — `preview_review-3cb6c2661802b929620d`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-paired-fan-compact-join:canonical-southeast.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-10-27T21:48:27.631996+00:00; evidence: [evidence/fan-width-audit.json]; environment: observation type: software-rendered image review; note: Explicit user approval of the unchanged clean angled and top fan-width review images: yeah looks good. go ahead and rerender the trumpet assembly, refresh the geometry audit. No game observation was supplied.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top</summary>

<a id="case-preview_review-f59bcfa100a7ff0db938"></a>

**General: passed** — `preview_review-f59bcfa100a7ff0db938`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-paired-fan-compact-join:canonical-top.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: user; confirmation method: explicit_user_confirmation; reviewer: User; confirmed at: 2026-10-27T21:48:27.631996+00:00; evidence: [evidence/fan-width-audit.json]; environment: observation type: software-rendered image review; note: Explicit user approval of the unchanged clean angled and top fan-width review images: yeah looks good. go ahead and rerender the trumpet assembly, refresh the geometry audit. No game observation was supplied.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-paired-fan-compact-join:connection-overview</summary>

<a id="case-preview_review-407c1640d6da76516db5"></a>

**General: unverified** — `preview_review-407c1640d6da76516db5`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-paired-fan-compact-join:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_render-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_render-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_render-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_render-2953a796038b1c66047b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_render-9f1c3339be8608575afb`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_render-3ebb754476ae4beaee16`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_render-aa233b7e5bab139363c3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_placement-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_placement-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_placement-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_placement-2953a796038b1c66047b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_placement-9f1c3339be8608575afb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_placement-3ebb754476ae4beaee16`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_placement-aa233b7e5bab139363c3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_demolition-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_demolition-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_demolition-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_demolition-2953a796038b1c66047b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_demolition-9f1c3339be8608575afb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_demolition-3ebb754476ae4beaee16`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_demolition-aa233b7e5bab139363c3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-2953a796038b1c66047b">[ ] unverified</a> | <a href="#case-in_game_save_reload-9f1c3339be8608575afb">[ ] unverified</a> | <a href="#case-in_game_save_reload-3ebb754476ae4beaee16">[ ] unverified</a> | <a href="#case-in_game_save_reload-aa233b7e5bab139363c3">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-2953a796038b1c66047b"></a>

**0° CCW: unverified** — `in_game_save_reload-2953a796038b1c66047b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9f1c3339be8608575afb"></a>

**90° CCW: unverified** — `in_game_save_reload-9f1c3339be8608575afb`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3ebb754476ae4beaee16"></a>

**180° CCW: unverified** — `in_game_save_reload-3ebb754476ae4beaee16`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-aa233b7e5bab139363c3"></a>

**270° CCW: unverified** — `in_game_save_reload-aa233b7e5bab139363c3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_route_query-efa01c69d3d0a595addc">[ ] unverified</a> | <a href="#case-in_game_route_query-f0765824bce6e2085023">[ ] unverified</a> | <a href="#case-in_game_route_query-accf1bc882028a242b30">[ ] unverified</a> | <a href="#case-in_game_route_query-6168c4cc5136e21b2f7b">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout | — | <a href="#case-in_game_route_query-65a9b6549c48f167a40e">[ ] unverified</a> | <a href="#case-in_game_route_query-fe64d25bac6aea848487">[ ] unverified</a> | <a href="#case-in_game_route_query-89e5e4b7f562bc923192">[ ] unverified</a> | <a href="#case-in_game_route_query-cec0cc3b6c354f5dbbcf">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_route_query-efa01c69d3d0a595addc"></a>

**0° CCW: unverified** — `in_game_route_query-efa01c69d3d0a595addc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-f0765824bce6e2085023"></a>

**90° CCW: unverified** — `in_game_route_query-f0765824bce6e2085023`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-accf1bc882028a242b30"></a>

**180° CCW: unverified** — `in_game_route_query-accf1bc882028a242b30`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-6168c4cc5136e21b2f7b"></a>

**270° CCW: unverified** — `in_game_route_query-6168c4cc5136e21b2f7b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout</summary>

<a id="case-in_game_route_query-65a9b6549c48f167a40e"></a>

**0° CCW: unverified** — `in_game_route_query-65a9b6549c48f167a40e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-fe64d25bac6aea848487"></a>

**90° CCW: unverified** — `in_game_route_query-fe64d25bac6aea848487`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-89e5e4b7f562bc923192"></a>

**180° CCW: unverified** — `in_game_route_query-89e5e4b7f562bc923192`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_route_query-cec0cc3b6c354f5dbbcf"></a>

**270° CCW: unverified** — `in_game_route_query-cec0cc3b6c354f5dbbcf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_visible_travel-efa01c69d3d0a595addc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f0765824bce6e2085023">[ ] unverified</a> | <a href="#case-in_game_visible_travel-accf1bc882028a242b30">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6168c4cc5136e21b2f7b">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout | — | <a href="#case-in_game_visible_travel-65a9b6549c48f167a40e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fe64d25bac6aea848487">[ ] unverified</a> | <a href="#case-in_game_visible_travel-89e5e4b7f562bc923192">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cec0cc3b6c354f5dbbcf">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_visible_travel-efa01c69d3d0a595addc"></a>

**0° CCW: unverified** — `in_game_visible_travel-efa01c69d3d0a595addc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-f0765824bce6e2085023"></a>

**90° CCW: unverified** — `in_game_visible_travel-f0765824bce6e2085023`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-accf1bc882028a242b30"></a>

**180° CCW: unverified** — `in_game_visible_travel-accf1bc882028a242b30`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-6168c4cc5136e21b2f7b"></a>

**270° CCW: unverified** — `in_game_visible_travel-6168c4cc5136e21b2f7b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout</summary>

<a id="case-in_game_visible_travel-65a9b6549c48f167a40e"></a>

**0° CCW: unverified** — `in_game_visible_travel-65a9b6549c48f167a40e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-fe64d25bac6aea848487"></a>

**90° CCW: unverified** — `in_game_visible_travel-fe64d25bac6aea848487`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-89e5e4b7f562bc923192"></a>

**180° CCW: unverified** — `in_game_visible_travel-89e5e4b7f562bc923192`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_visible_travel-cec0cc3b6c354f5dbbcf"></a>

**270° CCW: unverified** — `in_game_visible_travel-cec0cc3b6c354f5dbbcf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3ad08e7a19456cd90fd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d4bf82777d040a92574">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8a6e6bba23dded7d7ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-690df8549dc3f5fda576">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97aa23dd677c7b8c9e3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf602616988bd0a9a85a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c35a186b255281e199c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c046e5e0bc2afa332fca">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3ad08e7a19456cd90fd0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3ad08e7a19456cd90fd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d4bf82777d040a92574"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d4bf82777d040a92574`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8a6e6bba23dded7d7ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f8a6e6bba23dded7d7ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-690df8549dc3f5fda576"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-690df8549dc3f5fda576`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97aa23dd677c7b8c9e3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97aa23dd677c7b8c9e3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf602616988bd0a9a85a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf602616988bd0a9a85a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c35a186b255281e199c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c35a186b255281e199c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c046e5e0bc2afa332fca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c046e5e0bc2afa332fca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The retained evidence describes the version and scope recorded by its original report. A documentation reorganization does not create a new test run or extend an earlier observation to different inputs.
