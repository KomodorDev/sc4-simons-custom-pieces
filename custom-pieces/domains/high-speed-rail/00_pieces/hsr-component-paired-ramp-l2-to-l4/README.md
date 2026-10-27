# HSR Two-Track L2 to L4 Ramp

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

Two adjacent opposite-direction tracks change between 15.5 and 30.5 m; northbound climbs and southbound descends.

Exact reusable identifier: `hsr-component-paired-ramp-l2-to-l4`.

Footprint: **1 × 8 tiles**. Exact menu name: **HSR Two-Track L2 to L4 Ramp**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR Two-Track L2 to L4 Ramp](previews/preview.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/8 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Purpose: describe intrinsic directional interfaces and permitted service journeys.

Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | hsr / 7 / primary | out | [-2.0, -120.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 30.5]; [0.0, -1.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |
| `Sin` | hsr / 7 / primary | in | [2.0, -120.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-9b897a8bacb659f807fe` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 35, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-paired-ramp-l2-to-l4/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-paired-ramp-l2-to-l4/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-21d4d460c1e1b5f0c1e9">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-21d4d460c1e1b5f0c1e9"></a>

**General: unverified** — `software_resources-21d4d460c1e1b5f0c1e9`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-21d4d460c1e1b5f0c1e9">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-21d4d460c1e1b5f0c1e9"></a>

**General: unverified** — `software_connectivity-21d4d460c1e1b5f0c1e9`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-paired-ramp-l2-to-l4:canonical-southeast | <a href="#case-preview_review-7562da2fe1be3af9a6da">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-paired-ramp-l2-to-l4:canonical-southeast</summary>

<a id="case-preview_review-7562da2fe1be3af9a6da"></a>

**General: unverified** — `preview_review-7562da2fe1be3af9a6da`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-paired-ramp-l2-to-l4:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-9787bd83e5c40fde1a1f">[ ] unverified</a> | <a href="#case-in_game_render-78a49cc7fa072b2245e0">[ ] unverified</a> | <a href="#case-in_game_render-26e998fe7f91c177911b">[ ] unverified</a> | <a href="#case-in_game_render-2876d01a5902a2fb9320">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-9787bd83e5c40fde1a1f"></a>

**0° CCW: unverified** — `in_game_render-9787bd83e5c40fde1a1f`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-78a49cc7fa072b2245e0"></a>

**90° CCW: unverified** — `in_game_render-78a49cc7fa072b2245e0`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-26e998fe7f91c177911b"></a>

**180° CCW: unverified** — `in_game_render-26e998fe7f91c177911b`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2876d01a5902a2fb9320"></a>

**270° CCW: unverified** — `in_game_render-2876d01a5902a2fb9320`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-9787bd83e5c40fde1a1f">[ ] unverified</a> | <a href="#case-in_game_placement-78a49cc7fa072b2245e0">[ ] unverified</a> | <a href="#case-in_game_placement-26e998fe7f91c177911b">[ ] unverified</a> | <a href="#case-in_game_placement-2876d01a5902a2fb9320">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-9787bd83e5c40fde1a1f"></a>

**0° CCW: unverified** — `in_game_placement-9787bd83e5c40fde1a1f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-78a49cc7fa072b2245e0"></a>

**90° CCW: unverified** — `in_game_placement-78a49cc7fa072b2245e0`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-26e998fe7f91c177911b"></a>

**180° CCW: unverified** — `in_game_placement-26e998fe7f91c177911b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2876d01a5902a2fb9320"></a>

**270° CCW: unverified** — `in_game_placement-2876d01a5902a2fb9320`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-9787bd83e5c40fde1a1f">[ ] unverified</a> | <a href="#case-in_game_demolition-78a49cc7fa072b2245e0">[ ] unverified</a> | <a href="#case-in_game_demolition-26e998fe7f91c177911b">[ ] unverified</a> | <a href="#case-in_game_demolition-2876d01a5902a2fb9320">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-9787bd83e5c40fde1a1f"></a>

**0° CCW: unverified** — `in_game_demolition-9787bd83e5c40fde1a1f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-78a49cc7fa072b2245e0"></a>

**90° CCW: unverified** — `in_game_demolition-78a49cc7fa072b2245e0`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-26e998fe7f91c177911b"></a>

**180° CCW: unverified** — `in_game_demolition-26e998fe7f91c177911b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2876d01a5902a2fb9320"></a>

**270° CCW: unverified** — `in_game_demolition-2876d01a5902a2fb9320`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-9787bd83e5c40fde1a1f">[ ] unverified</a> | <a href="#case-in_game_save_reload-78a49cc7fa072b2245e0">[ ] unverified</a> | <a href="#case-in_game_save_reload-26e998fe7f91c177911b">[ ] unverified</a> | <a href="#case-in_game_save_reload-2876d01a5902a2fb9320">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-9787bd83e5c40fde1a1f"></a>

**0° CCW: unverified** — `in_game_save_reload-9787bd83e5c40fde1a1f`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-78a49cc7fa072b2245e0"></a>

**90° CCW: unverified** — `in_game_save_reload-78a49cc7fa072b2245e0`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-26e998fe7f91c177911b"></a>

**180° CCW: unverified** — `in_game_save_reload-26e998fe7f91c177911b`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2876d01a5902a2fb9320"></a>

**270° CCW: unverified** — `in_game_save_reload-2876d01a5902a2fb9320`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-c656ab3810a6e37cdae6">[ ] unverified</a> | <a href="#case-in_game_journey-bd35906522be958253ae">[ ] unverified</a> | <a href="#case-in_game_journey-b7e762d639e28606aef3">[ ] unverified</a> | <a href="#case-in_game_journey-6362e887de6e18289ffd">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-de1577e2a14a44e5e73d">[ ] unverified</a> | <a href="#case-in_game_journey-b61b621d1ef0bcf76cfd">[ ] unverified</a> | <a href="#case-in_game_journey-9fe0f55e5bb5420c60fc">[ ] unverified</a> | <a href="#case-in_game_journey-feb7c114e707a1bce6e1">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-c656ab3810a6e37cdae6"></a>

**0° CCW: unverified** — `in_game_journey-c656ab3810a6e37cdae6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-bd35906522be958253ae"></a>

**90° CCW: unverified** — `in_game_journey-bd35906522be958253ae`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-b7e762d639e28606aef3"></a>

**180° CCW: unverified** — `in_game_journey-b7e762d639e28606aef3`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-6362e887de6e18289ffd"></a>

**270° CCW: unverified** — `in_game_journey-6362e887de6e18289ffd`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-de1577e2a14a44e5e73d"></a>

**0° CCW: unverified** — `in_game_journey-de1577e2a14a44e5e73d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-b61b621d1ef0bcf76cfd"></a>

**90° CCW: unverified** — `in_game_journey-b61b621d1ef0bcf76cfd`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-9fe0f55e5bb5420c60fc"></a>

**180° CCW: unverified** — `in_game_journey-9fe0f55e5bb5420c60fc`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-feb7c114e707a1bce6e1"></a>

**270° CCW: unverified** — `in_game_journey-feb7c114e707a1bce6e1`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c96890bd76c03be8c8b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c892312f9b7acf6e865">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dc0a9464f8e8a3f7328">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab4a7968ab77050177d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-71c7bbfd0e14d0fe7220">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-758e2621816e1db4cd22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4b13e6a953f0ea5aa16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e474c0cac44ed1a8e93">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c96890bd76c03be8c8b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c96890bd76c03be8c8b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c892312f9b7acf6e865"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9c892312f9b7acf6e865`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dc0a9464f8e8a3f7328"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0dc0a9464f8e8a3f7328`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab4a7968ab77050177d0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab4a7968ab77050177d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-71c7bbfd0e14d0fe7220"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-71c7bbfd0e14d0fe7220`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-758e2621816e1db4cd22"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-758e2621816e1db4cd22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4b13e6a953f0ea5aa16"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e4b13e6a953f0ea5aa16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e474c0cac44ed1a8e93"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8e474c0cac44ed1a8e93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

This paired ramp occupies one column and eight rows. Its south boundary is at north coordinate −120 m and height 15.5 m; its north boundary is at north coordinate +8 m and height 30.5 m. Both ends have 8 m flat collars. The continuous eased grade has maximum 0.15625 rise/run, and the opposing track descends on the same deck.

Use the [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
