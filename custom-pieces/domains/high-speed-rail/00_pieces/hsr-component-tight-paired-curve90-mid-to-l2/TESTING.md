---
title: "HSR Tight Two-Track Corner 23 to 15.5 Metres: testing"
summary: "Define this reusable piece’s test scope, setup, software checks, game checks, results, known issues, and design history."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR Tight Two-Track Corner 23 to 15.5 Metres: testing

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

The [piece overview](README.md) contains the pictures, placement instructions, and intrinsic movement matrix. This document contains the corresponding procedures, exact cases, observations, limitations, and historical evidence.

## 1. Test scope

Use the [connection matrix](README.md#3-connection-matrix) to select a directed journey, then open its exact result link here. The measured connections below describe this reusable piece; they do not certify an arbitrary neighbouring piece.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | hsr / 7 / primary | out | [-2.0, -56.0, 23.0]; [0.0, -1.0]; 0.0 | `path-interface-f17a87c40e2280c52126` |
| `Sin` | hsr / 7 / primary | in | [2.0, -56.0, 23.0]; [0.0, 1.0]; 0.0 | `path-interface-c22acb858d4777168a58` |
| `Eout` | hsr / 7 / primary | out | [56.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Ein` | hsr / 7 / primary | in | [56.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Eout` | primary |
| hsr | `Ein` → `Sout` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Read [Piece and placement](README.md#2-piece-and-placement) for the required construction rectangle, complete joining boundaries, approach types, and supported rotations.
2. Follow the [separate build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md) to prepare the matching candidate and its dependencies before a game trial. Use a disposable flat test city, and keep the documented footprint clear.
3. Record the candidate’s actual file hashes, platform, game version, NAM profile, test-city conditions, and chosen rotation. Preserve those details with each observation through the [shared testing procedure](../../../../docs/TESTING.md).

Setup instructions describe a repeatable future test; they do not record a completed installation or successful game run.

## 3. Software checks

This tight paired graded corner owns ten cells, including three structural cells, and has six literal support centres. Its cardinal displacement is 56 m, its deck width is 15 m, its track offsets are ±2 m, and its flat collars are 8 m.

The tight-corner polynomial applies only to these two tight graded recipes. Their independent minimum-radius limit is 24 m; their approximately 0.1238 maximum grade remains inside the unchanged 0.156251 limit. Curvature, grade change, and the 5 × 5 m train corridor remain independently checked. These are software geometry criteria, rather than measured game limits.

The [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and [piece definition](piece.json) supply the exact expectations. Each of the two physical channels retains its identity through the curve; its member names differ at the two ends because those names identify local crossings, rather than new tracks.

The [documentation-refresh audit](evidence/documentation-refresh.json) records the exact unchanged saved files, actual-resource connector checks, image identities, and preserved observations.

The [measured saved-route record](connections.json), [authored connector declaration](connector-groups.jsonc), [resolved connector export](connector-data.json), and [connection-overview evidence](evidence/connection-overview.json) identify the current software scope. A PATH resource contains travel routes; an S3D resource contains visible triangles. Neither a correct route nor a rendered model establishes traffic operation in the game.

Shared network measurements remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). Building, installing, and observing are separate steps. To reproduce the pictures and connector cards, follow [documentation generation](../../../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md), select this exact piece ID, and use a verified build containing this same saved model and PATH set.

## 4. Game checks

Use the [exact test checklist](#test-checklist) for each required orientation and direction. Record Route Query separately from watching a train complete the same journey. Keep appearance, placement, forbidden movements, demolition, and save/reload observations in their own cases.

For a game trial, supply demand in every declared direction, inspect **Route Query**, and separately watch a train complete the journey. Repeat placement, appearance, travel, demolition, and save/reload observations in the supported orientations. Record only explicitly observed results through the [shared testing guide](../../../../docs/TESTING.md) and the exact command in the generated checklist below. Human preview approval, game appearance, traffic choice, and physical seams retain their recorded states.

## 5. Results and known issues

The generated status and checklist below retain the authoritative observations in [checks/manual-tests.json](checks/manual-tests.json), including failures, stale results, and their exact environments. Open an individual case for its evidence and recording scope.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
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

Current totals: unverified: 43, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-d0768e0a6f5aff280639">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-d0768e0a6f5aff280639"></a>

**General: passed** — `software_resources-d0768e0a6f5aff280639`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-d0768e0a6f5aff280639">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-d0768e0a6f5aff280639"></a>

**General: passed** — `software_connectivity-d0768e0a6f5aff280639`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-southeast | <a href="#case-preview_review-c8ceea09195bd3748b8c">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-top | <a href="#case-preview_review-ebc81b8fb304fec8c4a6">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-tight-paired-curve90-mid-to-l2:connection-overview | <a href="#case-preview_review-6e3fcc4aa3babfba5fd7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-southeast</summary>

<a id="case-preview_review-c8ceea09195bd3748b8c"></a>

**General: unverified** — `preview_review-c8ceea09195bd3748b8c`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-top</summary>

<a id="case-preview_review-ebc81b8fb304fec8c4a6"></a>

**General: unverified** — `preview_review-ebc81b8fb304fec8c4a6`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-tight-paired-curve90-mid-to-l2:connection-overview</summary>

<a id="case-preview_review-6e3fcc4aa3babfba5fd7"></a>

**General: unverified** — `preview_review-6e3fcc4aa3babfba5fd7`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-tight-paired-curve90-mid-to-l2:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-f627ea62430d13e37df7">[ ] unverified</a> | <a href="#case-in_game_render-a00c4dcf9b2d966b03e6">[ ] unverified</a> | <a href="#case-in_game_render-a2289220f8f390575e32">[ ] unverified</a> | <a href="#case-in_game_render-ee02fb8e6143d848f5ee">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-f627ea62430d13e37df7"></a>

**0° CCW: unverified** — `in_game_render-f627ea62430d13e37df7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a00c4dcf9b2d966b03e6"></a>

**90° CCW: unverified** — `in_game_render-a00c4dcf9b2d966b03e6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a2289220f8f390575e32"></a>

**180° CCW: unverified** — `in_game_render-a2289220f8f390575e32`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ee02fb8e6143d848f5ee"></a>

**270° CCW: unverified** — `in_game_render-ee02fb8e6143d848f5ee`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-f627ea62430d13e37df7">[ ] unverified</a> | <a href="#case-in_game_placement-a00c4dcf9b2d966b03e6">[ ] unverified</a> | <a href="#case-in_game_placement-a2289220f8f390575e32">[ ] unverified</a> | <a href="#case-in_game_placement-ee02fb8e6143d848f5ee">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-f627ea62430d13e37df7"></a>

**0° CCW: unverified** — `in_game_placement-f627ea62430d13e37df7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a00c4dcf9b2d966b03e6"></a>

**90° CCW: unverified** — `in_game_placement-a00c4dcf9b2d966b03e6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a2289220f8f390575e32"></a>

**180° CCW: unverified** — `in_game_placement-a2289220f8f390575e32`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ee02fb8e6143d848f5ee"></a>

**270° CCW: unverified** — `in_game_placement-ee02fb8e6143d848f5ee`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-f627ea62430d13e37df7">[ ] unverified</a> | <a href="#case-in_game_demolition-a00c4dcf9b2d966b03e6">[ ] unverified</a> | <a href="#case-in_game_demolition-a2289220f8f390575e32">[ ] unverified</a> | <a href="#case-in_game_demolition-ee02fb8e6143d848f5ee">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-f627ea62430d13e37df7"></a>

**0° CCW: unverified** — `in_game_demolition-f627ea62430d13e37df7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a00c4dcf9b2d966b03e6"></a>

**90° CCW: unverified** — `in_game_demolition-a00c4dcf9b2d966b03e6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a2289220f8f390575e32"></a>

**180° CCW: unverified** — `in_game_demolition-a2289220f8f390575e32`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ee02fb8e6143d848f5ee"></a>

**270° CCW: unverified** — `in_game_demolition-ee02fb8e6143d848f5ee`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-f627ea62430d13e37df7">[ ] unverified</a> | <a href="#case-in_game_save_reload-a00c4dcf9b2d966b03e6">[ ] unverified</a> | <a href="#case-in_game_save_reload-a2289220f8f390575e32">[ ] unverified</a> | <a href="#case-in_game_save_reload-ee02fb8e6143d848f5ee">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-f627ea62430d13e37df7"></a>

**0° CCW: unverified** — `in_game_save_reload-f627ea62430d13e37df7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a00c4dcf9b2d966b03e6"></a>

**90° CCW: unverified** — `in_game_save_reload-a00c4dcf9b2d966b03e6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a2289220f8f390575e32"></a>

**180° CCW: unverified** — `in_game_save_reload-a2289220f8f390575e32`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ee02fb8e6143d848f5ee"></a>

**270° CCW: unverified** — `in_game_save_reload-ee02fb8e6143d848f5ee`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_route_query-c609522f866468deda1c">[ ] unverified</a> | <a href="#case-in_game_route_query-caca662303c92a69755d">[ ] unverified</a> | <a href="#case-in_game_route_query-4224d99b63e3c6dfe042">[ ] unverified</a> | <a href="#case-in_game_route_query-fce87cacab3cca4e9739">[ ] unverified</a> |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout | — | <a href="#case-in_game_route_query-c0ea1a301c247af4a030">[ ] unverified</a> | <a href="#case-in_game_route_query-0192539723def2c635c0">[ ] unverified</a> | <a href="#case-in_game_route_query-debcb4d50826bf0dfe2b">[ ] unverified</a> | <a href="#case-in_game_route_query-8f17b5e62232dd993a0f">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_route_query-c609522f866468deda1c"></a>

**0° CCW: unverified** — `in_game_route_query-c609522f866468deda1c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-caca662303c92a69755d"></a>

**90° CCW: unverified** — `in_game_route_query-caca662303c92a69755d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-4224d99b63e3c6dfe042"></a>

**180° CCW: unverified** — `in_game_route_query-4224d99b63e3c6dfe042`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_route_query-fce87cacab3cca4e9739"></a>

**270° CCW: unverified** — `in_game_route_query-fce87cacab3cca4e9739`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout</summary>

<a id="case-in_game_route_query-c0ea1a301c247af4a030"></a>

**0° CCW: unverified** — `in_game_route_query-c0ea1a301c247af4a030`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-0192539723def2c635c0"></a>

**90° CCW: unverified** — `in_game_route_query-0192539723def2c635c0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-debcb4d50826bf0dfe2b"></a>

**180° CCW: unverified** — `in_game_route_query-debcb4d50826bf0dfe2b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-8f17b5e62232dd993a0f"></a>

**270° CCW: unverified** — `in_game_route_query-8f17b5e62232dd993a0f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_visible_travel-c609522f866468deda1c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-caca662303c92a69755d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4224d99b63e3c6dfe042">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fce87cacab3cca4e9739">[ ] unverified</a> |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout | — | <a href="#case-in_game_visible_travel-c0ea1a301c247af4a030">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0192539723def2c635c0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-debcb4d50826bf0dfe2b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8f17b5e62232dd993a0f">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_visible_travel-c609522f866468deda1c"></a>

**0° CCW: unverified** — `in_game_visible_travel-c609522f866468deda1c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-caca662303c92a69755d"></a>

**90° CCW: unverified** — `in_game_visible_travel-caca662303c92a69755d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-4224d99b63e3c6dfe042"></a>

**180° CCW: unverified** — `in_game_visible_travel-4224d99b63e3c6dfe042`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_visible_travel-fce87cacab3cca4e9739"></a>

**270° CCW: unverified** — `in_game_visible_travel-fce87cacab3cca4e9739`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout</summary>

<a id="case-in_game_visible_travel-c0ea1a301c247af4a030"></a>

**0° CCW: unverified** — `in_game_visible_travel-c0ea1a301c247af4a030`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-0192539723def2c635c0"></a>

**90° CCW: unverified** — `in_game_visible_travel-0192539723def2c635c0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-debcb4d50826bf0dfe2b"></a>

**180° CCW: unverified** — `in_game_visible_travel-debcb4d50826bf0dfe2b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-8f17b5e62232dd993a0f"></a>

**270° CCW: unverified** — `in_game_visible_travel-8f17b5e62232dd993a0f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a5af8eb524560251ee3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94cbded6f06f1c832e30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85bc638ea2f5e4612f2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c573921b8296828f57b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-961647d99405973fe109">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33a6d57149399f3814e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63c9ca69b01c537b0bc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4c619a8b7fd2a283b8b">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a5af8eb524560251ee3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a5af8eb524560251ee3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94cbded6f06f1c832e30"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94cbded6f06f1c832e30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85bc638ea2f5e4612f2e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85bc638ea2f5e4612f2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c573921b8296828f57b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c573921b8296828f57b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-961647d99405973fe109"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-961647d99405973fe109`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33a6d57149399f3814e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-33a6d57149399f3814e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63c9ca69b01c537b0bc0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63c9ca69b01c537b0bc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4c619a8b7fd2a283b8b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4c619a8b7fd2a283b8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The retained evidence describes the version and scope recorded by its original report. A documentation reorganization does not create a new test run or extend an earlier observation to different inputs.
