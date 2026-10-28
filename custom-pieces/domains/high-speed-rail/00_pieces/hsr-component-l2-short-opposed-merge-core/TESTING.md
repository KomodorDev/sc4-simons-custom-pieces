---
title: "HSR L2 Short Opposed Merge Core: testing"
summary: "Define this reusable piece’s test scope, setup, software checks, game checks, results, known issues, and design history."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR L2 Short Opposed Merge Core: testing

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
| `Win` | hsr / 7 / primary | in | [-8.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Wout` | hsr / 7 / primary | out | [-8.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Sin` | hsr / 7 / primary | in | [9.601481, -8.0, 15.5]; [0.9272548089646255, 0.3744309272108488]; 0.0 | `path-interface-0f4b8204e68941486c48` |
| `Nin` | hsr / 7 / primary | in | [38.398519, 8.0, 15.5]; [-0.9272548089646255, -0.3744309272108488]; 0.0 | `path-interface-0f4b8204e68941486c48` |
| `Eout` | hsr / 7 / primary | out | [56.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Ein` | hsr / 7 / primary | in | [56.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Win` → `Eout` | primary |
| hsr | `Sin` → `Eout` | primary |
| hsr | `Nin` → `Wout` | primary |
| hsr | `Ein` → `Wout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Win` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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

### Engineering sources and limits

The construction rectangle contains **4 × 1 tiles**, and all **four cells** are owned. Four supports remain centred along the mainline at 16 m intervals. Both paired mainline ends are ordinary, flat L2 boundaries; the northern and southern branch entrances are custom oblique cuts. The former western tile is now a separate placement of the existing paired straight, which owns that tile and its support.

The retained source cells were previously columns 1–4 of the five-tile core. Their local east coordinates are rebased by −16 m, and the core's assembly position moves +16 m east; the two changes preserve the retained geometry's world positions. The earlier west-tail extraction applied a bounded adjustment to the upper northern parapet and adjacent upper bed strip within **2.5 m** of the new western boundary, by at most **3.4524 mm**. The ballast-following border revision below keeps the original bed adjustment and supplies the native upper concrete directly. The [collar proof](evidence/west-parapet-collar-proof.json) measures a maximum of **3.452301025 mm**. The rail region, slab underside, pier, outside connections, and support positions are preserved. Intersecting triangles are partitioned at the blend boundaries, and texture coordinates at new vertices are interpolated; the deformation can change where the texture falls inside the collar.

That historical collar proof performed **6,518 finite section checks** at three heights and found **zero new gaps above 2 micrometres** in that scan. A micrometre is 0.001 mm. This finite scan is not an unrestricted proof that every surface is watertight. The later [complete-assembly extraction audit](../../01_assemblies/straight-stem-trumpet/evidence/merge-west-tail-extraction.json) independently checks the saved seam at all five zooms, six native joining sections, and 87 collar sections, using the declared position and gap tolerances.

The northern merge reuses the Short Mainline Diverge Core’s branch samples after reflecting the north/south coordinate and reversing travel. Both mainline routes, the direct southern route fragments, and each analytic context’s southern deck retain their earlier source values. The branch tracks are separate physical channels until their measured internal journeys merge into the appropriate mainline track; assigning them one component does not permit extra transfers.

The [geometry source](geometry.json) owns route samples, physical sweeps, selected cells, and support positions. Independent software contracts inspect encoded endpoints, direction, L2 height, route continuity, curvature, bed coverage, visible rail alignment, supports, and model budgets. These checks do not approve arbitrary neighbours, terrain behaviour, game appearance, or train operation. The generated matrix and checklist retain the scope and current state of each measured or observed result.

### Ballast-following concrete borders

The raised grey border continues along the northern branch's inside ballast outline from X1 into the retained curved concrete at the top of X2. The southern border follows the corresponding curve from X2 into the retained concrete at the bottom of X1. These accepted continuous banks remain intact. Positions use the standalone top view's authored 0° orientation; every cell is in Y0. The separate northern strip in X3 and southern strip in X0 now follow their actual branch ballast boundaries into the original curved wings, including the matching inside walls. The earlier perpendicular end faces are removed, so neither strip stops at a square cap before its curved wing.

The continuous sections follow the existing branch's exact mitered offsets at **2.6 m** from its centreline, while the existing minimum train half-width remains **2.5 m**. Both the concrete top and the inside wall continue into the original curved wing. The straight native parapet spans approximately **5.9965477–7.5 m** from the mainline centre; the branch profile uses a different reviewed width. Neither profile is narrowed to make the correction pass.

The source-derived northern X3 join follows the sampled ballast curve between [east,north] **[40.361872523,5.996547699] m** at the inside edge and **[43.654740688,7.5] m** at the outside edge. The southern X0 join follows the corresponding curve between [east,south] **[7.638127477,5.996547699] m** and **[4.330997170,7.5] m**. East increases rightward; north increases upward, and south increases downward in the top picture. These are source-backed join coordinates that the independent saved-model checks verify, rather than measurements read from pixels.

The [saved-model comparison](evidence/parapet-alignment.json) records the actual accepted-bank baseline and current DAT hashes, raised-top sections, inside-wall coverage, absence of the former flat caps, preserved continuous banks, resource identities, and unchanged encoded floor, rail, support, and original wing triangles. The independent checker rejects the earlier square-ended strips, interrupted tops, missing inside walls, overlapping faces, and concrete across the required branch openings. It runs alongside the existing complete-model train-clearance check. The [regression tests](../../tests/test_hsr_opposed_parapet.py) include positive controls and deliberate broken shapes.

The [current resource-check report](evidence/saved-resource-checks.json) identifies the one-piece build in `dist/opposed-outer-border-joined` and its normal saved-resource verification. The two complete analytic surface contexts were compiled for this correction, and the production west-collar normalizer ran against the measured new raw west-cell signature. The repaired upper concrete already supplies the native western profile, so this opt-in revision preserves those above-bed faces directly while retaining the original ballast-floor warp exactly; applying the old concrete displacement a second time would narrow the native joining profile by another 3.4523 mm. The current `opposed_parapet_alignment` rule adds the two outer curved joins while retaining its accepted continuous-bank values. All geometry outside that rule and the earlier west-collar definition retain their exact source values. Reusing those newly computed context models inside the same ordinary build does not introduce a different geometry source.

The canonical [angled-view evidence](evidence/preview.json), [top-view evidence](evidence/preview-top.json), and [connection-overview evidence](evidence/connection-overview.json) identify the current saved model. The [original border-repair snapshot](evidence/design-history/before-ballast-border-repair/index.json) preserves the state before the continuous banks were repaired. The [accepted-bank snapshot](evidence/design-history/before-outer-border-joins/index.json) preserves the exact source, artwork, reports, connector records, and observations before the subsequent X0/X3 curved joins. Earlier reports and observation dictionaries retain their exact original fingerprints and source scope; current evidence maps their active-path references to the corresponding preserved reports. Earlier whole-assembly and west-tail extraction proofs do not certify this border revision's assembled fit. The trumpet assembly has not been rebuilt or rerendered for these changes, and no new human approval or game observation is inferred.

The original five-tile [saved-resource report](evidence/design-history/saved-resource-checks-before-west-tail-extraction.json), [angled-view report](evidence/design-history/preview-before-west-tail-extraction.json), [top-view report](evidence/design-history/preview-top-before-west-tail-extraction.json), and [connection-overview report](evidence/design-history/connection-overview-before-west-tail-extraction.json) retain their original fingerprints and results. The [earlier combined preview report](evidence/design-history/preview-before-junction-rework.json) describes an even earlier stage before the branch-angle redesign and also remains historical.

### Reproduce this piece’s software checks

Run these commands from the repository root, the folder containing `custom-pieces/`, after completing the [shared dependency and native-input preparation](../../../../docs/BUILD_AND_INSTALL.md). Replace `/path/to/Plugins` with the existing NAM Plugins directory, and keep the quotation marks if its path contains spaces. Use a new output directory so an earlier build remains available for comparison.

```sh
python3 -B custom-pieces/scp.py build --include hsr-component-l2-short-opposed-merge-core --output custom-pieces/dist/hsr-l2-opposed-merge-review --plugins '/path/to/Plugins'
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/hsr-l2-opposed-merge-review
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

Current totals: unverified: 67, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-short-opposed-merge-core/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-short-opposed-merge-core/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-bb298338ce132e94abe3">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-bb298338ce132e94abe3"></a>

**General: passed** — `software_resources-bb298338ce132e94abe3`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:34.956270+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent atomic opposed-merge PATH and model contracts; confirmed at: 2026-10-27T18:29:44.936700+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent atomic opposed-merge PATH and model contracts; confirmed at: 2026-10-27T18:41:49.788201+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Current saved-resource verifier and independent one-plus-four extraction/assembly controls; confirmed at: 2026-10-28T09:50:03.583685+00:00; evidence: [evidence/saved-resource-checks.json, evidence/west-parapet-collar-proof.json]; environment: {}
- result: passed; authority: software; reviewer: Current one-piece normal saved-build verification, independent continuous opposed-border audit, and selected actual-resource extraction; confirmed at: 2026-10-28T15:43:47.113215+00:00; evidence: [evidence/saved-resource-checks.json, evidence/parapet-alignment.json]; environment: {}
- result: passed; authority: software; reviewer: Current one-piece native saved-build verification, independent X0/X3 curved-join and retained continuous-bank audits, selected actual PATH extraction, and connector freshness check; confirmed at: 2026-10-28T16:37:56.742438+00:00; evidence: [evidence/saved-resource-checks.json, evidence/parapet-alignment.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-bb298338ce132e94abe3">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-bb298338ce132e94abe3"></a>

**General: passed** — `software_connectivity-bb298338ce132e94abe3`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:34.964878+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent atomic opposed-merge PATH and model contracts; confirmed at: 2026-10-27T18:29:44.936700+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Normal saved-build verifier with independent atomic opposed-merge PATH and model contracts; confirmed at: 2026-10-27T18:41:49.788201+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}
- result: passed; authority: software; reviewer: Current saved-resource verifier and independent one-plus-four extraction/assembly controls; confirmed at: 2026-10-28T09:50:03.583685+00:00; evidence: [evidence/saved-resource-checks.json, evidence/west-parapet-collar-proof.json]; environment: {}
- result: passed; authority: software; reviewer: Current one-piece normal saved-build verification, independent continuous opposed-border audit, and selected actual-resource extraction; confirmed at: 2026-10-28T15:43:47.113215+00:00; evidence: [evidence/saved-resource-checks.json, evidence/parapet-alignment.json]; environment: {}
- result: passed; authority: software; reviewer: Current one-piece native saved-build verification, independent X0/X3 curved-join and retained continuous-bank audits, selected actual PATH extraction, and connector freshness check; confirmed at: 2026-10-28T16:37:56.742438+00:00; evidence: [evidence/saved-resource-checks.json, evidence/parapet-alignment.json]; environment: {}

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-5fa20a2de78ef24ee969">[ ] unverified</a> | <a href="#case-in_game_render-44036cf5ca9c219e69b6">[ ] unverified</a> | <a href="#case-in_game_render-e0bbb6e7f63828f7273a">[ ] unverified</a> | <a href="#case-in_game_render-64d5cec7500a6a74eb63">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-5fa20a2de78ef24ee969"></a>

**0° CCW: unverified** — `in_game_render-5fa20a2de78ef24ee969`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-44036cf5ca9c219e69b6"></a>

**90° CCW: unverified** — `in_game_render-44036cf5ca9c219e69b6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e0bbb6e7f63828f7273a"></a>

**180° CCW: unverified** — `in_game_render-e0bbb6e7f63828f7273a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-64d5cec7500a6a74eb63"></a>

**270° CCW: unverified** — `in_game_render-64d5cec7500a6a74eb63`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-5fa20a2de78ef24ee969">[ ] unverified</a> | <a href="#case-in_game_placement-44036cf5ca9c219e69b6">[ ] unverified</a> | <a href="#case-in_game_placement-e0bbb6e7f63828f7273a">[ ] unverified</a> | <a href="#case-in_game_placement-64d5cec7500a6a74eb63">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-5fa20a2de78ef24ee969"></a>

**0° CCW: unverified** — `in_game_placement-5fa20a2de78ef24ee969`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-44036cf5ca9c219e69b6"></a>

**90° CCW: unverified** — `in_game_placement-44036cf5ca9c219e69b6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e0bbb6e7f63828f7273a"></a>

**180° CCW: unverified** — `in_game_placement-e0bbb6e7f63828f7273a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-64d5cec7500a6a74eb63"></a>

**270° CCW: unverified** — `in_game_placement-64d5cec7500a6a74eb63`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-5fa20a2de78ef24ee969">[ ] unverified</a> | <a href="#case-in_game_demolition-44036cf5ca9c219e69b6">[ ] unverified</a> | <a href="#case-in_game_demolition-e0bbb6e7f63828f7273a">[ ] unverified</a> | <a href="#case-in_game_demolition-64d5cec7500a6a74eb63">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-5fa20a2de78ef24ee969"></a>

**0° CCW: unverified** — `in_game_demolition-5fa20a2de78ef24ee969`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-44036cf5ca9c219e69b6"></a>

**90° CCW: unverified** — `in_game_demolition-44036cf5ca9c219e69b6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e0bbb6e7f63828f7273a"></a>

**180° CCW: unverified** — `in_game_demolition-e0bbb6e7f63828f7273a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-64d5cec7500a6a74eb63"></a>

**270° CCW: unverified** — `in_game_demolition-64d5cec7500a6a74eb63`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-5fa20a2de78ef24ee969">[ ] unverified</a> | <a href="#case-in_game_save_reload-44036cf5ca9c219e69b6">[ ] unverified</a> | <a href="#case-in_game_save_reload-e0bbb6e7f63828f7273a">[ ] unverified</a> | <a href="#case-in_game_save_reload-64d5cec7500a6a74eb63">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-5fa20a2de78ef24ee969"></a>

**0° CCW: unverified** — `in_game_save_reload-5fa20a2de78ef24ee969`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-44036cf5ca9c219e69b6"></a>

**90° CCW: unverified** — `in_game_save_reload-44036cf5ca9c219e69b6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e0bbb6e7f63828f7273a"></a>

**180° CCW: unverified** — `in_game_save_reload-e0bbb6e7f63828f7273a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-64d5cec7500a6a74eb63"></a>

**270° CCW: unverified** — `in_game_save_reload-64d5cec7500a6a74eb63`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_route_query-893c5139b52951b645b6">[ ] unverified</a> | <a href="#case-in_game_route_query-12f69b3b913acae8201d">[ ] unverified</a> | <a href="#case-in_game_route_query-f3b3573e8f7ace23cff4">[ ] unverified</a> | <a href="#case-in_game_route_query-f8e53ac8ceee4f799d4b">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_route_query-4f0cf575be97d46acd86">[ ] unverified</a> | <a href="#case-in_game_route_query-19c54ca56f8042daf844">[ ] unverified</a> | <a href="#case-in_game_route_query-7d3a33b068031438fb81">[ ] unverified</a> | <a href="#case-in_game_route_query-bc99ac36a202cb86cb74">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_route_query-60ecb293929e38cf3d1f">[ ] unverified</a> | <a href="#case-in_game_route_query-6cc0dfabda71d80528f1">[ ] unverified</a> | <a href="#case-in_game_route_query-603647f229b7499b2763">[ ] unverified</a> | <a href="#case-in_game_route_query-5edf5624208c8e5ae91e">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_route_query-207ef3949b9f1fa27c42">[ ] unverified</a> | <a href="#case-in_game_route_query-0b0d18e5a4ca71cf43fe">[ ] unverified</a> | <a href="#case-in_game_route_query-3ef4c192a77b513915a5">[ ] unverified</a> | <a href="#case-in_game_route_query-1925b8fbd5168e2e637d">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_route_query-893c5139b52951b645b6"></a>

**0° CCW: unverified** — `in_game_route_query-893c5139b52951b645b6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-12f69b3b913acae8201d"></a>

**90° CCW: unverified** — `in_game_route_query-12f69b3b913acae8201d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-f3b3573e8f7ace23cff4"></a>

**180° CCW: unverified** — `in_game_route_query-f3b3573e8f7ace23cff4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-f8e53ac8ceee4f799d4b"></a>

**270° CCW: unverified** — `in_game_route_query-f8e53ac8ceee4f799d4b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_route_query-4f0cf575be97d46acd86"></a>

**0° CCW: unverified** — `in_game_route_query-4f0cf575be97d46acd86`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-19c54ca56f8042daf844"></a>

**90° CCW: unverified** — `in_game_route_query-19c54ca56f8042daf844`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-7d3a33b068031438fb81"></a>

**180° CCW: unverified** — `in_game_route_query-7d3a33b068031438fb81`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-bc99ac36a202cb86cb74"></a>

**270° CCW: unverified** — `in_game_route_query-bc99ac36a202cb86cb74`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_route_query-60ecb293929e38cf3d1f"></a>

**0° CCW: unverified** — `in_game_route_query-60ecb293929e38cf3d1f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-6cc0dfabda71d80528f1"></a>

**90° CCW: unverified** — `in_game_route_query-6cc0dfabda71d80528f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-603647f229b7499b2763"></a>

**180° CCW: unverified** — `in_game_route_query-603647f229b7499b2763`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-5edf5624208c8e5ae91e"></a>

**270° CCW: unverified** — `in_game_route_query-5edf5624208c8e5ae91e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_route_query-207ef3949b9f1fa27c42"></a>

**0° CCW: unverified** — `in_game_route_query-207ef3949b9f1fa27c42`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-0b0d18e5a4ca71cf43fe"></a>

**90° CCW: unverified** — `in_game_route_query-0b0d18e5a4ca71cf43fe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-3ef4c192a77b513915a5"></a>

**180° CCW: unverified** — `in_game_route_query-3ef4c192a77b513915a5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_route_query-1925b8fbd5168e2e637d"></a>

**270° CCW: unverified** — `in_game_route_query-1925b8fbd5168e2e637d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_visible_travel-893c5139b52951b645b6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-12f69b3b913acae8201d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f3b3573e8f7ace23cff4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f8e53ac8ceee4f799d4b">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_visible_travel-4f0cf575be97d46acd86">[ ] unverified</a> | <a href="#case-in_game_visible_travel-19c54ca56f8042daf844">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7d3a33b068031438fb81">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bc99ac36a202cb86cb74">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout | — | <a href="#case-in_game_visible_travel-60ecb293929e38cf3d1f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6cc0dfabda71d80528f1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-603647f229b7499b2763">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5edf5624208c8e5ae91e">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_visible_travel-207ef3949b9f1fa27c42">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0b0d18e5a4ca71cf43fe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3ef4c192a77b513915a5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1925b8fbd5168e2e637d">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_visible_travel-893c5139b52951b645b6"></a>

**0° CCW: unverified** — `in_game_visible_travel-893c5139b52951b645b6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-12f69b3b913acae8201d"></a>

**90° CCW: unverified** — `in_game_visible_travel-12f69b3b913acae8201d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-f3b3573e8f7ace23cff4"></a>

**180° CCW: unverified** — `in_game_visible_travel-f3b3573e8f7ace23cff4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-f8e53ac8ceee4f799d4b"></a>

**270° CCW: unverified** — `in_game_visible_travel-f8e53ac8ceee4f799d4b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_visible_travel-4f0cf575be97d46acd86"></a>

**0° CCW: unverified** — `in_game_visible_travel-4f0cf575be97d46acd86`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-19c54ca56f8042daf844"></a>

**90° CCW: unverified** — `in_game_visible_travel-19c54ca56f8042daf844`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-7d3a33b068031438fb81"></a>

**180° CCW: unverified** — `in_game_visible_travel-7d3a33b068031438fb81`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-bc99ac36a202cb86cb74"></a>

**270° CCW: unverified** — `in_game_visible_travel-bc99ac36a202cb86cb74`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout</summary>

<a id="case-in_game_visible_travel-60ecb293929e38cf3d1f"></a>

**0° CCW: unverified** — `in_game_visible_travel-60ecb293929e38cf3d1f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-6cc0dfabda71d80528f1"></a>

**90° CCW: unverified** — `in_game_visible_travel-6cc0dfabda71d80528f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-603647f229b7499b2763"></a>

**180° CCW: unverified** — `in_game_visible_travel-603647f229b7499b2763`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-5edf5624208c8e5ae91e"></a>

**270° CCW: unverified** — `in_game_visible_travel-5edf5624208c8e5ae91e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Nin>Wout; entry: Nin; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_visible_travel-207ef3949b9f1fa27c42"></a>

**0° CCW: unverified** — `in_game_visible_travel-207ef3949b9f1fa27c42`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-0b0d18e5a4ca71cf43fe"></a>

**90° CCW: unverified** — `in_game_visible_travel-0b0d18e5a4ca71cf43fe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-3ef4c192a77b513915a5"></a>

**180° CCW: unverified** — `in_game_visible_travel-3ef4c192a77b513915a5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_visible_travel-1925b8fbd5168e2e637d"></a>

**270° CCW: unverified** — `in_game_visible_travel-1925b8fbd5168e2e637d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-207270803a527230f629">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1fed664bf7e79661bb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4901a3adbd023156c295">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bd4ea3cffdeb32f0a21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7dd99ef9226dd9ae5cc2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ace301d7d331012dfac3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6da1e63af5bcd9339cee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56a3d4e78c3526c29ef4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a430fa085cdc293296ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-598f3f16a8f1a7e76b1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-217ae4d152ecfd03acbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a96f320a3615ec1876f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c49c60a8ee59fd1e7fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5d8a576cb782858ec32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d91ca221aae8c94f0245">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6546640b65f44fc33f06">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-207270803a527230f629"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-207270803a527230f629`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1fed664bf7e79661bb7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c1fed664bf7e79661bb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4901a3adbd023156c295"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4901a3adbd023156c295`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bd4ea3cffdeb32f0a21"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0bd4ea3cffdeb32f0a21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7dd99ef9226dd9ae5cc2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7dd99ef9226dd9ae5cc2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ace301d7d331012dfac3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ace301d7d331012dfac3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6da1e63af5bcd9339cee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6da1e63af5bcd9339cee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56a3d4e78c3526c29ef4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-56a3d4e78c3526c29ef4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a430fa085cdc293296ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a430fa085cdc293296ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-598f3f16a8f1a7e76b1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-598f3f16a8f1a7e76b1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-217ae4d152ecfd03acbb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-217ae4d152ecfd03acbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a96f320a3615ec1876f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a96f320a3615ec1876f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c49c60a8ee59fd1e7fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c49c60a8ee59fd1e7fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5d8a576cb782858ec32"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5d8a576cb782858ec32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d91ca221aae8c94f0245"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d91ca221aae8c94f0245`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6546640b65f44fc33f06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6546640b65f44fc33f06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-short-opposed-merge-core:canonical-southeast | <a href="#case-preview_review-82efb43975086d8a2c0f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-short-opposed-merge-core:canonical-top | <a href="#case-preview_review-7b1a76173037cf9da141">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-short-opposed-merge-core:connection-overview | <a href="#case-preview_review-348a0bea35fd99141ff0">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-opposed-merge-core:canonical-southeast</summary>

<a id="case-preview_review-82efb43975086d8a2c0f"></a>

**General: unverified** — `preview_review-82efb43975086d8a2c0f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-short-opposed-merge-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-opposed-merge-core:canonical-top</summary>

<a id="case-preview_review-7b1a76173037cf9da141"></a>

**General: unverified** — `preview_review-7b1a76173037cf9da141`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-short-opposed-merge-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-short-opposed-merge-core:connection-overview</summary>

<a id="case-preview_review-348a0bea35fd99141ff0"></a>

**General: unverified** — `preview_review-348a0bea35fd99141ff0`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-l2-short-opposed-merge-core:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

### Western approach extraction

The preceding version owned five tiles and five supports. After the separately approved northern branch-angle redesign, its westernmost cell contained only the two ordinary mainline routes. The accepted decomposition reuses the existing paired straight for that tile and retains the remaining four cells as this core. In the trumpet, P26 owns **(X9, Y13)** at 270°, while P07's four-tile core starts at **(X10, Y13)** at 0°. The external layout, train routes, and support positions are preserved; the narrow parapet-and-upper-bed adjustment has its own bound in chapter 3.

The historical **6.437054 mm** western-tail rejection in the assembly's [original decision ledger](../../01_assemblies/straight-stem-trumpet/checks/atomization.json) measured the deleted predecessor before its northern branch was redesigned. It is not a measurement of the later straight cell. The earlier **4.018 mm** eastern-tail extraction and its separate **24.5 mm** adjoining-curve bound also retain their original scope. See the assembly's [current extraction history](../../01_assemblies/straight-stem-trumpet/TESTING.md#western-merge-approach-extraction) for the placement mapping; frozen five-tile reports and original observations are preserved rather than relabelled as new verification or game evidence.

The retained evidence describes the version and scope recorded by its original report. A documentation reorganization does not create a new test run or extend an earlier observation to different inputs.
