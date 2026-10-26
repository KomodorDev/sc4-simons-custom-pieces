# HSR Tight Two-Track Corner 23 to 15.5 Metres

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

A 56 m right-angle paired corner descends from the custom 23 m connection to lower 15.5 m HSR. The reverse-direction track climbs; both ends have 8 m flat native collars.

Exact reusable identifier: `hsr-component-tight-paired-curve90-mid-to-l2`.

Footprint: **4 × 4 tiles**. Exact menu name: **HSR Tight Two-Track Corner 23 to 15.5 Metres**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR Tight Two-Track Corner 23 to 15.5 Metres](preview.png)

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
| `Sout` | hsr / 7 / primary | out | [-2.0, -56.0, 23.0]; [0.0, -1.0]; 0.0 | `path-interface-f17a87c40e2280c52126` |
| `Sin` | hsr / 7 / primary | in | [2.0, -56.0, 23.0]; [0.0, 1.0]; 0.0 | `path-interface-c22acb858d4777168a58` |
| `Eout` | hsr / 7 / primary | out | [56.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Ein` | hsr / 7 / primary | in | [56.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Eout` | primary |
| hsr | `Ein` → `Sout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-tight-paired-curve90-mid-to-l2/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-d0768e0a6f5aff280639">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-d0768e0a6f5aff280639"></a>

**General: unverified** — `software_resources-d0768e0a6f5aff280639`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-d0768e0a6f5aff280639">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-d0768e0a6f5aff280639"></a>

**General: unverified** — `software_connectivity-d0768e0a6f5aff280639`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-southeast | <a href="#case-preview_review-c8ceea09195bd3748b8c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-southeast</summary>

<a id="case-preview_review-c8ceea09195bd3748b8c"></a>

**General: unverified** — `preview_review-c8ceea09195bd3748b8c`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-tight-paired-curve90-mid-to-l2:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-f627ea62430d13e37df7">[ ] unverified</a> | <a href="#case-in_game_render-a00c4dcf9b2d966b03e6">[ ] unverified</a> | <a href="#case-in_game_render-a2289220f8f390575e32">[ ] unverified</a> | <a href="#case-in_game_render-ee02fb8e6143d848f5ee">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-f627ea62430d13e37df7"></a>

**0° CCW: unverified** — `in_game_render-f627ea62430d13e37df7`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a00c4dcf9b2d966b03e6"></a>

**90° CCW: unverified** — `in_game_render-a00c4dcf9b2d966b03e6`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a2289220f8f390575e32"></a>

**180° CCW: unverified** — `in_game_render-a2289220f8f390575e32`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ee02fb8e6143d848f5ee"></a>

**270° CCW: unverified** — `in_game_render-ee02fb8e6143d848f5ee`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-f627ea62430d13e37df7">[ ] unverified</a> | <a href="#case-in_game_placement-a00c4dcf9b2d966b03e6">[ ] unverified</a> | <a href="#case-in_game_placement-a2289220f8f390575e32">[ ] unverified</a> | <a href="#case-in_game_placement-ee02fb8e6143d848f5ee">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-f627ea62430d13e37df7"></a>

**0° CCW: unverified** — `in_game_placement-f627ea62430d13e37df7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a00c4dcf9b2d966b03e6"></a>

**90° CCW: unverified** — `in_game_placement-a00c4dcf9b2d966b03e6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a2289220f8f390575e32"></a>

**180° CCW: unverified** — `in_game_placement-a2289220f8f390575e32`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ee02fb8e6143d848f5ee"></a>

**270° CCW: unverified** — `in_game_placement-ee02fb8e6143d848f5ee`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-f627ea62430d13e37df7">[ ] unverified</a> | <a href="#case-in_game_demolition-a00c4dcf9b2d966b03e6">[ ] unverified</a> | <a href="#case-in_game_demolition-a2289220f8f390575e32">[ ] unverified</a> | <a href="#case-in_game_demolition-ee02fb8e6143d848f5ee">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-f627ea62430d13e37df7"></a>

**0° CCW: unverified** — `in_game_demolition-f627ea62430d13e37df7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a00c4dcf9b2d966b03e6"></a>

**90° CCW: unverified** — `in_game_demolition-a00c4dcf9b2d966b03e6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a2289220f8f390575e32"></a>

**180° CCW: unverified** — `in_game_demolition-a2289220f8f390575e32`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ee02fb8e6143d848f5ee"></a>

**270° CCW: unverified** — `in_game_demolition-ee02fb8e6143d848f5ee`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-f627ea62430d13e37df7">[ ] unverified</a> | <a href="#case-in_game_save_reload-a00c4dcf9b2d966b03e6">[ ] unverified</a> | <a href="#case-in_game_save_reload-a2289220f8f390575e32">[ ] unverified</a> | <a href="#case-in_game_save_reload-ee02fb8e6143d848f5ee">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-f627ea62430d13e37df7"></a>

**0° CCW: unverified** — `in_game_save_reload-f627ea62430d13e37df7`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a00c4dcf9b2d966b03e6"></a>

**90° CCW: unverified** — `in_game_save_reload-a00c4dcf9b2d966b03e6`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a2289220f8f390575e32"></a>

**180° CCW: unverified** — `in_game_save_reload-a2289220f8f390575e32`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ee02fb8e6143d848f5ee"></a>

**270° CCW: unverified** — `in_game_save_reload-ee02fb8e6143d848f5ee`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_journey-c609522f866468deda1c">[ ] unverified</a> | <a href="#case-in_game_journey-caca662303c92a69755d">[ ] unverified</a> | <a href="#case-in_game_journey-4224d99b63e3c6dfe042">[ ] unverified</a> | <a href="#case-in_game_journey-fce87cacab3cca4e9739">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout | — | <a href="#case-in_game_journey-c0ea1a301c247af4a030">[ ] unverified</a> | <a href="#case-in_game_journey-0192539723def2c635c0">[ ] unverified</a> | <a href="#case-in_game_journey-debcb4d50826bf0dfe2b">[ ] unverified</a> | <a href="#case-in_game_journey-8f17b5e62232dd993a0f">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_journey-c609522f866468deda1c"></a>

**0° CCW: unverified** — `in_game_journey-c609522f866468deda1c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-caca662303c92a69755d"></a>

**90° CCW: unverified** — `in_game_journey-caca662303c92a69755d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-4224d99b63e3c6dfe042"></a>

**180° CCW: unverified** — `in_game_journey-4224d99b63e3c6dfe042`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-fce87cacab3cca4e9739"></a>

**270° CCW: unverified** — `in_game_journey-fce87cacab3cca4e9739`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout</summary>

<a id="case-in_game_journey-c0ea1a301c247af4a030"></a>

**0° CCW: unverified** — `in_game_journey-c0ea1a301c247af4a030`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-0192539723def2c635c0"></a>

**90° CCW: unverified** — `in_game_journey-0192539723def2c635c0`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-debcb4d50826bf0dfe2b"></a>

**180° CCW: unverified** — `in_game_journey-debcb4d50826bf0dfe2b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-8f17b5e62232dd993a0f"></a>

**270° CCW: unverified** — `in_game_journey-8f17b5e62232dd993a0f`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a5af8eb524560251ee3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94cbded6f06f1c832e30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85bc638ea2f5e4612f2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c573921b8296828f57b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-961647d99405973fe109">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33a6d57149399f3814e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63c9ca69b01c537b0bc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4c619a8b7fd2a283b8b">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a5af8eb524560251ee3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a5af8eb524560251ee3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94cbded6f06f1c832e30"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94cbded6f06f1c832e30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85bc638ea2f5e4612f2e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85bc638ea2f5e4612f2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c573921b8296828f57b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c573921b8296828f57b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-961647d99405973fe109"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-961647d99405973fe109`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33a6d57149399f3814e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-33a6d57149399f3814e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63c9ca69b01c537b0bc0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63c9ca69b01c537b0bc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4c619a8b7fd2a283b8b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4c619a8b7fd2a283b8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

This tight paired graded corner occupies ten cells in a 4 × 4 rectangle, including three structural cells and six literal support centres. Its cardinal displacement is 56 m, its deck width is 15 m, its track offsets are ±2 m, and its flat collars are 8 m. The intermediate paired joint is Custom (23 m), with no nominal level; it does not accept ordinary HSR or a different-width authored narrow L3 interface merely because the path heights agree.

The tight-corner polynomial applies only to those two current recipes. Their independently reviewed minimum radius is 24 m. Their actual maximum grade is approximately 0.1238, inside the unchanged 0.156251 limit. Curvature, grade-change, and 5 × 5 m train-clearance checks remain mandatory. Other curve recipes retain their separate radius limits.

Use the [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
