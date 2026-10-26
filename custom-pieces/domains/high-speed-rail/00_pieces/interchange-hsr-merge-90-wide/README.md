# HSR L2 Merge 90 Degree Wide

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR L2 Merge 90 Degree Wide. Fixed click-to-place piece in a 6 by 6 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `interchange-hsr-merge-90-wide`.

Footprint: **6 × 6 tiles**. Exact menu name: **HSR L2 Merge 90 Degree Wide**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.json).

![HSR L2 Merge 90 Degree Wide](preview.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/12 applicable cases passed; 0 failed, 0 stale.

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
| `Sout` | hsr / 7 / primary | out | [-2.0, -88.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -88.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Bin` | hsr / 7 / primary | in | [88.0, -80.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-ac60d237d23f01143255` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Bin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Bin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 43, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-hsr-merge-90-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-hsr-merge-90-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-439ed010d087dcdf36c5">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-439ed010d087dcdf36c5"></a>

**General: unverified** — `software_resources-439ed010d087dcdf36c5`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-439ed010d087dcdf36c5">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-439ed010d087dcdf36c5"></a>

**General: unverified** — `software_connectivity-439ed010d087dcdf36c5`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-hsr-merge-90-wide:canonical-southeast | <a href="#case-preview_review-d234f8cc0e8ef047f0bf">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-hsr-merge-90-wide:canonical-southeast</summary>

<a id="case-preview_review-d234f8cc0e8ef047f0bf"></a>

**General: unverified** — `preview_review-d234f8cc0e8ef047f0bf`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-hsr-merge-90-wide:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-008e1fa1293dc40c526d">[ ] unverified</a> | <a href="#case-in_game_render-525bb499fea34afcd6dd">[ ] unverified</a> | <a href="#case-in_game_render-fdcd119df80336e619db">[ ] unverified</a> | <a href="#case-in_game_render-9fa2e9b3facba8f7ab81">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-008e1fa1293dc40c526d"></a>

**0° CCW: unverified** — `in_game_render-008e1fa1293dc40c526d`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-525bb499fea34afcd6dd"></a>

**90° CCW: unverified** — `in_game_render-525bb499fea34afcd6dd`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-fdcd119df80336e619db"></a>

**180° CCW: unverified** — `in_game_render-fdcd119df80336e619db`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9fa2e9b3facba8f7ab81"></a>

**270° CCW: unverified** — `in_game_render-9fa2e9b3facba8f7ab81`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-008e1fa1293dc40c526d">[ ] unverified</a> | <a href="#case-in_game_placement-525bb499fea34afcd6dd">[ ] unverified</a> | <a href="#case-in_game_placement-fdcd119df80336e619db">[ ] unverified</a> | <a href="#case-in_game_placement-9fa2e9b3facba8f7ab81">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-008e1fa1293dc40c526d"></a>

**0° CCW: unverified** — `in_game_placement-008e1fa1293dc40c526d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-525bb499fea34afcd6dd"></a>

**90° CCW: unverified** — `in_game_placement-525bb499fea34afcd6dd`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-fdcd119df80336e619db"></a>

**180° CCW: unverified** — `in_game_placement-fdcd119df80336e619db`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9fa2e9b3facba8f7ab81"></a>

**270° CCW: unverified** — `in_game_placement-9fa2e9b3facba8f7ab81`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-008e1fa1293dc40c526d">[ ] unverified</a> | <a href="#case-in_game_demolition-525bb499fea34afcd6dd">[ ] unverified</a> | <a href="#case-in_game_demolition-fdcd119df80336e619db">[ ] unverified</a> | <a href="#case-in_game_demolition-9fa2e9b3facba8f7ab81">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-008e1fa1293dc40c526d"></a>

**0° CCW: unverified** — `in_game_demolition-008e1fa1293dc40c526d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-525bb499fea34afcd6dd"></a>

**90° CCW: unverified** — `in_game_demolition-525bb499fea34afcd6dd`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-fdcd119df80336e619db"></a>

**180° CCW: unverified** — `in_game_demolition-fdcd119df80336e619db`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9fa2e9b3facba8f7ab81"></a>

**270° CCW: unverified** — `in_game_demolition-9fa2e9b3facba8f7ab81`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-008e1fa1293dc40c526d">[ ] unverified</a> | <a href="#case-in_game_save_reload-525bb499fea34afcd6dd">[ ] unverified</a> | <a href="#case-in_game_save_reload-fdcd119df80336e619db">[ ] unverified</a> | <a href="#case-in_game_save_reload-9fa2e9b3facba8f7ab81">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-008e1fa1293dc40c526d"></a>

**0° CCW: unverified** — `in_game_save_reload-008e1fa1293dc40c526d`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-525bb499fea34afcd6dd"></a>

**90° CCW: unverified** — `in_game_save_reload-525bb499fea34afcd6dd`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-fdcd119df80336e619db"></a>

**180° CCW: unverified** — `in_game_save_reload-fdcd119df80336e619db`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9fa2e9b3facba8f7ab81"></a>

**270° CCW: unverified** — `in_game_save_reload-9fa2e9b3facba8f7ab81`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-949c77b1c49afbb7e663">[ ] unverified</a> | <a href="#case-in_game_journey-dc1592d52b82b8af8efe">[ ] unverified</a> | <a href="#case-in_game_journey-b80ca5f7053129997ecd">[ ] unverified</a> | <a href="#case-in_game_journey-316928539ca8211d64d6">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-a7b880ef8c2915c3b549">[ ] unverified</a> | <a href="#case-in_game_journey-456066c1b080e24a9398">[ ] unverified</a> | <a href="#case-in_game_journey-d616e88c81d40d36605d">[ ] unverified</a> | <a href="#case-in_game_journey-06c561813d09d817fe74">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-246314e4e4171ed8a186">[ ] unverified</a> | <a href="#case-in_game_journey-9e4530b00d5ad28568f7">[ ] unverified</a> | <a href="#case-in_game_journey-9ed1a3f5dd1595c19b45">[ ] unverified</a> | <a href="#case-in_game_journey-2f5500e020abd9932310">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-949c77b1c49afbb7e663"></a>

**0° CCW: unverified** — `in_game_journey-949c77b1c49afbb7e663`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-dc1592d52b82b8af8efe"></a>

**90° CCW: unverified** — `in_game_journey-dc1592d52b82b8af8efe`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-b80ca5f7053129997ecd"></a>

**180° CCW: unverified** — `in_game_journey-b80ca5f7053129997ecd`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-316928539ca8211d64d6"></a>

**270° CCW: unverified** — `in_game_journey-316928539ca8211d64d6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-a7b880ef8c2915c3b549"></a>

**0° CCW: unverified** — `in_game_journey-a7b880ef8c2915c3b549`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-456066c1b080e24a9398"></a>

**90° CCW: unverified** — `in_game_journey-456066c1b080e24a9398`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-d616e88c81d40d36605d"></a>

**180° CCW: unverified** — `in_game_journey-d616e88c81d40d36605d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-06c561813d09d817fe74"></a>

**270° CCW: unverified** — `in_game_journey-06c561813d09d817fe74`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-246314e4e4171ed8a186"></a>

**0° CCW: unverified** — `in_game_journey-246314e4e4171ed8a186`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-9e4530b00d5ad28568f7"></a>

**90° CCW: unverified** — `in_game_journey-9e4530b00d5ad28568f7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-9ed1a3f5dd1595c19b45"></a>

**180° CCW: unverified** — `in_game_journey-9ed1a3f5dd1595c19b45`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-2f5500e020abd9932310"></a>

**270° CCW: unverified** — `in_game_journey-2f5500e020abd9932310`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10fa00f9dc74edcdd0f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb75ebc3b3614f30ecf2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a552fe0fd390c2718b7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95a85b8d0169aa1fdd74">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b751de3d488f0ad42cde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0566d771fd2231eebc50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dbde880e7c8b8c95f69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3542039edc0b669f02c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d16d8d2b1f1d3c2d922c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dbc97a4afefc9ae30ef3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23c44074f5bd9a66c75d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70aaf82849b766a2a021">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10fa00f9dc74edcdd0f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10fa00f9dc74edcdd0f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb75ebc3b3614f30ecf2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eb75ebc3b3614f30ecf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a552fe0fd390c2718b7a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a552fe0fd390c2718b7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95a85b8d0169aa1fdd74"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95a85b8d0169aa1fdd74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b751de3d488f0ad42cde"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b751de3d488f0ad42cde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0566d771fd2231eebc50"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0566d771fd2231eebc50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dbde880e7c8b8c95f69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6dbde880e7c8b8c95f69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3542039edc0b669f02c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c3542039edc0b669f02c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d16d8d2b1f1d3c2d922c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d16d8d2b1f1d3c2d922c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dbc97a4afefc9ae30ef3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dbc97a4afefc9ae30ef3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23c44074f5bd9a66c75d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-23c44074f5bd9a66c75d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70aaf82849b766a2a021"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-70aaf82849b766a2a021`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
