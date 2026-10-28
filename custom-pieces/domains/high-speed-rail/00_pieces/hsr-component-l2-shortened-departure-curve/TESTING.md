---
title: "HSR L2 Shortened One-Way Departure Curve: testing"
summary: "Define this reusable piece’s test scope, setup, software checks, game checks, results, known issues, and design history."
audience: "Testers, piece authors, and maintainers"
document_type: "reference"
---

# HSR L2 Shortened One-Way Departure Curve: testing

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
| `Win` | hsr / 7 / primary | in | [22.398519, 8.0, 15.5]; [0.9272548089646255, -0.3744309272108488]; 0.0 | `path-interface-d819a6d05c5e43d11db7` |
| `Sout` | hsr / 7 / primary | out | [64.0, -88.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-365752af76285c80cd0b` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Win` → `Sout` | primary |

#### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

1. Read [Piece and placement](README.md#2-piece-and-placement) for the required construction rectangle, complete joining boundaries, approach types, and supported rotations.
2. Follow the [separate build and installation procedure](../../../../docs/BUILD_AND_INSTALL.md) to prepare the matching candidate and its dependencies before a game trial. Use a disposable flat test city, and keep the documented footprint clear.
3. Record the candidate’s actual file hashes, platform, game version, NAM profile, test-city conditions, and chosen rotation. Preserve those details with each observation through the [shared testing procedure](../../../../docs/TESTING.md).

Setup instructions describe a repeatable future test; they do not record a completed installation or successful game run.

## 3. Software checks

The saved route and model checks are separate from a game observation. The generated intrinsic matrix covers this piece’s single directed journey. The authored physical channel keeps the same channel ID at both exposed ends, while each local directed member and boundary cut has its own ID.

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
- [ ] Route Query: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/4 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 27, passed: 2, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-shortened-departure-curve/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-shortened-departure-curve/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-83b743c98f8f90875b39">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-83b743c98f8f90875b39"></a>

**General: passed** — `software_resources-83b743c98f8f90875b39`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:35.055343+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-83b743c98f8f90875b39">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-83b743c98f8f90875b39"></a>

**General: passed** — `software_connectivity-83b743c98f8f90875b39`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus independent staged build resource checks; confirmed at: 2026-10-20T10:42:35.062051+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: {}
- result: passed; authority: software; reviewer: Actual final normal 13-piece saved-build verification; registered independent PATH, model, construction, menu, and shadow checks; confirmed at: 2026-10-27T21:57:25.376326+00:00; evidence: [evidence/saved-resource-checks.json]; environment: {}

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-shortened-departure-curve:canonical-southeast | <a href="#case-preview_review-61ced121192cf435cfcc">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-shortened-departure-curve:canonical-top | <a href="#case-preview_review-2a07200751b816a8ffdd">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-shortened-departure-curve:connection-overview | <a href="#case-preview_review-becf79702eb5e0f77906">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-shortened-departure-curve:canonical-southeast</summary>

<a id="case-preview_review-61ced121192cf435cfcc"></a>

**General: unverified** — `preview_review-61ced121192cf435cfcc`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-shortened-departure-curve:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-shortened-departure-curve:canonical-top</summary>

<a id="case-preview_review-2a07200751b816a8ffdd"></a>

**General: unverified** — `preview_review-2a07200751b816a8ffdd`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-shortened-departure-curve:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-shortened-departure-curve:connection-overview</summary>

<a id="case-preview_review-becf79702eb5e0f77906"></a>

**General: unverified** — `preview_review-becf79702eb5e0f77906`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:hsr-component-l2-shortened-departure-curve:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-74825559fda8bcf5d368">[ ] unverified</a> | <a href="#case-in_game_render-a075e907aed6ea794372">[ ] unverified</a> | <a href="#case-in_game_render-178d9502e2f60a643f59">[ ] unverified</a> | <a href="#case-in_game_render-4514d331142197f0d85d">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-74825559fda8bcf5d368"></a>

**0° CCW: unverified** — `in_game_render-74825559fda8bcf5d368`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a075e907aed6ea794372"></a>

**90° CCW: unverified** — `in_game_render-a075e907aed6ea794372`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-178d9502e2f60a643f59"></a>

**180° CCW: unverified** — `in_game_render-178d9502e2f60a643f59`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-4514d331142197f0d85d"></a>

**270° CCW: unverified** — `in_game_render-4514d331142197f0d85d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-74825559fda8bcf5d368">[ ] unverified</a> | <a href="#case-in_game_placement-a075e907aed6ea794372">[ ] unverified</a> | <a href="#case-in_game_placement-178d9502e2f60a643f59">[ ] unverified</a> | <a href="#case-in_game_placement-4514d331142197f0d85d">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-74825559fda8bcf5d368"></a>

**0° CCW: unverified** — `in_game_placement-74825559fda8bcf5d368`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a075e907aed6ea794372"></a>

**90° CCW: unverified** — `in_game_placement-a075e907aed6ea794372`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-178d9502e2f60a643f59"></a>

**180° CCW: unverified** — `in_game_placement-178d9502e2f60a643f59`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-4514d331142197f0d85d"></a>

**270° CCW: unverified** — `in_game_placement-4514d331142197f0d85d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-74825559fda8bcf5d368">[ ] unverified</a> | <a href="#case-in_game_demolition-a075e907aed6ea794372">[ ] unverified</a> | <a href="#case-in_game_demolition-178d9502e2f60a643f59">[ ] unverified</a> | <a href="#case-in_game_demolition-4514d331142197f0d85d">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-74825559fda8bcf5d368"></a>

**0° CCW: unverified** — `in_game_demolition-74825559fda8bcf5d368`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a075e907aed6ea794372"></a>

**90° CCW: unverified** — `in_game_demolition-a075e907aed6ea794372`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-178d9502e2f60a643f59"></a>

**180° CCW: unverified** — `in_game_demolition-178d9502e2f60a643f59`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-4514d331142197f0d85d"></a>

**270° CCW: unverified** — `in_game_demolition-4514d331142197f0d85d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-74825559fda8bcf5d368">[ ] unverified</a> | <a href="#case-in_game_save_reload-a075e907aed6ea794372">[ ] unverified</a> | <a href="#case-in_game_save_reload-178d9502e2f60a643f59">[ ] unverified</a> | <a href="#case-in_game_save_reload-4514d331142197f0d85d">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-74825559fda8bcf5d368"></a>

**0° CCW: unverified** — `in_game_save_reload-74825559fda8bcf5d368`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a075e907aed6ea794372"></a>

**90° CCW: unverified** — `in_game_save_reload-a075e907aed6ea794372`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-178d9502e2f60a643f59"></a>

**180° CCW: unverified** — `in_game_save_reload-178d9502e2f60a643f59`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-4514d331142197f0d85d"></a>

**270° CCW: unverified** — `in_game_save_reload-4514d331142197f0d85d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — hsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout | — | <a href="#case-in_game_route_query-bced605ea8a78ee7dcad">[ ] unverified</a> | <a href="#case-in_game_route_query-3e23849a17fb444dd57c">[ ] unverified</a> | <a href="#case-in_game_route_query-5db4891a5c3875cce170">[ ] unverified</a> | <a href="#case-in_game_route_query-bb8634179e4f87fed5fa">[ ] unverified</a> |


<details>
<summary>Route Query — Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout</summary>

<a id="case-in_game_route_query-bced605ea8a78ee7dcad"></a>

**0° CCW: unverified** — `in_game_route_query-bced605ea8a78ee7dcad`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-3e23849a17fb444dd57c"></a>

**90° CCW: unverified** — `in_game_route_query-3e23849a17fb444dd57c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-5db4891a5c3875cce170"></a>

**180° CCW: unverified** — `in_game_route_query-5db4891a5c3875cce170`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_route_query-bb8634179e4f87fed5fa"></a>

**270° CCW: unverified** — `in_game_route_query-bb8634179e4f87fed5fa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — hsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout | — | <a href="#case-in_game_visible_travel-bced605ea8a78ee7dcad">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3e23849a17fb444dd57c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5db4891a5c3875cce170">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bb8634179e4f87fed5fa">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout</summary>

<a id="case-in_game_visible_travel-bced605ea8a78ee7dcad"></a>

**0° CCW: unverified** — `in_game_visible_travel-bced605ea8a78ee7dcad`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-3e23849a17fb444dd57c"></a>

**90° CCW: unverified** — `in_game_visible_travel-3e23849a17fb444dd57c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-5db4891a5c3875cce170"></a>

**180° CCW: unverified** — `in_game_visible_travel-5db4891a5c3875cce170`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

<a id="case-in_game_visible_travel-bb8634179e4f87fed5fa"></a>

**270° CCW: unverified** — `in_game_visible_travel-bb8634179e4f87fed5fa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: hsr; role: primary; journey: 7:Win>Sout; entry: Win; exit: Sout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The retained evidence describes the version and scope recorded by its original report. A documentation reorganization does not create a new test run or extend an earlier observation to different inputs.

The [independent geometry source](geometry.json) preserves the retained core and its interfaces. The extracted ordinary tail had a 2.058 mm maximum deviation; the adjoining smooth join has a separate 8.2 mm correction bound. These historical extraction allowances do not authorize moving this current piece. The assembly’s [decision ledger](../../01_assemblies/straight-stem-trumpet/checks/atomization.json) and [resource contract](../../01_assemblies/straight-stem-trumpet/checks/resources.json) retain their exact scope.
