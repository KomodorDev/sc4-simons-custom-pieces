---
title: "Testing: RHW Ramp — Lower Full Exit Ramp — R40"
summary: "Check this exact component's traffic ownership, complete physical geometry, and scoped game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — Lower Full Exit Ramp — R40

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-lower-exit-r40` resources and the matching complete [assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). This lower ramp has four traffic ports and two intrinsic route fragments. An intrinsic fragment is the part of a traffic journey stored within this one piece. Between those fragments, the route crosses a highway-owned tile in the stamp. The visible ramp is continuous, but cars need the correctly placed stamp to join the fragments; the matrix does not promise a complete isolated highway-to-Avenue journey.

A **PATH** is a saved traffic-route resource, and an **S3D** is the visible model made from indexed triangles. Model faces can extend beyond the tiles that store this piece's PATHs. A flat physical cut at the native highway edge is different from the traffic connection at a city-tile edge. Check both, rather than assuming that one card describes the entire physical opening.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -12.231458, 0.0]; [-1.0, 0.0]; 0.0 | `path-interface-0fdd8de01bc6c8b7b1c8` |
| `1-E-in-2` | road / 1 / primary | in | [24.0, -10.207444, 6.745132]; [-0.9793492239542134, -0.20217590741797095]; -0.226757443 | `path-interface-daca863776677fe500f2` |
| `1-S-out-3` | road / 1 / primary | out | [33.960601, -8.0, 7.5]; [-0.9691702085915177, -0.2463921808391532]; 0.0 | `path-interface-3dcc6d5eb15355745274` |
| `1-E-in-4` | road / 1 / primary | in | [40.0, -6.634072, 7.5]; [-0.9935463584813209, -0.11342677615319352]; 0.0 | `path-interface-34a26816572a48081146` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-E-in-2` → `1-W-out-1` | primary |
| road | `1-E-in-4` → `1-S-out-3` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-E-in-2` | road / `1-S-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-E-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-lower-exit-r40/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-lower-exit-r40/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-1ed9103c3225850456a3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-1ed9103c3225850456a3"></a>

**General: unverified** — `software_resources-1ed9103c3225850456a3`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-1ed9103c3225850456a3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-1ed9103c3225850456a3"></a>

**General: unverified** — `software_connectivity-1ed9103c3225850456a3`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-fc5b6fafec8da0bf6d22">[ ] unverified</a> | <a href="#case-in_game_render-ce3070d5fc59a7ece4ca">[ ] unverified</a> | <a href="#case-in_game_render-ef18c83f4d8317a15d48">[ ] unverified</a> | <a href="#case-in_game_render-1b9e084bb42ad3eed892">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-fc5b6fafec8da0bf6d22"></a>

**0° CCW: unverified** — `in_game_render-fc5b6fafec8da0bf6d22`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ce3070d5fc59a7ece4ca"></a>

**90° CCW: unverified** — `in_game_render-ce3070d5fc59a7ece4ca`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ef18c83f4d8317a15d48"></a>

**180° CCW: unverified** — `in_game_render-ef18c83f4d8317a15d48`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1b9e084bb42ad3eed892"></a>

**270° CCW: unverified** — `in_game_render-1b9e084bb42ad3eed892`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-fc5b6fafec8da0bf6d22">[ ] unverified</a> | <a href="#case-in_game_placement-ce3070d5fc59a7ece4ca">[ ] unverified</a> | <a href="#case-in_game_placement-ef18c83f4d8317a15d48">[ ] unverified</a> | <a href="#case-in_game_placement-1b9e084bb42ad3eed892">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-fc5b6fafec8da0bf6d22"></a>

**0° CCW: unverified** — `in_game_placement-fc5b6fafec8da0bf6d22`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ce3070d5fc59a7ece4ca"></a>

**90° CCW: unverified** — `in_game_placement-ce3070d5fc59a7ece4ca`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ef18c83f4d8317a15d48"></a>

**180° CCW: unverified** — `in_game_placement-ef18c83f4d8317a15d48`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1b9e084bb42ad3eed892"></a>

**270° CCW: unverified** — `in_game_placement-1b9e084bb42ad3eed892`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-fc5b6fafec8da0bf6d22">[ ] unverified</a> | <a href="#case-in_game_demolition-ce3070d5fc59a7ece4ca">[ ] unverified</a> | <a href="#case-in_game_demolition-ef18c83f4d8317a15d48">[ ] unverified</a> | <a href="#case-in_game_demolition-1b9e084bb42ad3eed892">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-fc5b6fafec8da0bf6d22"></a>

**0° CCW: unverified** — `in_game_demolition-fc5b6fafec8da0bf6d22`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ce3070d5fc59a7ece4ca"></a>

**90° CCW: unverified** — `in_game_demolition-ce3070d5fc59a7ece4ca`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ef18c83f4d8317a15d48"></a>

**180° CCW: unverified** — `in_game_demolition-ef18c83f4d8317a15d48`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1b9e084bb42ad3eed892"></a>

**270° CCW: unverified** — `in_game_demolition-1b9e084bb42ad3eed892`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-fc5b6fafec8da0bf6d22">[ ] unverified</a> | <a href="#case-in_game_save_reload-ce3070d5fc59a7ece4ca">[ ] unverified</a> | <a href="#case-in_game_save_reload-ef18c83f4d8317a15d48">[ ] unverified</a> | <a href="#case-in_game_save_reload-1b9e084bb42ad3eed892">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-fc5b6fafec8da0bf6d22"></a>

**0° CCW: unverified** — `in_game_save_reload-fc5b6fafec8da0bf6d22`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ce3070d5fc59a7ece4ca"></a>

**90° CCW: unverified** — `in_game_save_reload-ce3070d5fc59a7ece4ca`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ef18c83f4d8317a15d48"></a>

**180° CCW: unverified** — `in_game_save_reload-ef18c83f4d8317a15d48`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1b9e084bb42ad3eed892"></a>

**270° CCW: unverified** — `in_game_save_reload-1b9e084bb42ad3eed892`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-d68e09c23fa21177c79f">[ ] unverified</a> | <a href="#case-in_game_route_query-8d81904fa5436610b291">[ ] unverified</a> | <a href="#case-in_game_route_query-e7f74d8e90c337f4a63b">[ ] unverified</a> | <a href="#case-in_game_route_query-c376e935e692fea9867b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3 | — | <a href="#case-in_game_route_query-bea74c1f32365f6d9586">[ ] unverified</a> | <a href="#case-in_game_route_query-f854a437581c8c8a72c1">[ ] unverified</a> | <a href="#case-in_game_route_query-88e3991641aa83ba82c5">[ ] unverified</a> | <a href="#case-in_game_route_query-d827a1629ddc6d9bb5b9">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-d68e09c23fa21177c79f"></a>

**0° CCW: unverified** — `in_game_route_query-d68e09c23fa21177c79f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-8d81904fa5436610b291"></a>

**90° CCW: unverified** — `in_game_route_query-8d81904fa5436610b291`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-e7f74d8e90c337f4a63b"></a>

**180° CCW: unverified** — `in_game_route_query-e7f74d8e90c337f4a63b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-c376e935e692fea9867b"></a>

**270° CCW: unverified** — `in_game_route_query-c376e935e692fea9867b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3</summary>

<a id="case-in_game_route_query-bea74c1f32365f6d9586"></a>

**0° CCW: unverified** — `in_game_route_query-bea74c1f32365f6d9586`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-f854a437581c8c8a72c1"></a>

**90° CCW: unverified** — `in_game_route_query-f854a437581c8c8a72c1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-88e3991641aa83ba82c5"></a>

**180° CCW: unverified** — `in_game_route_query-88e3991641aa83ba82c5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_route_query-d827a1629ddc6d9bb5b9"></a>

**270° CCW: unverified** — `in_game_route_query-d827a1629ddc6d9bb5b9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-d68e09c23fa21177c79f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8d81904fa5436610b291">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e7f74d8e90c337f4a63b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c376e935e692fea9867b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3 | — | <a href="#case-in_game_visible_travel-bea74c1f32365f6d9586">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f854a437581c8c8a72c1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-88e3991641aa83ba82c5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d827a1629ddc6d9bb5b9">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-d68e09c23fa21177c79f"></a>

**0° CCW: unverified** — `in_game_visible_travel-d68e09c23fa21177c79f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-8d81904fa5436610b291"></a>

**90° CCW: unverified** — `in_game_visible_travel-8d81904fa5436610b291`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-e7f74d8e90c337f4a63b"></a>

**180° CCW: unverified** — `in_game_visible_travel-e7f74d8e90c337f4a63b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-c376e935e692fea9867b"></a>

**270° CCW: unverified** — `in_game_visible_travel-c376e935e692fea9867b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-2>1-W-out-1; entry: 1-E-in-2; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3</summary>

<a id="case-in_game_visible_travel-bea74c1f32365f6d9586"></a>

**0° CCW: unverified** — `in_game_visible_travel-bea74c1f32365f6d9586`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-f854a437581c8c8a72c1"></a>

**90° CCW: unverified** — `in_game_visible_travel-f854a437581c8c8a72c1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-88e3991641aa83ba82c5"></a>

**180° CCW: unverified** — `in_game_visible_travel-88e3991641aa83ba82c5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-d827a1629ddc6d9bb5b9"></a>

**270° CCW: unverified** — `in_game_visible_travel-d827a1629ddc6d9bb5b9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-E-in-4>1-S-out-3; entry: 1-E-in-4; exit: 1-S-out-3.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6a16358fecd6bd3b2c4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac1b3110e01286248f17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-824be68562036aad94ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0156bce6b00a47f7be8f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d5fb538e55eece304325">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ea39e2d55af6439b995">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ac2e14443adb18bdcb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3ab598ba0e30767e727">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6a16358fecd6bd3b2c4a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6a16358fecd6bd3b2c4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac1b3110e01286248f17"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ac1b3110e01286248f17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-824be68562036aad94ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-824be68562036aad94ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0156bce6b00a47f7be8f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0156bce6b00a47f7be8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-2; to port: 1-S-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d5fb538e55eece304325"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d5fb538e55eece304325`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ea39e2d55af6439b995"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0ea39e2d55af6439b995`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ac2e14443adb18bdcb9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ac2e14443adb18bdcb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3ab598ba0e30767e727"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e3ab598ba0e30767e727`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-E-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-lower-exit-r40:canonical-southeast | <a href="#case-preview_review-0290e91f19e80cb19d57">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-lower-exit-r40:canonical-top | <a href="#case-preview_review-f1d5988f28423a58b712">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-lower-exit-r40:connection-overview | <a href="#case-preview_review-e30c01e895dd9b145230">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-exit-r40:canonical-southeast</summary>

<a id="case-preview_review-0290e91f19e80cb19d57"></a>

**General: unverified** — `preview_review-0290e91f19e80cb19d57`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-exit-r40:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-exit-r40:canonical-top</summary>

<a id="case-preview_review-f1d5988f28423a58b712"></a>

**General: unverified** — `preview_review-f1d5988f28423a58b712`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-exit-r40:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-lower-exit-r40:connection-overview</summary>

<a id="case-preview_review-e30c01e895dd9b145230"></a>

**General: unverified** — `preview_review-e30c01e895dd9b145230`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-lower-exit-r40:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The previous experimental stamp included curved branch throats and six extra wing cells. The corrected partition keeps a straight 21-cell stamp, transfers those six construction cells to full ramp owners, and moves all curved high-throat faces into the separately placed ramps. The independent partition audit preserves assembled geometry, UVs, materials, winding, and traffic routes, subject only to the exact float32 re-encoding required by a changed model anchor. Earlier renders and game observations do not approve this corrected ownership split.
