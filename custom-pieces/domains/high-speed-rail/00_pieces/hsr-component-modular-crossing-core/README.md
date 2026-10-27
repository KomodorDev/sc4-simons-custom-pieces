# HSR Modular One-Tile Two-Level Crossing

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

One city tile with north/south HSR at 30.5 m above east/west HSR at 15.5 m, four native paired connections and one lower support.

Exact reusable identifier: `hsr-component-modular-crossing-core`.

Footprint: **1 × 1 tiles**. Exact menu name: **HSR Modular One-Tile Two-Level Crossing**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR Modular One-Tile Two-Level Crossing](previews/preview.png)

![HSR Modular One-Tile Two-Level Crossing — top view](previews/preview-top.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/16 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTOR OVERVIEW -->

## Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 0 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

### Boundary A: `cell-0-0-south`

This service group is required at this edge.

#### Service group 1 / 1: HSR — Level 4 (30.5 m)

| Field | Value |
| --- | --- |
| End / component | `upper-end-a` / `upper-mainline` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[0,0]` / South |
| Section origin [E,N] (m) | `[0,-8]` |
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
| `upper-end-a-track-01` / `Sin` | `upper-channel-01` / `upper-end-a-cut-01` / monorail | Incoming | `[2,-8,30.5]` | +2 | 180° | 0 |
| `upper-end-a-track-02` / `Sout` | `upper-channel-02` / `upper-end-a-cut-02` / monorail | Outgoing | `[-2,-8,30.5]` | -2 | 180° | 0 |

### Boundary B: `cell-0-0-north`

This service group is required at this edge.

#### Service group 1 / 1: HSR — Level 4 (30.5 m)

| Field | Value |
| --- | --- |
| End / component | `upper-end-b` / `upper-mainline` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[0,0]` / North |
| Section origin [E,N] (m) | `[0,8]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 4 (30.5 m) |
| Outward heading | 0° (North) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-l4-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `upper-end-b-track-01` / `Nin` | `upper-channel-02` / `upper-end-b-cut-01` / monorail | Incoming | `[-2,8,30.5]` | +2 | 0° | 0 |
| `upper-end-b-track-02` / `Nout` | `upper-channel-01` / `upper-end-b-cut-02` / monorail | Outgoing | `[2,8,30.5]` | -2 | 0° | 0 |

### Boundary C: `cell-0-0-west`

This service group is required at this edge.

#### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `lower-end-a` / `lower-mainline` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[0,0]` / West |
| Section origin [E,N] (m) | `[-8,0]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 270° (West) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-l2-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `lower-end-a-track-01` / `Win` | `lower-channel-01` / `lower-end-a-cut-01` / monorail | Incoming | `[-8,-2,15.5]` | +2 | 270° | 0 |
| `lower-end-a-track-02` / `Wout` | `lower-channel-02` / `lower-end-a-cut-02` / monorail | Outgoing | `[-8,2,15.5]` | -2 | 270° | 0 |

### Boundary D: `cell-0-0-east`

This service group is required at this edge.

#### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `lower-end-b` / `lower-mainline` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[0,0]` / East |
| Section origin [E,N] (m) | `[8,0]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 90° (East) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-l2-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `lower-end-b-track-01` / `Ein` | `lower-channel-02` / `lower-end-b-cut-01` / monorail | Incoming | `[8,2,15.5]` | +2 | 90° | 0 |
| `lower-end-b-track-02` / `Eout` | `lower-channel-01` / `lower-end-b-cut-02` / monorail | Outgoing | `[8,-2,15.5]` | -2 | 90° | 0 |

Rendering checks source metadata, current compiled resource identities, and model structure. It does not re-extract PATHs or evaluate placement; physical seams, construction clearance, collisions, and game operation remain unverified.

<!-- END CONNECTOR OVERVIEW -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Purpose: describe intrinsic directional interfaces and permitted service journeys.

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Win` | hsr / 7 / primary | in | [-8.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Wout` | hsr / 7 / primary | out | [-8.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Sout` | hsr / 7 / primary | out | [-2.0, -8.0, 30.5]; [0.0, -1.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 30.5]; [0.0, -1.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |
| `Sin` | hsr / 7 / primary | in | [2.0, -8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-9b897a8bacb659f807fe` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-9b897a8bacb659f807fe` |
| `Eout` | hsr / 7 / primary | out | [8.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Ein` | hsr / 7 / primary | in | [8.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Win` → `Eout` | primary |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Ein` → `Wout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Win` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Win` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Win` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 85, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-modular-crossing-core/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-modular-crossing-core/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0ce2c7625a107ac300a9">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0ce2c7625a107ac300a9"></a>

**General: unverified** — `software_resources-0ce2c7625a107ac300a9`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0ce2c7625a107ac300a9">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0ce2c7625a107ac300a9"></a>

**General: unverified** — `software_connectivity-0ce2c7625a107ac300a9`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-60bb45d1c468daf9127a">[ ] unverified</a> | <a href="#case-in_game_render-5dd9163ea7feb4d233d9">[ ] unverified</a> | <a href="#case-in_game_render-aac75d58babe92d0df66">[ ] unverified</a> | <a href="#case-in_game_render-8c67ccb3f983d252d251">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-60bb45d1c468daf9127a"></a>

**0° CCW: unverified** — `in_game_render-60bb45d1c468daf9127a`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5dd9163ea7feb4d233d9"></a>

**90° CCW: unverified** — `in_game_render-5dd9163ea7feb4d233d9`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-aac75d58babe92d0df66"></a>

**180° CCW: unverified** — `in_game_render-aac75d58babe92d0df66`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8c67ccb3f983d252d251"></a>

**270° CCW: unverified** — `in_game_render-8c67ccb3f983d252d251`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-60bb45d1c468daf9127a">[ ] unverified</a> | <a href="#case-in_game_placement-5dd9163ea7feb4d233d9">[ ] unverified</a> | <a href="#case-in_game_placement-aac75d58babe92d0df66">[ ] unverified</a> | <a href="#case-in_game_placement-8c67ccb3f983d252d251">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-60bb45d1c468daf9127a"></a>

**0° CCW: unverified** — `in_game_placement-60bb45d1c468daf9127a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5dd9163ea7feb4d233d9"></a>

**90° CCW: unverified** — `in_game_placement-5dd9163ea7feb4d233d9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-aac75d58babe92d0df66"></a>

**180° CCW: unverified** — `in_game_placement-aac75d58babe92d0df66`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8c67ccb3f983d252d251"></a>

**270° CCW: unverified** — `in_game_placement-8c67ccb3f983d252d251`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-60bb45d1c468daf9127a">[ ] unverified</a> | <a href="#case-in_game_demolition-5dd9163ea7feb4d233d9">[ ] unverified</a> | <a href="#case-in_game_demolition-aac75d58babe92d0df66">[ ] unverified</a> | <a href="#case-in_game_demolition-8c67ccb3f983d252d251">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-60bb45d1c468daf9127a"></a>

**0° CCW: unverified** — `in_game_demolition-60bb45d1c468daf9127a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5dd9163ea7feb4d233d9"></a>

**90° CCW: unverified** — `in_game_demolition-5dd9163ea7feb4d233d9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-aac75d58babe92d0df66"></a>

**180° CCW: unverified** — `in_game_demolition-aac75d58babe92d0df66`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8c67ccb3f983d252d251"></a>

**270° CCW: unverified** — `in_game_demolition-8c67ccb3f983d252d251`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-60bb45d1c468daf9127a">[ ] unverified</a> | <a href="#case-in_game_save_reload-5dd9163ea7feb4d233d9">[ ] unverified</a> | <a href="#case-in_game_save_reload-aac75d58babe92d0df66">[ ] unverified</a> | <a href="#case-in_game_save_reload-8c67ccb3f983d252d251">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-60bb45d1c468daf9127a"></a>

**0° CCW: unverified** — `in_game_save_reload-60bb45d1c468daf9127a`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5dd9163ea7feb4d233d9"></a>

**90° CCW: unverified** — `in_game_save_reload-5dd9163ea7feb4d233d9`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-aac75d58babe92d0df66"></a>

**180° CCW: unverified** — `in_game_save_reload-aac75d58babe92d0df66`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8c67ccb3f983d252d251"></a>

**270° CCW: unverified** — `in_game_save_reload-8c67ccb3f983d252d251`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_journey-f4d9cf8f9cd43b3ed436">[ ] unverified</a> | <a href="#case-in_game_journey-5ea57b050a0a108944d2">[ ] unverified</a> | <a href="#case-in_game_journey-389d267436dcf471fba4">[ ] unverified</a> | <a href="#case-in_game_journey-9e0ac6b5dbf02c9f3695">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-c784d630dc08288b2fdf">[ ] unverified</a> | <a href="#case-in_game_journey-481ea42c7e9a990d906d">[ ] unverified</a> | <a href="#case-in_game_journey-fed4803926213bf8e9a9">[ ] unverified</a> | <a href="#case-in_game_journey-73116eb4a175a83f4b9f">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-f5ef54272d07300cac9a">[ ] unverified</a> | <a href="#case-in_game_journey-5b79e6464c43e4f6948a">[ ] unverified</a> | <a href="#case-in_game_journey-d95471d14adcbf720bc7">[ ] unverified</a> | <a href="#case-in_game_journey-cfc5120864436a36cad0">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_journey-4fe45956037912e0b05c">[ ] unverified</a> | <a href="#case-in_game_journey-6d8268095588e8c01445">[ ] unverified</a> | <a href="#case-in_game_journey-3296eead8f9757864acb">[ ] unverified</a> | <a href="#case-in_game_journey-ad335f8c4d250bee4c7d">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_journey-f4d9cf8f9cd43b3ed436"></a>

**0° CCW: unverified** — `in_game_journey-f4d9cf8f9cd43b3ed436`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-5ea57b050a0a108944d2"></a>

**90° CCW: unverified** — `in_game_journey-5ea57b050a0a108944d2`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-389d267436dcf471fba4"></a>

**180° CCW: unverified** — `in_game_journey-389d267436dcf471fba4`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-9e0ac6b5dbf02c9f3695"></a>

**270° CCW: unverified** — `in_game_journey-9e0ac6b5dbf02c9f3695`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-c784d630dc08288b2fdf"></a>

**0° CCW: unverified** — `in_game_journey-c784d630dc08288b2fdf`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-481ea42c7e9a990d906d"></a>

**90° CCW: unverified** — `in_game_journey-481ea42c7e9a990d906d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-fed4803926213bf8e9a9"></a>

**180° CCW: unverified** — `in_game_journey-fed4803926213bf8e9a9`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-73116eb4a175a83f4b9f"></a>

**270° CCW: unverified** — `in_game_journey-73116eb4a175a83f4b9f`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-f5ef54272d07300cac9a"></a>

**0° CCW: unverified** — `in_game_journey-f5ef54272d07300cac9a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-5b79e6464c43e4f6948a"></a>

**90° CCW: unverified** — `in_game_journey-5b79e6464c43e4f6948a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-d95471d14adcbf720bc7"></a>

**180° CCW: unverified** — `in_game_journey-d95471d14adcbf720bc7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-cfc5120864436a36cad0"></a>

**270° CCW: unverified** — `in_game_journey-cfc5120864436a36cad0`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_journey-4fe45956037912e0b05c"></a>

**0° CCW: unverified** — `in_game_journey-4fe45956037912e0b05c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-6d8268095588e8c01445"></a>

**90° CCW: unverified** — `in_game_journey-6d8268095588e8c01445`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-3296eead8f9757864acb"></a>

**180° CCW: unverified** — `in_game_journey-3296eead8f9757864acb`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-ad335f8c4d250bee4c7d"></a>

**270° CCW: unverified** — `in_game_journey-ad335f8c4d250bee4c7d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a21b5e58377bc7e9477c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0ea1e21f7e35e149c7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-257e260a5e0e3b46a9e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fce588ed8dcd146cf3a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4bd98de4f164984e9fc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04bd9840b8539a8f8669">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b83c83d81ecdbec41c03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da2dbf17021ee893ab1e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-898e76225b3e7c1300bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7e9e410a4f607066a8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4d436a9d0258fac92d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7efe47c4aaa7818decc3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d5e030b5e7d39415eb3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cba7df633e5c115d8642">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa78c871f4b77f24f7c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48157237cfd256c6c89c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a95f8121f4d8cc51c61f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41eab0006cd4606d5a6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63f875e919b33922cf5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dea39cc8508b7e50759c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c46dbac8020aa6f92ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4392e3b07173e215988d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c40d120ea97eb620863e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f25975adc643b7822604">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6bfa6d9a37f3aca18752">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8107929d9878d5a0959b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86114342dcaea8ef890a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d4512ef952b7702bd6a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab64d46ede8871adbd9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-571462c9653682c72a53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6c9ee6a90c983908971">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88224e287710de4e97f4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cf09a5bd45e2e7752d29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a10f3750f8b93a66835e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c98dfe0574ea9fcec70f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43f984a6b23af0f0537f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2eb11d5412e3c60c6e77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b5dbaad2c39a779f15d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d2182f2123024b2c4e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68688ab62c7015e5d104">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bd1568734121623c4fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3b58e424ac234cab0a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-851548d1526b194b0c9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-772ed9de71e4631fbc0d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e4a8eca7572428aaafc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49ba649326bcc2ae7336">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-089f52e1911ce6fbb622">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d0fc335efa31bfb639c">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a21b5e58377bc7e9477c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a21b5e58377bc7e9477c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0ea1e21f7e35e149c7e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0ea1e21f7e35e149c7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-257e260a5e0e3b46a9e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-257e260a5e0e3b46a9e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fce588ed8dcd146cf3a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3fce588ed8dcd146cf3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4bd98de4f164984e9fc4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4bd98de4f164984e9fc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04bd9840b8539a8f8669"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04bd9840b8539a8f8669`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b83c83d81ecdbec41c03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b83c83d81ecdbec41c03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da2dbf17021ee893ab1e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-da2dbf17021ee893ab1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-898e76225b3e7c1300bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-898e76225b3e7c1300bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7e9e410a4f607066a8b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7e9e410a4f607066a8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4d436a9d0258fac92d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b4d436a9d0258fac92d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7efe47c4aaa7818decc3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7efe47c4aaa7818decc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d5e030b5e7d39415eb3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d5e030b5e7d39415eb3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cba7df633e5c115d8642"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cba7df633e5c115d8642`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa78c871f4b77f24f7c4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aa78c871f4b77f24f7c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48157237cfd256c6c89c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-48157237cfd256c6c89c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a95f8121f4d8cc51c61f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a95f8121f4d8cc51c61f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41eab0006cd4606d5a6c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-41eab0006cd4606d5a6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63f875e919b33922cf5e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63f875e919b33922cf5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dea39cc8508b7e50759c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dea39cc8508b7e50759c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c46dbac8020aa6f92ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c46dbac8020aa6f92ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4392e3b07173e215988d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4392e3b07173e215988d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c40d120ea97eb620863e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c40d120ea97eb620863e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f25975adc643b7822604"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f25975adc643b7822604`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6bfa6d9a37f3aca18752"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6bfa6d9a37f3aca18752`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8107929d9878d5a0959b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8107929d9878d5a0959b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86114342dcaea8ef890a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-86114342dcaea8ef890a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d4512ef952b7702bd6a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d4512ef952b7702bd6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab64d46ede8871adbd9a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab64d46ede8871adbd9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-571462c9653682c72a53"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-571462c9653682c72a53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6c9ee6a90c983908971"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c6c9ee6a90c983908971`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88224e287710de4e97f4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-88224e287710de4e97f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cf09a5bd45e2e7752d29"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cf09a5bd45e2e7752d29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a10f3750f8b93a66835e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a10f3750f8b93a66835e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c98dfe0574ea9fcec70f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c98dfe0574ea9fcec70f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43f984a6b23af0f0537f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43f984a6b23af0f0537f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2eb11d5412e3c60c6e77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2eb11d5412e3c60c6e77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b5dbaad2c39a779f15d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b5dbaad2c39a779f15d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d2182f2123024b2c4e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8d2182f2123024b2c4e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68688ab62c7015e5d104"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68688ab62c7015e5d104`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bd1568734121623c4fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bd1568734121623c4fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3b58e424ac234cab0a0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a3b58e424ac234cab0a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-851548d1526b194b0c9a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-851548d1526b194b0c9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-772ed9de71e4631fbc0d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-772ed9de71e4631fbc0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e4a8eca7572428aaafc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e4a8eca7572428aaafc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49ba649326bcc2ae7336"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-49ba649326bcc2ae7336`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-089f52e1911ce6fbb622"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-089f52e1911ce6fbb622`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d0fc335efa31bfb639c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d0fc335efa31bfb639c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-modular-crossing-core:canonical-southeast | <a href="#case-preview_review-d05a525f61d0bcb557b7">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-modular-crossing-core:canonical-top | <a href="#case-preview_review-f5e92b1e244c8ca1bd7e">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-modular-crossing-core:connection-overview | <a href="#case-preview_review-11ea34ddb70834f03b05">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-modular-crossing-core:canonical-southeast</summary>

<a id="case-preview_review-d05a525f61d0bcb557b7"></a>

**General: unverified** — `preview_review-d05a525f61d0bcb557b7`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-modular-crossing-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-modular-crossing-core:canonical-top</summary>

<a id="case-preview_review-f5e92b1e244c8ca1bd7e"></a>

**General: unverified** — `preview_review-f5e92b1e244c8ca1bd7e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-modular-crossing-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-modular-crossing-core:connection-overview</summary>

<a id="case-preview_review-11ea34ddb70834f03b05"></a>

**General: unverified** — `preview_review-11ea34ddb70834f03b05`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:hsr-component-modular-crossing-core:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

Both paired levels meet in one occupied cell: upper north/south paths are at 30.5 m, and lower east/west paths are at 15.5 m. The encoded graph has four grade-separated track crossings with no turning transfer. Use matching separately placed standard straight approaches when assembling a larger crossing. Encoded no-transfer checks do not establish actual in-game level isolation.

Use the [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
