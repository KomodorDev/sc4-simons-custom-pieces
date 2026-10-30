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

Merges the upper on-ramp into an outer upper-deck lane. The final ramp section stays level above the lower deck. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-2` | road / 1 / primary | in | [-8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-3` | road / 1 / primary | out | [-8.0, -12.8, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-4` | road / 1 / primary | in | [-8.0, -12.8, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-N-in-5` | road / 1 / primary | in | [-3.2, -8.0, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-6` | road / 1 / primary | out | [-3.2, -8.0, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-S-in-7` | road / 1 / primary | in | [2.91305, -24.0, 14.952648]; [0.27715266728515847, 0.960825894226796]; 0.135128522 | `path-interface-c48dc5c1853ef9588fa8` |
| `1-N-in-8` | road / 1 / primary | in | [3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-9` | road / 1 / primary | out | [3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-W-out-10` | road / 1 / primary | out | [8.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-11` | road / 1 / primary | in | [8.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-12` | road / 1 / primary | out | [8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-13` | road / 1 / primary | in | [8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-N-in-14` | road / 1 / primary | in | [12.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-15` | road / 1 / primary | out | [12.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-16` | road / 1 / primary | in | [19.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-17` | road / 1 / primary | out | [19.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-2` → `1-N-out-9` | primary |
| road | `1-W-in-4` → `1-N-out-6` | primary |
| road | `1-N-in-5` → `1-W-out-3` | primary |
| road | `1-S-in-7` → `1-N-out-17` | primary |
| road | `1-N-in-8` → `1-W-out-1` | primary |
| road | `1-W-in-11` → `1-N-out-17` | primary |
| road | `1-W-in-13` → `1-N-out-15` | primary |
| road | `1-N-in-14` → `1-W-out-12` | primary |
| road | `1-N-in-16` → `1-W-out-10` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-2` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-7` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-7` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-7` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-7` | road / `1-N-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-7` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-7` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-7` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-N-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-11` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-11` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-11` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-11` | road / `1-N-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-11` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-11` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-11` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-13` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-13` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-13` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-13` | road / `1-N-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-13` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-13` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-13` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-N-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-N-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-16` | road / `1-N-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-upper-entry-branch --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The current assembly’s executed checks and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

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
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9 | — | <a href="#case-in_game_route_query-4d9377e9dbfc89ec2d23">[ ] unverified</a> | <a href="#case-in_game_route_query-565a3dd667ece62fa189">[ ] unverified</a> | <a href="#case-in_game_route_query-ecb6933129ed4b043f6b">[ ] unverified</a> | <a href="#case-in_game_route_query-0451f016d6c30db2f000">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6 | — | <a href="#case-in_game_route_query-07b604fd15d6ff2af07a">[ ] unverified</a> | <a href="#case-in_game_route_query-561bd86a0a8b57e94af5">[ ] unverified</a> | <a href="#case-in_game_route_query-513f4ed0f136b8d22b7e">[ ] unverified</a> | <a href="#case-in_game_route_query-32a2a3a989c16ae559d1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-532a7dc7b158b92dbe73">[ ] unverified</a> | <a href="#case-in_game_route_query-2491d06cc67ff0f4dd3b">[ ] unverified</a> | <a href="#case-in_game_route_query-b41b839755f9012d0dc8">[ ] unverified</a> | <a href="#case-in_game_route_query-4a16f3069df82fc9e180">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17 | — | <a href="#case-in_game_route_query-5c5b716945ec3e54d850">[ ] unverified</a> | <a href="#case-in_game_route_query-227f65d560f8fb2a6774">[ ] unverified</a> | <a href="#case-in_game_route_query-679f5ed69a11207b12cd">[ ] unverified</a> | <a href="#case-in_game_route_query-7d0f20062359f028482f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-9c736d0ac2a277005c50">[ ] unverified</a> | <a href="#case-in_game_route_query-cc22e46d2c536b242101">[ ] unverified</a> | <a href="#case-in_game_route_query-8f2f753274b2ca026f16">[ ] unverified</a> | <a href="#case-in_game_route_query-f4f2dd27bf7aaedbaca1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17 | — | <a href="#case-in_game_route_query-9c7b1963c9bde43cea9a">[ ] unverified</a> | <a href="#case-in_game_route_query-bac74e56f0150124e342">[ ] unverified</a> | <a href="#case-in_game_route_query-0d67c0406a25e8c5fdbb">[ ] unverified</a> | <a href="#case-in_game_route_query-9a827cfe87fc52d9ed3b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15 | — | <a href="#case-in_game_route_query-aa3eb582416d00ebfe79">[ ] unverified</a> | <a href="#case-in_game_route_query-3a0b252c7eb0859c6f94">[ ] unverified</a> | <a href="#case-in_game_route_query-8a515149e9bc3c7af950">[ ] unverified</a> | <a href="#case-in_game_route_query-536a84b01ca0cf7bed83">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12 | — | <a href="#case-in_game_route_query-a0bd7f483b16f08e2672">[ ] unverified</a> | <a href="#case-in_game_route_query-c90e0105c7f72b3f073f">[ ] unverified</a> | <a href="#case-in_game_route_query-490c3e2563d5b746d610">[ ] unverified</a> | <a href="#case-in_game_route_query-0fc1aebe164c2a337cf2">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10 | — | <a href="#case-in_game_route_query-cd7eb1a74a0e1a8f5bb7">[ ] unverified</a> | <a href="#case-in_game_route_query-e26791cd612c2ef6a8e1">[ ] unverified</a> | <a href="#case-in_game_route_query-83f1ca71839b447e1a55">[ ] unverified</a> | <a href="#case-in_game_route_query-f7603a7b28019cf79734">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9</summary>

<a id="case-in_game_route_query-4d9377e9dbfc89ec2d23"></a>

**0° CCW: unverified** — `in_game_route_query-4d9377e9dbfc89ec2d23`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9.

No observation recorded.

<a id="case-in_game_route_query-565a3dd667ece62fa189"></a>

**90° CCW: unverified** — `in_game_route_query-565a3dd667ece62fa189`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9.

No observation recorded.

<a id="case-in_game_route_query-ecb6933129ed4b043f6b"></a>

**180° CCW: unverified** — `in_game_route_query-ecb6933129ed4b043f6b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9.

No observation recorded.

<a id="case-in_game_route_query-0451f016d6c30db2f000"></a>

**270° CCW: unverified** — `in_game_route_query-0451f016d6c30db2f000`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9.

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
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17</summary>

<a id="case-in_game_route_query-5c5b716945ec3e54d850"></a>

**0° CCW: unverified** — `in_game_route_query-5c5b716945ec3e54d850`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-227f65d560f8fb2a6774"></a>

**90° CCW: unverified** — `in_game_route_query-227f65d560f8fb2a6774`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-679f5ed69a11207b12cd"></a>

**180° CCW: unverified** — `in_game_route_query-679f5ed69a11207b12cd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-7d0f20062359f028482f"></a>

**270° CCW: unverified** — `in_game_route_query-7d0f20062359f028482f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-9c736d0ac2a277005c50"></a>

**0° CCW: unverified** — `in_game_route_query-9c736d0ac2a277005c50`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-cc22e46d2c536b242101"></a>

**90° CCW: unverified** — `in_game_route_query-cc22e46d2c536b242101`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-8f2f753274b2ca026f16"></a>

**180° CCW: unverified** — `in_game_route_query-8f2f753274b2ca026f16`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-f4f2dd27bf7aaedbaca1"></a>

**270° CCW: unverified** — `in_game_route_query-f4f2dd27bf7aaedbaca1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17</summary>

<a id="case-in_game_route_query-9c7b1963c9bde43cea9a"></a>

**0° CCW: unverified** — `in_game_route_query-9c7b1963c9bde43cea9a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-bac74e56f0150124e342"></a>

**90° CCW: unverified** — `in_game_route_query-bac74e56f0150124e342`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-0d67c0406a25e8c5fdbb"></a>

**180° CCW: unverified** — `in_game_route_query-0d67c0406a25e8c5fdbb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_route_query-9a827cfe87fc52d9ed3b"></a>

**270° CCW: unverified** — `in_game_route_query-9a827cfe87fc52d9ed3b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15</summary>

<a id="case-in_game_route_query-aa3eb582416d00ebfe79"></a>

**0° CCW: unverified** — `in_game_route_query-aa3eb582416d00ebfe79`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_route_query-3a0b252c7eb0859c6f94"></a>

**90° CCW: unverified** — `in_game_route_query-3a0b252c7eb0859c6f94`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_route_query-8a515149e9bc3c7af950"></a>

**180° CCW: unverified** — `in_game_route_query-8a515149e9bc3c7af950`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_route_query-536a84b01ca0cf7bed83"></a>

**270° CCW: unverified** — `in_game_route_query-536a84b01ca0cf7bed83`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12</summary>

<a id="case-in_game_route_query-a0bd7f483b16f08e2672"></a>

**0° CCW: unverified** — `in_game_route_query-a0bd7f483b16f08e2672`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-c90e0105c7f72b3f073f"></a>

**90° CCW: unverified** — `in_game_route_query-c90e0105c7f72b3f073f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-490c3e2563d5b746d610"></a>

**180° CCW: unverified** — `in_game_route_query-490c3e2563d5b746d610`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-0fc1aebe164c2a337cf2"></a>

**270° CCW: unverified** — `in_game_route_query-0fc1aebe164c2a337cf2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10</summary>

<a id="case-in_game_route_query-cd7eb1a74a0e1a8f5bb7"></a>

**0° CCW: unverified** — `in_game_route_query-cd7eb1a74a0e1a8f5bb7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-e26791cd612c2ef6a8e1"></a>

**90° CCW: unverified** — `in_game_route_query-e26791cd612c2ef6a8e1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-83f1ca71839b447e1a55"></a>

**180° CCW: unverified** — `in_game_route_query-83f1ca71839b447e1a55`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-f7603a7b28019cf79734"></a>

**270° CCW: unverified** — `in_game_route_query-f7603a7b28019cf79734`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 36 cases; unverified: 36</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9 | — | <a href="#case-in_game_visible_travel-4d9377e9dbfc89ec2d23">[ ] unverified</a> | <a href="#case-in_game_visible_travel-565a3dd667ece62fa189">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ecb6933129ed4b043f6b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0451f016d6c30db2f000">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6 | — | <a href="#case-in_game_visible_travel-07b604fd15d6ff2af07a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-561bd86a0a8b57e94af5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-513f4ed0f136b8d22b7e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-32a2a3a989c16ae559d1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-532a7dc7b158b92dbe73">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2491d06cc67ff0f4dd3b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b41b839755f9012d0dc8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4a16f3069df82fc9e180">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17 | — | <a href="#case-in_game_visible_travel-5c5b716945ec3e54d850">[ ] unverified</a> | <a href="#case-in_game_visible_travel-227f65d560f8fb2a6774">[ ] unverified</a> | <a href="#case-in_game_visible_travel-679f5ed69a11207b12cd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7d0f20062359f028482f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-9c736d0ac2a277005c50">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cc22e46d2c536b242101">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8f2f753274b2ca026f16">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f4f2dd27bf7aaedbaca1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17 | — | <a href="#case-in_game_visible_travel-9c7b1963c9bde43cea9a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bac74e56f0150124e342">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0d67c0406a25e8c5fdbb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9a827cfe87fc52d9ed3b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15 | — | <a href="#case-in_game_visible_travel-aa3eb582416d00ebfe79">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3a0b252c7eb0859c6f94">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8a515149e9bc3c7af950">[ ] unverified</a> | <a href="#case-in_game_visible_travel-536a84b01ca0cf7bed83">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12 | — | <a href="#case-in_game_visible_travel-a0bd7f483b16f08e2672">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c90e0105c7f72b3f073f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-490c3e2563d5b746d610">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0fc1aebe164c2a337cf2">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10 | — | <a href="#case-in_game_visible_travel-cd7eb1a74a0e1a8f5bb7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e26791cd612c2ef6a8e1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-83f1ca71839b447e1a55">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f7603a7b28019cf79734">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9</summary>

<a id="case-in_game_visible_travel-4d9377e9dbfc89ec2d23"></a>

**0° CCW: unverified** — `in_game_visible_travel-4d9377e9dbfc89ec2d23`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-565a3dd667ece62fa189"></a>

**90° CCW: unverified** — `in_game_visible_travel-565a3dd667ece62fa189`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-ecb6933129ed4b043f6b"></a>

**180° CCW: unverified** — `in_game_visible_travel-ecb6933129ed4b043f6b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-0451f016d6c30db2f000"></a>

**270° CCW: unverified** — `in_game_visible_travel-0451f016d6c30db2f000`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-9; entry: 1-W-in-2; exit: 1-N-out-9.

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
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17</summary>

<a id="case-in_game_visible_travel-5c5b716945ec3e54d850"></a>

**0° CCW: unverified** — `in_game_visible_travel-5c5b716945ec3e54d850`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-227f65d560f8fb2a6774"></a>

**90° CCW: unverified** — `in_game_visible_travel-227f65d560f8fb2a6774`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-679f5ed69a11207b12cd"></a>

**180° CCW: unverified** — `in_game_visible_travel-679f5ed69a11207b12cd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-7d0f20062359f028482f"></a>

**270° CCW: unverified** — `in_game_visible_travel-7d0f20062359f028482f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-7>1-N-out-17; entry: 1-S-in-7; exit: 1-N-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-9c736d0ac2a277005c50"></a>

**0° CCW: unverified** — `in_game_visible_travel-9c736d0ac2a277005c50`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-cc22e46d2c536b242101"></a>

**90° CCW: unverified** — `in_game_visible_travel-cc22e46d2c536b242101`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-8f2f753274b2ca026f16"></a>

**180° CCW: unverified** — `in_game_visible_travel-8f2f753274b2ca026f16`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-f4f2dd27bf7aaedbaca1"></a>

**270° CCW: unverified** — `in_game_visible_travel-f4f2dd27bf7aaedbaca1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-1; entry: 1-N-in-8; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17</summary>

<a id="case-in_game_visible_travel-9c7b1963c9bde43cea9a"></a>

**0° CCW: unverified** — `in_game_visible_travel-9c7b1963c9bde43cea9a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-bac74e56f0150124e342"></a>

**90° CCW: unverified** — `in_game_visible_travel-bac74e56f0150124e342`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-0d67c0406a25e8c5fdbb"></a>

**180° CCW: unverified** — `in_game_visible_travel-0d67c0406a25e8c5fdbb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-9a827cfe87fc52d9ed3b"></a>

**270° CCW: unverified** — `in_game_visible_travel-9a827cfe87fc52d9ed3b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-11>1-N-out-17; entry: 1-W-in-11; exit: 1-N-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15</summary>

<a id="case-in_game_visible_travel-aa3eb582416d00ebfe79"></a>

**0° CCW: unverified** — `in_game_visible_travel-aa3eb582416d00ebfe79`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-3a0b252c7eb0859c6f94"></a>

**90° CCW: unverified** — `in_game_visible_travel-3a0b252c7eb0859c6f94`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-8a515149e9bc3c7af950"></a>

**180° CCW: unverified** — `in_game_visible_travel-8a515149e9bc3c7af950`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-536a84b01ca0cf7bed83"></a>

**270° CCW: unverified** — `in_game_visible_travel-536a84b01ca0cf7bed83`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-13>1-N-out-15; entry: 1-W-in-13; exit: 1-N-out-15.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12</summary>

<a id="case-in_game_visible_travel-a0bd7f483b16f08e2672"></a>

**0° CCW: unverified** — `in_game_visible_travel-a0bd7f483b16f08e2672`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-c90e0105c7f72b3f073f"></a>

**90° CCW: unverified** — `in_game_visible_travel-c90e0105c7f72b3f073f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-490c3e2563d5b746d610"></a>

**180° CCW: unverified** — `in_game_visible_travel-490c3e2563d5b746d610`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-0fc1aebe164c2a337cf2"></a>

**270° CCW: unverified** — `in_game_visible_travel-0fc1aebe164c2a337cf2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-12; entry: 1-N-in-14; exit: 1-W-out-12.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10</summary>

<a id="case-in_game_visible_travel-cd7eb1a74a0e1a8f5bb7"></a>

**0° CCW: unverified** — `in_game_visible_travel-cd7eb1a74a0e1a8f5bb7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-e26791cd612c2ef6a8e1"></a>

**90° CCW: unverified** — `in_game_visible_travel-e26791cd612c2ef6a8e1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-83f1ca71839b447e1a55"></a>

**180° CCW: unverified** — `in_game_visible_travel-83f1ca71839b447e1a55`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-f7603a7b28019cf79734"></a>

**270° CCW: unverified** — `in_game_visible_travel-f7603a7b28019cf79734`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-16>1-W-out-10; entry: 1-N-in-16; exit: 1-W-out-10.

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
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e0360c4cbb961e1cc9bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87255646e6578d7e2a68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffcd493be7462828d1f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f99169b50944dcbe0a1f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0d76b36733f058284fa4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c4d933f40b5c0e851af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91ffdc0f365a77a1c56b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-569ae6639a306132a9d4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ee4bd7183779ec5853c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0efd12bf0928779324cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a54f20cf6fbbd058cdc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-505d9448aa826c0b06af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aff639267f9f7fcd293d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7f028c64cca1c93d5d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e58fbf384c92ce9e925">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3a49acb88a20de193f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ebb55c4cb8b0aeca591">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f89d64a11397ce09e59b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d785a49f8969ca4362bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-471a71cc6796e610e0e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b20bdacd6ae5f60e5abf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe926284a16a9b2b639d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7a6b4c6d152a48aca45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89bfe1e6d6c5585a92b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fa24cd8320ddb01f1ce9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e19df3a1637ab7908b8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27cc138798a63feffca2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d4343f990d0743a28e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23a9150db63fe995aff0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41fbb2319c17a5912c96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94c54ebad68210e1e925">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a925ef9768102efe3155">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f45ceb3104a13fdef4a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d4e8c9c8249c3b11500">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e17383a91c2e7d00dd57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69de29599b134b0cac82">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ebba66d21f65e164e163">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98e70801d4e2adadfdeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb3e874f1ec2430d51af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ecb2d039dffafd08ee1a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-22b2b91b8c865bba3dfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fec4c7698b430c00395c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e75ecd7067fea8f334d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40f6cc64a80cbb46a558">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-92b0a12950dd954e6d7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f5807583eb516140abc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c19112a689de3cdb8c2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-141e937c5629a80f7ce2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-850f572991d629717868">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa9b6d3281d9c1ada1ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-881911e6523b26bea3ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c0b6ca32e47a4f0c156">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73182dc2d1e94ecfe0e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c569b5b3fec8be83745">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16e06469817a850812a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d08147b97f65744c4bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-77a7f6d83d51d97b3aa8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa346f6c0a3c62737474">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-557a818f9afe17a005a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d3bdb4c0c7aa68221c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-16d7401a2341132e68f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3729a6d0d8a0a8a6e34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-996eb22228ad1e5612c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c9debfab37084ec2d69">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a612be1ffbdef55037a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84a59456cefdcc36f2eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e018c89ef34d97ff65e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd7e9e0db1516803e740">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-250e27f1320e9179581f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7ccba8c19280cb8f3b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0d8c470da1d748e7d67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-964071c2d89740bacd5c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-02eea2185f038c18601f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a204597c4c9a7fd8c24f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-527fd78f1dfcf25bfa13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcb3197420c782dc28e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f21bd26389d48049fdf2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59d78a3eb423a107ea4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-173bf7f8030d2693f9e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ff15f378cb84b2c70b5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ecaaec444ea9786d331a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cab923df5d8030480cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-845af79b6a7839cbaf04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eceb6d1ac2fc7d6ee2c3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-7; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c378d7fd3fa9a478276d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c87573dc10fc495b5d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e85afe09af9b0fd3130">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-374cf4bd634c9965d166">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e9c6467f6e0ffc7636b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc47564f76636724196b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d5c36ecda15abb80ac3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3026392ccc10ba8d2dc9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-448e227a622e102c25f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e588e7fd7911c0ae1d9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09fe23a0f5c248de149c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c72e54e2eb53ada3bb29">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f10b50e71a0f0c037c0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62d4066f518d50011137">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ed291fd206137fc2189">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3a3a9cb5bc63bc4b2db">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8b5940f3e616e68cb381">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74eb1a3f42af25a55132">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4efdbb9f940e73a994e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9da9f4d3c0fddd8b9296">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f57f006a9f1c1606fdc6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c41067fe8445e422ea69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64827d27ef2bdb8aa259">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-120a8be65de4f6a2c177">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dcaff1e9644dc7868389">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86cd60295af72911ef64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b213abeeb57b6c01498">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95e36728d56ec53138cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d64dfb09b3f8048484f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae48ba8802fc610135a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5106bed63e5ca45bc4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27e895e9c1792be8d90b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-37b9bf833165cc9072ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49a285516b2100633b9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d06c48ba594d53616230">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9780ea730c6b6e933ae5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cf703cbc90c23b20036f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c666b4b50063a68a31a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ceeedd6f72897ea774d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-268d39352a93b1b65422">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-15769d090a96b3f4f2ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72907ecd915a620ca902">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78cc36d9c4143fb30557">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e78e43ad8d187a36e787">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-29ff51187daa4692f080">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2e8189408c9e934cf7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ad5ab7d821919e4afec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4a904d5415c9474c016">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c04d870c27acb38ccab9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0eee2f6cd4c1b4807cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf6ad3fb385dbf9c3370">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b04f19a94450cdd685c3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-932ab2b09a4cf2d506b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3932d70fa310c4f47fcb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ec9318bad12a12c79ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-152e6502b5e8974ee9d2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-11; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-679018791f61f5149e6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92a0c033f1fea9e2593e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c0157cf5d768da3ea67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec1f4eb478953f53a18b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-11; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c34d4868660b2c1265c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9828ae76f844e0e3fa51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1369df37a42a42ce3cb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f235b72eb2f070610df9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-11; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ae788d3aa4974ac61ac3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1843629755229d157b0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f53d1730112ac80a39d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-735996afdf44f8d08c85">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-11; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-658b2b3aa0509a8e2582">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67df4e4528e71a64ede8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e797d3178e6015c135e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd3453096f490dca144a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6dc9fc369c2febfd89ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93a1ccf8442efe757fd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87a187ab4ace465ac3d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6a50fa1e16af4012e3a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0168ec6d04e7a185a2bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eeed60d7d9fe928f38ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c91355ac78a0fbd1538c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa08e04f47fe7a50d1b0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c81a899ada8a8c40ce95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-638d83bf487c1bbb4658">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb397f246d9e64df6aa7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c284435db9fbfe5a6caf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-13; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-737dcf84eeeb0d016e9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cfba4a9ecb2837ebf91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c5ae106f54bb6e6642f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb35aac5fdabe7bae394">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bd1744e49ffb9d42ae0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88661b627ece76f987dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d46983dd5240d7c199a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf58fa289a055169b6bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-13; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-55f06d08c4ca1cc84da9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4edced4e7c4ec2b98a85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f71f97a96a6b83d6c51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fca9cd98b68022b8389d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-13; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce53854e4b578c352cdf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b1811ecf922cd2173f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf08caa133c5512a2bec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-676dd81ac7bcf72bb5b6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1ccaa0eaf183e349518">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c90079c03664967df759">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9766bf8b259918c37342">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05b4f55a742ce5d65700">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9c7360991e4c1d694dd2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-daa164e5d2b325cc1976">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0cd1d6334b0308edad3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0dad59c0f5de6ae687b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a5800828e134bb5a88d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91b747c7704fe3c6e273">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c57bc7ff2bf913773665">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21461c232b11bb014751">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97d65864a1e7655e1048">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70fc0babd324058e4796">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec745e7a13a7c81039d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f630acf775f70f07b432">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-729165d8cecfe7d45566">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ff56c916265312edf24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b83da76c23cf2585658">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-491061eb3eb4b1f633f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8c127e1a3fe590ed9abd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47808f3f791a869a0498">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aebfb56811bb0a4ad213">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2234465668fc0904d28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f532b7da51b0d052a597">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b5c0d174a919dab041a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-972d641fb50c0679867c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-528a23e699704438d423">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a0e402c2b01119f968c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55bbbcab9f20e64d6abc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17ef598784baab7a2b6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04108f3a33980624328e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-473df4314a2ea62a35ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ed95b6b48fc61e8f6db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd1683c73d991668b3d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebde7cc107db770d2b37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93ad0634085cbc5fb818">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-141a53be7636194e28bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3ceb76accc893e080ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca312c50a80f0c771d33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0b33a061d0fc779cbf72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c785184b2a030cc244a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23cf080cc8694cd9f39e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ece0d937a402c9c85a6e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-16; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2eb707e73446bb7647ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3e34accea5bf4940ad6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a744261f993686d7449a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d6e6a05bf525662d047">[ ] unverified</a> |
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
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e0360c4cbb961e1cc9bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e0360c4cbb961e1cc9bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87255646e6578d7e2a68"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-87255646e6578d7e2a68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffcd493be7462828d1f1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ffcd493be7462828d1f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f99169b50944dcbe0a1f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f99169b50944dcbe0a1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0d76b36733f058284fa4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0d76b36733f058284fa4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c4d933f40b5c0e851af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8c4d933f40b5c0e851af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91ffdc0f365a77a1c56b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-91ffdc0f365a77a1c56b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-569ae6639a306132a9d4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-569ae6639a306132a9d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fa24cd8320ddb01f1ce9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa24cd8320ddb01f1ce9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e19df3a1637ab7908b8f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e19df3a1637ab7908b8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27cc138798a63feffca2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27cc138798a63feffca2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d4343f990d0743a28e2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d4343f990d0743a28e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23a9150db63fe995aff0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23a9150db63fe995aff0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41fbb2319c17a5912c96"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-41fbb2319c17a5912c96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94c54ebad68210e1e925"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94c54ebad68210e1e925`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a925ef9768102efe3155"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a925ef9768102efe3155`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f45ceb3104a13fdef4a0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f45ceb3104a13fdef4a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d4e8c9c8249c3b11500"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d4e8c9c8249c3b11500`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e17383a91c2e7d00dd57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e17383a91c2e7d00dd57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69de29599b134b0cac82"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69de29599b134b0cac82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73182dc2d1e94ecfe0e8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73182dc2d1e94ecfe0e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c569b5b3fec8be83745"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0c569b5b3fec8be83745`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16e06469817a850812a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-16e06469817a850812a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d08147b97f65744c4bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7d08147b97f65744c4bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-77a7f6d83d51d97b3aa8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-77a7f6d83d51d97b3aa8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa346f6c0a3c62737474"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa346f6c0a3c62737474`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-557a818f9afe17a005a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-557a818f9afe17a005a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d3bdb4c0c7aa68221c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d3bdb4c0c7aa68221c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-16d7401a2341132e68f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-16d7401a2341132e68f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3729a6d0d8a0a8a6e34"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a3729a6d0d8a0a8a6e34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-996eb22228ad1e5612c6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-996eb22228ad1e5612c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c9debfab37084ec2d69"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c9debfab37084ec2d69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-S-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-02eea2185f038c18601f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-02eea2185f038c18601f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a204597c4c9a7fd8c24f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a204597c4c9a7fd8c24f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-527fd78f1dfcf25bfa13"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-527fd78f1dfcf25bfa13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcb3197420c782dc28e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fcb3197420c782dc28e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f21bd26389d48049fdf2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f21bd26389d48049fdf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59d78a3eb423a107ea4a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-59d78a3eb423a107ea4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-173bf7f8030d2693f9e5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-173bf7f8030d2693f9e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ff15f378cb84b2c70b5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ff15f378cb84b2c70b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ecaaec444ea9786d331a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ecaaec444ea9786d331a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cab923df5d8030480cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5cab923df5d8030480cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-845af79b6a7839cbaf04"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-845af79b6a7839cbaf04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eceb6d1ac2fc7d6ee2c3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eceb6d1ac2fc7d6ee2c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-7; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c378d7fd3fa9a478276d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c378d7fd3fa9a478276d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c87573dc10fc495b5d5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c87573dc10fc495b5d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e85afe09af9b0fd3130"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1e85afe09af9b0fd3130`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-374cf4bd634c9965d166"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-374cf4bd634c9965d166`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e9c6467f6e0ffc7636b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e9c6467f6e0ffc7636b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc47564f76636724196b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bc47564f76636724196b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d5c36ecda15abb80ac3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d5c36ecda15abb80ac3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3026392ccc10ba8d2dc9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3026392ccc10ba8d2dc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-448e227a622e102c25f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-448e227a622e102c25f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e588e7fd7911c0ae1d9b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e588e7fd7911c0ae1d9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09fe23a0f5c248de149c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-09fe23a0f5c248de149c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c72e54e2eb53ada3bb29"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c72e54e2eb53ada3bb29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f10b50e71a0f0c037c0b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f10b50e71a0f0c037c0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62d4066f518d50011137"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62d4066f518d50011137`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ed291fd206137fc2189"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ed291fd206137fc2189`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3a3a9cb5bc63bc4b2db"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d3a3a9cb5bc63bc4b2db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-7; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8b5940f3e616e68cb381"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b5940f3e616e68cb381`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74eb1a3f42af25a55132"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74eb1a3f42af25a55132`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4efdbb9f940e73a994e3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4efdbb9f940e73a994e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9da9f4d3c0fddd8b9296"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9da9f4d3c0fddd8b9296`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f57f006a9f1c1606fdc6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f57f006a9f1c1606fdc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c41067fe8445e422ea69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c41067fe8445e422ea69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64827d27ef2bdb8aa259"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-64827d27ef2bdb8aa259`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-120a8be65de4f6a2c177"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-120a8be65de4f6a2c177`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dcaff1e9644dc7868389"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dcaff1e9644dc7868389`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86cd60295af72911ef64"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-86cd60295af72911ef64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b213abeeb57b6c01498"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8b213abeeb57b6c01498`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95e36728d56ec53138cb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95e36728d56ec53138cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d64dfb09b3f8048484f4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d64dfb09b3f8048484f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae48ba8802fc610135a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae48ba8802fc610135a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5106bed63e5ca45bc4b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a5106bed63e5ca45bc4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27e895e9c1792be8d90b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27e895e9c1792be8d90b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-37b9bf833165cc9072ed"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-37b9bf833165cc9072ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49a285516b2100633b9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-49a285516b2100633b9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d06c48ba594d53616230"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d06c48ba594d53616230`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9780ea730c6b6e933ae5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9780ea730c6b6e933ae5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cf703cbc90c23b20036f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cf703cbc90c23b20036f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c666b4b50063a68a31a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0c666b4b50063a68a31a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ceeedd6f72897ea774d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ceeedd6f72897ea774d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-268d39352a93b1b65422"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-268d39352a93b1b65422`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-15769d090a96b3f4f2ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-15769d090a96b3f4f2ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72907ecd915a620ca902"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-72907ecd915a620ca902`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78cc36d9c4143fb30557"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78cc36d9c4143fb30557`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e78e43ad8d187a36e787"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e78e43ad8d187a36e787`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-29ff51187daa4692f080"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-29ff51187daa4692f080`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2e8189408c9e934cf7a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f2e8189408c9e934cf7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ad5ab7d821919e4afec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ad5ab7d821919e4afec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4a904d5415c9474c016"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4a904d5415c9474c016`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c04d870c27acb38ccab9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c04d870c27acb38ccab9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0eee2f6cd4c1b4807cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0eee2f6cd4c1b4807cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf6ad3fb385dbf9c3370"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cf6ad3fb385dbf9c3370`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b04f19a94450cdd685c3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b04f19a94450cdd685c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-932ab2b09a4cf2d506b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-932ab2b09a4cf2d506b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3932d70fa310c4f47fcb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3932d70fa310c4f47fcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ec9318bad12a12c79ea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7ec9318bad12a12c79ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-152e6502b5e8974ee9d2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-152e6502b5e8974ee9d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-11; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-679018791f61f5149e6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-679018791f61f5149e6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92a0c033f1fea9e2593e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-92a0c033f1fea9e2593e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c0157cf5d768da3ea67"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c0157cf5d768da3ea67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec1f4eb478953f53a18b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec1f4eb478953f53a18b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-11; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c34d4868660b2c1265c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c34d4868660b2c1265c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9828ae76f844e0e3fa51"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9828ae76f844e0e3fa51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1369df37a42a42ce3cb9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1369df37a42a42ce3cb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f235b72eb2f070610df9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f235b72eb2f070610df9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-11; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ae788d3aa4974ac61ac3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ae788d3aa4974ac61ac3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1843629755229d157b0e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1843629755229d157b0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f53d1730112ac80a39d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f53d1730112ac80a39d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-735996afdf44f8d08c85"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-735996afdf44f8d08c85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-11; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-658b2b3aa0509a8e2582"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-658b2b3aa0509a8e2582`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67df4e4528e71a64ede8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67df4e4528e71a64ede8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e797d3178e6015c135e3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e797d3178e6015c135e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd3453096f490dca144a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fd3453096f490dca144a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-11; to port: 1-N-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6dc9fc369c2febfd89ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6dc9fc369c2febfd89ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93a1ccf8442efe757fd1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-93a1ccf8442efe757fd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87a187ab4ace465ac3d9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-87a187ab4ace465ac3d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6a50fa1e16af4012e3a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6a50fa1e16af4012e3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0168ec6d04e7a185a2bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0168ec6d04e7a185a2bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eeed60d7d9fe928f38ed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eeed60d7d9fe928f38ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c91355ac78a0fbd1538c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c91355ac78a0fbd1538c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa08e04f47fe7a50d1b0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aa08e04f47fe7a50d1b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c81a899ada8a8c40ce95"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c81a899ada8a8c40ce95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-638d83bf487c1bbb4658"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-638d83bf487c1bbb4658`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb397f246d9e64df6aa7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fb397f246d9e64df6aa7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c284435db9fbfe5a6caf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c284435db9fbfe5a6caf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-13; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-737dcf84eeeb0d016e9c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-737dcf84eeeb0d016e9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cfba4a9ecb2837ebf91"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1cfba4a9ecb2837ebf91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c5ae106f54bb6e6642f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c5ae106f54bb6e6642f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb35aac5fdabe7bae394"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb35aac5fdabe7bae394`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bd1744e49ffb9d42ae0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bd1744e49ffb9d42ae0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88661b627ece76f987dd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-88661b627ece76f987dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d46983dd5240d7c199a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d46983dd5240d7c199a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf58fa289a055169b6bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bf58fa289a055169b6bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-13; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-55f06d08c4ca1cc84da9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-55f06d08c4ca1cc84da9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4edced4e7c4ec2b98a85"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4edced4e7c4ec2b98a85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f71f97a96a6b83d6c51"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5f71f97a96a6b83d6c51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fca9cd98b68022b8389d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fca9cd98b68022b8389d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-13; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce53854e4b578c352cdf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce53854e4b578c352cdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b1811ecf922cd2173f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b1811ecf922cd2173f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf08caa133c5512a2bec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bf08caa133c5512a2bec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-676dd81ac7bcf72bb5b6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-676dd81ac7bcf72bb5b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-13; to port: 1-N-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97d65864a1e7655e1048"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97d65864a1e7655e1048`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70fc0babd324058e4796"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-70fc0babd324058e4796`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec745e7a13a7c81039d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ec745e7a13a7c81039d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f630acf775f70f07b432"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f630acf775f70f07b432`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-729165d8cecfe7d45566"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-729165d8cecfe7d45566`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ff56c916265312edf24"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ff56c916265312edf24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b83da76c23cf2585658"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8b83da76c23cf2585658`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-491061eb3eb4b1f633f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-491061eb3eb4b1f633f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0b33a061d0fc779cbf72"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b33a061d0fc779cbf72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c785184b2a030cc244a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0c785184b2a030cc244a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23cf080cc8694cd9f39e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-23cf080cc8694cd9f39e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ece0d937a402c9c85a6e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ece0d937a402c9c85a6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-N-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-16; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2eb707e73446bb7647ef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2eb707e73446bb7647ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3e34accea5bf4940ad6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a3e34accea5bf4940ad6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a744261f993686d7449a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a744261f993686d7449a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d6e6a05bf525662d047"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d6e6a05bf525662d047`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-16; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-upper-entry-branch:canonical-southeast | <a href="#case-preview_review-1e28f35de70eb66906db">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-upper-entry-branch:canonical-top | <a href="#case-preview_review-1e6759e12ec6b2d2fadd">[ ] unverified</a> | — | — | — | — |


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

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
