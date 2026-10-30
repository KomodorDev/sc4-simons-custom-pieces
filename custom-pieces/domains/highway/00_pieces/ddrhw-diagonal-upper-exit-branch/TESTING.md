---
title: "Testing: DD RHW-4 \u2014 Upper Diagonal Exit Branch"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Upper Diagonal Exit Branch

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Divides an outer upper-deck lane into a continuing highway lane and an off-ramp towards the southeast avenue access. The ramp stays level until it clears the lower deck. The opposite upper-deck edge remains closed, and the branch owns the outer native cell crossed by its ramp faces. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

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
| `1-N-in-5` | road / 1 / primary | in | [12.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-6` | road / 1 / primary | out | [12.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-7` | road / 1 / primary | in | [19.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-8` | road / 1 / primary | out | [19.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-W-out-9` | road / 1 / primary | out | [24.0, -3.2, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-10` | road / 1 / primary | in | [24.0, -3.2, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-11` | road / 1 / primary | out | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-12` | road / 1 / primary | in | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-N-in-13` | road / 1 / primary | in | [28.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-14` | road / 1 / primary | out | [28.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-15` | road / 1 / primary | in | [35.2, 8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-16` | road / 1 / primary | out | [35.2, 8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-E-out-17` | road / 1 / primary | out | [40.0, -8.142765, 12.25824]; [0.9273187516299957, 0.3742725382330187]; -0.296094955 | `path-interface-92b7bb8a032d6d3b22a6` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-2` → `1-E-out-17` | primary |
| road | `1-W-in-2` → `1-N-out-8` | primary |
| road | `1-W-in-4` → `1-N-out-6` | primary |
| road | `1-N-in-5` → `1-W-out-3` | primary |
| road | `1-N-in-7` → `1-W-out-1` | primary |
| road | `1-W-in-10` → `1-N-out-16` | primary |
| road | `1-W-in-12` → `1-N-out-14` | primary |
| road | `1-N-in-13` → `1-W-out-11` | primary |
| road | `1-N-in-15` → `1-W-out-9` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-2` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-N-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-10` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-12` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-13` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-13` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-13` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-13` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-13` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-13` | road / `1-N-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-13` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-13` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-15` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-15` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-15` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-15` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-15` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-15` | road / `1-N-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-15` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-15` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-upper-exit-branch --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
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

Current totals: unverified: 344, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-upper-exit-branch/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-upper-exit-branch/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-30435f050af4dddc4402">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-30435f050af4dddc4402"></a>

**General: unverified** — `software_resources-30435f050af4dddc4402`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-30435f050af4dddc4402">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-30435f050af4dddc4402"></a>

**General: unverified** — `software_connectivity-30435f050af4dddc4402`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-upper-exit-branch:canonical-southeast | <a href="#case-preview_review-11004322b7ae9415cef0">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-upper-exit-branch:canonical-top | <a href="#case-preview_review-c03d8bbead86720db7e9">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-upper-exit-branch:canonical-southeast</summary>

<a id="case-preview_review-11004322b7ae9415cef0"></a>

**General: unverified** — `preview_review-11004322b7ae9415cef0`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-diagonal-upper-exit-branch:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-upper-exit-branch:canonical-top</summary>

<a id="case-preview_review-c03d8bbead86720db7e9"></a>

**General: unverified** — `preview_review-c03d8bbead86720db7e9`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-diagonal-upper-exit-branch:canonical-top.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-a392dce6281d4c6b964a">[ ] unverified</a> | <a href="#case-in_game_render-1b41066e605804068b83">[ ] unverified</a> | <a href="#case-in_game_render-eb59547e24a07c975251">[ ] unverified</a> | <a href="#case-in_game_render-100e580c5d7886a0926e">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-a392dce6281d4c6b964a"></a>

**0° CCW: unverified** — `in_game_render-a392dce6281d4c6b964a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1b41066e605804068b83"></a>

**90° CCW: unverified** — `in_game_render-1b41066e605804068b83`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-eb59547e24a07c975251"></a>

**180° CCW: unverified** — `in_game_render-eb59547e24a07c975251`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-100e580c5d7886a0926e"></a>

**270° CCW: unverified** — `in_game_render-100e580c5d7886a0926e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-a392dce6281d4c6b964a">[ ] unverified</a> | <a href="#case-in_game_placement-1b41066e605804068b83">[ ] unverified</a> | <a href="#case-in_game_placement-eb59547e24a07c975251">[ ] unverified</a> | <a href="#case-in_game_placement-100e580c5d7886a0926e">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-a392dce6281d4c6b964a"></a>

**0° CCW: unverified** — `in_game_placement-a392dce6281d4c6b964a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1b41066e605804068b83"></a>

**90° CCW: unverified** — `in_game_placement-1b41066e605804068b83`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-eb59547e24a07c975251"></a>

**180° CCW: unverified** — `in_game_placement-eb59547e24a07c975251`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-100e580c5d7886a0926e"></a>

**270° CCW: unverified** — `in_game_placement-100e580c5d7886a0926e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-a392dce6281d4c6b964a">[ ] unverified</a> | <a href="#case-in_game_demolition-1b41066e605804068b83">[ ] unverified</a> | <a href="#case-in_game_demolition-eb59547e24a07c975251">[ ] unverified</a> | <a href="#case-in_game_demolition-100e580c5d7886a0926e">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-a392dce6281d4c6b964a"></a>

**0° CCW: unverified** — `in_game_demolition-a392dce6281d4c6b964a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1b41066e605804068b83"></a>

**90° CCW: unverified** — `in_game_demolition-1b41066e605804068b83`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-eb59547e24a07c975251"></a>

**180° CCW: unverified** — `in_game_demolition-eb59547e24a07c975251`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-100e580c5d7886a0926e"></a>

**270° CCW: unverified** — `in_game_demolition-100e580c5d7886a0926e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-a392dce6281d4c6b964a">[ ] unverified</a> | <a href="#case-in_game_save_reload-1b41066e605804068b83">[ ] unverified</a> | <a href="#case-in_game_save_reload-eb59547e24a07c975251">[ ] unverified</a> | <a href="#case-in_game_save_reload-100e580c5d7886a0926e">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-a392dce6281d4c6b964a"></a>

**0° CCW: unverified** — `in_game_save_reload-a392dce6281d4c6b964a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1b41066e605804068b83"></a>

**90° CCW: unverified** — `in_game_save_reload-1b41066e605804068b83`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-eb59547e24a07c975251"></a>

**180° CCW: unverified** — `in_game_save_reload-eb59547e24a07c975251`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-100e580c5d7886a0926e"></a>

**270° CCW: unverified** — `in_game_save_reload-100e580c5d7886a0926e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17 | — | <a href="#case-in_game_route_query-77d1e715223e907493b4">[ ] unverified</a> | <a href="#case-in_game_route_query-a2230482caa3419b2444">[ ] unverified</a> | <a href="#case-in_game_route_query-415f6f0f613ad899ee18">[ ] unverified</a> | <a href="#case-in_game_route_query-4c204898eb8b2224cf3a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8 | — | <a href="#case-in_game_route_query-a9cd01cd0aa83c5c0c17">[ ] unverified</a> | <a href="#case-in_game_route_query-c6f1e3d92f88d015478d">[ ] unverified</a> | <a href="#case-in_game_route_query-a2f1d117653db1befbd7">[ ] unverified</a> | <a href="#case-in_game_route_query-062025eea805ffdf3625">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6 | — | <a href="#case-in_game_route_query-28ef6c9004b804688317">[ ] unverified</a> | <a href="#case-in_game_route_query-3d479d59532f7f429d09">[ ] unverified</a> | <a href="#case-in_game_route_query-79c3c85d5ae82bfddfa7">[ ] unverified</a> | <a href="#case-in_game_route_query-612ae2d46d26f3581998">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-5f8f169a294c52371f4e">[ ] unverified</a> | <a href="#case-in_game_route_query-2cc2ce4b9c9ab60c873b">[ ] unverified</a> | <a href="#case-in_game_route_query-1dc5d518f3f36558adac">[ ] unverified</a> | <a href="#case-in_game_route_query-36abe771de475584a615">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-f7f154ec2d53c9902875">[ ] unverified</a> | <a href="#case-in_game_route_query-16cd46dc65e05d5c1a9e">[ ] unverified</a> | <a href="#case-in_game_route_query-b68f353c4a79cfe918ff">[ ] unverified</a> | <a href="#case-in_game_route_query-b72926268932fa653d0f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16 | — | <a href="#case-in_game_route_query-a977c3c16e7c8481949f">[ ] unverified</a> | <a href="#case-in_game_route_query-d651f4cd1f20cb071433">[ ] unverified</a> | <a href="#case-in_game_route_query-5c2a08b46d440faee3d0">[ ] unverified</a> | <a href="#case-in_game_route_query-746a5f49df25e35dbaaf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14 | — | <a href="#case-in_game_route_query-3e27a03aef3c6075dd88">[ ] unverified</a> | <a href="#case-in_game_route_query-c5a3ce89163b1d2750bc">[ ] unverified</a> | <a href="#case-in_game_route_query-63bca56a03ff787de01e">[ ] unverified</a> | <a href="#case-in_game_route_query-d4c56f95f5c622c85f1e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11 | — | <a href="#case-in_game_route_query-f25cded85c4f3b4d9dd4">[ ] unverified</a> | <a href="#case-in_game_route_query-c56a948b99081462fe0b">[ ] unverified</a> | <a href="#case-in_game_route_query-dbba4a702d5c74e4ce0e">[ ] unverified</a> | <a href="#case-in_game_route_query-0cf3bfe62f913e311a21">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9 | — | <a href="#case-in_game_route_query-2d13aaf71d7fd9b224d2">[ ] unverified</a> | <a href="#case-in_game_route_query-bb992f226a7b9273e0c4">[ ] unverified</a> | <a href="#case-in_game_route_query-74a74bbd1cc42dd6dc41">[ ] unverified</a> | <a href="#case-in_game_route_query-a9072eee5aeedd23846d">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17</summary>

<a id="case-in_game_route_query-77d1e715223e907493b4"></a>

**0° CCW: unverified** — `in_game_route_query-77d1e715223e907493b4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-a2230482caa3419b2444"></a>

**90° CCW: unverified** — `in_game_route_query-a2230482caa3419b2444`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-415f6f0f613ad899ee18"></a>

**180° CCW: unverified** — `in_game_route_query-415f6f0f613ad899ee18`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-4c204898eb8b2224cf3a"></a>

**270° CCW: unverified** — `in_game_route_query-4c204898eb8b2224cf3a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8</summary>

<a id="case-in_game_route_query-a9cd01cd0aa83c5c0c17"></a>

**0° CCW: unverified** — `in_game_route_query-a9cd01cd0aa83c5c0c17`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-c6f1e3d92f88d015478d"></a>

**90° CCW: unverified** — `in_game_route_query-c6f1e3d92f88d015478d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-a2f1d117653db1befbd7"></a>

**180° CCW: unverified** — `in_game_route_query-a2f1d117653db1befbd7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-062025eea805ffdf3625"></a>

**270° CCW: unverified** — `in_game_route_query-062025eea805ffdf3625`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6</summary>

<a id="case-in_game_route_query-28ef6c9004b804688317"></a>

**0° CCW: unverified** — `in_game_route_query-28ef6c9004b804688317`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-3d479d59532f7f429d09"></a>

**90° CCW: unverified** — `in_game_route_query-3d479d59532f7f429d09`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-79c3c85d5ae82bfddfa7"></a>

**180° CCW: unverified** — `in_game_route_query-79c3c85d5ae82bfddfa7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-612ae2d46d26f3581998"></a>

**270° CCW: unverified** — `in_game_route_query-612ae2d46d26f3581998`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3</summary>

<a id="case-in_game_route_query-5f8f169a294c52371f4e"></a>

**0° CCW: unverified** — `in_game_route_query-5f8f169a294c52371f4e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-2cc2ce4b9c9ab60c873b"></a>

**90° CCW: unverified** — `in_game_route_query-2cc2ce4b9c9ab60c873b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-1dc5d518f3f36558adac"></a>

**180° CCW: unverified** — `in_game_route_query-1dc5d518f3f36558adac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-36abe771de475584a615"></a>

**270° CCW: unverified** — `in_game_route_query-36abe771de475584a615`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-f7f154ec2d53c9902875"></a>

**0° CCW: unverified** — `in_game_route_query-f7f154ec2d53c9902875`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-16cd46dc65e05d5c1a9e"></a>

**90° CCW: unverified** — `in_game_route_query-16cd46dc65e05d5c1a9e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-b68f353c4a79cfe918ff"></a>

**180° CCW: unverified** — `in_game_route_query-b68f353c4a79cfe918ff`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-b72926268932fa653d0f"></a>

**270° CCW: unverified** — `in_game_route_query-b72926268932fa653d0f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16</summary>

<a id="case-in_game_route_query-a977c3c16e7c8481949f"></a>

**0° CCW: unverified** — `in_game_route_query-a977c3c16e7c8481949f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_route_query-d651f4cd1f20cb071433"></a>

**90° CCW: unverified** — `in_game_route_query-d651f4cd1f20cb071433`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_route_query-5c2a08b46d440faee3d0"></a>

**180° CCW: unverified** — `in_game_route_query-5c2a08b46d440faee3d0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_route_query-746a5f49df25e35dbaaf"></a>

**270° CCW: unverified** — `in_game_route_query-746a5f49df25e35dbaaf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14</summary>

<a id="case-in_game_route_query-3e27a03aef3c6075dd88"></a>

**0° CCW: unverified** — `in_game_route_query-3e27a03aef3c6075dd88`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14.

No observation recorded.

<a id="case-in_game_route_query-c5a3ce89163b1d2750bc"></a>

**90° CCW: unverified** — `in_game_route_query-c5a3ce89163b1d2750bc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14.

No observation recorded.

<a id="case-in_game_route_query-63bca56a03ff787de01e"></a>

**180° CCW: unverified** — `in_game_route_query-63bca56a03ff787de01e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14.

No observation recorded.

<a id="case-in_game_route_query-d4c56f95f5c622c85f1e"></a>

**270° CCW: unverified** — `in_game_route_query-d4c56f95f5c622c85f1e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11</summary>

<a id="case-in_game_route_query-f25cded85c4f3b4d9dd4"></a>

**0° CCW: unverified** — `in_game_route_query-f25cded85c4f3b4d9dd4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-c56a948b99081462fe0b"></a>

**90° CCW: unverified** — `in_game_route_query-c56a948b99081462fe0b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-dbba4a702d5c74e4ce0e"></a>

**180° CCW: unverified** — `in_game_route_query-dbba4a702d5c74e4ce0e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-0cf3bfe62f913e311a21"></a>

**270° CCW: unverified** — `in_game_route_query-0cf3bfe62f913e311a21`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9</summary>

<a id="case-in_game_route_query-2d13aaf71d7fd9b224d2"></a>

**0° CCW: unverified** — `in_game_route_query-2d13aaf71d7fd9b224d2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-bb992f226a7b9273e0c4"></a>

**90° CCW: unverified** — `in_game_route_query-bb992f226a7b9273e0c4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-74a74bbd1cc42dd6dc41"></a>

**180° CCW: unverified** — `in_game_route_query-74a74bbd1cc42dd6dc41`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-a9072eee5aeedd23846d"></a>

**270° CCW: unverified** — `in_game_route_query-a9072eee5aeedd23846d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17 | — | <a href="#case-in_game_visible_travel-77d1e715223e907493b4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a2230482caa3419b2444">[ ] unverified</a> | <a href="#case-in_game_visible_travel-415f6f0f613ad899ee18">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4c204898eb8b2224cf3a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8 | — | <a href="#case-in_game_visible_travel-a9cd01cd0aa83c5c0c17">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c6f1e3d92f88d015478d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a2f1d117653db1befbd7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-062025eea805ffdf3625">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6 | — | <a href="#case-in_game_visible_travel-28ef6c9004b804688317">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3d479d59532f7f429d09">[ ] unverified</a> | <a href="#case-in_game_visible_travel-79c3c85d5ae82bfddfa7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-612ae2d46d26f3581998">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-5f8f169a294c52371f4e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2cc2ce4b9c9ab60c873b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1dc5d518f3f36558adac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-36abe771de475584a615">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-f7f154ec2d53c9902875">[ ] unverified</a> | <a href="#case-in_game_visible_travel-16cd46dc65e05d5c1a9e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b68f353c4a79cfe918ff">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b72926268932fa653d0f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16 | — | <a href="#case-in_game_visible_travel-a977c3c16e7c8481949f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d651f4cd1f20cb071433">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5c2a08b46d440faee3d0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-746a5f49df25e35dbaaf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14 | — | <a href="#case-in_game_visible_travel-3e27a03aef3c6075dd88">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c5a3ce89163b1d2750bc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-63bca56a03ff787de01e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d4c56f95f5c622c85f1e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11 | — | <a href="#case-in_game_visible_travel-f25cded85c4f3b4d9dd4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c56a948b99081462fe0b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dbba4a702d5c74e4ce0e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0cf3bfe62f913e311a21">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9 | — | <a href="#case-in_game_visible_travel-2d13aaf71d7fd9b224d2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bb992f226a7b9273e0c4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-74a74bbd1cc42dd6dc41">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a9072eee5aeedd23846d">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17</summary>

<a id="case-in_game_visible_travel-77d1e715223e907493b4"></a>

**0° CCW: unverified** — `in_game_visible_travel-77d1e715223e907493b4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-a2230482caa3419b2444"></a>

**90° CCW: unverified** — `in_game_visible_travel-a2230482caa3419b2444`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-415f6f0f613ad899ee18"></a>

**180° CCW: unverified** — `in_game_visible_travel-415f6f0f613ad899ee18`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-4c204898eb8b2224cf3a"></a>

**270° CCW: unverified** — `in_game_visible_travel-4c204898eb8b2224cf3a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-17; entry: 1-W-in-2; exit: 1-E-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8</summary>

<a id="case-in_game_visible_travel-a9cd01cd0aa83c5c0c17"></a>

**0° CCW: unverified** — `in_game_visible_travel-a9cd01cd0aa83c5c0c17`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-c6f1e3d92f88d015478d"></a>

**90° CCW: unverified** — `in_game_visible_travel-c6f1e3d92f88d015478d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-a2f1d117653db1befbd7"></a>

**180° CCW: unverified** — `in_game_visible_travel-a2f1d117653db1befbd7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-062025eea805ffdf3625"></a>

**270° CCW: unverified** — `in_game_visible_travel-062025eea805ffdf3625`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6</summary>

<a id="case-in_game_visible_travel-28ef6c9004b804688317"></a>

**0° CCW: unverified** — `in_game_visible_travel-28ef6c9004b804688317`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-3d479d59532f7f429d09"></a>

**90° CCW: unverified** — `in_game_visible_travel-3d479d59532f7f429d09`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-79c3c85d5ae82bfddfa7"></a>

**180° CCW: unverified** — `in_game_visible_travel-79c3c85d5ae82bfddfa7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-612ae2d46d26f3581998"></a>

**270° CCW: unverified** — `in_game_visible_travel-612ae2d46d26f3581998`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3</summary>

<a id="case-in_game_visible_travel-5f8f169a294c52371f4e"></a>

**0° CCW: unverified** — `in_game_visible_travel-5f8f169a294c52371f4e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-2cc2ce4b9c9ab60c873b"></a>

**90° CCW: unverified** — `in_game_visible_travel-2cc2ce4b9c9ab60c873b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-1dc5d518f3f36558adac"></a>

**180° CCW: unverified** — `in_game_visible_travel-1dc5d518f3f36558adac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-36abe771de475584a615"></a>

**270° CCW: unverified** — `in_game_visible_travel-36abe771de475584a615`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-f7f154ec2d53c9902875"></a>

**0° CCW: unverified** — `in_game_visible_travel-f7f154ec2d53c9902875`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-16cd46dc65e05d5c1a9e"></a>

**90° CCW: unverified** — `in_game_visible_travel-16cd46dc65e05d5c1a9e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-b68f353c4a79cfe918ff"></a>

**180° CCW: unverified** — `in_game_visible_travel-b68f353c4a79cfe918ff`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-b72926268932fa653d0f"></a>

**270° CCW: unverified** — `in_game_visible_travel-b72926268932fa653d0f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16</summary>

<a id="case-in_game_visible_travel-a977c3c16e7c8481949f"></a>

**0° CCW: unverified** — `in_game_visible_travel-a977c3c16e7c8481949f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-d651f4cd1f20cb071433"></a>

**90° CCW: unverified** — `in_game_visible_travel-d651f4cd1f20cb071433`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-5c2a08b46d440faee3d0"></a>

**180° CCW: unverified** — `in_game_visible_travel-5c2a08b46d440faee3d0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-746a5f49df25e35dbaaf"></a>

**270° CCW: unverified** — `in_game_visible_travel-746a5f49df25e35dbaaf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-10>1-N-out-16; entry: 1-W-in-10; exit: 1-N-out-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14</summary>

<a id="case-in_game_visible_travel-3e27a03aef3c6075dd88"></a>

**0° CCW: unverified** — `in_game_visible_travel-3e27a03aef3c6075dd88`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14.

No observation recorded.

<a id="case-in_game_visible_travel-c5a3ce89163b1d2750bc"></a>

**90° CCW: unverified** — `in_game_visible_travel-c5a3ce89163b1d2750bc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14.

No observation recorded.

<a id="case-in_game_visible_travel-63bca56a03ff787de01e"></a>

**180° CCW: unverified** — `in_game_visible_travel-63bca56a03ff787de01e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14.

No observation recorded.

<a id="case-in_game_visible_travel-d4c56f95f5c622c85f1e"></a>

**270° CCW: unverified** — `in_game_visible_travel-d4c56f95f5c622c85f1e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-12>1-N-out-14; entry: 1-W-in-12; exit: 1-N-out-14.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11</summary>

<a id="case-in_game_visible_travel-f25cded85c4f3b4d9dd4"></a>

**0° CCW: unverified** — `in_game_visible_travel-f25cded85c4f3b4d9dd4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-c56a948b99081462fe0b"></a>

**90° CCW: unverified** — `in_game_visible_travel-c56a948b99081462fe0b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-dbba4a702d5c74e4ce0e"></a>

**180° CCW: unverified** — `in_game_visible_travel-dbba4a702d5c74e4ce0e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-0cf3bfe62f913e311a21"></a>

**270° CCW: unverified** — `in_game_visible_travel-0cf3bfe62f913e311a21`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-13>1-W-out-11; entry: 1-N-in-13; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9</summary>

<a id="case-in_game_visible_travel-2d13aaf71d7fd9b224d2"></a>

**0° CCW: unverified** — `in_game_visible_travel-2d13aaf71d7fd9b224d2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-bb992f226a7b9273e0c4"></a>

**90° CCW: unverified** — `in_game_visible_travel-bb992f226a7b9273e0c4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-74a74bbd1cc42dd6dc41"></a>

**180° CCW: unverified** — `in_game_visible_travel-74a74bbd1cc42dd6dc41`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-a9072eee5aeedd23846d"></a>

**270° CCW: unverified** — `in_game_visible_travel-a9072eee5aeedd23846d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-9; entry: 1-N-in-15; exit: 1-W-out-9.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 252 cases; unverified: 252</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8439a09ee2b05204ed90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47111575c5bb3e1b5414">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a290bda9eda517c6615">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fc9bae610b881da5f65">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-733e4b92ce60624082bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e692f2c03cd7017f3471">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2fd471f2eccbe9c30a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d97cceadb2ecb397263">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3e4ef75062901491bde9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0455c16f3583539d1978">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ec1f2cfb2e075175717">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-954c7cd006416a29c57a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f8b7be838d167a318535">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fcd4ecd2585a16dada1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12ec5b151bd818e959e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4a6fee3d50e3d84dd63">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-96473888df6ea00e3304">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d26b5aeb220af9684aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dcd795656cb15eb3e43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8495db0dae736beee5c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1fb1df230f528f41ba67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce5b4c4a72307aa454f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c32ccce866bdf3870eeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1949b226b330c19ecd81">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d07c44f5b9433922a91a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ec0c53754f9da415d27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-911bac781d687ed7b98a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-536253cd3427a0333478">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7188da8e7ebec77820f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33e186705b0f9f81b48f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-991167ac09cd24938a94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-803a34cd8ffa9921ce8e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-efc4d4f1fff8660946b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2001a53726bb58b541e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-144d4b0b1bdaf23cd377">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27a67bda079ebfd8b13e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9ef6591d7a585f5684bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8c21cd6a9f33fbba0c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74430d84c96783b088b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55c1d5b97cd3b23b4423">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-379406e53e76bb5b6c50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-120d0ddfc2ea675039ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5600b2437cdb8ee9e345">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22011450bf0dbf34f21c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e557dff43b8a9ccfb4fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5c85789cd03cf99d06b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fe1fcf6462bc47da923">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebf281c732511c2b09b0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-80c4eb293a557559363b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74558bd8f80ec4d7fde3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c3cf25471313e40f4f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bc4931d4194550fffc7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b004aa75aee78527c3a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cee03886ff282325071">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-173d1683268996553e66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44207d6eaf21361058fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20b124d692df646c8262">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24bbb6ac11a102354f85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-965cf7a03b27bce2f6d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7b4f3cf123a2ba2c06a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8e00a9beccd832159d19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31f0f342a0f3ecb8b23d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63568b99be414d117610">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a10b76a547c2bfc9e0ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-350a65e6533292307cf5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fd716676db2c6f32f6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9856d5d1114a434fb126">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-537a732987d9a98b348c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e54713594651d52e033c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9efa9e030eb9d116813">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5934703253bc56870c59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-658d3fd57f5efc89451e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f2e217dc628a941fad97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0648b166f29fc581d5ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-169c134d2958411d3384">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab1acdbc9c7693228b9c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93921d686531aa57428d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a2182c5086dbdd181ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a0854bc3d62ee35d0a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2281b8e285067b89bda6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1cc33594c41fe00c37b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-105bd0d56586cfa45e63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68cb3962116e853b9199">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2fd31f48f2294a96a44">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-43e92b0e5a351a84d5a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d24c8c842ae008ad691">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71dde294cee257b14720">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adc5cc0b4f527f0c18d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3e511d78604e8c78f1e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cec37b5a28a130a43c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bde77578a91227e79ba3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40dbbaa61a15a5ce794d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-028786d117055e19f9d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-658f8842b00e028d5b14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a569d82aae7de640770">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e2e1dcf1bfa9b6338d1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4b713b1e2a1bc5d5df99">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-990c5c5b98c497025d1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1684d9688134e3fc3bf4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46a48511efccd0230aa4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2ea3167f87de717452c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1653961963535f892a7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e4f1b96842dd5ebfd0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6689ae5692246215f569">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f8ca31890c2f702e8e00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7716e6e8322291e7476d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dfabffac69cb3c99a61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-807e6683d0bbb88ceac4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a942953597e37f78d8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91f9d40c025971455364">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-669f7a2eb0b52de855b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c56884dd3698a296fdf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9561dffa7404b743f6bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aeca451cf1e499a022b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-849ee3d62554c984615a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a34c9481ea411f7103ff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2a526b73f098fb731c9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b32c46f37b76057dc654">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-452f3e7a4d944ee31aba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc23d7a7f811e228a77c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-484ec3f24ad3c03128ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16c8c149d8f81bec9be5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9561781437e8f25d926f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-432f66d4bfc73cfeee53">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5073ff66098c7bd8a67c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c20c95eb3b3f363ea10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4441438beb98b296804">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a20c7c7eec641640efc9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0202390c0fc153bb6c5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edda02b2d4c4e154207b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-caa678c7b29637f31712">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfffe5cc37618fb70de1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4305fbc6a9cc3e1169ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-349fabde90e139f8995f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2930682ebb7cda2db6f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e091a3922eaa972c649">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-750e2b3c9de00b5587c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c16d42dcba941b861513">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc897da972a136cc2e13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0ce02f1a438adffcaac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fbc28d090c736e3cf7b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b23fa1104fd117bf554">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16c4d5e2364aed4d1775">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-484c100ccbd3299c1cd6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-660862d91cc09d156f02">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed9add4ff7e3b8db6aed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fa7f8917f650c9cea38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-845c0eec49a17b5f9f82">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f2e56ce4cfaa2d92c51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a663894182c95e9d5d3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc790da732a00e0d2070">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77d88c3c87f9f0634fe0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-10; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9e5fa94f7d7d90d2a05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b3967d850e2010a545d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d50f9e82a024d9342d75">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdf10e419e0c836833a0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d361f46014a4a0915eca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0fd29476782edfd7ab5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04938e15bd6e20d9e847">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed13e3941c5cd8e6af5c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1de597cc92790e7bbc4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-285e353de4f77d1eb3d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c730de98cf12387e63e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-811478bc1202d1da3bdb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d22ca23ac465e4ec04ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b4f07a12440e0110ce6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f61ff407a97276a12bed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-140d34705794a3e35d4b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4cf544a50bce0930c36f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b40db6b311104394707">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc268248f0d9e0619b84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e92ca6ce5f09ecff1d5e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12d3b19075425465e5ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2663a72e00be8e5462b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3fd8e783af1f3096f44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62b1a73aa5e418c9acac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0fca6c2f326e8322d27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad0192874358e57836af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7edcf25d108ce4d6ffc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab80db7f316bdcd2c169">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-72cb7b0a90ecb0819219">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09898981e92570b783d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d399a9604da2ae1b4937">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2d5abac220818ff7482">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-12; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9f5c065b78f7f1ee049f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94b76dad531331943e1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2082d6a23e4cd42bb0b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-947f103efcfaf910de74">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e299c233a85a4df439b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b751d04e52ba3342cc0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf1be5b16a733f9c7417">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23c89a7b69d51582e1ae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e7c5cfe00bba82afb06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9bfb5f606f089c56983">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79e374cbb523f0b7d498">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbdaab5c835dc00adec2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93fa4ec28fffff4b8225">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f19f2009eabaa4e2baa4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fc26ea1b3ebb5f2fbea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1e4ba9093eeb4b8c447">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f57fb3dddab0f837e379">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56c11cbad2eae032e8b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6692075b568a0c5b88d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1387daffdf24873b6778">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-002ab2a026dc9a375f27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eba176a58211c1a5ad95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39767fb41fdfb333052c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17309ee1e16bede482b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-13; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7d8329ccd5cca8b30b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21d2a3fb1f4efd88d553">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19264f0e6134bc44311d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4a8ce49ae84e22b274d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-13; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a61a5c06dcebcd9fe9d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf901dc4e0c5176a9b4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23dbb1ba4f32bd8f33d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b2f1334fa323b82b09c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f201d10fd10e45c2ec98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-016ba85d52707eea7157">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82bf46afb68d98f9c14e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-782ea1a8d675b6f809b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-778b69ec0176df859115">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b7e99e495cfe48f13cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ac55bb1656fb634fa9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dcb4fc37e5fc408f21ed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c024b6d719d608bf5d47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5f83fb9fa831625c896">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bc366d19823ed16abc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c009847ce17b5f9f3fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-60bb707eec4bc7e2ac21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee11562fc98f4d659b85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29deb65ee92b099a2cea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c9e502e508092bbf896">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b49a185ce64a975d12c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-983af45288974153ca6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7d404a7aaed18b03b34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5270934c9c532e6383ee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ffb0924abe5da542bd44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3778c65429e3e367d8ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78a59dce631e01ea9e86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5f62f1d7a101e8538ad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a88545c3c8e4b794d918">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7b7f2e7ecfe5a67e7a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a8f98f8ed915b5b7926">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10ad872a50a664279e6d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4694464b98b0cec5e5c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6541ba195930e8368a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bb821b99629ab890250">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c25d19c6726bf0fb9d3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1ac9c19eb66a6da50b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ced7f19b119b37f3812">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00f3bf1c3fca8e285662">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8443437f47c685ef570e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8439a09ee2b05204ed90"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8439a09ee2b05204ed90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47111575c5bb3e1b5414"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47111575c5bb3e1b5414`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a290bda9eda517c6615"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6a290bda9eda517c6615`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fc9bae610b881da5f65"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9fc9bae610b881da5f65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-733e4b92ce60624082bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-733e4b92ce60624082bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e692f2c03cd7017f3471"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e692f2c03cd7017f3471`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2fd471f2eccbe9c30a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e2fd471f2eccbe9c30a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d97cceadb2ecb397263"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d97cceadb2ecb397263`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3e4ef75062901491bde9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e4ef75062901491bde9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0455c16f3583539d1978"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0455c16f3583539d1978`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ec1f2cfb2e075175717"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2ec1f2cfb2e075175717`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-954c7cd006416a29c57a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-954c7cd006416a29c57a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f8b7be838d167a318535"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f8b7be838d167a318535`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fcd4ecd2585a16dada1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1fcd4ecd2585a16dada1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12ec5b151bd818e959e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-12ec5b151bd818e959e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4a6fee3d50e3d84dd63"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4a6fee3d50e3d84dd63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-96473888df6ea00e3304"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-96473888df6ea00e3304`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d26b5aeb220af9684aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d26b5aeb220af9684aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dcd795656cb15eb3e43"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9dcd795656cb15eb3e43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8495db0dae736beee5c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b8495db0dae736beee5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1fb1df230f528f41ba67"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1fb1df230f528f41ba67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce5b4c4a72307aa454f3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce5b4c4a72307aa454f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c32ccce866bdf3870eeb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c32ccce866bdf3870eeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1949b226b330c19ecd81"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1949b226b330c19ecd81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d07c44f5b9433922a91a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d07c44f5b9433922a91a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ec0c53754f9da415d27"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1ec0c53754f9da415d27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-911bac781d687ed7b98a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-911bac781d687ed7b98a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-536253cd3427a0333478"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-536253cd3427a0333478`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7188da8e7ebec77820f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7188da8e7ebec77820f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33e186705b0f9f81b48f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-33e186705b0f9f81b48f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-991167ac09cd24938a94"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-991167ac09cd24938a94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-803a34cd8ffa9921ce8e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-803a34cd8ffa9921ce8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-efc4d4f1fff8660946b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-efc4d4f1fff8660946b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2001a53726bb58b541e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2001a53726bb58b541e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-144d4b0b1bdaf23cd377"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-144d4b0b1bdaf23cd377`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27a67bda079ebfd8b13e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27a67bda079ebfd8b13e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9ef6591d7a585f5684bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9ef6591d7a585f5684bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8c21cd6a9f33fbba0c7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d8c21cd6a9f33fbba0c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74430d84c96783b088b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74430d84c96783b088b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55c1d5b97cd3b23b4423"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55c1d5b97cd3b23b4423`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-379406e53e76bb5b6c50"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-379406e53e76bb5b6c50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-120d0ddfc2ea675039ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-120d0ddfc2ea675039ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5600b2437cdb8ee9e345"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5600b2437cdb8ee9e345`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22011450bf0dbf34f21c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22011450bf0dbf34f21c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e557dff43b8a9ccfb4fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e557dff43b8a9ccfb4fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5c85789cd03cf99d06b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a5c85789cd03cf99d06b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fe1fcf6462bc47da923"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8fe1fcf6462bc47da923`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebf281c732511c2b09b0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ebf281c732511c2b09b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-80c4eb293a557559363b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-80c4eb293a557559363b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74558bd8f80ec4d7fde3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74558bd8f80ec4d7fde3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c3cf25471313e40f4f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7c3cf25471313e40f4f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bc4931d4194550fffc7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0bc4931d4194550fffc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b004aa75aee78527c3a7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b004aa75aee78527c3a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cee03886ff282325071"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7cee03886ff282325071`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-173d1683268996553e66"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-173d1683268996553e66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44207d6eaf21361058fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-44207d6eaf21361058fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20b124d692df646c8262"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20b124d692df646c8262`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24bbb6ac11a102354f85"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24bbb6ac11a102354f85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-965cf7a03b27bce2f6d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-965cf7a03b27bce2f6d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7b4f3cf123a2ba2c06a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b7b4f3cf123a2ba2c06a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8e00a9beccd832159d19"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8e00a9beccd832159d19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31f0f342a0f3ecb8b23d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-31f0f342a0f3ecb8b23d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63568b99be414d117610"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63568b99be414d117610`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a10b76a547c2bfc9e0ce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a10b76a547c2bfc9e0ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-350a65e6533292307cf5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-350a65e6533292307cf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fd716676db2c6f32f6a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5fd716676db2c6f32f6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9856d5d1114a434fb126"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9856d5d1114a434fb126`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-537a732987d9a98b348c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-537a732987d9a98b348c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e54713594651d52e033c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e54713594651d52e033c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9efa9e030eb9d116813"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9efa9e030eb9d116813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5934703253bc56870c59"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5934703253bc56870c59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-658d3fd57f5efc89451e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-658d3fd57f5efc89451e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f2e217dc628a941fad97"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2e217dc628a941fad97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0648b166f29fc581d5ab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0648b166f29fc581d5ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-169c134d2958411d3384"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-169c134d2958411d3384`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab1acdbc9c7693228b9c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab1acdbc9c7693228b9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93921d686531aa57428d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93921d686531aa57428d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a2182c5086dbdd181ca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a2182c5086dbdd181ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a0854bc3d62ee35d0a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a0854bc3d62ee35d0a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2281b8e285067b89bda6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2281b8e285067b89bda6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1cc33594c41fe00c37b9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1cc33594c41fe00c37b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-105bd0d56586cfa45e63"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-105bd0d56586cfa45e63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68cb3962116e853b9199"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-68cb3962116e853b9199`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2fd31f48f2294a96a44"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a2fd31f48f2294a96a44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-43e92b0e5a351a84d5a6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-43e92b0e5a351a84d5a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d24c8c842ae008ad691"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d24c8c842ae008ad691`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71dde294cee257b14720"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-71dde294cee257b14720`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adc5cc0b4f527f0c18d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-adc5cc0b4f527f0c18d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3e511d78604e8c78f1e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e511d78604e8c78f1e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cec37b5a28a130a43c0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5cec37b5a28a130a43c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bde77578a91227e79ba3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bde77578a91227e79ba3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40dbbaa61a15a5ce794d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40dbbaa61a15a5ce794d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-028786d117055e19f9d2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-028786d117055e19f9d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-658f8842b00e028d5b14"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-658f8842b00e028d5b14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a569d82aae7de640770"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a569d82aae7de640770`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e2e1dcf1bfa9b6338d1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5e2e1dcf1bfa9b6338d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4b713b1e2a1bc5d5df99"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4b713b1e2a1bc5d5df99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-990c5c5b98c497025d1c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-990c5c5b98c497025d1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1684d9688134e3fc3bf4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1684d9688134e3fc3bf4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46a48511efccd0230aa4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-46a48511efccd0230aa4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2ea3167f87de717452c6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2ea3167f87de717452c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1653961963535f892a7b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1653961963535f892a7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e4f1b96842dd5ebfd0e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e4f1b96842dd5ebfd0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6689ae5692246215f569"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6689ae5692246215f569`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f8ca31890c2f702e8e00"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f8ca31890c2f702e8e00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7716e6e8322291e7476d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7716e6e8322291e7476d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dfabffac69cb3c99a61"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1dfabffac69cb3c99a61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-807e6683d0bbb88ceac4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-807e6683d0bbb88ceac4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a942953597e37f78d8c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a942953597e37f78d8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91f9d40c025971455364"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-91f9d40c025971455364`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-669f7a2eb0b52de855b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-669f7a2eb0b52de855b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c56884dd3698a296fdf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c56884dd3698a296fdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9561dffa7404b743f6bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9561dffa7404b743f6bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aeca451cf1e499a022b5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aeca451cf1e499a022b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-849ee3d62554c984615a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-849ee3d62554c984615a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a34c9481ea411f7103ff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a34c9481ea411f7103ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2a526b73f098fb731c9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2a526b73f098fb731c9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b32c46f37b76057dc654"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b32c46f37b76057dc654`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-452f3e7a4d944ee31aba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-452f3e7a4d944ee31aba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc23d7a7f811e228a77c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc23d7a7f811e228a77c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-484ec3f24ad3c03128ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-484ec3f24ad3c03128ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16c8c149d8f81bec9be5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-16c8c149d8f81bec9be5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9561781437e8f25d926f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9561781437e8f25d926f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-432f66d4bfc73cfeee53"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-432f66d4bfc73cfeee53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5073ff66098c7bd8a67c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5073ff66098c7bd8a67c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c20c95eb3b3f363ea10"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1c20c95eb3b3f363ea10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4441438beb98b296804"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b4441438beb98b296804`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a20c7c7eec641640efc9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a20c7c7eec641640efc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0202390c0fc153bb6c5d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0202390c0fc153bb6c5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edda02b2d4c4e154207b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-edda02b2d4c4e154207b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-caa678c7b29637f31712"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-caa678c7b29637f31712`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfffe5cc37618fb70de1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cfffe5cc37618fb70de1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4305fbc6a9cc3e1169ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4305fbc6a9cc3e1169ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-349fabde90e139f8995f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-349fabde90e139f8995f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2930682ebb7cda2db6f6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2930682ebb7cda2db6f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e091a3922eaa972c649"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2e091a3922eaa972c649`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-750e2b3c9de00b5587c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-750e2b3c9de00b5587c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c16d42dcba941b861513"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c16d42dcba941b861513`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc897da972a136cc2e13"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc897da972a136cc2e13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0ce02f1a438adffcaac"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0ce02f1a438adffcaac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fbc28d090c736e3cf7b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fbc28d090c736e3cf7b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b23fa1104fd117bf554"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b23fa1104fd117bf554`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16c4d5e2364aed4d1775"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-16c4d5e2364aed4d1775`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-484c100ccbd3299c1cd6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-484c100ccbd3299c1cd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-660862d91cc09d156f02"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-660862d91cc09d156f02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed9add4ff7e3b8db6aed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ed9add4ff7e3b8db6aed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fa7f8917f650c9cea38"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3fa7f8917f650c9cea38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-845c0eec49a17b5f9f82"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-845c0eec49a17b5f9f82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7f2e56ce4cfaa2d92c51"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f2e56ce4cfaa2d92c51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a663894182c95e9d5d3e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a663894182c95e9d5d3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc790da732a00e0d2070"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc790da732a00e0d2070`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77d88c3c87f9f0634fe0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77d88c3c87f9f0634fe0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-10; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9e5fa94f7d7d90d2a05"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9e5fa94f7d7d90d2a05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b3967d850e2010a545d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b3967d850e2010a545d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d50f9e82a024d9342d75"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d50f9e82a024d9342d75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdf10e419e0c836833a0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bdf10e419e0c836833a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-10; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d361f46014a4a0915eca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d361f46014a4a0915eca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0fd29476782edfd7ab5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0fd29476782edfd7ab5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04938e15bd6e20d9e847"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-04938e15bd6e20d9e847`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed13e3941c5cd8e6af5c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed13e3941c5cd8e6af5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1de597cc92790e7bbc4b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1de597cc92790e7bbc4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-285e353de4f77d1eb3d8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-285e353de4f77d1eb3d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c730de98cf12387e63e6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c730de98cf12387e63e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-811478bc1202d1da3bdb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-811478bc1202d1da3bdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d22ca23ac465e4ec04ab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d22ca23ac465e4ec04ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b4f07a12440e0110ce6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b4f07a12440e0110ce6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f61ff407a97276a12bed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f61ff407a97276a12bed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-140d34705794a3e35d4b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-140d34705794a3e35d4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4cf544a50bce0930c36f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4cf544a50bce0930c36f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b40db6b311104394707"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b40db6b311104394707`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc268248f0d9e0619b84"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dc268248f0d9e0619b84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e92ca6ce5f09ecff1d5e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e92ca6ce5f09ecff1d5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12d3b19075425465e5ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12d3b19075425465e5ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2663a72e00be8e5462b6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2663a72e00be8e5462b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3fd8e783af1f3096f44"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b3fd8e783af1f3096f44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62b1a73aa5e418c9acac"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-62b1a73aa5e418c9acac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0fca6c2f326e8322d27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0fca6c2f326e8322d27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad0192874358e57836af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ad0192874358e57836af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7edcf25d108ce4d6ffc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d7edcf25d108ce4d6ffc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab80db7f316bdcd2c169"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab80db7f316bdcd2c169`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-72cb7b0a90ecb0819219"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-72cb7b0a90ecb0819219`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09898981e92570b783d7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-09898981e92570b783d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d399a9604da2ae1b4937"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d399a9604da2ae1b4937`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2d5abac220818ff7482"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f2d5abac220818ff7482`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-12; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9f5c065b78f7f1ee049f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f5c065b78f7f1ee049f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94b76dad531331943e1d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94b76dad531331943e1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2082d6a23e4cd42bb0b3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2082d6a23e4cd42bb0b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-947f103efcfaf910de74"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-947f103efcfaf910de74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-12; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e299c233a85a4df439b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e299c233a85a4df439b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b751d04e52ba3342cc0b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b751d04e52ba3342cc0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf1be5b16a733f9c7417"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bf1be5b16a733f9c7417`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23c89a7b69d51582e1ae"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-23c89a7b69d51582e1ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e7c5cfe00bba82afb06"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e7c5cfe00bba82afb06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9bfb5f606f089c56983"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9bfb5f606f089c56983`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79e374cbb523f0b7d498"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-79e374cbb523f0b7d498`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbdaab5c835dc00adec2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fbdaab5c835dc00adec2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93fa4ec28fffff4b8225"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93fa4ec28fffff4b8225`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f19f2009eabaa4e2baa4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f19f2009eabaa4e2baa4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fc26ea1b3ebb5f2fbea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1fc26ea1b3ebb5f2fbea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1e4ba9093eeb4b8c447"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f1e4ba9093eeb4b8c447`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f57fb3dddab0f837e379"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f57fb3dddab0f837e379`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56c11cbad2eae032e8b8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-56c11cbad2eae032e8b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6692075b568a0c5b88d3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6692075b568a0c5b88d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1387daffdf24873b6778"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1387daffdf24873b6778`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-002ab2a026dc9a375f27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-002ab2a026dc9a375f27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eba176a58211c1a5ad95"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eba176a58211c1a5ad95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39767fb41fdfb333052c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-39767fb41fdfb333052c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17309ee1e16bede482b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-17309ee1e16bede482b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-13; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7d8329ccd5cca8b30b6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7d8329ccd5cca8b30b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21d2a3fb1f4efd88d553"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-21d2a3fb1f4efd88d553`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19264f0e6134bc44311d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-19264f0e6134bc44311d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4a8ce49ae84e22b274d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c4a8ce49ae84e22b274d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-13; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a61a5c06dcebcd9fe9d0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a61a5c06dcebcd9fe9d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf901dc4e0c5176a9b4b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bf901dc4e0c5176a9b4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23dbb1ba4f32bd8f33d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-23dbb1ba4f32bd8f33d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b2f1334fa323b82b09c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b2f1334fa323b82b09c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f201d10fd10e45c2ec98"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f201d10fd10e45c2ec98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-016ba85d52707eea7157"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-016ba85d52707eea7157`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82bf46afb68d98f9c14e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-82bf46afb68d98f9c14e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-782ea1a8d675b6f809b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-782ea1a8d675b6f809b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-13; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-778b69ec0176df859115"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-778b69ec0176df859115`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b7e99e495cfe48f13cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9b7e99e495cfe48f13cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ac55bb1656fb634fa9b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ac55bb1656fb634fa9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dcb4fc37e5fc408f21ed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dcb4fc37e5fc408f21ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c024b6d719d608bf5d47"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c024b6d719d608bf5d47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5f83fb9fa831625c896"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e5f83fb9fa831625c896`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bc366d19823ed16abc7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9bc366d19823ed16abc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c009847ce17b5f9f3fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9c009847ce17b5f9f3fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-60bb707eec4bc7e2ac21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60bb707eec4bc7e2ac21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee11562fc98f4d659b85"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ee11562fc98f4d659b85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29deb65ee92b099a2cea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-29deb65ee92b099a2cea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c9e502e508092bbf896"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5c9e502e508092bbf896`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b49a185ce64a975d12c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b49a185ce64a975d12c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-983af45288974153ca6d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-983af45288974153ca6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7d404a7aaed18b03b34"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f7d404a7aaed18b03b34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5270934c9c532e6383ee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5270934c9c532e6383ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ffb0924abe5da542bd44"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ffb0924abe5da542bd44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3778c65429e3e367d8ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3778c65429e3e367d8ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78a59dce631e01ea9e86"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78a59dce631e01ea9e86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5f62f1d7a101e8538ad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c5f62f1d7a101e8538ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a88545c3c8e4b794d918"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a88545c3c8e4b794d918`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7b7f2e7ecfe5a67e7a8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a7b7f2e7ecfe5a67e7a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a8f98f8ed915b5b7926"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1a8f98f8ed915b5b7926`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10ad872a50a664279e6d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10ad872a50a664279e6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4694464b98b0cec5e5c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4694464b98b0cec5e5c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6541ba195930e8368a7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c6541ba195930e8368a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bb821b99629ab890250"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0bb821b99629ab890250`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c25d19c6726bf0fb9d3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c25d19c6726bf0fb9d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d1ac9c19eb66a6da50b8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1ac9c19eb66a6da50b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ced7f19b119b37f3812"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8ced7f19b119b37f3812`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00f3bf1c3fca8e285662"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-00f3bf1c3fca8e285662`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8443437f47c685ef570e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8443437f47c685ef570e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
