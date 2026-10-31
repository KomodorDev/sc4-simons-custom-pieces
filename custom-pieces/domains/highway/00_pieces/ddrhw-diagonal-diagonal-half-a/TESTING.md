---
title: "Testing: DD RHW-4 \u2014 Diagonal Continuation A"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Diagonal Continuation A

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Preserves one native diagonal DD RHW-4 continuation half and adds one 0.8 m-square concrete centre column from ground to the upper deck. Use the complementary half beside it; a single half does not supply the complete roadway boundary. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-S-out-1` | road / 1 / primary | out | [-3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-S-in-2` | road / 1 / primary | in | [-3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-S-out-3` | road / 1 / primary | out | [3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-S-in-4` | road / 1 / primary | in | [3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `1-E-in-5` | road / 1 / primary | in | [8.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-E-out-6` | road / 1 / primary | out | [8.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-E-in-7` | road / 1 / primary | in | [8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-E-out-8` | road / 1 / primary | out | [8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-S-in-2` → `1-E-out-8` | primary |
| road | `1-S-in-4` → `1-E-out-6` | primary |
| road | `1-E-in-5` → `1-S-out-3` | primary |
| road | `1-E-in-7` → `1-S-out-1` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-S-in-2` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-2` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-4` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-5` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-7` | road / `1-E-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-diagonal-half-a --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-diagonal-half-a/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-diagonal-half-a/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-e2a26c1b65672fe79daa">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-e2a26c1b65672fe79daa"></a>

**General: unverified** — `software_resources-e2a26c1b65672fe79daa`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-e2a26c1b65672fe79daa">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-e2a26c1b65672fe79daa"></a>

**General: unverified** — `software_connectivity-e2a26c1b65672fe79daa`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-eebd362bf912c7de2bae">[ ] unverified</a> | <a href="#case-in_game_render-2c06aefe1cf1192855e5">[ ] unverified</a> | <a href="#case-in_game_render-105e394fb9da1fe6c030">[ ] unverified</a> | <a href="#case-in_game_render-bbc30152786595adf1af">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-eebd362bf912c7de2bae"></a>

**0° CCW: unverified** — `in_game_render-eebd362bf912c7de2bae`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2c06aefe1cf1192855e5"></a>

**90° CCW: unverified** — `in_game_render-2c06aefe1cf1192855e5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-105e394fb9da1fe6c030"></a>

**180° CCW: unverified** — `in_game_render-105e394fb9da1fe6c030`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-bbc30152786595adf1af"></a>

**270° CCW: unverified** — `in_game_render-bbc30152786595adf1af`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-eebd362bf912c7de2bae">[ ] unverified</a> | <a href="#case-in_game_placement-2c06aefe1cf1192855e5">[ ] unverified</a> | <a href="#case-in_game_placement-105e394fb9da1fe6c030">[ ] unverified</a> | <a href="#case-in_game_placement-bbc30152786595adf1af">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-eebd362bf912c7de2bae"></a>

**0° CCW: unverified** — `in_game_placement-eebd362bf912c7de2bae`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2c06aefe1cf1192855e5"></a>

**90° CCW: unverified** — `in_game_placement-2c06aefe1cf1192855e5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-105e394fb9da1fe6c030"></a>

**180° CCW: unverified** — `in_game_placement-105e394fb9da1fe6c030`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-bbc30152786595adf1af"></a>

**270° CCW: unverified** — `in_game_placement-bbc30152786595adf1af`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-eebd362bf912c7de2bae">[ ] unverified</a> | <a href="#case-in_game_demolition-2c06aefe1cf1192855e5">[ ] unverified</a> | <a href="#case-in_game_demolition-105e394fb9da1fe6c030">[ ] unverified</a> | <a href="#case-in_game_demolition-bbc30152786595adf1af">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-eebd362bf912c7de2bae"></a>

**0° CCW: unverified** — `in_game_demolition-eebd362bf912c7de2bae`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2c06aefe1cf1192855e5"></a>

**90° CCW: unverified** — `in_game_demolition-2c06aefe1cf1192855e5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-105e394fb9da1fe6c030"></a>

**180° CCW: unverified** — `in_game_demolition-105e394fb9da1fe6c030`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-bbc30152786595adf1af"></a>

**270° CCW: unverified** — `in_game_demolition-bbc30152786595adf1af`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-eebd362bf912c7de2bae">[ ] unverified</a> | <a href="#case-in_game_save_reload-2c06aefe1cf1192855e5">[ ] unverified</a> | <a href="#case-in_game_save_reload-105e394fb9da1fe6c030">[ ] unverified</a> | <a href="#case-in_game_save_reload-bbc30152786595adf1af">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-eebd362bf912c7de2bae"></a>

**0° CCW: unverified** — `in_game_save_reload-eebd362bf912c7de2bae`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2c06aefe1cf1192855e5"></a>

**90° CCW: unverified** — `in_game_save_reload-2c06aefe1cf1192855e5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-105e394fb9da1fe6c030"></a>

**180° CCW: unverified** — `in_game_save_reload-105e394fb9da1fe6c030`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-bbc30152786595adf1af"></a>

**270° CCW: unverified** — `in_game_save_reload-bbc30152786595adf1af`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8 | — | <a href="#case-in_game_route_query-7e299d3cdf10f1b5df41">[ ] unverified</a> | <a href="#case-in_game_route_query-1daaa0a0ce4379f89a13">[ ] unverified</a> | <a href="#case-in_game_route_query-b39bd7180a87511aa9c7">[ ] unverified</a> | <a href="#case-in_game_route_query-ddb473cc03b333845cbf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6 | — | <a href="#case-in_game_route_query-b2677c07f80373fba6f2">[ ] unverified</a> | <a href="#case-in_game_route_query-1f8b22ec31bb6673412e">[ ] unverified</a> | <a href="#case-in_game_route_query-9d19291e94097a1972eb">[ ] unverified</a> | <a href="#case-in_game_route_query-d8c7ae32dde1f082f330">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3 | — | <a href="#case-in_game_route_query-2a3a1dad24f30c649b04">[ ] unverified</a> | <a href="#case-in_game_route_query-ae812e1613797dd70aa0">[ ] unverified</a> | <a href="#case-in_game_route_query-6a2601e8c05a803b948d">[ ] unverified</a> | <a href="#case-in_game_route_query-ed728f9e37ae24c5cf45">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1 | — | <a href="#case-in_game_route_query-c24962a1e364b7c1fd72">[ ] unverified</a> | <a href="#case-in_game_route_query-bdb4c1e64ead516c3e25">[ ] unverified</a> | <a href="#case-in_game_route_query-1dda5d1bbcc1dd673ef5">[ ] unverified</a> | <a href="#case-in_game_route_query-3b8534ce855d15c8af10">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8</summary>

<a id="case-in_game_route_query-7e299d3cdf10f1b5df41"></a>

**0° CCW: unverified** — `in_game_route_query-7e299d3cdf10f1b5df41`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-1daaa0a0ce4379f89a13"></a>

**90° CCW: unverified** — `in_game_route_query-1daaa0a0ce4379f89a13`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-b39bd7180a87511aa9c7"></a>

**180° CCW: unverified** — `in_game_route_query-b39bd7180a87511aa9c7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_route_query-ddb473cc03b333845cbf"></a>

**270° CCW: unverified** — `in_game_route_query-ddb473cc03b333845cbf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6</summary>

<a id="case-in_game_route_query-b2677c07f80373fba6f2"></a>

**0° CCW: unverified** — `in_game_route_query-b2677c07f80373fba6f2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-1f8b22ec31bb6673412e"></a>

**90° CCW: unverified** — `in_game_route_query-1f8b22ec31bb6673412e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-9d19291e94097a1972eb"></a>

**180° CCW: unverified** — `in_game_route_query-9d19291e94097a1972eb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-d8c7ae32dde1f082f330"></a>

**270° CCW: unverified** — `in_game_route_query-d8c7ae32dde1f082f330`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3</summary>

<a id="case-in_game_route_query-2a3a1dad24f30c649b04"></a>

**0° CCW: unverified** — `in_game_route_query-2a3a1dad24f30c649b04`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-ae812e1613797dd70aa0"></a>

**90° CCW: unverified** — `in_game_route_query-ae812e1613797dd70aa0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-6a2601e8c05a803b948d"></a>

**180° CCW: unverified** — `in_game_route_query-6a2601e8c05a803b948d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-ed728f9e37ae24c5cf45"></a>

**270° CCW: unverified** — `in_game_route_query-ed728f9e37ae24c5cf45`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1</summary>

<a id="case-in_game_route_query-c24962a1e364b7c1fd72"></a>

**0° CCW: unverified** — `in_game_route_query-c24962a1e364b7c1fd72`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-bdb4c1e64ead516c3e25"></a>

**90° CCW: unverified** — `in_game_route_query-bdb4c1e64ead516c3e25`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-1dda5d1bbcc1dd673ef5"></a>

**180° CCW: unverified** — `in_game_route_query-1dda5d1bbcc1dd673ef5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-3b8534ce855d15c8af10"></a>

**270° CCW: unverified** — `in_game_route_query-3b8534ce855d15c8af10`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8 | — | <a href="#case-in_game_visible_travel-7e299d3cdf10f1b5df41">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1daaa0a0ce4379f89a13">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b39bd7180a87511aa9c7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ddb473cc03b333845cbf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6 | — | <a href="#case-in_game_visible_travel-b2677c07f80373fba6f2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1f8b22ec31bb6673412e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9d19291e94097a1972eb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d8c7ae32dde1f082f330">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3 | — | <a href="#case-in_game_visible_travel-2a3a1dad24f30c649b04">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ae812e1613797dd70aa0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6a2601e8c05a803b948d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ed728f9e37ae24c5cf45">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1 | — | <a href="#case-in_game_visible_travel-c24962a1e364b7c1fd72">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bdb4c1e64ead516c3e25">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1dda5d1bbcc1dd673ef5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3b8534ce855d15c8af10">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8</summary>

<a id="case-in_game_visible_travel-7e299d3cdf10f1b5df41"></a>

**0° CCW: unverified** — `in_game_visible_travel-7e299d3cdf10f1b5df41`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-1daaa0a0ce4379f89a13"></a>

**90° CCW: unverified** — `in_game_visible_travel-1daaa0a0ce4379f89a13`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-b39bd7180a87511aa9c7"></a>

**180° CCW: unverified** — `in_game_visible_travel-b39bd7180a87511aa9c7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-ddb473cc03b333845cbf"></a>

**270° CCW: unverified** — `in_game_visible_travel-ddb473cc03b333845cbf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-2>1-E-out-8; entry: 1-S-in-2; exit: 1-E-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6</summary>

<a id="case-in_game_visible_travel-b2677c07f80373fba6f2"></a>

**0° CCW: unverified** — `in_game_visible_travel-b2677c07f80373fba6f2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-1f8b22ec31bb6673412e"></a>

**90° CCW: unverified** — `in_game_visible_travel-1f8b22ec31bb6673412e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-9d19291e94097a1972eb"></a>

**180° CCW: unverified** — `in_game_visible_travel-9d19291e94097a1972eb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-d8c7ae32dde1f082f330"></a>

**270° CCW: unverified** — `in_game_visible_travel-d8c7ae32dde1f082f330`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-4>1-E-out-6; entry: 1-S-in-4; exit: 1-E-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3</summary>

<a id="case-in_game_visible_travel-2a3a1dad24f30c649b04"></a>

**0° CCW: unverified** — `in_game_visible_travel-2a3a1dad24f30c649b04`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-ae812e1613797dd70aa0"></a>

**90° CCW: unverified** — `in_game_visible_travel-ae812e1613797dd70aa0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-6a2601e8c05a803b948d"></a>

**180° CCW: unverified** — `in_game_visible_travel-6a2601e8c05a803b948d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-ed728f9e37ae24c5cf45"></a>

**270° CCW: unverified** — `in_game_visible_travel-ed728f9e37ae24c5cf45`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-5>1-S-out-3; entry: 1-E-in-5; exit: 1-S-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1</summary>

<a id="case-in_game_visible_travel-c24962a1e364b7c1fd72"></a>

**0° CCW: unverified** — `in_game_visible_travel-c24962a1e364b7c1fd72`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-bdb4c1e64ead516c3e25"></a>

**90° CCW: unverified** — `in_game_visible_travel-bdb4c1e64ead516c3e25`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-1dda5d1bbcc1dd673ef5"></a>

**180° CCW: unverified** — `in_game_visible_travel-1dda5d1bbcc1dd673ef5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-3b8534ce855d15c8af10"></a>

**270° CCW: unverified** — `in_game_visible_travel-3b8534ce855d15c8af10`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-7>1-S-out-1; entry: 1-E-in-7; exit: 1-S-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-72eae0c27ae290240404">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd1bdf866cb831d96c40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2ba28bda46b37b4b796">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62e50201ae85d1b0daef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1780d9ff3898f9e07b67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ae614dfd609f7389a74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92869f21d976bc9cf017">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99c061e5f5ce4c7c5f6d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce5aa217176de84912e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-505f31badb660856e20c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-352841defabdc1b016e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88dc6ab0e2b131f45a96">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8e9112aa8042ac3348c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ef175a2caf88434a400">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60328b18f9a7030675ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03e2505ad2b780e43657">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-78c2f609dc3b69a3818a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26f852f1bac33d8ce4e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c27892708b65433fc3d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9aa4131a547a70be767c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0eb6a4cfe5c6e961762b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a83aecbfe683303429fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a49de36c63e3da4d15f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b518db0be540f99098a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca2fc7df66c1a5ebf850">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14e2efa63a41fb1401ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf77f4cd290584953676">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-162baa7510bc9709a8bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d8b41d012c10bf211ad1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00d4f13add8f04a96ca7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6291b8bf7a2b93417c91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9335dae5cec84ab7c43b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e373203c101b8611de8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3c8d07ab8fa43f8a7e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d42cc3a58c1c8d5d4ad9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f692229283295ee191c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-03af9887363039575eb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d8ea62823547b7b9ea9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8619bdb1638ba8b5c04b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb2b31442cb92d6c6a89">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d86f9e9248fa7c0b2ab3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d32e8fd4ec0d24de19b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-121af8a58a89c0f718be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12ecaf92fe90a6538bf5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2176c6ca657977bc241e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8065103729e1816b6e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2d4e9e56175045778d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a68394ec104f28cb9c5">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-72eae0c27ae290240404"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-72eae0c27ae290240404`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd1bdf866cb831d96c40"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd1bdf866cb831d96c40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2ba28bda46b37b4b796"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2ba28bda46b37b4b796`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62e50201ae85d1b0daef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-62e50201ae85d1b0daef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1780d9ff3898f9e07b67"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1780d9ff3898f9e07b67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ae614dfd609f7389a74"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4ae614dfd609f7389a74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92869f21d976bc9cf017"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-92869f21d976bc9cf017`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99c061e5f5ce4c7c5f6d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-99c061e5f5ce4c7c5f6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce5aa217176de84912e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce5aa217176de84912e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-505f31badb660856e20c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-505f31badb660856e20c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-352841defabdc1b016e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-352841defabdc1b016e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88dc6ab0e2b131f45a96"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-88dc6ab0e2b131f45a96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-2; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8e9112aa8042ac3348c6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8e9112aa8042ac3348c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ef175a2caf88434a400"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6ef175a2caf88434a400`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60328b18f9a7030675ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-60328b18f9a7030675ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03e2505ad2b780e43657"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03e2505ad2b780e43657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-78c2f609dc3b69a3818a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-78c2f609dc3b69a3818a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26f852f1bac33d8ce4e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-26f852f1bac33d8ce4e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c27892708b65433fc3d9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c27892708b65433fc3d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9aa4131a547a70be767c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9aa4131a547a70be767c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0eb6a4cfe5c6e961762b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0eb6a4cfe5c6e961762b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a83aecbfe683303429fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a83aecbfe683303429fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a49de36c63e3da4d15f3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a49de36c63e3da4d15f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b518db0be540f99098a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b518db0be540f99098a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-4; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca2fc7df66c1a5ebf850"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca2fc7df66c1a5ebf850`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14e2efa63a41fb1401ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-14e2efa63a41fb1401ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf77f4cd290584953676"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cf77f4cd290584953676`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-162baa7510bc9709a8bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-162baa7510bc9709a8bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d8b41d012c10bf211ad1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d8b41d012c10bf211ad1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00d4f13add8f04a96ca7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00d4f13add8f04a96ca7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6291b8bf7a2b93417c91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6291b8bf7a2b93417c91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9335dae5cec84ab7c43b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9335dae5cec84ab7c43b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e373203c101b8611de8a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e373203c101b8611de8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3c8d07ab8fa43f8a7e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c3c8d07ab8fa43f8a7e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d42cc3a58c1c8d5d4ad9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d42cc3a58c1c8d5d4ad9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f692229283295ee191c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f692229283295ee191c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-5; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-03af9887363039575eb3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-03af9887363039575eb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d8ea62823547b7b9ea9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6d8ea62823547b7b9ea9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8619bdb1638ba8b5c04b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8619bdb1638ba8b5c04b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb2b31442cb92d6c6a89"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eb2b31442cb92d6c6a89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d86f9e9248fa7c0b2ab3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d86f9e9248fa7c0b2ab3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d32e8fd4ec0d24de19b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d32e8fd4ec0d24de19b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-121af8a58a89c0f718be"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-121af8a58a89c0f718be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12ecaf92fe90a6538bf5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-12ecaf92fe90a6538bf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2176c6ca657977bc241e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2176c6ca657977bc241e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8065103729e1816b6e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b8065103729e1816b6e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2d4e9e56175045778d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2d4e9e56175045778d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a68394ec104f28cb9c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a68394ec104f28cb9c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-7; to port: 1-E-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-diagonal-half-a:canonical-southeast | <a href="#case-preview_review-b94b06fc714aafb04d90">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-diagonal-half-a:canonical-top | <a href="#case-preview_review-69d8b8d6ab5d3c879367">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-diagonal-half-a:connection-overview | <a href="#case-preview_review-c4ed3850f270bc836862">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-diagonal-half-a:canonical-southeast</summary>

<a id="case-preview_review-b94b06fc714aafb04d90"></a>

**General: unverified** — `preview_review-b94b06fc714aafb04d90`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-diagonal-half-a:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-diagonal-half-a:canonical-top</summary>

<a id="case-preview_review-69d8b8d6ab5d3c879367"></a>

**General: unverified** — `preview_review-69d8b8d6ab5d3c879367`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-diagonal-half-a:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-diagonal-half-a:connection-overview</summary>

<a id="case-preview_review-c4ed3850f270bc836862"></a>

**General: unverified** — `preview_review-c4ed3850f270bc836862`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-diagonal-half-a:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
