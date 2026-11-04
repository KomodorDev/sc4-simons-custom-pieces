# Testing — DD RHW-4 — Orthogonal Y Connection Core — L1/L2 — Reversed Traffic

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
| `a-b-in` | road / 1 / primary | in | [6.332766, -8.0, 7.5]; [0.2572557340982241, 0.9663433588914366]; 0.0 | `path-interface-7ac653a2387e790053a9` |
| `b-a-out` | road / 1 / primary | out | [6.332766, -8.0, 15.0]; [-0.2572557340982241, -0.9663433588914366]; 0.0 | `path-interface-92892adb3bd2bdba401e` |
| `a-b-out` | road / 1 / primary | out | [6.332766, 8.0, 7.5]; [-0.2572557340982241, 0.9663433588914366]; 0.0 | `path-interface-ac1fd402b55f95edaa5b` |
| `b-a-in` | road / 1 / primary | in | [6.332766, 8.0, 15.0]; [0.2572557340982241, -0.9663433588914366]; 0.0 | `path-interface-72c8b7a87f82a3fe3e76` |
| `b-c-in` | road / 1 / primary | in | [23.700047, 8.0, 12.159544]; [0.8923143757368847, -0.45141450447819453]; -0.248976792 | `path-interface-93f54f456af3587023cf` |
| `a-c-in` | road / 1 / primary | in | [37.321807, -8.0, 7.5]; [0.9475295413188497, 0.31966821601168016]; 0.0 | `path-interface-c791c496692b36ecf9fc` |
| `c-a-out` | road / 1 / primary | out | [37.321807, -8.0, 15.0]; [-0.9475295413188497, -0.31966821601168016]; 0.0 | `path-interface-5176920b754720e94972` |
| `c-b-out` | road / 1 / primary | out | [46.247886, 8.0, 14.711544]; [-0.8870803546319371, 0.4616150392113289]; -0.085894367 | `path-interface-85d9bc718374dfbaaab9` |
| `a-c-out` | road / 1 / primary | out | [72.0, -2.5, 7.5]; [1.0, 0.0]; 0.0 | `path-interface-b2fe320b9e0bb31bdb27` |
| `c-a-in` | road / 1 / primary | in | [72.0, -2.5, 15.0]; [-1.0, 0.0]; 0.0 | `path-interface-02def3c4ce1dd299e969` |
| `b-c-out` | road / 1 / primary | out | [72.0, 2.5, 7.5]; [1.0, 0.0]; 0.0 | `path-interface-fddc704c2b84d595ec6f` |
| `c-b-in` | road / 1 / primary | in | [72.0, 2.5, 15.0]; [-1.0, 0.0]; 0.0 | `path-interface-991f143956c37b818e99` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `a-b-in` → `a-b-out` | primary |
| road | `b-a-in` → `b-a-out` | primary |
| road | `b-c-in` → `b-c-out` | primary |
| road | `a-c-in` → `a-c-out` | primary |
| road | `c-a-in` → `c-a-out` | primary |
| road | `c-b-in` → `c-b-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `a-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-b-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-a-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `b-c-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `a-c-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `c-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-a-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `b-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `a-b-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `c-a-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `a-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `c-b-in` | road / `b-c-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the audited NAM 50 right-hand-traffic inputs and a disposable flat test city. Install deliberately, restart the game, and place all three reversed components afresh using the [placement table](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/README.md#3-placements). This type is **P03** at **(X1, Y3)**, and its native socket is **(X6, Y3)**. Keep the original Y's types and observations separate.

The upper southwest deck is outgoing, and both upper branch decks are incoming. The lower decks carry the opposite directions. Every yellow line must be on the driver's left. This component's east orthogonal helper is `57530000` at quarter-turn pose 1. The assembly's A/B diagonal helpers instead use `57530200` at poses 0 and 3; the original Y's diagonal `57530900` helper phase is not a substitute for those reversed interfaces.

## 3. Software checks

Follow the [exact build, saved-resource, connector, rendering, and regression commands](../../01_assemblies/ddrhw-compact-diagonal-y-junction-reversed/TESTING.md#3-software-checks). The checker reads the saved models, traffic paths, texture coordinates, and construction rules. Texture coordinates, also called UV coordinates, select positions in a texture image. Source diagrams alone cannot establish these checks.

The complete assembly must pass ownership, all six journeys, native profile contact, car-strip clearance, full-width underside depth, closed road and barrier shells, support contacts, and actual texture-pixel marking checks. The original type's accepted geometry, exceptions, software counts, and human report do not establish the reversed type's result.

## 4. Game checks

1. Find the exact reversed assembly button, and verify the component's tooltip and Tab order. Check that the original assembly remains available.
2. Place **P03** at **(X1, Y3)**, inspect its entire occupied shape, and verify its ordinary native socket at **(X6, Y3)**. Check automatic socket appearance, outward native dragging, and connection to a prebuilt matching approach separately.
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
- [ ] Route Query: 0/24 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/24 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 189, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-y-reversed-orthogonal-core/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-y-reversed-orthogonal-core/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-4165cba542545e361c35">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-4165cba542545e361c35"></a>

**General: unverified** — `software_resources-4165cba542545e361c35`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-4165cba542545e361c35">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-4165cba542545e361c35"></a>

**General: unverified** — `software_connectivity-4165cba542545e361c35`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-af8a4bc9c7efcb882175">[ ] unverified</a> | <a href="#case-in_game_render-088ef25b68254e8f97cb">[ ] unverified</a> | <a href="#case-in_game_render-e4ae7db044a4235a885c">[ ] unverified</a> | <a href="#case-in_game_render-85ce467e39bb9e36bfd5">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-af8a4bc9c7efcb882175"></a>

**0° CCW: unverified** — `in_game_render-af8a4bc9c7efcb882175`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-088ef25b68254e8f97cb"></a>

**90° CCW: unverified** — `in_game_render-088ef25b68254e8f97cb`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e4ae7db044a4235a885c"></a>

**180° CCW: unverified** — `in_game_render-e4ae7db044a4235a885c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-85ce467e39bb9e36bfd5"></a>

**270° CCW: unverified** — `in_game_render-85ce467e39bb9e36bfd5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-af8a4bc9c7efcb882175">[ ] unverified</a> | <a href="#case-in_game_placement-088ef25b68254e8f97cb">[ ] unverified</a> | <a href="#case-in_game_placement-e4ae7db044a4235a885c">[ ] unverified</a> | <a href="#case-in_game_placement-85ce467e39bb9e36bfd5">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-af8a4bc9c7efcb882175"></a>

**0° CCW: unverified** — `in_game_placement-af8a4bc9c7efcb882175`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-088ef25b68254e8f97cb"></a>

**90° CCW: unverified** — `in_game_placement-088ef25b68254e8f97cb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e4ae7db044a4235a885c"></a>

**180° CCW: unverified** — `in_game_placement-e4ae7db044a4235a885c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-85ce467e39bb9e36bfd5"></a>

**270° CCW: unverified** — `in_game_placement-85ce467e39bb9e36bfd5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-af8a4bc9c7efcb882175">[ ] unverified</a> | <a href="#case-in_game_demolition-088ef25b68254e8f97cb">[ ] unverified</a> | <a href="#case-in_game_demolition-e4ae7db044a4235a885c">[ ] unverified</a> | <a href="#case-in_game_demolition-85ce467e39bb9e36bfd5">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-af8a4bc9c7efcb882175"></a>

**0° CCW: unverified** — `in_game_demolition-af8a4bc9c7efcb882175`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-088ef25b68254e8f97cb"></a>

**90° CCW: unverified** — `in_game_demolition-088ef25b68254e8f97cb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e4ae7db044a4235a885c"></a>

**180° CCW: unverified** — `in_game_demolition-e4ae7db044a4235a885c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-85ce467e39bb9e36bfd5"></a>

**270° CCW: unverified** — `in_game_demolition-85ce467e39bb9e36bfd5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-af8a4bc9c7efcb882175">[ ] unverified</a> | <a href="#case-in_game_save_reload-088ef25b68254e8f97cb">[ ] unverified</a> | <a href="#case-in_game_save_reload-e4ae7db044a4235a885c">[ ] unverified</a> | <a href="#case-in_game_save_reload-85ce467e39bb9e36bfd5">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-af8a4bc9c7efcb882175"></a>

**0° CCW: unverified** — `in_game_save_reload-af8a4bc9c7efcb882175`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-088ef25b68254e8f97cb"></a>

**90° CCW: unverified** — `in_game_save_reload-088ef25b68254e8f97cb`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e4ae7db044a4235a885c"></a>

**180° CCW: unverified** — `in_game_save_reload-e4ae7db044a4235a885c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-85ce467e39bb9e36bfd5"></a>

**270° CCW: unverified** — `in_game_save_reload-85ce467e39bb9e36bfd5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_route_query-fe7c01d49b0a96b35427">[ ] unverified</a> | <a href="#case-in_game_route_query-ad80a2b79ffabab1f9ac">[ ] unverified</a> | <a href="#case-in_game_route_query-da89c0b8a23b7ca3a974">[ ] unverified</a> | <a href="#case-in_game_route_query-c43d87e2c662fdc396d0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_route_query-5b96428d575eba8323cf">[ ] unverified</a> | <a href="#case-in_game_route_query-17d8ab81d134ebdb9c9e">[ ] unverified</a> | <a href="#case-in_game_route_query-4ce76b3c6286cf9a40ba">[ ] unverified</a> | <a href="#case-in_game_route_query-f19030504310690901cf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out | — | <a href="#case-in_game_route_query-295add80c99d169bf040">[ ] unverified</a> | <a href="#case-in_game_route_query-95b8f75fc1f12c770c0a">[ ] unverified</a> | <a href="#case-in_game_route_query-5d866a243ac258010c38">[ ] unverified</a> | <a href="#case-in_game_route_query-36487aa215c1665f2fd6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out | — | <a href="#case-in_game_route_query-213f3d041b6219b97307">[ ] unverified</a> | <a href="#case-in_game_route_query-21cff48e94d59d776167">[ ] unverified</a> | <a href="#case-in_game_route_query-9d81b14d36e549529168">[ ] unverified</a> | <a href="#case-in_game_route_query-df3874f0929a68b93623">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out | — | <a href="#case-in_game_route_query-1dd6bd6a13b810ad058f">[ ] unverified</a> | <a href="#case-in_game_route_query-6624a4fdb31a7b71d098">[ ] unverified</a> | <a href="#case-in_game_route_query-63bbc9993f17eb1ba979">[ ] unverified</a> | <a href="#case-in_game_route_query-bc7f36cf0448bf53483e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out | — | <a href="#case-in_game_route_query-334e8545d173f700a70a">[ ] unverified</a> | <a href="#case-in_game_route_query-b10c6a5ca4eb9c084108">[ ] unverified</a> | <a href="#case-in_game_route_query-f3d5b5c320feba41ad60">[ ] unverified</a> | <a href="#case-in_game_route_query-4787c5eed9cb97195c03">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_route_query-fe7c01d49b0a96b35427"></a>

**0° CCW: unverified** — `in_game_route_query-fe7c01d49b0a96b35427`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-ad80a2b79ffabab1f9ac"></a>

**90° CCW: unverified** — `in_game_route_query-ad80a2b79ffabab1f9ac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-da89c0b8a23b7ca3a974"></a>

**180° CCW: unverified** — `in_game_route_query-da89c0b8a23b7ca3a974`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_route_query-c43d87e2c662fdc396d0"></a>

**270° CCW: unverified** — `in_game_route_query-c43d87e2c662fdc396d0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_route_query-5b96428d575eba8323cf"></a>

**0° CCW: unverified** — `in_game_route_query-5b96428d575eba8323cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-17d8ab81d134ebdb9c9e"></a>

**90° CCW: unverified** — `in_game_route_query-17d8ab81d134ebdb9c9e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-4ce76b3c6286cf9a40ba"></a>

**180° CCW: unverified** — `in_game_route_query-4ce76b3c6286cf9a40ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_route_query-f19030504310690901cf"></a>

**270° CCW: unverified** — `in_game_route_query-f19030504310690901cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out</summary>

<a id="case-in_game_route_query-295add80c99d169bf040"></a>

**0° CCW: unverified** — `in_game_route_query-295add80c99d169bf040`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-95b8f75fc1f12c770c0a"></a>

**90° CCW: unverified** — `in_game_route_query-95b8f75fc1f12c770c0a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-5d866a243ac258010c38"></a>

**180° CCW: unverified** — `in_game_route_query-5d866a243ac258010c38`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_route_query-36487aa215c1665f2fd6"></a>

**270° CCW: unverified** — `in_game_route_query-36487aa215c1665f2fd6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out</summary>

<a id="case-in_game_route_query-213f3d041b6219b97307"></a>

**0° CCW: unverified** — `in_game_route_query-213f3d041b6219b97307`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-21cff48e94d59d776167"></a>

**90° CCW: unverified** — `in_game_route_query-21cff48e94d59d776167`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-9d81b14d36e549529168"></a>

**180° CCW: unverified** — `in_game_route_query-9d81b14d36e549529168`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_route_query-df3874f0929a68b93623"></a>

**270° CCW: unverified** — `in_game_route_query-df3874f0929a68b93623`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out</summary>

<a id="case-in_game_route_query-1dd6bd6a13b810ad058f"></a>

**0° CCW: unverified** — `in_game_route_query-1dd6bd6a13b810ad058f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-6624a4fdb31a7b71d098"></a>

**90° CCW: unverified** — `in_game_route_query-6624a4fdb31a7b71d098`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-63bbc9993f17eb1ba979"></a>

**180° CCW: unverified** — `in_game_route_query-63bbc9993f17eb1ba979`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_route_query-bc7f36cf0448bf53483e"></a>

**270° CCW: unverified** — `in_game_route_query-bc7f36cf0448bf53483e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out</summary>

<a id="case-in_game_route_query-334e8545d173f700a70a"></a>

**0° CCW: unverified** — `in_game_route_query-334e8545d173f700a70a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-b10c6a5ca4eb9c084108"></a>

**90° CCW: unverified** — `in_game_route_query-b10c6a5ca4eb9c084108`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-f3d5b5c320feba41ad60"></a>

**180° CCW: unverified** — `in_game_route_query-f3d5b5c320feba41ad60`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_route_query-4787c5eed9cb97195c03"></a>

**270° CCW: unverified** — `in_game_route_query-4787c5eed9cb97195c03`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out | — | <a href="#case-in_game_visible_travel-fe7c01d49b0a96b35427">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ad80a2b79ffabab1f9ac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-da89c0b8a23b7ca3a974">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c43d87e2c662fdc396d0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out | — | <a href="#case-in_game_visible_travel-5b96428d575eba8323cf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-17d8ab81d134ebdb9c9e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4ce76b3c6286cf9a40ba">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f19030504310690901cf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out | — | <a href="#case-in_game_visible_travel-295add80c99d169bf040">[ ] unverified</a> | <a href="#case-in_game_visible_travel-95b8f75fc1f12c770c0a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5d866a243ac258010c38">[ ] unverified</a> | <a href="#case-in_game_visible_travel-36487aa215c1665f2fd6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out | — | <a href="#case-in_game_visible_travel-213f3d041b6219b97307">[ ] unverified</a> | <a href="#case-in_game_visible_travel-21cff48e94d59d776167">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9d81b14d36e549529168">[ ] unverified</a> | <a href="#case-in_game_visible_travel-df3874f0929a68b93623">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out | — | <a href="#case-in_game_visible_travel-1dd6bd6a13b810ad058f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6624a4fdb31a7b71d098">[ ] unverified</a> | <a href="#case-in_game_visible_travel-63bbc9993f17eb1ba979">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bc7f36cf0448bf53483e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out | — | <a href="#case-in_game_visible_travel-334e8545d173f700a70a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b10c6a5ca4eb9c084108">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f3d5b5c320feba41ad60">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4787c5eed9cb97195c03">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out</summary>

<a id="case-in_game_visible_travel-fe7c01d49b0a96b35427"></a>

**0° CCW: unverified** — `in_game_visible_travel-fe7c01d49b0a96b35427`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-ad80a2b79ffabab1f9ac"></a>

**90° CCW: unverified** — `in_game_visible_travel-ad80a2b79ffabab1f9ac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-da89c0b8a23b7ca3a974"></a>

**180° CCW: unverified** — `in_game_visible_travel-da89c0b8a23b7ca3a974`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-c43d87e2c662fdc396d0"></a>

**270° CCW: unverified** — `in_game_visible_travel-c43d87e2c662fdc396d0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-b-in>a-b-out; entry: a-b-in; exit: a-b-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out</summary>

<a id="case-in_game_visible_travel-5b96428d575eba8323cf"></a>

**0° CCW: unverified** — `in_game_visible_travel-5b96428d575eba8323cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-17d8ab81d134ebdb9c9e"></a>

**90° CCW: unverified** — `in_game_visible_travel-17d8ab81d134ebdb9c9e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-4ce76b3c6286cf9a40ba"></a>

**180° CCW: unverified** — `in_game_visible_travel-4ce76b3c6286cf9a40ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-f19030504310690901cf"></a>

**270° CCW: unverified** — `in_game_visible_travel-f19030504310690901cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-a-in>b-a-out; entry: b-a-in; exit: b-a-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out</summary>

<a id="case-in_game_visible_travel-295add80c99d169bf040"></a>

**0° CCW: unverified** — `in_game_visible_travel-295add80c99d169bf040`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-95b8f75fc1f12c770c0a"></a>

**90° CCW: unverified** — `in_game_visible_travel-95b8f75fc1f12c770c0a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-5d866a243ac258010c38"></a>

**180° CCW: unverified** — `in_game_visible_travel-5d866a243ac258010c38`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-36487aa215c1665f2fd6"></a>

**270° CCW: unverified** — `in_game_visible_travel-36487aa215c1665f2fd6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:b-c-in>b-c-out; entry: b-c-in; exit: b-c-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out</summary>

<a id="case-in_game_visible_travel-213f3d041b6219b97307"></a>

**0° CCW: unverified** — `in_game_visible_travel-213f3d041b6219b97307`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-21cff48e94d59d776167"></a>

**90° CCW: unverified** — `in_game_visible_travel-21cff48e94d59d776167`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-9d81b14d36e549529168"></a>

**180° CCW: unverified** — `in_game_visible_travel-9d81b14d36e549529168`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

<a id="case-in_game_visible_travel-df3874f0929a68b93623"></a>

**270° CCW: unverified** — `in_game_visible_travel-df3874f0929a68b93623`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:a-c-in>a-c-out; entry: a-c-in; exit: a-c-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out</summary>

<a id="case-in_game_visible_travel-1dd6bd6a13b810ad058f"></a>

**0° CCW: unverified** — `in_game_visible_travel-1dd6bd6a13b810ad058f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-6624a4fdb31a7b71d098"></a>

**90° CCW: unverified** — `in_game_visible_travel-6624a4fdb31a7b71d098`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-63bbc9993f17eb1ba979"></a>

**180° CCW: unverified** — `in_game_visible_travel-63bbc9993f17eb1ba979`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

<a id="case-in_game_visible_travel-bc7f36cf0448bf53483e"></a>

**270° CCW: unverified** — `in_game_visible_travel-bc7f36cf0448bf53483e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-a-in>c-a-out; entry: c-a-in; exit: c-a-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out</summary>

<a id="case-in_game_visible_travel-334e8545d173f700a70a"></a>

**0° CCW: unverified** — `in_game_visible_travel-334e8545d173f700a70a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-b10c6a5ca4eb9c084108"></a>

**90° CCW: unverified** — `in_game_visible_travel-b10c6a5ca4eb9c084108`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-f3d5b5c320feba41ad60"></a>

**180° CCW: unverified** — `in_game_visible_travel-f3d5b5c320feba41ad60`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

<a id="case-in_game_visible_travel-4787c5eed9cb97195c03"></a>

**270° CCW: unverified** — `in_game_visible_travel-4787c5eed9cb97195c03`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:c-b-in>c-b-out; entry: c-b-in; exit: c-b-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 120 cases; unverified: 120</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9ed4f7db290a92c79c0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5521ed7582b134aa1ab3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29c1a6b642a8f8a70784">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79d35d367d97421f3923">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5f86d7591cba70996ab9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-103714d701415488ee4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-107982195edafefb56e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ca4d3b260974324db54">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b3d7bef5f9c3c46f4493">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e91f195cbe18665dc390">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b4f79d900519ead8bce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35d411eacf5f3ff80a7b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-369f2af1254a78f5c508">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd8d2105dbf22601822b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4760bd138f63fe492176">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4db7d4aba651af80c704">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5cb4f8e8aee96086e3cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8f23992d565ccde295a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fe44b13ad7430e87ff1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c3257acb32f67dd405b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5de982b8f0b9d6f5e38f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee361181b691dec0d259">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55998ac55bdb7e988e7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3df4fa377fad90b5efff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-55cc930e52335e08626c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5bc54916a18f0fd50af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6d1a5ddf5d6373df1b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4683ce26097d4f94d0fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc46e053ca83f7d22e39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adfa0dfa5d28db12dc68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a96cfd02074b21f0e085">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-046d328561faf7005c09">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a37a4c60befe02fc1173">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ad8ad899cb50d574f56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-968089806009bbb9fac5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd05397ad4d62bb86ee9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e26e24f03c2b3fa95be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd2630f05480b58e2aef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-760820cb5aeed657be6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f390214399880c0db716">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-652509d59657d33910da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac262f3a7c4a3989bb20">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-443707cac077bda666d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d96f7a9d89ad0ba52f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a06e8cc542d6eed20309">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d0f599f1dbedf5d28bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07c1cb8edb9942102df7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2d1614812e7e61f0a02">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ccface7371e74e8d677f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b6522c8386753b3be0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4d218f0290e5d512dbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ea03ac9c1beb07c6d49">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ceaec1a2a592a6837470">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d41b0176ecfa1cc102e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8483f6f564acde93ded6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1096598d3dccd5f88ec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2ebcad5dce135b4667c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-204edb9fd700a1c54968">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-701fb392e032f38b94f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-494d422157431efcdc76">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a378e7ad8a89c2c8332c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06b3559dd0528922be98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8133d11d31ae056001d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c26419956787664d8440">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b3c70abb4a1dc3ada96c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b1658787867ec1babd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50bcc196a41a64adecca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68f04a986988f173957f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-842314025ba5d77c97c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc9c76ba622319aa1701">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27a47ace3acbc5c2b1b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2509186a79b5da972f21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e0a35844d3871430ec16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-558c9781abeb329c8f92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49e1e32e5e105456a02a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98e45e98b5cd1c00eeba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ef468d3be70dadf5a303">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb70cf8269234a3c6459">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-970ecc99f2992272dbdf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e955b7af925b6dd174ba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ff679700e06e6ccd3a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7372fc384e14fe083a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b65d181a484ad571830">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f803bf403dd29e7f697c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9dadf5649f2b29173b49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d1c36ce36c47b06d9ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0ac89da534102b6aae3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cf429136b58e6642840">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e19646300424981c2cbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0e53294b91ebf44ef71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fac5b57136c3a719b3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5aac6863c994931a7ca3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-05de2e86bd72c422ac31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aab7f6e296ebf8f045c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2291830b6619e3f58d80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25a4d1a12c03e49e9813">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2b09dff078e41000d50d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36ca037c1f88c0d0d981">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b880d1e83d46e12e7beb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd05a389dabf2f3aa04b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2d52096fa98119e54780">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99590ab4c2a24aef28cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3adab45a5ceec1a59d14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-174df944fadffee01ddb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8cddc0af8afe11c00823">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f82072a47449991aac60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7103a26bdb81c3df45e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67ecd7143c646fc52cc0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-905aa8d40901cfbd4640">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d6113f14c9f8ba5508f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2c6b9d16d9ef36da954">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38d3c0da103c5e29de2a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-48c03611c62e106192f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e35eca5982e17111063">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c636d062982d00c4e95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdab89d096b45774ab5f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-519d5bc9c14c5b345f92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46f71a6979b114cc7c17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d03c86cc764c96778fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba0bc987fccad5eefe00">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9ed4f7db290a92c79c0d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9ed4f7db290a92c79c0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5521ed7582b134aa1ab3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5521ed7582b134aa1ab3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29c1a6b642a8f8a70784"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-29c1a6b642a8f8a70784`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79d35d367d97421f3923"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79d35d367d97421f3923`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5f86d7591cba70996ab9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5f86d7591cba70996ab9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-103714d701415488ee4a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-103714d701415488ee4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-107982195edafefb56e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-107982195edafefb56e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ca4d3b260974324db54"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ca4d3b260974324db54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b3d7bef5f9c3c46f4493"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b3d7bef5f9c3c46f4493`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e91f195cbe18665dc390"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e91f195cbe18665dc390`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b4f79d900519ead8bce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5b4f79d900519ead8bce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35d411eacf5f3ff80a7b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-35d411eacf5f3ff80a7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-369f2af1254a78f5c508"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-369f2af1254a78f5c508`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd8d2105dbf22601822b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bd8d2105dbf22601822b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4760bd138f63fe492176"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4760bd138f63fe492176`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4db7d4aba651af80c704"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4db7d4aba651af80c704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5cb4f8e8aee96086e3cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5cb4f8e8aee96086e3cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8f23992d565ccde295a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c8f23992d565ccde295a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fe44b13ad7430e87ff1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4fe44b13ad7430e87ff1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c3257acb32f67dd405b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2c3257acb32f67dd405b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5de982b8f0b9d6f5e38f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5de982b8f0b9d6f5e38f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee361181b691dec0d259"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ee361181b691dec0d259`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55998ac55bdb7e988e7b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-55998ac55bdb7e988e7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3df4fa377fad90b5efff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3df4fa377fad90b5efff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-55cc930e52335e08626c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-55cc930e52335e08626c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5bc54916a18f0fd50af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d5bc54916a18f0fd50af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6d1a5ddf5d6373df1b9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d6d1a5ddf5d6373df1b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4683ce26097d4f94d0fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4683ce26097d4f94d0fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc46e053ca83f7d22e39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc46e053ca83f7d22e39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adfa0dfa5d28db12dc68"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-adfa0dfa5d28db12dc68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a96cfd02074b21f0e085"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a96cfd02074b21f0e085`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-046d328561faf7005c09"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-046d328561faf7005c09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a37a4c60befe02fc1173"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a37a4c60befe02fc1173`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ad8ad899cb50d574f56"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ad8ad899cb50d574f56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-968089806009bbb9fac5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-968089806009bbb9fac5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd05397ad4d62bb86ee9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dd05397ad4d62bb86ee9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e26e24f03c2b3fa95be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e26e24f03c2b3fa95be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd2630f05480b58e2aef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dd2630f05480b58e2aef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-760820cb5aeed657be6f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-760820cb5aeed657be6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f390214399880c0db716"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f390214399880c0db716`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-652509d59657d33910da"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-652509d59657d33910da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac262f3a7c4a3989bb20"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ac262f3a7c4a3989bb20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-443707cac077bda666d6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-443707cac077bda666d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d96f7a9d89ad0ba52f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d96f7a9d89ad0ba52f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a06e8cc542d6eed20309"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a06e8cc542d6eed20309`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d0f599f1dbedf5d28bc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d0f599f1dbedf5d28bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07c1cb8edb9942102df7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-07c1cb8edb9942102df7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2d1614812e7e61f0a02"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2d1614812e7e61f0a02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ccface7371e74e8d677f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ccface7371e74e8d677f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b6522c8386753b3be0c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b6522c8386753b3be0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4d218f0290e5d512dbc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4d218f0290e5d512dbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ea03ac9c1beb07c6d49"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ea03ac9c1beb07c6d49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ceaec1a2a592a6837470"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ceaec1a2a592a6837470`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d41b0176ecfa1cc102e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d41b0176ecfa1cc102e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8483f6f564acde93ded6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8483f6f564acde93ded6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1096598d3dccd5f88ec"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d1096598d3dccd5f88ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2ebcad5dce135b4667c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2ebcad5dce135b4667c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-204edb9fd700a1c54968"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-204edb9fd700a1c54968`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-701fb392e032f38b94f1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-701fb392e032f38b94f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-494d422157431efcdc76"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-494d422157431efcdc76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: b-c-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a378e7ad8a89c2c8332c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a378e7ad8a89c2c8332c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06b3559dd0528922be98"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-06b3559dd0528922be98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8133d11d31ae056001d7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8133d11d31ae056001d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c26419956787664d8440"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c26419956787664d8440`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b3c70abb4a1dc3ada96c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b3c70abb4a1dc3ada96c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b1658787867ec1babd6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b1658787867ec1babd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50bcc196a41a64adecca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-50bcc196a41a64adecca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68f04a986988f173957f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68f04a986988f173957f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-842314025ba5d77c97c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-842314025ba5d77c97c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc9c76ba622319aa1701"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cc9c76ba622319aa1701`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27a47ace3acbc5c2b1b5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27a47ace3acbc5c2b1b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2509186a79b5da972f21"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2509186a79b5da972f21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e0a35844d3871430ec16"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e0a35844d3871430ec16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-558c9781abeb329c8f92"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-558c9781abeb329c8f92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49e1e32e5e105456a02a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-49e1e32e5e105456a02a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98e45e98b5cd1c00eeba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-98e45e98b5cd1c00eeba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ef468d3be70dadf5a303"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ef468d3be70dadf5a303`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb70cf8269234a3c6459"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fb70cf8269234a3c6459`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-970ecc99f2992272dbdf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-970ecc99f2992272dbdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e955b7af925b6dd174ba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e955b7af925b6dd174ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: a-c-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ff679700e06e6ccd3a0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ff679700e06e6ccd3a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7372fc384e14fe083a8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b7372fc384e14fe083a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b65d181a484ad571830"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4b65d181a484ad571830`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f803bf403dd29e7f697c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f803bf403dd29e7f697c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9dadf5649f2b29173b49"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9dadf5649f2b29173b49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d1c36ce36c47b06d9ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6d1c36ce36c47b06d9ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0ac89da534102b6aae3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0ac89da534102b6aae3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cf429136b58e6642840"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6cf429136b58e6642840`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e19646300424981c2cbe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e19646300424981c2cbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0e53294b91ebf44ef71"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e0e53294b91ebf44ef71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fac5b57136c3a719b3c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8fac5b57136c3a719b3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5aac6863c994931a7ca3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5aac6863c994931a7ca3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: c-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-05de2e86bd72c422ac31"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-05de2e86bd72c422ac31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aab7f6e296ebf8f045c5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aab7f6e296ebf8f045c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2291830b6619e3f58d80"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2291830b6619e3f58d80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25a4d1a12c03e49e9813"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-25a4d1a12c03e49e9813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2b09dff078e41000d50d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2b09dff078e41000d50d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36ca037c1f88c0d0d981"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-36ca037c1f88c0d0d981`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b880d1e83d46e12e7beb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b880d1e83d46e12e7beb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd05a389dabf2f3aa04b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd05a389dabf2f3aa04b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-a-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2d52096fa98119e54780"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d52096fa98119e54780`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99590ab4c2a24aef28cc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-99590ab4c2a24aef28cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3adab45a5ceec1a59d14"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3adab45a5ceec1a59d14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-174df944fadffee01ddb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-174df944fadffee01ddb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8cddc0af8afe11c00823"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8cddc0af8afe11c00823`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f82072a47449991aac60"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f82072a47449991aac60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7103a26bdb81c3df45e4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7103a26bdb81c3df45e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67ecd7143c646fc52cc0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-67ecd7143c646fc52cc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-b-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-905aa8d40901cfbd4640"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-905aa8d40901cfbd4640`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d6113f14c9f8ba5508f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d6113f14c9f8ba5508f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2c6b9d16d9ef36da954"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2c6b9d16d9ef36da954`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38d3c0da103c5e29de2a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-38d3c0da103c5e29de2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: c-a-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-48c03611c62e106192f0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-48c03611c62e106192f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e35eca5982e17111063"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e35eca5982e17111063`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c636d062982d00c4e95"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9c636d062982d00c4e95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdab89d096b45774ab5f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bdab89d096b45774ab5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: a-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-519d5bc9c14c5b345f92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-519d5bc9c14c5b345f92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46f71a6979b114cc7c17"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-46f71a6979b114cc7c17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d03c86cc764c96778fc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8d03c86cc764c96778fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba0bc987fccad5eefe00"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ba0bc987fccad5eefe00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: c-b-in; to port: b-c-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-y-reversed-orthogonal-core:canonical-southeast | <a href="#case-preview_review-1af901df4100511f9681">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-reversed-orthogonal-core:canonical-top | <a href="#case-preview_review-8206713d6e7447740e54">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-y-reversed-orthogonal-core:connection-overview | <a href="#case-preview_review-5ade6409a3516829dd09">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-orthogonal-core:canonical-southeast</summary>

<a id="case-preview_review-1af901df4100511f9681"></a>

**General: unverified** — `preview_review-1af901df4100511f9681`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-orthogonal-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-orthogonal-core:canonical-top</summary>

<a id="case-preview_review-8206713d6e7447740e54"></a>

**General: unverified** — `preview_review-8206713d6e7447740e54`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-orthogonal-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-y-reversed-orthogonal-core:connection-overview</summary>

<a id="case-preview_review-5ade6409a3516829dd09"></a>

**General: unverified** — `preview_review-5ade6409a3516829dd09`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-y-reversed-orthogonal-core:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested another variant with yellow on the opposite physical side and clarified that yellow must remain on the driver's left. This implementation reverses all directed journeys at the original arm positions and uses a separate native phase, component identities, and menu cycle. The original junction and its human observations remain separate.

Follow the [shared observation procedure](../../../../docs/TESTING.md). Copy the exact case ID from the generated checklist, record the installed candidate, pose, environment, and observed behavior, and retain failures or uncertainty. A software pass or preview review does not create a human game pass.
