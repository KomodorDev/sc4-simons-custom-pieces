# Testing — DD RHW-4 — Diagonal Branch and Paired Graded Links — L1/L2 — Reversed Traffic

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
| `a-b-out` | road / 1 / primary | out | [8.0, -19.2, 7.5]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `b-a-in` | road / 1 / primary | in | [8.0, -19.2, 15.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `c-b-out` | road / 1 / primary | out | [8.0, -12.8, 7.5]; [-0.7071067811865119, 0.7071067811865831]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `b-c-in` | road / 1 / primary | in | [8.0, -12.8, 15.0]; [0.7071067811865119, -0.7071067811865831]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `a-b-in` | road / 1 / primary | in | [22.332766, -40.0, 7.5]; [-0.25725570106816964, 0.9663433676845538]; 0.0 | `path-interface-ac1fd402b55f95edaa5b` |
| `b-a-out` | road / 1 / primary | out | [22.332766, -40.0, 15.0]; [0.25725570106816964, -0.9663433676845538]; 0.0 | `path-interface-72c8b7a87f82a3fe3e76` |
| `b-c-out` | road / 1 / primary | out | [39.700047, -40.0, 12.159544]; [0.8923143763223463, -0.45141450332090804]; -0.248976814 | `path-interface-93f54f456af3587023cf` |
| `c-b-in` | road / 1 / primary | in | [62.247886, -40.0, 14.711544]; [-0.8870803545357738, 0.4616150393961248]; -0.085894374 | `path-interface-85d9bc718374dfbaaab9` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `b-a-in` → `b-a-out` | primary |
| road | `b-c-in` → `b-c-out` | primary |
| road | `a-b-in` → `a-b-out` | primary |
| road | `c-b-in` → `c-b-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `b-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the audited NAM 50 right-hand-traffic inputs and a disposable flat test city. Install deliberately, restart the game, and place all three reversed components afresh using the [placement table](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/README.md#3-placements). This type is **P02** at **(X0, Y6)**, and its native socket is **(X0, Y5)**. Keep the original Y's types and observations separate.

The upper southwest deck is outgoing, and both upper branch decks are incoming. The lower decks carry the opposite directions. Every yellow line must be on the driver's left. This component's northwest diagonal helper is `57530200` at quarter-turn pose 3. The original Y's `57530900` helper phase is not a substitute for this reversed interface.

## 3. Software checks

Follow the [exact build, saved-resource, connector, rendering, and regression commands](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/TESTING.md#3-software-checks). The checker reads the saved models, traffic paths, texture coordinates, and construction rules. Texture coordinates, also called UV coordinates, select positions in a texture image. Source diagrams alone cannot establish these checks.

The complete assembly must pass ownership, all six journeys, native profile contact, car-strip clearance, full-width underside depth, closed road and barrier shells, support contacts, and actual texture-pixel marking checks. The original type's accepted geometry, exceptions, software counts, and human report do not establish the reversed type's result.

## 4. Game checks

1. Find the exact reversed assembly button, and verify the component's tooltip and Tab order. Check that the original assembly remains available.
2. Place **P02** at **(X0, Y6)**, inspect its entire occupied shape, and verify its ordinary native socket at **(X0, Y5)**. Check automatic socket appearance, outward native dragging, and connection to a prebuilt matching approach separately.
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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-y-reversed-diagonal-branch/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-y-reversed-diagonal-branch/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-57323e34f361fdf22946">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-57323e34f361fdf22946"></a>

**General: unverified** — `software_resources-57323e34f361fdf22946`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-57323e34f361fdf22946">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-57323e34f361fdf22946"></a>

**General: unverified** — `software_connectivity-57323e34f361fdf22946`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-447c7a13cf1d9e80c747">[ ] unverified</a> | <a href="#case-in_game_render-1e52c5b5e777b0bfc41f">[ ] unverified</a> | <a href="#case-in_game_render-cae3b47a25b783fdef34">[ ] unverified</a> | <a href="#case-in_game_render-bd8df5144fafd13ba975">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-447c7a13cf1d9e80c747"></a>

**0° CCW: unverified** — `in_game_render-447c7a13cf1d9e80c747`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1e52c5b5e777b0bfc41f"></a>

**90° CCW: unverified** — `in_game_render-1e52c5b5e777b0bfc41f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-cae3b47a25b783fdef34"></a>

**180° CCW: unverified** — `in_game_render-cae3b47a25b783fdef34`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-bd8df5144fafd13ba975"></a>

**270° CCW: unverified** — `in_game_render-bd8df5144fafd13ba975`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-447c7a13cf1d9e80c747">[ ] unverified</a> | <a href="#case-in_game_placement-1e52c5b5e777b0bfc41f">[ ] unverified</a> | <a href="#case-in_game_placement-cae3b47a25b783fdef34">[ ] unverified</a> | <a href="#case-in_game_placement-bd8df5144fafd13ba975">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-447c7a13cf1d9e80c747"></a>

**0° CCW: unverified** — `in_game_placement-447c7a13cf1d9e80c747`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1e52c5b5e777b0bfc41f"></a>

**90° CCW: unverified** — `in_game_placement-1e52c5b5e777b0bfc41f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-cae3b47a25b783fdef34"></a>

**180° CCW: unverified** — `in_game_placement-cae3b47a25b783fdef34`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-bd8df5144fafd13ba975"></a>

**270° CCW: unverified** — `in_game_placement-bd8df5144fafd13ba975`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-447c7a13cf1d9e80c747">[ ] unverified</a> | <a href="#case-in_game_demolition-1e52c5b5e777b0bfc41f">[ ] unverified</a> | <a href="#case-in_game_demolition-cae3b47a25b783fdef34">[ ] unverified</a> | <a href="#case-in_game_demolition-bd8df5144fafd13ba975">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-447c7a13cf1d9e80c747"></a>

**0° CCW: unverified** — `in_game_demolition-447c7a13cf1d9e80c747`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1e52c5b5e777b0bfc41f"></a>

**90° CCW: unverified** — `in_game_demolition-1e52c5b5e777b0bfc41f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-cae3b47a25b783fdef34"></a>

**180° CCW: unverified** — `in_game_demolition-cae3b47a25b783fdef34`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-bd8df5144fafd13ba975"></a>

**270° CCW: unverified** — `in_game_demolition-bd8df5144fafd13ba975`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-447c7a13cf1d9e80c747">[ ] unverified</a> | <a href="#case-in_game_save_reload-1e52c5b5e777b0bfc41f">[ ] unverified</a> | <a href="#case-in_game_save_reload-cae3b47a25b783fdef34">[ ] unverified</a> | <a href="#case-in_game_save_reload-bd8df5144fafd13ba975">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-447c7a13cf1d9e80c747"></a>

**0° CCW: unverified** — `in_game_save_reload-447c7a13cf1d9e80c747`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1e52c5b5e777b0bfc41f"></a>

**90° CCW: unverified** — `in_game_save_reload-1e52c5b5e777b0bfc41f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-cae3b47a25b783fdef34"></a>

**180° CCW: unverified** — `in_game_save_reload-cae3b47a25b783fdef34`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-bd8df5144fafd13ba975"></a>

**270° CCW: unverified** — `in_game_save_reload-bd8df5144fafd13ba975`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_route_query-2fb57bfef973150ac18c">[ ] unverified</a> | <a href="#case-in_game_route_query-ccafcefe0bb19aa44abc">[ ] unverified</a> | <a href="#case-in_game_route_query-fb7996c675f04cfcc104">[ ] unverified</a> | <a href="#case-in_game_route_query-f56249eff3e788fa4d4f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out | — | <a href="#case-in_game_route_query-1171de4be78e95449eac">[ ] unverified</a> | <a href="#case-in_game_route_query-a625ff5705dfb5561e04">[ ] unverified</a> | <a href="#case-in_game_route_query-8a6b8f66706b8d8acfce">[ ] unverified</a> | <a href="#case-in_game_route_query-fba17b22249461580017">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_route_query-aff745d54901ffc59b95">[ ] unverified</a> | <a href="#case-in_game_route_query-88512eaa5a4d4079ad61">[ ] unverified</a> | <a href="#case-in_game_route_query-cbcb06559452b70cbcf4">[ ] unverified</a> | <a href="#case-in_game_route_query-ceb233708ab909d44870">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out | — | <a href="#case-in_game_route_query-612cbbaade0e3379ddde">[ ] unverified</a> | <a href="#case-in_game_route_query-dae2961b56054165d84b">[ ] unverified</a> | <a href="#case-in_game_route_query-bb62921c49a44a9570dd">[ ] unverified</a> | <a href="#case-in_game_route_query-94343963515c63e0b43c">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_route_query-2fb57bfef973150ac18c"></a>

**0° CCW: unverified** — `in_game_route_query-2fb57bfef973150ac18c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-ccafcefe0bb19aa44abc"></a>

**90° CCW: unverified** — `in_game_route_query-ccafcefe0bb19aa44abc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-fb7996c675f04cfcc104"></a>

**180° CCW: unverified** — `in_game_route_query-fb7996c675f04cfcc104`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-f56249eff3e788fa4d4f"></a>

**270° CCW: unverified** — `in_game_route_query-f56249eff3e788fa4d4f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out</summary>

<a id="case-in_game_route_query-1171de4be78e95449eac"></a>

**0° CCW: unverified** — `in_game_route_query-1171de4be78e95449eac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-a625ff5705dfb5561e04"></a>

**90° CCW: unverified** — `in_game_route_query-a625ff5705dfb5561e04`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-8a6b8f66706b8d8acfce"></a>

**180° CCW: unverified** — `in_game_route_query-8a6b8f66706b8d8acfce`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-fba17b22249461580017"></a>

**270° CCW: unverified** — `in_game_route_query-fba17b22249461580017`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_route_query-aff745d54901ffc59b95"></a>

**0° CCW: unverified** — `in_game_route_query-aff745d54901ffc59b95`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-88512eaa5a4d4079ad61"></a>

**90° CCW: unverified** — `in_game_route_query-88512eaa5a4d4079ad61`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-cbcb06559452b70cbcf4"></a>

**180° CCW: unverified** — `in_game_route_query-cbcb06559452b70cbcf4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-ceb233708ab909d44870"></a>

**270° CCW: unverified** — `in_game_route_query-ceb233708ab909d44870`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out</summary>

<a id="case-in_game_route_query-612cbbaade0e3379ddde"></a>

**0° CCW: unverified** — `in_game_route_query-612cbbaade0e3379ddde`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-dae2961b56054165d84b"></a>

**90° CCW: unverified** — `in_game_route_query-dae2961b56054165d84b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-bb62921c49a44a9570dd"></a>

**180° CCW: unverified** — `in_game_route_query-bb62921c49a44a9570dd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-94343963515c63e0b43c"></a>

**270° CCW: unverified** — `in_game_route_query-94343963515c63e0b43c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_visible_travel-2fb57bfef973150ac18c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ccafcefe0bb19aa44abc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fb7996c675f04cfcc104">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f56249eff3e788fa4d4f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out | — | <a href="#case-in_game_visible_travel-1171de4be78e95449eac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a625ff5705dfb5561e04">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8a6b8f66706b8d8acfce">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fba17b22249461580017">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_visible_travel-aff745d54901ffc59b95">[ ] unverified</a> | <a href="#case-in_game_visible_travel-88512eaa5a4d4079ad61">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cbcb06559452b70cbcf4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ceb233708ab909d44870">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out | — | <a href="#case-in_game_visible_travel-612cbbaade0e3379ddde">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dae2961b56054165d84b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bb62921c49a44a9570dd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-94343963515c63e0b43c">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_visible_travel-2fb57bfef973150ac18c"></a>

**0° CCW: unverified** — `in_game_visible_travel-2fb57bfef973150ac18c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-ccafcefe0bb19aa44abc"></a>

**90° CCW: unverified** — `in_game_visible_travel-ccafcefe0bb19aa44abc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-fb7996c675f04cfcc104"></a>

**180° CCW: unverified** — `in_game_visible_travel-fb7996c675f04cfcc104`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-f56249eff3e788fa4d4f"></a>

**270° CCW: unverified** — `in_game_visible_travel-f56249eff3e788fa4d4f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out</summary>

<a id="case-in_game_visible_travel-1171de4be78e95449eac"></a>

**0° CCW: unverified** — `in_game_visible_travel-1171de4be78e95449eac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-a625ff5705dfb5561e04"></a>

**90° CCW: unverified** — `in_game_visible_travel-a625ff5705dfb5561e04`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-8a6b8f66706b8d8acfce"></a>

**180° CCW: unverified** — `in_game_visible_travel-8a6b8f66706b8d8acfce`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-fba17b22249461580017"></a>

**270° CCW: unverified** — `in_game_visible_travel-fba17b22249461580017`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_visible_travel-aff745d54901ffc59b95"></a>

**0° CCW: unverified** — `in_game_visible_travel-aff745d54901ffc59b95`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-88512eaa5a4d4079ad61"></a>

**90° CCW: unverified** — `in_game_visible_travel-88512eaa5a4d4079ad61`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-cbcb06559452b70cbcf4"></a>

**180° CCW: unverified** — `in_game_visible_travel-cbcb06559452b70cbcf4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-ceb233708ab909d44870"></a>

**270° CCW: unverified** — `in_game_visible_travel-ceb233708ab909d44870`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out</summary>

<a id="case-in_game_visible_travel-612cbbaade0e3379ddde"></a>

**0° CCW: unverified** — `in_game_visible_travel-612cbbaade0e3379ddde`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-dae2961b56054165d84b"></a>

**90° CCW: unverified** — `in_game_visible_travel-dae2961b56054165d84b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-bb62921c49a44a9570dd"></a>

**180° CCW: unverified** — `in_game_visible_travel-bb62921c49a44a9570dd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-94343963515c63e0b43c"></a>

**270° CCW: unverified** — `in_game_visible_travel-94343963515c63e0b43c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66198faf2f1dbfa7d2b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b54a552e00f84f5a8754">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd5493e6a98372bcc913">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2150234ae3b64ee31e03">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f50d8231f2a0e4acee68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5807f29175303aa932e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-976df7c0f527c36053c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79e27d6a72b0a0836f9c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-05c1c07221a586ce207b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-693050cee9fc96ef9ec8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88a664473a6d9ef93cd2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57d27143278c8075f6ef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca7683a3fa6fadfc7f25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b3506f32ef307bfbea0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b43915fa21cad5e545cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00ebcbb13416c4032b50">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-008e4678e9390ee5499f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f5e89a6c78624b87774">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92713c53e8d90a4157a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5a6389c9cdc8cdf8691">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9f45f2cdd07fd4ef124d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e81c2fa83ecdbd2f917">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d4c1b03ce35ed7ed62a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8704e40d826eddf06c96">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0d0be5bb23098ce41614">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bcbbc6784dc7d3158ebc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3eb238586ef90b30210f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-331f450ec7ee6edbd036">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dcd20699a45ff596565d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80269ca77ab6ecbe6090">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf23dcc0fed6514cbdcd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-114d43aab3786c15939b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41ae8fa9a32ed6a15149">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a336c5990c81fa399092">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4737b4fafa88b0f0fd92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9872eb8df9e4c8849ce6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32d01874c935eb5bd023">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31d87c003e0b0b7ad02c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-886c55a7facac7a3b559">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ba23b95bc3730dd1dc1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-29bfda7588b5a9b07c95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-037928940519be1d957c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc8c23fb8cc3c529e14d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adc636249e8c88c01849">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e194a91bd60c4dba2a6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72e3ba0a3b4eab61a853">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4dede67a629eb0eb67e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96243c5fc325c7d58ae6">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-66198faf2f1dbfa7d2b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66198faf2f1dbfa7d2b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b54a552e00f84f5a8754"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b54a552e00f84f5a8754`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd5493e6a98372bcc913"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cd5493e6a98372bcc913`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2150234ae3b64ee31e03"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2150234ae3b64ee31e03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f50d8231f2a0e4acee68"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f50d8231f2a0e4acee68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5807f29175303aa932e7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5807f29175303aa932e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-976df7c0f527c36053c0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-976df7c0f527c36053c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79e27d6a72b0a0836f9c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79e27d6a72b0a0836f9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-05c1c07221a586ce207b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-05c1c07221a586ce207b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-693050cee9fc96ef9ec8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-693050cee9fc96ef9ec8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88a664473a6d9ef93cd2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-88a664473a6d9ef93cd2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57d27143278c8075f6ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-57d27143278c8075f6ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca7683a3fa6fadfc7f25"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca7683a3fa6fadfc7f25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b3506f32ef307bfbea0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b3506f32ef307bfbea0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b43915fa21cad5e545cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b43915fa21cad5e545cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00ebcbb13416c4032b50"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-00ebcbb13416c4032b50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-008e4678e9390ee5499f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-008e4678e9390ee5499f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f5e89a6c78624b87774"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f5e89a6c78624b87774`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92713c53e8d90a4157a6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-92713c53e8d90a4157a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5a6389c9cdc8cdf8691"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c5a6389c9cdc8cdf8691`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9f45f2cdd07fd4ef124d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f45f2cdd07fd4ef124d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e81c2fa83ecdbd2f917"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e81c2fa83ecdbd2f917`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d4c1b03ce35ed7ed62a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d4c1b03ce35ed7ed62a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8704e40d826eddf06c96"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8704e40d826eddf06c96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0d0be5bb23098ce41614"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0d0be5bb23098ce41614`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bcbbc6784dc7d3158ebc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bcbbc6784dc7d3158ebc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3eb238586ef90b30210f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3eb238586ef90b30210f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-331f450ec7ee6edbd036"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-331f450ec7ee6edbd036`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dcd20699a45ff596565d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dcd20699a45ff596565d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80269ca77ab6ecbe6090"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-80269ca77ab6ecbe6090`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf23dcc0fed6514cbdcd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cf23dcc0fed6514cbdcd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-114d43aab3786c15939b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-114d43aab3786c15939b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41ae8fa9a32ed6a15149"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41ae8fa9a32ed6a15149`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a336c5990c81fa399092"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a336c5990c81fa399092`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4737b4fafa88b0f0fd92"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4737b4fafa88b0f0fd92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9872eb8df9e4c8849ce6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9872eb8df9e4c8849ce6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32d01874c935eb5bd023"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32d01874c935eb5bd023`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31d87c003e0b0b7ad02c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-31d87c003e0b0b7ad02c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-886c55a7facac7a3b559"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-886c55a7facac7a3b559`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ba23b95bc3730dd1dc1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0ba23b95bc3730dd1dc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-29bfda7588b5a9b07c95"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-29bfda7588b5a9b07c95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-037928940519be1d957c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-037928940519be1d957c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc8c23fb8cc3c529e14d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fc8c23fb8cc3c529e14d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adc636249e8c88c01849"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-adc636249e8c88c01849`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e194a91bd60c4dba2a6c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e194a91bd60c4dba2a6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72e3ba0a3b4eab61a853"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-72e3ba0a3b4eab61a853`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4dede67a629eb0eb67e3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4dede67a629eb0eb67e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96243c5fc325c7d58ae6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-96243c5fc325c7d58ae6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-y-reversed-diagonal-branch:canonical-southeast | <a href="#case-preview_review-b7a1079d4a2aaa9a2673">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-reversed-diagonal-branch:canonical-top | <a href="#case-preview_review-b50e7477434ee9a5ea30">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-reversed-diagonal-branch:connection-overview | <a href="#case-preview_review-b6fdb141ed359c9a4473">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-diagonal-branch:canonical-southeast</summary>

<a id="case-preview_review-b7a1079d4a2aaa9a2673"></a>

**General: unverified** — `preview_review-b7a1079d4a2aaa9a2673`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-diagonal-branch:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-diagonal-branch:canonical-top</summary>

<a id="case-preview_review-b50e7477434ee9a5ea30"></a>

**General: unverified** — `preview_review-b50e7477434ee9a5ea30`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-diagonal-branch:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-diagonal-branch:connection-overview</summary>

<a id="case-preview_review-b6fdb141ed359c9a4473"></a>

**General: unverified** — `preview_review-b6fdb141ed359c9a4473`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-diagonal-branch:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested another variant with yellow on the opposite physical side and clarified that yellow must remain on the driver's left. This implementation reverses all directed journeys at the original arm positions and uses a separate native phase, component identities, and menu cycle. The original junction and its human observations remain separate.

Follow the [shared observation procedure](../../../../docs/TESTING.md). Copy the exact case ID from the generated checklist, record the installed candidate, pose, environment, and observed behavior, and retain failures or uncertainty. A software pass or preview review does not create a human game pass.
