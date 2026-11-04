# Testing — DD RHW-4 — Diagonal Two-Branch Stem — L1/L2 — Reversed Traffic

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Use the [piece guide](README.md) for its occupied cells and socket, and the [assembly testing guide](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/TESTING.md) for all six complete journeys. The generated table describes this component's intrinsic route cuts.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `a-c-in` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `c-a-out` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `a-b-in` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `b-a-out` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `a-b-out` | road / 1 / primary | out | [22.332766, 8.0, 7.5]; [0.25725570106816964, 0.9663433676845538]; 0.0 | `path-interface-7ac653a2387e790053a9` |
| `b-a-in` | road / 1 / primary | in | [22.332766, 8.0, 15.0]; [-0.25725570106816964, -0.9663433676845538]; 0.0 | `path-interface-92892adb3bd2bdba401e` |
| `a-c-out` | road / 1 / primary | out | [53.321807, 8.0, 7.5]; [0.9475295370856598, 0.31966822855929156]; 0.0 | `path-interface-c791c496692b36ecf9fc` |
| `c-a-in` | road / 1 / primary | in | [53.321807, 8.0, 15.0]; [-0.9475295370856598, -0.31966822855929156]; 0.0 | `path-interface-5176920b754720e94972` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `a-c-in` → `a-c-out` | primary |
| road | `a-b-in` → `a-b-out` | primary |
| road | `b-a-in` → `b-a-out` | primary |
| road | `c-a-in` → `c-a-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `a-c-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the audited NAM 50 right-hand-traffic inputs and a disposable flat test city. Install deliberately, restart the game, and place all three reversed components afresh using the [placement table](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/README.md#3-placements). This type is **P01** at **(X0, Y2)**, and its native socket is **(X0, Y1)**. Keep the original Y's types and observations separate.

The upper southwest deck is outgoing, and both upper branch decks are incoming. The lower decks carry the opposite directions. Every yellow line must be on the driver's left. This component's southwest diagonal helper is `57530200` at quarter-turn pose 0. The original Y's `57530900` helper phase is not a substitute for this reversed interface.

## 3. Software checks

Follow the [exact build, saved-resource, connector, rendering, and regression commands](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/TESTING.md#3-software-checks). The checker reads the saved models, traffic paths, texture coordinates, and construction rules. Texture coordinates, also called UV coordinates, select positions in a texture image. Source diagrams alone cannot establish these checks.

The complete assembly must pass ownership, all six journeys, native profile contact, car-strip clearance, full-width underside depth, closed road and barrier shells, support contacts, and actual texture-pixel marking checks. The original type's accepted geometry, exceptions, software counts, and human report do not establish the reversed type's result.

## 4. Game checks

1. Find the exact reversed assembly button, and verify the component's tooltip and Tab order. Check that the original assembly remains available.
2. Place **P01** at **(X0, Y2)**, inspect its entire occupied shape, and verify its ordinary native socket at **(X0, Y1)**. Check automatic socket appearance, outward native dragging, and connection to a prebuilt matching approach separately.
3. Complete all three placements. Use Route Query and an actual moving car to check each complete journey independently. Inspect yellow on the driver's left on both decks and the descending links.
4. Inspect all zooms and four camera orientations, redraw the native approach, replace one component, save, exit, and reload. Record only the precise behavior observed, with the matching candidate and pose.

## 5. Results and known issues

Implementation verification and final package evidence are recorded in the [assembly results](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/TESTING.md#5-results-and-known-issues). No human game result has been transferred from the original junction to this counterpart. The generated cases below remain the authoritative detailed observation record.

The material change between native DD highway pavement and the single-lane ramp can show a tone seam. Native automatic placement is experimental, projected custom shadows are disabled, and the steep links need game observation. Four proper rotations are supported; reflections and another relative grid alignment are outside this type.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-y-reversed-diagonal-stem-split/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-y-reversed-diagonal-stem-split/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-91ab691238c7e7473061">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-91ab691238c7e7473061"></a>

**General: unverified** — `software_resources-91ab691238c7e7473061`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-91ab691238c7e7473061">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-91ab691238c7e7473061"></a>

**General: unverified** — `software_connectivity-91ab691238c7e7473061`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-8be21832cb3ef4006ac4">[ ] unverified</a> | <a href="#case-in_game_render-8196d0b6f7bda5e627d4">[ ] unverified</a> | <a href="#case-in_game_render-ea09fb25f88101469ba9">[ ] unverified</a> | <a href="#case-in_game_render-1c0130a847b53d06c35d">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-8be21832cb3ef4006ac4"></a>

**0° CCW: unverified** — `in_game_render-8be21832cb3ef4006ac4`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8196d0b6f7bda5e627d4"></a>

**90° CCW: unverified** — `in_game_render-8196d0b6f7bda5e627d4`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ea09fb25f88101469ba9"></a>

**180° CCW: unverified** — `in_game_render-ea09fb25f88101469ba9`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1c0130a847b53d06c35d"></a>

**270° CCW: unverified** — `in_game_render-1c0130a847b53d06c35d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-8be21832cb3ef4006ac4">[ ] unverified</a> | <a href="#case-in_game_placement-8196d0b6f7bda5e627d4">[ ] unverified</a> | <a href="#case-in_game_placement-ea09fb25f88101469ba9">[ ] unverified</a> | <a href="#case-in_game_placement-1c0130a847b53d06c35d">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-8be21832cb3ef4006ac4"></a>

**0° CCW: unverified** — `in_game_placement-8be21832cb3ef4006ac4`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8196d0b6f7bda5e627d4"></a>

**90° CCW: unverified** — `in_game_placement-8196d0b6f7bda5e627d4`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ea09fb25f88101469ba9"></a>

**180° CCW: unverified** — `in_game_placement-ea09fb25f88101469ba9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1c0130a847b53d06c35d"></a>

**270° CCW: unverified** — `in_game_placement-1c0130a847b53d06c35d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-8be21832cb3ef4006ac4">[ ] unverified</a> | <a href="#case-in_game_demolition-8196d0b6f7bda5e627d4">[ ] unverified</a> | <a href="#case-in_game_demolition-ea09fb25f88101469ba9">[ ] unverified</a> | <a href="#case-in_game_demolition-1c0130a847b53d06c35d">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-8be21832cb3ef4006ac4"></a>

**0° CCW: unverified** — `in_game_demolition-8be21832cb3ef4006ac4`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8196d0b6f7bda5e627d4"></a>

**90° CCW: unverified** — `in_game_demolition-8196d0b6f7bda5e627d4`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ea09fb25f88101469ba9"></a>

**180° CCW: unverified** — `in_game_demolition-ea09fb25f88101469ba9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1c0130a847b53d06c35d"></a>

**270° CCW: unverified** — `in_game_demolition-1c0130a847b53d06c35d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-8be21832cb3ef4006ac4">[ ] unverified</a> | <a href="#case-in_game_save_reload-8196d0b6f7bda5e627d4">[ ] unverified</a> | <a href="#case-in_game_save_reload-ea09fb25f88101469ba9">[ ] unverified</a> | <a href="#case-in_game_save_reload-1c0130a847b53d06c35d">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-8be21832cb3ef4006ac4"></a>

**0° CCW: unverified** — `in_game_save_reload-8be21832cb3ef4006ac4`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8196d0b6f7bda5e627d4"></a>

**90° CCW: unverified** — `in_game_save_reload-8196d0b6f7bda5e627d4`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ea09fb25f88101469ba9"></a>

**180° CCW: unverified** — `in_game_save_reload-ea09fb25f88101469ba9`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1c0130a847b53d06c35d"></a>

**270° CCW: unverified** — `in_game_save_reload-1c0130a847b53d06c35d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out | — | <a href="#case-in_game_route_query-881fd24a1dbd73fc1245">[ ] unverified</a> | <a href="#case-in_game_route_query-851053303283d0809491">[ ] unverified</a> | <a href="#case-in_game_route_query-30f2177c97ff2f818b42">[ ] unverified</a> | <a href="#case-in_game_route_query-eec534ad9edaf5651348">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_route_query-a4ba5a250e8a25ba74bb">[ ] unverified</a> | <a href="#case-in_game_route_query-9eb2b82d638a6cce5dc5">[ ] unverified</a> | <a href="#case-in_game_route_query-63f06cc962eca6ba7c44">[ ] unverified</a> | <a href="#case-in_game_route_query-580e1ac64efe8ef38407">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_route_query-4714aa5f7029874baaa8">[ ] unverified</a> | <a href="#case-in_game_route_query-64d12ff11a678e3c1c79">[ ] unverified</a> | <a href="#case-in_game_route_query-f9e5a08ae105ade82c3b">[ ] unverified</a> | <a href="#case-in_game_route_query-476b2e17b3f50dc538f1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out | — | <a href="#case-in_game_route_query-25032d10f1a934342fc5">[ ] unverified</a> | <a href="#case-in_game_route_query-3982eff2cb4bb06c79da">[ ] unverified</a> | <a href="#case-in_game_route_query-7097b584bbb9ff9535fc">[ ] unverified</a> | <a href="#case-in_game_route_query-3f6e165171b0f6ef1114">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out</summary>

<a id="case-in_game_route_query-881fd24a1dbd73fc1245"></a>

**0° CCW: unverified** — `in_game_route_query-881fd24a1dbd73fc1245`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-851053303283d0809491"></a>

**90° CCW: unverified** — `in_game_route_query-851053303283d0809491`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-30f2177c97ff2f818b42"></a>

**180° CCW: unverified** — `in_game_route_query-30f2177c97ff2f818b42`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-eec534ad9edaf5651348"></a>

**270° CCW: unverified** — `in_game_route_query-eec534ad9edaf5651348`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_route_query-a4ba5a250e8a25ba74bb"></a>

**0° CCW: unverified** — `in_game_route_query-a4ba5a250e8a25ba74bb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-9eb2b82d638a6cce5dc5"></a>

**90° CCW: unverified** — `in_game_route_query-9eb2b82d638a6cce5dc5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-63f06cc962eca6ba7c44"></a>

**180° CCW: unverified** — `in_game_route_query-63f06cc962eca6ba7c44`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-580e1ac64efe8ef38407"></a>

**270° CCW: unverified** — `in_game_route_query-580e1ac64efe8ef38407`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_route_query-4714aa5f7029874baaa8"></a>

**0° CCW: unverified** — `in_game_route_query-4714aa5f7029874baaa8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-64d12ff11a678e3c1c79"></a>

**90° CCW: unverified** — `in_game_route_query-64d12ff11a678e3c1c79`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-f9e5a08ae105ade82c3b"></a>

**180° CCW: unverified** — `in_game_route_query-f9e5a08ae105ade82c3b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-476b2e17b3f50dc538f1"></a>

**270° CCW: unverified** — `in_game_route_query-476b2e17b3f50dc538f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out</summary>

<a id="case-in_game_route_query-25032d10f1a934342fc5"></a>

**0° CCW: unverified** — `in_game_route_query-25032d10f1a934342fc5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-3982eff2cb4bb06c79da"></a>

**90° CCW: unverified** — `in_game_route_query-3982eff2cb4bb06c79da`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-7097b584bbb9ff9535fc"></a>

**180° CCW: unverified** — `in_game_route_query-7097b584bbb9ff9535fc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-3f6e165171b0f6ef1114"></a>

**270° CCW: unverified** — `in_game_route_query-3f6e165171b0f6ef1114`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out | — | <a href="#case-in_game_visible_travel-881fd24a1dbd73fc1245">[ ] unverified</a> | <a href="#case-in_game_visible_travel-851053303283d0809491">[ ] unverified</a> | <a href="#case-in_game_visible_travel-30f2177c97ff2f818b42">[ ] unverified</a> | <a href="#case-in_game_visible_travel-eec534ad9edaf5651348">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_visible_travel-a4ba5a250e8a25ba74bb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9eb2b82d638a6cce5dc5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-63f06cc962eca6ba7c44">[ ] unverified</a> | <a href="#case-in_game_visible_travel-580e1ac64efe8ef38407">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_visible_travel-4714aa5f7029874baaa8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-64d12ff11a678e3c1c79">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f9e5a08ae105ade82c3b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-476b2e17b3f50dc538f1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out | — | <a href="#case-in_game_visible_travel-25032d10f1a934342fc5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3982eff2cb4bb06c79da">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7097b584bbb9ff9535fc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3f6e165171b0f6ef1114">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out</summary>

<a id="case-in_game_visible_travel-881fd24a1dbd73fc1245"></a>

**0° CCW: unverified** — `in_game_visible_travel-881fd24a1dbd73fc1245`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-851053303283d0809491"></a>

**90° CCW: unverified** — `in_game_visible_travel-851053303283d0809491`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-30f2177c97ff2f818b42"></a>

**180° CCW: unverified** — `in_game_visible_travel-30f2177c97ff2f818b42`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-eec534ad9edaf5651348"></a>

**270° CCW: unverified** — `in_game_visible_travel-eec534ad9edaf5651348`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_visible_travel-a4ba5a250e8a25ba74bb"></a>

**0° CCW: unverified** — `in_game_visible_travel-a4ba5a250e8a25ba74bb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-9eb2b82d638a6cce5dc5"></a>

**90° CCW: unverified** — `in_game_visible_travel-9eb2b82d638a6cce5dc5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-63f06cc962eca6ba7c44"></a>

**180° CCW: unverified** — `in_game_visible_travel-63f06cc962eca6ba7c44`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-580e1ac64efe8ef38407"></a>

**270° CCW: unverified** — `in_game_visible_travel-580e1ac64efe8ef38407`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_visible_travel-4714aa5f7029874baaa8"></a>

**0° CCW: unverified** — `in_game_visible_travel-4714aa5f7029874baaa8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-64d12ff11a678e3c1c79"></a>

**90° CCW: unverified** — `in_game_visible_travel-64d12ff11a678e3c1c79`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-f9e5a08ae105ade82c3b"></a>

**180° CCW: unverified** — `in_game_visible_travel-f9e5a08ae105ade82c3b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-476b2e17b3f50dc538f1"></a>

**270° CCW: unverified** — `in_game_visible_travel-476b2e17b3f50dc538f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out</summary>

<a id="case-in_game_visible_travel-25032d10f1a934342fc5"></a>

**0° CCW: unverified** — `in_game_visible_travel-25032d10f1a934342fc5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-3982eff2cb4bb06c79da"></a>

**90° CCW: unverified** — `in_game_visible_travel-3982eff2cb4bb06c79da`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-7097b584bbb9ff9535fc"></a>

**180° CCW: unverified** — `in_game_visible_travel-7097b584bbb9ff9535fc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-3f6e165171b0f6ef1114"></a>

**270° CCW: unverified** — `in_game_visible_travel-3f6e165171b0f6ef1114`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-25ab2e332dc49634fc6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d14acc5b08c981825e1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf892b22f2fb36401b11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21fc83a9ae8f5bbb3beb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-52c7a540dff7d1ebee33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-542a5f0823ba249eb37f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e441d2df62eac687af94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-869df24f002497e41146">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1682b11abebe90092473">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2c11e9ac4de9d0a7f4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65edd4d8ce2a2e73c6b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-639f48549732d2e5972c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1cbf0d11a4d5d7767ca4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-153722d7d24fd3c13c9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-527618ab7912432a20e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eba389ae43983e3ba4a9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7cd25e317d1ed7caf0d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68414322e7ec0a066615">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6048ce987e867c312d6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c875ce5914900b2c33c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f13226d0dfe8be9d491f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a2d1a666f2fc5574dcd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8a3599021744622b626">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8af42e55933f047be8d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99e324b21d569191643a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a92ef88edcb1e392b4bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9d3251801b36b0fd546">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4da4e4fc88aae8dfaa6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b2f0320d6403d072883d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1741c9f2df3bd196adae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-621525929f597128d11c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f994105842cce4472f09">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be9cce0327fbc025c593">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c764681279288d1f3e8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7c76616c1f2ade1807b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f4bd4c7c72d32fa62c6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e899b5d51edb0e3611da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acbc217cbc495c696d5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf25a109f5aa29526b7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64fb01726ba131800d79">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c85e05d9a9fe81573dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdc9db0d952f4f3f288d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9da0ca157b47b4658fdb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdfd8a2803081a740fd1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32277a530487e46af4cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7b3b42504c3e38cc481">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6a5b33851c837d0ebc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b8857602e50da9e3791">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-25ab2e332dc49634fc6b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-25ab2e332dc49634fc6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d14acc5b08c981825e1f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d14acc5b08c981825e1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf892b22f2fb36401b11"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bf892b22f2fb36401b11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21fc83a9ae8f5bbb3beb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-21fc83a9ae8f5bbb3beb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-52c7a540dff7d1ebee33"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-52c7a540dff7d1ebee33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-542a5f0823ba249eb37f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-542a5f0823ba249eb37f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e441d2df62eac687af94"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e441d2df62eac687af94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-869df24f002497e41146"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-869df24f002497e41146`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1682b11abebe90092473"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1682b11abebe90092473`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2c11e9ac4de9d0a7f4b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f2c11e9ac4de9d0a7f4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65edd4d8ce2a2e73c6b8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65edd4d8ce2a2e73c6b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-639f48549732d2e5972c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-639f48549732d2e5972c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1cbf0d11a4d5d7767ca4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1cbf0d11a4d5d7767ca4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-153722d7d24fd3c13c9b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-153722d7d24fd3c13c9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-527618ab7912432a20e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-527618ab7912432a20e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eba389ae43983e3ba4a9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eba389ae43983e3ba4a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7cd25e317d1ed7caf0d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7cd25e317d1ed7caf0d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68414322e7ec0a066615"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-68414322e7ec0a066615`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6048ce987e867c312d6a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6048ce987e867c312d6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c875ce5914900b2c33c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2c875ce5914900b2c33c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f13226d0dfe8be9d491f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f13226d0dfe8be9d491f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a2d1a666f2fc5574dcd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2a2d1a666f2fc5574dcd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8a3599021744622b626"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b8a3599021744622b626`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8af42e55933f047be8d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8af42e55933f047be8d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99e324b21d569191643a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99e324b21d569191643a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a92ef88edcb1e392b4bc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a92ef88edcb1e392b4bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9d3251801b36b0fd546"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c9d3251801b36b0fd546`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4da4e4fc88aae8dfaa6c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4da4e4fc88aae8dfaa6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b2f0320d6403d072883d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2f0320d6403d072883d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1741c9f2df3bd196adae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1741c9f2df3bd196adae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-621525929f597128d11c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-621525929f597128d11c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f994105842cce4472f09"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f994105842cce4472f09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be9cce0327fbc025c593"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be9cce0327fbc025c593`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c764681279288d1f3e8a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c764681279288d1f3e8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7c76616c1f2ade1807b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f7c76616c1f2ade1807b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f4bd4c7c72d32fa62c6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f4bd4c7c72d32fa62c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e899b5d51edb0e3611da"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e899b5d51edb0e3611da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acbc217cbc495c696d5d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-acbc217cbc495c696d5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf25a109f5aa29526b7f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bf25a109f5aa29526b7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64fb01726ba131800d79"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64fb01726ba131800d79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c85e05d9a9fe81573dd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c85e05d9a9fe81573dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdc9db0d952f4f3f288d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cdc9db0d952f4f3f288d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9da0ca157b47b4658fdb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9da0ca157b47b4658fdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdfd8a2803081a740fd1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cdfd8a2803081a740fd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32277a530487e46af4cc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32277a530487e46af4cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7b3b42504c3e38cc481"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f7b3b42504c3e38cc481`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6a5b33851c837d0ebc0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d6a5b33851c837d0ebc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b8857602e50da9e3791"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b8857602e50da9e3791`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-y-reversed-diagonal-stem-split:canonical-southeast | <a href="#case-preview_review-612c3c9081253b8d240f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-reversed-diagonal-stem-split:canonical-top | <a href="#case-preview_review-9a3856a5fb0ddc9415a3">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-reversed-diagonal-stem-split:connection-overview | <a href="#case-preview_review-93818a32116c48648f80">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-diagonal-stem-split:canonical-southeast</summary>

<a id="case-preview_review-612c3c9081253b8d240f"></a>

**General: unverified** — `preview_review-612c3c9081253b8d240f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-diagonal-stem-split:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-diagonal-stem-split:canonical-top</summary>

<a id="case-preview_review-9a3856a5fb0ddc9415a3"></a>

**General: unverified** — `preview_review-9a3856a5fb0ddc9415a3`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-diagonal-stem-split:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-diagonal-stem-split:connection-overview</summary>

<a id="case-preview_review-93818a32116c48648f80"></a>

**General: unverified** — `preview_review-93818a32116c48648f80`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-diagonal-stem-split:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested another variant with yellow on the opposite physical side and clarified that yellow must remain on the driver's left. This implementation reverses all directed journeys at the original arm positions and uses a separate native phase, component identities, and menu cycle. The original junction and its human observations remain separate.

Follow the [shared observation procedure](../../../../docs/TESTING.md). Copy the exact case ID from the generated checklist, record the installed candidate, pose, environment, and observed behavior, and retain failures or uncertainty. A software pass or preview review does not create a human game pass.
