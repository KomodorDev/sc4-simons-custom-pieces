---
title: "Testing: RHW Ramp \u2014 L2 Exit Lateral Departure \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: RHW Ramp — L2 Exit Lateral Departure — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **RHW Ramp — L2 Exit Lateral Departure — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-upper-exit-departure`, as **P10** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 1 cells inside its 1 × 1 bounding footprint. Flat lateral departure at 15 m. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-01-in` | road / 1 / primary | in | [-8.0, 7.328254, 15.0]; [0.9918914891233332, 0.12708766189011628]; 0.0 | `path-interface-dfc49a604de1ebc10b30` |
| `channel-02-out` | road / 1 / primary | out | [0.265154, 8.0, 15.0]; [0.9227775912579842, 0.38533299504728746]; 0.0 | `path-interface-2575dc74752582c1c38f` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-02-out` | primary |

#### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-upper-exit-departure
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **3,421 indexed triangles** and **1 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

This type’s complete measured ports, movements, channel associations, and saved-chord witnesses are frozen in the [B accepted connector contract](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/checks/accepted-connector-contracts.jsonc). That source passed the independent saved-resource and whole-assembly checks before extraction; the generated views retain their own freshness requirements. Its precise saved grades and separately retained reviewed and sampled tangents follow the [shared precision convention](../../../../docs/CONNECTOR_METADATA.md#5-matching-procedure-and-evidence). Arbitrary-neighbour matching and game operation remain outside that record.

## 4. Game checks

1. Select this exact B type from its assembly cycle, place a fresh copy at the reference coordinate, and inspect its model, markings, barriers, and supports. Repeat proper construction rotations with Home or End; rotating the camera alone is insufficient.
2. Place the matching B neighbours from the assembly plan, connect the required native approaches, and let new traffic enter. Record Route Query separately from an actual car crossing each required join. Check both through decks wherever this type owns their fragments.
3. For ground Avenue ownership, separately inspect changing pavement appearance and moving pedestrians. A ramp driveway crosses its adjacent pedestrian route; road asphalt at that crossing is distinct from a missing sidewalk elsewhere.
4. At Medium and High shadow quality, inspect all camera views and zoom levels for unwanted custom shadows. The source's no-shadow policy is not an observed game result.
5. Save, quit, reload, and repeat representative joins. In a separate saved copy, demolish this component, inspect neighbouring native tiles and attachments, replace it, and retest.

Use the [shared observation procedure](../../../../docs/TESTING.md#4-record-one-observation), recording the exact candidate, component, orientation, neighbours, and environment. Native draggable joins, occupied-neighbour placement, visible traffic, redraw, demolition, and save/reload remain unverified without a matching human observation.

## 5. Results and known issues

This piece passed its saved-resource checks in the first native B build; its [assembly evidence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) records the exact candidate and placed-layout scope. Final connector exports and the assembly-menu package retain their own source fingerprints and checks. **Installation and all game observations remain unverified.** The assembly’s [TESTING document](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/TESTING.md) owns the complete layout’s evidence and limits.

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

Current totals: unverified: 29, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-exit-departure/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-exit-departure/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-261b8c8188f3d84599f4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-261b8c8188f3d84599f4"></a>

**General: unverified** — `software_resources-261b8c8188f3d84599f4`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-261b8c8188f3d84599f4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-261b8c8188f3d84599f4"></a>

**General: unverified** — `software_connectivity-261b8c8188f3d84599f4`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-cfbb8e7cf3dee10b186e">[ ] unverified</a> | <a href="#case-in_game_render-7224647e3932f0174266">[ ] unverified</a> | <a href="#case-in_game_render-5787e0e07224e91021a4">[ ] unverified</a> | <a href="#case-in_game_render-8f8f17c5599b99698c2b">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-cfbb8e7cf3dee10b186e"></a>

**0° CCW: unverified** — `in_game_render-cfbb8e7cf3dee10b186e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7224647e3932f0174266"></a>

**90° CCW: unverified** — `in_game_render-7224647e3932f0174266`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5787e0e07224e91021a4"></a>

**180° CCW: unverified** — `in_game_render-5787e0e07224e91021a4`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8f8f17c5599b99698c2b"></a>

**270° CCW: unverified** — `in_game_render-8f8f17c5599b99698c2b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-cfbb8e7cf3dee10b186e">[ ] unverified</a> | <a href="#case-in_game_placement-7224647e3932f0174266">[ ] unverified</a> | <a href="#case-in_game_placement-5787e0e07224e91021a4">[ ] unverified</a> | <a href="#case-in_game_placement-8f8f17c5599b99698c2b">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-cfbb8e7cf3dee10b186e"></a>

**0° CCW: unverified** — `in_game_placement-cfbb8e7cf3dee10b186e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7224647e3932f0174266"></a>

**90° CCW: unverified** — `in_game_placement-7224647e3932f0174266`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5787e0e07224e91021a4"></a>

**180° CCW: unverified** — `in_game_placement-5787e0e07224e91021a4`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8f8f17c5599b99698c2b"></a>

**270° CCW: unverified** — `in_game_placement-8f8f17c5599b99698c2b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-cfbb8e7cf3dee10b186e">[ ] unverified</a> | <a href="#case-in_game_demolition-7224647e3932f0174266">[ ] unverified</a> | <a href="#case-in_game_demolition-5787e0e07224e91021a4">[ ] unverified</a> | <a href="#case-in_game_demolition-8f8f17c5599b99698c2b">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-cfbb8e7cf3dee10b186e"></a>

**0° CCW: unverified** — `in_game_demolition-cfbb8e7cf3dee10b186e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7224647e3932f0174266"></a>

**90° CCW: unverified** — `in_game_demolition-7224647e3932f0174266`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5787e0e07224e91021a4"></a>

**180° CCW: unverified** — `in_game_demolition-5787e0e07224e91021a4`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8f8f17c5599b99698c2b"></a>

**270° CCW: unverified** — `in_game_demolition-8f8f17c5599b99698c2b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-cfbb8e7cf3dee10b186e">[ ] unverified</a> | <a href="#case-in_game_save_reload-7224647e3932f0174266">[ ] unverified</a> | <a href="#case-in_game_save_reload-5787e0e07224e91021a4">[ ] unverified</a> | <a href="#case-in_game_save_reload-8f8f17c5599b99698c2b">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-cfbb8e7cf3dee10b186e"></a>

**0° CCW: unverified** — `in_game_save_reload-cfbb8e7cf3dee10b186e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7224647e3932f0174266"></a>

**90° CCW: unverified** — `in_game_save_reload-7224647e3932f0174266`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5787e0e07224e91021a4"></a>

**180° CCW: unverified** — `in_game_save_reload-5787e0e07224e91021a4`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8f8f17c5599b99698c2b"></a>

**270° CCW: unverified** — `in_game_save_reload-8f8f17c5599b99698c2b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out | — | <a href="#case-in_game_route_query-dcbcdb47038fcd280c19">[ ] unverified</a> | <a href="#case-in_game_route_query-7212a44a7004c3c75f25">[ ] unverified</a> | <a href="#case-in_game_route_query-37df436f7faf8462a7f0">[ ] unverified</a> | <a href="#case-in_game_route_query-5805ba90552015236e3f">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out</summary>

<a id="case-in_game_route_query-dcbcdb47038fcd280c19"></a>

**0° CCW: unverified** — `in_game_route_query-dcbcdb47038fcd280c19`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_route_query-7212a44a7004c3c75f25"></a>

**90° CCW: unverified** — `in_game_route_query-7212a44a7004c3c75f25`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_route_query-37df436f7faf8462a7f0"></a>

**180° CCW: unverified** — `in_game_route_query-37df436f7faf8462a7f0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_route_query-5805ba90552015236e3f"></a>

**270° CCW: unverified** — `in_game_route_query-5805ba90552015236e3f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out | — | <a href="#case-in_game_visible_travel-dcbcdb47038fcd280c19">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7212a44a7004c3c75f25">[ ] unverified</a> | <a href="#case-in_game_visible_travel-37df436f7faf8462a7f0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5805ba90552015236e3f">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out</summary>

<a id="case-in_game_visible_travel-dcbcdb47038fcd280c19"></a>

**0° CCW: unverified** — `in_game_visible_travel-dcbcdb47038fcd280c19`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-7212a44a7004c3c75f25"></a>

**90° CCW: unverified** — `in_game_visible_travel-7212a44a7004c3c75f25`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-37df436f7faf8462a7f0"></a>

**180° CCW: unverified** — `in_game_visible_travel-37df436f7faf8462a7f0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-5805ba90552015236e3f"></a>

**270° CCW: unverified** — `in_game_visible_travel-5805ba90552015236e3f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-02-out; entry: channel-01-in; exit: channel-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-departure:canonical-southeast | <a href="#case-preview_review-a2ca6e2493e99394a64d">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-departure:canonical-top | <a href="#case-preview_review-612d31205760ac2c3f2b">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-departure:connection-overview | <a href="#case-preview_review-9ce0e3edd933945cf4df">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-departure:canonical-southeast</summary>

<a id="case-preview_review-a2ca6e2493e99394a64d"></a>

**General: unverified** — `preview_review-a2ca6e2493e99394a64d`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-departure:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-departure:canonical-top</summary>

<a id="case-preview_review-612d31205760ac2c3f2b"></a>

**General: unverified** — `preview_review-612d31205760ac2c3f2b`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-departure:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-departure:connection-overview</summary>

<a id="case-preview_review-9ce0e3edd933945cf4df"></a>

**General: unverified** — `preview_review-9ce0e3edd933945cf4df`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-departure:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the departure function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
