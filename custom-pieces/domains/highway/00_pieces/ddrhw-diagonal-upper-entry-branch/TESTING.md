---
title: "Testing: DD RHW-4 \u2014 Upper Diagonal Entry Branch"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Upper Diagonal Entry Branch

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Merges the on-ramp from the southeast avenue access into an outer upper-deck lane. Its final section stays level above the lower deck. The opposite upper-deck edge remains closed, and the branch owns the outer native cell crossed by its ramp faces. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

This branch uses a real flat auxiliary lane in the former highway shoulder, with a 16 m taper and a 8 m parallel section. Its saved driving path changes between the native outer through lane and that auxiliary lane. Native-material dashed separators and a painted split area identify the join; both highway through lanes remain available.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -35.2, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-2` | road / 1 / primary | in | [-8.0, -35.2, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-3` | road / 1 / primary | out | [-8.0, -28.8, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-4` | road / 1 / primary | in | [-8.0, -28.8, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-N-in-5` | road / 1 / primary | in | [-3.2, -24.0, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-6` | road / 1 / primary | out | [-3.2, -24.0, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-7` | road / 1 / primary | in | [3.2, -24.0, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-8` | road / 1 / primary | out | [3.2, -24.0, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-W-out-9` | road / 1 / primary | out | [8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-10` | road / 1 / primary | in | [8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-11` | road / 1 / primary | out | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-12` | road / 1 / primary | in | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-S-in-13` | road / 1 / primary | in | [8.142765, -40.0, 12.25824]; [0.3742725382330187, 0.9273187516299957]; 0.296094955 | `path-interface-fdc40a0b543fd33d9da0` |
| `1-N-in-14` | road / 1 / primary | in | [28.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-15` | road / 1 / primary | out | [28.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-16` | road / 1 / primary | in | [35.2, 8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-17` | road / 1 / primary | out | [35.2, 8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-2` → `1-N-out-8` | primary |
| road | `1-W-in-4` → `1-N-out-6` | primary |
| road | `1-N-in-5` → `1-W-out-3` | primary |
| road | `1-N-in-7` → `1-W-out-1` | primary |
| road | `1-W-in-10` → `1-N-out-17` | primary |
| road | `1-W-in-12` → `1-N-out-15` | primary |
| road | `1-S-in-13` → `1-N-out-17` | primary |
| road | `1-N-in-14` → `1-W-out-11` | primary |
| road | `1-N-in-16` → `1-W-out-9` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-2` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-upper-entry-branch --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/36 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/36 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 345, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-upper-entry-branch/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-upper-entry-branch/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-c63fa7fd479936a01204">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-c63fa7fd479936a01204"></a>

**General: unverified** — `software_resources-c63fa7fd479936a01204`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-c63fa7fd479936a01204">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-c63fa7fd479936a01204"></a>

**General: unverified** — `software_connectivity-c63fa7fd479936a01204`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-e3e03a745a6696759c92">[ ] unverified</a> | <a href="#case-in_game_render-c15ccd5da79c92f5007c">[ ] unverified</a> | <a href="#case-in_game_render-b10b2044f2dfd8a45229">[ ] unverified</a> | <a href="#case-in_game_render-20a8d46a3f8042b58394">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-e3e03a745a6696759c92"></a>

**0° CCW: unverified** — `in_game_render-e3e03a745a6696759c92`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c15ccd5da79c92f5007c"></a>

**90° CCW: unverified** — `in_game_render-c15ccd5da79c92f5007c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-b10b2044f2dfd8a45229"></a>

**180° CCW: unverified** — `in_game_render-b10b2044f2dfd8a45229`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-20a8d46a3f8042b58394"></a>

**270° CCW: unverified** — `in_game_render-20a8d46a3f8042b58394`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-e3e03a745a6696759c92">[ ] unverified</a> | <a href="#case-in_game_placement-c15ccd5da79c92f5007c">[ ] unverified</a> | <a href="#case-in_game_placement-b10b2044f2dfd8a45229">[ ] unverified</a> | <a href="#case-in_game_placement-20a8d46a3f8042b58394">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-e3e03a745a6696759c92"></a>

**0° CCW: unverified** — `in_game_placement-e3e03a745a6696759c92`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c15ccd5da79c92f5007c"></a>

**90° CCW: unverified** — `in_game_placement-c15ccd5da79c92f5007c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-b10b2044f2dfd8a45229"></a>

**180° CCW: unverified** — `in_game_placement-b10b2044f2dfd8a45229`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-20a8d46a3f8042b58394"></a>

**270° CCW: unverified** — `in_game_placement-20a8d46a3f8042b58394`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-e3e03a745a6696759c92">[ ] unverified</a> | <a href="#case-in_game_demolition-c15ccd5da79c92f5007c">[ ] unverified</a> | <a href="#case-in_game_demolition-b10b2044f2dfd8a45229">[ ] unverified</a> | <a href="#case-in_game_demolition-20a8d46a3f8042b58394">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-e3e03a745a6696759c92"></a>

**0° CCW: unverified** — `in_game_demolition-e3e03a745a6696759c92`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c15ccd5da79c92f5007c"></a>

**90° CCW: unverified** — `in_game_demolition-c15ccd5da79c92f5007c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-b10b2044f2dfd8a45229"></a>

**180° CCW: unverified** — `in_game_demolition-b10b2044f2dfd8a45229`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-20a8d46a3f8042b58394"></a>

**270° CCW: unverified** — `in_game_demolition-20a8d46a3f8042b58394`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-e3e03a745a6696759c92">[ ] unverified</a> | <a href="#case-in_game_save_reload-c15ccd5da79c92f5007c">[ ] unverified</a> | <a href="#case-in_game_save_reload-b10b2044f2dfd8a45229">[ ] unverified</a> | <a href="#case-in_game_save_reload-20a8d46a3f8042b58394">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-e3e03a745a6696759c92"></a>

**0° CCW: unverified** — `in_game_save_reload-e3e03a745a6696759c92`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c15ccd5da79c92f5007c"></a>

**90° CCW: unverified** — `in_game_save_reload-c15ccd5da79c92f5007c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-b10b2044f2dfd8a45229"></a>

**180° CCW: unverified** — `in_game_save_reload-b10b2044f2dfd8a45229`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-20a8d46a3f8042b58394"></a>

**270° CCW: unverified** — `in_game_save_reload-20a8d46a3f8042b58394`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8 | — | <a href="#case-in_game_route_query-312697fbd48dee48f659">[ ] unverified</a> | <a href="#case-in_game_route_query-be0451e740e4dea8e9c8">[ ] unverified</a> | <a href="#case-in_game_route_query-eb5e5aeef3afb9fcf707">[ ] unverified</a> | <a href="#case-in_game_route_query-44cd8ed07c49459e34d5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6 | — | <a href="#case-in_game_route_query-07b604fd15d6ff2af07a">[ ] unverified</a> | <a href="#case-in_game_route_query-561bd86a0a8b57e94af5">[ ] unverified</a> | <a href="#case-in_game_route_query-513f4ed0f136b8d22b7e">[ ] unverified</a> | <a href="#case-in_game_route_query-32a2a3a989c16ae559d1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-532a7dc7b158b92dbe73">[ ] unverified</a> | <a href="#case-in_game_route_query-2491d06cc67ff0f4dd3b">[ ] unverified</a> | <a href="#case-in_game_route_query-b41b839755f9012d0dc8">[ ] unverified</a> | <a href="#case-in_game_route_query-4a16f3069df82fc9e180">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-103469cee15692a2af75">[ ] unverified</a> | <a href="#case-in_game_route_query-9adc40ded4dcf4607f38">[ ] unverified</a> | <a href="#case-in_game_route_query-78eaa064c6964ce0da79">[ ] unverified</a> | <a href="#case-in_game_route_query-6870faf47b255b7eda29">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17 | — | <a href="#case-in_game_route_query-f269e259772525b7d6e8">[ ] unverified</a> | <a href="#case-in_game_route_query-693a52cd620fcd9b4ac5">[ ] unverified</a> | <a href="#case-in_game_route_query-449a8a83e855bd3d16cc">[ ] unverified</a> | <a href="#case-in_game_route_query-7a4f90d0fb7e202e56ec">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15 | — | <a href="#case-in_game_route_query-1f8a9984715cdada118e">[ ] unverified</a> | <a href="#case-in_game_route_query-656c2323f3a7fe3d1aaf">[ ] unverified</a> | <a href="#case-in_game_route_query-944a34e0352e398a52fe">[ ] unverified</a> | <a href="#case-in_game_route_query-44a14e113fe8e6d32b4f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17 | — | <a href="#case-in_game_route_query-474719545888b39235cd">[ ] unverified</a> | <a href="#case-in_game_route_query-747532a951b8907d8354">[ ] unverified</a> | <a href="#case-in_game_route_query-7d40b614b1c816394407">[ ] unverified</a> | <a href="#case-in_game_route_query-fdc2a651d46da95e9815">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11 | — | <a href="#case-in_game_route_query-c203030e90895068848d">[ ] unverified</a> | <a href="#case-in_game_route_query-b198626cd9f13f371481">[ ] unverified</a> | <a href="#case-in_game_route_query-e891fdba0cac3e02177b">[ ] unverified</a> | <a href="#case-in_game_route_query-5f2cf0201de07499336c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9 | — | <a href="#case-in_game_route_query-f5bf402242c70d8ef08d">[ ] unverified</a> | <a href="#case-in_game_route_query-17e8958034f81b8d6faa">[ ] unverified</a> | <a href="#case-in_game_route_query-93b61a565e2908d61b36">[ ] unverified</a> | <a href="#case-in_game_route_query-269a01580873da3d9a43">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8</summary>

<a id="case-in_game_route_query-312697fbd48dee48f659"></a>

**0° CCW: unverified** — `in_game_route_query-312697fbd48dee48f659`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-be0451e740e4dea8e9c8"></a>

**90° CCW: unverified** — `in_game_route_query-be0451e740e4dea8e9c8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-eb5e5aeef3afb9fcf707"></a>

**180° CCW: unverified** — `in_game_route_query-eb5e5aeef3afb9fcf707`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-44cd8ed07c49459e34d5"></a>

**270° CCW: unverified** — `in_game_route_query-44cd8ed07c49459e34d5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6</summary>

<a id="case-in_game_route_query-07b604fd15d6ff2af07a"></a>

**0° CCW: unverified** — `in_game_route_query-07b604fd15d6ff2af07a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-561bd86a0a8b57e94af5"></a>

**90° CCW: unverified** — `in_game_route_query-561bd86a0a8b57e94af5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-513f4ed0f136b8d22b7e"></a>

**180° CCW: unverified** — `in_game_route_query-513f4ed0f136b8d22b7e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-32a2a3a989c16ae559d1"></a>

**270° CCW: unverified** — `in_game_route_query-32a2a3a989c16ae559d1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3</summary>

<a id="case-in_game_route_query-532a7dc7b158b92dbe73"></a>

**0° CCW: unverified** — `in_game_route_query-532a7dc7b158b92dbe73`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-2491d06cc67ff0f4dd3b"></a>

**90° CCW: unverified** — `in_game_route_query-2491d06cc67ff0f4dd3b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-b41b839755f9012d0dc8"></a>

**180° CCW: unverified** — `in_game_route_query-b41b839755f9012d0dc8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-4a16f3069df82fc9e180"></a>

**270° CCW: unverified** — `in_game_route_query-4a16f3069df82fc9e180`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-103469cee15692a2af75"></a>

**0° CCW: unverified** — `in_game_route_query-103469cee15692a2af75`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-9adc40ded4dcf4607f38"></a>

**90° CCW: unverified** — `in_game_route_query-9adc40ded4dcf4607f38`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-78eaa064c6964ce0da79"></a>

**180° CCW: unverified** — `in_game_route_query-78eaa064c6964ce0da79`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-6870faf47b255b7eda29"></a>

**270° CCW: unverified** — `in_game_route_query-6870faf47b255b7eda29`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17</summary>

<a id="case-in_game_route_query-f269e259772525b7d6e8"></a>

**0° CCW: unverified** — `in_game_route_query-f269e259772525b7d6e8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-693a52cd620fcd9b4ac5"></a>

**90° CCW: unverified** — `in_game_route_query-693a52cd620fcd9b4ac5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-449a8a83e855bd3d16cc"></a>

**180° CCW: unverified** — `in_game_route_query-449a8a83e855bd3d16cc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-7a4f90d0fb7e202e56ec"></a>

**270° CCW: unverified** — `in_game_route_query-7a4f90d0fb7e202e56ec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15</summary>

<a id="case-in_game_route_query-1f8a9984715cdada118e"></a>

**0° CCW: unverified** — `in_game_route_query-1f8a9984715cdada118e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_route_query-656c2323f3a7fe3d1aaf"></a>

**90° CCW: unverified** — `in_game_route_query-656c2323f3a7fe3d1aaf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_route_query-944a34e0352e398a52fe"></a>

**180° CCW: unverified** — `in_game_route_query-944a34e0352e398a52fe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_route_query-44a14e113fe8e6d32b4f"></a>

**270° CCW: unverified** — `in_game_route_query-44a14e113fe8e6d32b4f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17</summary>

<a id="case-in_game_route_query-474719545888b39235cd"></a>

**0° CCW: unverified** — `in_game_route_query-474719545888b39235cd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-747532a951b8907d8354"></a>

**90° CCW: unverified** — `in_game_route_query-747532a951b8907d8354`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-7d40b614b1c816394407"></a>

**180° CCW: unverified** — `in_game_route_query-7d40b614b1c816394407`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-fdc2a651d46da95e9815"></a>

**270° CCW: unverified** — `in_game_route_query-fdc2a651d46da95e9815`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11</summary>

<a id="case-in_game_route_query-c203030e90895068848d"></a>

**0° CCW: unverified** — `in_game_route_query-c203030e90895068848d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-b198626cd9f13f371481"></a>

**90° CCW: unverified** — `in_game_route_query-b198626cd9f13f371481`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-e891fdba0cac3e02177b"></a>

**180° CCW: unverified** — `in_game_route_query-e891fdba0cac3e02177b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-5f2cf0201de07499336c"></a>

**270° CCW: unverified** — `in_game_route_query-5f2cf0201de07499336c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9</summary>

<a id="case-in_game_route_query-f5bf402242c70d8ef08d"></a>

**0° CCW: unverified** — `in_game_route_query-f5bf402242c70d8ef08d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-17e8958034f81b8d6faa"></a>

**90° CCW: unverified** — `in_game_route_query-17e8958034f81b8d6faa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-93b61a565e2908d61b36"></a>

**180° CCW: unverified** — `in_game_route_query-93b61a565e2908d61b36`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-269a01580873da3d9a43"></a>

**270° CCW: unverified** — `in_game_route_query-269a01580873da3d9a43`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8 | — | <a href="#case-in_game_visible_travel-312697fbd48dee48f659">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be0451e740e4dea8e9c8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-eb5e5aeef3afb9fcf707">[ ] unverified</a> | <a href="#case-in_game_visible_travel-44cd8ed07c49459e34d5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6 | — | <a href="#case-in_game_visible_travel-07b604fd15d6ff2af07a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-561bd86a0a8b57e94af5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-513f4ed0f136b8d22b7e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-32a2a3a989c16ae559d1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-532a7dc7b158b92dbe73">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2491d06cc67ff0f4dd3b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b41b839755f9012d0dc8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4a16f3069df82fc9e180">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-103469cee15692a2af75">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9adc40ded4dcf4607f38">[ ] unverified</a> | <a href="#case-in_game_visible_travel-78eaa064c6964ce0da79">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6870faf47b255b7eda29">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17 | — | <a href="#case-in_game_visible_travel-f269e259772525b7d6e8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-693a52cd620fcd9b4ac5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-449a8a83e855bd3d16cc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7a4f90d0fb7e202e56ec">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15 | — | <a href="#case-in_game_visible_travel-1f8a9984715cdada118e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-656c2323f3a7fe3d1aaf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-944a34e0352e398a52fe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-44a14e113fe8e6d32b4f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17 | — | <a href="#case-in_game_visible_travel-474719545888b39235cd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-747532a951b8907d8354">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7d40b614b1c816394407">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fdc2a651d46da95e9815">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11 | — | <a href="#case-in_game_visible_travel-c203030e90895068848d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b198626cd9f13f371481">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e891fdba0cac3e02177b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5f2cf0201de07499336c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9 | — | <a href="#case-in_game_visible_travel-f5bf402242c70d8ef08d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-17e8958034f81b8d6faa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-93b61a565e2908d61b36">[ ] unverified</a> | <a href="#case-in_game_visible_travel-269a01580873da3d9a43">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8</summary>

<a id="case-in_game_visible_travel-312697fbd48dee48f659"></a>

**0° CCW: unverified** — `in_game_visible_travel-312697fbd48dee48f659`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-be0451e740e4dea8e9c8"></a>

**90° CCW: unverified** — `in_game_visible_travel-be0451e740e4dea8e9c8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-eb5e5aeef3afb9fcf707"></a>

**180° CCW: unverified** — `in_game_visible_travel-eb5e5aeef3afb9fcf707`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-44cd8ed07c49459e34d5"></a>

**270° CCW: unverified** — `in_game_visible_travel-44cd8ed07c49459e34d5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6</summary>

<a id="case-in_game_visible_travel-07b604fd15d6ff2af07a"></a>

**0° CCW: unverified** — `in_game_visible_travel-07b604fd15d6ff2af07a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-561bd86a0a8b57e94af5"></a>

**90° CCW: unverified** — `in_game_visible_travel-561bd86a0a8b57e94af5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-513f4ed0f136b8d22b7e"></a>

**180° CCW: unverified** — `in_game_visible_travel-513f4ed0f136b8d22b7e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-32a2a3a989c16ae559d1"></a>

**270° CCW: unverified** — `in_game_visible_travel-32a2a3a989c16ae559d1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3</summary>

<a id="case-in_game_visible_travel-532a7dc7b158b92dbe73"></a>

**0° CCW: unverified** — `in_game_visible_travel-532a7dc7b158b92dbe73`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-2491d06cc67ff0f4dd3b"></a>

**90° CCW: unverified** — `in_game_visible_travel-2491d06cc67ff0f4dd3b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-b41b839755f9012d0dc8"></a>

**180° CCW: unverified** — `in_game_visible_travel-b41b839755f9012d0dc8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-4a16f3069df82fc9e180"></a>

**270° CCW: unverified** — `in_game_visible_travel-4a16f3069df82fc9e180`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-103469cee15692a2af75"></a>

**0° CCW: unverified** — `in_game_visible_travel-103469cee15692a2af75`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-9adc40ded4dcf4607f38"></a>

**90° CCW: unverified** — `in_game_visible_travel-9adc40ded4dcf4607f38`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-78eaa064c6964ce0da79"></a>

**180° CCW: unverified** — `in_game_visible_travel-78eaa064c6964ce0da79`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-6870faf47b255b7eda29"></a>

**270° CCW: unverified** — `in_game_visible_travel-6870faf47b255b7eda29`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17</summary>

<a id="case-in_game_visible_travel-f269e259772525b7d6e8"></a>

**0° CCW: unverified** — `in_game_visible_travel-f269e259772525b7d6e8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-693a52cd620fcd9b4ac5"></a>

**90° CCW: unverified** — `in_game_visible_travel-693a52cd620fcd9b4ac5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-449a8a83e855bd3d16cc"></a>

**180° CCW: unverified** — `in_game_visible_travel-449a8a83e855bd3d16cc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-7a4f90d0fb7e202e56ec"></a>

**270° CCW: unverified** — `in_game_visible_travel-7a4f90d0fb7e202e56ec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-17; entry: 1-W-in-10; exit: 1-N-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15</summary>

<a id="case-in_game_visible_travel-1f8a9984715cdada118e"></a>

**0° CCW: unverified** — `in_game_visible_travel-1f8a9984715cdada118e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-656c2323f3a7fe3d1aaf"></a>

**90° CCW: unverified** — `in_game_visible_travel-656c2323f3a7fe3d1aaf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-944a34e0352e398a52fe"></a>

**180° CCW: unverified** — `in_game_visible_travel-944a34e0352e398a52fe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-44a14e113fe8e6d32b4f"></a>

**270° CCW: unverified** — `in_game_visible_travel-44a14e113fe8e6d32b4f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-15; entry: 1-W-in-12; exit: 1-N-out-15.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17</summary>

<a id="case-in_game_visible_travel-474719545888b39235cd"></a>

**0° CCW: unverified** — `in_game_visible_travel-474719545888b39235cd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-747532a951b8907d8354"></a>

**90° CCW: unverified** — `in_game_visible_travel-747532a951b8907d8354`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-7d40b614b1c816394407"></a>

**180° CCW: unverified** — `in_game_visible_travel-7d40b614b1c816394407`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-fdc2a651d46da95e9815"></a>

**270° CCW: unverified** — `in_game_visible_travel-fdc2a651d46da95e9815`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-N-out-17; entry: 1-S-in-13; exit: 1-N-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11</summary>

<a id="case-in_game_visible_travel-c203030e90895068848d"></a>

**0° CCW: unverified** — `in_game_visible_travel-c203030e90895068848d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-b198626cd9f13f371481"></a>

**90° CCW: unverified** — `in_game_visible_travel-b198626cd9f13f371481`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-e891fdba0cac3e02177b"></a>

**180° CCW: unverified** — `in_game_visible_travel-e891fdba0cac3e02177b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-5f2cf0201de07499336c"></a>

**270° CCW: unverified** — `in_game_visible_travel-5f2cf0201de07499336c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-11; entry: 1-N-in-14; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9</summary>

<a id="case-in_game_visible_travel-f5bf402242c70d8ef08d"></a>

**0° CCW: unverified** — `in_game_visible_travel-f5bf402242c70d8ef08d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-17e8958034f81b8d6faa"></a>

**90° CCW: unverified** — `in_game_visible_travel-17e8958034f81b8d6faa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-93b61a565e2908d61b36"></a>

**180° CCW: unverified** — `in_game_visible_travel-93b61a565e2908d61b36`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-269a01580873da3d9a43"></a>

**270° CCW: unverified** — `in_game_visible_travel-269a01580873da3d9a43`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-9; entry: 1-N-in-16; exit: 1-W-out-9.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 252 cases; unverified: 252</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0aee0d649fbcb98b476">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b45f8990b42d54ce8d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c21c5069f06d3dcbc20c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25a6621bd2fb5c88f1c3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d1d1b2d29096bf5913c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f56f55ed986b2f3875e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4528e2ff9e4ab75b9ab0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37420a17d208be8c0e5f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-695f02d1c34621886a25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f8c23283236b6f2c3d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-360bea405e0bc4d6ab86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9228957aac0773490591">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a24c754d90ec99df446">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-081049ebc9ed19e8054e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f12c18b0d923bfdc2dd4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb43794351b675f13541">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2d3dac869b3d07eaf373">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf0ba817dd9ce62f88bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d1d6bf96a15e6364523">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a06b2f1b4e7e53cf875d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ee4bd7183779ec5853c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0efd12bf0928779324cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a54f20cf6fbbd058cdc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-505d9448aa826c0b06af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aff639267f9f7fcd293d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7f028c64cca1c93d5d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e58fbf384c92ce9e925">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3a49acb88a20de193f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ebb55c4cb8b0aeca591">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f89d64a11397ce09e59b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d785a49f8969ca4362bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-471a71cc6796e610e0e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b20bdacd6ae5f60e5abf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe926284a16a9b2b639d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7a6b4c6d152a48aca45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89bfe1e6d6c5585a92b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f5b23f1709a12ff183cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-105050c589056c7e9f3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cd029222e02348e7f70">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c476167e337d0f0bed11">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ade5156c8adba798613b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c779196af54e72144d83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32c3395e59371851d94c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2df4adb87d3b877ef71e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6068810aa5adb992a035">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-886bbab5c84c1f74ae16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-437f6ed737948195c9fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3a3e8c6d9e8db5c7ec5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ebba66d21f65e164e163">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98e70801d4e2adadfdeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb3e874f1ec2430d51af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ecb2d039dffafd08ee1a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-22b2b91b8c865bba3dfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fec4c7698b430c00395c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e75ecd7067fea8f334d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40f6cc64a80cbb46a558">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-92b0a12950dd954e6d7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f5807583eb516140abc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c19112a689de3cdb8c2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-141e937c5629a80f7ce2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-850f572991d629717868">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa9b6d3281d9c1ada1ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-881911e6523b26bea3ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c0b6ca32e47a4f0c156">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f268add71f2a26500e47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3ebe30cd95bbe702a14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54821921f778f5a6c9e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ced4cf5d2b0d803a3c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9cb1292a8911ee6276b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94e2c74615375070e5e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec873040a7eb2d870b6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76dc277994cf07dbb089">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b7bc8907fddc6da3c542">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce07d348d5eadc440e14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7a5bed9403333c0292a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db6ba1076890cecd3d77">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a612be1ffbdef55037a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84a59456cefdcc36f2eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e018c89ef34d97ff65e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd7e9e0db1516803e740">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-250e27f1320e9179581f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7ccba8c19280cb8f3b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0d8c470da1d748e7d67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-964071c2d89740bacd5c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e0e4dd002b59153e18e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44df032c7fbf60ccf5ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29c3f6768ecc9cb5c0ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4705882b7b0b580dfc8f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-08bd786b0633143a951f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd3caff71e4e26625d5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1eca825f745f156f9df2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27392ab3254dedc5161e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-53cf22c1f3f269a5a814">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb9f1cc7ec4206bff6e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b29a4ec67e819994dc5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77e38c7d7d2f642e5a29">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79e8139231c2667c70ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ac743443c80606649f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf9a4fd3f87961ece580">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11323185e24a6f6acf94">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bc35220c34cecdd8cb37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f8418b85d07f980941e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cbe1615158a044d0f66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9caeb233bc0c94ff7b5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e6cf515ab5c56d47e7ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a96772be0e70e587e077">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7223e128a6bdd960c641">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04ff20f1e78b9381b1e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab914021d3b168f09d8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edfc21046f837b04f15f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bbf4d888b943c9ef00b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99c7599f86b6ead8d769">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-52b8729068dca5035cbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be9d426b0087cdbb1431">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f04f02d2c4dcdd8a7c16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-755f9f50acd31955aabd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-83ae180da58159709598">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f8e20473ef761030f4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c42b8b719ce7ce6d18a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe934629f88331709ee8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bb63cc8ec4de8afdd610">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d42836b8289dfe89816">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d88a3a599ca6df797b79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b71888b70cfe91a0fbe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9326b84e8e403fb3d3f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46e15ee3a8dd084221b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08c1435ba07ad0e9a6a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0190fbee93cb4afc94e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-42239666222bb50e6e2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d226638bccd55672fe0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ebf7c06759fa34b8d27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d17837f850e746231510">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c15dc450eccfda9eea6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f84f4c0e15028ec9afbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acc9141f9a9b3590cc4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7645a46db453c1ae5b69">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c22d33589e983e08153">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81455f29f8649d32918a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c156fdc6281a0c1a238d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b7ef89c56dda2b7653f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2170a2d0418ca4fcd585">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-213f5da0d8f08046fe62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3d0eeb7b9e6b92c6a6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32ce6e82973d9a3f86bd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8051bf6f529c859c9803">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73d8c5f49db8d382f57f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1f968d09e166123344d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-625ff59c4b46e35eaacf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-48f20387552fdd714a8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1530cf2260f4c8bed86f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67c3ec599d5d567e33d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dec69300b3316c694fda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51f604b47f6829732515">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f26263ebaf9ecbbfd73e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98548bf9a07e7527e00a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ffc4cf04e21a096f36d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8f3cd686fb759cde2ea0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e55c502b0883421db3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43aeca3c40cbc5017385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0a4cc543cb8ceb380d1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e7e36b0a693e3f842ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-615752d245f74e31e015">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5b3f3a44e9abcb707ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a81d07fdde70d137802b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-54ef600aeb3df589e4dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-098733b7321672e97827">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eea31cac566c9fd45e14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c39a30538384d00f7b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3fdd8c28667cb6f1f4f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7bcd22f78c305dc85423">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d7b814916d3a1e96382">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f029e4a84bdce484680a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-08a4819f05e9788c9006">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe3ed51c914a8d09e937">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bc3a3cbfc074df0b6d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a001aaf9280be125b73">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-17221f87d2766da02a43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90d05bfe98e8c62cf012">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc3eb8d3d0d7d135adb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-996147649816d9b7a209">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-49f9df403a53f7e50efb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3164555cd9757cd7184c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93185d0d637044f34f86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4bf23ad41c25fc6372f2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-15a9f4bdb69338eba383">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee2172a4925fe347e144">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f61da10c6baf221888f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b898766f375ea1fa848a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3ce81e34d36967da0439">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-025749828a1ff91385c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a35b56eba022ac0e2961">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09d6a0606978ff7c9953">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d1eb60553fe814dbcd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-961b735ad2676b42d55b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9deb81d44c7fb2ec1db9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39c56d5cc1eeec2f1cd3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1ccaa0eaf183e349518">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c90079c03664967df759">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9766bf8b259918c37342">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05b4f55a742ce5d65700">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9c7360991e4c1d694dd2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-daa164e5d2b325cc1976">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0cd1d6334b0308edad3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0dad59c0f5de6ae687b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a5800828e134bb5a88d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91b747c7704fe3c6e273">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c57bc7ff2bf913773665">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21461c232b11bb014751">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1610feb83e1b9ff4ceea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a50b4d03aef7a15b9f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5807009694d8e5da6418">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-314f81c1aac745ff5496">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b45e70b87e16c785b747">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4facae4cb3e930d599d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ff4a1438c4a68d0867f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-575293f22a886e4ee3cf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8c127e1a3fe590ed9abd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47808f3f791a869a0498">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aebfb56811bb0a4ad213">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2234465668fc0904d28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f532b7da51b0d052a597">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b5c0d174a919dab041a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-972d641fb50c0679867c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-528a23e699704438d423">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a0e402c2b01119f968c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55bbbcab9f20e64d6abc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17ef598784baab7a2b6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04108f3a33980624328e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-473df4314a2ea62a35ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ed95b6b48fc61e8f6db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd1683c73d991668b3d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebde7cc107db770d2b37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93ad0634085cbc5fb818">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-141a53be7636194e28bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3ceb76accc893e080ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca312c50a80f0c771d33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7397e8dbadd3eb378e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9687e76c9e460fc5cf6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e01a9eed89491afeb9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-218b2e25568e04a88b67">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ebd7caab27b31e7828a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0d8262cf72d8241fc6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34bb3ace4d4bb4abb834">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6eb603830ca9f7f2d873">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d46f7a56185bfc1f1d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a424b5fd9f3e89c678ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15a62b627f368919dd3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db3e183a5d42f7f0080c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2820a1627fce6b7d578">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6f02a58bc0c0d6c0e5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4a58e1e3d36e30024de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a093600ca3e7b3d6720">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0aee0d649fbcb98b476"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0aee0d649fbcb98b476`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b45f8990b42d54ce8d3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b45f8990b42d54ce8d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c21c5069f06d3dcbc20c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c21c5069f06d3dcbc20c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25a6621bd2fb5c88f1c3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-25a6621bd2fb5c88f1c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d1d1b2d29096bf5913c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d1d1b2d29096bf5913c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f56f55ed986b2f3875e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3f56f55ed986b2f3875e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4528e2ff9e4ab75b9ab0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4528e2ff9e4ab75b9ab0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37420a17d208be8c0e5f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-37420a17d208be8c0e5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-695f02d1c34621886a25"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-695f02d1c34621886a25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f8c23283236b6f2c3d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f8c23283236b6f2c3d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-360bea405e0bc4d6ab86"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-360bea405e0bc4d6ab86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9228957aac0773490591"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9228957aac0773490591`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a24c754d90ec99df446"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a24c754d90ec99df446`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-081049ebc9ed19e8054e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-081049ebc9ed19e8054e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f12c18b0d923bfdc2dd4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f12c18b0d923bfdc2dd4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb43794351b675f13541"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb43794351b675f13541`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2d3dac869b3d07eaf373"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d3dac869b3d07eaf373`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf0ba817dd9ce62f88bc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf0ba817dd9ce62f88bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d1d6bf96a15e6364523"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2d1d6bf96a15e6364523`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a06b2f1b4e7e53cf875d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a06b2f1b4e7e53cf875d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ee4bd7183779ec5853c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ee4bd7183779ec5853c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0efd12bf0928779324cb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0efd12bf0928779324cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a54f20cf6fbbd058cdc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a54f20cf6fbbd058cdc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-505d9448aa826c0b06af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-505d9448aa826c0b06af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aff639267f9f7fcd293d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aff639267f9f7fcd293d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7f028c64cca1c93d5d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d7f028c64cca1c93d5d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e58fbf384c92ce9e925"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1e58fbf384c92ce9e925`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3a49acb88a20de193f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a3a49acb88a20de193f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ebb55c4cb8b0aeca591"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ebb55c4cb8b0aeca591`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f89d64a11397ce09e59b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f89d64a11397ce09e59b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d785a49f8969ca4362bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d785a49f8969ca4362bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-471a71cc6796e610e0e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-471a71cc6796e610e0e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b20bdacd6ae5f60e5abf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b20bdacd6ae5f60e5abf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe926284a16a9b2b639d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe926284a16a9b2b639d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7a6b4c6d152a48aca45"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f7a6b4c6d152a48aca45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89bfe1e6d6c5585a92b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89bfe1e6d6c5585a92b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f5b23f1709a12ff183cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f5b23f1709a12ff183cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-105050c589056c7e9f3e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-105050c589056c7e9f3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cd029222e02348e7f70"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4cd029222e02348e7f70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c476167e337d0f0bed11"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c476167e337d0f0bed11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ade5156c8adba798613b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ade5156c8adba798613b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c779196af54e72144d83"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c779196af54e72144d83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32c3395e59371851d94c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-32c3395e59371851d94c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2df4adb87d3b877ef71e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2df4adb87d3b877ef71e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6068810aa5adb992a035"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6068810aa5adb992a035`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-886bbab5c84c1f74ae16"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-886bbab5c84c1f74ae16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-437f6ed737948195c9fa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-437f6ed737948195c9fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3a3e8c6d9e8db5c7ec5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f3a3e8c6d9e8db5c7ec5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ebba66d21f65e164e163"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ebba66d21f65e164e163`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98e70801d4e2adadfdeb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-98e70801d4e2adadfdeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb3e874f1ec2430d51af"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eb3e874f1ec2430d51af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ecb2d039dffafd08ee1a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ecb2d039dffafd08ee1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-22b2b91b8c865bba3dfa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-22b2b91b8c865bba3dfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fec4c7698b430c00395c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fec4c7698b430c00395c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e75ecd7067fea8f334d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5e75ecd7067fea8f334d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40f6cc64a80cbb46a558"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40f6cc64a80cbb46a558`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-92b0a12950dd954e6d7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-92b0a12950dd954e6d7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f5807583eb516140abc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0f5807583eb516140abc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c19112a689de3cdb8c2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c19112a689de3cdb8c2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-141e937c5629a80f7ce2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-141e937c5629a80f7ce2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-850f572991d629717868"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-850f572991d629717868`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa9b6d3281d9c1ada1ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa9b6d3281d9c1ada1ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-881911e6523b26bea3ad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-881911e6523b26bea3ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c0b6ca32e47a4f0c156"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1c0b6ca32e47a4f0c156`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f268add71f2a26500e47"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f268add71f2a26500e47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3ebe30cd95bbe702a14"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e3ebe30cd95bbe702a14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54821921f778f5a6c9e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54821921f778f5a6c9e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ced4cf5d2b0d803a3c7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ced4cf5d2b0d803a3c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9cb1292a8911ee6276b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9cb1292a8911ee6276b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94e2c74615375070e5e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94e2c74615375070e5e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec873040a7eb2d870b6f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ec873040a7eb2d870b6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76dc277994cf07dbb089"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-76dc277994cf07dbb089`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b7bc8907fddc6da3c542"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b7bc8907fddc6da3c542`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce07d348d5eadc440e14"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce07d348d5eadc440e14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7a5bed9403333c0292a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f7a5bed9403333c0292a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db6ba1076890cecd3d77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db6ba1076890cecd3d77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a612be1ffbdef55037a5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a612be1ffbdef55037a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84a59456cefdcc36f2eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-84a59456cefdcc36f2eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e018c89ef34d97ff65e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e018c89ef34d97ff65e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd7e9e0db1516803e740"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd7e9e0db1516803e740`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-250e27f1320e9179581f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-250e27f1320e9179581f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7ccba8c19280cb8f3b3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d7ccba8c19280cb8f3b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0d8c470da1d748e7d67"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0d8c470da1d748e7d67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-964071c2d89740bacd5c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-964071c2d89740bacd5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e0e4dd002b59153e18e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e0e4dd002b59153e18e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44df032c7fbf60ccf5ee"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-44df032c7fbf60ccf5ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29c3f6768ecc9cb5c0ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-29c3f6768ecc9cb5c0ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4705882b7b0b580dfc8f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4705882b7b0b580dfc8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-08bd786b0633143a951f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-08bd786b0633143a951f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd3caff71e4e26625d5c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd3caff71e4e26625d5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1eca825f745f156f9df2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1eca825f745f156f9df2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27392ab3254dedc5161e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27392ab3254dedc5161e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-53cf22c1f3f269a5a814"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53cf22c1f3f269a5a814`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb9f1cc7ec4206bff6e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eb9f1cc7ec4206bff6e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b29a4ec67e819994dc5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6b29a4ec67e819994dc5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77e38c7d7d2f642e5a29"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77e38c7d7d2f642e5a29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79e8139231c2667c70ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79e8139231c2667c70ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ac743443c80606649f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1ac743443c80606649f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf9a4fd3f87961ece580"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bf9a4fd3f87961ece580`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11323185e24a6f6acf94"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-11323185e24a6f6acf94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bc35220c34cecdd8cb37"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bc35220c34cecdd8cb37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f8418b85d07f980941e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f8418b85d07f980941e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cbe1615158a044d0f66"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6cbe1615158a044d0f66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9caeb233bc0c94ff7b5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b9caeb233bc0c94ff7b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e6cf515ab5c56d47e7ad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e6cf515ab5c56d47e7ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a96772be0e70e587e077"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a96772be0e70e587e077`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7223e128a6bdd960c641"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7223e128a6bdd960c641`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04ff20f1e78b9381b1e4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-04ff20f1e78b9381b1e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab914021d3b168f09d8d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab914021d3b168f09d8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edfc21046f837b04f15f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-edfc21046f837b04f15f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bbf4d888b943c9ef00b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2bbf4d888b943c9ef00b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99c7599f86b6ead8d769"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-99c7599f86b6ead8d769`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-52b8729068dca5035cbb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-52b8729068dca5035cbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be9d426b0087cdbb1431"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-be9d426b0087cdbb1431`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f04f02d2c4dcdd8a7c16"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f04f02d2c4dcdd8a7c16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-755f9f50acd31955aabd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-755f9f50acd31955aabd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-83ae180da58159709598"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-83ae180da58159709598`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f8e20473ef761030f4f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f8e20473ef761030f4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c42b8b719ce7ce6d18a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c42b8b719ce7ce6d18a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe934629f88331709ee8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe934629f88331709ee8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bb63cc8ec4de8afdd610"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bb63cc8ec4de8afdd610`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d42836b8289dfe89816"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6d42836b8289dfe89816`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d88a3a599ca6df797b79"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d88a3a599ca6df797b79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b71888b70cfe91a0fbe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b71888b70cfe91a0fbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9326b84e8e403fb3d3f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9326b84e8e403fb3d3f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46e15ee3a8dd084221b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-46e15ee3a8dd084221b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08c1435ba07ad0e9a6a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-08c1435ba07ad0e9a6a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0190fbee93cb4afc94e4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0190fbee93cb4afc94e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-42239666222bb50e6e2d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-42239666222bb50e6e2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d226638bccd55672fe0f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d226638bccd55672fe0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ebf7c06759fa34b8d27"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0ebf7c06759fa34b8d27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d17837f850e746231510"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d17837f850e746231510`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c15dc450eccfda9eea6e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c15dc450eccfda9eea6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f84f4c0e15028ec9afbc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f84f4c0e15028ec9afbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acc9141f9a9b3590cc4e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-acc9141f9a9b3590cc4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7645a46db453c1ae5b69"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7645a46db453c1ae5b69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c22d33589e983e08153"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c22d33589e983e08153`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81455f29f8649d32918a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81455f29f8649d32918a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c156fdc6281a0c1a238d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c156fdc6281a0c1a238d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b7ef89c56dda2b7653f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b7ef89c56dda2b7653f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2170a2d0418ca4fcd585"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2170a2d0418ca4fcd585`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-213f5da0d8f08046fe62"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-213f5da0d8f08046fe62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3d0eeb7b9e6b92c6a6e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a3d0eeb7b9e6b92c6a6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32ce6e82973d9a3f86bd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-32ce6e82973d9a3f86bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8051bf6f529c859c9803"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8051bf6f529c859c9803`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73d8c5f49db8d382f57f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-73d8c5f49db8d382f57f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1f968d09e166123344d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a1f968d09e166123344d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-625ff59c4b46e35eaacf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-625ff59c4b46e35eaacf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-48f20387552fdd714a8d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-48f20387552fdd714a8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1530cf2260f4c8bed86f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1530cf2260f4c8bed86f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67c3ec599d5d567e33d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67c3ec599d5d567e33d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dec69300b3316c694fda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dec69300b3316c694fda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51f604b47f6829732515"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51f604b47f6829732515`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f26263ebaf9ecbbfd73e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f26263ebaf9ecbbfd73e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98548bf9a07e7527e00a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98548bf9a07e7527e00a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ffc4cf04e21a096f36d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ffc4cf04e21a096f36d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8f3cd686fb759cde2ea0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f3cd686fb759cde2ea0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e55c502b0883421db3c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e55c502b0883421db3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43aeca3c40cbc5017385"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-43aeca3c40cbc5017385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0a4cc543cb8ceb380d1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c0a4cc543cb8ceb380d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e7e36b0a693e3f842ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e7e36b0a693e3f842ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-615752d245f74e31e015"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-615752d245f74e31e015`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5b3f3a44e9abcb707ac"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5b3f3a44e9abcb707ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a81d07fdde70d137802b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a81d07fdde70d137802b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-54ef600aeb3df589e4dd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-54ef600aeb3df589e4dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-098733b7321672e97827"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-098733b7321672e97827`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eea31cac566c9fd45e14"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eea31cac566c9fd45e14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c39a30538384d00f7b9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5c39a30538384d00f7b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3fdd8c28667cb6f1f4f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3fdd8c28667cb6f1f4f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7bcd22f78c305dc85423"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7bcd22f78c305dc85423`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d7b814916d3a1e96382"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d7b814916d3a1e96382`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f029e4a84bdce484680a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f029e4a84bdce484680a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-08a4819f05e9788c9006"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-08a4819f05e9788c9006`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe3ed51c914a8d09e937"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe3ed51c914a8d09e937`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bc3a3cbfc074df0b6d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8bc3a3cbfc074df0b6d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a001aaf9280be125b73"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1a001aaf9280be125b73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-17221f87d2766da02a43"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-17221f87d2766da02a43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90d05bfe98e8c62cf012"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-90d05bfe98e8c62cf012`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc3eb8d3d0d7d135adb9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fc3eb8d3d0d7d135adb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-996147649816d9b7a209"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-996147649816d9b7a209`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-49f9df403a53f7e50efb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49f9df403a53f7e50efb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3164555cd9757cd7184c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3164555cd9757cd7184c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93185d0d637044f34f86"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-93185d0d637044f34f86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4bf23ad41c25fc6372f2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4bf23ad41c25fc6372f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-15a9f4bdb69338eba383"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-15a9f4bdb69338eba383`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee2172a4925fe347e144"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ee2172a4925fe347e144`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f61da10c6baf221888f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f61da10c6baf221888f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b898766f375ea1fa848a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b898766f375ea1fa848a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3ce81e34d36967da0439"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3ce81e34d36967da0439`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-025749828a1ff91385c7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-025749828a1ff91385c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a35b56eba022ac0e2961"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a35b56eba022ac0e2961`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09d6a0606978ff7c9953"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-09d6a0606978ff7c9953`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d1eb60553fe814dbcd1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d1eb60553fe814dbcd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-961b735ad2676b42d55b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-961b735ad2676b42d55b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9deb81d44c7fb2ec1db9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9deb81d44c7fb2ec1db9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39c56d5cc1eeec2f1cd3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39c56d5cc1eeec2f1cd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d1ccaa0eaf183e349518"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1ccaa0eaf183e349518`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c90079c03664967df759"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c90079c03664967df759`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9766bf8b259918c37342"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9766bf8b259918c37342`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05b4f55a742ce5d65700"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-05b4f55a742ce5d65700`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9c7360991e4c1d694dd2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9c7360991e4c1d694dd2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-daa164e5d2b325cc1976"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-daa164e5d2b325cc1976`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0cd1d6334b0308edad3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f0cd1d6334b0308edad3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0dad59c0f5de6ae687b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a0dad59c0f5de6ae687b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a5800828e134bb5a88d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a5800828e134bb5a88d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91b747c7704fe3c6e273"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-91b747c7704fe3c6e273`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c57bc7ff2bf913773665"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c57bc7ff2bf913773665`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21461c232b11bb014751"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-21461c232b11bb014751`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1610feb83e1b9ff4ceea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1610feb83e1b9ff4ceea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a50b4d03aef7a15b9f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a50b4d03aef7a15b9f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5807009694d8e5da6418"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5807009694d8e5da6418`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-314f81c1aac745ff5496"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-314f81c1aac745ff5496`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b45e70b87e16c785b747"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b45e70b87e16c785b747`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4facae4cb3e930d599d8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4facae4cb3e930d599d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ff4a1438c4a68d0867f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7ff4a1438c4a68d0867f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-575293f22a886e4ee3cf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-575293f22a886e4ee3cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8c127e1a3fe590ed9abd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8c127e1a3fe590ed9abd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47808f3f791a869a0498"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47808f3f791a869a0498`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aebfb56811bb0a4ad213"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aebfb56811bb0a4ad213`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2234465668fc0904d28"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d2234465668fc0904d28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f532b7da51b0d052a597"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f532b7da51b0d052a597`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b5c0d174a919dab041a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1b5c0d174a919dab041a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-972d641fb50c0679867c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-972d641fb50c0679867c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-528a23e699704438d423"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-528a23e699704438d423`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a0e402c2b01119f968c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a0e402c2b01119f968c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55bbbcab9f20e64d6abc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-55bbbcab9f20e64d6abc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17ef598784baab7a2b6d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-17ef598784baab7a2b6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04108f3a33980624328e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-04108f3a33980624328e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-473df4314a2ea62a35ef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-473df4314a2ea62a35ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ed95b6b48fc61e8f6db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ed95b6b48fc61e8f6db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd1683c73d991668b3d6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dd1683c73d991668b3d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebde7cc107db770d2b37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ebde7cc107db770d2b37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93ad0634085cbc5fb818"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93ad0634085cbc5fb818`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-141a53be7636194e28bd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-141a53be7636194e28bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3ceb76accc893e080ba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d3ceb76accc893e080ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca312c50a80f0c771d33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ca312c50a80f0c771d33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7397e8dbadd3eb378e2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7397e8dbadd3eb378e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9687e76c9e460fc5cf6a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9687e76c9e460fc5cf6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e01a9eed89491afeb9a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7e01a9eed89491afeb9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-218b2e25568e04a88b67"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-218b2e25568e04a88b67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ebd7caab27b31e7828a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ebd7caab27b31e7828a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0d8262cf72d8241fc6c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0d8262cf72d8241fc6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34bb3ace4d4bb4abb834"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-34bb3ace4d4bb4abb834`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6eb603830ca9f7f2d873"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6eb603830ca9f7f2d873`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d46f7a56185bfc1f1d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d46f7a56185bfc1f1d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a424b5fd9f3e89c678ee"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a424b5fd9f3e89c678ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15a62b627f368919dd3a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-15a62b627f368919dd3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db3e183a5d42f7f0080c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db3e183a5d42f7f0080c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c2820a1627fce6b7d578"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c2820a1627fce6b7d578`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6f02a58bc0c0d6c0e5e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f6f02a58bc0c0d6c0e5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4a58e1e3d36e30024de"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4a58e1e3d36e30024de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a093600ca3e7b3d6720"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0a093600ca3e7b3d6720`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-upper-entry-branch:canonical-southeast | <a href="#case-preview_review-1e28f35de70eb66906db">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-upper-entry-branch:canonical-top | <a href="#case-preview_review-1e6759e12ec6b2d2fadd">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-upper-entry-branch:connection-overview | <a href="#case-preview_review-a74e627aaea446a7edd8">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-upper-entry-branch:canonical-southeast</summary>

<a id="case-preview_review-1e28f35de70eb66906db"></a>

**General: unverified** — `preview_review-1e28f35de70eb66906db`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-upper-entry-branch:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-upper-entry-branch:canonical-top</summary>

<a id="case-preview_review-1e6759e12ec6b2d2fadd"></a>

**General: unverified** — `preview_review-1e6759e12ec6b2d2fadd`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-upper-entry-branch:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-upper-entry-branch:connection-overview</summary>

<a id="case-preview_review-a74e627aaea446a7edd8"></a>

**General: unverified** — `preview_review-a74e627aaea446a7edd8`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-upper-entry-branch:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
