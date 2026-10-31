---
title: "Testing: RHW Ramp — Lower Full Exit Ramp — Compact"
summary: "Check this exact component's traffic ownership, complete physical geometry, and scoped game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — Lower Full Exit Ramp — Compact

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-lower-exit-compact` resources and the matching complete [assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). This lower ramp has four traffic ports and two intrinsic route fragments. An intrinsic fragment is the part of a traffic journey stored within this one piece. Between those fragments, the route crosses a highway-owned tile in the stamp. The visible ramp is continuous, but cars need the correctly placed stamp to join the fragments; the matrix does not promise a complete isolated highway-to-Avenue journey.

A **PATH** is a saved traffic-route resource, and an **S3D** is the visible model made from indexed triangles. Model faces can extend beyond the tiles that store this piece's PATHs. A flat physical cut at the native highway edge is different from the traffic connection at a city-tile edge. Check both, rather than assuming that one card describes the entire physical opening.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -14.245568, 3.000444]; [-0.9442561859245556, -0.3292115662354699]; -0.226761428 | `path-interface-aeabf380377c95bbb5f1` |
| `1-E-in-2` | road / 1 / primary | in | [8.0, -10.207444, 6.745132]; [-0.9793492239542138, -0.2021759074179693]; -0.226757443 | `path-interface-daca863776677fe500f2` |
| `1-S-out-3` | road / 1 / primary | out | [17.960601, -8.0, 7.5]; [-0.969170208591516, -0.24639218083915987]; 0.0 | `path-interface-3dcc6d5eb15355745274` |
| `1-E-in-4` | road / 1 / primary | in | [24.0, -6.634072, 7.5]; [-0.9935463584813209, -0.11342677615319352]; 0.0 | `path-interface-34a26816572a48081146` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-E-in-2` → `1-W-out-1` | primary |
| road | `1-E-in-4` → `1-S-out-3` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-E-in-2` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-E-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including Wine or CrossOver. Follow the [shared build guide](../../../../docs/BUILD_AND_INSTALL.md) for exact dependency hashes and the captured Avenue input. Build the `ddrhw-modular-ramp-kit` set, and prepare the `modular-diagonal-diamond` Highways menu. Building and rendering do not install game files. Use flat terrain in a disposable city, and follow the [piece placement instructions](README.md#2-piece-and-placement).

The default assembly cycles seven R40 components. The four full compact ramps and two retained compact Avenue junctions have separate buttons outside that cycle. Replace a matching ramp pair and its terminal together; the old compact grade-only types do not contain the transferred curved throats.

## 3. Software checks

Follow the [assembly software commands](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#3-software-checks), including `python3 -B tools/run_tests.py` from the repository root and verification of the selected saved build. The focused family tests check exclusive construction ownership, exact retained high samples, signed slopes, the new R40 sections, the four flat R40 ground ports, and continuous texture phase. The face-partition tests specifically keep a centre pier when its old concrete mesh also contains a curved barrier bridge.

The [independent partition proof](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/evidence/straight-partition-preservation.json) compares complete assembled indexed triangles, original material bytes, UVs, winding, and per-cell PATH bytes against the immutable accepted checkpoint. Re-anchored faces use exactly one float32 translation from their old cell to their new host. The [reviewed model contract](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/straight-partition-models.jsonc) binds each resulting saved model; it does not approve game behaviour.

For physical joins, compare the complete pavement, 1 m underside, Jersey profiles, and inset bridge strips at the native highway edge. For traffic, compare every exposed tile-edge port, including all four ports of each lower full ramp. Standalone model overhang is deliberate; continuous route support must be checked against the assembled model union.

## 4. Game checks

Place this component in the complete matching assembly. Inspect the placed result after clicking, including rotations, barriers, pavement, supports, and shadows; the construction preview is a separate observation. Use Route Query on every required movement, watch a car complete it, confirm the opposite-carriageway ramp movements remain unavailable, save the city, close it, and reload it. Test the lower ramps through both intrinsic fragments and their stamp-owned middle tile.

For the stamp and Avenue terminals, extend an ordinary Avenue, develop nearby zoning, and inspect whether pedestrian pavement appears and rotates with the road. Check both pedestrian directions separately. Record only the exact service, direction, pose, and environment actually observed, following the [shared testing procedure](../../../../docs/TESTING.md).

## 5. Results and known issues

The independent partition audit passed its source-preservation comparison. That result is separate from verification of a newly saved DAT and from every human game observation in the generated checklist. The full retained high-prefix traffic centre-lines contain sampled transition minima of approximately 1.735 m on the lower ramps and 3.500 m on the upper ramps. These inherited kinks are preserved by the exact source partition; R40 describes only the new circular sections. The 30% maximum grade is a compact game experiment, rather than a normal real-world highway design limit. Every game result for these corrected resources remains unverified until an explicit matching observation is recorded.

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

Current totals: unverified: 45, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-lower-exit-compact/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-lower-exit-compact/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-21798e343feff90b0003">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-21798e343feff90b0003"></a>

**General: unverified** — `software_resources-21798e343feff90b0003`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-21798e343feff90b0003">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-21798e343feff90b0003"></a>

**General: unverified** — `software_connectivity-21798e343feff90b0003`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-a362cc12b9aa47878a9d">[ ] unverified</a> | <a href="#case-in_game_render-fd0821cccf124998f71d">[ ] unverified</a> | <a href="#case-in_game_render-ec0e7af6631d9370cc41">[ ] unverified</a> | <a href="#case-in_game_render-0bc436a3c306e6c22930">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-a362cc12b9aa47878a9d"></a>

**0° CCW: unverified** — `in_game_render-a362cc12b9aa47878a9d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-fd0821cccf124998f71d"></a>

**90° CCW: unverified** — `in_game_render-fd0821cccf124998f71d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ec0e7af6631d9370cc41"></a>

**180° CCW: unverified** — `in_game_render-ec0e7af6631d9370cc41`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0bc436a3c306e6c22930"></a>

**270° CCW: unverified** — `in_game_render-0bc436a3c306e6c22930`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-a362cc12b9aa47878a9d">[ ] unverified</a> | <a href="#case-in_game_placement-fd0821cccf124998f71d">[ ] unverified</a> | <a href="#case-in_game_placement-ec0e7af6631d9370cc41">[ ] unverified</a> | <a href="#case-in_game_placement-0bc436a3c306e6c22930">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-a362cc12b9aa47878a9d"></a>

**0° CCW: unverified** — `in_game_placement-a362cc12b9aa47878a9d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-fd0821cccf124998f71d"></a>

**90° CCW: unverified** — `in_game_placement-fd0821cccf124998f71d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ec0e7af6631d9370cc41"></a>

**180° CCW: unverified** — `in_game_placement-ec0e7af6631d9370cc41`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0bc436a3c306e6c22930"></a>

**270° CCW: unverified** — `in_game_placement-0bc436a3c306e6c22930`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-a362cc12b9aa47878a9d">[ ] unverified</a> | <a href="#case-in_game_demolition-fd0821cccf124998f71d">[ ] unverified</a> | <a href="#case-in_game_demolition-ec0e7af6631d9370cc41">[ ] unverified</a> | <a href="#case-in_game_demolition-0bc436a3c306e6c22930">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-a362cc12b9aa47878a9d"></a>

**0° CCW: unverified** — `in_game_demolition-a362cc12b9aa47878a9d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-fd0821cccf124998f71d"></a>

**90° CCW: unverified** — `in_game_demolition-fd0821cccf124998f71d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ec0e7af6631d9370cc41"></a>

**180° CCW: unverified** — `in_game_demolition-ec0e7af6631d9370cc41`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0bc436a3c306e6c22930"></a>

**270° CCW: unverified** — `in_game_demolition-0bc436a3c306e6c22930`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-a362cc12b9aa47878a9d">[ ] unverified</a> | <a href="#case-in_game_save_reload-fd0821cccf124998f71d">[ ] unverified</a> | <a href="#case-in_game_save_reload-ec0e7af6631d9370cc41">[ ] unverified</a> | <a href="#case-in_game_save_reload-0bc436a3c306e6c22930">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-a362cc12b9aa47878a9d"></a>

**0° CCW: unverified** — `in_game_save_reload-a362cc12b9aa47878a9d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-fd0821cccf124998f71d"></a>

**90° CCW: unverified** — `in_game_save_reload-fd0821cccf124998f71d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ec0e7af6631d9370cc41"></a>

**180° CCW: unverified** — `in_game_save_reload-ec0e7af6631d9370cc41`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0bc436a3c306e6c22930"></a>

**270° CCW: unverified** — `in_game_save_reload-0bc436a3c306e6c22930`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-1d9e1e2ce788a06a8921">[ ] unverified</a> | <a href="#case-in_game_route_query-cd9e80a256b646b18e1f">[ ] unverified</a> | <a href="#case-in_game_route_query-e635eff14e7ee7b52318">[ ] unverified</a> | <a href="#case-in_game_route_query-b0d9394718f5fa76dc0d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3 | — | <a href="#case-in_game_route_query-caa2b1107fecb68b15ea">[ ] unverified</a> | <a href="#case-in_game_route_query-33f82282cfdde948700f">[ ] unverified</a> | <a href="#case-in_game_route_query-497804a4bc73496cdf09">[ ] unverified</a> | <a href="#case-in_game_route_query-5473dfbcc88973588a07">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-1d9e1e2ce788a06a8921"></a>

**0° CCW: unverified** — `in_game_route_query-1d9e1e2ce788a06a8921`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-cd9e80a256b646b18e1f"></a>

**90° CCW: unverified** — `in_game_route_query-cd9e80a256b646b18e1f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-e635eff14e7ee7b52318"></a>

**180° CCW: unverified** — `in_game_route_query-e635eff14e7ee7b52318`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-b0d9394718f5fa76dc0d"></a>

**270° CCW: unverified** — `in_game_route_query-b0d9394718f5fa76dc0d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3</summary>

<a id="case-in_game_route_query-caa2b1107fecb68b15ea"></a>

**0° CCW: unverified** — `in_game_route_query-caa2b1107fecb68b15ea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-33f82282cfdde948700f"></a>

**90° CCW: unverified** — `in_game_route_query-33f82282cfdde948700f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-497804a4bc73496cdf09"></a>

**180° CCW: unverified** — `in_game_route_query-497804a4bc73496cdf09`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-5473dfbcc88973588a07"></a>

**270° CCW: unverified** — `in_game_route_query-5473dfbcc88973588a07`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-1d9e1e2ce788a06a8921">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cd9e80a256b646b18e1f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e635eff14e7ee7b52318">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b0d9394718f5fa76dc0d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3 | — | <a href="#case-in_game_visible_travel-caa2b1107fecb68b15ea">[ ] unverified</a> | <a href="#case-in_game_visible_travel-33f82282cfdde948700f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-497804a4bc73496cdf09">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5473dfbcc88973588a07">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-1d9e1e2ce788a06a8921"></a>

**0° CCW: unverified** — `in_game_visible_travel-1d9e1e2ce788a06a8921`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-cd9e80a256b646b18e1f"></a>

**90° CCW: unverified** — `in_game_visible_travel-cd9e80a256b646b18e1f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-e635eff14e7ee7b52318"></a>

**180° CCW: unverified** — `in_game_visible_travel-e635eff14e7ee7b52318`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-b0d9394718f5fa76dc0d"></a>

**270° CCW: unverified** — `in_game_visible_travel-b0d9394718f5fa76dc0d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3</summary>

<a id="case-in_game_visible_travel-caa2b1107fecb68b15ea"></a>

**0° CCW: unverified** — `in_game_visible_travel-caa2b1107fecb68b15ea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-33f82282cfdde948700f"></a>

**90° CCW: unverified** — `in_game_visible_travel-33f82282cfdde948700f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-497804a4bc73496cdf09"></a>

**180° CCW: unverified** — `in_game_visible_travel-497804a4bc73496cdf09`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-5473dfbcc88973588a07"></a>

**270° CCW: unverified** — `in_game_visible_travel-5473dfbcc88973588a07`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d276541958fa97f6b86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fc1b695267485bda2ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c81a7672c537a96ece85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7269027399b48ec45aba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4b8730eef9709bd4fbb2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0500f4fec7a1a548de23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42ba7df9c8e9d3bbd9e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98e50c40096704cf902d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d276541958fa97f6b86"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d276541958fa97f6b86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fc1b695267485bda2ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1fc1b695267485bda2ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c81a7672c537a96ece85"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c81a7672c537a96ece85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7269027399b48ec45aba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7269027399b48ec45aba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4b8730eef9709bd4fbb2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4b8730eef9709bd4fbb2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0500f4fec7a1a548de23"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0500f4fec7a1a548de23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42ba7df9c8e9d3bbd9e3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42ba7df9c8e9d3bbd9e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98e50c40096704cf902d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-98e50c40096704cf902d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-lower-exit-compact:canonical-southeast | <a href="#case-preview_review-bdf883373ac14285174a">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-lower-exit-compact:canonical-top | <a href="#case-preview_review-1f155c32a51061bc1806">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-lower-exit-compact:connection-overview | <a href="#case-preview_review-1120a00a57d4cd09bd1f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-exit-compact:canonical-southeast</summary>

<a id="case-preview_review-bdf883373ac14285174a"></a>

**General: unverified** — `preview_review-bdf883373ac14285174a`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-exit-compact:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-exit-compact:canonical-top</summary>

<a id="case-preview_review-1f155c32a51061bc1806"></a>

**General: unverified** — `preview_review-1f155c32a51061bc1806`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-exit-compact:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-exit-compact:connection-overview</summary>

<a id="case-preview_review-1120a00a57d4cd09bd1f"></a>

**General: unverified** — `preview_review-1120a00a57d4cd09bd1f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-exit-compact:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The previous experimental stamp included curved branch throats and six extra wing cells. The corrected partition keeps a straight 21-cell stamp, transfers those six construction cells to full ramp owners, and moves all curved high-throat faces into the separately placed ramps. The independent partition audit preserves assembled geometry, UVs, materials, winding, and traffic routes, subject only to the exact float32 re-encoding required by a changed model anchor. Earlier renders and game observations do not approve this corrected ownership split.
