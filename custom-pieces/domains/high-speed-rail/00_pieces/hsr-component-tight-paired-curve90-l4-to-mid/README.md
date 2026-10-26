# HSR Tight Two-Track Corner 30.5 to 23 Metres

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

A 56 m right-angle paired corner descends from 30.5 m to the custom 23 m matching connection. The reverse-direction track climbs; both ends have 8 m flat native collars.

Exact reusable identifier: `hsr-component-tight-paired-curve90-l4-to-mid`.

Footprint: **4 × 4 tiles**. Exact menu name: **HSR Tight Two-Track Corner 30.5 to 23 Metres**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR Tight Two-Track Corner 30.5 to 23 Metres](preview.png)

![HSR Tight Two-Track Corner 30.5 to 23 Metres — top view](preview-top.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/8 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTOR OVERVIEW -->

## Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 3 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

### Boundary A: `cell-0-3-south`

This service group is required at this edge.

#### Service group 1 / 1: HSR — Level 4 (30.5 m)

| Field | Value |
| --- | --- |
| End / component | `curve-end-a` / `graded-corner` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[0,3]` / South |
| Section origin [E,N] (m) | `[0,-56]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 4 (30.5 m) |
| Outward heading | 180° (South) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-l4-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `curve-end-a-track-01` / `Sin` | `curve-channel-01` / `curve-end-a-cut-01` / monorail | Incoming | `[2,-56,30.5]` | +2 | 180° | 0 |
| `curve-end-a-track-02` / `Sout` | `curve-channel-02` / `curve-end-a-cut-02` / monorail | Outgoing | `[-2,-56,30.5]` | -2 | 180° | 0 |

### Boundary B: `cell-3-0-east`

This service group is required at this edge.

#### Service group 1 / 1: HSR — Custom (23 m)

| Field | Value |
| --- | --- |
| End / component | `curve-end-b` / `graded-corner` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[3,0]` / East |
| Section origin [E,N] (m) | `[56,0]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Custom (23 m); no nominal level |
| Outward heading | 90° (East) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-h23000mm-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `curve-end-b-track-01` / `Ein` | `curve-channel-02` / `curve-end-b-cut-01` / monorail | Incoming | `[56,2,23]` | +2 | 90° | 0 |
| `curve-end-b-track-02` / `Eout` | `curve-channel-01` / `curve-end-b-cut-02` / monorail | Outgoing | `[56,-2,23]` | -2 | 90° | 0 |

Rendering checks source metadata, current compiled resource identities, and model structure. It does not re-extract PATHs or evaluate placement; physical seams, construction clearance, collisions, and game operation remain unverified.

<!-- END CONNECTOR OVERVIEW -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Purpose: describe intrinsic directional interfaces and permitted service journeys.

Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | hsr / 7 / primary | out | [-2.0, -56.0, 30.5]; [0.0, -1.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |
| `Sin` | hsr / 7 / primary | in | [2.0, -56.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-9b897a8bacb659f807fe` |
| `Eout` | hsr / 7 / primary | out | [56.0, -2.0, 23.0]; [1.0, 0.0]; 0.0 | `path-interface-f17a87c40e2280c52126` |
| `Ein` | hsr / 7 / primary | in | [56.0, 2.0, 23.0]; [-1.0, 0.0]; 0.0 | `path-interface-c22acb858d4777168a58` |

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

Current totals: unverified: 37, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-tight-paired-curve90-l4-to-mid/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-8852858b47c067896097">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-8852858b47c067896097"></a>

**General: unverified** — `software_resources-8852858b47c067896097`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-8852858b47c067896097">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-8852858b47c067896097"></a>

**General: unverified** — `software_connectivity-8852858b47c067896097`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-21e3a5277cb911952a2a">[ ] unverified</a> | <a href="#case-in_game_render-e7388d687daf2a1a145f">[ ] unverified</a> | <a href="#case-in_game_render-95c932d62338881500c0">[ ] unverified</a> | <a href="#case-in_game_render-a842fd04ee6f1631d0ef">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-21e3a5277cb911952a2a"></a>

**0° CCW: unverified** — `in_game_render-21e3a5277cb911952a2a`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-e7388d687daf2a1a145f"></a>

**90° CCW: unverified** — `in_game_render-e7388d687daf2a1a145f`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-95c932d62338881500c0"></a>

**180° CCW: unverified** — `in_game_render-95c932d62338881500c0`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a842fd04ee6f1631d0ef"></a>

**270° CCW: unverified** — `in_game_render-a842fd04ee6f1631d0ef`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-21e3a5277cb911952a2a">[ ] unverified</a> | <a href="#case-in_game_placement-e7388d687daf2a1a145f">[ ] unverified</a> | <a href="#case-in_game_placement-95c932d62338881500c0">[ ] unverified</a> | <a href="#case-in_game_placement-a842fd04ee6f1631d0ef">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-21e3a5277cb911952a2a"></a>

**0° CCW: unverified** — `in_game_placement-21e3a5277cb911952a2a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-e7388d687daf2a1a145f"></a>

**90° CCW: unverified** — `in_game_placement-e7388d687daf2a1a145f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-95c932d62338881500c0"></a>

**180° CCW: unverified** — `in_game_placement-95c932d62338881500c0`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a842fd04ee6f1631d0ef"></a>

**270° CCW: unverified** — `in_game_placement-a842fd04ee6f1631d0ef`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-21e3a5277cb911952a2a">[ ] unverified</a> | <a href="#case-in_game_demolition-e7388d687daf2a1a145f">[ ] unverified</a> | <a href="#case-in_game_demolition-95c932d62338881500c0">[ ] unverified</a> | <a href="#case-in_game_demolition-a842fd04ee6f1631d0ef">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-21e3a5277cb911952a2a"></a>

**0° CCW: unverified** — `in_game_demolition-21e3a5277cb911952a2a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-e7388d687daf2a1a145f"></a>

**90° CCW: unverified** — `in_game_demolition-e7388d687daf2a1a145f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-95c932d62338881500c0"></a>

**180° CCW: unverified** — `in_game_demolition-95c932d62338881500c0`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a842fd04ee6f1631d0ef"></a>

**270° CCW: unverified** — `in_game_demolition-a842fd04ee6f1631d0ef`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-21e3a5277cb911952a2a">[ ] unverified</a> | <a href="#case-in_game_save_reload-e7388d687daf2a1a145f">[ ] unverified</a> | <a href="#case-in_game_save_reload-95c932d62338881500c0">[ ] unverified</a> | <a href="#case-in_game_save_reload-a842fd04ee6f1631d0ef">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-21e3a5277cb911952a2a"></a>

**0° CCW: unverified** — `in_game_save_reload-21e3a5277cb911952a2a`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-e7388d687daf2a1a145f"></a>

**90° CCW: unverified** — `in_game_save_reload-e7388d687daf2a1a145f`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-95c932d62338881500c0"></a>

**180° CCW: unverified** — `in_game_save_reload-95c932d62338881500c0`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a842fd04ee6f1631d0ef"></a>

**270° CCW: unverified** — `in_game_save_reload-a842fd04ee6f1631d0ef`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_journey-e67c358a04d6ec6a9f0e">[ ] unverified</a> | <a href="#case-in_game_journey-7aba2689b102bb8937dd">[ ] unverified</a> | <a href="#case-in_game_journey-565812d7c331e3d48f87">[ ] unverified</a> | <a href="#case-in_game_journey-ccdc1381c7498fd69456">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout | — | <a href="#case-in_game_journey-944353620d4cec304f86">[ ] unverified</a> | <a href="#case-in_game_journey-3f919a87941df09b0bc0">[ ] unverified</a> | <a href="#case-in_game_journey-911dca45dc47a95371ab">[ ] unverified</a> | <a href="#case-in_game_journey-835b7904f22f708ce10f">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_journey-e67c358a04d6ec6a9f0e"></a>

**0° CCW: unverified** — `in_game_journey-e67c358a04d6ec6a9f0e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-7aba2689b102bb8937dd"></a>

**90° CCW: unverified** — `in_game_journey-7aba2689b102bb8937dd`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-565812d7c331e3d48f87"></a>

**180° CCW: unverified** — `in_game_journey-565812d7c331e3d48f87`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-ccdc1381c7498fd69456"></a>

**270° CCW: unverified** — `in_game_journey-ccdc1381c7498fd69456`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout</summary>

<a id="case-in_game_journey-944353620d4cec304f86"></a>

**0° CCW: unverified** — `in_game_journey-944353620d4cec304f86`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-3f919a87941df09b0bc0"></a>

**90° CCW: unverified** — `in_game_journey-3f919a87941df09b0bc0`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-911dca45dc47a95371ab"></a>

**180° CCW: unverified** — `in_game_journey-911dca45dc47a95371ab`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-835b7904f22f708ce10f"></a>

**270° CCW: unverified** — `in_game_journey-835b7904f22f708ce10f`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-91d5709c0b682d7c68be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2b630167400fa4ec271">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbbe5125797d9e852588">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cccf53434469ebeb75b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4f042adfeaa17c52e23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ea79fd8c4f99a7d5b4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c3e22e14f261cde15cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71d957e4c75bbaec054d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-91d5709c0b682d7c68be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-91d5709c0b682d7c68be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2b630167400fa4ec271"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f2b630167400fa4ec271`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbbe5125797d9e852588"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cbbe5125797d9e852588`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cccf53434469ebeb75b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8cccf53434469ebeb75b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4f042adfeaa17c52e23"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4f042adfeaa17c52e23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ea79fd8c4f99a7d5b4a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6ea79fd8c4f99a7d5b4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c3e22e14f261cde15cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2c3e22e14f261cde15cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71d957e4c75bbaec054d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71d957e4c75bbaec054d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-tight-paired-curve90-l4-to-mid:canonical-southeast | <a href="#case-preview_review-a9790b691fbde7664203">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-tight-paired-curve90-l4-to-mid:canonical-top | <a href="#case-preview_review-b469758fbb87449dcd1e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-tight-paired-curve90-l4-to-mid:connection-overview | <a href="#case-preview_review-fa6f03435675f4f2d88d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-tight-paired-curve90-l4-to-mid:canonical-southeast</summary>

<a id="case-preview_review-a9790b691fbde7664203"></a>

**General: unverified** — `preview_review-a9790b691fbde7664203`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-tight-paired-curve90-l4-to-mid:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-tight-paired-curve90-l4-to-mid:canonical-top</summary>

<a id="case-preview_review-b469758fbb87449dcd1e"></a>

**General: unverified** — `preview_review-b469758fbb87449dcd1e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-tight-paired-curve90-l4-to-mid:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-tight-paired-curve90-l4-to-mid:connection-overview</summary>

<a id="case-preview_review-fa6f03435675f4f2d88d"></a>

**General: unverified** — `preview_review-fa6f03435675f4f2d88d`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-tight-paired-curve90-l4-to-mid:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

This tight paired graded corner occupies ten cells in a 4 × 4 rectangle, including three structural cells and six literal support centres. Its cardinal displacement is 56 m, its deck width is 15 m, its track offsets are ±2 m, and its flat collars are 8 m. The intermediate paired joint is Custom (23 m), with no nominal level; it does not accept ordinary HSR or a different-width authored narrow L3 interface merely because the path heights agree.

The tight-corner polynomial applies only to those two current recipes. Their independently reviewed minimum radius is 24 m. Their actual maximum grade is approximately 0.1238, inside the unchanged 0.156251 limit. Curvature, grade-change, and 5 × 5 m train-clearance checks remain mandatory. Other curve recipes retain their separate radius limits.

Use the [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
