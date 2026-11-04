---
title: "Testing: DD RHW-4 \u2014 L1/L2 \u2194 RHW-4 L0 \u2014 Orthogonal Transition \u2014 Lower Deck Bends Right \u2014 6 Tiles"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Orthogonal Transition — Lower Deck Bends Right — 6 Tiles

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Check this exact straight-approach adapter with the lower road bending right. It must expose one DD boundary and two ground boundaries, each with the directed lane services in the [placement table](README.md#21-reserve-the-footprint-and-its-native-connections).

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `lower-lane-01-out` | road / 1 / primary | out | [-2.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-a980347eab2bc32dd576` |
| `lower-lane-02-out` | road / 1 / primary | out | [2.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-3cd860990d731c95fb5e` |
| `upper-lane-02-in` | road / 1 / primary | in | [13.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-d977a84d7a911bc0048d` |
| `lower-lane-01-in` | road / 1 / primary | in | [13.5, 8.0, 7.5]; [0.0, -1.0]; 0.0 | `path-interface-b2fe320b9e0bb31bdb27` |
| `upper-lane-02-out` | road / 1 / primary | out | [13.5, 8.0, 15.0]; [0.0, 1.0]; 0.0 | `path-interface-02def3c4ce1dd299e969` |
| `upper-lane-01-in` | road / 1 / primary | in | [18.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-57700a60d1579dc24dce` |
| `lower-lane-02-in` | road / 1 / primary | in | [18.5, 8.0, 7.5]; [0.0, -1.0]; 0.0 | `path-interface-fddc704c2b84d595ec6f` |
| `upper-lane-01-out` | road / 1 / primary | out | [18.5, 8.0, 15.0]; [0.0, 1.0]; 0.0 | `path-interface-991f143956c37b818e99` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `upper-lane-02-in` → `upper-lane-02-out` | primary |
| road | `lower-lane-01-in` → `lower-lane-01-out` | primary |
| road | `upper-lane-01-in` → `upper-lane-01-out` | primary |
| road | `lower-lane-02-in` → `lower-lane-02-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `upper-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the audited NAM 50 right-hand traffic inputs and a disposable flat city. Close and restart SimCity 4 around installation, and use fresh placements so each case checks the current candidate. Leave the two-by-six core, three ordinary socket tiles, and the continuing approaches clear. Record the SimCity 4 version, whether it runs directly or through Wine, the installed candidate, and the placement rotation.

## 3. Software checks

From the repository root, activate the environment described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md#3-prepare-local-development-inputs). The first command builds only this piece. The second reads the saved DAT archives and verifies their construction rules, models, and traffic paths.

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
```

Replace `BUILD_NAME` with the same unused name in both commands. Check all four rotations, eight native lane endpoints, four complete same-lane journeys, twelve forbidden transfers, individual lane grades, fourteen support solids, and clearance around both roads. A **grade** measures height change divided by horizontal distance, so 20% means 2 m of height change over 10 m horizontally. The ceiling applies to each individual lane.

## 4. Game checks

1. Follow the [placement steps](README.md#22-place-and-connect-the-adapter) and repeat the placement in all four rotations. Check the terrain under the core and the level of all three connections.
2. Draw outward from each ordinary socket with **RealHighway (RHW-2)**. For a separate control, choose **RealHighway (RHW) Starter Pieces**. Select **Double-Decker RHW-4 Starter Piece (Upper Deck: Level 2, Lower Deck: Level 1)** for the DD road and **RHW-4 Starter Piece** for each ground road. Build the matching directions first, place the adapter with short gaps, and drag inward from each existing road to its socket. Try a third fresh placement beside completed matching approaches. Record the gaps, rotation, and any terrain change.
3. Run traffic through both lanes of each carriageway. Use **Route Query** to check each displayed path, then watch a vehicle complete each journey. Check yellow on the driver’s left, the join paint and pavement, and shadows at Medium and High settings. Save, reopen, and check the same placement.

## 5. Results and known issues

The [saved native verification](evidence/saved-native-verification.jsonc) checks all four directed lane journeys, eight native end members in four rotations, and all twelve owned tiles. The maximum saved lane grade is 19.23077%. The source profile’s lower-lane peak is 15.58%. The original NAM continuation rules and all eight required native lookup rows were verified from the pinned inputs.

The saved model check covers 45,754 indexed triangles, fourteen closed support solids, and 1,546 lane segments against a 2.5 m wide × 3.8 m high vehicle envelope. It checks both complete decks and their barriers for clearance. The surface comparison excluded one zero- or sub-float32-area face under its declared tolerance. The piece has 3 m flat collars at all three external joins.

The [saved marking samples](evidence/native-markings-verification.jsonc) place yellow to the driver’s left in all twelve samples across the four lanes. Reversing the lateral texture coordinates in either the native collars or the generated atlas fails the corresponding control. The [angled](evidence/preview.json), [top](evidence/preview-top.json), and [connector overview](evidence/connection-overview.json) reports identify the same saved DAT. Game observations are pending. Record the exact placement, drawing order, lane, rotation, and game version for each result.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-3d9a4da4d5d226d7de21">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-3d9a4da4d5d226d7de21"></a>

**General: unverified** — `software_resources-3d9a4da4d5d226d7de21`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-3d9a4da4d5d226d7de21">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-3d9a4da4d5d226d7de21"></a>

**General: unverified** — `software_connectivity-3d9a4da4d5d226d7de21`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-e1b983b35394cf18a4fe">[ ] unverified</a> | <a href="#case-in_game_render-642fd3692ab541387b80">[ ] unverified</a> | <a href="#case-in_game_render-50f47f5a8f7e8ed79956">[ ] unverified</a> | <a href="#case-in_game_render-4530e5a10fd0d78b80ee">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-e1b983b35394cf18a4fe"></a>

**0° CCW: unverified** — `in_game_render-e1b983b35394cf18a4fe`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-642fd3692ab541387b80"></a>

**90° CCW: unverified** — `in_game_render-642fd3692ab541387b80`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-50f47f5a8f7e8ed79956"></a>

**180° CCW: unverified** — `in_game_render-50f47f5a8f7e8ed79956`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-4530e5a10fd0d78b80ee"></a>

**270° CCW: unverified** — `in_game_render-4530e5a10fd0d78b80ee`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-e1b983b35394cf18a4fe">[ ] unverified</a> | <a href="#case-in_game_placement-642fd3692ab541387b80">[ ] unverified</a> | <a href="#case-in_game_placement-50f47f5a8f7e8ed79956">[ ] unverified</a> | <a href="#case-in_game_placement-4530e5a10fd0d78b80ee">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-e1b983b35394cf18a4fe"></a>

**0° CCW: unverified** — `in_game_placement-e1b983b35394cf18a4fe`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-642fd3692ab541387b80"></a>

**90° CCW: unverified** — `in_game_placement-642fd3692ab541387b80`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-50f47f5a8f7e8ed79956"></a>

**180° CCW: unverified** — `in_game_placement-50f47f5a8f7e8ed79956`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-4530e5a10fd0d78b80ee"></a>

**270° CCW: unverified** — `in_game_placement-4530e5a10fd0d78b80ee`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-e1b983b35394cf18a4fe">[ ] unverified</a> | <a href="#case-in_game_demolition-642fd3692ab541387b80">[ ] unverified</a> | <a href="#case-in_game_demolition-50f47f5a8f7e8ed79956">[ ] unverified</a> | <a href="#case-in_game_demolition-4530e5a10fd0d78b80ee">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-e1b983b35394cf18a4fe"></a>

**0° CCW: unverified** — `in_game_demolition-e1b983b35394cf18a4fe`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-642fd3692ab541387b80"></a>

**90° CCW: unverified** — `in_game_demolition-642fd3692ab541387b80`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-50f47f5a8f7e8ed79956"></a>

**180° CCW: unverified** — `in_game_demolition-50f47f5a8f7e8ed79956`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-4530e5a10fd0d78b80ee"></a>

**270° CCW: unverified** — `in_game_demolition-4530e5a10fd0d78b80ee`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-e1b983b35394cf18a4fe">[ ] unverified</a> | <a href="#case-in_game_save_reload-642fd3692ab541387b80">[ ] unverified</a> | <a href="#case-in_game_save_reload-50f47f5a8f7e8ed79956">[ ] unverified</a> | <a href="#case-in_game_save_reload-4530e5a10fd0d78b80ee">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-e1b983b35394cf18a4fe"></a>

**0° CCW: unverified** — `in_game_save_reload-e1b983b35394cf18a4fe`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-642fd3692ab541387b80"></a>

**90° CCW: unverified** — `in_game_save_reload-642fd3692ab541387b80`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-50f47f5a8f7e8ed79956"></a>

**180° CCW: unverified** — `in_game_save_reload-50f47f5a8f7e8ed79956`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-4530e5a10fd0d78b80ee"></a>

**270° CCW: unverified** — `in_game_save_reload-4530e5a10fd0d78b80ee`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_route_query-d975ff161877122f0e6b">[ ] unverified</a> | <a href="#case-in_game_route_query-059add34adf294436fb9">[ ] unverified</a> | <a href="#case-in_game_route_query-de75eebe546b40d70a11">[ ] unverified</a> | <a href="#case-in_game_route_query-34de88b0b7c714ddff60">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_route_query-888411b03dfe135c6417">[ ] unverified</a> | <a href="#case-in_game_route_query-ee690ae1c453e8a3423f">[ ] unverified</a> | <a href="#case-in_game_route_query-1f3c999068beeba19ba4">[ ] unverified</a> | <a href="#case-in_game_route_query-029ff53f28a532fcee1a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_route_query-8981e36a8ece06e4af42">[ ] unverified</a> | <a href="#case-in_game_route_query-9ff0e2afe57233f47794">[ ] unverified</a> | <a href="#case-in_game_route_query-db897b1483861eec17f4">[ ] unverified</a> | <a href="#case-in_game_route_query-425d8b28448be664c77f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_route_query-57b41bf7628a8bfe3087">[ ] unverified</a> | <a href="#case-in_game_route_query-0f714495a35403e776e0">[ ] unverified</a> | <a href="#case-in_game_route_query-dab27ebd3518fd4c90ca">[ ] unverified</a> | <a href="#case-in_game_route_query-db966cbc1f7777e38e33">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_route_query-d975ff161877122f0e6b"></a>

**0° CCW: unverified** — `in_game_route_query-d975ff161877122f0e6b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-059add34adf294436fb9"></a>

**90° CCW: unverified** — `in_game_route_query-059add34adf294436fb9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-de75eebe546b40d70a11"></a>

**180° CCW: unverified** — `in_game_route_query-de75eebe546b40d70a11`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-34de88b0b7c714ddff60"></a>

**270° CCW: unverified** — `in_game_route_query-34de88b0b7c714ddff60`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_route_query-888411b03dfe135c6417"></a>

**0° CCW: unverified** — `in_game_route_query-888411b03dfe135c6417`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-ee690ae1c453e8a3423f"></a>

**90° CCW: unverified** — `in_game_route_query-ee690ae1c453e8a3423f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-1f3c999068beeba19ba4"></a>

**180° CCW: unverified** — `in_game_route_query-1f3c999068beeba19ba4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-029ff53f28a532fcee1a"></a>

**270° CCW: unverified** — `in_game_route_query-029ff53f28a532fcee1a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_route_query-8981e36a8ece06e4af42"></a>

**0° CCW: unverified** — `in_game_route_query-8981e36a8ece06e4af42`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-9ff0e2afe57233f47794"></a>

**90° CCW: unverified** — `in_game_route_query-9ff0e2afe57233f47794`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-db897b1483861eec17f4"></a>

**180° CCW: unverified** — `in_game_route_query-db897b1483861eec17f4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-425d8b28448be664c77f"></a>

**270° CCW: unverified** — `in_game_route_query-425d8b28448be664c77f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_route_query-57b41bf7628a8bfe3087"></a>

**0° CCW: unverified** — `in_game_route_query-57b41bf7628a8bfe3087`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-0f714495a35403e776e0"></a>

**90° CCW: unverified** — `in_game_route_query-0f714495a35403e776e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-dab27ebd3518fd4c90ca"></a>

**180° CCW: unverified** — `in_game_route_query-dab27ebd3518fd4c90ca`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-db966cbc1f7777e38e33"></a>

**270° CCW: unverified** — `in_game_route_query-db966cbc1f7777e38e33`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_visible_travel-d975ff161877122f0e6b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-059add34adf294436fb9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-de75eebe546b40d70a11">[ ] unverified</a> | <a href="#case-in_game_visible_travel-34de88b0b7c714ddff60">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_visible_travel-888411b03dfe135c6417">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ee690ae1c453e8a3423f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1f3c999068beeba19ba4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-029ff53f28a532fcee1a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_visible_travel-8981e36a8ece06e4af42">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9ff0e2afe57233f47794">[ ] unverified</a> | <a href="#case-in_game_visible_travel-db897b1483861eec17f4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-425d8b28448be664c77f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_visible_travel-57b41bf7628a8bfe3087">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0f714495a35403e776e0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dab27ebd3518fd4c90ca">[ ] unverified</a> | <a href="#case-in_game_visible_travel-db966cbc1f7777e38e33">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_visible_travel-d975ff161877122f0e6b"></a>

**0° CCW: unverified** — `in_game_visible_travel-d975ff161877122f0e6b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-059add34adf294436fb9"></a>

**90° CCW: unverified** — `in_game_visible_travel-059add34adf294436fb9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-de75eebe546b40d70a11"></a>

**180° CCW: unverified** — `in_game_visible_travel-de75eebe546b40d70a11`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-34de88b0b7c714ddff60"></a>

**270° CCW: unverified** — `in_game_visible_travel-34de88b0b7c714ddff60`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_visible_travel-888411b03dfe135c6417"></a>

**0° CCW: unverified** — `in_game_visible_travel-888411b03dfe135c6417`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-ee690ae1c453e8a3423f"></a>

**90° CCW: unverified** — `in_game_visible_travel-ee690ae1c453e8a3423f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-1f3c999068beeba19ba4"></a>

**180° CCW: unverified** — `in_game_visible_travel-1f3c999068beeba19ba4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-029ff53f28a532fcee1a"></a>

**270° CCW: unverified** — `in_game_visible_travel-029ff53f28a532fcee1a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_visible_travel-8981e36a8ece06e4af42"></a>

**0° CCW: unverified** — `in_game_visible_travel-8981e36a8ece06e4af42`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-9ff0e2afe57233f47794"></a>

**90° CCW: unverified** — `in_game_visible_travel-9ff0e2afe57233f47794`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-db897b1483861eec17f4"></a>

**180° CCW: unverified** — `in_game_visible_travel-db897b1483861eec17f4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-425d8b28448be664c77f"></a>

**270° CCW: unverified** — `in_game_visible_travel-425d8b28448be664c77f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_visible_travel-57b41bf7628a8bfe3087"></a>

**0° CCW: unverified** — `in_game_visible_travel-57b41bf7628a8bfe3087`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-0f714495a35403e776e0"></a>

**90° CCW: unverified** — `in_game_visible_travel-0f714495a35403e776e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-dab27ebd3518fd4c90ca"></a>

**180° CCW: unverified** — `in_game_visible_travel-dab27ebd3518fd4c90ca`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-db966cbc1f7777e38e33"></a>

**270° CCW: unverified** — `in_game_visible_travel-db966cbc1f7777e38e33`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a6b5783796057e50879a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16ed9053baf1011b0bb5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acfc531a83d99ff79477">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4de9b607429256ea517c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9d33e0eb8f243e9c533">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a2b8453d9146837b5b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38c87265115e565fd3fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0219108344a6ff69bd40">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-17df8ef27508d53cb3e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad95124948ce5b027f9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91cc3422841f7ad92af0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b61e0204debcfec0cad9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a41fe03dc3b8783406c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5544618a85f97fac02f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56c08d20682bc24a7786">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-299531f11b79c166fe5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ed037450d16112254df8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-212a11cf5fdf561ffcc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11b7ad415cae9521dc83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7935a87d59bc7aed4619">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99ced5bf6cc4f32bd2be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38e7af7bb28198cbc113">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7ba21c0822f4b9ba104">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-557286bd1587b7f6bc58">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d708a283f04a50f2bb37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04b27e4182705e1d3247">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef431e11edd6fbd90964">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f25806d75e9edcd5471f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de73e5c4631cf19c4a0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66063696cef61d59ff58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4f351fd5860c533c912">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2df9448577d8ced1ea3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e3c6bc46e8e5830ea56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b2f2ad1db56d09cddcb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16b141f2bab3e02a1da8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78ad4a4ecad184dbc4f2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b65a851162eff0ffb8a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a53a49da2d55c4ebb4e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-509fff75cd5010b45798">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d70fb70e4f06640a163">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-54dc8461f694f231dd90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a90357040caf828dc70a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0078202ba18193c9736">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ee6e91bfb41e09571ff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8242d42603b9b7aedec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d3d35647954e349282c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65d416b2c40460af6124">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f2e63e449d24f12dbef">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a6b5783796057e50879a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6b5783796057e50879a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16ed9053baf1011b0bb5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-16ed9053baf1011b0bb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acfc531a83d99ff79477"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-acfc531a83d99ff79477`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4de9b607429256ea517c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4de9b607429256ea517c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9d33e0eb8f243e9c533"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9d33e0eb8f243e9c533`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a2b8453d9146837b5b5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8a2b8453d9146837b5b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38c87265115e565fd3fe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-38c87265115e565fd3fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0219108344a6ff69bd40"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0219108344a6ff69bd40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-17df8ef27508d53cb3e3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-17df8ef27508d53cb3e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad95124948ce5b027f9a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ad95124948ce5b027f9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91cc3422841f7ad92af0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-91cc3422841f7ad92af0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b61e0204debcfec0cad9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b61e0204debcfec0cad9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a41fe03dc3b8783406c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a41fe03dc3b8783406c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5544618a85f97fac02f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5544618a85f97fac02f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56c08d20682bc24a7786"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-56c08d20682bc24a7786`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-299531f11b79c166fe5b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-299531f11b79c166fe5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ed037450d16112254df8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ed037450d16112254df8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-212a11cf5fdf561ffcc8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-212a11cf5fdf561ffcc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11b7ad415cae9521dc83"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-11b7ad415cae9521dc83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7935a87d59bc7aed4619"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7935a87d59bc7aed4619`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99ced5bf6cc4f32bd2be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99ced5bf6cc4f32bd2be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38e7af7bb28198cbc113"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-38e7af7bb28198cbc113`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7ba21c0822f4b9ba104"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e7ba21c0822f4b9ba104`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-557286bd1587b7f6bc58"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-557286bd1587b7f6bc58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d708a283f04a50f2bb37"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d708a283f04a50f2bb37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04b27e4182705e1d3247"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04b27e4182705e1d3247`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef431e11edd6fbd90964"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ef431e11edd6fbd90964`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f25806d75e9edcd5471f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f25806d75e9edcd5471f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de73e5c4631cf19c4a0c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de73e5c4631cf19c4a0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66063696cef61d59ff58"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-66063696cef61d59ff58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4f351fd5860c533c912"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c4f351fd5860c533c912`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2df9448577d8ced1ea3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e2df9448577d8ced1ea3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e3c6bc46e8e5830ea56"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e3c6bc46e8e5830ea56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b2f2ad1db56d09cddcb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b2f2ad1db56d09cddcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16b141f2bab3e02a1da8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-16b141f2bab3e02a1da8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78ad4a4ecad184dbc4f2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-78ad4a4ecad184dbc4f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b65a851162eff0ffb8a5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b65a851162eff0ffb8a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a53a49da2d55c4ebb4e9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a53a49da2d55c4ebb4e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-509fff75cd5010b45798"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-509fff75cd5010b45798`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d70fb70e4f06640a163"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0d70fb70e4f06640a163`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-54dc8461f694f231dd90"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-54dc8461f694f231dd90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a90357040caf828dc70a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a90357040caf828dc70a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0078202ba18193c9736"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b0078202ba18193c9736`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ee6e91bfb41e09571ff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2ee6e91bfb41e09571ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8242d42603b9b7aedec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8242d42603b9b7aedec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d3d35647954e349282c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d3d35647954e349282c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65d416b2c40460af6124"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65d416b2c40460af6124`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f2e63e449d24f12dbef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f2e63e449d24f12dbef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:canonical-southeast | <a href="#case-preview_review-a67e24e4c1f947dee39b">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:canonical-top | <a href="#case-preview_review-9744fb5f7ea486614f1f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:connection-overview | <a href="#case-preview_review-296b5198c70ed28fe338">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:canonical-southeast</summary>

<a id="case-preview_review-a67e24e4c1f947dee39b"></a>

**General: unverified** — `preview_review-a67e24e4c1f947dee39b`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:canonical-top</summary>

<a id="case-preview_review-9744fb5f7ea486614f1f"></a>

**General: unverified** — `preview_review-9744fb5f7ea486614f1f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:connection-overview</summary>

<a id="case-preview_review-296b5198c70ed28fe338"></a>

**General: unverified** — `preview_review-296b5198c70ed28fe338`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-rhw-l0-orthogonal-lower-right-6tile:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The original straight transition family shifts the upper road. This variant places the lower road’s ground connection one tile to the right of the fixed upper centreline. The upper grade was recalculated for the straight run, and the lower grade was checked along both offset lane paths.
