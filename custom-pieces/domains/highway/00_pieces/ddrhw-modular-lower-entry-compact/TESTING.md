---
title: "Testing: RHW Ramp — Lower Full Entry Ramp — Compact"
summary: "Check this exact component's traffic ownership, complete physical geometry, and scoped game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — Lower Full Entry Ramp — Compact

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-lower-entry-compact` resources and the matching complete [assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). This lower ramp has four traffic ports and two intrinsic route fragments. An intrinsic fragment is the part of a traffic journey stored within this one piece. Between those fragments, the route crosses a highway-owned tile in the stamp. The visible ramp is continuous, but cars need the correctly placed stamp to join the fragments; the matrix does not promise a complete isolated highway-to-Avenue journey.

A **PATH** is a saved traffic-route resource, and an **S3D** is the visible model made from indexed triangles. Model faces can extend beyond the tiles that store this piece's PATHs. A flat physical cut at the native highway edge is different from the traffic connection at a city-tile edge. Check both, rather than assuming that one card describes the entire physical opening.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-S-out-1` | road / 1 / primary | out | [6.634072, -24.0, 7.5]; [-0.11342677615319352, -0.9935463584813209]; 0.0 | `path-interface-80baad95505e6e935a1d` |
| `1-E-in-2` | road / 1 / primary | in | [8.0, -17.960601, 7.5]; [-0.24639218083915987, -0.969170208591516]; 0.0 | `path-interface-d227520a15c3abcdb327` |
| `1-S-out-3` | road / 1 / primary | out | [10.207444, -8.0, 6.745132]; [-0.2021759074179693, -0.9793492239542138]; 0.226757443 | `path-interface-ac5ba964cbefb6350eb2` |
| `1-N-in-4` | road / 1 / primary | in | [14.245568, 8.0, 3.000444]; [-0.3292115662354699, -0.9442561859245556]; 0.226761428 | `path-interface-9a0f9ddca22564095128` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-E-in-2` → `1-S-out-1` | primary |
| road | `1-N-in-4` → `1-S-out-3` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-E-in-2` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-S-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-lower-entry-compact/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-lower-entry-compact/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-3e38f76cf5f4eb6b772a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-3e38f76cf5f4eb6b772a"></a>

**General: unverified** — `software_resources-3e38f76cf5f4eb6b772a`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-3e38f76cf5f4eb6b772a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-3e38f76cf5f4eb6b772a"></a>

**General: unverified** — `software_connectivity-3e38f76cf5f4eb6b772a`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-897f525621f3ffad7ea7">[ ] unverified</a> | <a href="#case-in_game_render-407efd89661715970818">[ ] unverified</a> | <a href="#case-in_game_render-bdda83fd84824f177e2a">[ ] unverified</a> | <a href="#case-in_game_render-90a856ed16ca8c1c24ef">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-897f525621f3ffad7ea7"></a>

**0° CCW: unverified** — `in_game_render-897f525621f3ffad7ea7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-407efd89661715970818"></a>

**90° CCW: unverified** — `in_game_render-407efd89661715970818`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-bdda83fd84824f177e2a"></a>

**180° CCW: unverified** — `in_game_render-bdda83fd84824f177e2a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-90a856ed16ca8c1c24ef"></a>

**270° CCW: unverified** — `in_game_render-90a856ed16ca8c1c24ef`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-897f525621f3ffad7ea7">[ ] unverified</a> | <a href="#case-in_game_placement-407efd89661715970818">[ ] unverified</a> | <a href="#case-in_game_placement-bdda83fd84824f177e2a">[ ] unverified</a> | <a href="#case-in_game_placement-90a856ed16ca8c1c24ef">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-897f525621f3ffad7ea7"></a>

**0° CCW: unverified** — `in_game_placement-897f525621f3ffad7ea7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-407efd89661715970818"></a>

**90° CCW: unverified** — `in_game_placement-407efd89661715970818`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-bdda83fd84824f177e2a"></a>

**180° CCW: unverified** — `in_game_placement-bdda83fd84824f177e2a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-90a856ed16ca8c1c24ef"></a>

**270° CCW: unverified** — `in_game_placement-90a856ed16ca8c1c24ef`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-897f525621f3ffad7ea7">[ ] unverified</a> | <a href="#case-in_game_demolition-407efd89661715970818">[ ] unverified</a> | <a href="#case-in_game_demolition-bdda83fd84824f177e2a">[ ] unverified</a> | <a href="#case-in_game_demolition-90a856ed16ca8c1c24ef">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-897f525621f3ffad7ea7"></a>

**0° CCW: unverified** — `in_game_demolition-897f525621f3ffad7ea7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-407efd89661715970818"></a>

**90° CCW: unverified** — `in_game_demolition-407efd89661715970818`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-bdda83fd84824f177e2a"></a>

**180° CCW: unverified** — `in_game_demolition-bdda83fd84824f177e2a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-90a856ed16ca8c1c24ef"></a>

**270° CCW: unverified** — `in_game_demolition-90a856ed16ca8c1c24ef`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-897f525621f3ffad7ea7">[ ] unverified</a> | <a href="#case-in_game_save_reload-407efd89661715970818">[ ] unverified</a> | <a href="#case-in_game_save_reload-bdda83fd84824f177e2a">[ ] unverified</a> | <a href="#case-in_game_save_reload-90a856ed16ca8c1c24ef">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-897f525621f3ffad7ea7"></a>

**0° CCW: unverified** — `in_game_save_reload-897f525621f3ffad7ea7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-407efd89661715970818"></a>

**90° CCW: unverified** — `in_game_save_reload-407efd89661715970818`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-bdda83fd84824f177e2a"></a>

**180° CCW: unverified** — `in_game_save_reload-bdda83fd84824f177e2a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-90a856ed16ca8c1c24ef"></a>

**270° CCW: unverified** — `in_game_save_reload-90a856ed16ca8c1c24ef`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1 | — | <a href="#case-in_game_route_query-6954a9fbd776b27d426e">[ ] unverified</a> | <a href="#case-in_game_route_query-d69e7fd64c924d243e42">[ ] unverified</a> | <a href="#case-in_game_route_query-bc3f1f35640e3f4627fe">[ ] unverified</a> | <a href="#case-in_game_route_query-d524bd2e971841809206">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3 | — | <a href="#case-in_game_route_query-c86ca710dad4239c9d0d">[ ] unverified</a> | <a href="#case-in_game_route_query-7568354ea824699171a6">[ ] unverified</a> | <a href="#case-in_game_route_query-02f559762d9cfd8fe512">[ ] unverified</a> | <a href="#case-in_game_route_query-5bc063559ee5c253001a">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1</summary>

<a id="case-in_game_route_query-6954a9fbd776b27d426e"></a>

**0° CCW: unverified** — `in_game_route_query-6954a9fbd776b27d426e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-d69e7fd64c924d243e42"></a>

**90° CCW: unverified** — `in_game_route_query-d69e7fd64c924d243e42`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-bc3f1f35640e3f4627fe"></a>

**180° CCW: unverified** — `in_game_route_query-bc3f1f35640e3f4627fe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_route_query-d524bd2e971841809206"></a>

**270° CCW: unverified** — `in_game_route_query-d524bd2e971841809206`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3</summary>

<a id="case-in_game_route_query-c86ca710dad4239c9d0d"></a>

**0° CCW: unverified** — `in_game_route_query-c86ca710dad4239c9d0d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-7568354ea824699171a6"></a>

**90° CCW: unverified** — `in_game_route_query-7568354ea824699171a6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-02f559762d9cfd8fe512"></a>

**180° CCW: unverified** — `in_game_route_query-02f559762d9cfd8fe512`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-5bc063559ee5c253001a"></a>

**270° CCW: unverified** — `in_game_route_query-5bc063559ee5c253001a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1 | — | <a href="#case-in_game_visible_travel-6954a9fbd776b27d426e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d69e7fd64c924d243e42">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bc3f1f35640e3f4627fe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d524bd2e971841809206">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3 | — | <a href="#case-in_game_visible_travel-c86ca710dad4239c9d0d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7568354ea824699171a6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-02f559762d9cfd8fe512">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5bc063559ee5c253001a">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1</summary>

<a id="case-in_game_visible_travel-6954a9fbd776b27d426e"></a>

**0° CCW: unverified** — `in_game_visible_travel-6954a9fbd776b27d426e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-d69e7fd64c924d243e42"></a>

**90° CCW: unverified** — `in_game_visible_travel-d69e7fd64c924d243e42`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-bc3f1f35640e3f4627fe"></a>

**180° CCW: unverified** — `in_game_visible_travel-bc3f1f35640e3f4627fe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-d524bd2e971841809206"></a>

**270° CCW: unverified** — `in_game_visible_travel-d524bd2e971841809206`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-S-out-1; entry: 1-E-in-2; exit: 1-S-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3</summary>

<a id="case-in_game_visible_travel-c86ca710dad4239c9d0d"></a>

**0° CCW: unverified** — `in_game_visible_travel-c86ca710dad4239c9d0d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-7568354ea824699171a6"></a>

**90° CCW: unverified** — `in_game_visible_travel-7568354ea824699171a6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-02f559762d9cfd8fe512"></a>

**180° CCW: unverified** — `in_game_visible_travel-02f559762d9cfd8fe512`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-5bc063559ee5c253001a"></a>

**270° CCW: unverified** — `in_game_visible_travel-5bc063559ee5c253001a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-S-out-3; entry: 1-N-in-4; exit: 1-S-out-3.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0fe09b418d6a774e34f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-378341c56ce87089a68e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d85ed45cb8421e1e927">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5a69ca5a4e1689502df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4bb2d8f80e93fed001e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5580ac58f7a8139f68ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fef1bdcb98133bfad0ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-860154502c882e3e34bd">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0fe09b418d6a774e34f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0fe09b418d6a774e34f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-378341c56ce87089a68e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-378341c56ce87089a68e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d85ed45cb8421e1e927"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3d85ed45cb8421e1e927`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5a69ca5a4e1689502df"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5a69ca5a4e1689502df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4bb2d8f80e93fed001e2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4bb2d8f80e93fed001e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5580ac58f7a8139f68ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5580ac58f7a8139f68ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fef1bdcb98133bfad0ed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fef1bdcb98133bfad0ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-860154502c882e3e34bd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-860154502c882e3e34bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-S-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-lower-entry-compact:canonical-southeast | <a href="#case-preview_review-092dcb907cfe74fbed58">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-lower-entry-compact:canonical-top | <a href="#case-preview_review-c883f038ec826603e059">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-lower-entry-compact:connection-overview | <a href="#case-preview_review-50d7f4e64f681afbcf61">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-entry-compact:canonical-southeast</summary>

<a id="case-preview_review-092dcb907cfe74fbed58"></a>

**General: unverified** — `preview_review-092dcb907cfe74fbed58`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-entry-compact:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-entry-compact:canonical-top</summary>

<a id="case-preview_review-c883f038ec826603e059"></a>

**General: unverified** — `preview_review-c883f038ec826603e059`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-entry-compact:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-entry-compact:connection-overview</summary>

<a id="case-preview_review-50d7f4e64f681afbcf61"></a>

**General: unverified** — `preview_review-50d7f4e64f681afbcf61`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-entry-compact:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The previous experimental stamp included curved branch throats and six extra wing cells. The corrected partition keeps a straight 21-cell stamp, transfers those six construction cells to full ramp owners, and moves all curved high-throat faces into the separately placed ramps. The independent partition audit preserves assembled geometry, UVs, materials, winding, and traffic routes, subject only to the exact float32 re-encoding required by a changed model anchor. Earlier renders and game observations do not approve this corrected ownership split.
