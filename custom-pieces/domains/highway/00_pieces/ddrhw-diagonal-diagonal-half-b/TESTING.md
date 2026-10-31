---
title: "Testing: DD RHW-4 \u2014 Diagonal Continuation B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Diagonal Continuation B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Preserves the complementary native diagonal DD RHW-4 continuation half and adds one 0.8 m-square concrete centre column from ground to the upper deck. Its lane positions differ from continuation A, so the halves are not interchangeable. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-2` | road / 1 / primary | in | [-8.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-3` | road / 1 / primary | out | [-8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-4` | road / 1 / primary | in | [-8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-N-in-5` | road / 1 / primary | in | [-3.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-6` | road / 1 / primary | out | [-3.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-7` | road / 1 / primary | in | [3.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-8` | road / 1 / primary | out | [3.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-2` → `1-N-out-8` | primary |
| road | `1-W-in-4` → `1-N-out-6` | primary |
| road | `1-N-in-5` → `1-W-out-3` | primary |
| road | `1-N-in-7` → `1-W-out-1` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-2` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-diagonal-half-b --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-diagonal-half-b/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-diagonal-half-b/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-6ce48a0b0061a76032d1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-6ce48a0b0061a76032d1"></a>

**General: unverified** — `software_resources-6ce48a0b0061a76032d1`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-6ce48a0b0061a76032d1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-6ce48a0b0061a76032d1"></a>

**General: unverified** — `software_connectivity-6ce48a0b0061a76032d1`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-8317ebfa194a2352be94">[ ] unverified</a> | <a href="#case-in_game_render-7c72fb5a15aa49797233">[ ] unverified</a> | <a href="#case-in_game_render-63870c6579b5e722242c">[ ] unverified</a> | <a href="#case-in_game_render-53920490d73c0d8a89e1">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-8317ebfa194a2352be94"></a>

**0° CCW: unverified** — `in_game_render-8317ebfa194a2352be94`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7c72fb5a15aa49797233"></a>

**90° CCW: unverified** — `in_game_render-7c72fb5a15aa49797233`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-63870c6579b5e722242c"></a>

**180° CCW: unverified** — `in_game_render-63870c6579b5e722242c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-53920490d73c0d8a89e1"></a>

**270° CCW: unverified** — `in_game_render-53920490d73c0d8a89e1`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-8317ebfa194a2352be94">[ ] unverified</a> | <a href="#case-in_game_placement-7c72fb5a15aa49797233">[ ] unverified</a> | <a href="#case-in_game_placement-63870c6579b5e722242c">[ ] unverified</a> | <a href="#case-in_game_placement-53920490d73c0d8a89e1">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-8317ebfa194a2352be94"></a>

**0° CCW: unverified** — `in_game_placement-8317ebfa194a2352be94`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7c72fb5a15aa49797233"></a>

**90° CCW: unverified** — `in_game_placement-7c72fb5a15aa49797233`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-63870c6579b5e722242c"></a>

**180° CCW: unverified** — `in_game_placement-63870c6579b5e722242c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-53920490d73c0d8a89e1"></a>

**270° CCW: unverified** — `in_game_placement-53920490d73c0d8a89e1`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-8317ebfa194a2352be94">[ ] unverified</a> | <a href="#case-in_game_demolition-7c72fb5a15aa49797233">[ ] unverified</a> | <a href="#case-in_game_demolition-63870c6579b5e722242c">[ ] unverified</a> | <a href="#case-in_game_demolition-53920490d73c0d8a89e1">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-8317ebfa194a2352be94"></a>

**0° CCW: unverified** — `in_game_demolition-8317ebfa194a2352be94`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7c72fb5a15aa49797233"></a>

**90° CCW: unverified** — `in_game_demolition-7c72fb5a15aa49797233`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-63870c6579b5e722242c"></a>

**180° CCW: unverified** — `in_game_demolition-63870c6579b5e722242c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-53920490d73c0d8a89e1"></a>

**270° CCW: unverified** — `in_game_demolition-53920490d73c0d8a89e1`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-8317ebfa194a2352be94">[ ] unverified</a> | <a href="#case-in_game_save_reload-7c72fb5a15aa49797233">[ ] unverified</a> | <a href="#case-in_game_save_reload-63870c6579b5e722242c">[ ] unverified</a> | <a href="#case-in_game_save_reload-53920490d73c0d8a89e1">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-8317ebfa194a2352be94"></a>

**0° CCW: unverified** — `in_game_save_reload-8317ebfa194a2352be94`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7c72fb5a15aa49797233"></a>

**90° CCW: unverified** — `in_game_save_reload-7c72fb5a15aa49797233`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-63870c6579b5e722242c"></a>

**180° CCW: unverified** — `in_game_save_reload-63870c6579b5e722242c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-53920490d73c0d8a89e1"></a>

**270° CCW: unverified** — `in_game_save_reload-53920490d73c0d8a89e1`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8 | — | <a href="#case-in_game_route_query-96fa10f3a9c7168c8410">[ ] unverified</a> | <a href="#case-in_game_route_query-058a623c8aca1df094a8">[ ] unverified</a> | <a href="#case-in_game_route_query-b090ba61bbc8b77d2ce5">[ ] unverified</a> | <a href="#case-in_game_route_query-bd04461526a605d28d4b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6 | — | <a href="#case-in_game_route_query-b24508a14e3f1d713d01">[ ] unverified</a> | <a href="#case-in_game_route_query-cac79b2388cda6c9c818">[ ] unverified</a> | <a href="#case-in_game_route_query-74afed48e813d872f6d8">[ ] unverified</a> | <a href="#case-in_game_route_query-8be0c86bc5ffef9ca9bf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-59058363138f7d4fbb3a">[ ] unverified</a> | <a href="#case-in_game_route_query-d5b7845c7fc48e2d54d6">[ ] unverified</a> | <a href="#case-in_game_route_query-ec5b86494ef3f1847b93">[ ] unverified</a> | <a href="#case-in_game_route_query-c16571331dea3c96b258">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-83ee6157b50702e2f441">[ ] unverified</a> | <a href="#case-in_game_route_query-439b5aa801de87fe4b55">[ ] unverified</a> | <a href="#case-in_game_route_query-8cf965709ea77c1139e5">[ ] unverified</a> | <a href="#case-in_game_route_query-cb0902fffe1ea0d9f888">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8</summary>

<a id="case-in_game_route_query-96fa10f3a9c7168c8410"></a>

**0° CCW: unverified** — `in_game_route_query-96fa10f3a9c7168c8410`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-058a623c8aca1df094a8"></a>

**90° CCW: unverified** — `in_game_route_query-058a623c8aca1df094a8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-b090ba61bbc8b77d2ce5"></a>

**180° CCW: unverified** — `in_game_route_query-b090ba61bbc8b77d2ce5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_route_query-bd04461526a605d28d4b"></a>

**270° CCW: unverified** — `in_game_route_query-bd04461526a605d28d4b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6</summary>

<a id="case-in_game_route_query-b24508a14e3f1d713d01"></a>

**0° CCW: unverified** — `in_game_route_query-b24508a14e3f1d713d01`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-cac79b2388cda6c9c818"></a>

**90° CCW: unverified** — `in_game_route_query-cac79b2388cda6c9c818`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-74afed48e813d872f6d8"></a>

**180° CCW: unverified** — `in_game_route_query-74afed48e813d872f6d8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_route_query-8be0c86bc5ffef9ca9bf"></a>

**270° CCW: unverified** — `in_game_route_query-8be0c86bc5ffef9ca9bf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3</summary>

<a id="case-in_game_route_query-59058363138f7d4fbb3a"></a>

**0° CCW: unverified** — `in_game_route_query-59058363138f7d4fbb3a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-d5b7845c7fc48e2d54d6"></a>

**90° CCW: unverified** — `in_game_route_query-d5b7845c7fc48e2d54d6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-ec5b86494ef3f1847b93"></a>

**180° CCW: unverified** — `in_game_route_query-ec5b86494ef3f1847b93`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-c16571331dea3c96b258"></a>

**270° CCW: unverified** — `in_game_route_query-c16571331dea3c96b258`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-83ee6157b50702e2f441"></a>

**0° CCW: unverified** — `in_game_route_query-83ee6157b50702e2f441`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-439b5aa801de87fe4b55"></a>

**90° CCW: unverified** — `in_game_route_query-439b5aa801de87fe4b55`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-8cf965709ea77c1139e5"></a>

**180° CCW: unverified** — `in_game_route_query-8cf965709ea77c1139e5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-cb0902fffe1ea0d9f888"></a>

**270° CCW: unverified** — `in_game_route_query-cb0902fffe1ea0d9f888`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8 | — | <a href="#case-in_game_visible_travel-96fa10f3a9c7168c8410">[ ] unverified</a> | <a href="#case-in_game_visible_travel-058a623c8aca1df094a8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b090ba61bbc8b77d2ce5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bd04461526a605d28d4b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6 | — | <a href="#case-in_game_visible_travel-b24508a14e3f1d713d01">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cac79b2388cda6c9c818">[ ] unverified</a> | <a href="#case-in_game_visible_travel-74afed48e813d872f6d8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8be0c86bc5ffef9ca9bf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-59058363138f7d4fbb3a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d5b7845c7fc48e2d54d6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ec5b86494ef3f1847b93">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c16571331dea3c96b258">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-83ee6157b50702e2f441">[ ] unverified</a> | <a href="#case-in_game_visible_travel-439b5aa801de87fe4b55">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8cf965709ea77c1139e5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cb0902fffe1ea0d9f888">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8</summary>

<a id="case-in_game_visible_travel-96fa10f3a9c7168c8410"></a>

**0° CCW: unverified** — `in_game_visible_travel-96fa10f3a9c7168c8410`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-058a623c8aca1df094a8"></a>

**90° CCW: unverified** — `in_game_visible_travel-058a623c8aca1df094a8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-b090ba61bbc8b77d2ce5"></a>

**180° CCW: unverified** — `in_game_visible_travel-b090ba61bbc8b77d2ce5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-bd04461526a605d28d4b"></a>

**270° CCW: unverified** — `in_game_visible_travel-bd04461526a605d28d4b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-8; entry: 1-W-in-2; exit: 1-N-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6</summary>

<a id="case-in_game_visible_travel-b24508a14e3f1d713d01"></a>

**0° CCW: unverified** — `in_game_visible_travel-b24508a14e3f1d713d01`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-cac79b2388cda6c9c818"></a>

**90° CCW: unverified** — `in_game_visible_travel-cac79b2388cda6c9c818`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-74afed48e813d872f6d8"></a>

**180° CCW: unverified** — `in_game_visible_travel-74afed48e813d872f6d8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-8be0c86bc5ffef9ca9bf"></a>

**270° CCW: unverified** — `in_game_visible_travel-8be0c86bc5ffef9ca9bf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-6; entry: 1-W-in-4; exit: 1-N-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3</summary>

<a id="case-in_game_visible_travel-59058363138f7d4fbb3a"></a>

**0° CCW: unverified** — `in_game_visible_travel-59058363138f7d4fbb3a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-d5b7845c7fc48e2d54d6"></a>

**90° CCW: unverified** — `in_game_visible_travel-d5b7845c7fc48e2d54d6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-ec5b86494ef3f1847b93"></a>

**180° CCW: unverified** — `in_game_visible_travel-ec5b86494ef3f1847b93`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-c16571331dea3c96b258"></a>

**270° CCW: unverified** — `in_game_visible_travel-c16571331dea3c96b258`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-83ee6157b50702e2f441"></a>

**0° CCW: unverified** — `in_game_visible_travel-83ee6157b50702e2f441`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-439b5aa801de87fe4b55"></a>

**90° CCW: unverified** — `in_game_visible_travel-439b5aa801de87fe4b55`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-8cf965709ea77c1139e5"></a>

**180° CCW: unverified** — `in_game_visible_travel-8cf965709ea77c1139e5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-cb0902fffe1ea0d9f888"></a>

**270° CCW: unverified** — `in_game_visible_travel-cb0902fffe1ea0d9f888`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-W-out-1; entry: 1-N-in-7; exit: 1-W-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc2427a060eb1d08a69e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e131bb0a3673aa1b0453">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab0d3ea74af454cbf1de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccb149983d087db713c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0848c25791260558a010">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a397179434a7b7a4d4c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-609fbffb454187fd8b88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3163a3dd36ad038bd44">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f746c779e0e5794308cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f46f023456e516bc819">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b526e9c73b6357183620">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72e4d2163b9b079ffbf0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-59e93eedd0c865427a1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9443109ab416074b792">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-572a05075913045cffc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63bc11cd638d98e4b0d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e71bc4ad24a0863e0578">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7be39f6c5a4f63c030e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e7142fb59143fd4258e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-691b39028745f9c10777">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ddb2f0310088f6648dc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfe07d5a9b35f2b23e77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34f0f7c9dad4f20c8d79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40583b7ac859debbbf7e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-716a36ba8a7d8c889bd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86ea1021d47cff206263">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f24f19e1ae6931e6485e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05e436737dc03400dd1c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc5cd266dca5283b78ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72396eab2092ed4191d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1436691c9c9aec351a79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79c746cbb6fb69af50f5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f42147d0f2cb4b17c46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e6014c96c8c8b126b26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-559094e6bf88ebe24db7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-958f5b75f2ff34b8b1fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2041ae287320a10f5212">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1de752a940f49b542b29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44b9a0cfb1eba53e9579">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d786c395ecb328869860">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3729503dd81886537f61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-711074d91fe72696dcaf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e6a532428116229a516">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ad225a520b3fc5d3dcb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7059a23841d6c2bf4616">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2b2e2d8387e4b39b023">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-305f42eca9e02b7e15a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bd4b890e8b1c203baf9">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc2427a060eb1d08a69e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc2427a060eb1d08a69e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e131bb0a3673aa1b0453"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e131bb0a3673aa1b0453`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab0d3ea74af454cbf1de"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ab0d3ea74af454cbf1de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccb149983d087db713c7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ccb149983d087db713c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0848c25791260558a010"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0848c25791260558a010`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a397179434a7b7a4d4c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2a397179434a7b7a4d4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-609fbffb454187fd8b88"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-609fbffb454187fd8b88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3163a3dd36ad038bd44"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a3163a3dd36ad038bd44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f746c779e0e5794308cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f746c779e0e5794308cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f46f023456e516bc819"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f46f023456e516bc819`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b526e9c73b6357183620"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b526e9c73b6357183620`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72e4d2163b9b079ffbf0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-72e4d2163b9b079ffbf0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-59e93eedd0c865427a1f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-59e93eedd0c865427a1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9443109ab416074b792"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e9443109ab416074b792`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-572a05075913045cffc9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-572a05075913045cffc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63bc11cd638d98e4b0d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-63bc11cd638d98e4b0d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e71bc4ad24a0863e0578"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e71bc4ad24a0863e0578`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7be39f6c5a4f63c030e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7be39f6c5a4f63c030e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e7142fb59143fd4258e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e7142fb59143fd4258e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-691b39028745f9c10777"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-691b39028745f9c10777`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ddb2f0310088f6648dc4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ddb2f0310088f6648dc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfe07d5a9b35f2b23e77"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bfe07d5a9b35f2b23e77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34f0f7c9dad4f20c8d79"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-34f0f7c9dad4f20c8d79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40583b7ac859debbbf7e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40583b7ac859debbbf7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-716a36ba8a7d8c889bd0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-716a36ba8a7d8c889bd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86ea1021d47cff206263"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-86ea1021d47cff206263`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f24f19e1ae6931e6485e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f24f19e1ae6931e6485e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05e436737dc03400dd1c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-05e436737dc03400dd1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc5cd266dca5283b78ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc5cd266dca5283b78ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72396eab2092ed4191d5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-72396eab2092ed4191d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1436691c9c9aec351a79"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1436691c9c9aec351a79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79c746cbb6fb69af50f5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79c746cbb6fb69af50f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7f42147d0f2cb4b17c46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f42147d0f2cb4b17c46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e6014c96c8c8b126b26"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2e6014c96c8c8b126b26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-559094e6bf88ebe24db7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-559094e6bf88ebe24db7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-958f5b75f2ff34b8b1fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-958f5b75f2ff34b8b1fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2041ae287320a10f5212"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2041ae287320a10f5212`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1de752a940f49b542b29"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1de752a940f49b542b29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44b9a0cfb1eba53e9579"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-44b9a0cfb1eba53e9579`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d786c395ecb328869860"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d786c395ecb328869860`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3729503dd81886537f61"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3729503dd81886537f61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-711074d91fe72696dcaf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-711074d91fe72696dcaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e6a532428116229a516"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e6a532428116229a516`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ad225a520b3fc5d3dcb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ad225a520b3fc5d3dcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7059a23841d6c2bf4616"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7059a23841d6c2bf4616`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2b2e2d8387e4b39b023"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f2b2e2d8387e4b39b023`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-305f42eca9e02b7e15a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-305f42eca9e02b7e15a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bd4b890e8b1c203baf9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5bd4b890e8b1c203baf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-diagonal-half-b:canonical-southeast | <a href="#case-preview_review-0261bae3845b05461994">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-diagonal-half-b:canonical-top | <a href="#case-preview_review-f9f9f92962ae7f8db7e4">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-diagonal-half-b:connection-overview | <a href="#case-preview_review-dcb0be1d3b4e9fadd4b7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-diagonal-half-b:canonical-southeast</summary>

<a id="case-preview_review-0261bae3845b05461994"></a>

**General: unverified** — `preview_review-0261bae3845b05461994`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-diagonal-half-b:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-diagonal-half-b:canonical-top</summary>

<a id="case-preview_review-f9f9f92962ae7f8db7e4"></a>

**General: unverified** — `preview_review-f9f9f92962ae7f8db7e4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-diagonal-half-b:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-diagonal-half-b:connection-overview</summary>

<a id="case-preview_review-dcb0be1d3b4e9fadd4b7"></a>

**General: unverified** — `preview_review-dcb0be1d3b4e9fadd4b7`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-diagonal-half-b:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
